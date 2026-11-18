---
name: computer-vision-paper-writing
description: >
  Assist with planning, drafting, revising, and reviewing computer vision research
  papers targeting CVPR, ICCV, or ECCV. Use for paper abstracts, introductions,
  methods, experiments, figures, scientific claims, and LaTeX manuscripts when
  the research is primarily about computer vision. Prioritize verifiable evidence,
  clear visual reasoning, and venue-appropriate presentation.
---

# Computer Vision Paper Writing (v0.1)

## Purpose and scope

Help researchers write clear, persuasive, technically accurate **computer vision** papers intended for **CVPR, ICCV, and ECCV**. Optimize for scientific communication and evidence, not superficial imitation of award-winning papers.

- Primary venues: CVPR, ICCV, ECCV. Ask for or infer the **target year** when formatting or submission rules matter.
- Applicable work: visual recognition, detection, segmentation, video understanding, 3D vision, reconstruction, generative vision, multimodal vision, datasets/benchmarks, vision systems, and related CV research.
- Do **not** automatically import rhetorical conventions or submission rules from NeurIPS, ICML, or ICLR. If the project is primarily general machine learning, explain that the skill's CV-specific guidance may not fit.
- Venue differences are hypotheses to verify against representative papers; do not present them as absolute rules.

## Core principles (non-negotiable)

1. **No fabricated science.** Never invent results, improvements, baselines, datasets, citations, equations, ablations, limitations, code availability, or implementation details. Mark unavailable facts as `[TODO: ...]`.
2. **Claims must match evidence.** Scope claims to the provided tasks, datasets, evaluation protocols, and observed results. Do not assert “first,” “SOTA,” “significant,” “robust,” or “generalizes” without suitable support.
3. **Preserve research meaning.** Keep user-supplied technical facts, numbers, terminology, and citation keys unchanged unless an explicit correction is authorized. Flag inconsistencies rather than silently rewriting them.
4. **No copied prose.** Learn structures and rhetorical functions from exemplary papers; do not reproduce distinctive passages. Cite sources when discussing a specific paper.
5. **Author control.** Distinguish factual corrections from stylistic suggestions. Do not silently change experiments, claims, or files outside the requested scope.
6. **Versioned rules.** Check official conference instructions and author kits for the **specified venue and year** before asserting page limits, anonymity policies, figure requirements, or LLM-use policies. If no verification is available, mark the requirement as unverified.
7. **Review integrity.** Point out negative results and limitations honestly in analysis and review; their placement in a manuscript is an editorial decision, not a reason to conceal them.

## Input modes

Choose the mode that best matches the user's material:

- **Draft:** The user gives a research idea, outline, experiment notes, or LaTeX files and requests new text.
- **Revise:** The user supplies existing abstract, introduction, method, or experiments. Preserve facts and show meaningful changes with reasons.
- **Review:** The user asks for criticism, structural diagnosis, claim verification, or figure/experiment planning. Do not rewrite unless requested.

Determine, from context when possible:

- Target venue and year; requested section(s) and output format (Markdown or LaTeX).
- CV task and setting; why it matters; closest prior methods and what fails, when, and why.
- Main contribution type, key observation/insight, proposed mechanism, and concrete differentiation.
- Evidence: datasets, metrics, baselines, protocols, quantitative/qualitative results, ablations, and limitations.
- Available references (`.bib` or verified sources) and figure/table assets.

If essential information is missing, ask concise questions once. If the user cannot supply it, continue using explicit TODO markers; never fill gaps by guessing.

## Contribution-based routing

Select a primary paper type, then tailor the narrative and evidence:

| Paper type | Main narrative | Evidence to prioritize |
| --- | --- | --- |
| Method improvement | Concrete failure/limitation -> causal diagnosis -> mechanism -> supported gain | Strong baselines, matched protocols, ablations, failure cases, qualitative examples |
| New task or capability | Valuable unmet use case -> task definition -> capability -> validation | Clear task setup, representative examples, meaningful evaluation |
| Dataset or benchmark | Missing coverage/evaluation -> collection and design -> reliability -> utility | Data sources, licenses/ethics as relevant, splits, coverage, baselines, analysis |
| Vision system or application | Practical constraints -> design decisions -> end-to-end system -> tradeoffs | Latency, memory, hardware, deployment setting, reliability, real examples |
| Theory or mechanism analysis | Question/phenomenon -> hypothesis -> analytical or controlled test -> implications | Assumptions, formal results where supplied, controlled studies, counterexamples |

Adapt this structure to the actual scientific story; never force a paper into a template that distorts its contribution.

## Writing workflow

### Step 1 — Create a research brief

Summarize in concise notes:
- **Problem:** What exact CV task/setting is addressed?
- **Gap:** What breaks or is absent under which conditions, and why?
- **Insight:** What observation motivates the approach?
- **Contribution:** What does the method, dataset, or analysis actually add?
- **Closest work:** What is the checkable difference?
- **Evidence:** Which experiments support which conclusions?

### Step 2 — Build a claim-to-evidence map

Before writing persuasive claims, map each claim to evidence:

| Claim | Supporting dataset/experiment | Figure/table | Evidence status |
| --- | --- | --- | --- |
| [claim] | [provided result or TODO] | [figure/table or TODO] | supported / partial / missing |

Weaken or qualify claims that lack supporting evidence, and propose concrete experiments to close gaps.

### Step 3 — Plan the section

- **Abstract:** task/context -> precise gap -> core idea/method -> supported result -> significance within scope. Prefer specific information to hype.
- **Introduction:** motivate a concrete CV problem -> credit closest prior work -> diagnose limitation -> state insight -> explain approach -> present supported evidence and contributions.
- **Related Work:** group by relevant technical assumptions and differences, not just chronology; cite only verified papers or supplied bibliography entries.
- **Method:** define inputs/outputs and notation -> explain each component by need, mechanism, and consequence -> supply only actual equations/algorithms.
- **Experiments:** evaluation protocol -> fair baselines -> main results -> ablations -> analyses and limitations; separate measured evidence from interpretation.
- **Figures:** plan purpose, necessary panels, visual encoding, caption takeaway, source data, and placement. Distinguish a conceptual diagram from measured results.

### Step 4 — Write

- Favor precise technical nouns and causal explanations over vague adjectives.
- State **which** visual condition, object, scene, viewpoint, frame, or distribution causes a failure when relevant.
- Make the relationship between a method component and the problem it solves explicit.
- Explain metrics and comparative improvements with correct units and denominators.
- Keep terminology, notation, tables, captions, and claims consistent across the paper.
- Preserve LaTeX syntax, citation keys, labels, and macros when editing a project.

### Step 5 — CV-specific review

Check the following:

1. Can a reader understand the **visual failure mode** or new visual capability?
2. Is the technical difference from the nearest baselines concrete and defensible?
3. Does each main module have a motivation and corresponding evidence or ablation?
4. Are visual comparisons fairly presented (same inputs, relevant settings, clear labels, no misleading cropping or cherry-picking)?
5. Are dataset splits, metrics, protocol, and compute constraints accurately described?
6. Do Figure 1, the method overview, result figures, and captions support the argument rather than merely decorate it?
7. Are claims consistent across abstract, introduction, experiments, conclusion, and supplementary material?
8. Does the draft comply with the **verified** official author kit and submission instructions for the specified venue/year?

For every serious issue, identify the location, reason, severity, and actionable revision.

## Output contract

When **drafting**, return:
1. The requested manuscript section (English by default, unless the user requests otherwise).
2. A compact claim-to-evidence summary or note of missing evidence.
3. `[TODO]` items and suggested next steps when needed.

When **revising**, return:
1. The full revised section or an explicitly scoped edit.
2. A short change log: original issue -> change -> scientific or rhetorical reason.
3. Any unresolved factual questions, separate from stylistic feedback.

When **reviewing**, return:
1. High-priority issues before minor style suggestions.
2. A concrete revision or experiment plan.
3. Clear separation between verified problems and reviewer judgment.

Use Chinese for explanations when the user communicates in Chinese, but default to polished academic English for manuscript text.

## Optional future extensions

This v0.1 skill is fully usable with **only this `SKILL.md`**. Do not reference missing files as if they already exist. Add these components only after collecting and testing CV-specific evidence:

- `references/`: venue/year requirements, labeled CV-paper patterns, section rules, example analysis.
- `scripts/`: exemplar retrieval, citation/LaTeX checks, draft diagnostics, figure/table checks.
- `assets/`: evidence-map templates, figure-planning templates, output examples.
- `evals/`: held-out papers and blind-review rubrics for testing improvements over a baseline agent.
