---
name: co-mimic
description: Orchestrate a complete biomedical mimic-topic workflow by managing co-search, internal routine distillation, co-topic, and co-debate. Use when Codex must start from a disease, molecule, field, paper, or paper cluster; build the literature source set through co-search; distill reusable evidence architecture without copying targets; generate 3-5 topics through co-topic; debate exactly five hypotheses through co-debate; and deliver the user-selected hypothesis to co-paper or co-plan.
---

# Co-Mimic / 仿生选题总控

## Goal

Run the complete topic-development workflow. `$co-mimic` is the parent orchestrator; `$co-search`, `$co-topic`, and `$co-debate` are managed subskills.

```text
co-mimic
|-- co-search: build the source corpus
|-- internal distillation: extract the reusable routine
|-- co-topic: generate and rank 3-5 topic candidates
`-- co-debate: challenge and rank five hypotheses for the selected topic
```

Default to Chinese reports unless the user requests another language.

## Inputs

Accept a research field, disease, molecule, intervention, phenotype, cell type, method, paper, DOI, PDF, paper cluster, existing literature matrix, or user constraints.

## Orchestration Workflow

### Stage 1: Manage Co-Search

1. Translate the user's seed into search scope and exclusions.
2. Call `$co-search` to build the literature matrix, evidence ledger, method inventory, novelty exclusions, and ranked source set.
3. Verify provenance and coverage. If search is blocked or too narrow, record the blocker and revise the search before continuing.
4. Return control to Co-Mimic; do not route from Co-Search directly to Co-Topic.

### Stage 2: Distill the routine inside Co-Mimic

5. Extract the shared biological question, novelty move, figure order, statistics, translational endpoint, and three evidence jobs: bioinformatics exploration, experimental validation, and bioinformatics validation.
6. Extract candidate-discovery methods, perturbation logic, direct-binding assays, rescue logic, and decisive readouts.
7. Separate demonstrated findings, author interpretation, and speculation.
8. Record source-paper molecules as examples, controls, or exclusions. Preserve unresolved transferable nodes as `???` with allowed family, context, discovery route, and novelty filter.
9. Save the routine and a controlled `$co-topic` handoff.

### Stage 3: Manage Co-Topic

10. Call `$co-topic` with the distilled routine, `???` slots, exclusions, constraints, and reviewer risks.
11. Require 3-5 biologically distinct topic cards with three-module outlines, falsification criteria, and collision-risk scoring.
12. Stop for the user to select one topic unless automatic continuation was requested.
13. Return the selected topic to Co-Mimic and prepare the `$co-debate` handoff.

### Stage 4: Manage Co-Debate

14. Call `$co-debate` for exactly five genuinely competing hypotheses around the selected topic.
15. Require reviewer objections, alternatives, decisive tests, falsification criteria, and ranked scores.
16. Stop for the user to select one hypothesis unless automatic continuation was requested.
17. Save the final hypothesis, rejected alternatives, evidence gaps, and three-module implications.

### Stage 5: Final handoff

18. Offer the selected hypothesis as an optional seed for `$co-paper` or `$co-plan`.
19. Do not automatically enter Co-Paper unless the user requested continuous execution.

Read `references/routine_schema.md` for distillation and handoff schemas.

## Guardrails

- Copy evidence structure, not prose, targets, or complete biological stories.
- Preserve citation provenance for every routine element.
- Do not nominate a source-paper molecule or close prior target as the new core innovation.
- Keep discovery, experimental validation, and independent bioinformatics validation distinct.
- Require rescue for mediator claims or mark it missing.
- Treat public-data evidence as association or inference unless perturbation establishes causality.
- If no sufficiently distinct topic survives, stop with failure modes rather than forcing a winner.

## State and Outputs

Save under `co_mimic/` or the requested directory:

- `mimic_state.md`
- `decision_log.md`
- `01_search/`: Co-Search outputs
- `02_distill/`: routine, figure logic, evidence map, exclusions, `???` handoff
- `03_topics/`: Co-Topic outputs and user selection
- `04_debate/`: Co-Debate outputs and user selection
- `mimic_final_handoff.md`

The final handoff must identify the selected topic and hypothesis, active claim, alternative explanation, falsification criteria, evidence gaps, novelty boundary, and requirements for bioinformatics exploration, experimental validation, and bioinformatics validation.
