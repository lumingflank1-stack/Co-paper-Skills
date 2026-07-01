---
name: co-result
description: Draft Chinese biomedical or life-science manuscript Results sections from user-provided experiment designs, actual results, partial results, or explicitly requested simulated positive results. Use when Codex needs to write or package Results, figure legends, panel-indexed claims, raw-data requirements, figure prompts or images, or prompt-directed virtual result packages while recording in Markdown reports whether each result is real, assumed, or simulated. 用于撰写结果、图注、原始数据需求、图片提示和按要求生成的虚拟结果包。
---

# Co-Result / 结果部分撰写

## Operating Goal / 运行目标

**English:** Turn experiment designs, actual findings, partial findings, or explicitly requested simulated findings into a compact manuscript Results package: Results prose, panel-indexed figure references, figure prompts or images, legends, raw-data requirements, and optional virtual Excel tables.

**中文：** 将实验设计、真实结果、部分结果或用户明确要求的虚拟结果转化为紧凑的论文 Results 包：结果正文、图版索引、图片提示或图片、图注、原始数据需求和可选虚拟 Excel 表。

Default to Chinese biomedical manuscript style unless the user requests another language. All generated Markdown reports, Results drafts, figure legends, source notes, and manuscript inputs should be Chinese-only by default; do not create bilingual Chinese-English project reports unless explicitly requested.  
除非用户要求其他语言，默认使用中文生物医学论文风格。所有生成的 Markdown 报告、Results 草稿、图注、来源说明和全文输入默认只写中文；除非用户明确要求，不生成中英双语项目报告。

## Result Source Modes / 结果来源模式

Choose mode before drafting / 撰写前先判断模式：

1. `input_results`: **EN:** user provides actual or partial results; draft only from those inputs.  
   **中：** 用户提供真实或部分结果；只基于这些输入撰写。
2. `assumed_results`: **EN:** user says the result should be treated as true, such as "假设结果成立"; label it as assumed.  
   **中：** 用户说明“假设结果成立”等；按假设结果处理，并在报告中记录。
3. `virtual_positive_results`: **EN:** user explicitly asks for virtual, simulated, mock, or positive expected results; generate only according to the prompt.  
   **中：** 用户明确要求虚拟、模拟、mock 或阳性预期结果；只按 prompt 生成。
4. `requirements_only`: **EN:** user asks what data are needed or the prompt is ambiguous; do not generate results.  
   **中：** 用户只问需要什么数据，或 prompt 不明确；不生成结果，只输出需求。

If virtual/simulated results are not explicitly requested, do not invent positive results.  
如果没有明确要求虚拟/模拟结果，不要自行编造阳性结果。

## Core Workflow / 工作流

1. **EN:** Parse biological question, assays, groups, endpoints, expected direction, and source mode.  
   **中：** 解析生物学问题、实验、分组、终点、预期方向和来源模式。
2. **EN:** Build a logic map linking each conclusion to figure panel, assay, comparison, evidence, and source mode.  
   **中：** 建立结果逻辑图，将每个结论连接到图版、实验、比较、证据和来源模式。
3. **EN:** Write Results with panel indexing such as `(Figure 1A)` and `(Figure 1A-D)`.  
   **中：** 用 `(Figure 1A)`、`(Figure 1A-D)` 等方式在正文中索引图版。
4. **EN:** Write figure legends after Results and distinguish schematic, representative image, quantification, and statistical panels.  
   **中：** Results 后写图注，并区分示意图、代表图、定量图和统计图。
5. **EN:** For full Results packages, virtual-result packages, assumed-result manuscript packages, or `$co-paper` manuscript assembly, identify every independent manuscript figure from Results text and legends (`Figure 1`, `Figure 2`, etc.), then call the available image generation path (`imagegen` / GPT Image 2 when available) to create one complete multi-panel bitmap per independent figure. Save each selected bitmap in the project workspace, update the manuscript Markdown with image links, and write a figure asset manifest. Do not satisfy a full manuscript package with only one combined montage when multiple independent figures are present. If image generation is unavailable, blocked, or the user asks for text only, save `figure_generation_prompts.md` plus `figure_generation_blockers.md` and state the blocker.  
   **中：** 对完整 Results 包、虚拟结果包、假设结果全文包或 `$co-paper` 全文组装，先从 Results 正文和图注识别所有独立论文图（`Figure 1`、`Figure 2` 等），再默认调用可用图片生成路径（可用时使用 `imagegen` / GPT Image 2）为每个独立 Figure 生成一张完整 multi-panel 位图。每张选定图片都要保存到项目目录，更新全文 Markdown 的图片链接，并写出 figure asset manifest。多个独立 Figure 存在时，不能只用一张总拼图替代完整全文图组。如果图片生成不可用、受阻，或用户要求只输出文字，则保存 `figure_generation_prompts.md` 和 `figure_generation_blockers.md` 并说明原因。
6. **EN:** Identify raw-data requirements for every claim and panel.  
   **中：** 为每个 claim 和 panel 标出原始数据需求。
7. **EN:** Generate virtual data only in `virtual_positive_results` mode or when the user explicitly asks for a virtual workbook. Record simulation status only in Markdown report and `result_source_ledger.md`; do not mark every result paragraph, table row, sheet, numeric block, or figure legend as simulated.  
   **中：** 只有在 `virtual_positive_results` 模式或用户明确要求虚拟 workbook 时才生成虚拟数据。模拟状态只记录在 Markdown 报告和 `result_source_ledger.md` 中，不在每段结果、每行表格、每个 sheet、每个数值块或每条图注里反复标记。
8. **EN:** Export Markdown and assets by default; export PDF only when requested and supported.  
   **中：** 默认导出 Markdown 和素材；只有用户要求且本地支持时才导出 PDF。

## Reference Loading / 参考文件加载

- `references/result_writing.md`: Results order and claim strength / 结果顺序和 claim 强度。
- `references/figure_generation.md`: figure prompts or image generation / 图片提示或图片生成。
- `references/raw_data_and_virtual_excel.md`: raw-data requirements and virtual Excel / 原始数据需求和虚拟 Excel。
- `references/output_contract.md`: full package structure / 完整交付结构。
- `scripts/write_virtual_workbook.py`: structured workbook export / 结构化 workbook 导出。

## Drafting Rules / 撰写规则

- **EN:** Write like Results, not a grant proposal or Discussion.  
  **中：** 写成 Results，不写成基金申请或 Discussion。
- **EN:** Start from direct evidence, then quantification, mechanism, and integrative conclusion.  
  **中：** 从直接证据开始，再到定量、机制和整合结论。
- **EN:** Avoid causal overstatement; use conservative words unless experiments prove mechanism.  
  **中：** 避免因果过度表述；除非实验直接证明机制，否则使用保守措辞。
- **EN:** Do not fabricate exact p values, n values, Kd values, fold changes, or clinical endpoints unless provided or explicitly requested for virtual values.  
  **中：** 除非用户提供或明确要求虚拟数值，不编造精确 p 值、n 值、Kd、fold change 或临床终点。

## Virtual Result Rules / 虚拟结果规则

Virtual results are allowed only when the user explicitly asks for them.  
只有用户明确要求时才允许虚拟结果。

In virtual mode / 在虚拟模式下：

- **EN:** Before generating virtual results, perform a compact literature, public-data feasibility, and novelty scan unless the user provides a fixed result axis. Choose the positive result axis that is both highly plausible and maximally innovative, with no directly equivalent prior study found in the scanned literature. Do not use a generic placeholder. Save an explanation file such as `virtual_result_rationale.md` or `assumed_result_explanation.md` that lists the closest prior work, why the selected axis is different, and what remains uncertain.  
  **中：** 生成虚拟结果前，除非用户已经指定固定结果轴，否则先做一轮简洁的文献、公共数据可行性和创新性扫描。选择既高度可能成立、又最有创新性，且在已扫描文献中未见直接同构研究的阳性结果轴；不使用泛泛占位物。保存 `virtual_result_rationale.md` 或 `assumed_result_explanation.md` 等解释文件，列出最接近的既往工作、所选结果轴的新意差异，以及仍不确定的地方。
- **EN:** Record virtual-result status once in the Markdown source note and `result_source_ledger.md`.  
  **中：** 只在 Markdown 来源说明和 `result_source_ledger.md` 中记录虚拟结果状态。
- **EN:** Follow the user's requested direction, assays, groups, variance, and output format.  
  **中：** 遵循用户指定的方向、实验、分组、变异和输出格式。
- **EN:** Preserve realistic variance and round workbook numeric values to four decimals unless specified otherwise.  
  **中：** 保留合理变异；除非用户另有要求，workbook 数值保留四位小数。
- **EN:** When the user requests virtual-result mode, write the manuscript-facing Results, legends, Methods inputs, and Discussion inputs in the same conventional style as corresponding analysis or wet-lab findings; keep the virtual source status in the Markdown report and `result_source_ledger.md`, not repeated inside every paragraph, table, or legend.  
  **中：** 当用户要求虚拟结果模式时，面向论文正文的 Results、图注、Methods 输入和 Discussion 输入可按对应生信分析或湿实验结果的常规写法呈现；虚拟来源状态只记录在 Markdown 报告和 `result_source_ledger.md` 中，不在每段正文、每个表格或每条图注里反复标注。
- **EN:** Keep prose, table cells, figure legends, and workbook data sheets clean unless the user asks for visible labels.  
  **中：** 除非用户要求显式标注，结果正文、表格单元格、图注和 workbook 数据 sheet 保持干净。

## Output Contract / 输出契约

For a full request, save / 完整任务需保存：

- `*_results_section.md`: Results, legends, image links, source notes / 结果、图注、图片链接和来源说明。
- `result_source_ledger.md`: panel-level source mode map / panel 级来源模式表。
- `virtual_result_rationale.md` or `assumed_result_explanation.md`: literature/data/novelty rationale for virtual or assumed positive results, including closest prior work and difference from directly equivalent studies / 虚拟或假设阳性结果的文献、数据和创新性解释，包括最接近既往工作及与直接同构研究的差异。
- `figures/Figure_*.png`: generated planning or manuscript figures by default when image generation is available / 图片生成可用时默认生成的规划图或论文图。
- `figure_asset_manifest.md`: one row per generated independent figure, with source prompt, saved path, manuscript link status, and inspection note / 每个独立生成 Figure 一行，记录来源 prompt、保存路径、全文链接状态和检查说明。
- `figure_generation_prompts.md`: prompts for figures / 图片生成 prompt。
- `figure_generation_blockers.md`: why bitmap figures were not generated, if generation is unavailable or blocked / 图片生成不可用或受阻时的原因说明。
- `raw_data_requirements_summary.md`: raw-data requirement map / 原始数据需求表。
- `*_virtual_raw_data.xlsx`: virtual workbook only when explicitly requested / 仅在明确要求时生成虚拟 workbook。

Final response should report saved paths and point to the Markdown source ledger.  
最终回复需报告保存路径，并指向 Markdown 来源账本。
