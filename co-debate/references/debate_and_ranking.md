# Co-Debate Hypothesis and Ranking Contract

## Hypothesis Card

```markdown
### H1. Short hypothesis name

- Selected module:
- Core mechanism:
- Predicted axis:
- Evidence supporting it:
- Evidence tier:
- Key predictions:
- Strongest reviewer objection:
- Alternative or null explanation:
- Decisive analysis or experiment:
- Falsification criteria:
- Main feasibility risk:
- Collision risk with prior work:
- Status: prioritized / viable / high-risk / weakened
```

## Ranking Columns

`rank,hypothesis_id,hypothesis_name,novelty,evidence_strength,feasibility,causal_testability,translational_value,collision_risk,risk_penalty,total,decision,main_reason`

Score positive criteria from 1 to 5. Score `collision_risk` and `risk_penalty` from 0 to 5. Use:

`total = novelty + evidence_strength + feasibility + causal_testability + translational_value - collision_risk - risk_penalty`

Rank from highest to lowest. Break ties by causal testability, feasibility, then novelty.

## Required Top Five Composition

- Five hypotheses must address the same selected module.
- At least three must represent genuinely different mechanisms or causal structures.
- Include one null/confounding/reverse-causation hypothesis when evidence is associative.
- A high-novelty, low-evidence hypothesis may remain in the Top 5 only with `high-risk` status.
- Do not insert a known literature target as the winner solely because it has the most publications.

## User Selection Menu

```markdown
# Hypothesis Selection

Select one:

1. H1 — <name and one-line tradeoff>
2. H2 — <name and one-line tradeoff>
3. H3 — <name and one-line tradeoff>
4. H4 — <name and one-line tradeoff>
5. H5 — <name and one-line tradeoff>

Alternative actions:

- rerank with changed weights
- revise one or more hypotheses
- return to co-search and select another module
```

## Co-Plan Handoff

After user selection, save:

```markdown
# Co-Plan Handoff

- Selected module:
- Selected hypothesis ID:
- Selected hypothesis:
- Why the user selected it:
- Active claim to test:
- Key predictions:
- Main alternative explanation:
- Falsification criteria:
- Evidence gaps:
- Relationship to prior module: standalone / parallel / progressive_downstream / progressive_upstream
```

