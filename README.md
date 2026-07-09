# Co-Paper / 论文协作 Skill 集

## Overview / 概览

**English:** `co-paper` is the overall skill collection and top-level coordinator for modular biomedical paper building. It advances one research module at a time: literature innovation search, user-selected module planning, module Results writing, next-module decision, final manuscript assembly, completion review, and dynamic branching.

**中文：** `co-paper` 是这套“按模块递进”的生物医学论文工作流总入口。它一次只推进一个研究模块：文献创新点检索、用户选择模块、模块计划、模块 Results、下一模块决策、最终全文组装、完成审稿和动态分支。

**English:** This collection supersedes the earlier single `co-scientist` style skill. The recommended entry point is now `$co-paper`; `biomedical-co-scientist` is kept as a lower-level hypothesis and interpretation engine for compatibility.

**中文：** 这个 skill 集用于替代原来单一的 `co-scientist` 风格 skill。现在推荐入口是 `$co-paper`；`biomedical-co-scientist` 保留为底层假说生成和结果解释引擎，以便兼容已有用法。

**English:** The former `co-manager/` top-level workflow folder has been renamed to `co-paper/`; use `Use $co-paper` for new projects.

**中文：** 原来的顶层工作流文件夹 `co-manager/` 已改名为 `co-paper/`；新项目请使用 `Use $co-paper`。

**English:** `biomedical-co-scientist` is a Codex skill for biomedical research reasoning. It helps Codex generate competing mechanistic hypotheses, critique them, rank them, design bioinformatics analyses, interpret results conservatively, revise hypotheses, and propose wet-lab and translational validation plans.

**中文：** `biomedical-co-scientist` 是一个用于生物医学科研推理的 Codex skill。它帮助 Codex 生成竞争性机制假说、审稿式反驳、假说排序、设计生信分析、保守解释结果、迭代修正假说，并进一步提出实验验证和转化研究方案。

**English:** `co-method` is a Codex skill for drafting concise Chinese biomedical Methods sections from an abstract and results. It requires internet verification for specific reagents, antibodies, primer sequences, shRNA/siRNA/sgRNA target sequences, instruments, software versions, numbered software citations, catalog numbers, companies, and countries when those details are needed.

**中文：** `co-method` 是一个根据论文摘要和结果用中文精简撰写生物医学论文“材料与方法”的 Codex skill。它默认联网优先从中国公司补全特异性试剂、抗体、qPCR 引物、shRNA/siRNA/sgRNA 靶向序列、细胞系、仪器、软件版本、R 包/软件编号文献引用、货号、公司和国家，并按医学论文和 Nature-style 可复现写法输出。

**English:** `co-paper` is the upper-level modular paper workflow. It coordinates `co-search`, `co-plan`, `co-result`, `co-method`, `co-discussion`, and `co-completer`. `$co-search` classifies literature innovation points into five module families: new phenotype, new mechanism, new molecule type, new experimental method, and new bioinformatics analysis. The user chooses one module, `$co-plan` designs its relationship plus discovery and validation layers, `$co-result` closes it with both layers represented, and the user decides the next downstream/upstream/parallel module or final manuscript assembly.

**中文：** `co-paper` 是上层模块化论文工作流。它协调 `co-search`、`co-plan`、`co-result`、`co-method`、`co-discussion` 和 `co-completer`。`$co-search` 只按五类创新点分类：新表型、新机制、新分子类型、新实验方法、新生信分析。用户选择一个模块后，`$co-plan` 设计模块关系以及发现层和验证层，`$co-result` 在两层证据均被表示后结束该模块，再由用户决定下一下游/上游/并列模块或进入最终全文组装。

**English:** `co-completer` is a targeted workflow for strengthening an existing manuscript. It first performs independent reviewer-style critique, then proposes revision and supplement plans, waits for user approval, plans upstream/downstream or deeper mechanism work, recommends bioinformatics analyses and public datasets, recommends supplemental experiments and required data, and finally hands confirmed real, assumed, or explicitly approved virtual results to `co-result` for marked Results rewriting and Markdown/DOCX export.

**中文：** `co-completer` 面向已有论文的完整修改补强。它先进行独立审稿，再形成修改和补充建议，等待用户确认后，继续设计上下游或深入机制拓展、生信分析和公共数据集、补充实验和所需数据，最后把已确认的真实、假设或明确允许的虚拟结果交给 `co-result` 重写 Results，并导出带红色加粗标记的 Markdown 和 Word。

**English:** `wechat-med-literature` and `wechat-med-routine` form a public-account style workflow. The first skill searches and classifies recent high-impact biomedical papers for a user topic; after the user chooses a category, the second skill distills the research routine, generates two 16:9 figure assets, proposes three analogous topics, and exports a six-minute narration Word document.

**中文：** `wechat-med-literature` 和 `wechat-med-routine` 组成医学研究公众号工作流。第一个 skill 根据主题检索并分类近期高分医学论文；用户选择类别后，第二个 skill 分析科研套路，生成两张 16:9 示意图，提出 3 个类似课题，并导出 6 分钟口播 Word 文档。

## Core Workflow / 核心流程

**English:**

```text
Generate -> Debate -> Rank -> Test -> Analyze -> Revise -> Translate
```

**中文：**

```text
提出假说 -> 反驳假说 -> 排序假说 -> 设计验证 -> 分析数据 -> 修正假说 -> 转化应用
```

**Co-Paper workflow / Co-Paper 论文工作流：**

```text
co-search -> user selects one innovation module -> co-plan -> co-result
-> user chooses next downstream module or ends project
-> if continuing: repeat co-search -> co-plan -> co-result
-> if ending: final co-result -> co-method -> co-discussion
-> full manuscript -> co-completer
```

**WeChat medical research workflow / 医学公众号工作流：**

```text
wechat-med-literature -> user selects category -> wechat-med-routine
-> routine analysis + 16:9 figure -> 3 analogous topics + 16:9 figure
-> six-minute narration Word document
```

**Existing-manuscript revision workflow / 已有论文修改补强工作流：**

```text
co-completer -> independent review -> revision recommendations
-> user approval -> mechanism completion plan -> bioinformatics datasets and analyses
-> supplemental experiments and required data -> source-mode confirmation
-> co-result -> marked Results -> Markdown + DOCX export
```

## Default Output Rules / 默认输出规则

**English:** Unless the user explicitly requests English or bilingual output, every generated Markdown deliverable in `co-paper` and the WeChat medical workflow should be Chinese-only. This includes reports, category indexes, handoff files, routine analyses, figure prompt Markdown files, narration scripts, blocker notes, and captions. The final `manuscript/full_manuscript.md` should be one Chinese full manuscript by default, not parallel Chinese and English versions.

**中文：** 除非用户明确要求英文或中英双语，`co-paper` 和医学公众号工作流中所有生成的 Markdown 成品默认只写中文，包括报告、类别索引、交接文件、套路分析、图片提示词 Markdown、口播稿、阻断说明和图注。最终 `manuscript/full_manuscript.md` 默认只生成一个中文全文，不生成中英双语或中英文两套版本。论文原题、期刊名、基因/蛋白名、实验名、数据库/软件名、DOI、PMID、URL 和官方术语可保留原文。

**English:** For full Results packages, virtual-result packages, assumed-result manuscript packages, and `$co-paper` full-manuscript assembly, `$co-result` should call the available image generation path (`imagegen` / GPT Image 2 when available) by default to save complete multi-panel PNG figures. If generation is unavailable or blocked, save `figure_generation_prompts.md` and `figure_generation_blockers.md`.

**中文：** 对完整 Results 包、虚拟结果包、假设结果全文包和 `$co-paper` 全文组装，`$co-result` 默认调用可用图片生成路径（可用时使用 `imagegen` / GPT Image 2）生成完整 multi-panel PNG 图。若图片生成不可用或受阻，则保存 `figure_generation_prompts.md` 和 `figure_generation_blockers.md`。

**English:** When virtual or assumed positive results are requested, first perform a compact literature, public-data feasibility, and novelty scan unless the user fixes the result axis. Choose the result axis that is both highly plausible and maximally innovative, with no directly equivalent prior study found in the scanned literature; record closest prior work, the novelty difference, and remaining uncertainty in `virtual_result_rationale.md` or `assumed_result_explanation.md`. Virtual-result status is recorded in Markdown reports and source ledgers, not repeated in every paragraph, table, or figure legend.

**中文：** 当用户要求虚拟或假设阳性结果时，除非用户已经固定结果轴，否则先做一轮简洁的文献、公共数据可行性和创新性扫描；选择既高度可能成立、又最有创新性，且在已扫描文献中未见直接同构研究的结果轴；在 `virtual_result_rationale.md` 或 `assumed_result_explanation.md` 中记录最接近既往工作、创新性差异和剩余不确定性。虚拟结果状态只记录在 Markdown 报告和来源账本中，不在每段正文、每个表格或每条图注里反复标注。

**English:** For mechanism papers, every complete module should preserve two evidence jobs: (1) discovery experiments or analyses that find downstream molecules, mechanism nodes, phenotype-linked mediators, or analysis targets, often through omics, public data, screens, or high-throughput experiments; and (2) validation experiments that perturb the upstream/input side and observe the downstream/output side. If testing a mediator, include rescue or explicitly mark rescue as missing. Validation plans should consider decisive assays such as conditional knockout, tissue/cell-specific knockout, mass-spectrometry confirmation, SPR/BLI/ITC molecular interaction assays, Co-IP/CETSA/DARTS, rescue, and phenotype readouts.

**中文：** 对机制论文，每个完整模块都要保留两类证据功能：1）发现实验或分析，用组学、公共数据、筛选或高通量实验发现下游分子、机制节点、表型关联介质或分析目标；2）验证实验，干预上游/输入端并观察下游/输出端。如果验证中介，需要包含 rescue，或明确标记 rescue 缺失。验证计划应考虑关键实验，例如条件性敲除、组织/细胞特异性敲除、质谱确认、SPR/BLI/ITC 分子互作检测、Co-IP/CETSA/DARTS、rescue 和表型读出。

**English:** `$co-paper` does not use `$co-distill` or `$co-topic` in the active mainline. Literature can inspire one module at a time, but it should not produce a complete study design or reuse source-paper molecules as if they were new targets.

**中文：** `$co-paper` 主线不再使用 `$co-distill` 或 `$co-topic`。文献只能启发一个模块，不能直接产出完整研究设计，也不能把来源论文中已有分子当成新靶点复用。

**English:** After `manuscript/full_manuscript.md` is assembled, `$co-paper` should call `$co-completer` by default. `$co-completer` performs completion review and writing, judges rigor, novelty, newsworthiness, journal fit, evidence sufficiency, decisive missing experiments, and whether virtual or assumed results still block real submission. It then asks the user to choose: mark the project complete, dynamically branch/resume from an earlier checkpoint, or start a new downstream module loop through `$co-search -> $co-plan -> $co-result`.

**中文：** `manuscript/full_manuscript.md` 组装后，`$co-paper` 默认调用 `$co-completer`。`$co-completer` 负责完成审稿和写作，判断严谨性、创新性、新闻性、期刊匹配度、证据充分性、关键缺失实验，以及虚拟/假设结果是否仍然阻断真实投稿。随后让用户选择：标记项目完成；动态回跳/分支到早期节点；或启动新的下游模块循环 `$co-search -> $co-plan -> $co-result`。

**English:** For existing manuscripts, `$co-completer` must stop after revision recommendations and ask which changes to apply. It must also ask before generating virtual or simulated positive results. New or substantially revised manuscript-facing text is marked as red and bold in Markdown and Word.

**中文：** 对已有论文，`$co-completer` 必须在形成修改建议后暂停，询问用户采纳哪些建议；也必须在生成虚拟或模拟阳性结果前再次确认。新增或实质重写的论文正文内容在 Markdown 和 Word 中用红色加粗标记。

## When To Use / 什么时候使用

**English:** Use this skill when you want Codex to:

- Generate biomedical mechanisms from an observation.
- Compare several competing hypotheses instead of giving one answer.
- Critique correlation, confounding, and alternative explanations.
- Design single-cell, bulk RNA-seq, multi-omics, or pathway analyses.
- Design node-discovery experiments that identify downstream molecules, mechanism nodes, or phenotype-linked mediators.
- Interpret analysis results and revise mechanisms.
- Design wet-lab validation, perturbation, rescue, mass-spectrometry, molecular interaction, or translational experiments.
- Frame a project as a manuscript, grant, or figure plan.

**中文：** 当你希望 Codex 做下面这些事时使用：

- 根据科研现象提出机制假说。
- 同时比较多个竞争性假说，而不是只给一个结论。
- 主动质疑相关性、混杂因素和替代解释。
- 设计单细胞、bulk RNA-seq、多组学或通路分析。
- 设计发现下游分子、机制节点或表型关联介质的节点实验。
- 根据分析结果解释证据，并修正机制假说。
- 设计湿实验验证、扰动、rescue、质谱、分子互作或转化实验。
- 把课题整理成论文、基金或图版逻辑。

## How To Trigger / 如何触发

**English:** In a new Codex conversation, explicitly invoke the skill:

```text
Use $biomedical-co-scientist to generate, critique, rank, and test hypotheses for my biomedical project.
```

**中文：** 在新的 Codex 对话里，可以显式触发：

```text
Use $biomedical-co-scientist 帮我围绕这个生物医学课题提出假说、反驳假说、排序并设计验证分析。
```

You can also describe the task naturally:

也可以自然语言触发：

```text
用 biomedical-co-scientist skill 分析这个现象，并提出可证伪的机制假说和生信验证方案。
```

For Methods drafting:

Methods 部分撰写可这样触发：

```text
Use $co-method 根据下面的摘要和结果，用中文精简撰写材料与方法；联网优先从中国公司补齐抗体、qPCR 引物、siRNA/shRNA、细胞系、试剂、仪器、软件版本和 R 包/软件的编号文献引用。
```

For choosing the right `co-paper` entry point:

选择 `co-paper` 子技能入口时，可按任务类型触发：

- 想做完整论文工作流：说 `Use $co-paper`，最好。
- 想按五类创新点检索文献：说 `Use $co-search`。
- 想做公共数据或实验计划：说 `Use $co-plan`。
- 有结果或明确要虚拟结果：说 `Use $co-result`。
- 写 Methods：说 `Use $co-method`。
- 写 Introduction/Discussion：说 `Use $co-discussion`。
- 已有论文需要审稿、修改补强、生信和实验补充、重写 Results 并导出 Word：说 `Use $co-completer`。

For the full interactive paper workflow:

完整互动式论文工作流可这样触发：

```text
Use $co-paper

Topic seed: macrophage metabolism and osteoarthritis
Goal: 按模块递进，不要整体设计论文。先调用 co-search 检索文献，但只分类文献中的五类创新点：新表型、新机制、新分子类型、新实验方法、新生信分析。让我选择其中一个模块后，调用 co-plan 设计模块关系、节点发现层和验证层；发现层用于筛出新东西，验证层用于干预上游并观察下游，如果验证中介要包含 rescue 或标记缺失。根据真实结果、部分结果、假设结果或我明确允许的虚拟结果调用 co-result 写出该模块 Results，Results 中也要同时包含发现层和验证层。模块结束后让我决定下一下游/上游/并列模块，重复 co-search -> co-plan -> co-result。等我说结束整个项目后，再整合所有模块结果，调用 co-method、co-discussion，组装 full_manuscript.md，最后调用 co-completer。
Output defaults: 每一步 Markdown 默认中文；full_manuscript.md 只给一个中文全文；虚拟结果前先调研文献、公共数据可行性和创新性，选择既可能成立又最创新、未见直接同构研究的阳性结果轴并保存解释文件；图片生成可用时生成 Figure PNG。
Completion: 全文完成后调用 co-completer，生成 completion_review.md、completion_revision_plan.md 和 completion_decision_menu.md；然后让我选择标记项目完成、动态回跳/分支，或启动新的下游模块循环 co-search -> co-plan -> co-result。
```

For the medical research public-account workflow:

医学研究公众号工作流可这样触发：

```text
Use $wechat-med-literature

Topic: osteoarthritis macrophage metabolism
Goal: 调研近1年10分以上论文并分类；同时调研近半年20分以上论文并分类；导出两个 Markdown 报告和类别索引。所有 Markdown 成品默认中文。完成后让我选择一个类别，不要直接进入套路分析。
```

After selecting a category:

选择类别后继续：

```text
Use $wechat-med-routine

Selected category: C1 - macrophage metabolic checkpoint
Source folder: outputs/wechat_med/<topic>/<date>/01_literature
Goal: 分析该类别科研套路，重点分析创新表型、机制、节点发现实验和验证实验；生成两张16:9图；提出3个类似课题；导出6分钟口播Word。所有 Markdown 成品默认中文。
```

For revising an existing manuscript:

已有论文修改补强可这样触发：

```text
Use $co-completer

Manuscript: /path/to/manuscript.docx
Figures: /path/to/figures
Target: 预投稿或大修前补强
Goal: 先独立审稿，不要直接改稿；形成修改和补充建议后让我确认。确认后，请提出上下游和深入机制研究方案，先给出生信分析建议和可用公共数据集，再给出补充实验数据需求和可用数据集。最后根据我提供或明确允许模拟的结果调用 co-result 重写 Results，新增或实质修改内容用红色加粗标记，并导出 Markdown 和 Word。
```

## Recommended Test Prompt / 推荐测试 Prompt

**English:**

```text
Use $biomedical-co-scientist

Project: FICT1 in simulated inflammatory macrophage activation
Observation: In a toy single-cell dataset, the fictional gene FICT1 is upregulated in stimulated macrophages and positively correlated with MOCK2, ANTIGEN-A, and ANTIGEN-B. A proxy perturbation analysis suggests MOCK2 may be a downstream candidate.
Goal: Generate 5 competing mechanistic hypotheses. For each hypothesis, include evidence, weaknesses, alternative explanations, bioinformatics validation, falsification criteria, wet-lab validation, translational value, and a ranking table.
```

**中文：**

```text
Use $biomedical-co-scientist

Project: FICT1 in simulated inflammatory macrophage activation
Observation: 在一个虚拟单细胞数据集中，虚构基因 FICT1 在刺激后的巨噬细胞中上调，并与 MOCK2、ANTIGEN-A、ANTIGEN-B 正相关；proxy perturbation 分析提示 MOCK2 可能是下游候选。
Goal: 请生成 5 个竞争性机制假说。每个假说都要包含证据、漏洞、替代解释、生信验证、关键证伪标准、实验验证和转化价值，并给出排序表。
```

**Co-Method test prompt / Co-Method 测试 Prompt：**

```text
Use $co-method

Task: 根据下面虚构论文的摘要和结果撰写 Methods。
Abstract: FICT1 knockdown attenuated inflammatory activation in a simulated macrophage model.
Results: (1) FICT1 shRNA reduced FICT1 mRNA and protein expression. (2) LPS-induced IL6 and TNF expression decreased after FICT1 knockdown. (3) Immunofluorescence showed reduced nuclear p65 signal. (4) RNA-seq identified downregulation of NF-kappaB-related genes.
Requirements: 用中文精简撰写材料与方法；默认只输出正文、软件参考文献和高风险需作者核对；联网优先搜索中国官方供应商/厂家页面；抗体优先武汉三鹰/Proteintech，qPCR 引物优先上海生工生物，细胞系优先中科院上海细胞库，常规试剂优先正能生物等中国供应商；抗体、引物、siRNA/shRNA 序列、试剂盒、仪器、软件在物品后用括号写货号/公司/国家/版本；R 包或软件用 [1]、[2] 形式编号引用相关方法论文或官方 citation；没有现成序列时给出设计候选序列。
```

## Data Analysis Prompt / 数据分析 Prompt

**English:**

```text
Use $biomedical-co-scientist

I have a toy single-cell dataset at /path/to/data.rds. First inspect the data structure, then design and run donor-level pseudobulk, module score, partial correlation, and visualization analyses around the fictional FICT1-MOCK2-macrophage axis. After analysis, revise the original hypotheses based on the results.
```

**中文：**

```text
Use $biomedical-co-scientist

我有一个虚拟单细胞数据在 /path/to/data.rds。请先检查数据结构，然后围绕虚构的 FICT1-MOCK2-巨噬细胞轴设计并执行 donor-level pseudobulk、module score、partial correlation 和可视化分析。分析完成后，根据结果修正原始假说。
```

## Repository Layout / 仓库结构

```text
co-method/
├── SKILL.md
├── agents/
│   └── openai.yaml
└── references/
    ├── medical_methods_format.md
    ├── output_templates.md
    ├── reagent_search.md
    └── software_citation.md

biomedical-co-scientist/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── hypothesis_framework.md
│   ├── bioinformatics_analysis.md
│   └── iteration_translation.md
└── scripts/
    └── scaffold_report.py

co-paper/
├── SKILL.md
├── agents/
├── references/
└── scripts/

co-completer/
├── SKILL.md
├── agents/
├── references/
└── scripts/

co-search/
co-plan/
co-result/
co-discussion/
wechat-med-literature/
wechat-med-routine/
```

**English:**

- `SKILL.md`: Main trigger description and operating workflow.
- `references/hypothesis_framework.md`: Hypothesis cards, evidence tiers, critique, and scoring.
- `references/bioinformatics_analysis.md`: Bioinformatics analysis patterns and decision rules.
- `references/iteration_translation.md`: Result interpretation, hypothesis revision, validation, translation, and manuscript framing.
- `scripts/scaffold_report.py`: Creates a reusable report scaffold for a project.
- `co-method/SKILL.md`: Main workflow for concise Chinese biomedical Methods drafting.
- `co-method/references/reagent_search.md`: Internet-search rules for exact reagents, sequences, catalog numbers, companies, and countries.
- `co-method/references/software_citation.md`: Numbered citation rules for R packages, software, databases, and command-line tools.
- `co-method/references/medical_methods_format.md`: Medical/Nature-style Methods structure and reproducibility rules.
- `co-method/references/output_templates.md`: Concise Chinese draft skeletons, indexes, ledgers, and reusable prompt.
- `co-paper/SKILL.md`: Upper-level orchestration for multi-round literature-to-paper workflows.
- `co-search/SKILL.md`: Literature retrieval, screening, classification, and representative paper selection.
- `co-plan/SKILL.md`: Public dataset, bioinformatics, experiment, and virtual-result prompt planning.
- `co-result/SKILL.md`: Results writing from input results or explicitly requested simulated results.
- `co-discussion/SKILL.md`: Literature-backed Introduction and Discussion writing with numbered citations.
- `co-completer/SKILL.md`: Existing-manuscript review, approved revision planning, mechanism completion, bioinformatics and experiment supplements, marked Results rewriting, and Markdown/DOCX export.
- `wechat-med-literature/SKILL.md`: Topic-based recent high-impact biomedical paper retrieval, classification, and Markdown export.
- `wechat-med-routine/SKILL.md`: Selected-category routine analysis, figure generation, analogous topic generation, and six-minute narration DOCX export.

**中文：**

- `SKILL.md`：主触发描述和工作流程。
- `references/hypothesis_framework.md`：假说卡、证据分层、反驳和评分规则。
- `references/bioinformatics_analysis.md`：生信分析模式和判断标准。
- `references/iteration_translation.md`：结果解释、假说修正、实验验证、转化和论文基金框架。
- `scripts/scaffold_report.py`：为项目生成可复用的报告骨架。
- `co-method/SKILL.md`：中文精简撰写材料与方法的主流程。
- `co-method/references/reagent_search.md`：联网核对试剂、序列、货号、公司和国家的规则。
- `co-method/references/software_citation.md`：R 包、软件、数据库和命令行工具的编号文献引用规则。
- `co-method/references/medical_methods_format.md`：医学论文和 Nature-style Methods 结构与可复现写法。
- `co-method/references/output_templates.md`：中文精简草稿骨架、索引表、证据表和可复用 prompt。
- `co-paper/SKILL.md`：多轮“文献到论文”工作流总控。
- `co-search/SKILL.md`：文献检索、筛选、分类和代表论文选择。
- `co-plan/SKILL.md`：规划公共数据集、生信分析、实验验证和虚拟结果 prompt。
- `co-result/SKILL.md`：基于输入结果或明确要求的模拟结果撰写 Results。
- `co-discussion/SKILL.md`：先调研文献，再用编号引用撰写 Introduction 和 Discussion。
- `co-completer/SKILL.md`：已有论文审稿、确认后修改补强、机制完善、生信和实验补充、带标记重写 Results，并导出 Markdown/DOCX。
- `wechat-med-literature/SKILL.md`：按主题检索近期高分医学论文，分类并导出 Markdown。
- `wechat-med-routine/SKILL.md`：对选定类别做套路分析、生成示意图、生成类似课题并导出 6 分钟口播 Word。

## Report Scaffold Script / 报告骨架脚本

**English:** Create a structured workspace for a new hypothesis project:

```bash
python biomedical-co-scientist/scripts/scaffold_report.py \
  --project "FICT1 macrophage toy project" \
  --out outputs/co_scientist/fict1-macrophage-toy \
  --hypotheses 5
```

**中文：** 为一个新的假说项目生成结构化输出目录：

```bash
python biomedical-co-scientist/scripts/scaffold_report.py \
  --project "FICT1 macrophage toy project" \
  --out outputs/co_scientist/fict1-macrophage-toy \
  --hypotheses 5
```

The script creates:

脚本会生成：

- `hypothesis_cards.md`
- `analysis_plan.md`
- `final_report.md`
- `evidence_ledger.csv`
- `prioritization.csv`

**Co-Paper project scaffold / Co-Paper 项目骨架：**

```bash
python co-paper/scripts/scaffold_project.py \
  --project "macrophage metabolism OA paper" \
  --out outputs/co_paper/macrophage-metabolism-oa \
  --rounds 2
```

This creates state ledgers, stage folders, round folders, and a manuscript folder.

该脚本会生成状态记录、阶段目录、迭代轮次目录和 manuscript 目录。

## Installation / 安装

**English:** This repository is designed as a Codex skill collection. The top-level coordinator folder is now `co-paper/`. To install globally, copy each skill directory into `~/.codex/skills/`:

```bash
cp -R biomedical-co-scientist ~/.codex/skills/biomedical-co-scientist
cp -R co-method ~/.codex/skills/co-method
cp -R co-paper ~/.codex/skills/co-paper
cp -R co-search ~/.codex/skills/co-search
cp -R co-plan ~/.codex/skills/co-plan
cp -R co-result ~/.codex/skills/co-result
cp -R co-discussion ~/.codex/skills/co-discussion
cp -R co-completer ~/.codex/skills/co-completer
cp -R wechat-med-literature ~/.codex/skills/wechat-med-literature
cp -R wechat-med-routine ~/.codex/skills/wechat-med-routine
```

**中文：** 这个仓库是 Codex skill 集合。顶层总控文件夹现在是 `co-paper/`。全局安装时，将各个 skill 目录复制到 `~/.codex/skills/`：

```bash
cp -R biomedical-co-scientist ~/.codex/skills/biomedical-co-scientist
cp -R co-method ~/.codex/skills/co-method
cp -R co-paper ~/.codex/skills/co-paper
cp -R co-search ~/.codex/skills/co-search
cp -R co-plan ~/.codex/skills/co-plan
cp -R co-result ~/.codex/skills/co-result
cp -R co-discussion ~/.codex/skills/co-discussion
cp -R co-completer ~/.codex/skills/co-completer
cp -R wechat-med-literature ~/.codex/skills/wechat-med-literature
cp -R wechat-med-routine ~/.codex/skills/wechat-med-routine
```

## Validation / 验证

**English:** Validate the skill with Codex's skill creator validator:

```bash
UV_CACHE_DIR=/tmp/uv-skill-validate-cache \
uv run --with pyyaml \
python ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py biomedical-co-scientist
UV_CACHE_DIR=/tmp/uv-skill-validate-cache \
uv run --with pyyaml \
python ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py co-method
UV_CACHE_DIR=/tmp/uv-skill-validate-cache \
uv run --with pyyaml \
python ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py co-paper
UV_CACHE_DIR=/tmp/uv-skill-validate-cache \
uv run --with pyyaml \
python ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py co-search
UV_CACHE_DIR=/tmp/uv-skill-validate-cache \
uv run --with pyyaml \
python ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py co-plan
UV_CACHE_DIR=/tmp/uv-skill-validate-cache \
uv run --with pyyaml \
python ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py co-result
UV_CACHE_DIR=/tmp/uv-skill-validate-cache \
uv run --with pyyaml \
python ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py co-discussion
UV_CACHE_DIR=/tmp/uv-skill-validate-cache \
uv run --with pyyaml \
python ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py co-completer
UV_CACHE_DIR=/tmp/uv-skill-validate-cache \
uv run --with pyyaml \
python ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py wechat-med-literature
UV_CACHE_DIR=/tmp/uv-skill-validate-cache \
uv run --with pyyaml \
python ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py wechat-med-routine
```

**中文：** 使用 Codex 的 skill creator validator 验证：

```bash
UV_CACHE_DIR=/tmp/uv-skill-validate-cache \
uv run --with pyyaml \
python ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py biomedical-co-scientist
UV_CACHE_DIR=/tmp/uv-skill-validate-cache \
uv run --with pyyaml \
python ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py co-method
UV_CACHE_DIR=/tmp/uv-skill-validate-cache \
uv run --with pyyaml \
python ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py co-paper
UV_CACHE_DIR=/tmp/uv-skill-validate-cache \
uv run --with pyyaml \
python ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py co-search
UV_CACHE_DIR=/tmp/uv-skill-validate-cache \
uv run --with pyyaml \
python ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py co-plan
UV_CACHE_DIR=/tmp/uv-skill-validate-cache \
uv run --with pyyaml \
python ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py co-result
UV_CACHE_DIR=/tmp/uv-skill-validate-cache \
uv run --with pyyaml \
python ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py co-discussion
UV_CACHE_DIR=/tmp/uv-skill-validate-cache \
uv run --with pyyaml \
python ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py co-completer
UV_CACHE_DIR=/tmp/uv-skill-validate-cache \
uv run --with pyyaml \
python ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py wechat-med-literature
UV_CACHE_DIR=/tmp/uv-skill-validate-cache \
uv run --with pyyaml \
python ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py wechat-med-routine
```

## Scientific Guardrails / 科学约束

**English:**

- Do not treat correlation as causation.
- Always include alternative explanations.
- Always define falsification criteria.
- Separate observation, association, network inference, perturbation evidence, and causal validation.
- Prefer donor-level or sample-level evidence over cell-level-only associations.
- Treat pathway enrichment, GRN, ligand-receptor, proxy knockout, and CMap results as hypothesis-generating unless directly validated.

**中文：**

- 不把相关性当作因果关系。
- 每个假说都必须包含替代解释。
- 每个假说都必须给出证伪标准。
- 区分观察现象、相关性、网络推断、扰动证据和因果验证。
- 优先使用 donor-level 或 sample-level 证据，而不是只依赖 cell-level 相关。
- 通路富集、GRN、配体-受体、proxy KO、CMap 等结果默认作为假说生成证据，除非有直接验证。
