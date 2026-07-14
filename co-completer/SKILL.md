---
name: co-completer
description: Complete the final stage of an interactive modular biomedical or life-science paper workflow, or review, revise, supplement, and complete an existing manuscript. Use for reviewer-style critique, manuscript writing, completion judgment, dynamic branch/resume decisions, or a new downstream loop through co-search, co-debate, co-plan, and co-result. 用于 co-paper 终稿后的审稿、写作补全、完成判定、动态分支，或启动包含 co-debate 的新模块循环。
---

# Co-Completer

## Operating Goal / 运行目标

Turn a nearly complete manuscript into a review-driven completion package. In `$co-paper`, `$co-completer` is the final gate after `manuscript/full_manuscript.md`: it reviews, writes or rewrites what is needed, and then asks the user to choose whether to mark complete, branch/resume, or start a new module loop through `$co-search`, user module selection, `$co-debate`, user hypothesis selection, `$co-plan`, and `$co-result`.

将接近完成的全文转化为“审稿驱动的完成包”。如需新增模块，必须重新经过 `$co-search → 用户选模块 → $co-debate Top 5 → 用户选假说 → $co-plan → $co-result`。

## Core Workflow / 核心流程

1. **Intake and language detection / 接收材料并判断语言**
   - Inspect the manuscript, abstract, figures, supplements, reviewer comments, target journal, and user goals when provided.
   - If files are missing, start from the pasted text but record missing inputs.
   - Decide manuscript-facing language from the manuscript itself, not from the user's interface language.

2. **Completion review first / 先做完成审稿**
   - Do not edit the manuscript during the first pass.
   - Save `completion_review.md` with major concerns, minor concerns, figure-by-figure logic audit, claim-evidence gaps, statistics and reproducibility risks, novelty risks, newsworthiness, final-readiness judgment, and decisive missing experiments.
   - Load `references/review_and_revision.md` for the review structure.

3. **Revision recommendations and approval checkpoint / 形成修改建议并等待确认**
   - Save `completion_revision_plan.md` with prioritized actions, rationale, expected manuscript impact, required data, feasibility, and risk.
   - Ask the user which recommendations to accept before rewriting or adding content.
   - If the user explicitly says to proceed automatically, still pause before generating virtual or simulated results.

4. **Mechanism completion plan / 完善机制逻辑**
   - After approval, map the current manuscript logic into `upstream -> core mechanism -> downstream phenotype -> validation -> translational relevance`.
   - Propose upstream drivers, downstream effectors, and deeper mechanistic tests that make the story more complete without overclaiming.
   - Load `references/mechanism_and_dataset_planning.md` for analysis and experiment planning.

5. **Bioinformatics recommendations and usable datasets / 生信分析建议和可用数据集**
   - Provide analyses in priority order: what question each analysis answers, what public dataset type is needed, where to search, what result would support or weaken the claim, and what figure panel it can become.
   - Prefer current database lookup for specific dataset IDs because public datasets are time-sensitive.
   - Save `bioinformatics_supplement_plan.md` and `dataset_manifest.csv`.

6. **Supplemental experiment data and usable datasets / 补充实验数据和可用数据集**
   - Propose wet-lab or in vivo validation after bioinformatics planning.
   - Separate node-discovery experiments from decisive validation experiments.
   - Identify the concrete raw data needed for each assay, including qPCR, western blot, ELISA, IF/IHC, flow cytometry, perturbation, rescue, animal models, organoids, direct binding, proteomics, metabolomics, or spatial validation when relevant.
   - Save `experimental_supplement_plan.md`.

7. **Result-source checkpoint / 结果来源确认**
   - Before rewriting Results, classify each planned result as `real`, `partial`, `assumed`, `virtual_positive`, or `requirements_only`.
   - If results are not supplied, ask whether the user wants to provide real results, treat some findings as assumed, or generate virtual positive results. Never invent positive results without explicit confirmation.
   - Save `result_source_ledger.md`.

8. **Call `$co-result` / 调用 `$co-result`**
   - Use `$co-result` after source modes are clear. Pass the accepted revision plan, planned figures, bioinformatics result summaries, experimental result summaries, and source ledger.
   - If `$co-result` is unavailable, follow the same output contract and state that the specialist skill could not be loaded.
   - Load `references/results_and_export.md` for the handoff prompt, markup, and export rules.

9. **Marked revision and export / 标记修改并导出**
   - In Markdown, wrap newly added or substantially revised manuscript-facing content with:
     `<span style="color:red"><strong>new or revised text</strong></span>`
   - Mark additions and substantive rewrites, not unchanged sentences.
   - Export both Markdown and Word. Use `scripts/export_marked_docx.py` when a DOCX is requested or expected.

10. **Completion decision menu / 完成决策菜单**
   - Save `completion_decision_menu.md`.
   - Stop and ask the user to choose one of three routes:
     1. `complete_project`: mark the current project complete and save `project_completion_record.md`.
     2. `dynamic_branch`: return to an earlier checkpoint, choose another module/Figure/result/experiment node, and create a new project or subfolder under `branches/YYYYMMDD_<target>/` or the user-requested folder.
     3. `new_module_loop`: restart `$co-search -> user module choice -> $co-debate -> user hypothesis choice -> $co-plan -> $co-result`.

## Human Checkpoints / 用户确认点

Stop and ask the user to confirm at these points:

1. After `completion_revision_plan.md`: ask which changes to accept.
2. Before any virtual or simulated Results: ask whether virtual positive results are allowed and what direction should be simulated.
3. Before final export if major claims are still `assumed` or `virtual_positive`: ask whether to keep them as manuscript text, move them to proposed future work, or label them only in the project report.
4. After `completion_decision_menu.md`: ask whether to mark complete, branch/resume, or start a new module loop that includes `$co-debate` and both user selections.

## Required Outputs / 必要输出

For a full task, save these files under a task-specific folder such as `outputs/manuscript_revision/<project-slug>/`:

- `independent_review.md`
- `completion_review.md`
- `completion_revision_plan.md`
- `completion_decision_menu.md`
- `bioinformatics_supplement_plan.md`
- `dataset_manifest.csv`
- `experimental_supplement_plan.md`
- `result_source_ledger.md`
- `revised_results_marked.md`
- `revised_results_marked.docx`
- `raw_data_requirements_summary.md`

When full manuscript changes are requested, also save:

- `revised_manuscript_marked.md`
- `revised_manuscript_marked.docx`
- `change_log.md`
- `project_completion_record.md` when the user marks the project complete / 用户标记完成时生成。
- `new_module_loop_plan.md` when the user chooses another downstream module / 用户选择继续下游模块时生成。

## Scientific Rules / 科学规则

- Separate observation, association, public-data support, perturbation evidence, direct mechanism, and animal or clinical validation.
- Do not convert correlation or enrichment into causal language unless supported by direct perturbation and rescue.
- For virtual Results, record virtual status in source ledgers and project notes; keep manuscript-facing paragraphs clean unless the user asks for visible labels.
- If the manuscript is English, preserve English scientific style and only use Chinese in user-facing planning notes if helpful.
- If public dataset IDs, reagent details, or current database availability matter, verify them live rather than relying on memory.
- Do not close a `$co-paper` project silently after writing. Always present the completion decision menu unless the user has already specified the final route.
- When branching or creating a new project/subfolder, preserve the original project files and write inherited-file notes; do not overwrite prior manuscripts unless the user explicitly requests overwrite.

## References / 参考文件

Load only the needed reference:

- `references/review_and_revision.md`: completion review, reviewer-style critique, revision recommendation schema, and final decision menu.
- `references/mechanism_and_dataset_planning.md`: upstream/downstream mechanism extension, bioinformatics plans, public dataset sources, and experimental supplement design.
- `references/results_and_export.md`: `$co-result` handoff, source modes, red-bold markup, and DOCX export rules.

## Script / 脚本

Use the DOCX export script after writing a marked Markdown file:

```bash
python co-completer/scripts/export_marked_docx.py \
  revised_results_marked.md \
  revised_results_marked.docx
```
