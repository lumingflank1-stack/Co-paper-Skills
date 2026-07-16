# Co-Paper Workflow Explanation

## Two separate routes

Topic development is optional, separate, and controlled by Co-Mimic:

```text
co-mimic
|-- co-search
|-- internal routine distillation
|-- co-topic
`-- co-debate
```

- Co-Mimic manages state, checkpoints, and all handoffs.
- Co-Search builds the source corpus and returns control to Co-Mimic.
- Co-Mimic distills the reusable evidence architecture internally.
- Co-Topic generates 3-5 candidates and returns the selection to Co-Mimic.
- Co-Debate ranks five hypotheses and returns the final selection to Co-Mimic.

Co-Paper execution starts directly from the user's field, disease, phenotype, intervention, molecule, research question, or the selected Co-Debate hypothesis:

```text
research seed -> co-plan -> co-result -> co-method -> co-discussion
-> manuscript/full_manuscript.md -> co-completer
```

Co-Paper must not automatically prepend Co-Search and must not stop after Co-Result when the manuscript route is active.

## Three-module evidence cycle

Co-Plan designs all three modules together:

1. Bioinformatics exploration discovers and prioritizes the candidate axis.
2. Experimental validation perturbs the axis and tests phenotype, mechanism, direct interaction, and rescue.
3. Bioinformatics validation tests reproducibility, robustness, specificity, or clinical relevance in independent or orthogonal data.

Co-Result integrates the three modules with conservative claim strength. Reusing the same cohort and contrast does not count as independent bioinformatics validation.

## Checkpoints

1. Clarify the active claim only when the user seed is materially ambiguous.
2. Approve the coordinated Co-Plan.
3. Confirm source modes and missing modules before Co-Result.
4. Explicitly approve any assumed or virtual positive result.
5. Approve full manuscript assembly.
6. After Co-Completer choose `complete_project`, `dynamic_branch`, or `new_evidence_cycle`.

## Final assembly

```text
co-result -> co-method -> co-discussion
-> manuscript/full_manuscript.md -> co-completer
```

Co-Completer reviews readiness and may send the project back to Co-Plan for another three-module evidence cycle.
