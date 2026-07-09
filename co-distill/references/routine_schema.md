# Routine Distillation Schema

## Routine Distillation Report

```markdown
# Routine Distillation

## Source Set

## One-Sentence Routine

In [disease/context], identify [frontier phenotype/state] through [public-data or omics move], define the unresolved core molecule as `???`, discover `???` through [node-discovery experiment], validate `???` through [validation ladder], and test mechanism through [experiment ladder], leading to [manuscript claim]. Source-paper molecules are recorded as known examples or exclusion items, not as the new topic's proposed core target.

## Reusable Routine

1. Entry problem:
2. Public-data discovery:
3. Node-discovery experiment:
4. Candidate prioritization:
5. Cross-dataset validation:
6. Cell-type or tissue specificity:
7. Mechanistic inference:
8. Validation experiment:
9. Experimental perturbation:
10. Rescue or causality:
11. Translational angle:

## What To Copy

## What Not To Copy

## Reviewer Risks
```

## Figure Logic Table Columns

`figure,panel,panel_job,input_data_or_assay,comparison,claim_supported,evidence_tier,common_design_pattern,reusable_for_new_topic,notes`

## Dataset and Assay Inventory Columns

`item_id,source_paper,data_or_assay_type,accession_or_reagent,organism,tissue_or_cell_type,comparison,role_in_routine,node_discovery_or_validation,reusable_requirement,notes`

## Unknown Node Handoff

Use this handoff whenever the source papers contain already-studied molecules that should not be reused as new targets. The goal is to transfer phenotype and discovery strategy, while leaving the core target or mechanism molecule unresolved as `???` for co-plan.

```markdown
| Slot ID | Placeholder | Phenotype or mechanism gap | Known molecules to exclude | Allowed family-level hints | Discovery route | Minimum novelty filter |
|---|---|---|---|---|---|---|
| U1 | ??? |  |  |  | public-data screen / perturbation omics / proteomics / metabolomics / spatial screen / CRISPR screen / target fishing | no direct same molecule-same disease-same phenotype prior study |
```

## Node Discovery Experiment Map

Track how each source paper discovers the downstream molecule, mechanism node, or phenotype-linked mediator. For new-topic design, the source paper's exact node should usually become an exclusion item and the new node should be represented as `???` until discovered by co-plan:

```markdown
| Paper | Upstream perturbation or condition | Discovery assay | Data type | Source node found | Reusable discovery logic | Exclude from new topic? | Follow-up validation |
|---|---|---|---|---|---|---|---|
```

Typical node-discovery experiments include:

- differential transcriptomics after disease, treatment, knockout, knockdown, overexpression, or conditional knockout;
- proteomics, phosphoproteomics, secretomics, metabolomics, ubiquitinomics, acetylomics, or spatial omics;
- IP-MS, pull-down-MS, thermal proteome profiling, DARTS/CETSA-MS, or target-fishing assays;
- CRISPR/RNAi screen, reporter screen, pooled perturb-seq, or CMap-style perturbation matching;
- phenotype-linked imaging, flow, spatial neighborhood, ligand-receptor, or cell-cell communication screens.

Validation experiments are separate and should be extracted explicitly. Important validation examples include conditional knockout or tissue/cell-specific knockout, knockdown/overexpression, rescue, neutralization, inhibitor/agonist, mass-spectrometry detection or confirmation such as targeted MS/PRM/SRM, Co-IP-MS, IP-MS or pull-down-MS confirmation, SPR/BLI/ITC molecular interaction assays, Co-IP, CETSA/DARTS, reporter assays, and phenotype rescue.

验证实验必须单独提取。重要验证实验包括条件性敲除或组织/细胞特异性敲除、敲低/过表达、rescue、中和、抑制剂/激动剂、质谱检测或确认如 targeted MS/PRM/SRM、Co-IP-MS、IP-MS 或 pull-down-MS 确认、SPR/BLI/ITC 分子互作检测、Co-IP、CETSA/DARTS、报告基因和表型 rescue。

## Novelty and Gap Map

Track three layers:

- `known`: already established in source papers; these molecules should usually be excluded from new-topic core claims.
- `unknown_slot`: the `???` molecule, node, mediator, target class, or mechanism slot that co-plan should discover.
- `transferable_gap`: same routine could answer a different disease, cell type, phenotype, node family, or intervention without reusing the exact source molecule.
- `danger_zone`: too close to source papers or unsupported by available data.

## Replication Template

The template should be abstract enough to reuse:

```markdown
1. Select disease/context with unmet mechanism.
2. Retrieve public dataset type A.
3. Identify frontier phenotype, cell state, spatial niche, or response pattern by contrast B.
4. Define the unresolved core molecule or mechanism mediator as `???`; list exact source-paper molecules as known exclusions.
5. Run or reuse node-discovery experiment C to discover `???`.
6. Validate across dataset type D and run a novelty filter against close prior work.
7. Test cell-type specificity.
8. Link `???` to pathway, mediator, or phenotype.
9. Validate `???` by perturbation, rescue, direct interaction, or orthogonal assay as appropriate.
10. Add rescue or downstream phenotype readout.
11. Write Results in figure order.
```
