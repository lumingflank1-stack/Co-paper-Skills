---
name: co-plan
description: Design an executable plan for one user-selected biomedical hypothesis within one selected innovation module. Use after co-search module selection and co-debate Top 5 ranking, only when the user has chosen one hypothesis. Plan module relationship, public-data analysis, node discovery, validation, mediator rescue, virtual-result prompts, and next-module rules. 用于用户先选择创新模块、再从 co-debate Top 5 中选择一个假说后，为该单一假说设计模块关系、生信、发现层、验证层和 rescue 计划。
---

# Co-Plan / 模块分析与实验计划

## Operating Goal / 运行目标

**English:** Convert one user-selected hypothesis within one selected innovation module into the next executable research step. Do not plan directly from an unranked module and do not design the whole paper at once.

**中文：** 将用户从 `$co-debate` Top 5 中选中的一个假说转化为下一步可执行研究动作。不要从未辩论的模块直接规划，也不要一次性设计整篇论文。

Default to Chinese reports unless the user requests another language. Generated Markdown reports should be Chinese-only by default; do not create bilingual project reports unless explicitly requested.

## Inputs / 输入

Use one or more:

- Selected innovation module from `$co-search`.
- Selected hypothesis and rank from `$co-debate`.
- `co_plan_handoff.md`, including predictions, alternative explanation, falsification criteria, and evidence gaps.
- `innovation_points.md`, `innovation_point_matrix.csv`, or `module_options.md`.
- Analysis results, figures, tables, or experiment notes from a previous module.
- User constraints: species, data type, local compute, assays, timeline, target journal.

Do not require topic cards from `$co-topic` or distilled routines from `$co-distill` in the active `$co-paper` workflow.

## Workflow / 工作流

1. Confirm the selected module family, innovation point, hypothesis ID, rank, and user selection. If no hypothesis was selected, return to `$co-debate`.
2. Convert the selected hypothesis into one conservative active claim.
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
- `selected_hypothesis.md`
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
