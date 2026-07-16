# Co-Search Source-Set Schema

## Literature matrix

`paper_id,title,year,journal,doi,pmid,study_type,disease_or_context,species,tissue_or_cell_type,molecule_or_intervention,phenotype,data_types,public_accessions,discovery_strategy,experimental_validation,bioinformatics_validation,rescue_or_causality,figure_logic,key_results,limitations,distillation_priority,notes`

## Evidence ledger

`evidence_id,paper_id,claim,evidence_type,evidence_tier,assay_or_dataset,comparison,direction,causal_strength,limitations,reusable_job,provenance`

Evidence tiers: `background`, `association`, `multi_dataset_support`, `mechanistic_inference`, `perturbation`, `direct_interaction`, `causal_rescue`.

## Method and dataset inventory

`item_id,paper_id,item_type,name_or_accession,role,discovery_or_validation,required_metadata,reusable_requirement,limitations`

## Co-Mimic handoff

Record:

- Research scope and constraints.
- Ranked source papers and why each matters.
- Common evidence architecture.
- Candidate discovery methods.
- Experimental validation ladder.
- Independent bioinformatics validation pattern.
- Known targets and crowded combinations to exclude.
- Unresolved gaps suitable for `???` slots.
- Search limitations and novelty boundary.

Do not include a Co-Plan recommendation. The next stage is `$co-mimic`.
