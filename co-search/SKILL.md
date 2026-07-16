---
name: co-search
description: Search, screen, and organize biomedical literature as a subskill managed by co-mimic, or as a standalone fixed-corpus search. Use when Co-Mimic needs a source corpus, literature matrix, evidence ledger, method inventory, novelty/exclusion map, and ranked paper set for internal routine distillation. Return control and outputs to co-mimic; do not route directly to co-topic, co-plan, or co-paper.
---

# Co-Search / 文献检索与来源集构建

## Goal

Build a traceable literature source set under `$co-mimic` management. Search broadly enough to expose reusable evidence architectures, but do not distill the final routine, generate topics, select hypotheses, or plan a Co-Paper project.

Default to Chinese reports unless the user requests another language.

## Workflow

1. Define the disease, molecule, intervention, phenotype, cell type, method, date window, and exclusions.
2. Build fielded queries with synonyms and search current literature unless the user supplies a fixed corpus or forbids browsing.
3. Screen titles, abstracts, full texts, figures, and supplements as available.
4. Build a literature matrix and evidence ledger.
5. Tag each paper by biological question, discovery strategy, experimental validation, bioinformatics validation, rescue/causality, figure logic, and translational endpoint.
6. Record known molecules, crowded mechanisms, and close-prior combinations that downstream skills must exclude.
7. Rank papers for routine distillation, save a `$co-mimic` handoff, and return control to the parent orchestrator.

Read `references/search_and_classification.md` for schemas.

## Evidence Rules

- Separate observations, author interpretation, database annotation, computational inference, perturbation, and direct causality.
- Treat enrichment, networks, regulons, trajectory, ligand-receptor inference, and public-data association as hypothesis-generating.
- Prefer primary research and official databases; use reviews for orientation.
- Do not claim novelty from a single query or database.
- Do not route directly to `$co-plan` or `$co-result`.
- In a Co-Mimic run, do not call `$co-topic` or `$co-debate`; Co-Mimic controls those stages.

## Required Outputs

Save under `01_search/` or the requested directory:

- `search_strategy.md`
- `literature_matrix.csv`
- `evidence_ledger.csv`
- `method_and_dataset_inventory.csv`
- `novelty_exclusion_map.md`
- `source_set_for_mimic.md`
- `co_mimic_handoff.md`
- `exclusion_log.csv`

If search is blocked, still save `search_strategy.md` and `search_blockers.md`.
