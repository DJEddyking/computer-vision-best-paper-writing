#!/usr/bin/env python3
"""Small, stdlib-only CLI for a traceable CV paper database.

Examples:
  python scripts/manage_papers.py validate
  python scripts/manage_papers.py search --venue ECCV --year 2024
  python scripts/manage_papers.py add --file /path/to/paper.json
  python scripts/manage_papers.py update user-paper-id --file /path/to/patch.json

It does not scrape papers or verify awards over the network.
"""
import argparse
import hashlib
import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "database"
CURATED = ROOT / "curated_papers.jsonl"
USER = ROOT / "user_papers.jsonl"
SPLITS = {"annotation", "held_out", "backlog", "user"}
STATUSES = {"not_started", "in_progress", "reviewed"}


def read_jsonl(path):
    records = []
    if not path.exists():
        return records
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            record = json.loads(line)
        except json.JSONDecodeError as e:
            raise ValueError(f"{path}:{line_no}: {e}") from e
        if not isinstance(record, dict):
            raise ValueError(f"{path}:{line_no}: expected a JSON object")
        records.append(record)
    return records


def write_jsonl(path, records):
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(
        "".join(json.dumps(r, ensure_ascii=False, sort_keys=False) + "\n" for r in records),
        encoding="utf-8",
    )
    tmp.replace(path)


def normalize_title(title):
    return re.sub(r"[^\w]+", "", title.casefold(), flags=re.UNICODE)


def key_for(record):
    return (normalize_title(record["title"]), str(record["venue"]).upper(), int(record["year"]))


def safe_url(value, field):
    if value is not None and (not isinstance(value, str) or not value.startswith(("https://", "http://"))):
        raise ValueError(f"{field} must be an http(s) URL or null")


def validate_records(curated, users):
    seen_ids, seen_titles, seen_dois = set(), set(), set()
    for source, records in (("curated", curated), ("user", users)):
        for r in records:
            for field in ("paper_id", "title", "venue", "year"):
                if field not in r or r[field] in ("", None):
                    raise ValueError(f"{source} record missing required field: {field}")
            if not isinstance(r["year"], int) or not (1950 <= r["year"] <= 2100):
                raise ValueError(f"{r['paper_id']}: invalid year")
            if not isinstance(r["paper_id"], str):
                raise ValueError("paper_id must be a string")
            if r["paper_id"] in seen_ids:
                raise ValueError(f"duplicate paper_id: {r['paper_id']}")
            seen_ids.add(r["paper_id"])
            title_key = key_for(r)
            if title_key in seen_titles:
                raise ValueError(f"duplicate title/venue/year: {r['title']}")
            seen_titles.add(title_key)
            doi = str(r.get("doi") or "").lower().replace("https://doi.org/", "").strip()
            if doi:
                if doi in seen_dois:
                    raise ValueError(f"duplicate DOI: {doi}")
                seen_dois.add(doi)
            for f in ("paper_url", "recognition_source_url"):
                safe_url(r.get(f), f)
            if r.get("corpus_split") not in SPLITS:
                raise ValueError(f"{r['paper_id']}: invalid corpus_split")
            if r.get("annotation_status") not in STATUSES:
                raise ValueError(f"{r['paper_id']}: invalid annotation_status")
            if not isinstance(r.get("annotations"), list):
                raise ValueError(f"{r['paper_id']}: annotations must be a list")
            if source == "user" and (r["corpus_split"] != "user" or r.get("recognition_verification") == "official_verified"):
                raise ValueError(f"{r['paper_id']}: user entry cannot claim curated or official-verified status")


def load():
    curated, users = read_jsonl(CURATED), read_jsonl(USER)
    validate_records(curated, users)
    return curated, users


def read_object(path):
    obj = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(obj, dict):
        raise ValueError("input JSON must be an object")
    return obj


def generated_id(r):
    slug = re.sub(r"[^a-z0-9]+", "-", r["title"].lower()).strip("-")[:50].strip("-")
    if not slug:
        slug = hashlib.sha256(r["title"].encode("utf-8")).hexdigest()[:12]
    return "user-" + str(r["year"]) + "-" + slug


def add_paper(args):
    curated, users = load()
    entry = read_object(args.file)
    for field in ("title", "venue", "year"):
        if not entry.get(field):
            raise ValueError(f"new user paper must include {field}")
    if isinstance(entry["year"], bool):
        raise ValueError("year must be an integer")
    entry["year"] = int(entry["year"])
    entry["paper_id"] = entry.get("paper_id") or generated_id(entry)
    entry["corpus_split"] = "user"
    entry["recognition_verification"] = "unverified_user"
    entry["annotation_status"] = entry.get("annotation_status", "not_started")
    entry["annotations"] = entry.get("annotations", [])
    entry["annotation_version"] = entry.get("annotation_version", 0)
    entry["paper_link_status"] = entry.get("paper_link_status", "not_checked")
    entry["recognition"] = entry.get("recognition")
    entry["recognition_source_url"] = entry.get("recognition_source_url")
    entry["paper_url"] = entry.get("paper_url")
    entry["doi"] = entry.get("doi")
    users.append(entry)
    validate_records(curated, users)
    write_jsonl(USER, users)
    print(f"added {entry['paper_id']}")


def update_paper(args):
    curated, users = load()
    patch = read_object(args.file)
    forbidden = {"paper_id", "corpus_split", "recognition_verification"}
    if forbidden.intersection(patch):
        raise ValueError("cannot patch identity, split, or verification status")
    for index, entry in enumerate(users):
        if entry["paper_id"] == args.paper_id:
            updated = dict(entry)
            updated.update(patch)
            updated["recognition_verification"] = "unverified_user"
            users[index] = updated
            validate_records(curated, users)
            write_jsonl(USER, users)
            print(f"updated {args.paper_id}")
            return
    if any(r["paper_id"] == args.paper_id for r in curated):
        raise ValueError("curated records must be reviewed and changed via a Git pull request")
    raise ValueError(f"user paper not found: {args.paper_id}")


def search(args):
    curated, users = load()
    records = curated + users
    if not args.include_held_out:
        records = [r for r in records if r["corpus_split"] != "held_out"]
    if args.venue:
        records = [r for r in records if r["venue"].lower() == args.venue.lower()]
    if args.year:
        records = [r for r in records if r["year"] == args.year]
    if args.task:
        records = [r for r in records if args.task.casefold() in str(r.get("cv_task", "")).casefold()]
    if args.query:
        records = [r for r in records if args.query.casefold() in (" ".join(str(r.get(f, "")) for f in ("title", "writing_focus", "selection_reason"))).casefold()]
    if args.reviewed_only:
        records = [r for r in records if r["annotation_status"] == "reviewed"]
    for r in records:
        if args.json:
            print(json.dumps(r, ensure_ascii=False))
        else:
            print(f"{r['paper_id']} | {r['venue']} {r['year']} | {r['corpus_split']} | {r['title']}")
    print(f"{len(records)} matches", file=sys.stderr)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("validate")
    adding = commands.add_parser("add")
    adding.add_argument("--file", required=True, help="JSON paper record")
    updating = commands.add_parser("update")
    updating.add_argument("paper_id")
    updating.add_argument("--file", required=True, help="JSON object of modified fields")
    querying = commands.add_parser("search")
    querying.add_argument("--venue")
    querying.add_argument("--year", type=int)
    querying.add_argument("--task")
    querying.add_argument("--query")
    querying.add_argument("--reviewed-only", action="store_true", help="only use checked exemplar annotations")
    querying.add_argument("--include-held-out", action="store_true", help="audit only; do not train on these papers")
    querying.add_argument("--json", action="store_true", help="JSONL output")
    args = parser.parse_args()
    try:
        if args.command == "validate":
            curated, users = load()
            print(f"valid: curated={len(curated)}, user={len(users)}")
            print("splits:", dict(Counter(r["corpus_split"] for r in curated + users)))
        elif args.command == "add":
            add_paper(args)
        elif args.command == "update":
            update_paper(args)
        else:
            search(args)
    except (ValueError, OSError, TypeError) as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(2)


if __name__ == "__main__":
    main()
