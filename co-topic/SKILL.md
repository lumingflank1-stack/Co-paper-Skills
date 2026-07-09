---
name: co-topic
description: Generate and rank biomedical research topics from a distilled paper routine, evidence ledger, disease context, public-data availability, and validation feasibility. Use when Codex needs to transform co-distill output into candidate hypotheses, mechanisms, figure plans, topic cards, falsification criteria, or manuscript-ready project concepts. 用于基于文章套路生成、反驳和排序新课题。
---

# Co-Topic / 课题生成

## Operating Goal / 运行目标

**English:** Generate testable biomedical topic skeletons from a distilled article routine. Adapt the co-scientist loop to topic generation: generate, critique, rank, test, revise, and translate. When the core target or mechanism molecule has not been discovered in this project, represent it as `???` rather than naming a molecule already studied by the source papers.

**中文：** 从蒸馏出的文章套路中生成可检验的生物医学课题骨架。把共同科学家循环应用到选题：生成、反驳、排序、验证设计、修正和转化表达。当本项目尚未发现核心靶点或机制分子时，用 `???` 占位，而不是直接命名来源论文已经研究过的分子。

Default to Chinese reports unless the user requests another language. Generated Markdown reports should be Chinese-only by default; do not create bilingual project reports unless explicitly requested.  
除非用户要求其他语言，报告默认使用中文。生成的 Markdown 报告默认只写中文；除非用户明确要求，不生成中英双语项目报告。

## Inputs / 输入

- `routine_distillation.md` from `$co-distill` / `$co-distill` 生成的 `routine_distillation.md`。
- `evidence_ledger.csv` and selected literature class from `$co-search` / `$co-search` 的证据账本和选定文献类别。
- User constraints: disease, cell type, public data, model, intervention, journal, feasibility / 用户约束：疾病、细胞类型、公共数据、模型、干预方式、目标期刊和可行性。

## Workflow / 工作流

1. **EN:** Restate the distilled routine in one sentence.  
   **中：** 用一句话重述蒸馏出的文章套路。
2. **EN:** Generate 3-5 candidate topic skeletons that reuse the routine but change the biological question enough to be novel. If the core molecule is not project-discovered, write it as `???` and give only family-level or module-level hints.
   **中：** 生成 3-5 个候选课题骨架，复用套路但更换足够新的生物学问题。如果核心分子还不是本项目发现的，写成 `???`，只给家族级或模块级提示。
3. **EN:** For each topic, build a card with phenotype-level mechanism, `???` discovery slot, public datasets, bioinformatics tests, node-discovery experiments, validation experiments, figure plan, and falsification criteria.
   **中：** 为每个课题建立卡片，包含表型层机制、`???` 发现槽位、公共数据集、生信测试、节点发现实验、验证实验、图版计划和证伪标准。
4. **EN:** Critique each topic as a skeptical reviewer.  
   **中：** 像审稿人一样质疑每个课题。
5. **EN:** Rank topics by novelty, evidence, feasibility, causal testability, public-data availability, and manuscript potential.  
   **中：** 按新颖性、证据、可行性、因果可检验性、公共数据可用性和成文潜力排序。
6. **EN:** Recommend one primary topic and one backup topic.  
   **中：** 推荐一个主课题和一个备选课题。
7. **EN:** Save topic files and ask the user to choose when running inside `$co-paper`.  
   **中：** 保存课题文件；在 `$co-paper` 中运行时请用户选择。

Read `references/topic_schema.md` for schemas.  
读取 `references/topic_schema.md` 获取课题卡和排序表格式。

## Scientific Rules / 科学规则

- **EN:** Generate competing topics, not minor variants of the same axis.  
  **中：** 生成相互竞争的课题，而不是同一轴线的小变体。
- **EN:** Keep causal wording conservative until perturbation or rescue evidence exists.  
  **中：** 在没有扰动或 rescue 证据前，因果表述保持保守。
- **EN:** Include at least one null or confounding explanation for each topic.  
  **中：** 每个课题至少包含一个零假说或混杂解释。
- **EN:** Define what result would weaken or falsify each topic.  
  **中：** 明确什么结果会削弱或证伪该课题。
- **EN:** Distinguish public-data support from wet-lab causal validation.  
  **中：** 区分公共数据支持和湿实验因果验证。
- **EN:** Do not copy the source routine mechanically, but preserve the evidence jobs: every serious topic should specify how the downstream mechanism node or phenotype-linked mediator will be discovered, and how that node will then be validated.  
  **中：** 不要求生硬模仿来源套路，但必须保留证据功能：每个成熟课题都要说明如何发现下游机制节点或表型关联介质，以及随后如何验证该节点。
- **EN:** Use `???` for unresolved core molecules. Do not promote already-studied source-paper molecules, close prior targets, or obvious literature hits as the new topic's core target. Exact names may appear only in `known molecules to avoid`, positive controls, rationale, or validation comparator sections until this project discovers and filters a candidate.
  **中：** 未解析的核心分子必须使用 `???`。不要把来源论文已经研究过的分子、相近既往靶点或显而易见的文献命中直接提升为新课题核心靶点。在本项目通过发现和创新性过滤前，具体名称只能出现在“应避免的已知分子”、阳性对照、理由说明或验证比较项中。
- **EN:** Validation sections should name decisive validation experiments, not just say "validate". Consider conditional knockout or cell/tissue-specific knockout, mass-spectrometry confirmation, SPR/BLI/ITC molecular interaction assays, Co-IP/CETSA/DARTS, rescue, and phenotype readouts where appropriate.  
  **中：** 验证部分不能只写“验证”，要写出关键验证实验。根据课题需要考虑条件性敲除或细胞/组织特异性敲除、质谱确认、SPR/BLI/ITC 分子互作检测、Co-IP/CETSA/DARTS、rescue 和表型读出。

## Required Outputs / 必要输出

Save in `03_topics/` or the requested directory / 保存到 `03_topics/` 或指定目录：

- `topic_cards.md`
- `topic_prioritization.csv`
- `figure_plan.md`
- `dataset_needs.csv`
- `node_discovery_plan.md`
- `experiment_needs.md`
- `falsification_plan.md`
- `topic_selection_brief.md`

If no topic is mature enough, save `topic_failure_modes.md` and propose how to rerun `$co-search` or `$co-distill`.  
如果没有足够成熟的课题，保存 `topic_failure_modes.md`，并建议如何重跑 `$co-search` 或 `$co-distill`。
