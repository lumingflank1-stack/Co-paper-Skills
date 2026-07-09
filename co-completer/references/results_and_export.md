# Results and Export Contract

Use this reference when the accepted revision plan is ready to become manuscript-facing Results or a marked manuscript.

## Source Modes

Classify every result before writing:

- `real`: user provided actual result or analysis output.
- `partial`: user provided incomplete result; write only supported claims and flag missing details.
- `assumed`: user asks to treat a result as true.
- `virtual_positive`: user explicitly asks for simulated, mock, virtual, or expected positive results.
- `requirements_only`: user asks what data are needed; do not write Results.

If a result is `assumed` or `virtual_positive`, save the status in `result_source_ledger.md`. Do not hide the status from project reports.

## Handoff to `$co-result`

Invoke `$co-result` with a compact package:

```text
Use $co-result

Task: Draft revised Results for an existing manuscript after approved revision.
Language: <Chinese unless manuscript is English; if English manuscript, use English>
Source mode: <real / partial / assumed / virtual_positive mixed by panel>
Manuscript claim: <central claim>
Accepted revision plan: <bullets>
Bioinformatics results: <real or approved virtual summaries>
Experimental results: <real or approved virtual summaries>
Figure plan: <Figure 1A-D etc.>
Source ledger: <panel-level source modes>
Markup rule: wrap added or substantially revised manuscript-facing text in <span style="color:red"><strong>...</strong></span>.
Outputs: revised_results_marked.md, result_source_ledger.md, raw_data_requirements_summary.md, and DOCX export.
```

If `$co-result` is not available, use its visible contract: Results prose, figure legends, source ledger, raw-data requirements, and Markdown outputs. Do not generate virtual results without explicit permission.

## Red Bold Markup

Use this exact Markdown/HTML pattern for additions or substantial rewrites:

```html
<span style="color:red"><strong>newly added or substantially revised manuscript text</strong></span>
```

Rules:

- Mark new manuscript-facing content and major rewrites.
- Do not mark unchanged sentences.
- Do not mark project notes, source ledgers, or internal planning comments unless the user asks.
- Keep the visible manuscript fluent; source status belongs in ledgers and notes.
- If the manuscript is English, the marked text should be English.

## File Naming

Use these defaults:

- `completion_review.md`
- `completion_revision_plan.md`
- `revised_results_marked.md`
- `revised_results_marked.docx`
- `revised_manuscript_marked.md`
- `revised_manuscript_marked.docx`
- `change_log.md`
- `result_source_ledger.md`
- `raw_data_requirements_summary.md`
- `completion_decision_menu.md`
- `project_completion_record.md`
- `new_module_loop_plan.md`

## DOCX Export

After saving marked Markdown, run:

```bash
python co-completer/scripts/export_marked_docx.py \
  revised_results_marked.md \
  revised_results_marked.docx
```

The exporter recognizes the red-bold span above and writes the corresponding DOCX run in red and bold. It also supports `{{ADD:...}}` and `<red>...</red>` as emergency shorthand, but the manuscript Markdown should use the formal HTML span.
