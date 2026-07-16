# Three-Module Co-Plan Schema

## Integrated plan

```markdown
# Integrated Three-Module Plan

## Research seed and active claim
- Field/disease/context:
- Molecule/intervention:
- Exposure/input:
- Candidate mediator:
- Outcome:
- Main alternative explanation:
- Falsification boundary:

## Module A: Bioinformatics exploration
- Discovery question:
- Dataset/user data:
- Required metadata and QC:
- Contrast/model/covariates:
- Candidate-generation method:
- Prioritization rule:
- Expected figures:
- Support/failure criteria:

## Module B: Experimental validation
- Model and groups:
- Perturbation/dose/time:
- Phenotype and molecular readouts:
- Direct interaction/mechanism assay:
- Controls:
- Rescue:
- Decisive experiment:
- Support/failure criteria:

## Module C: Bioinformatics validation
- Independent/orthogonal dataset or held-out design:
- Replication target:
- Robustness and specificity tests:
- Clinical/external validation:
- Expected figures:
- Support/failure criteria:

## Integrated decision rules
- Strong support:
- Partial support:
- Neutral:
- Contradictory:
- Not interpretable:
```

## Claim-module map

`claim_id,claim,exploration_source,experimental_test,bioinformatics_validation,independence_check,rescue_required,minimum_evidence,status`

## Dataset manifest

`dataset_id,module,source_database,accession,species,tissue_or_cell_type,data_type,comparison,required_metadata,download_status,local_path,analysis_role,independent_from,minimum_success_condition,notes`

## Circularity check

For each validation analysis state whether it uses an independent cohort, held-out samples, orthogonal modality, preregistered feature set, or genuinely orthogonal method. If none applies, label it internal robustness rather than external validation.

## Virtual result prompt

Specify source mode separately for all three modules. Virtual outputs require explicit user approval and a rationale file describing closest prior work, feasibility, novelty boundary, and remaining uncertainty.
