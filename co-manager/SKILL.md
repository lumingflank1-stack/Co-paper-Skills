---
name: co-manager
description: Orchestrate an interactive biomedical paper co-scientist workflow from literature search, classification, routine distillation, topic generation, public-data and experiment planning, iterative result interpretation, Results, Methods, Introduction, Discussion, full manuscript assembly, independent manuscript review, and dynamic post-review branching/resume. Use when Codex needs to coordinate co-search, co-distill, co-topic, co-plan, co-result, co-method, co-discussion, academic-paper-reviewer, save stage reports, or manage human checkpoints. 用于统筹从文献到全文、独立审稿和审稿后回跳迭代的多轮论文工作流。
---

# Co-Manager / 论文工作流总控

## Operating Goal / 运行目标

**English:** Run a stateful, interactive research-to-paper workflow. Co-Manager is the outer coordinator: it calls specialist skills, preserves provenance, stops at user decision points, and saves a report file for every stage.

**中文：** 运行有状态、互动式的“研究到论文”工作流。Co-Manager 是外层总控：负责调用专门 skill、保留证据来源、在用户决策点暂停，并为每个阶段保存报告文件。

Default to Chinese for user-facing reports unless the user requests another language. Stage Markdown reports and `manuscript/full_manuscript.md` should be Chinese-only by default; do not create parallel English or bilingual versions unless explicitly requested.  
除非用户要求其他语言，面向用户的报告默认使用中文。阶段性 Markdown 报告和 `manuscript/full_manuscript.md` 默认只写中文；除非用户明确要求，不创建英文或中英双语版本。

## Core Principle / 核心原则

```text
co-search -> user chooses class -> co-distill -> co-topic -> user chooses topic
-> co-plan -> analysis or experiment round(s) -> co-result -> co-method
-> co-discussion -> full manuscript assembly -> independent review
-> user chooses revise / branch / resume from an earlier checkpoint
```

**English:** Co-Manager manages state; inner skills perform specialist tasks.  
**中文：** Co-Manager 负责状态和流程管理；内部 skill 负责专门任务。

## Skill Routing / Skill 路由

- **EN:** Use `$co-search` for literature retrieval, screening, classification, and literature matrices.  
  **中：** 用 `$co-search` 做文献检索、筛选、分类和文献矩阵。
- **EN:** Use `$co-distill` to reverse engineer the selected paper class into a reusable article routine, including the node-discovery experiment that finds downstream mechanism molecules or phenotype-linked mediators.  
  **中：** 用 `$co-distill` 从选定文献类别中反推可复用文章套路，并提取发现下游机制分子或表型关联介质的节点发现实验。
- **EN:** Use `$co-topic` to generate, critique, and rank research topics from the distilled routine.  
  **中：** 用 `$co-topic` 基于蒸馏套路生成、反驳和排序课题。
- **EN:** Use `$co-plan` to design public-data analyses, node-discovery experiments, wet-lab validation, next-round decisions, and virtual-result prompts.  
  **中：** 用 `$co-plan` 设计公共数据分析、节点发现实验、湿实验验证、下一轮决策和虚拟结果 prompt。
- **EN:** Use `$co-result` only after results are available or after the user explicitly requests prompt-directed virtual positive results.  
  **中：** 只有在已有结果或用户明确要求按 prompt 生成虚拟阳性结果时，才调用 `$co-result`。
- **EN:** Use `$co-method` after Results are drafted so Methods align to actual result panels.  
  **中：** Results 成稿后再用 `$co-method`，确保 Methods 对应实际图版和结果。
- **EN:** Use `$co-discussion` after Results are stable so Introduction and Discussion are evidence-framed and cited.  
  **中：** Results 稳定后再用 `$co-discussion`，让引言和讨论围绕真实证据和编号引用展开。
- **EN:** Use `$academic-paper-reviewer` or the final-review contract after `manuscript/full_manuscript.md` is assembled to produce an independent review, rigor/novelty/newsworthiness assessment, editorial decision, and revision/resume roadmap.  
  **中：** `manuscript/full_manuscript.md` 组装后，用 `$academic-paper-reviewer` 或终稿审稿契约生成独立审稿、严谨性/创新性/新闻性评估、编辑决定和修订/回跳路线图。

If a named skill is unavailable, continue with the same output contract and state the gap.  
如果某个被点名的 skill 不可用，继续按同一输出契约完成，并说明缺口。

## State Files / 状态文件

Read `references/project_contract.md` before creating a workspace or assembling the final paper.  
创建项目目录或组装全文前，读取 `references/project_contract.md`。

Minimum state files / 最小状态文件：

- `project_state.md`: current question, selected class, selected topic, current round, active claims, next decision / 当前问题、选定类别、选定课题、当前轮次、活跃 claim 和下一步决策。
- `decision_log.md`: every user choice and why it mattered / 每个用户选择及其意义。
- `evidence_ledger.csv`: literature, public data, local analysis, experimental, and virtual-result evidence / 文献、公共数据、本地分析、实验和虚拟结果证据账本。
- `source_mode_ledger.csv`: source mode for each result / 每个结果的来源模式。

Use `scripts/scaffold_project.py` when starting a new project folder.  
新建项目目录时使用 `scripts/scaffold_project.py`。

## Human Checkpoints / 人类决策点

Stop for user choice unless the user explicitly says to continue automatically.  
除非用户明确要求自动继续，否则在以下节点暂停等待选择。

1. After `$co-search`: choose one literature class / 在 `$co-search` 后选择一个文献类别。
2. After `$co-topic`: choose one main topic or request revision / 在 `$co-topic` 后选择主课题或要求重写。
3. After every `$co-plan` round: choose public-data analysis, node-discovery experiment, validation experiment, or virtual-result simulation / 每轮 `$co-plan` 后选择公共数据分析、节点发现实验、验证实验或虚拟结果模拟。
4. Before `$co-result` generates virtual positive results, confirm the literature/public-data feasibility and novelty rationale, the closest prior work, and the selected positive result axis that is both plausible and maximally innovative / `$co-result` 生成虚拟阳性结果前，确认文献/公共数据可行性和创新性解释、最接近既往工作，以及既可能成立又最有创新性的阳性结果轴。
5. Before final manuscript assembly, confirm the source ledger exists for any simulation-only major claim / 组装全文前，确认任何仅基于模拟的重要 claim 都已有来源账本记录。
6. After independent review, ask the user to choose one next path: revise current manuscript, return to literature class selection, return to topic generation, continue from a selected Figure/result/experiment node, or start a branched manuscript version / 独立审稿后，让用户选择下一步：修订当前全文、回到文献类别选择、回到课题生成、从某个 Figure/结果/实验节点继续，或开启一个分支稿件版本。

## Round Logic / 迭代逻辑

1. **EN:** Record the planned claim, required evidence, and falsification criteria before analyzing.  
   **中：** 分析前记录计划中的 claim、所需证据和证伪标准。
2. **EN:** Record which step is discovering the node and which step is validating the node.  
   **中：** 记录哪一步是在发现节点，哪一步是在验证节点。
3. **EN:** For validation steps, record decisive assays such as conditional knockout, mass-spectrometry confirmation, SPR/BLI/ITC interaction detection, rescue, and phenotype readouts when relevant.  
   **中：** 对验证步骤，在相关时记录关键实验，如条件性敲除、质谱确认、SPR/BLI/ITC 互作检测、rescue 和表型读出。
4. **EN:** Inspect available files before writing code.  
   **中：** 写代码前先检查可用文件。
5. **EN:** Save scripts, figures, tables, and interpretation under `round_##/`.  
   **中：** 将脚本、图、表和解释报告保存到 `round_##/`。
6. **EN:** Classify each result as strong support, moderate support, weak support, neutral, contradictory, or not interpretable.  
   **中：** 将每个结果归类为强支持、中等支持、弱支持、中性、矛盾或不可解释。
7. **EN:** Revise the hypothesis and call `$co-plan` for the next dataset, node-discovery experiment, validation experiment, or virtual-result prompt.  
   **中：** 修正假说，并调用 `$co-plan` 设计下一步数据集、节点发现实验、验证实验或虚拟结果 prompt。

Never force a positive narrative when a result is neutral or contradictory.  
当结果中性或矛盾时，不要强行写成正向故事。

## Manuscript Assembly / 全文组装

1. `$co-result`: `manuscript/results.md`, legends, figure prompts/images, raw-data needs, source notes / 结果、图注、图片提示或图片、原始数据需求和来源说明。
2. `$co-method`: `manuscript/methods.md` from final Results / 基于最终 Results 撰写 Methods。
3. `$co-discussion`: `manuscript/introduction.md`, `manuscript/discussion.md`, numbered references / 撰写引言、讨论和编号参考文献。
4. `manuscript/full_manuscript.md`: one Chinese full manuscript by default, including title placeholder, abstract placeholder, Introduction, Results, Discussion, Methods, References, and figure legends / 默认只生成一个中文全文，包括标题占位、摘要占位、引言、结果、讨论、方法、参考文献和图注。
5. `manuscript/figures/Figure_*.png`: generated planning or manuscript figures when image generation is available; otherwise save figure prompts and blockers / 图片生成可用时保存规划图或论文图；否则保存图片 prompt 和阻断说明。
6. `manuscript/independent_peer_review.md`: independent review of rigor, novelty, newsworthiness, journal fit, risks, and revision roadmap / 独立审稿，评估严谨性、创新性、新闻性、期刊匹配度、风险和修订路线图。
7. `manuscript/iteration_resume_plan.md`: post-review dynamic continuation options and branch/resume targets / 审稿后的动态继续选项和分支/回跳目标。

Read `references/final_review_and_dynamic_resume.md` before running the final review or resuming from a post-review checkpoint.  
终稿审稿或审稿后回跳继续前，读取 `references/final_review_and_dynamic_resume.md`。

Keep simulation status in project reports and source ledgers even when manuscript-facing prose is written in conventional Results style.  
即使论文正文按常规 Results 风格书写，也要在项目报告和来源账本中保留模拟结果状态。

Before manuscript assembly, if any major claim uses `virtual_positive_results` or `assumed_results`, require `virtual_result_rationale.md` or `assumed_result_explanation.md` describing the literature search, public-data feasibility check, novelty scan, closest prior work, selected plausible-and-innovative result axis, why it is not a direct repeat, and remaining uncertainty.  
组装全文前，如果任何主要 claim 使用 `virtual_positive_results` 或 `assumed_results`，必须有 `virtual_result_rationale.md` 或 `assumed_result_explanation.md`，说明文献调研、公共数据可行性检查、创新性扫描、最接近既往工作、所选既可能成立又有创新性的结果轴、为什么不是直接重复，以及剩余不确定性。

## Required Outputs / 必要输出

**English:** Every stage must save a Chinese Markdown report by default. Tables should be CSV or TSV. Figures should be PNG when generated; otherwise save `figure_prompts.md` and `figure_generation_blockers.md`.

**中文：** 每个阶段默认都必须保存中文 Markdown 报告。表格使用 CSV 或 TSV。生成图片时保存 PNG；没有实际图片时保存 `figure_prompts.md` 和 `figure_generation_blockers.md`。

Default folders / 默认目录：

- `01_search/`
- `02_distill/`
- `03_topics/`
- `04_plan/`
- `round_01/`, `round_02/`, ...
- `manuscript/`
- `branches/`

Final response should list saved paths and the current next decision.  
最终回复需列出关键保存路径和当前下一步决策。
