#!/usr/bin/env python3
"""Create a five-hypothesis Co-Debate scaffold without overwriting outputs."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--module", required=True, help="Selected module name")
    parser.add_argument("--out", required=True, help="Output debate directory")
    args = parser.parse_args()

    out = Path(args.out).resolve()
    if out.exists():
        raise SystemExit(f"Refusing to overwrite existing directory: {out}")
    out.mkdir(parents=True)

    (out / "debate_question.md").write_text(
        f"# Debate Question\n\n- Selected module: {args.module}\n- Decision needed: choose one hypothesis for co-plan\n",
        encoding="utf-8",
    )

    cards = [f"# Hypothesis Cards: {args.module}\n"]
    for index in range(1, 6):
        cards.append(
            f"""## H{index}. Hypothesis name

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
- Status: candidate
"""
        )
    (out / "hypothesis_cards.md").write_text("\n".join(cards), encoding="utf-8")

    with (out / "hypothesis_ranking.csv").open("w", newline="", encoding="utf-8") as handle:
        csv.writer(handle).writerow(
            [
                "rank", "hypothesis_id", "hypothesis_name", "novelty",
                "evidence_strength", "feasibility", "causal_testability",
                "translational_value", "collision_risk", "risk_penalty",
                "total", "decision", "main_reason",
            ]
        )

    (out / "reviewer_debate.md").write_text("# Reviewer Debate\n", encoding="utf-8")
    (out / "hypothesis_selection_menu.md").write_text(
        "# Hypothesis Selection\n\nSelect H1, H2, H3, H4, or H5 for co-plan.\n",
        encoding="utf-8",
    )
    print(f"Created Co-Debate scaffold: {out}")


if __name__ == "__main__":
    main()

