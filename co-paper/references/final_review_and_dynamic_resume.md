# Co-Completer Finalization and Dynamic Resume

Use this reference after `manuscript/full_manuscript.md` is assembled, or when the user wants to continue from a module checkpoint after `$co-completer`.

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
2. **Dynamic branch/resume (`dynamic_branch`)**: return to a prior module, a selected Figure/result/experiment node, or manuscript revision; create a new project or subfolder under `branches/YYYYMMDD_<target>/` or a user-named folder.
3. **New module loop (`new_module_loop`)**: restart `$co-search -> user module choice -> $co-debate -> user hypothesis choice -> $co-plan -> $co-result`.

## Resume State

Write `completion_decision_menu.md` with:

```markdown
# Completion Decision Menu

- Current manuscript:
- Completion review:
- Completion revision/writing:
- Completed modules:
- Recommended route:
- Route A complete_project:
- Route B dynamic_branch:
- Route C new_module_loop:
- User-selected route:
- Output folder if branching:
- Next module seed if continuing:
- Stop/go criteria for closure:
```

## Branching Rules

- Never overwrite prior manuscript outputs unless the user explicitly asks.
- Keep `module_ledger.csv`, `source_mode_ledger.csv`, and `evidence_ledger.csv` linked or copied into the branch.
- When resuming from a Figure/result, preserve the original Figure ID in the branch state, then assign new IDs only when the manuscript structure changes.
- If the user chooses a new downstream module, treat it as `new_module_loop`, including a fresh `$co-debate` Top 5 ranking and hypothesis selection, not as a silent replacement of the previous module.
- Do not run `$co-distill` or `$co-topic` in the active `$co-paper` branch unless the user explicitly requests those legacy tools.
