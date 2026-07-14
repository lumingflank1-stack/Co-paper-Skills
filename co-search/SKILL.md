---
name: co-search
description: "Search, screen, and summarize biomedical literature by innovation points rather than complete paper routines. Use in co-paper to classify innovations into five module families, then stop for the user to choose one module for co-debate. Do not hand off directly to co-plan. 用于文献检索并按新表型、新机制、新分子类型、新实验方法和新生信分析五类创新点分类；用户选定模块后交给 co-debate，而不是直接进入 co-plan。"
---

# Co-Search / 文献创新点检索

## Operating Goal / 运行目标

**English:** Retrieve, screen, and summarize biomedical literature so the user can choose one innovation module for downstream `$co-debate`. Do not classify whole papers into complete article routines for `$co-paper` and do not generate the final hypothesis ranking here.

**中文：** 检索、筛选并总结生物医学文献，让用户从文献创新点中选择一个模块进入 `$co-debate`。本阶段不生成最终假说排名，也不直接进入 `$co-plan`。

Default to Chinese reports unless the user asks otherwise. Generated Markdown reports should be Chinese-only by default; do not create bilingual project reports unless explicitly requested.  
除非用户另有要求，报告默认使用中文。生成的 Markdown 报告默认只写中文；除非用户明确要求，不生成中英双语项目报告。

## Search Rules / 检索规则

Use current literature search unless the user provides a fixed corpus or forbids browsing. Prefer primary sources and structured databases.

- PubMed or Europe PMC for biomedical papers / 生物医学论文优先 PubMed 或 Europe PMC。
- BioRxiv or medRxiv only when preprints are allowed / 只有允许预印本时才使用 bioRxiv 或 medRxiv。
- Journal pages, DOI pages, and official database pages for metadata confirmation / 用期刊页、DOI 页和官方数据库页确认 metadata。
- Generic web search only as fallback for exact article pages / 通用网页搜索只作为定位文章页面的补充手段。

Honor user constraints exactly: journal set, date window, disease, cell type, species, method, paper type, and language.  
严格遵守用户约束：期刊范围、时间窗口、疾病、细胞类型、物种、方法、论文类型和语言。

## Workflow / 工作流

1. Define the search question and constraints.
2. Build fielded queries with synonyms, abbreviations, and exclusion terms.
3. Screen titles and abstracts against criteria.
4. Extract a literature matrix.
5. Extract innovation points from each relevant paper.
6. Classify innovation points into five module families:
   - `new_phenotype`
   - `new_mechanism`
   - `new_molecule_type`
   - `new_experimental_method`
   - `new_bioinformatics_analysis`
7. Save a module-oriented report and ask the user to choose one innovation module when used inside `$co-paper`.
8. After selection, save a concise `co_debate_handoff.md` containing the selected module, evidence pointers, prior-module relationship, and unresolved questions; hand off to `$co-debate`.

Read `references/search_and_classification.md` for schemas and dimensions.  
读取 `references/search_and_classification.md` 获取输出格式和分类维度。

## Innovation Families / 五类创新点

- `new_phenotype`: disease phenotype, cell state, spatial pattern, pathological process, clinical subgroup, or functional readout.
- `new_mechanism`: pathway, causal loop, cell-cell interaction, metabolic route, immune axis, stress response, transcriptional regulation, epigenetic regulation, or PTM logic.
- `new_molecule_type`: molecule class rather than necessarily one named target, such as cytokine, receptor, metabolite, lipid mediator, lncRNA, circRNA, enzyme, transporter, PTM regulator, ECM factor, or extracellular vesicle cargo.
- `new_experimental_method`: model, perturbation, screen, omics assay, spatial method, organoid/co-culture system, direct binding assay, imaging assay, or validation ladder.
- `new_bioinformatics_analysis`: public-data strategy, single-cell/spatial analysis, multi-omics integration, network method, causal inference, perturbation signature, or patient-stratification analysis.

## Evidence Discipline / 证据纪律

Separate:

- Literature observation.
- Author interpretation.
- Public database annotation.
- Computational inference.
- Perturbation evidence.
- Direct causal validation.

Do not treat Discussion claims as proven mechanisms unless Results directly validate them.  
除非 Results 中直接验证，否则不要把 Discussion 里的观点当作已证明机制。

## Required Outputs / 必要输出

Save in `01_search/` or the chosen directory:

- `search_strategy.md`
- `literature_matrix.csv`
- `innovation_points.md`
- `innovation_point_matrix.csv`
- `module_options.md`
- `evidence_ledger.csv`
- `exclusion_log.csv`
- `co_debate_handoff.md` after the user selects a module

If search is blocked, still save `search_strategy.md` and `search_blockers.md`.  
如果检索受阻，仍需保存 `search_strategy.md` 和 `search_blockers.md`。
