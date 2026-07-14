# Search and Innovation-Point Classification Schema

## Search Strategy Report

`search_strategy.md` should include:

- Research question.
- User constraints.
- Databases searched.
- Exact query strings.
- Search date.
- Inclusion criteria.
- Exclusion criteria.
- Known search limitations.

## Literature Matrix Columns

`paper_id,title,authors,year,journal,doi,pmid,study_type,disease_or_context,species,tissue_or_cell_type,main_axis,data_types,public_dataset_accessions,key_results,validation_level,limitations,notes`

## Innovation Point Matrix Columns

`innovation_id,paper_id,innovation_family,innovation_point,biological_context,why_new_or_useful,evidence_type,key_method_or_dataset,validation_level,can_be_selected_as_module,likely_next_step,limitations,notes`

Innovation families:

- `new_phenotype`
- `new_mechanism`
- `new_molecule_type`
- `new_experimental_method`
- `new_bioinformatics_analysis`

## Module Options Report

Save `module_options.md` with the five sections below. Each section should list selectable modules rather than whole paper classes.

```markdown
# Module Options

## 1. New Phenotypes

| Option | Innovation point | Representative papers | Why useful | First co-debate move |
|---|---|---|---|---|

## 2. New Mechanisms

| Option | Innovation point | Representative papers | Why useful | First co-debate move |
|---|---|---|---|---|

## 3. New Molecule Types

| Option | Innovation point | Representative papers | Why useful | First co-debate move |
|---|---|---|---|---|

## 4. New Experimental Methods

| Option | Innovation point | Representative papers | Why useful | First co-debate move |
|---|---|---|---|---|

## 5. New Bioinformatics Analyses

| Option | Innovation point | Representative papers | Why useful | First co-debate move |
|---|---|---|---|---|

## Recommended Choice

- Best first module:
- Rationale:
- What it can answer:
- What it cannot answer:
- Suggested prompt for `$co-debate`:
```

## Co-Debate Handoff

After the user selects one module, save `co_debate_handoff.md`:

```markdown
# Co-Debate Handoff

- Selected innovation family:
- Selected innovation point:
- User selection reason:
- Parent or parallel module:
- Key supporting papers and evidence-ledger rows:
- Known mechanisms or targets to avoid:
- Main uncertainties:
- Required debate output: five competing hypotheses ranked highest to lowest
```

## Evidence Tier Labels

- `background`: useful context, not direct evidence.
- `association`: correlation or differential abundance/expression.
- `multi_dataset_support`: repeated association across cohorts.
- `mechanistic_inference`: pathway, network, ligand-receptor, regulon, trajectory, or CMap inference.
- `perturbation`: knockdown, knockout, inhibitor, stimulation, or rescue.
- `causal_rescue`: perturbation plus downstream rescue or phenotype reversal.

When classifying validation ladders, explicitly capture decisive assays such as conditional knockout, tissue/cell-specific knockout, mass-spectrometry detection or confirmation, SPR/BLI/ITC molecular interaction assays, Co-IP, CETSA/DARTS, rescue, and phenotype readouts.

Use the weakest applicable tier when a paper mixes strong and weak claims.

## What Not To Do

- Do not output `topic_classes.md` as the main `$co-paper` decision file.
- Do not ask the user to choose a whole literature class.
- Do not infer a complete study design from one paper or one literature cluster.
