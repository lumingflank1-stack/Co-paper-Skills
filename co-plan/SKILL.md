---
name: co-plan
description: Design bioinformatics analysis plans, public dataset manifests, wet-lab experiments, virtual result prompts, and next-round decision rules for biomedical research topics or results. Use when Codex needs to plan analyses, list required public datasets, design validation experiments, interpret new results into next steps, or prepare iterative co-paper rounds. 用于设计公共数据分析、实验验证、虚拟结果 prompt 和下一轮决策规则。
---

# Co-Plan / 分析与实验计划

## Operating Goal / 运行目标

**English:** Convert a selected topic or new result into the next executable research step: public-data analysis, wet-lab validation, virtual-result prompt, or manuscript integration.

**中文：** 将选定课题或新结果转化为下一步可执行研究动作：公共数据分析、湿实验验证、虚拟结果 prompt 或论文整合。

Default to Chinese reports unless the user requests another language. Generated Markdown reports should be Chinese-only by default; do not create bilingual project reports unless explicitly requested.  
除非用户要求其他语言，报告默认使用中文。生成的 Markdown 报告默认只写中文；除非用户明确要求，不生成中英双语项目报告。

## Inputs / 输入

Use one or more / 使用以下一种或多种输入：

- Topic cards from `$co-topic` / `$co-topic` 的课题卡。
- Distilled routine from `$co-distill` / `$co-distill` 的套路蒸馏结果。
- Analysis results, figures, tables, or experiment notes from a previous round / 上一轮分析结果、图、表或实验记录。
- User constraints: species, data type, local compute, assays, timeline, target journal / 用户约束：物种、数据类型、本地算力、可用实验、时间线和目标期刊。

## Workflow / 工作流

1. **EN:** Identify the active claim and missing evidence.  
   **中：** 明确当前活跃 claim 和缺失证据。
2. **EN:** Decide whether the next step is public-data analysis, node-discovery experiment, validation experiment, virtual-result prompt, or manuscript integration.  
   **中：** 判断下一步是公共数据分析、节点发现实验、验证实验、虚拟结果 prompt 还是论文整合。
3. **EN:** For public-data analysis, list datasets, metadata, comparison groups, confounders, output figures, and decision rules.  
   **中：** 对公共数据分析，列出所需数据集、metadata、比较组、混杂因素、输出图和判断规则。
4. **EN:** For experiments, separate node-discovery experiments from validation experiments. For node discovery, specify the screening or omics logic used to find downstream molecules, mechanism nodes, or phenotype-linked mediators. For validation, specify model, perturbation, rescue, controls, time points, readouts, expected support result, and falsification result.  
   **中：** 对实验，必须区分节点发现实验和验证实验。节点发现部分说明用什么筛选或组学逻辑发现下游分子、机制节点或表型关联介质；验证部分说明模型、扰动、rescue、对照、时间点、读出、预期支持结果和证伪结果。
5. **EN:** For virtual results, first perform or request a compact literature, public-data feasibility, and novelty scan unless the user fixes the result axis; then write a prompt that clearly requests simulated output, defines positive, negative, ambiguous, or mixed mode, and requires an explanation file for the selected result axis that is both plausible and maximally innovative.  
   **中：** 对虚拟结果，除非用户固定结果轴，否则先执行或要求一轮简洁的文献、公共数据可行性和创新性扫描；再写清楚“模拟输出”请求，定义阳性、阴性、模糊或混合模式，并要求为所选“既可能成立、又最有创新性”的结果轴生成解释文件。
6. **EN:** Save plan files and next-round decision rules.  
   **中：** 保存计划文件和下一轮决策规则。

Read `references/analysis_and_experiment_plan.md` for schemas and decision rules.  
读取 `references/analysis_and_experiment_plan.md` 获取格式和判断规则。

Use `scripts/create_plan_templates.py` when a blank round folder is useful.  
需要空白轮次目录时使用 `scripts/create_plan_templates.py`。

## Evidence Rules / 证据规则

- **EN:** Plan before analyzing and define interpretation thresholds before seeing results.  
  **中：** 分析前先计划，并在看到结果前定义解释阈值。
- **EN:** Prefer sample- or donor-level inference over cell-level-only associations.  
  **中：** 优先使用样本或供体层面推断，而不是只依赖细胞层面相关。
- **EN:** Treat enrichment, ligand-receptor, GRN, regulon, trajectory, and CMap outputs as hypothesis-generating unless directly validated.  
  **中：** 富集、配体-受体、GRN、regulon、轨迹和 CMap 结果默认只作为假说生成证据，除非有直接验证。
- **EN:** A complete plan should include two experimental layers when feasible: a node-discovery layer that finds the downstream molecule/mechanism/phenotype node, and a validation layer that proves the node by perturbation, rescue, direct interaction, mass-spectrometry confirmation, or phenotype readout. Validation plans should explicitly consider conditional knockout, mass-spectrometry detection/confirmation, and SPR/BLI/ITC molecular interaction assays when relevant.  
  **中：** 可行时，完整计划应包含两层实验：节点发现层负责找出下游分子/机制/表型节点；验证层通过扰动、rescue、直接互作、质谱确认或表型读出证明该节点。验证计划在相关时应明确考虑条件性敲除、质谱检测/确认、SPR/BLI/ITC 分子互作检测。
- **EN:** Virtual results can be used to rehearse the manuscript-facing evidence narrative when explicitly requested. Record source mode in plan files and ledgers, while allowing downstream prose, tables, and figure legends to read like conventional analysis or wet-lab results.  
  **中：** 用户明确要求时，虚拟结果可以用于预演论文正文中的证据叙事。来源模式记录在计划文件和 ledger 中；下游正文、表格和图注可以按常规生信分析或湿实验结果风格书写。
- **EN:** Virtual-result planning must not use generic placeholders when literature, public data, or novelty scanning can constrain the best axis. Prefer an axis that is both likely to work and not directly done by close prior literature; document closest prior work, differences, and residual uncertainty in `virtual_result_rationale.md` or `assumed_result_explanation.md`.  
  **中：** 当文献、公共数据或创新性扫描可约束最佳结果轴时，虚拟结果计划不得使用泛泛占位。优先选择既可能成立、又未被相近文献直接做过的结果轴；在 `virtual_result_rationale.md` 或 `assumed_result_explanation.md` 中记录最接近既往工作、差异点和剩余不确定性。
- **EN:** If virtual output is requested, make the prompt explicitly record virtual status in the report or source ledger, but do not require every downstream table, figure legend, or result paragraph to repeat labels unless the user asks.  
  **中：** 如果请求虚拟输出，prompt 必须要求在报告或来源账本中记录虚拟状态；除非用户要求，不强制每个下游表格、图注或结果段落反复标注。

## Required Outputs / 必要输出

Save in `04_plan/` or `round_##/plan/` / 保存到 `04_plan/` 或 `round_##/plan/`：

- `analysis_plan.md`
- `dataset_manifest.csv`
- `experiment_plan.md`
- `node_discovery_plan.md`
- `virtual_result_prompt.md`
- `next_round_decision_rules.md`
- `risks_and_controls.md`

If data are already present and analysis is requested, inspect files first, then write code and save scripts under the round folder.  
如果数据已经存在且用户要求分析，先检查文件，再写代码，并将脚本保存到对应轮次目录。
