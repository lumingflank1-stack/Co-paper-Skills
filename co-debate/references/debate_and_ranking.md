# Co-Debate Contract

## Hypothesis card

```markdown
### H1. Short name

- Selected topic:
- Core mechanism:
- Predicted axis:
- Supporting evidence and tier:
- Key predictions:
- Strongest reviewer objection:
- Alternative or null explanation:
- Decisive analysis or experiment:
- Falsification criteria:
- Bioinformatics exploration implication:
- Experimental validation implication:
- Bioinformatics validation implication:
- Feasibility risk:
- Collision risk:
- Status: prioritized / viable / high-risk / weakened
```

## Ranking

`rank,hypothesis_id,hypothesis_name,novelty,evidence_strength,feasibility,causal_testability,translational_value,collision_risk,risk_penalty,total,decision,main_reason`

Use `total = novelty + evidence_strength + feasibility + causal_testability + translational_value - collision_risk - risk_penalty`. Break ties by causal testability, feasibility, then novelty.

Exactly five hypotheses must address the same selected topic; at least three must use genuinely different causal structures. Include a null/confounding/reverse-causation hypothesis when appropriate.

## Return to Co-Mimic

After user selection record the topic, selected hypothesis, active claim, predictions, alternative explanation, falsification criteria, evidence gaps, and requirements for all three Co-Plan modules. Return this package to Co-Mimic. Co-Mimic decides whether to stop or, with user approval, hand it to `$co-paper` or `$co-plan`.
