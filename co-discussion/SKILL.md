---
name: co-discussion
description: Research literature and draft numbered-citation Introduction and Discussion sections from completed Results, evidence ledgers, and manuscript claim maps. Use when Codex needs to write or plan Introduction, Discussion, literature positioning, limitations, future directions, numbered references, or full-manuscript narrative around biomedical results. 用于先调研文献，再基于结果撰写带编号引用的引言和讨论。
---

# Co-Discussion / 引言与讨论撰写

## Operating Goal / 运行目标

**English:** Write manuscript Introduction and Discussion after Results are stable. First research and map literature, then draft section prose with numbered citations.

**中文：** 在 Results 稳定后撰写论文 Introduction 和 Discussion。先调研并映射文献，再用编号引用撰写正文。

Default to Chinese manuscript prose unless the user requests English or another language. Generated Markdown reports, Introduction, Discussion, and manuscript inputs should be Chinese-only by default; do not create bilingual project reports unless explicitly requested.  
除非用户要求英文或其他语言，默认使用中文论文正文。生成的 Markdown 报告、Introduction、Discussion 和全文输入默认只写中文；除非用户明确要求，不生成中英双语项目报告。

## Required Inputs / 必要输入

Use the most complete available version / 使用可获得的最完整版本：

- Results section from `$co-result` / `$co-result` 生成的 Results。
- Figure legends or figure plan / 图注或图版计划。
- Evidence ledger and source mode ledger from `$co-paper` / `$co-paper` 的证据账本和来源模式账本。
- Literature matrix from `$co-search` / `$co-search` 的文献矩阵。

If Results are missing, produce an outline and missing-input ledger rather than inventing findings.  
如果缺少 Results，输出大纲和缺失输入清单，不编造发现。

## Literature Step / 文献步骤

**English:** Use literature search unless the user forbids it or supplies a fixed reference set. Prefer PubMed, Europe PMC, DOI pages, journal pages, and official database documentation.

**中文：** 除非用户禁止联网或提供固定参考文献集，否则先进行文献检索。优先使用 PubMed、Europe PMC、DOI 页、期刊页和官方数据库文档。

Search for / 检索内容：

- Field background and disease relevance / 领域背景和疾病相关性。
- Prior work on mechanism, cell type, pathway, target, metabolite, or dataset / 关键机制、细胞类型、通路、靶点、代谢物或数据集的既往研究。
- Rival explanations and conflicting evidence / 竞争解释和相反证据。
- Methodological precedents for the routine / 支撑该套路的方法学先例。
- Translational or clinical context when relevant / 相关时补充转化或临床背景。

Read `references/intro_discussion_writing.md` and `references/literature_citation.md` before drafting full sections.  
完整撰写前读取 `references/intro_discussion_writing.md` 和 `references/literature_citation.md`。

## Writing Logic / 写作逻辑

Use the research-paper hourglass / 使用研究论文沙漏结构：

- **Introduction EN:** field scale -> bottleneck -> prior work -> unresolved gap -> present study.  
  **引言中：** 领域尺度 -> 瓶颈 -> 既往工作 -> 未解决 gap -> 本研究。
- **Discussion EN:** central advance -> meaning of evidence -> relation to prior work -> limitations and rival explanations -> future work.  
  **讨论中：** 核心进展 -> 证据意义 -> 与既往工作的关系 -> 局限和竞争解释 -> 未来工作。

Do not draft Introduction before the Results claim map is known.  
在 Results claim map 明确前，不要正式撰写 Introduction。

## Citation Rules / 引用规则

- **EN:** Use numbered citations in order of first appearance, such as `[1]` and `[2,3]`.  
  **中：** 按首次出现顺序使用编号引用，如 `[1]`、`[2,3]`。
- **EN:** Do not invent references, PMID, DOI, authors, years, or journal details.  
  **中：** 不编造参考文献、PMID、DOI、作者、年份或期刊信息。
- **EN:** Every citation must appear in `references_numbered.md` and `citation_ledger.csv`.  
  **中：** 每条引用都必须出现在 `references_numbered.md` 和 `citation_ledger.csv`。
- **EN:** Cite prior work to position claims, not to decorate the bibliography.  
  **中：** 引用用于定位 claim，不是装饰参考文献列表。

## Required Outputs / 必要输出

Save in `manuscript/` or the requested directory / 保存到 `manuscript/` 或指定目录：

- `introduction.md`
- `discussion.md`
- `references_numbered.md`
- `citation_ledger.csv`
- `claim_evidence_citation_map.csv`
- `limitations_and_alternatives.md`

If literature search is blocked, save `literature_search_blockers.md` and draft only a citation-placeholder scaffold.  
如果文献检索受阻，保存 `literature_search_blockers.md`，只写带引用占位符的骨架。
