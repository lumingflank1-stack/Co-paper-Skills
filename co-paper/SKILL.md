---
name: co-paper
description: "Orchestrate a modular, progressive biomedical paper workflow. Use when Codex needs to coordinate co-search, co-plan, co-result, co-method, co-discussion, and co-completer through one research module at a time: literature search classifies innovation points into new phenotype, new mechanism, new molecule type, new experimental method, and new bioinformatics analysis; the user chooses one module; co-plan records whether it is parallel, upstream, downstream, or standalone and designs both node-discovery and validation layers; co-result closes that module only after both layers are represented or explicitly marked; the user then decides the next upstream, downstream, parallel module, or manuscript assembly. Do not use co-distill or co-topic in the main co-paper workflow. 用于按模块递进推进生物医学论文：co-search 只按五类创新点分类，用户选择一个模块后进入 co-plan，记录模块关系并设计节点发现层和验证层；co-result 在两层证据均被表示或明确标记缺失后结束模块；每轮只完成一个模块，用户决定下一上游/下游/并列模块或结束项目后再进入 co-result、co-method、co-discussion、full_manuscript.md 和 co-completer。"
---

# Co-Paper / 论文工作流总控

## Operating Goal / 运行目标

**English:** Run a stateful, interactive biomedical manuscript workflow one module at a time. Co-Paper does not design a whole biological study at once and does not copy a full article routine. It builds a paper by modular progression: search innovation points, choose one module, plan it, write its results, then let the user decide the next downstream module.

**中文：** 以“单模块递进”的方式运行生物医学论文工作流。Co-Paper 不一次性设计整篇生物学研究，也不复刻完整文章套路；它通过“检索创新点、选择一个模块、规划该模块、写出该模块结果、再由用户决定下一下游模块”的方式逐步形成论文。

Default to Chinese for user-facing reports unless the user requests another language. Stage Markdown reports and `manuscript/full_manuscript.md` should be Chinese-only by default; do not create parallel English or bilingual versions unless explicitly requested.
除非用户要求其他语言，面向用户的报告默认使用中文。阶段性 Markdown 报告和 `manuscript/full_manuscript.md` 默认只写中文；除非用户明确要求，不创建英文或中英双语版本。

## Core Principle / 核心原则

```text
co-search -> user chooses one innovation module -> co-plan -> co-result
-> user chooses next downstream module or ends project
-> if continuing: repeat co-search -> co-plan -> co-result
-> if ending: final co-result integration -> co-method -> co-discussion
-> manuscript/full_manuscript.md -> co-completer
```

**English:** Each loop completes one research module. A module may be a phenotype, mechanism, molecule type, experimental method, or bioinformatics analysis. Modules may be parallel branches or progressive upstream/downstream steps, but each complete module must keep two evidence layers: (1) a node-discovery layer that finds the new thing, usually through omics, public-data analysis, screening, or another high-throughput/broad experiment; and (2) a validation layer that perturbs the upstream/input side and observes the downstream/output side. If the claim tests a mediator, include rescue logic. The next module is decided only after both layers are interpreted or explicitly marked missing.
**中文：** 每一轮只完成一个研究模块。模块可以是新表型、新机制、新分子类型、新实验方法或新生信分析。模块之间可以是并列分支，也可以是上游/下游递进关系；但每个完整模块都必须保留两层证据：1）节点发现层，用组学、公共数据分析、筛选或其他高通量/大批量实验发现“新东西”；2）验证层，干预上游或输入端并观察下游或输出端。如果 claim 是验证中介，还要设计 rescue 逻辑。只有两层证据解释清楚，或明确标记缺失后，才决定下一模块。

## Prohibited Mainline Steps / 主线禁用步骤

- Do not call `$co-distill` in the main `$co-paper` workflow.
- Do not call `$co-topic` in the main `$co-paper` workflow.
- Do not ask `$co-search` to classify whole papers into complete article routines.
- Do not infer a complete manuscript structure from one literature category.
- Do not force upstream, downstream, mechanism, molecule, bioinformatics, and experiment modules into one initial design.

`$co-distill` and `$co-topic` may remain as legacy or standalone tools, but they are not part of the active `$co-paper` route.

## Skill Routing / Skill 路由

- **EN:** Use `$co-search` to retrieve literature and classify only the innovation points in the literature into five module families: new phenotype, new mechanism, new molecule type, new experimental method, and new bioinformatics analysis.
  **中：** 用 `$co-search` 检索文献，并且只把文献中的创新点按五类模块分类：新表型、新机制、新分子类型、新实验方法、新生信分析。
- **EN:** After `$co-search`, stop and ask the user to choose one innovation module, not one whole paper class.
  **中：** `$co-search` 后暂停，让用户选择一个创新模块，而不是选择一个完整文献类别。
- **EN:** Use `$co-plan` to convert the selected module into an executable plan: public-data analysis, node-discovery experiment, validation experiment, virtual-result prompt, or manuscript integration for that module only.
  **中：** 用 `$co-plan` 把用户选中的模块转化为可执行计划：公共数据分析、节点发现实验、验证实验、虚拟结果 prompt 或该模块的论文整合。
- **EN:** Ask `$co-plan` to classify the module relationship as `parallel`, `progressive_downstream`, `progressive_upstream`, or `standalone`, and to plan both a node-discovery layer and a validation layer.
  **中：** 要求 `$co-plan` 标记模块关系为 `parallel`、`progressive_downstream`、`progressive_upstream` 或 `standalone`，并同时规划节点发现层和验证层。
- **EN:** Use `$co-result` after the selected module has real, partial, assumed, or explicitly approved virtual results. `$co-result` closes the current module by writing module Results, figure logic, source ledger, and raw-data needs.
  **中：** 当该模块已有真实、部分、假设或用户明确允许的虚拟结果后，用 `$co-result` 写出该模块 Results、图版逻辑、来源账本和原始数据需求。到这里一个模块结束。
- **EN:** Before `$co-result` closes a module, confirm that discovery evidence and validation evidence are both present, partial, assumed, virtual-with-approval, or requirements-only. Do not silently write a complete module from discovery-only evidence.
  **中：** `$co-result` 关闭模块前，确认发现证据和验证证据均已处于真实、部分、假设、用户批准的虚拟或仅需求状态。不要把只有发现层的证据悄悄写成完整模块。
- **EN:** After each module closes, ask the user whether to continue to a downstream module, branch to another innovation point, or end the project. If continuing, restart `$co-search -> $co-plan -> $co-result` for the next module.
  **中：** 每个模块结束后，询问用户是继续到下游模块、转向另一个创新点，还是结束项目。如果继续，则对下一模块重新启动 `$co-search -> $co-plan -> $co-result`。
- **EN:** Only when the user decides to end the whole project, integrate the accumulated module results with final `$co-result`, then call `$co-method`, `$co-discussion`, assemble `manuscript/full_manuscript.md`, and call `$co-completer`.
  **中：** 只有用户决定结束整个项目时，才用最终 `$co-result` 整合所有模块结果，然后调用 `$co-method`、`$co-discussion`，组装 `manuscript/full_manuscript.md`，再调用 `$co-completer`。

If a named skill is unavailable, continue with the same output contract and state the gap.
如果某个被点名的 skill 不可用，继续按同一输出契约完成，并说明缺口。

## State Files / 状态文件

Read `references/project_contract.md` before creating a workspace or assembling the final paper.
创建项目目录或组装全文前，读取 `references/project_contract.md`。

Read `references/co_paper_workflow_explanation.md` when the user asks how `$co-paper` works, how modules progress, how `$co-completer` is integrated, how to resume or branch, or when a human-readable workflow explanation is needed.
当用户询问 `$co-paper` 如何运行、模块如何递进、`$co-completer` 如何整合、如何回跳/分支，或需要一份人类可读流程解释时，读取 `references/co_paper_workflow_explanation.md`。

Minimum state files / 最小状态文件：

- `project_state.md`: current biological question, current module, completed modules, current round, active claims, next decision / 当前生物学问题、当前模块、已完成模块、当前轮次、活跃 claim 和下一步决策。
- `decision_log.md`: every user choice and why it mattered / 每个用户选择及其意义。
- `module_ledger.csv`: one row per module, including selected innovation angle, plan, result status, and downstream decision / 每个模块一行，记录创新角度、计划、结果状态和下游决策。
- `evidence_ledger.csv`: literature, public data, local analysis, experimental, and virtual-result evidence / 文献、公共数据、本地分析、实验和虚拟结果证据账本。
- `source_mode_ledger.csv`: source mode for each result / 每个结果的来源模式。

Use `scripts/scaffold_project.py` when starting a new project folder.
新建项目目录时使用 `scripts/scaffold_project.py`。

## Human Checkpoints / 人类决策点

Stop for user choice unless the user explicitly says to continue automatically.

1. After `$co-search`: choose one innovation module from the five families.
2. After `$co-plan`: choose analysis, experiment, virtual-result simulation, or revise the plan.
3. Before `$co-result`: confirm whether both module evidence layers are available or whether one layer should be written as requirements-only.
4. Before `$co-result` generates virtual positive results: confirm source mode, novelty rationale, simulation direction, and whether virtual discovery, virtual validation, or both are allowed.
5. After each `$co-result` module: choose next downstream module, parallel branch, upstream branch, or end the project.
6. Before final manuscript assembly: confirm source ledgers and rationale files for any simulation-only major claims.
7. After `$co-completer`: choose `complete_project`, `dynamic_branch`, or `new_module_loop`.

## Public Data Download Policy / 公共数据下载策略

**EN:** For public datasets, default to user-managed download. Co-Paper should ask `$co-plan` to save a ranked data download priority list with the dataset accession, why it matters for the selected module, required files, minimum metadata, expected analysis, and what evidence it can or cannot provide. Do not automatically download large, permissioned, Git-LFS, SRA/dbGaP, Synapse, institutional, or unstable public-data files unless the user explicitly asks for Codex-side download.

**中文：** 公共数据默认由用户手动下载。Co-Paper 应要求 `$co-plan` 保存按优先级排序的数据下载清单，写清数据编号、为什么对当前模块重要、所需文件、最低 metadata、预期分析和可提供/不可提供的证据。除非用户明确要求 Codex 侧下载，不要自动下载大型、需权限、Git-LFS、SRA/dbGaP、Synapse、机构访问或不稳定的公共数据文件。

## Module Round Logic / 模块轮次逻辑

1. Record the selected innovation module and why the user chose it.
2. Record whether this module is parallel to, downstream of, upstream of, or standalone relative to prior modules.
3. Define one active claim for the module.
4. Define the minimum evidence needed to close both the node-discovery layer and the validation layer.
5. Ensure the validation layer perturbs the upstream/input side and observes the downstream/output side; if the tested node is a mediator, require rescue or explicitly mark rescue as missing.
6. Use `$co-plan` to predefine support, neutral, contradictory, and non-interpretable outcomes for both layers.
7. Inspect available files before coding or analysis.
8. Save scripts, figures, tables, and interpretation under `module_##/`.
9. Use `$co-result` to close the module only after both layers are represented in the source ledger or explicitly marked requirements-only.
10. Update `module_ledger.csv`, `project_state.md`, `evidence_ledger.csv`, and `source_mode_ledger.csv`.
11. Ask the user to choose the next downstream module, a parallel branch, an upstream branch, or end the project.

Never force a positive narrative when a module result is neutral or contradictory.
当模块结果中性或矛盾时，不要强行写成正向故事。

## Manuscript Assembly / 全文组装

Run manuscript assembly only when the user says the project should end or move to full manuscript.

1. Final `$co-result`: integrate all completed module Results, legends, figure prompts/images, raw-data needs, and source notes.
2. `$co-method`: write `manuscript/methods.md` from final Results panels.
3. `$co-discussion`: write `manuscript/introduction.md`, `manuscript/discussion.md`, and numbered references.
4. `manuscript/full_manuscript.md`: one Chinese full manuscript by default, including title placeholder, abstract placeholder, Introduction, Results, Discussion, Methods, References, and figure legends.
5. `$co-completer`: write `manuscript/completion_review.md`, `manuscript/completion_revision_plan.md`, `manuscript/completion_decision_menu.md`, and any marked revisions or branch/new-module plans.
6. If the user chooses `complete_project`, save `manuscript/project_completion_record.md`; if `dynamic_branch`, create a new project/subfolder under `branches/`; if `new_module_loop`, restart `$co-search -> $co-plan -> $co-result` for the selected downstream module.

Read `references/final_review_and_dynamic_resume.md` before invoking `$co-completer` or resuming from a completion checkpoint.
调用 `$co-completer` 或从完成检查点继续前，读取 `references/final_review_and_dynamic_resume.md`。

Keep simulation status in project reports and source ledgers even when manuscript-facing prose is written in conventional Results style.
即使论文正文按常规 Results 风格书写，也要在项目报告和来源账本中保留模拟结果状态。

Before manuscript assembly, if any major claim uses `virtual_positive_results` or `assumed_results`, require `virtual_result_rationale.md` or `assumed_result_explanation.md`.
组装全文前，如果任何主要 claim 使用 `virtual_positive_results` 或 `assumed_results`，必须有 `virtual_result_rationale.md` 或 `assumed_result_explanation.md`。

## Required Outputs / 必要输出

Every stage must save a Chinese Markdown report by default. Tables should be CSV or TSV. Figures should be PNG when generated; otherwise save `figure_prompts.md` and `figure_generation_blockers.md`.

Default folders / 默认目录：

- `01_search/`
- `02_modules/`
- `module_01/`, `module_02/`, ...
- `manuscript/`
- `branches/`

Final response should list saved paths and the current next decision.
最终回复需列出关键保存路径和当前下一步决策。
