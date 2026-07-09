# Review and Revision Schema

Use this reference when the task begins with an existing manuscript, reviewer comments, a `$co-paper` final manuscript, or a request to make the study more complete.

## Intake Checklist

Record what is available before reviewing:

- Manuscript text, abstract, Results, Methods, figures, legends, tables, supplemental files.
- Target journal or article type.
- User goal: response to reviewers, pre-submission strengthening, major revision, language polishing, or mechanism expansion.
- Existing datasets and experiments.
- Claims that are central to the story.
- Claims that already have direct evidence.
- Claims supported only by association, enrichment, public data, or inference.

If essential inputs are absent, continue with the available text and list missing inputs in the review.

## Independent Review Output

Save `completion_review.md` by default. If the user explicitly asks for a classic peer-review file, `independent_review.md` can also be generated as an alias. Include these sections:

1. `Manuscript Snapshot`: one-paragraph summary of the central claim and evidence chain.
2. `Overall Completion Assessment`: likely editorial decision, novelty, rigor, coherence, newsworthiness, completion status, and biggest risk.
3. `Major Concerns`: 3-8 numbered issues, each with evidence gap, affected figure/result, why it matters, and required fix.
4. `Minor Concerns`: wording, figure clarity, methods transparency, statistics, controls, and citation issues.
5. `Figure-by-Figure Audit`: for each figure, list claim, evidence type, missing controls, and recommended panel additions.
6. `Claim-Evidence Matrix`: claim, current evidence, strength, missing evidence, suggested analysis or experiment.
7. `Statistics and Reproducibility`: sample size, biological replicate, donor or animal unit, batch, normalization, multiple testing, blinding/randomization when relevant.
8. `Alternative Explanations`: at least one plausible alternative for every main mechanism.
9. `Decisive Missing Evidence`: the smallest set of analyses or experiments that would materially improve the manuscript.
10. `Completion Readiness`: one of `ready_to_complete`, `complete_after_minor_writing`, `needs_branch_or_more_data`, or `needs_new_module_loop`.

## Revision Recommendation Output

Save `completion_revision_plan.md` after the review. Use a priority table:

| Priority | Issue | Recommended change | Needed data | Expected impact | Risk if omitted |
|---|---|---|---|---|---|

Classify recommendations:

- `must_fix`: needed for logic, rigor, or reviewer acceptance.
- `high_value`: improves mechanism depth or novelty.
- `optional`: useful but not essential.
- `future_work`: better for Discussion than current Results.

End with a checkpoint question:

```text
请确认要采纳哪些建议。我可以按 must_fix + high_value 默认推进；如果要使用虚拟/模拟阳性结果，请明确说明允许模拟哪些结果方向。
```

For English manuscripts, ask the same checkpoint in English.

## Completion Decision Menu

After accepted review-driven writing or revision, save `completion_decision_menu.md` and stop for user choice unless the user already specified a route.

```markdown
# Completion Decision Menu

- Current manuscript:
- Completion review:
- Revision/writing files:
- Source mode status:
- Recommended route:

## Route A: Mark Project Complete
- Action:
- Files to preserve:
- Completion record:

## Route B: Dynamic Branch / Resume
- Candidate resume checkpoints:
- Candidate new project/subfolder:
- Inherited files:
- First next skill:

## Route C: New Module Loop
- Next downstream module question:
- One `$co-search` target:
- One `$co-plan` target:
- Expected `$co-result` output:
- Stop condition:
```

Route definitions:

- `complete_project`: write `project_completion_record.md`, mark the final manuscript path, source ledgers, figures, review, and completion date.
- `dynamic_branch`: create or propose `branches/YYYYMMDD_<target>/` or a user-named new project/subfolder; resume from a module, plan, Figure/result, node-discovery, validation, or manuscript revision checkpoint.
- `new_module_loop`: define one downstream module question, run `$co-search` to classify innovation points, ask the user to choose one module, run `$co-plan`, then close that module with `$co-result`.

## Review Tone

Be direct but constructive. Treat the manuscript as improvable, not broken. Avoid rewriting before the user approves the revision path.
