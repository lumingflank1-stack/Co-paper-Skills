# Completion Review and Route Schema

## Completion review

Include:

1. Manuscript snapshot and central claim.
2. Overall editorial/readiness assessment.
3. Major and minor concerns.
4. Figure-by-figure audit.
5. Claim-evidence matrix.
6. Three-module audit: bioinformatics exploration, experimental validation, bioinformatics validation.
7. Statistics, reproducibility, and source-mode audit.
8. Rival explanations and limitations.
9. Smallest decisive missing evidence set.
10. Readiness: `ready_to_complete`, `complete_after_minor_writing`, `needs_branch_or_more_data`, or `needs_new_evidence_cycle`.

## Revision plan

`priority,issue,recommended_change,needed_data,affected_claim_or_figure,expected_impact,risk_if_omitted`

Classify actions as `must_fix`, `high_value`, `optional`, or `future_work`. Wait for approval before rewriting.

## Completion decision menu

- `complete_project`: preserve the accepted manuscript, figures, ledgers, review, and completion date.
- `dynamic_branch`: resume a prior plan, module, claim, Figure, result, method, or manuscript checkpoint without overwriting.
- `new_evidence_cycle`: start `co-plan -> co-result -> co-method -> co-discussion` from a revised claim.
- Topic change is not an evidence-cycle route; explicitly switch to `co-mimic` when requested.
