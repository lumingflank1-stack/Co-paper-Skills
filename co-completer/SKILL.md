---
name: co-completer
description: Complete the final stage of co-paper or review and revise an existing biomedical manuscript. Use after manuscript/full_manuscript.md for reviewer-style critique, readiness judgment, approved writing, marked Markdown or Word export, and a final route choice: complete_project, dynamic_branch, or new_evidence_cycle. A new evidence cycle returns directly to co-plan, then co-result, co-method, and co-discussion; use co-mimic separately only when the user wants a new topic or hypothesis.
---

# Co-Completer / 论文终审与动态恢复

## Goal

Act as the final gate after `manuscript/full_manuscript.md`. Review first, propose revisions second, wait for approval third, then write or supplement the manuscript. Never silently mark a project complete.

Default to Chinese reports unless the manuscript is in another language; manuscript-facing text follows the manuscript language.

## Workflow

1. Inspect the manuscript, Results, Methods, figures, supplements, ledgers, target journal, reviewer comments, and user goals.
2. Save `completion_review.md` before editing. Audit novelty, rigor, claim-evidence alignment, three-module completeness, statistics, reproducibility, figures, methods, rival explanations, and submission readiness.
3. Save `completion_revision_plan.md` with `must_fix`, `high_value`, `optional`, and `future_work` actions. Stop for user approval unless automatic continuation was requested.
4. If more evidence is needed, define one revised active claim and call `$co-plan` directly for a coordinated cycle:
   - bioinformatics exploration;
   - experimental validation;
   - independent bioinformatics validation.
5. Before Results writing, classify every planned output as `real`, `partial`, `assumed`, `virtual_positive`, `requirements_only`, or `missing`. Virtual positive results require explicit approval.
6. Call `$co-result` to integrate the three modules and create Methods/Discussion handoffs.
7. Call `$co-method` and `$co-discussion` after stabilized Results, then reassemble `manuscript/full_manuscript.md` when the accepted revisions change the manuscript.
8. For marked revisions, wrap new or substantially revised manuscript-facing text with `<span style="color:red"><strong>...</strong></span>`. Use `scripts/export_marked_docx.py` when DOCX export is requested.
9. Save `completion_decision_menu.md` and stop for one route:
   - `complete_project`: save `project_completion_record.md`.
   - `dynamic_branch`: resume a prior claim, Figure, result, plan, method, or manuscript checkpoint under `branches/YYYYMMDD_<target>/` without overwriting prior outputs.
   - `new_evidence_cycle`: start `co-plan -> co-result -> co-method -> co-discussion` from a revised question, field, molecule, or claim.

If the user wants to discover a different topic or hypothesis rather than strengthen the current paper, leave Co-Paper and call `$co-mimic`, which manages `$co-search`, `$co-topic`, and `$co-debate`.

## Evidence and Safety Rules

- Separate association, computational inference, perturbation, direct interaction, rescue, independent validation, and clinical relevance.
- Do not turn enrichment or network inference into causality.
- Do not invent Results or precise numerical values without supplied data or explicit virtual approval.
- Assumed or virtual major claims are not ready for real-evidence submission.
- Preserve source modes in ledgers and keep manuscript prose conventional unless visible labels are requested.
- Preserve prior branches and manuscripts unless the user explicitly requests overwrite.

## Human Checkpoints

1. After `completion_revision_plan.md`.
2. Before any assumed or virtual positive result.
3. Before final export when major claims remain assumed, virtual, requirements-only, or missing.
4. After `completion_decision_menu.md`.

## Required Outputs

Save under `manuscript/` or a task-specific revision folder:

- `completion_review.md`
- `completion_revision_plan.md`
- `completion_decision_menu.md`
- `claim_evidence_gap_map.csv`
- `result_source_ledger.md`
- `revised_results_marked.md` when revised
- `revised_manuscript_marked.md` when revised
- corresponding `.docx` files when requested
- `change_log.md`
- `raw_data_requirements_summary.md`
- `project_completion_record.md` for `complete_project`
- `branch_resume_plan.md` for `dynamic_branch`
- `new_evidence_cycle_plan.md` for `new_evidence_cycle`

## References

- `references/review_and_revision.md`: review and final route schema.
- `references/mechanism_and_dataset_planning.md`: three-module evidence-cycle planning.
- `references/results_and_export.md`: source modes, downstream handoff, marked revisions, and DOCX export.
