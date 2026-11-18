# Paper corpus schema v0.1

Each line of `curated_papers.jsonl` and `user_papers.jsonl` is a standalone JSON object (UTF-8). JSONL is kept human-reviewable for Git-based PRs.

## Required fields

| Field | Type | Meaning |
| --- | --- | --- |
| `paper_id` | string | Stable identifier, unique across both libraries |
| `title` | string | Paper title |
| `venue` | string | CVPR / ECCV / ICCV (user library can be other) |
| `year` | integer | Conference year |
| `paper_url` | string or null | Public paper or author page; URL is not assumed verified |
| `paper_link_status` | string | `official_award_pdf_link`, `official_oral_page`, `author_project_page`, `unverified_cvf_html`, or `not_checked` |
| `recognition` | string or null | Official award label or unverified user claim |
| `recognition_source_url` | string or null | Page asserting the award/presentation |
| `recognition_verification` | string | `official_verified`, `author_confirmed`, or `unverified_user` |
| `corpus_split` | string | `annotation` / `held_out` / `backlog` / `user` |
| `annotation_status` | string | `not_started`, `in_progress`, `reviewed` |
| `annotations` | array | Structured evidence-backed writing annotations (empty until research) |

Other metadata includes `cv_task`, `paper_type`, `writing_focus`, `selection_reason`, `presentation`, `doi`, `metadata_checked_at`, `annotation_version`, and `notes`.

## Annotation structure (planned)

A validated annotation entry should include `section` (e.g. introduction), `rhetorical_move` (e.g. gap.cause), `analysis` (original commentary, **not copied prose**), `source_location` (paper section/page/paragraph), `source_url`, `annotator`, and `review_status`. Never infer source locations, quoted sentences, metrics, or author intent without reading the paper.

## Deduplication and updates

- Treat normalized title + year + venue as a candidate duplicate; use DOI/official IDs when available.
- Reuse `paper_id`; never create a new record for a metadata correction.
- Store user additions in `user_papers.jsonl`; do not modify curated entries via the user-management CLI.
- Use a Git commit/PR for traceable changes. Keep held-out evaluation papers excluded from exemplar retrieval and style-calibration scripts.
- Treat unknown presentation classes as `null`, not `Poster` or `Oral`.
- Do not turn unverified author/user-provided claims into official verified fields without checked evidence.

## Source-located annotation files

Annotations may be kept in an external `database/annotations/<paper_id>.jsonl` file while they are being reviewed. A curated paper can set `annotation_file` and `annotation_card` to point to this file and a human-readable commentary card. `annotation_version` tracks draft revisions. `annotation_status=in_progress` **must not** pass the `search --reviewed-only` filter.

For each source-located annotation we store:
- `annotation_id`, `paper_id`, `section`
- `source_location` (PDF page, section and sentence/paragraph/figure identifier)
- `source_url` (paper URL)
- `rhetorical_move`, `content_summary_zh`, `writing_analysis_zh`
- `review_status`: `draft` until a human validates claims, locations and interpretation.

An external draft annotation is *not* automatically a model-approved writing exemplar; keep its review lifecycle separate from the metadata record. No copied paragraph text or inaccessible PDF is committed.
