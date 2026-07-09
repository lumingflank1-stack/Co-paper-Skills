# Module Analysis and Experiment Plan Schema

## Module Plan

```markdown
# Module Plan

## Selected Module

- Module ID:
- Module relationship: standalone / parallel / progressive_downstream / progressive_upstream
- Parent module ID:
- Parallel group:
- Innovation family: new_phenotype / new_mechanism / new_molecule_type / new_experimental_method / new_bioinformatics_analysis
- Selected innovation point:
- Upstream context:
- Downstream question this module could enable:

## Active Claim

## Evidence Needed To Close This Module

- Node-discovery layer:
- Validation layer:
- Rescue requirement if this is a mediator claim:
- Minimum status to treat module as complete:

## Planned Route

- Public-data analysis:
- Node-discovery experiment:
- Validation experiment:
- Rescue experiment if mediator:
- Virtual result prompt:
- Manuscript integration:

## Decision Rules

- Strong support:
- Partial support:
- Neutral:
- Contradictory:
- Not interpretable:

## Layer-Specific Decision Rules

- Discovery layer support:
- Discovery layer failure:
- Validation layer support:
- Validation layer failure:
- Rescue support if mediator:
- Rescue failure if mediator:

## Next Module Options After Result

- If strong support:
- If partial support:
- If neutral:
- If contradictory:
```

## Analysis Plan

```markdown
# Analysis Plan

## Module Question

## Input Data

## Required Metadata

## Preprocessing and QC

## Main Comparison or Model

## Covariates and Confounders

## Decision Rules

## Expected Tables

## Expected Figures

## Failure Modes
```

## Dataset Manifest Columns

`dataset_id,source_database,accession,title,species,tissue_or_cell_type,data_type,comparison,required_metadata,download_status,local_path,analysis_role,expected_signal,minimum_success_condition,notes`

Download status values:

- `needs_search`
- `needs_download`
- `downloaded`
- `blocked`
- `not_suitable`

## Experiment Plan

```markdown
# Experiment Plan

## Discovery Layer

- Biological question:
- Starting contrast or perturbation:
- Model or sample:
- Discovery assay:
- Data type:
- Candidate or readout selection rule:
- Expected molecule/mechanism/phenotype/method readout:
- Orthogonal shortlist and novelty check:
- Required controls:
- Failure or ambiguity mode:

## Validation Layer

- Model:
- Samples:
- Upstream/input perturbation:
- Downstream/output readout:
- Conditional knockout or tissue/cell-specific knockout:
- Mass-spectrometry detection or confirmation:
- Rescue, required if testing a mediator:
- Direct interaction assay:
- SPR/BLI/ITC molecular interaction assay:
- Stimulation:
- Controls:
- Time points:
- Readouts:
- Expected support result:
- Falsification result:
- Sample size logic:
- Technical risks:
- Backup plan:
```

Discovery and validation are different evidence jobs:

- Discovery finds the downstream molecule, mechanism node, phenotype-linked mediator, assay readout, or analysis target for this module.
- Validation tests whether the selected node, mechanism, method, or phenotype claim is required, sufficient, reproducible, or clinically relevant by perturbing the upstream/input side and measuring the downstream/output side.
- If the module claims a mediator, validation should include rescue: perturb upstream, restore or block the mediator, and show downstream output restoration or loss.
- A complete module should not be written as complete from discovery-only evidence unless the user explicitly accepts a requirements-only or exploratory module status.

## Virtual Result Prompt

Use only when the user explicitly wants simulated or virtual results.

Before writing this prompt, perform or require a compact literature/public-data feasibility and novelty scan unless the user has fixed the result axis. Select the result axis that is both plausible and useful for the current module. Save the reasoning in `virtual_result_rationale.md` or `assumed_result_explanation.md`.

```markdown
# Virtual Result Prompt

You are generating virtual planning data for manuscript drafting. Write downstream manuscript-facing prose in conventional Results style, and record virtual source status only in the report or source ledger unless the user asks for visible labels.

Module ID:
Module relationship:
Parent or parallel module:
Innovation family:
Selected module:
Active claim:
Desired result mode: positive / negative / ambiguous / mixed
Discovery assays to simulate:
Validation assays to simulate:
Rescue assays to simulate if mediator:
Groups:
Replicates:
Expected direction:
Required tables:
Required figure summaries:
Constraints:
Output format:
Source-status requirement: record virtual status in the report or source ledger; do not repeat labels in every table, figure caption, or result paragraph unless requested.
Rationale requirement: save a separate rationale file explaining the literature search, public-data feasibility check, novelty scan, closest prior work, selected plausible-and-useful result axis, and remaining uncertainty.
```

## Decision Rules

Pre-register support levels:

- Strong support: sample-level or perturbation evidence matches prediction and controls major confounders.
- Partial support: discovery supports the module but decisive perturbation/downstream validation or mediator rescue is missing.
- Weak support: cell-level-only association or indirect enrichment.
- Neutral: inconsistent or underpowered result.
- Contradictory: decisive readout moves opposite to prediction.
- Not interpretable: missing metadata, failed QC, or inappropriate unit of replication.

## What Not To Do

- Do not design all upstream and downstream modules at once.
- Do not require `$co-distill` or `$co-topic` inputs.
- Do not turn a literature innovation point into a causal claim without planned evidence.
- Do not write Results from a plan unless real, partial, assumed, or explicitly approved virtual results exist.
