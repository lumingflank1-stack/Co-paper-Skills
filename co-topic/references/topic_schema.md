# Co-Topic Candidate and Selection Schema

## Topic card

```markdown
### T1. Topic name

- Distilled routine used:
- New biological context:
- Core phenotype or mechanism:
- Unknown core slot: `???`
- Allowed family:
- Known targets to exclude:
- Why this is not a copy:
- Bioinformatics exploration module:
- Experimental validation module:
- Bioinformatics validation module:
- Rescue requirement:
- Decisive test:
- Falsification criteria:
- Alternative explanation:
- Reviewer concern:
- Translational angle:
- Status: candidate / prioritized / backup / rejected
```

## Prioritization columns

`rank,topic_id,topic_name,unknown_core_slot,novelty,evidence,public_data_feasibility,analysis_feasibility,experiment_feasibility,unknown_node_discoverability,causal_testability,manuscript_potential,collision_risk,risk_penalty,total,decision,main_risk`

Score positive criteria 1-5 and risks 0-5. State the total formula.

## Return to Co-Mimic

Return the selected topic, user rationale, evidence boundary, `???` slot, exclusions, three-module outline, decisive test, alternative explanation, falsification criteria, and unresolved hypothesis choice to Co-Mimic. Co-Mimic creates the Co-Debate handoff.
