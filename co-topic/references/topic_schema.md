# Topic Generation Schema

## Topic Card

```markdown
### T1. Short Topic Name

- Distilled routine used:
- New biological context:
- Core mechanism: use phenotype-level mechanism with `???` for unresolved core molecule or mechanism mediator.
- Unknown core slot: `???`; include expected molecule family/module, known molecules to avoid, and how `???` will be discovered.
- Why this is not just copying the source papers:
- Primary evidence:
- Evidence tier:
- Public datasets needed:
- Bioinformatics tests:
- Node-discovery experiments:
- Expected figure plan:
- Decisive experiment:
- Validation experiments:
  - Conditional knockout or tissue/cell-specific knockout, if causal in vivo claim is intended:
  - Mass-spectrometry validation, if the node is a protein complex, target, post-translational modification, secreted factor, or metabolite:
  - SPR/BLI/ITC molecular interaction assay, if direct binding is claimed:
  - Rescue or phenotype readout:
- Falsification criteria:
- Alternative explanation:
- Reviewer concern:
- Translational angle:
- Current status: candidate / prioritized / backup / rejected
```

## Topic Prioritization Columns

`rank,topic_id,topic_name,unknown_core_slot,novelty,evidence,public_data_feasibility,analysis_feasibility,experiment_feasibility,unknown_node_discoverability,prior_collision_risk,causal_testability,manuscript_potential,total,decision,main_risk`

Score each numeric criterion from 1 to 5.

## Dataset Needs Columns

`topic_id,dataset_type,preferred_database,accession_if_known,species,tissue_or_cell_type,comparison,required_metadata,why_needed,minimum_success_condition`

## Node Discovery Plan

For each topic, specify how the downstream mechanism molecule, node, or phenotype-linked mediator will be found. If the topic card contains `???`, the plan must explain how `???` will be discovered and how known source-paper molecules will be excluded. Do not only list validation assays.

```markdown
### Node Discovery for <topic_id>

- Starting perturbation or contrast:
- Discovery assay: transcriptomics / proteomics / phosphoproteomics / secretomics / metabolomics / IP-MS / pull-down-MS / CRISPR screen / perturb-seq / spatial screen / ligand-receptor screen / target-fishing / other
- Samples or model:
- Candidate selection rule:
- Known molecules or close prior targets to exclude:
- Expected node type or family-level hint:
- Orthogonal shortlist check:
- Novelty filter before naming `???`:
- How this differs from direct validation:
```

## Experiment Needs

For each topic:

- Model.
- Node-discovery experiment.
- Perturbation.
- Conditional knockout or tissue/cell-specific knockout, if relevant.
- Mass-spectrometry detection or confirmation, if relevant.
- SPR/BLI/ITC molecular interaction detection, if relevant.
- Rescue, if causal claim is intended.
- Direct interaction assay, if physical binding is claimed.
- Controls.
- Readouts.
- Expected support result.
- Falsification result.
- Backup plan.

## Selection Brief

End with:

- Recommended main topic.
- Backup topic.
- Why the main topic is the best first test.
- Which `???` slot must be resolved first by co-plan.
- What the user must choose next.
