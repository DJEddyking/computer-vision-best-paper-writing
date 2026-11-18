# Writing the Introduction for CVPR, ICCV, and ECCV

Use this guide with the research brief and claim-to-evidence map in the repository skill. A reader should be able to identify the visual problem, explain what differs from the closest work, and locate the evidence for the central claim. [Computer Vision Paper Writing skill](../SKILL.md)

## Prepare the research brief

- Define the task, inputs, outputs, and setting. Identify the visual condition that matters, such as occlusion, small objects, viewpoint changes, or sparse views, and explain its effect on the task.
- Identify the closest work by technical assumption or capability. Record what it already accomplishes, the specific gap that remains, and the citations or results that establish that gap.
- State the observation that motivated the work, the contribution it led to, and the evidence that supports it. Collect the relevant dataset, split, metric, protocol, baseline, and figure or table references.
- Preserve supplied terminology, measurements, and citation keys. Ask for essential missing facts once. Use a specific marker such as `[TODO: verify the baseline and evaluation split]` when a fact remains unavailable.

## Plan the Introduction

Treat these as functions to cover. Combine them or adjust their order to fit the contribution.

1. **Motivate the problem.** Name the task early and use a concrete visual example or application constraint to show why it is difficult or consequential. Use opening background that helps the reader understand this problem.
2. **Position the closest work and diagnose the gap.** Credit what existing approaches achieve. Name the assumption, missing capability, or failure that matters under the stated setting. Support the diagnosis with verified citations or supplied observations. Label a proposed cause as a hypothesis when the evidence establishes only the symptom.
3. **State the insight and approach.** Explain what the work changes and how that change addresses the gap. Describe the mechanism at the level needed to understand the intuition. Save implementation detail for the Method section.
4. **Preview the evidence and contributions.** Summarize the strongest result that answers the opening problem, with its evaluation scope. If a contribution list clarifies the argument, use each item to identify a distinct deliverable or finding and the evidence that supports it. Include a material qualification when it affects how the reader should interpret the result.

| Primary contribution | What to foreground | Evidence to preview |
| --- | --- | --- |
| Method improvement | A specific failure under a defined visual condition and the mechanism intended to address it | Matched baselines, an analysis of the affected cases, and ablations for mechanism claims |
| New task or capability | The unmet use case and the new inputs, outputs, or capabilities | Representative examples and a protocol that tests the capability |
| Dataset or benchmark | Missing coverage or an evaluation gap and the design choices that address it | Coverage, annotation or split quality, and baseline results that demonstrate utility |
| Vision system or application | Practical constraints and the design tradeoffs they motivate | End-to-end quality, memory or latency, and the hardware and input conditions |
| Theory or mechanism analysis | The visual phenomenon, question, and relevant assumptions | A formal result or controlled study, with boundary conditions and counterexamples where available |

## Match claims to evidence

| Claim in the Introduction | Check before using it |
| --- | --- |
| A method improves performance | Verify the comparison, dataset and split, metric, and matching conditions. Distinguish an absolute point gain from a relative percentage. |
| A component explains the improvement | Use a controlled ablation or direct analysis that isolates the component. A comparison of complete systems supports a system-level result. |
| A model is robust or generalizes | Name the specific shift, perturbation, or transfer setting that was tested. Scope the claim to that setting. |
| A system is faster or more efficient | Specify hardware, input size, and batch size where relevant. Identify whether the result measures latency, throughput, memory, or theoretical computation. |
| The contribution is first or state of the art | Verify the novelty scope against the closest literature or verify the performance claim against comparable published results. Describe the concrete difference or measured comparison when broader support is unavailable. |

For a draft, record each central claim beside its supporting citation, experiment, figure, or table and mark the evidence as supported, partial, or missing. Qualify or remove unsupported claims from manuscript prose and flag unresolved facts with specific TODOs in the handoff or draft.

## Use Figure 1 to support the argument

Choose a figure that makes a specific failure, capability, or mechanism easier to understand. Refer to the relevant panel in the Introduction and state what the reader should see. A caption should identify the inputs and outputs and say whether a panel is a conceptual illustration or an observed result.

For qualitative comparisons, use the same input and comparable settings, label methods and ground truth when available, and use consistent crops, viewpoints, or frame selections. Explain how examples were selected when it affects interpretation. Use representative cases and relevant failures, and rely on quantitative evaluation for claims about prevalence or average performance.

## Published examples across the three venues

These examples illustrate choices made for particular papers. When tailoring a submission, compare recent papers from the target venue and subfield. Check the official author instructions and template for the target year before asserting requirements about page limits, anonymity, formatting, figures, or disclosure. Mark any unverified rule as such.

- **CVPR 2022, Mask2Former.** The Introduction acknowledges progress on universal segmentation and narrows the motivation to remaining performance and training obstacles. Figure 1 makes the performance gap visible across the segmentation tasks, with instance segmentation providing a concrete example. [Cheng et al., Section 1 and Figure 1](https://arxiv.org/pdf/2112.01527)
- **ICCV 2021, Swin Transformer.** The Introduction ties variation in object scale and the cost of dense high-resolution inputs to two design choices, hierarchical feature maps and local attention. It then explains how shifting the windows allows information to cross window boundaries. [Liu et al., Section 1 and Figures 1–2](https://arxiv.org/pdf/2103.14030)
- **ECCV 2020, DETR.** The Introduction defines the detector's output as a set of boxes and labels, which motivates direct set prediction and makes the training-time matching in Figure 1 easy to place. It reports a competitive comparison on COCO and identifies weaker small-object performance. [Carion et al., Section 1 and Figure 1](https://arxiv.org/pdf/2005.12872)

## Worked example with incomplete evidence

Suppose the supplied notes describe video instance segmentation under short occlusions. A pilot shows tracks receiving new identities on reappearance, and the proposed association module retains pre-occlusion track features. The notes contain no aggregate results.

> In video instance segmentation, a track can receive a new identity when an object reappears after a short occlusion, as observed in our pilot examples. We retain features from before the occlusion and use them to associate reappearing detections with existing tracks.

| Draft claim | Evidence status and action |
| --- | --- |
| Identity switches occur in the observed reappearance cases | Supported by the stipulated pilot examples. Cite the actual examples in a manuscript and keep the claim scoped to them. |
| The new association rule differs from the closest tracker | Missing. `[TODO: identify and cite the closest tracker, then verify how it handles occlusion]` |
| Retaining features reduces identity switches | Missing. `[TODO: compare identity switches with and without feature retention on a defined occlusion subset under the same protocol]` |

## Draft, revise, and review

- **When drafting**, return the section in the requested format, a compact claim-to-evidence summary, and any specific TODOs. Default to academic English for manuscript prose and use Chinese for explanations when the user communicates in Chinese.
- **When revising**, preserve research facts, citation keys, and LaTeX labels and macros. Return the revised text, explain consequential edits, and flag unresolved factual questions.
- **When reviewing**, report the most important issues first. Give each issue a location, severity, reason, and concrete revision or evidence request. Identify where an assessment depends on editorial judgment.

Before handing off, check that the opening identifies the visual setting, the gap fairly represents the closest work, the approach addresses that gap, and every result preview or contribution can be traced to evidence. Cross-check terminology, comparisons, and qualifications against the Abstract, Experiments, figure captions, and Conclusion.
