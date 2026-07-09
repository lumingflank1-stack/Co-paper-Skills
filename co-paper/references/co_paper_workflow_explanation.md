# Co-Paper Modular Workflow Explanation / Co-Paper 模块递进流程解释

Use this file when the user asks what `$co-paper` does, why `$co-distill`/`$co-topic` are no longer in the main route, how modules progress, where `$co-completer` fits, or how to resume/branch after a module or manuscript is assembled.

## Core Correction

Biomedical research should not be designed as one whole paper routine copied from literature. A paper usually grows by modules: one phenotype, one mechanism, one molecule class, one method, or one bioinformatics analysis leads to the next downstream question.

A large paper is therefore a set of modules, not a single monolithic design. Modules can be:

- `parallel`: separate branches that support the same central story from different angles.
- `progressive_downstream`: a later module explains or extends an earlier result.
- `progressive_upstream`: a later module searches for the regulator that controls an earlier result.
- `standalone`: a self-contained module that may later become part of the final story.

Each complete module has two evidence layers:

1. **Node-discovery layer**: finds the new thing in the module. This is often omics, public-data analysis, single-cell/spatial analysis, perturb-seq, CRISPR screen, proteomics, metabolomics, imaging screen, or another high-throughput/broad experiment.
2. **Validation layer**: tests the discovered or selected thing by perturbing the upstream/input side and observing the downstream/output side. If the module claims a mediator, the validation layer should include rescue, or clearly mark rescue as missing.

Therefore `$co-paper` uses a modular loop:

```text
co-search
-> classify literature innovation points into five module families
-> user chooses one module
-> co-plan
-> co-result
-> user chooses next downstream module or ends the project
```

Only after the user decides to end the whole project does `$co-paper` assemble the manuscript:

```text
final co-result integration
-> co-method
-> co-discussion
-> manuscript/full_manuscript.md
-> co-completer
```

## The Five Innovation Families

`$co-search` does not classify whole papers into complete article routines. It extracts and classifies innovation points from the literature into five families:

1. `new_phenotype`: new disease phenotype, cell state, spatial pattern, pathological process, clinical subgroup, or functional readout.
2. `new_mechanism`: new pathway, regulatory relationship, causal loop, cell-cell interaction, metabolic route, immune axis, or stress-response mechanism.
3. `new_molecule_type`: new class of mediator such as cytokine, receptor, metabolite, lipid mediator, lncRNA, circRNA, enzyme, transporter, PTM regulator, ECM factor, or extracellular vesicle cargo.
4. `new_experimental_method`: new model, perturbation, screen, omics assay, spatial method, organoid/co-culture system, direct binding assay, imaging assay, or validation ladder.
5. `new_bioinformatics_analysis`: new public-data strategy, single-cell/spatial analysis, multi-omics integration, network method, causal inference, perturbation signature, or patient-stratification analysis.

The user selects one innovation point or one family. That selected item becomes the current module.

## Stage Roles

| Stage | Skill | Main job | Required checkpoint |
|---|---|---|---|
| Innovation search | `$co-search` | Retrieve literature and classify innovation points into five module families | User chooses one module |
| Module planning | `$co-plan` | Convert the chosen module into a two-layer plan: node discovery plus validation, with rescue when testing a mediator | User approves plan or chooses route |
| Module result | `$co-result` | Write Results for the current module with discovery evidence and validation evidence, plus source ledger and raw-data needs | User decides next module or ends project |
| Final integration | `$co-result` | Integrate all closed modules into coherent manuscript Results | Only after user ends project |
| Methods | `$co-method` | Draft Methods from final Results panels | After Results are stable |
| Intro/Discussion | `$co-discussion` | Write literature-backed Introduction and Discussion | After Results are stable |
| Completion | `$co-completer` | Review, write/rewrite, judge readiness, and ask for final route | User chooses complete, branch, or new module loop |

## Removed Mainline Steps

`$co-distill` and `$co-topic` are no longer part of the main `$co-paper` route.

Why:

- A literature paper rarely offers a complete reusable biological research routine.
- Copying a full routine easily imports already-studied molecules or mechanisms.
- Useful literature borrowing is usually partial: one phenotype, one method, one molecular class, one analysis, or one validation trick.
- Topic generation should not happen as a one-shot global design. It should emerge from the selected module and the result of the previous module.

They can remain as standalone or legacy tools, but `$co-paper` should not call them unless the user explicitly asks.

## State and Provenance

Minimum state files:

- `project_state.md`: current biological question, current module, completed modules, active claims, and next decision.
- `decision_log.md`: user choices and why they mattered.
- `module_ledger.csv`: one row per module.
- `evidence_ledger.csv`: literature, public data, local analysis, wet-lab, virtual, and unresolved evidence.
- `source_mode_ledger.csv`: source mode for each result.

Suggested `module_ledger.csv` columns:

```text
module_id,relationship_type,parent_module_id,parallel_group,innovation_family,selected_innovation_point,biological_question,active_claim,discovery_status,validation_status,rescue_status,plan_file,result_file,source_modes,result_interpretation,next_downstream_options,user_decision,status
```

## Human Checkpoints

Stop for user choice unless the user explicitly asks for automatic continuation:

1. After `$co-search`: choose one innovation module from the five families.
2. After `$co-plan`: approve the module relationship and the two-layer plan, or choose analysis, experiment, virtual-result simulation, or revision.
3. Before `$co-result`: confirm whether both discovery and validation evidence are real, partial, assumed, explicitly virtual, or requirements-only.
4. Before virtual positive results: confirm source mode and direction for discovery, validation, rescue, or all layers.
5. After `$co-result`: decide whether the module is closed and whether the next module is downstream, upstream, parallel, or final assembly.
6. Before final manuscript assembly: confirm that all important module Results have source ledgers.
7. After `$co-completer`: choose `complete_project`, `dynamic_branch`, or `new_module_loop`.

## How Modules Progress

Example progression:

```text
Module 1: new phenotype
  -> co-search finds frontier phenotypes
  -> user chooses one phenotype
  -> co-plan designs a discovery layer to identify the phenotype and a validation layer to perturb/test it
  -> co-result writes phenotype Results with both layers

Module 2: downstream mechanism
  -> user asks what could explain the phenotype
  -> co-search finds mechanism innovation points
  -> user chooses one mechanism direction
  -> co-plan designs node discovery plus upstream perturbation/downstream readout validation
  -> co-result writes mechanism Results, including rescue if a mediator is claimed

Module 3: molecule or method, either downstream or parallel
  -> user chooses a molecular class or experimental method to deepen the mechanism
  -> repeat co-search -> co-plan -> co-result
```

This is a chain or graph of decisions, not a single global design. A new module can extend the prior one, look upstream, or run as a parallel branch, but each module still needs a discovery layer and a validation layer before it is treated as complete.

## How `$co-completer` Fits

`$co-completer` is used only after the user wants to end the project or after `manuscript/full_manuscript.md` is assembled.

It should produce:

- `manuscript/completion_review.md`
- `manuscript/completion_revision_plan.md`
- `manuscript/completion_decision_menu.md`
- marked revised Results or manuscript files if writing is performed
- `manuscript/project_completion_record.md` only after the user chooses `complete_project`

The completion menu should offer:

| Route | Meaning | Output |
|---|---|---|
| `complete_project` | Accept the current manuscript package as complete | `project_completion_record.md` |
| `dynamic_branch` | Resume from a prior module or manuscript checkpoint without overwriting current outputs | `branches/YYYYMMDD_<target>/` |
| `new_module_loop` | Start another downstream module | Return to `$co-search -> $co-plan -> $co-result` |

## Source-Mode Rules

Use conservative source labels:

- `real`: actual user-provided or computed result.
- `partial`: incomplete result; only write supported claims.
- `assumed`: user says to treat a result as true.
- `virtual_positive`: user explicitly asks for virtual, simulated, mock, or expected positive results.
- `requirements_only`: data are not available; write requirements, not Results.

Never invent positive Results without explicit user permission.

## Practical Trigger Prompt

```text
Use $co-paper

Topic seed: <biomedical topic>
Goal: 按模块递进，不要整体设计论文。先调用 co-search 检索文献，但只分类文献中的五类创新点：新表型、新机制、新分子类型、新实验方法、新生信分析。让我选择其中一个模块后，调用 co-plan 设计该模块，并标记它与既有模块是并列、上游还是下游关系。每个模块必须包含节点发现层和验证层：发现层用于筛出新东西，验证层用于干预上游并观察下游；如果验证中介，还要包含 rescue 或标记缺失。再根据真实结果、部分结果、假设结果或我明确允许的虚拟结果调用 co-result 写出该模块 Results。模块结束后让我决定下一下游/上游/并列模块，重复 co-search -> co-plan -> co-result。等我说结束整个项目后，再整合所有模块结果，调用 co-method、co-discussion，组装 full_manuscript.md，最后调用 co-completer。
```

## Default Language

Use Chinese for user-facing reports by default. If the manuscript itself is English, manuscript-facing revision text, Results, and figure legends should be English; project planning notes may remain Chinese unless the user requests otherwise.
