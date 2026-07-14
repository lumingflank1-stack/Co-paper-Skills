# Co-Paper Project Contract

Use this reference when creating a project workspace, continuing a module round, or assembling the final manuscript.

## Folder Contract

```text
project_slug/
├── project_state.md
├── decision_log.md
├── module_ledger.csv
├── hypothesis_ledger.csv
├── evidence_ledger.csv
├── source_mode_ledger.csv
├── 01_search/
├── 02_modules/
├── module_01/
│   ├── plan/
│   ├── debate/
│   ├── scripts/
│   ├── figures/
│   ├── tables/
│   └── interpretation_and_next_module.md
├── module_02/
└── manuscript/
    ├── results.md
    ├── methods.md
    ├── introduction.md
    ├── discussion.md
    ├── references_numbered.md
    ├── virtual_result_rationale.md
    ├── full_manuscript.md
    ├── completion_review.md
    ├── completion_revision_plan.md
    ├── completion_decision_menu.md
    └── project_completion_record.md
branches/
└── YYYYMMDD_<resume_target>/
    ├── branch_state.md
    ├── inherited_files.md
    ├── module_##/
    └── manuscript/
```

## Module Ledger Columns

`module_id,relationship_type,parent_module_id,parallel_group,innovation_family,selected_innovation_point,selected_hypothesis_id,selected_hypothesis,biological_question,active_claim,discovery_status,validation_status,rescue_status,plan_file,result_file,source_modes,result_interpretation,next_downstream_options,user_decision,status`

## Hypothesis Ledger Columns

`module_id,selected_innovation_point,hypothesis_id,rank,hypothesis_name,novelty,evidence_strength,feasibility,causal_testability,translational_value,collision_risk,risk_penalty,total,user_decision,status,co_plan_handoff`

Record all five ranked `$co-debate` hypotheses. Mark exactly one as `selected` before `$co-plan`; the others remain `not_selected`, `high_risk`, `weakened`, or `rejected`.

Relationship values:

- `standalone`
- `parallel`
- `progressive_downstream`
- `progressive_upstream`

Layer status values:

- `planned`
- `real`
- `partial`
- `assumed`
- `virtual_approved`
- `requirements_only`
- `missing`

Innovation families:

- `new_phenotype`
- `new_mechanism`
- `new_molecule_type`
- `new_experimental_method`
- `new_bioinformatics_analysis`

## Evidence Ledger Columns

`id,stage,module_id,claim,evidence_type,source,source_detail,evidence_tier,direction,confidence,limitations,next_action`

Evidence types:

- `literature`
- `public_dataset`
- `local_analysis`
- `node_discovery`
- `validation_perturbation`
- `mediator_rescue`
- `wet_lab`
- `virtual_simulated`
- `database_annotation`
- `computational_inference`
- `unresolved`

## Source Mode Ledger Columns

`result_id,stage,module_id,figure_panel,claim,source_mode,input_file_or_source,simulation_status,allowed_in_manuscript,notes`

Use `allowed_in_manuscript=draft_with_source_note` for virtual results when the manuscript-facing prose should read like a conventional paper draft, and keep the virtual status in `source_mode_ledger.csv` or the Markdown report.

For any virtual or assumed-positive major claim, save `virtual_result_rationale.md` or `assumed_result_explanation.md` before final assembly.

默认情况下，`manuscript/full_manuscript.md` 只输出中文全文；除非用户明确要求，不生成英文或中英双语版本。

## Decision Log Template

```markdown
## Decision YYYY-MM-DD Module N

- Decision:
- Options considered:
- Innovation family:
- Selected module:
- Top 5 hypothesis ranking file:
- Selected hypothesis ID and rank:
- Selected hypothesis:
- Module relationship: standalone / parallel / progressive_downstream / progressive_upstream
- Parent or parallel module:
- Reason:
- Required node-discovery layer:
- Required validation layer:
- Rescue requirement if mediator:
- Evidence used:
- What this enables:
- What remains uncertain:
```

## Final Assembly Checklist

- Every included module has a result file and source-mode entries.
- Every included module records the five co-debate hypotheses and the user's selected hypothesis.
- Every included module records its relationship to other modules: standalone, parallel, upstream, or downstream.
- Every complete module has both a node-discovery layer and a validation layer, or explicitly marks one layer as requirements-only/missing.
- Mediator claims include rescue evidence or an explicit unresolved-rescue note.
- Results claims have source modes.
- Methods map to every Results panel.
- Introduction cites prior work and does not overclaim novelty.
- Discussion addresses rival explanations and boundaries.
- References are numbered consistently.
- Virtual results are recorded in state files, source ledgers, or final notes.
- Virtual or assumed-positive major claims have a rationale/explanation file before manuscript assembly.
- `full_manuscript.md` is a single Chinese manuscript unless another language was explicitly requested.
- `$co-completer` has produced `completion_review.md`, `completion_revision_plan.md`, and `completion_decision_menu.md`.
- `completion_decision_menu.md` asks the user to choose `complete_project`, `dynamic_branch`, or `new_module_loop`.

## Dynamic Resume Rules

After `$co-completer`, do not treat the workflow as closed until the user chooses a terminal route. The user may resume from any checkpoint with enough state:

- `module_search`: go back to `$co-search` and classify innovation points for a new downstream question.
- `module_debate`: rerun `$co-debate`, rerank the Top 5, or select another hypothesis without overwriting prior outputs.
- `module_plan`: revise or rerun `$co-plan` for the user-selected hypothesis.
- `module_result`: regenerate or extend `$co-result` for a selected module.
- `figure_or_result`: select a Figure, panel, result, or failed experiment and call `$co-plan` for the next public-data, node-discovery, validation, or virtual-result round.
- `manuscript_revision`: use `completion_review.md` and `completion_revision_plan.md` as the roadmap and regenerate affected Results, Methods, Introduction, Discussion, figures, or full manuscript.
- `new_module_loop`: restart `$co-search -> user module choice -> $co-debate -> user hypothesis choice -> $co-plan -> $co-result`.

When branching, create a new folder under `branches/YYYYMMDD_<resume_target>/`, copy or reference inherited files in `inherited_files.md`, and never overwrite the prior manuscript unless the user explicitly asks to overwrite.
