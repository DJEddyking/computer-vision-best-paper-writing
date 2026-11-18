# Manage the paper database

The CLI uses only Python standard-library modules. Run it from the repository root.

```bash
python3 scripts/manage_papers.py validate
python3 scripts/manage_papers.py search --venue CVPR --year 2024
python3 scripts/manage_papers.py search --task "3D" --json
python3 scripts/manage_papers.py search --reviewed-only --json
python3 scripts/manage_papers.py search --include-held-out  # audit only
```

Add a user paper with a JSON record (e.g. `/tmp/paper.json`):

```json
{
  "title": "Example User Paper",
  "venue": "CVPR",
  "year": 2025,
  "paper_url": "https://example.org/example-paper",
  "cv_task": "Video segmentation",
  "paper_type": "Method improvement",
  "writing_focus": "experimental analysis"
}
```

```bash
python3 scripts/manage_papers.py add --file /tmp/paper.json
```

The CLI creates a stable user ID, stores the record in `database/user_papers.jsonl`, and marks the recognition as `unverified_user`. It blocks exact duplicate IDs, normalized title+year+venue combinations, and duplicate DOIs.

Update a **user record only** by creating a patch file with fields to change:

```json
{"cv_task": "Video object segmentation", "writing_focus": "controlled ablations"}
```

```bash
python3 scripts/manage_papers.py update user-2025-example-user-paper --file /tmp/patch.json
```

Curated entries require a reviewed GitHub PR. User entries cannot claim official verification using the CLI. Changes made locally are **not synced to GitHub until you commit and push them**.

When retrieving prose exemplars for writing, only use annotations with `annotation_status=reviewed`; do not mine the `held_out` split. `search --reviewed-only` will return no records until the first paper is genuinely annotated and reviewed.

This script **does not** download PDFs, scrape websites, verify award claims, or automatically generate paper annotations.
