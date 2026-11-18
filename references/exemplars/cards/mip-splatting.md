# Mip-Splatting — CVPR 2024 writing analysis (draft)

- Paper ID: `cvpr2024-mip-splatting`
- Venue: CVPR 2024; Best Student Paper
- Original: [CVF Open Access](https://openaccess.thecvf.com/content/CVPR2024/html/Yu_Mip-Splatting_Alias-free_3D_Gaussian_Splatting_CVPR_2024_paper.html)
- Readable author-hosted paper: [Yu et al., PDF](https://www.cvlibs.net/publications/Yu2024CVPR.pdf)
- DOI: `10.1109/CVPR52733.2024.01839`
- Annotation status: **draft / pending human review**. Paragraph groups are *rhetorical* units, not verbatim quotations. PDF page numbers are **1-based**, based on the linked PDF.
- Structured dataset: [database/annotations/cvpr2024-mip-splatting.jsonl](../../../database/annotations/cvpr2024-mip-splatting.jsonl)

> This file is original Chinese commentary and compact paraphrases, not the source article's complete text. Read the source PDF for exact wording. Do not copy a paper's distinctive prose into new work.

## Abstract: one paragraph, seven sentence roles (PDF p.1)

| Unit | Content paraphrase (ZH) | Function |
|---|---|---|
| A1 | 承认 3DGS 的高画质与高效率 | Credit to prior success |
| A2 | 焦距和距离变化造成伪影 | Concrete failure setting |
| A3 | 指明 3D 频率约束缺失与 2D dilation 机制 | Two-part causal diagnosis |
| A4 | 引入由训练视图决定频率上界的 3D smoothing | Remedy for representation frequency |
| A5 | 阐明其缓解放大时高频伪影 | Component-to-outcome link |
| A6 | 用 2D Mip filter 近似像素积分代替 dilation | Second remedy for sampling |
| A7 | 用单尺度训练、多尺度测试论证有效性 | Evaluation protocol |

**Transferable move:** Prior achievement → failure under a specific perturbation → causal diagnosis → each mechanism addresses a cause → evidence setting. No fixed abstract numerical quota is implied.

## Introduction: paragraph-level structure (PDF pp.1–2)

| Unit | Content paraphrase (ZH) | Analysis |
|---|---|---|
| I1 | 从 NVS 和 NeRF 铺垫到 3DGS 的质量、速度优势 | 承认强基线并说明研究的重要性 |
| I2 | 介绍 3DGS 的投影和 dilation，诊断 zoom-out 与 zoom-in 的不同伪影 | 先讲原机制，后讲具体边界条件与失败原因 |
| I3 | 将训练视图采样率与可表示 3D 频率联系起来，导出三维平滑 | 科学观察先于方法模块，是从原因到设计的关键桥梁 |
| I4 | 解释三维平滑无法独立应对 zoom-out，提出二维 Mip 滤波并定位相关工作 | 第二模块解决第一模块的残留问题，不是平行堆砌 |
| I5 | 依次列出根因分析、两项滤波修改以及实验验证 | Contributions 与前面的问题链条保持一致 |

**Reusable skeleton:** Domain / strong baseline → concrete failure and mechanism → physical or mathematical insight → remedy 1 → residual issue → remedy 2 → verifiable contributions. Not a universal CVPR template.

## Method: prerequisite → diagnosis → design (PDF pp.3–6)

| Unit | Text content summary | Why the organization works |
|---|---|---|
| M1 (Sec. 3.1) | Nyquist–Shannon 采样条件 | 引入刚好需要的理论 |
| M2 (Sec. 3.2) | 3D Gaussian 参数、投影、混合渲染和 dilation（Eqs. 1–5） | 定义真正发生错误的算子 |
| M3–M4 (Sec. 4) | 退化表示、缩小时亮度/膨胀、放大时侵蚀/高频伪影 | 技术诊断有可视化对应 |
| M5 (Sec. 4) | 直接移除 dilation 会造成优化困难，且仍有混叠 | 排除显而易见但不足够的修复 |
| M6 (Sec. 5.1) | 从训练视角推导每个高斯的最大采样率（Eqs. 6–7; Fig. 3） | 参数由成像与几何关系约束 |
| M7 (Sec. 5.1) | 3D smoothing 的卷积定义与高斯性质（Eqs. 8–9） | Need → Mechanism → Property |
| M8–M9 (Sec. 5.2) | 2D Mip 近似单像素积分（Eq. 10），解释与 EWA 的差别 | 按剩余问题引出第二个模块，并与最接近方法区分 |

## Experiments: each protocol tests a specific claim (PDF pp.6–8)

| Unit | Content summary | Claim being tested |
|---|---|---|
| E1–E2 (Sec. 6 / 6.1) | 设置实验顺序、3DGS 基础配置、滤波参数 | 透明报告可比较的实验协议 |
| E3 (Sec. 6.2, Tab. 1) | Blender 多尺度训练、测试 | 常规多尺度精度 |
| E4 (Sec. 6.2, Tab. 2, Fig. 4) | Blender 单尺度训练、低分辨率测试 | Zoom-out 下的抗混叠与视觉保真 |
| E5 (Sec. 6.3, Tab. 3, Fig. 5) | Mip-NeRF 360 低分辨率训练、高分辨率测试 | Zoom-in 下的高频与侵蚀伪影 |
| E6 (Sec. 6.3, Tab. 4) | Mip-NeRF 360 同尺度训练、测试 | 改善分布外情景是否损害常规性能 |
| E7 (Sec. 6.4) | 盒滤波近似误差与训练额外开销 | 局限与定量结果相互呼应 |

**A numeric check from the source:** Blender single-scale training, 1/8 resolution test (Tab. 2), PSNR: 3DGS **17.69 dB**, Mip-Splatting **28.67 dB**. This is one *specific protocol*, not a general performance claim. The same-scale comparison (Tab. 4) is much closer: 3DGS+EWA **27.77 dB**, Mip-Splatting **27.79 dB**.

## Figure 1 (PDF p.1)

| Panel | Visual meaning | Rhetorical role |
|---|---|---|
| (a) | Faithful 3D representation and projection | Establishes reference behavior |
| (b) | Degenerate 3D representation that can look similar after dilation | Makes the hidden ambiguity visible |
| (c) | Zoom-out with dilation/brightening | Reveals one failure mode |
| (d) | Zoom-in with erosion/high-frequency artifacts | Reveals the opposite failure mode |

**Transferable lesson:** If a method solves a visual failure, Figure 1 can *explain the mechanism of failure*, not merely advertise the model. Couple conceptual diagrams with real, comparable visual examples.

## Evidence and limitations of this annotation

- Original paper text and figure captions were inspected through the author PDF, plus selected full-page screenshots; direct CVF PDF fetching was blocked but the official HTML landing page confirms the published paper.
- Source location and section/figure/table IDs are tracked in the structured JSONL. Comments are our own paraphrases.
- Sentence/paragraph grouping may differ from the original LaTeX line wrapping; grouped methods are not claimed to be one paragraph each.
- This is **one case**, not an empirical style frequency or a statistically justified writing rule. Keep annotation state `in_progress` until human validation; do not treat as an approved exemplar automatically.
