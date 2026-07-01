# Co-Completer Finalization and Dynamic Resume

Use this reference after `manuscript/full_manuscript.md` is assembled, or when the user wants to continue from a middle checkpoint after `$co-completer`.

## Finalization Through `$co-completer`

Do not let `$co-paper` end with a standalone independent review. After full manuscript assembly, hand off to `$co-completer`.

`$co-completer` must perform completion review and writing, then save:

- `manuscript/completion_review.md`: rigor, novelty, newsworthiness, journal fit, evidence sufficiency, source modes, missing experiments, and final readiness.
- `manuscript/completion_revision_plan.md`: accepted or proposed writing/revision/supplement plan.
- `manuscript/completion_decision_menu.md`: the user's terminal-route choices.
- marked manuscript or Results files if writing/revision is performed.

If any major claim still uses `virtual_positive_results` or `assumed_results`, `$co-completer` must explicitly judge the manuscript as not ready for real evidence submission, while still evaluating the value of the project plan.

## Completion Decision Menu

After `$co-completer` review/writing, stop and ask the user to choose one route unless they asked to continue automatically:

1. **Mark project complete (`complete_project`)**: save `manuscript/project_completion_record.md`, listing final manuscript, figures, ledgers, source modes, review/writing files, and completion date.
2. **Dynamic branch/resume (`dynamic_branch`)**: return to literature class selection, topic generation, plan, selected Figure/result/experiment node, or manuscript revision; create a new project or subfolder under `branches/YYYYMMDD_<target>/` or a user-named folder.
3. **Deepen then close (`deepen_then_close`)**: after `$co-completer` review/writing, define one deeper research or supplement question, run one focused `$co-search` and one `$co-distill` cycle, save supplement reports, then return to the completion decision or mark complete.

## Resume State

Write `completion_decision_menu.md` with:

```markdown
# Completion Decision Menu

- Current manuscript:
- Completion review:
- Completion revision/writing:
- Recommended route:
- Route A complete_project:
- Route B dynamic_branch:
- Route C deepen_then_close:
- User-selected route:
- Output folder if branching:
- Stop/go criteria for closure:
```

## Branching Rules

- Never overwrite prior manuscript outputs unless the user explicitly asks.
- Keep `source_mode_ledger.csv` and `evidence_ledger.csv` linked or copied into the branch.
- When resuming from a Figure/result, preserve the original Figure ID in the branch state, then assign new IDs only when the manuscript structure changes.
- If the user chooses a different literature class, treat it as a new branch, not a silent replacement of the prior class.
- If the user chooses `deepen_then_close`, keep the cycle bounded to one `$co-search` plus one `$co-distill` unless the user explicitly asks for another round.
