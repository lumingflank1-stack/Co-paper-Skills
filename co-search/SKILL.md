---
name: co-search
description: Search, screen, classify, and summarize biomedical literature into topic classes and evidence ledgers. Use when Codex needs to find papers, build literature matrices, compare directions, classify mechanisms, identify representative papers, or create a literature report for downstream co-distill or co-topic workflows. 用于文献检索、筛选、分类、代表论文选择和证据账本构建。
---

# Co-Search / 文献检索与分类

## Operating Goal / 运行目标

**English:** Retrieve, screen, classify, and summarize biomedical literature so the user can choose a research class for downstream routine distillation.

**中文：** 检索、筛选、分类并总结生物医学文献，让用户选择一个研究类别，供后续文章套路蒸馏使用。

Default to Chinese reports unless the user asks otherwise. Generated Markdown reports should be Chinese-only by default; do not create bilingual project reports unless explicitly requested.  
除非用户另有要求，报告默认使用中文。生成的 Markdown 报告默认只写中文；除非用户明确要求，不生成中英双语项目报告。

## Search Rules / 检索规则

**English:** Use current literature search unless the user provides a fixed corpus or forbids browsing. Prefer primary sources and structured databases.

**中文：** 除非用户提供固定文献集或禁止联网，否则使用当前文献检索。优先使用原始来源和结构化数据库。

- PubMed or Europe PMC for biomedical papers / 生物医学论文优先 PubMed 或 Europe PMC。
- BioRxiv or medRxiv only when preprints are allowed / 只有允许预印本时才使用 bioRxiv 或 medRxiv。
- Journal pages, DOI pages, and official database pages for metadata confirmation / 用期刊页、DOI 页和官方数据库页确认 metadata。
- Generic web search only as fallback for exact article pages / 通用网页搜索只作为定位文章页面的补充手段。

Honor user constraints exactly: journal set, date window, disease, cell type, species, method, paper type, and language.  
严格遵守用户约束：期刊范围、时间窗口、疾病、细胞类型、物种、方法、论文类型和语言。

## Workflow / 工作流

1. **EN:** Define the search question and constraints.  
   **中：** 明确检索问题和约束。
2. **EN:** Build fielded queries with synonyms, abbreviations, and exclusion terms.  
   **中：** 用同义词、缩写和排除词构建字段化检索式。
3. **EN:** Screen titles and abstracts against criteria.  
   **中：** 按纳入/排除标准筛选题目和摘要。
4. **EN:** Extract a literature matrix.  
   **中：** 提取文献矩阵。
5. **EN:** Classify papers by mechanism, model, node-discovery experiment, omics strategy, validation style, and article routine.  
   **中：** 按机制、模型、节点发现实验、组学策略、验证方式和文章套路分类。
6. **EN:** Pick representative papers for each class.  
   **中：** 为每一类选择代表论文。
7. **EN:** Save a report and ask the user to choose a class when used inside `$co-paper`.  
   **中：** 保存报告；在 `$co-paper` 中运行时，请用户选择一个类别。

Read `references/search_and_classification.md` for schemas and dimensions.  
读取 `references/search_and_classification.md` 获取输出格式和分类维度。

## Classification Dimensions / 分类维度

- Disease or biological context / 疾病或生物学背景。
- Cell type, tissue, organ, or model system / 细胞类型、组织、器官或模型系统。
- Molecular axis or pathway / 分子轴或通路。
- Omics or public-data strategy / 组学或公共数据策略。
- Node-discovery experiment: how the paper discovers downstream molecules, mechanism nodes, or phenotype-linked mediators / 节点发现实验：论文如何发现下游分子、机制节点或表型关联介质。
- Experimental validation ladder / 实验验证阶梯。
- Figure logic and article routine / 图版逻辑和文章套路。
- Novelty move: target, cell state, dataset integration, intervention, disease framing / 创新动作：新靶点、新细胞状态、新数据整合、新干预或新疾病框架。

## Evidence Discipline / 证据纪律

Separate / 区分：

- Literature observation / 文献观察。
- Author interpretation / 作者解释。
- Public database annotation / 公共数据库注释。
- Computational inference / 计算推断。
- Perturbation evidence / 扰动证据。
- Direct causal validation / 直接因果验证。

Do not treat Discussion claims as proven mechanisms unless Results directly validate them.  
除非 Results 中直接验证，否则不要把 Discussion 里的观点当作已证明机制。

## Required Outputs / 必要输出

Save in `01_search/` or the chosen directory / 保存到 `01_search/` 或指定目录：

- `search_strategy.md`
- `literature_matrix.csv`
- `topic_classes.md`
- `representative_papers.md`
- `evidence_ledger.csv`
- `exclusion_log.csv`

If search is blocked, still save `search_strategy.md` and `search_blockers.md`.  
如果检索受阻，仍需保存 `search_strategy.md` 和 `search_blockers.md`。
