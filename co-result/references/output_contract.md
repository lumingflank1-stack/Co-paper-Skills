# Co-Result Output Contract

```text
02_results/
|-- three_module_results_section.md
|-- module_evidence_map.md
|-- claim_panel_map.csv
|-- result_source_ledger.md
|-- raw_data_requirements_summary.md
|-- methods_input.md
|-- discussion_input.md
|-- downstream_handoff.md
|-- figure_generation_prompts.md
|-- figure_generation_blockers.md
|-- figure_asset_manifest.md
|-- figures/
`-- virtual_result_rationale.md
```

`module_evidence_map.md` must show separate status for bioinformatics exploration, experimental validation, experimental rescue, and bioinformatics validation. It must also record whether the validation dataset is independent, held-out, orthogonal, or only an internal robustness check.

Do not call the integrated claim complete when a required module is missing unless the user explicitly accepts a requirements-only planning package.

When Results are stable, `downstream_handoff.md` must route first to `$co-method` and then to `$co-discussion`. It must name the exact Results, legends, maps, ledgers, and unresolved gaps each downstream skill should consume.
