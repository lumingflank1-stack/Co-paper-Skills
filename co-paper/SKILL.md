---
name: co-paper
description: Orchestrate a stateful modular biomedical paper workflow through co-search, user module selection, co-debate Top 5 hypothesis ranking, user hypothesis selection, co-plan, co-result, and final manuscript assembly. Use when Codex must build one research module at a time while preserving evidence provenance, discovery and validation layers, explicit human checkpoints, branching, and completion review. 用于按模块递进构建生物医学论文：co-search 分类创新模块，用户选模块，co-debate 生成并排序 Top 5 假说，用户再选一个假说，co-plan 规划，co-result 关闭模块，最后组装全文并由 co-completer 审核。
---

# Co-Paper / 模块化论文工作流总控

## Operating Goal / 运行目标

Build a biomedical paper as a graph of independently testable modules rather than one monolithic design. Advance one module at a time, preserve source provenance, and stop at required user decisions unless automatic continuation is explicitly authorized.

把论文构建为一组可独立检验、可上下游或并列连接的研究模块，而不是一次性设计整篇文章。每轮只推进一个模块，保存证据来源，并在必要的人类决策点暂停。

Default user-facing reports and manuscript files to Chinese unless another language is requested.

## Core Workflow / 核心流程

```text
co-search
-> user chooses one innovation module
-> co-debate generates and ranks Top 5 hypotheses
-> user chooses one hypothesis
-> co-plan
-> co-result
-> user chooses upstream/downstream/parallel module or ends project
```

If continuing, repeat the full loop from `$co-search`, including `$co-debate`. If ending:

```text
final co-result integration
-> co-method
-> co-discussion
-> manuscript/full_manuscript.md
-> co-completer
```

## Module Evidence Contract / 模块证据契约

Every module must distinguish:

1. **Node-discovery layer:** omics, public data, screening, single-cell/spatial analysis, proteomics, metabolomics, or another broad method finds the relevant phenotype, molecule, mechanism node, or readout.
2. **Validation layer:** perturb the upstream/input side and observe the downstream/output side. If a mediator is claimed, include rescue or mark rescue as missing.

Do not close a module as complete when only discovery evidence exists. Record the validation layer as real, partial, assumed, virtual-approved, requirements-only, or missing.

## Skill Routing / 技能路由

1. Use `$co-search` to retrieve literature and classify innovation points into:
   - `new_phenotype`
   - `new_mechanism`
   - `new_molecule_type`
   - `new_experimental_method`
   - `new_bioinformatics_analysis`
2. Stop and ask the user to choose one innovation module.
3. Use `$co-debate` on that selected module. Generate exactly five genuinely competing hypotheses, critique them, rank them highest to lowest, and save a selection menu.
4. Stop and ask the user to choose one hypothesis or request reranking/revision.
5. Use `$co-plan` only after hypothesis selection. Pass the selected module, selected hypothesis, falsification criteria, alternatives, and evidence gaps.
6. Use `$co-result` when real, partial, assumed, explicitly approved virtual, or requirements-only evidence is available. Close only the current module.
7. After closure, ask whether to start an upstream, downstream, parallel, or standalone module, or end the project.
8. Assemble the manuscript only after the user ends the project.

## Prohibited Mainline Steps / 主线禁用步骤

- Do not skip `$co-debate` after module selection.
- Do not call `$co-plan` before the user selects one ranked hypothesis.
- Do not classify whole papers as reusable complete routines.
- Do not generate positive virtual Results without explicit user permission.
- Do not force neutral or contradictory evidence into a positive narrative.

## Human Checkpoints / 人类决策点

Stop unless automatic continuation was explicitly requested:

1. After `$co-search`: select one innovation module.
2. After `$co-debate`: select one of the ranked Top 5 hypotheses, rerank, revise, or return to search.
3. After `$co-plan`: approve analysis/experiment route or revise the plan.
4. Before `$co-result`: confirm discovery and validation source modes.
5. Before virtual positive results: confirm direction and permitted virtual layers.
6. After each `$co-result`: choose the next module relation or end the project.
7. Before final assembly: confirm source ledgers and rationale files.
8. After `$co-completer`: choose `complete_project`, `dynamic_branch`, or `new_module_loop`.

## State and Provenance / 状态与来源

Read `references/project_contract.md` before scaffolding or final assembly. Read `references/co_paper_workflow_explanation.md` when explaining or changing the workflow. Read `references/final_review_and_dynamic_resume.md` before completion or resume.

Minimum state files:

- `project_state.md`
- `decision_log.md`
- `module_ledger.csv`
- `hypothesis_ledger.csv`
- `evidence_ledger.csv`
- `source_mode_ledger.csv`

Use `scripts/scaffold_project.py` for a new project.

## Public Data Policy / 公共数据策略

Default large or permissioned data to user-managed download. `$co-plan` must save a ranked download list with accession, required files, metadata, analysis role, minimum success condition, and access limitations. Do not automatically download large SRA/dbGaP, Synapse, institutional, Git-LFS, or unstable files unless explicitly requested.

## Manuscript Assembly / 全文组装

Only after the user ends the project:

1. Final `$co-result` integrates closed modules and figure logic.
2. `$co-method` writes Methods from stable Results.
3. `$co-discussion` writes Introduction, Discussion, and numbered references.
4. Assemble one `manuscript/full_manuscript.md` in Chinese by default.
5. `$co-completer` reviews readiness and offers completion, dynamic branch, or a new module loop.

Any new module loop restarts:

```text
co-search -> user module choice -> co-debate -> user hypothesis choice -> co-plan -> co-result
```

## Required Outputs / 必要输出

Use default folders:

- `01_search/`
- `02_modules/`
- `module_##/debate/`
- `module_##/plan/`
- `module_##/figures/`
- `module_##/tables/`
- `manuscript/`
- `branches/`

Every final response must list saved paths and the current next decision.
