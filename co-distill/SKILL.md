---
name: co-distill
description: Distill biomedical papers into reusable research routines, figure logic, dataset patterns, assay modules, novelty moves, and replication templates. Use when Codex needs to extract a paper routine, reverse engineer article structure, identify common workflows from a literature class, or produce routine_distillation output for co-topic. 用于从文献类别中蒸馏文章套路、图版逻辑、数据模式和复刻模板。
---

# Co-Distill / 文章套路蒸馏

## Operating Goal / 运行目标

**English:** Turn a selected paper class into a reusable research routine. Distill structure, evidence ladder, data strategy, and figure logic without copying the original biological topic too literally.

**中文：** 将选定文献类别转化为可复用的研究套路。蒸馏文章结构、证据阶梯、数据策略和图版逻辑，但不要机械复制原始生物学主题。

Default to Chinese reports unless the user requests another language. Generated Markdown reports should be Chinese-only by default; do not create bilingual project reports unless explicitly requested.  
除非用户要求其他语言，报告默认使用中文。生成的 Markdown 报告默认只写中文；除非用户明确要求，不生成中英双语项目报告。

## Inputs / 输入

Use one or more / 使用以下一种或多种输入：

- `$co-search` outputs / `$co-search` 输出。
- A list of papers or DOIs / 论文列表或 DOI。
- User-provided PDFs, abstracts, figures, or notes / 用户提供的 PDF、摘要、图或笔记。
- A selected literature class from `$co-paper` / `$co-paper` 中选定的文献类别。

## Workflow / 工作流

1. **EN:** Build a source ledger from selected papers.  
   **中：** 根据选定论文建立来源账本。
2. **EN:** Extract the common biological question and novelty move.  
   **中：** 提取共同生物学问题和创新动作。
3. **EN:** Reconstruct the article routine: public-data entry, node-discovery experiment, computational discovery, validation ladder, mechanism test, and translational relevance.  
   **中：** 重建文章套路：公共数据入口、节点发现实验、计算发现、验证阶梯、机制测试和转化相关性。
4. **EN:** Map figure order and the job of each panel.  
   **中：** 映射图版顺序和每个 panel 的功能。
5. **EN:** Identify reusable datasets, node-discovery experiments, validation experiments, models, perturbations, and statistics.  
   **中：** 识别可复用的数据集、节点发现实验、验证实验、模型、扰动和统计方法。
6. **EN:** Separate what should be copied as a routine from what should not be copied as a topic.  
   **中：** 区分可复刻的套路和不应照搬的课题内容。
7. **EN:** Save the distilled routine and hand it to `$co-topic`.  
   **中：** 保存蒸馏套路，并交给 `$co-topic`。

Read `references/routine_schema.md` for table schemas.  
读取 `references/routine_schema.md` 获取表格格式。

## Distillation Rules / 蒸馏规则

- **EN:** Distill paper structure, not prose.  
  **中：** 蒸馏文章结构，不复制文字。
- **EN:** Preserve citation provenance for every extracted routine element.  
  **中：** 每个套路元素都保留文献来源。
- **EN:** Label speculation and author interpretation separately from demonstrated evidence.  
  **中：** 将推测、作者解释和已验证证据分开。
- **EN:** Do not overfit to one paper when the input is a class.  
  **中：** 输入是一类论文时，不要过拟合到单篇文章。
- **EN:** Identify reviewer risks and missing controls in the original routine.  
  **中：** 识别原套路中的审稿风险和缺失对照。
- **EN:** Always separate node-discovery experiments from validation experiments. Node-discovery experiments explain how the paper found downstream molecules, mechanism mediators, or phenotype-linked nodes, such as screening omics, perturbation omics after conditional knockout/knockdown, proteomics/phosphoproteomics/secretomics/metabolomics, IP-MS/pull-down-MS, spatial/cell-cell screening, CRISPR/RNAi screens, or target-fishing assays. Validation experiments then prove or test the node, and important examples must be emphasized: conditional knockout or tissue/cell-specific knockout, knockdown/overexpression, rescue, neutralization, inhibitor/agonist, mass-spectrometry validation such as targeted MS/PRM/SRM, Co-IP-MS, IP-MS or pull-down-MS confirmation, SPR/BLI/ITC molecular interaction assays, Co-IP, CETSA/DARTS, reporter assays, and phenotype rescue.  
  **中：** 必须区分“节点发现实验”和“验证实验”。节点发现实验回答论文如何发现下游分子、机制介质或表型关联节点，例如筛选组学、条件性敲除/敲低后的扰动组学、蛋白组/磷酸化组/分泌组/代谢组、IP-MS/pull-down-MS、空间/细胞互作筛选、CRISPR/RNAi screen 或 target-fishing 实验。验证实验再证明或检验该节点，且必须强调重要验证实验：条件性敲除或组织/细胞特异性敲除、敲低/过表达、rescue、中和、抑制剂/激动剂、质谱验证如 targeted MS/PRM/SRM、Co-IP-MS、IP-MS 或 pull-down-MS 确认、SPR/BLI/ITC 分子互作检测、Co-IP、CETSA/DARTS、报告基因和表型 rescue。

## Required Outputs / 必要输出

Save in `02_distill/` or the requested directory / 保存到 `02_distill/` 或指定目录：

- `routine_distillation.md`
- `figure_logic_table.csv`
- `dataset_assay_inventory.csv`
- `node_discovery_experiments.md`
- `novelty_and_gap_map.md`
- `replication_template.md`
- `reviewer_risk_ledger.md`
- `evidence_ledger_update.csv`

If figures are needed but not generated, save `figure_reconstruction_prompts.md`.  
如果需要图片但未实际生成，保存 `figure_reconstruction_prompts.md`。
