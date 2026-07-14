# Co-Paper Modular Workflow Explanation

Use this reference when explaining the workflow, module progression, hypothesis debate, branching, or manuscript assembly.

## Core Model

A biomedical paper grows as a graph of modules rather than a copied whole-paper routine. A module may be `standalone`, `parallel`, `progressive_downstream`, or `progressive_upstream`.

Each module requires:

1. A node-discovery layer that finds a phenotype, molecule, mechanism node, or readout.
2. A validation layer that perturbs the upstream/input side and observes the downstream/output side. Mediator claims require rescue or an explicit missing-rescue label.

## Workflow

```text
co-search
-> classify literature innovation points into five families
-> user selects one innovation module
-> co-debate generates five competing hypotheses
-> co-debate critiques and ranks Top 5 from highest to lowest
-> user selects one hypothesis
-> co-plan designs discovery, validation, rescue, data, and decision rules
-> co-result closes the current module
-> user selects an upstream, downstream, parallel, or standalone next module, or ends the project
```
Every continuing module restarts the complete loop, including both user selections.

Final assembly begins only when the user ends the project:

```text
final co-result integration
-> co-method
-> co-discussion
-> manuscript/full_manuscript.md
-> co-completer
```

## Why Co-Debate Is Separate

`$co-search` organizes the literature landscape; it should not silently choose a mechanism. `$co-debate` converts the selected module into five explicit competing hypotheses and exposes assumptions, collision risk, alternatives, and falsification criteria before planning begins. `$co-plan` therefore receives one user-selected hypothesis rather than an unranked topic or an agent-selected story.

This separation creates two independent human decisions:

1. Which innovation module is worth pursuing?
2. Which mechanistic hypothesis within that module should be tested?

## Five Innovation Families

- `new_phenotype`
- `new_mechanism`
- `new_molecule_type`
- `new_experimental_method`
- `new_bioinformatics_analysis`

## Stage Responsibilities

| Stage | Main job | Required checkpoint |
|---|---|---|
| `$co-search` | Retrieve literature and classify module options | User selects one module |
| `$co-debate` | Generate, challenge, and rank five competing hypotheses | User selects one hypothesis or requests reranking |
| `$co-plan` | Build an executable two-layer plan for the selected hypothesis | User approves route |
| `$co-result` | Interpret evidence and close the current module | User selects next module relation or ends project |
| final `$co-result` | Integrate closed module Results | Project has ended |
| `$co-method` | Draft Methods from stable Results | Results are stable |
| `$co-discussion` | Draft Introduction, Discussion, and references | Results are stable |
| `$co-completer` | Review readiness and offer completion or resume routes | User chooses final route |

## Co-Debate Top 5 Contract

The five hypotheses must compete, not repeat one mechanism with different labels. At least one null, confounding, or reverse-causation hypothesis is required when evidence is associative. Each hypothesis includes evidence tier, predictions, strongest objection, alternative explanation, decisive test, falsification criteria, feasibility risk, and collision risk.

Ranking uses novelty, evidence strength, feasibility, causal testability, translational value, collision risk, and a risk penalty. Rank highest to lowest, then stop for user choice. Do not call `$co-plan` before selection.

## State and Provenance

Maintain:

- `project_state.md`
- `decision_log.md`
- `module_ledger.csv`
- `hypothesis_ledger.csv`
- `evidence_ledger.csv`
- `source_mode_ledger.csv`

`hypothesis_ledger.csv` keeps all five hypotheses, their scores, and the user's selected hypothesis. This prevents later manuscript writing from hiding discarded alternatives.

## Human Checkpoints

1. Select one module after `$co-search`.
2. Select one hypothesis after `$co-debate`.
3. Approve or revise `$co-plan`.
4. Confirm source modes before `$co-result`.
5. Explicitly approve any virtual positive Results.
6. Select next module relation or end the project.
7. Confirm ledgers before manuscript assembly.
8. After `$co-completer`, choose `complete_project`, `dynamic_branch`, or `new_module_loop`.

## Branch and Resume

- `module_search`: return to `$co-search`.
- `module_debate`: rerank or select another hypothesis.
- `module_plan`: revise the selected hypothesis plan.
- `module_result`: extend or regenerate current Results.
- `dynamic_branch`: create `branches/YYYYMMDD_<target>/` without overwriting prior outputs.
- `new_module_loop`: restart the complete workflow including `$co-debate`.

## Source Modes

- `real`
- `partial`
- `assumed`
- `virtual_positive`
- `requirements_only`

Never invent positive Results without explicit permission.

## Practical Trigger

```text
Use $co-paper. First run co-search and let me select one innovation module. Then run co-debate to generate, critique, and rank five competing hypotheses from highest to lowest. Let me select one hypothesis before co-plan. Plan discovery and validation layers for that hypothesis, use co-result only with declared source modes, and repeat the complete loop for every new module. Assemble the manuscript only after I end the project.
```
