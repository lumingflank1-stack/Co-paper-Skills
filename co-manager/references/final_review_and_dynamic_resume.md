# Final Review and Dynamic Resume

Use this reference after `manuscript/full_manuscript.md` is assembled, or when the user wants to continue from a middle checkpoint after review.

## Final Independent Review

Generate `manuscript/independent_peer_review.md` by default. Use `$academic-paper-reviewer` when available; otherwise follow this contract directly.

The review must evaluate:

- rigor / 严谨性;
- novelty / 创新性;
- newsworthiness or story value / 新闻性;
- target-journal fit / 目标期刊匹配度;
- evidence sufficiency and source mode / 证据充分性和来源模式;
- decisive missing experiments and analyses / 关键缺失实验和分析;
- whether the manuscript is ready for real submission, only suitable as a planning scaffold, or should branch to another workflow path / 是否可真实投稿、仅适合作为规划稿，或应分支到其他流程。

If any major claim still uses `virtual_positive_results` or `assumed_results`, explicitly judge the manuscript as not ready for real evidence submission, while still evaluating the value of the project plan.

Recommended files:

- `manuscript/independent_peer_review.md`
- `manuscript/iteration_resume_plan.md`
- optional `manuscript/revision_checklist.csv`

## Dynamic Resume Menu

After review, stop and ask the user to choose one route unless they asked to continue automatically:

1. **Revise current manuscript**: use review comments to regenerate affected sections and figures.
2. **Return to literature class**: go back to `01_search/` and choose a different class or rerun `$co-search`.
3. **Return to topic generation**: reuse `02_distill/` and call `$co-topic` again.
4. **Continue from a result/Figure node**: select a Figure, panel, result, node-discovery experiment, validation experiment, or contradictory result, then call `$co-plan`.
5. **Create a branch**: start `branches/YYYYMMDD_<resume_target>/` and write new outputs there without overwriting the previous manuscript.

## Resume State

Write `iteration_resume_plan.md` with:

```markdown
# Iteration Resume Plan

- Current manuscript:
- Review file:
- Recommended decision:
- Available resume targets:
- User-selected target:
- Files inherited:
- Files to regenerate:
- New output folder:
- Stop/go criteria:
```

## Branching Rules

- Never overwrite prior manuscript outputs unless the user explicitly asks.
- Keep `source_mode_ledger.csv` and `evidence_ledger.csv` linked or copied into the branch.
- When resuming from a Figure/result, preserve the original Figure ID in the branch state, then assign new IDs only when the manuscript structure changes.
- If the user chooses a different literature class, treat it as a new branch, not a silent replacement of the prior class.
