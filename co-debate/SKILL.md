---
name: co-debate
description: "Generate, challenge, and rank exactly five competing biomedical hypotheses after a user has selected one innovation module from co-search. Use inside co-paper between co-search and co-plan: consume the selected module plus its evidence ledger, produce a highest-to-lowest Top 5 hypothesis list with reviewer critique, alternatives, falsification criteria, and decisive tests, then stop for the user to select one hypothesis before co-plan. 用于 co-paper 中用户选择创新模块后、co-plan 之前的科学辩论：围绕所选模块生成、反驳并由高到低排序五个竞争性假说，随后暂停，让用户选择一个假说进入 co-plan。"
---

# Co-Debate / 科学假说辩论与排序

## Operating Goal / 运行目标

Turn one user-selected innovation module into five competing, testable hypotheses. Debate them as a hostile but fair reviewer, rank them from highest to lowest, and stop for user selection. Do not design the full analysis or experiment plan; that belongs to `$co-plan`.

将用户从 `$co-search` 选中的一个创新模块转化为五个相互竞争、可检验的科学假说。以严厉但公平的审稿人视角逐一反驳，并从高到低排序，然后暂停让用户选择。不要在本阶段展开完整分析或实验计划；该工作属于 `$co-plan`。

Default to Chinese unless the user requests another language.

## Required Inputs / 必要输入

- Selected innovation family and innovation point from `$co-search`.
- `literature_matrix.csv`, `innovation_point_matrix.csv`, and `evidence_ledger.csv` when available.
- Parent module, parallel group, prior results, and user constraints when this is not the first module.

If the selected module or supporting evidence is missing, return to `$co-search`; do not invent a module.

## Debate Workflow / 辩论流程

1. Restate the selected module and the decision the user must make.
2. Separate observations, literature interpretation, database annotation, computational inference, perturbation evidence, and direct causal evidence.
3. Generate exactly five hypotheses that genuinely compete. Include at least one null, confounding, or reverse-causation hypothesis when current evidence is associative.
4. For each hypothesis, state mechanism, predictions, supporting evidence, strongest objection, alternative explanation, decisive test, and falsification criteria.
5. Score each hypothesis from 1 to 5 on novelty, evidence strength, feasibility, causal testability, translational value, and collision risk.
6. Apply a risk penalty: high novelty with weak evidence remains visible but is labeled `high-risk`; known or crowded mechanisms are penalized for collision risk.
7. Rank H1-H5 from highest to lowest total priority. Ties are broken by causal testability, then feasibility, then novelty.
8. Save the debate outputs and stop. Ask the user to select exactly one hypothesis or request a rerank/revision.
9. Pass only the selected hypothesis, its falsification criteria, and its evidence gaps to `$co-plan`.

Read `references/debate_and_ranking.md` for the hypothesis card, scoring schema, and handoff contract.

Use `scripts/scaffold_debate.py` when a blank debate folder is useful.

## Scientific Rules / 科学规则

- Do not present correlation, enrichment, regulons, ligand-receptor inference, virtual knockout, or network centrality as causal proof.
- Prefer donor/sample-level evidence over cell-level-only significance.
- Distinguish disease, treatment, cell type, donor, batch, and technical effects.
- Every hypothesis must include an alternative explanation and a result that would weaken or falsify it.
- Do not let five hypotheses become cosmetic variants of one mechanism.
- Do not choose on behalf of the user unless the user explicitly requests automatic continuation.
- Do not call `$co-plan` until the user has selected one ranked hypothesis.

## Required Outputs / 必要输出

Save under `01_search/debate/`, `module_##/debate/`, or the selected module folder:

- `debate_question.md`
- `hypothesis_cards.md`
- `hypothesis_ranking.csv`
- `reviewer_debate.md`
- `hypothesis_selection_menu.md`
- `co_plan_handoff.md` only after the user selects one hypothesis
