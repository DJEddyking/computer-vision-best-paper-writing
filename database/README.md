# Curated CV paper corpus (seed v0.1)

This database contains **26 shortlisted main-conference papers** across CVPR 2024/2025, ECCV 2024/2026, and ICCV 2023/2025. The shortlist prioritizes best-paper awards, honorable mentions, and ECCV 2024 award-candidate orals; it is *not* an exhaustive listing of all orals/highlights.

## Corpus coverage

| Conference | Year | Candidates |
|---|---:|---:|
| CVPR | 2024 | 6 |
| CVPR | 2025 | 5 |
| ECCV | 2024 | 5 |
| ECCV | 2026 | 3 |
| ICCV | 2023 | 3 |
| ICCV | 2025 | 4 |
| **Total** | | **26** |

## What is and is not verified

- **Award labels and titles** were checked against the official CVPR award announcements, ECCV 2024 Awards, ICCV TCPAMI awards, and ECCV 2026 accepted-paper award badges. ECCV 2026 LSRM honorable mention is checked against an author's page; its record is marked `author_confirmed`.
- **Paper links** tagged `official_award_pdf_link` or `official_oral_page` are directly linked by official pages. Links tagged `unverified_cvf_html` are plausible CVF Open Access paths **not independently fetch-verified** (the Open Access site returned access restrictions in this check). Author project pages are marked `author_project_page`, not confused with official proceedings.
- Award identity and display format are separate: papers with a best-paper award may also be displayed in poster sessions. `presentation: null` means the format was not independently verified.
- `annotation_status: not_started` is deliberate. The Mip-Splatting author PDF has now been read for a first, source-located annotation draft, but it is **not yet human-reviewed**; the other 25 candidate papers have not undergone full-text annotation. Selection rationale and `writing_focus` are *proposed study angles*, not empirically learned style rules.

## Files

- `curated_papers.jsonl` — 26 curated seed records; protected from edits by the user-library utility.
- `user_papers.jsonl` — an initially empty file for user-added records.
- `SCHEMA.md` — database schema, verification semantics, deduplication rules.
- `ANNOTATION_PLAN.md` — six papers to annotate first, six strict hold-outs, remaining backlog.
- `../scripts/manage_papers.py` — add, update, search and validate without network access.
- `annotations/cvpr2024-mip-splatting.jsonl` — 29 draft rhetorical annotations with PDF source locations (excluded from reviewed exemplar retrieval).

## Provenance sources

- CVPR 2024: https://cvpr.thecvf.com/Conferences/2024/News/Awards
- CVPR 2025: https://cvpr.thecvf.com/Conferences/2025/BestPapersDemos
- ECCV 2024: https://eccv.ecva.net/Conferences/2024/Awards
- ECCV 2026: https://eccv.ecva.net/Conferences/2026/AcceptedPapers
- ICCV 2023/2025: https://tc.computer.org/tcpami/awards/iccv-paper-awards/
- ECCV 2026 LSRM author confirmation: https://sites.google.com/view/zhengqinli

## Curation policy

Only **verified** facts can be asserted in user-facing generated writing. A paper's award is evidence of its selection for study, not evidence that particular wording causes award success. Style advice must eventually cite **your own annotation** plus the paper/section location. Scientific claims require independent primary references. Do not redistribute full PDFs or copy exemplar paragraphs into generated papers.
