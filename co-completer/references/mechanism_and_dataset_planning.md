# Mechanism and Dataset Planning

Use this reference after the user approves revision recommendations.

## Mechanism Completion Map

Build a concise chain:

```text
Context or disease state -> upstream driver -> core molecule/cell pathway
-> downstream effector -> phenotype -> validation -> translational relevance
```

For each weak link, propose one analysis and one experiment that can strengthen it.

## Deepen-Then-Close Route

Use this route when the user chooses to go beyond normal completion after `$co-completer` review/writing.

The route is intentionally bounded:

1. Define one deeper research question or missing routine.
2. Call `$co-search` once to search and classify the most relevant supplement literature.
3. Call `$co-distill` once to extract the supplement routine, node-discovery logic, validation ladder, or figure logic.
4. Save `deepening_co_search_distill_plan.md` plus the supplement search/distill outputs.
5. Return to the completion menu and ask whether to close, branch, or revise.

Do not run an unbounded research loop in the completion stage unless the user explicitly asks.

## Mechanism Extension Axes

Use these axes to make the story more complete:

- `Upstream`: ligand, receptor, transcription factor, epigenetic state, mechanical stress, metabolism, microbiome/metabolite, cytokine, hypoxia, aging, sex, diet, drug exposure, or disease-stage driver.
- `Downstream`: effector molecule, secreted factor, cell-cell communication, ECM remodeling, angiogenesis, innervation, immune recruitment, cell death, senescence, fibrosis, barrier function, or tissue remodeling.
- `Deeper mechanism`: direct binding, post-translational modification, chromatin occupancy, causal perturbation, rescue, temporal ordering, spatial localization, human validation, or dose-response.

## Bioinformatics Plan

For each suggested analysis, include:

- Biological question.
- Dataset type.
- Candidate public sources to search.
- Minimal metadata required.
- Analysis method.
- Supportive result.
- Contradictory result.
- Figure panel candidate.
- Limitation and required wet-lab follow-up.

Common analysis options:

- Bulk RNA-seq or microarray: differential expression, GSEA, GSVA, WGCNA, deconvolution, subtype scoring, perturbation signature comparison.
- scRNA-seq: sample-level pseudobulk, cell-state abundance, module scores, differential state, trajectory, ligand-receptor analysis, regulon analysis, donor-aware statistics.
- scATAC-seq or multiome: motif enrichment, peak-to-gene links, TF activity, regulatory accessibility around candidate genes.
- Spatial transcriptomics or imaging: localization of target cells, neighborhood analysis, spatial co-expression, disease-region gradients.
- Proteomics or phosphoproteomics: pathway activation, target protein abundance, post-translational mechanism.
- Metabolomics: pathway flux proxy, metabolite-mediator links, integration with transcriptomics.
- Genetics and clinical association: GWAS Catalog, eQTL, pQTL, colocalization, Open Targets, survival or clinical association when disease-appropriate.
- Perturbation resources: CRISPR screens, drug signatures, DepMap, LINCS, CMap, or public knockdown/overexpression datasets.

## Public Dataset Sources

Search current resources for specific IDs rather than inventing them:

| Need | Sources to search |
|---|---|
| Bulk expression | GEO, SRA, ArrayExpress or BioStudies, recount, GREIN |
| Single-cell | GEO, CELLxGENE Census, Human Cell Atlas, Single Cell Portal, PanglaoDB, TISCH2 for cancer |
| Spatial | GEO, CELLxGENE, HuBMAP, spatialLIBD, platform-specific repositories |
| Cancer cohorts | TCGA, cBioPortal, CPTAC, ICGC, DepMap |
| Proteomics | PRIDE, ProteomeXchange, CPTAC |
| Metabolomics | MetaboLights, Metabolomics Workbench, HMDB for annotation |
| Genetics | GWAS Catalog, Open Targets, GTEx, eQTL Catalogue, FinnGen, UK Biobank resources when available |
| Epigenomics | ENCODE, Roadmap Epigenomics, Cistrome, GEO |
| Drug perturbation | LINCS, CMap, DrugBank or ChEMBL for annotation, DepMap for dependency |

When reporting a dataset, include accession, species, tissue, disease/model, assay, sample size, key metadata, usability, and caveats.

## Experimental Supplement Plan

Separate two jobs:

1. `Node discovery`: finding downstream mediators or phenotype-linked mechanism nodes.
2. `Node validation`: proving the selected node is required and sufficient.

Candidate experiments:

- Expression validation: qPCR, western blot, ELISA, IF/IHC, flow cytometry.
- Causal perturbation: siRNA/shRNA, CRISPR knockout, CRISPRi/a, overexpression, inhibitor, neutralizing antibody.
- Rescue: gene rescue, mutant rescue, recombinant ligand, pathway agonist/antagonist, metabolite add-back.
- Direct mechanism: Co-IP, pull-down, PLA, CETSA, DARTS, SPR, BLI, ITC, kinase assay, ubiquitination or phosphorylation assay.
- Regulatory mechanism: ChIP-qPCR/ChIP-seq, ATAC-qPCR/ATAC-seq, luciferase reporter, CUT&Tag.
- Phenotype: migration, proliferation, apoptosis, senescence, differentiation, barrier integrity, matrix degradation, immune activation, organoid phenotype, animal model readout.
- In vivo validation: disease model, tissue-specific knockout, local delivery, pharmacologic intervention, histology, behavior or function when relevant.

## Dataset Manifest Fields

Write `dataset_manifest.csv` with:

```text
dataset_id,source,species,tissue_or_cell,disease_or_model,assay,n_samples,key_metadata,planned_analysis,claim_supported,limitations,priority
```

Do not list fake accession numbers unless the user explicitly asks for virtual dataset placeholders.
