# First annotation and evaluation plan

The corpus has 26 candidate papers. **No full-paper rhetorical annotations have been completed yet.** This document records a split that avoids evaluation leakage.

## Annotation queue: six papers, one per meeting

| Paper ID | Primary training objective |
| --- | --- |
| `cvpr2024-mip-splatting` | Concrete visual failure -> technical cause -> anti-aliasing mechanism |
| `cvpr2025-vggt` | Unifying multiple geometry tasks in one method narrative |
| `eccv2024-minimalist-vision` | From a surprising imaging principle to demonstrated applications |
| `eccv2026-heat-kernel-textures` | Representation limitations -> intrinsic geometry-aware alternative |
| `iccv2023-segment-anything` | Capability -> model -> data engine -> evaluation |
| `iccv2025-flowedit` | Removing a costly operation from a generative workflow |

For each: read the paper, annotate Abstract **sentence roles**, Introduction **paragraph roles**, the Method's **need -> mechanism -> property**, Experiment **claim -> evidence**, Figure 1 and figure/caption role. Store section/page evidence, clear source URLs, and original (nonverbatim) analysis; have a human review annotations before using them as normative style guidance.

## Strict held-out evaluation: six papers (never in style/exemplar training)

| Paper ID | Evaluation focus |
| --- | --- |
| `cvpr2024-generative-image-dynamics` | New capability / visual storytelling |
| `cvpr2025-molmo-pixmo` | Data and vision-language model resource |
| `eccv2024-sea-raft` | Efficiency + accuracy technical explanation |
| `eccv2026-poppy` | Imaging modality and physical evidence |
| `iccv2023-tracking-everything` | Temporal video problem framing |
| `iccv2025-brick-structures` | Generation under physical constraints |

## Backlog

14 remaining candidates are neither training exemplars nor test fixtures until deliberately assigned. The plan may be revised, but **do not use held-out content to derive rules or choose hyperparameters**; revise the split only with clear disclosure and evaluation reset.

## Evaluation procedure

1. Prepare an author-side brief containing only information a researcher could legitimately provide.
2. Compare an unmodified baseline agent and this Skill using **identical** brief and model conditions.
3. Score claim fidelity, specificity of gap, mechanism clarity, correctness of comparisons, CV-relevant experimental reasoning, figure planning, and provenance.
4. Run blind human assessment and record errors; do not reward copying source paper sentences.
