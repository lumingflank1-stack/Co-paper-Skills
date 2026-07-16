---
name: co-method
description: Draft concise, reproducible biomedical Methods after co-result and prepare a structured handoff for co-discussion. Use in co-paper after Results stabilize to map every bioinformatics exploration, experimental validation, and bioinformatics validation panel to datasets, samples, assays, reagents, instruments, software, statistics, ethics, and reproducibility details, then save manuscript/methods.md and co_discussion_handoff.md.
---

# Co-Method / 方法部分撰写

## Operating Goal / 运行目标

**English:** Write Methods as a concise reproducibility document, not a narrative summary. Start from the user's abstract and results, infer required experiments, then verify method-specific details from user files or internet sources before drafting.

**中文：** 将 Methods 写成简洁的可复现文档，而不是叙事总结。先根据摘要和结果反推需要的方法模块，再从用户文件或网络来源核对具体实验细节。

Default to concise Chinese manuscript prose unless the user requests another language. Generated Markdown reports and manuscript inputs should be Chinese-only by default; do not create bilingual project reports unless explicitly requested.  
除非用户要求其他语言，默认使用精简中文论文正文。生成的 Markdown 报告和全文输入默认只写中文；除非用户明确要求，不生成中英双语项目报告。

Default output / 默认输出：

- **EN:** Methods正文, essential software references, and a short `高风险需作者核对` note.  
  **中：** Methods 正文、必要软件参考文献，以及简短的 `高风险需作者核对`。
- **EN:** Full maps, ledgers, reagent tables, and audit tables only when requested or when needed for reproducibility.  
  **中：** 只有用户要求或复现性需要时，才输出完整结果-方法映射、检索账本、试剂表和审计表。

## Core Workflow / 核心流程

1. **EN:** Extract study design, biological system, interventions, comparisons, assays, datasets, and statistics from all provided material.  
   **中：** 从摘要、结果、图、图注、表格和笔记中提取研究设计、生物系统、干预、比较、实验、数据集和统计方法。
2. **EN:** Build a result-to-method map; each result panel or claim must map to a method subsection, sample source, assay, instrument, reagent set, analysis step, and statistical test.  
   **中：** 建立结果-方法映射；每个结果 panel 或 claim 都要对应方法小节、样本来源、实验、仪器、试剂、分析步骤和统计检验。
3. **EN:** Identify missing details, then actively fill them by internet search and domain-standard reagent selection when a reasonable citable option exists.  
   **中：** 先识别缺失信息；若存在合理且可引用的商业试剂、引物、siRNA/shRNA、细胞系或软件引用，应主动联网补齐。
4. **EN:** Search exact materials and metadata whenever catalog numbers, sequences, manufacturers, instrument vendors, or software versions are missing. Prefer Chinese official suppliers first.  
   **中：** 当缺少货号、序列、厂家、仪器厂商或软件版本时，联网核对精确信息。优先使用中国官方供应商。
5. **EN:** Draft concise Methods with searched candidate materials in prose, appending only essential references and high-risk unresolved details.  
   **中：** 用已检索候选材料撰写精简 Methods，仅附必要参考文献和高风险待核对信息。
6. **EN:** Run a reproducibility audit and remove vague phrases when concrete parameters can be supplied.  
   **中：** 做复现性审计；凡能替换成具体参数、来源或标识符的模糊表达都要替换。

## Reference Loading / 参考文件加载

## Co-Paper Handoff Contract

In the Co-Paper route, run `$co-method` immediately after `$co-result`.

Required inputs:

- `three_module_results_section.md`
- Figure legends and `claim_panel_map.csv`
- `module_evidence_map.md` and `result_source_ledger.md`
- `raw_data_requirements_summary.md`
- `methods_input.md`

Required handoff outputs:

- `manuscript/methods.md`
- `manuscript/result_to_method_map.csv`
- `manuscript/high_risk_author_verification.md`
- `manuscript/co_discussion_handoff.md`

The handoff must summarize the study design, three module types, models and cohorts, interventions, assays, statistics, ethics, unresolved method details, and source-mode boundaries. After saving it, continue to `$co-discussion`; do not treat Methods as the end of Co-Paper.


- `references/reagent_search.md`: reagents, antibodies, primers, shRNA/siRNA, chemicals, kits, cell lines, plasmids, animal strains, sequencing products / 试剂、抗体、引物、shRNA/siRNA、化学品、试剂盒、细胞系、质粒、动物品系和测序产品。
- `references/software_citation.md`: R/Python packages, command-line tools, databases, web tools, commercial software, numbered citations / R/Python 包、命令行工具、数据库、网页工具、商业软件和编号引用。
- `references/medical_methods_format.md`: Methods structure, ethics, statistics, medical reporting, Nature-style logic / 方法结构、伦理、统计、医学报告格式和 Nature-style 逻辑。
- `references/output_templates.md`: complete drafts, tables, audit checklist, reusable prompt / 完整草稿、表格、审计清单和可复用 prompt。

## Search Rules / 检索规则

Use web search unless the user forbids it. Prefer current official or primary sources in this order.  
除非用户禁止联网，否则使用网络检索。按以下顺序优先使用当前官方或一手来源。

1. **EN:** User-provided protocols, supplementary methods, raw manifests, ELN notes, or purchase records.  
   **中：** 用户提供的 protocol、补充方法、原始清单、实验记录或采购记录。
2. **EN:** China-based official supplier pages when plausible, especially Proteintech/武汉三鹰 for antibodies, 正能生物 and similar Chinese suppliers for kits/reagents/services, 上海生工生物 for primers and oligos, and 中科院上海细胞库 for cell lines.  
   **中：** 可行时优先中国官方供应商：抗体优先 Proteintech/武汉三鹰；试剂盒、常规试剂和服务优先正能生物等国内供应商；引物和寡核苷酸优先上海生工；细胞系优先中科院上海细胞库。
3. **EN:** Official manufacturer, datasheet, IFU, SDS, Addgene, RRID/Antibody Registry, NCBI, PrimerBank, or repository pages.  
   **中：** 官方厂家页、datasheet、IFU、SDS、Addgene、RRID/抗体注册库、NCBI、PrimerBank 或数据库页面。
4. **EN:** Global official manufacturer pages when Chinese sources do not provide the needed identifier.  
   **中：** 中国来源无法提供必要标识符时，使用全球官方厂家页。
5. **EN:** Peer-reviewed Methods only for contextual protocol parameters or previously reported sequences; do not use them to invent what the user used.  
   **中：** 同行评议 Methods 只用于参考参数或既往报道序列，不能用来虚构用户实际使用的材料。

Do not cite shopping aggregators, reseller pages without manufacturer identity, blogs, or AI summaries as final evidence.  
不要把购物聚合页、无厂家身份的经销商页、博客或 AI 摘要作为最终证据。

## Required Specificity / 具体性要求

Every specific item should be indexed immediately after its name.  
每个具体物品都应在名称后立即标注信息。

- **EN:** Reagents, antibodies, kits, chemicals, plasmids, cell lines, animal strains: `(Cat. no.; Company, Country; clone/host/dilution/RRID/lot/concentration/source when available)`.  
  **中：** 试剂、抗体、试剂盒、化学品、质粒、细胞系、动物品系：`(货号；公司，国家；如有则写 clone/宿主/稀释度/RRID/批号/浓度/来源)`。
- **EN:** Primers: `(forward 5'-...-3', reverse 5'-...-3'; amplicon length; Company, Country; design/source)`.  
  **中：** 引物：`(forward 5'-...-3'，reverse 5'-...-3'；扩增长度；公司，国家；设计或来源)`。
- **EN:** shRNA/siRNA/sgRNA: `(target or guide sequence; vector/modification; Company, Country; design/source)`.  
  **中：** shRNA/siRNA/sgRNA：`(靶向或 guide 序列；载体/修饰；公司，国家；设计或来源)`。
- **EN:** Instruments: `(model; Company, Country)`.  
  **中：** 仪器：`(型号；公司，国家)`。
- **EN:** Software/packages: `(version; Company/Developer, Country) [numbered citation]`.  
  **中：** 软件或包：`(版本；公司/开发者，国家) [编号引用]`。

## Methods Drafting Principles / 方法撰写原则

- **EN:** Use Nature-style method logic: task or biological context -> overview -> procedure modules -> implementation details -> assumptions and boundaries.  
  **中：** 使用 Nature-style 方法逻辑：任务或生物学背景 -> 概览 -> 操作模块 -> 实施细节 -> 假设和边界。
- **EN:** Include motivation, procedure, and evidence role for each module.  
  **中：** 每个模块说明目的、操作过程和支撑哪个结果。
- **EN:** Use medical-literature structure when applicable: ethics, participants/animals, sample collection, randomization/blinding, interventions, outcomes, assays, processing, statistics, availability.  
  **中：** 适用时使用医学论文结构：伦理、受试者/动物、样本采集、随机化/盲法、干预、终点、实验、数据处理、统计和数据可用性。

Avoid unsupported vague phrases / 避免无支撑的模糊表达：

- `under standard conditions`
- `according to the manufacturer's instructions` without kit name and critical deviations
- `routine methods`
- `data were analyzed statistically`
- `samples were randomly assigned` without method
- `validated antibody` without clone/catalog/RRID and validation basis

## Output Contract / 输出契约

Default Methods request / 默认方法撰写任务：

1. **EN:** Concise Methods section with conventional subheadings.  
   **中：** 带常规小标题的精简 Methods 正文。
2. **EN:** Numbered software/package references when software or R packages are named.  
   **中：** 若出现软件或 R 包，给出编号引用。
3. **EN:** Brief `高风险需作者核对` only for ethically or scientifically non-inferable details.  
   **中：** 仅对无法伦理或科学推断的信息列出简短 `高风险需作者核对`。

Full or audit-style request / 完整或审计型任务：

1. Alignment note / 对齐说明。
2. Result-to-method map / 结果-方法映射。
3. Drafted Methods / Methods 正文。
4. Materials and sequence index / 材料和序列表。
5. Instrument index / 仪器表。
6. Software and statistics index with numbered references / 软件和统计索引及编号参考文献。
7. Search evidence ledger / 检索证据账本。
8. Numbered reference list / 编号参考文献。
9. High-risk author-verification ledger / 高风险作者核对清单。

If the user asks only for a prompt or template, provide the concise reusable prompt from `references/output_templates.md` and adapt it.  
如果用户只要 prompt 或模板，调用 `references/output_templates.md` 中的精简可复用 prompt 并适配当前稿件。
