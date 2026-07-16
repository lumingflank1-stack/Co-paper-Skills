---
name: co-paper
description: Orchestrate a biomedical paper workflow that starts directly from the user's research field, disease, phenotype, intervention, molecule, or a hypothesis selected by co-mimic, and runs co-plan -> co-result -> co-method -> co-discussion -> full manuscript -> co-completer. Co-search is not a co-paper stage. When topic development is requested, use co-mimic as the separate parent orchestrator that manages co-search, co-topic, and co-debate.
---

# Co-Paper / 生物医学论文执行主控

## Goal

Turn the user's research question, field, disease, phenotype, intervention, molecule, or a selected `$co-debate` hypothesis directly into an executable three-module evidence plan and then a Results package.

Default to Chinese for project reports and manuscript files unless the user requests another language.

## Core Route

```text
user research field / molecule / question / selected hypothesis
-> co-plan
   -> bioinformatics exploration module
   -> experimental validation module
   -> bioinformatics validation module
-> co-result
-> co-method
-> co-discussion
-> manuscript/full_manuscript.md
-> co-completer
```

Do not automatically call `$co-mimic`, `$co-search`, `$co-topic`, or `$co-debate` inside Co-Paper. Topic development is a separate optional workflow controlled by Co-Mimic:

```text
co-mimic
|-- co-search
|-- internal routine distillation
|-- co-topic
`-- co-debate
```

Co-Mimic's selected hypothesis may be handed to Co-Paper as the research question.

## Three Required Modules

1. **Bioinformatics exploration:** discover candidate molecules, pathways, phenotypes, cell states, targets, or mechanisms using public data, omics, networks, screens, or user data.
2. **Experimental validation:** test the nominated axis using perturbation, phenotypic and molecular readouts, direct-binding or mechanism assays, and rescue when claiming a mediator.
3. **Bioinformatics validation:** test reproducibility and generalizability in independent datasets or orthogonal computational analyses, including cross-cohort replication, robustness, specificity, clinical association, or external validation.

Exploration and bioinformatics validation must not reuse the same dataset and contrast as if they were independent evidence. If independent validation is unavailable, mark it `requirements_only` or `missing`.

## Routing

1. Parse the user's question and constraints. Do not require a literature-classification checkpoint.
2. Call `$co-plan` once to design all three modules as a coordinated evidence cycle.
3. Ask the user to approve or revise the plan when a consequential choice remains.
4. Call `$co-result` only when each module has real, partial, assumed, explicitly approved virtual, requirements-only, or missing status.
5. Integrate the three modules in this order unless evidence supports another order: exploration -> experimental validation -> bioinformatics validation.
6. Never force a positive story when any module is neutral or contradictory.
7. When Results stabilize, require `$co-result` to save `methods_input.md` and `discussion_input.md`.
8. Call `$co-method` to write `manuscript/methods.md` and the Results-to-Methods map.
9. Call `$co-discussion` with Results plus Methods to write Introduction, Discussion, references, and the full-manuscript handoff.
10. Assemble `manuscript/full_manuscript.md`, then call `$co-completer`.

Read `references/project_contract.md` before scaffolding or final assembly. Read `references/co_paper_workflow_explanation.md` when explaining or resuming the workflow. Read `references/final_review_and_dynamic_resume.md` before `$co-completer` or a resumed evidence cycle.

Use `scripts/scaffold_project.py` when creating a new project workspace.

## Source Modes

- `real`: user-provided or computed result.
- `partial`: incomplete result; write only supported claims.
- `assumed`: user directs Codex to treat it as true.
- `virtual_positive`: explicitly requested simulated result.
- `requirements_only`: data are absent; write requirements, not findings.
- `missing`: required evidence is not yet represented.

Never invent positive results without explicit permission. Preserve source mode in project ledgers even when manuscript prose uses conventional Results style.

## Minimum State

- `project_state.md`
- `decision_log.md`
- `module_ledger.csv`
- `evidence_ledger.csv`
- `source_mode_ledger.csv`

## Human Checkpoints

Stop unless automatic continuation was requested:

1. After parsing the research seed when the active claim remains ambiguous.
2. After `$co-plan` to approve the coordinated three-module plan.
3. Before virtual or assumed positive results.
4. Before `$co-result` if any module is unrepresented.
5. Before full manuscript assembly.
6. After `$co-completer`: choose `complete_project`, `dynamic_branch`, or `new_evidence_cycle`.

## Required Folders

- `01_plan/`
- `02_results/`
- `modules/bioinformatics_exploration/`
- `modules/experimental_validation/`
- `modules/bioinformatics_validation/`
- `manuscript/`
- `branches/`

Final responses must list saved paths and the current next decision.
