# Co-Paper Project Contract

## Folder contract

```text
project_slug/
|-- project_state.md
|-- decision_log.md
|-- module_ledger.csv
|-- evidence_ledger.csv
|-- source_mode_ledger.csv
|-- 01_plan/
|-- 02_results/
|-- modules/
|   |-- bioinformatics_exploration/
|   |-- experimental_validation/
|   `-- bioinformatics_validation/
|-- manuscript/
`-- branches/
```

## Module ledger

`cycle_id,module_type,biological_question,active_claim,plan_file,result_file,status,source_modes,interpretation,user_decision`

Module types:

- `bioinformatics_exploration`
- `experimental_validation`
- `bioinformatics_validation`

Statuses: `planned`, `real`, `partial`, `assumed`, `virtual_approved`, `requirements_only`, `missing`, `neutral`, `contradictory`, `not_interpretable`.

## Evidence ledger

`id,cycle_id,module_type,claim,evidence_type,source,source_detail,evidence_tier,direction,confidence,limitations,next_action`

## Source-mode ledger

`result_id,cycle_id,module_type,figure_panel,claim,source_mode,input_file_or_source,simulation_status,allowed_in_manuscript,notes`

## Decision log

Record the research seed, active claim, three-module plan, independence boundary, rescue requirement, source modes, evidence gaps, user approvals, and next action.

## Final assembly gate

- All three modules have a status and source-mode entries.
- Exploration and bioinformatics validation are independent or explicitly labeled internal robustness.
- Experimental claims map to perturbation and downstream readouts.
- Mediator claims include rescue or state the gap.
- Neutral and contradictory findings are preserved.
- Methods map to every Results panel.
- Co-Result has produced `methods_input.md`, `discussion_input.md`, and `downstream_handoff.md`.
- Co-Method has produced `manuscript/methods.md`, the result-to-method map, and `co_discussion_handoff.md`.
- Co-Discussion has produced Introduction, Discussion, numbered references, limitations, and `full_manuscript_handoff.md`.
- Virtual or assumed major claims have rationale files and are not submission-ready evidence.
- Co-Completer produces review, revision plan, and route menu.

## Resume

- `plan_revision`: revise one or all three module plans.
- `result_extension`: add evidence to a module and rerun Co-Result.
- `figure_or_claim`: return a specific panel or claim to Co-Plan.
- `manuscript_revision`: revise assembled manuscript files.
- `new_evidence_cycle`: start another `co-plan -> co-result` cycle from a revised question or molecule.

Never return automatically to Co-Search from Co-Paper. Use the topic-development pipeline only when the user explicitly wants new topic discovery.
