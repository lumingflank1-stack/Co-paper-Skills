# Three-Module Evidence-Cycle Planning

Use this reference after the user approves revisions that require more evidence.

## Route

```text
revised field / molecule / question / claim
-> co-plan
   -> bioinformatics exploration
   -> experimental validation
   -> independent bioinformatics validation
-> co-result -> co-method -> co-discussion
-> full_manuscript.md -> co-completer
```

Do not call Co-Search from the Co-Paper completion loop. If the user wants a new topic, switch explicitly to Co-Mimic.

## Required planning map

- Active claim and alternative explanation.
- Bioinformatics exploration dataset, model, candidate-generation rule, and decision threshold.
- Experimental model, perturbation, phenotype/molecular readouts, direct mechanism, controls, and rescue.
- Independent or orthogonal bioinformatics validation dataset, replication target, robustness, specificity, and clinical relevance.
- Circularity check between exploration and validation.
- Strong, partial, neutral, contradictory, and not-interpretable outcomes.
- Raw-data requirements and source modes.

For public datasets include accession when verified, species, tissue/cell type, assay, sample size, metadata, planned role, independence status, usability, and caveats. Never invent accessions.
