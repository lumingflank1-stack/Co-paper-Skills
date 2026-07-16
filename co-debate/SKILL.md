---
name: co-debate
description: Generate, challenge, and rank exactly five competing biomedical hypotheses as the final subskill managed by co-mimic. Consume the topic selected through co-topic plus Co-Mimic's routine, evidence ledger, ??? slot, exclusions, and falsification boundary; return the selected hypothesis to co-mimic for the final optional co-paper or co-plan handoff.
---

# Co-Debate / 科学假说辩论与排序

## Goal

Turn the Co-Mimic-selected topic into exactly five genuinely competing, testable hypotheses. Rank them as a skeptical but fair reviewer, stop for user selection unless automatic continuation was requested, and return control to Co-Mimic.

Default to Chinese reports unless the user requests another language.

## Inputs

- Selected topic card from `$co-topic`.
- Co-Mimic routine, `???` slot, exclusions, evidence ledger, and falsification boundary.
- User constraints and any prior project evidence.

If the topic card is missing, return to `$co-topic`. If its literature basis is weak, return to `$co-search` rather than inventing evidence.

## Workflow

1. Restate the selected topic and unresolved decision.
2. Separate observation, association, inference, perturbation, rescue, and direct causality.
3. Generate exactly five competing hypotheses; include a null, confounding, or reverse-causation hypothesis when evidence is associative.
4. For each hypothesis, state mechanism, predictions, supporting evidence, strongest objection, alternative explanation, decisive test, and falsification criteria.
5. Score novelty, evidence strength, feasibility, causal testability, translational value, and collision risk.
6. Rank H1-H5 from highest to lowest; label high-novelty/low-evidence options `high-risk`.
7. Stop for the user to choose one hypothesis or request revision/reranking.
8. Save only the chosen hypothesis, alternatives, falsification criteria, evidence gaps, and three-module implications, then return the handoff to `$co-mimic`.

Read `references/debate_and_ranking.md` for schemas. Use `scripts/scaffold_debate.py` when a blank debate folder is useful.

## Required Outputs

Save under `04_debate/` or the selected topic folder:

- `debate_question.md`
- `hypothesis_cards.md`
- `hypothesis_ranking.csv`
- `reviewer_debate.md`
- `hypothesis_selection_menu.md`
- `co_plan_handoff.md` after user selection
