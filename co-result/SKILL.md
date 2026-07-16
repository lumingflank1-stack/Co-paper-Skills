---
name: co-result
description: Draft and package Chinese biomedical Results from a co-plan three-module evidence cycle or user-provided findings, then prepare explicit handoffs for co-method and co-discussion. Use after co-plan to integrate bioinformatics exploration, experimental validation, and independent bioinformatics validation while recording source modes, panel-indexed claims, figures, raw-data requirements, Methods inputs, and Discussion inputs.
---

# Co-Result / 三模块结果撰写

## Goal

Turn the coordinated Co-Plan outputs and available findings into a compact Results package organized around three evidence modules: bioinformatics exploration, experimental validation, and bioinformatics validation.

Default to Chinese biomedical manuscript style unless the user requests another language.

## Source Modes

Choose before drafting:

1. `input_results`: actual or partial user-provided/computed results.
2. `assumed_results`: the user explicitly directs Codex to treat a result as true.
3. `virtual_positive_results`: the user explicitly requests simulated, mock, expected, or positive virtual results.
4. `requirements_only`: data are absent or the request asks only for requirements.
5. `missing`: a required module has no usable evidence or approved substitute.

Never invent positive findings without explicit permission.

## Workflow

1. Parse the active claim, planned assays, comparisons, endpoints, expected direction, and source mode.
2. Build a three-module evidence map:
   - bioinformatics exploration evidence;
   - experimental validation evidence, including rescue when required;
   - bioinformatics validation evidence from independent or orthogonal data/analysis.
3. Confirm each module is `real`, `partial`, `assumed`, `virtual_approved`, `requirements_only`, or `missing`.
4. Check independence between exploration and validation datasets. Do not present reuse of the same cohort/model as external validation.
5. Link each conclusion to figure panel, assay/dataset, comparison, module, evidence tier, and source mode.
6. Write Results in the default order: discovery signal -> experimental perturbation/causality -> independent bioinformatics replication/robustness -> integrated conclusion and boundary.
7. If evidence is neutral, contradictory, or not interpretable, write that outcome directly rather than forcing a positive narrative.
8. Write figure legends and raw-data requirements for every panel.
9. For a full package, identify every independent manuscript Figure and use the available image-generation route when appropriate; otherwise save prompts and blockers.
10. Generate virtual data or workbooks only in explicitly approved virtual mode. Record simulation status in the Markdown source note and `result_source_ledger.md`, not repeatedly in manuscript prose.
11. Derive `methods_input.md` from every Results panel, dataset, assay, comparison, statistic, reagent class, and model that requires a reproducible method.
12. Derive `discussion_input.md` from the central advance, evidence strength, independent validation, rival explanations, limitations, and unresolved claims.
13. Hand stabilized Results first to `$co-method`, then pass Results plus completed Methods to `$co-discussion`. Do not end the Co-Paper route at `$co-result`.

## Downstream Handoff

The required manuscript route is:

```text
co-result -> co-method -> co-discussion
-> manuscript/full_manuscript.md -> co-completer
```

- `$co-method` consumes Results, figure legends, `claim_panel_map.csv`, raw-data requirements, and `methods_input.md`.
- `$co-discussion` consumes Results, Methods, evidence/source ledgers, `discussion_input.md`, and the final claim map.
- If Results are not stable, mark the handoff blocked and return to `$co-plan` rather than drafting unsupported Methods or Discussion.

## Claim Strength Rules

- Exploration alone supports discovery or association, not causality.
- Experimental perturbation supports functional relevance; mediator rescue is required for the strongest mediation claim.
- Bioinformatics validation supports reproducibility, robustness, specificity, or clinical relevance, not experimental causality.
- A complete integrated claim normally requires all three modules; otherwise state the precise boundary.
- Do not fabricate exact p values, n values, Kd values, fold changes, or clinical endpoints unless supplied or explicitly requested as virtual values.

## Reference Loading

- `references/result_writing.md`: Results order and claim strength.
- `references/figure_generation.md`: figure generation.
- `references/raw_data_and_virtual_excel.md`: raw-data and virtual workbook rules.
- `references/output_contract.md`: package structure.
- `scripts/write_virtual_workbook.py`: optional structured workbook export.

## Required Outputs

- `three_module_results_section.md`
- `module_evidence_map.md`
- `claim_panel_map.csv`
- `result_source_ledger.md`
- `figure_generation_prompts.md`
- `figure_generation_blockers.md` when needed
- `figures/Figure_*.png` when generated
- `figure_asset_manifest.md` when figures are generated
- `raw_data_requirements_summary.md`
- `methods_input.md`
- `discussion_input.md`
- `downstream_handoff.md`
- `virtual_result_rationale.md` or `assumed_result_explanation.md` when applicable
- `*_virtual_raw_data.xlsx` only when explicitly requested

Final responses must list saved paths and point to the source ledger.
