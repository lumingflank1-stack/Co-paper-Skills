# Co-Manager Project Contract

Use this reference when creating a project workspace, continuing an iterative round, or assembling the final manuscript.

## Folder Contract

```text
project_slug/
├── project_state.md
├── decision_log.md
├── evidence_ledger.csv
├── source_mode_ledger.csv
├── 01_search/
├── 02_distill/
├── 03_topics/
├── 04_plan/
├── round_01/
│   ├── plan/
│   ├── scripts/
│   ├── figures/
│   ├── tables/
│   └── interpretation_and_revision.md
├── round_02/
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
    ├── round_##/
    └── manuscript/
```

## Evidence Ledger Columns

`id,stage,claim,evidence_type,source,source_detail,evidence_tier,direction,confidence,limitations,next_action`

Evidence types:

- `literature`
- `public_dataset`
- `local_analysis`
- `wet_lab`
- `virtual_simulated`
- `database_annotation`
- `computational_inference`
- `unresolved`

## Source Mode Ledger Columns

`result_id,stage,figure_panel,claim,source_mode,input_file_or_source,simulation_status,allowed_in_manuscript,notes`

Use `allowed_in_manuscript=draft_with_source_note` for virtual results when the manuscript-facing prose should read like a conventional paper draft, and keep the virtual status in `source_mode_ledger.csv` or the Markdown report.

For any virtual or assumed-positive major claim, save `virtual_result_rationale.md` or `assumed_result_explanation.md` before final assembly. The rationale file should summarize the literature search, public-data feasibility check, novelty scan, closest prior work, selected plausible-and-innovative positive result axis, why it is not a direct repeat, and remaining uncertainty.

默认情况下，`manuscript/full_manuscript.md` 只输出中文全文；除非用户明确要求，不生成英文或中英双语版本。

## Decision Log Template

```markdown
## Decision YYYY-MM-DD Round N

- Decision:
- Options considered:
- Reason:
- Evidence used:
- What this enables:
- What remains uncertain:
```

## Final Assembly Checklist

- Results claims have source modes.
- Methods map to every Results panel.
- Introduction cites prior work and does not overclaim novelty.
- Discussion addresses rival explanations and boundaries.
- References are numbered consistently.
- Virtual results are recorded in state files, source ledgers, or final notes even when manuscript-facing prose uses conventional Results style.
- Virtual or assumed-positive major claims have a rationale/explanation file before manuscript assembly, including closest prior work and novelty difference from direct repeats.
- `full_manuscript.md` is a single Chinese manuscript unless another language was explicitly requested.
- `$co-completer` has produced `completion_review.md`, `completion_revision_plan.md`, and `completion_decision_menu.md`.
- `completion_review.md` evaluates rigor, novelty, newsworthiness, journal fit, decisive missing evidence, and whether any virtual or assumed result is still blocking real submission.
- `completion_decision_menu.md` asks the user to choose `complete_project`, `dynamic_branch`, or `deepen_then_close`.

## Dynamic Resume Rules

After `$co-completer`, do not treat the workflow as closed until the user chooses a terminal route. The user may resume from any checkpoint that has enough state:

- `search_class`: go back to `01_search/` and choose or create a different literature class.
- `distilled_routine`: reuse `02_distill/` but ask `$co-topic` for new topics.
- `topic`: reuse or modify a selected topic and call `$co-plan`.
- `figure_or_result`: select a Figure, panel, result, or failed experiment and call `$co-plan` for the next public-data, node-discovery, validation, or virtual-result round.
- `manuscript_revision`: use `completion_review.md` and `completion_revision_plan.md` as the roadmap and regenerate affected Results, Methods, Introduction, Discussion, figures, or full manuscript.
- `deepen_then_close`: run one focused `$co-search` and one `$co-distill` cycle for a supplement question identified by `$co-completer`, then return to the completion menu or mark complete.

When branching, create a new folder under `branches/YYYYMMDD_<resume_target>/`, copy or reference inherited files in `inherited_files.md`, and never overwrite the prior manuscript unless the user explicitly asks to overwrite.
