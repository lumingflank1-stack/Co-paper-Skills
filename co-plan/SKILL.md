---
name: co-plan
description: Design one coordinated biomedical evidence plan directly from a user's research field, disease, phenotype, intervention, molecule, or selected hypothesis. Use as the first active stage of co-paper to simultaneously produce a bioinformatics exploration module, an experimental validation module, and an independent bioinformatics validation module, with cross-module claims, decision rules, rescue logic, datasets, assays, and source-mode requirements.
---

# Co-Plan / 三模块研究计划

## Goal

Convert the user's research seed directly into one executable evidence cycle containing three coordinated modules. Do not require `$co-search`, innovation-family selection, topic cards, or a prior debate.

Default to Chinese reports unless the user requests another language.

## Inputs

Use one or more:

- Research field, disease, phenotype, biological process, intervention, or molecule supplied by the user.
- A selected `$co-debate` hypothesis, when available.
- Existing data, figures, tables, pilot experiments, or manuscript claims.
- Constraints: species, tissue/cell type, data type, assays, compute, timeline, and target journal.

## Workflow

1. Define the research question, active claim, exposure/input, candidate mediator, outcome, biological context, and evidence boundary.
2. Plan all three modules simultaneously:
   - **Bioinformatics exploration:** select discovery datasets or user data, QC, contrasts, covariates, candidate-generation analyses, prioritization rules, and exploration figures.
   - **Experimental validation:** define model, groups, perturbation, dose/time, phenotype and molecular readouts, direct-binding or mechanism assays, controls, rescue, falsification result, and backup plan.
   - **Bioinformatics validation:** select independent datasets or orthogonal computational methods; define replication, robustness, specificity, external/clinical validation, and validation figures.
3. Map every major claim to the module that discovers it and the modules that test it.
4. Prevent circular validation: exploration and validation must not reuse the same cohort, contrast, feature selection, and model without an explicit resampling or held-out design.
5. Define strong support, partial support, neutral, contradictory, and not-interpretable outcomes for each module and for the integrated claim.
6. Mark unavailable modules as `requirements_only` or `missing`; never hide the gap.
7. For mediator claims, require rescue or explicitly mark the causal tier as incomplete.
8. For virtual results, require explicit user approval and record which modules may be simulated.
9. Save plan files and a `$co-result` handoff.

Read `references/analysis_and_experiment_plan.md` for schemas and decision rules. Use `scripts/create_plan_templates.py` when a blank plan folder is useful.

## Evidence Rules

- Plan before analyzing and predefine interpretation thresholds.
- Prefer sample- or donor-level inference over cell-level-only significance.
- Treat enrichment, networks, regulons, trajectories, ligand-receptor inference, and CMap as hypothesis-generating.
- Bioinformatics validation requires an independent cohort, held-out subset, orthogonal data type, or genuinely orthogonal analysis; label weaker checks honestly.
- Experimental causality requires perturbation and downstream readout; mediator claims require rescue for the strongest tier.
- Default large public-data downloads to user-managed unless the user requests Codex-side download.

## Required Outputs

Save under `01_plan/` or the requested directory:

- `research_question_and_claim.md`
- `integrated_three_module_plan.md`
- `claim_module_map.csv`
- `bioinformatics_exploration_plan.md`
- `exploration_dataset_manifest.csv`
- `experimental_validation_plan.md`
- `bioinformatics_validation_plan.md`
- `validation_dataset_manifest.csv`
- `decision_rules.md`
- `risks_controls_and_rescue.md`
- `data_download_priority.md` when datasets are absent
- `virtual_result_prompt.md` only when requested
- `co_result_handoff.md`
