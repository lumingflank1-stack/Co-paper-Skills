---
name: co-topic
description: Generate, critique, and preliminarily rank 3-5 biomedical topic candidates as a subskill managed by co-mimic. Consume Co-Mimic's distilled routine, ??? slots, exclusions, and constraints; return topic cards and the user-selected topic to co-mimic. Do not call co-debate directly when running under Co-Mimic because the parent orchestrator controls that handoff.
---

# Co-Topic / 仿生课题生成与筛选

## Goal

Transform Co-Mimic's distilled evidence routine into 3-5 biologically distinct topic candidates. Keep unknown innovation nodes as `???`, assess collision risk, and return the selected topic to the Co-Mimic parent orchestrator.

Default to Chinese reports unless the user requests another language.

## Inputs

- `$co-mimic` outputs, especially `routine_distillation.md`, `unknown_node_handoff.md`, `novelty_and_gap_map.md`, `reviewer_risk_ledger.md`, and `co_topic_handoff.md`.
- Disease, molecule, model, dataset, assay, timeline, and journal constraints.

If routine distillation is absent, return to `$co-mimic`. If the source basis is inadequate, return to `$co-search`.

## Workflow

1. Identify transferable evidence jobs and biological elements that must change.
2. Generate 3-5 candidates with different disease, cell, phenotype, molecule-family, intervention, or mechanistic contexts.
3. Preserve every undiscovered core node as `???`; specify its permitted family and discovery route without naming it.
4. For each topic, define phenotype-level mechanism, public datasets, discovery route, experimental validation, bioinformatics validation, rescue need, decisive test, alternative explanation, and falsification criteria.
5. Exclude source-paper molecules and close same-target/same-context collisions.
6. Score novelty, evidence, public-data feasibility, analysis feasibility, experimental feasibility, unknown-node discoverability, causal testability, collision risk, and manuscript potential.
7. Recommend a primary and backup topic, but stop for user selection unless automatic continuation was requested.
8. Save the selected topic card and evidence boundary, then return control to `$co-mimic`; Co-Mimic decides when to invoke `$co-debate`.

Read `references/topic_schema.md` for schemas.

## Required Outputs

Save under `03_topics/` or the requested directory:

- `topic_cards.md`
- `topic_prioritization.csv`
- `three_module_outline.md`
- `dataset_needs.csv`
- `unknown_node_discovery_plan.md`
- `experiment_needs.md`
- `falsification_plan.md`
- `topic_selection_brief.md`
- `co_debate_handoff.md` after user selection

If no candidate is sufficiently distinct, save `topic_failure_modes.md` and recommend changing the source set or context.
