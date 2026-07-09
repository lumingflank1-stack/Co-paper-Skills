---
name: co-plan
description: Design executable plans for one selected biomedical research module at a time. Use after co-search when the user has chosen one innovation module, such as a new phenotype, new mechanism, new molecule type, new experimental method, or new bioinformatics analysis. Plan the module relationship, public-data analyses, node-discovery layer, validation layer, mediator rescue if needed, virtual result prompts, and next-module decision rules for the selected module only. 用于用户选择一个创新模块后，设计该模块关系、生信分析、公共数据、节点发现层、验证层、中介 rescue、虚拟结果 prompt 和下一模块决策规则。
---

# Co-Plan / 模块分析与实验计划

## Operating Goal / 运行目标

**English:** Convert one selected innovation module into the next executable research step. Do not design the whole paper at once. The plan should close the current module and define what downstream module can be considered after results are interpreted.

**中文：** 将用户选中的一个创新模块转化为下一步可执行研究动作。不要一次性设计整篇论文。计划的目标是完成当前模块，并在结果解释后给出可考虑的下游模块。

Default to Chinese reports unless the user requests another language. Generated Markdown reports should be Chinese-only by default; do not create bilingual project reports unless explicitly requested.

## Inputs / 输入

Use one or more:

- Selected innovation module from `$co-search`.
- `innovation_points.md`, `innovation_point_matrix.csv`, or `module_options.md`.
- Analysis results, figures, tables, or experiment notes from a previous module.
- User constraints: species, data type, local compute, assays, timeline, target journal.

Do not require topic cards from `$co-topic` or distilled routines from `$co-distill` in the active `$co-paper` workflow.

## Workflow / 工作流

1. Identify the selected module family and selected innovation point.
2. Define one active claim for this module.
3. Classify the module relationship as `standalone`, `parallel`, `progressive_downstream`, or `progressive_upstream`; record the parent module or parallel group when known.
4. Plan both required evidence layers unless the user explicitly marks the module exploratory-only:
   - Node-discovery layer: how to find the new molecule, mechanism node, phenotype-linked mediator, method readout, or analysis target.
   - Validation layer: how to perturb the upstream/input side and observe the downstream/output side.
5. If the active claim tests a mediator, add rescue logic or mark rescue as a missing decisive experiment.
6. For public-data analysis, list datasets, metadata, comparison groups, confounders, output figures, and decision rules. Create a ranked user-download priority list before any analysis when local files are not already available.
7. For virtual results, first perform or request a compact literature, public-data feasibility, and novelty scan unless the user fixes the result axis. Specify whether virtual results are needed for discovery, validation, rescue, or all layers.
8. Save plan files and next-module decision rules.

Read `references/analysis_and_experiment_plan.md` for schemas and decision rules.
读取 `references/analysis_and_experiment_plan.md` 获取格式和判断规则。

Use `scripts/create_plan_templates.py` when a blank module folder is useful.
需要空白模块目录时使用 `scripts/create_plan_templates.py`。

## Evidence Rules / 证据规则

- Plan before analyzing and define interpretation thresholds before seeing results.
- Default public data acquisition to user-managed download.
- Prefer sample- or donor-level inference over cell-level-only associations.
- Treat enrichment, ligand-receptor, GRN, regulon, trajectory, and CMap outputs as hypothesis-generating unless directly validated.
- A complete module plan must define support, partial support, neutral, contradictory, and not-interpretable outcomes separately for the discovery layer and validation layer.
- Do not close a mechanism module from discovery-only omics or screening evidence; require perturbation and downstream readout validation, or mark validation as missing/requirements-only.
- For mediator claims, rescue is the decisive validation tier unless the user explicitly accepts a weaker module.
- Virtual results can be used only when explicitly requested. Record source mode in plan files and ledgers.

## Required Outputs / 必要输出

Save in `02_modules/`, `module_##/plan/`, or the chosen directory:

- `module_plan.md`
- `analysis_plan.md`
- `dataset_manifest.csv`
- `experiment_plan.md`
- `node_discovery_plan.md`
- `validation_plan.md`
- `module_relationship.md`
- `virtual_result_prompt.md`
- `next_module_decision_rules.md`
- `risks_and_controls.md`

When local public data are not yet present, also save:

- `data_download_priority.md`: ranked dataset/accession list, why each dataset matters for this module, required files and metadata, suggested local folder name, analysis to run after user download, and what evidence remains impossible without that dataset.

After each completed module, update the next-module decision rules with downstream options and a refreshed priority list for not-yet-analyzed datasets.
