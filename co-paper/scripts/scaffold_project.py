#!/usr/bin/env python3
"""Create a Co-Paper project workspace without overwriting existing files."""

from __future__ import annotations

import argparse
import csv
from datetime import date
from pathlib import Path


EVIDENCE_COLUMNS = [
    "id",
    "stage",
    "module_id",
    "claim",
    "evidence_type",
    "source",
    "source_detail",
    "evidence_tier",
    "direction",
    "confidence",
    "limitations",
    "next_action",
]

SOURCE_MODE_COLUMNS = [
    "result_id",
    "stage",
    "module_id",
    "figure_panel",
    "claim",
    "source_mode",
    "input_file_or_source",
    "simulation_status",
    "allowed_in_manuscript",
    "notes",
]

MODULE_COLUMNS = [
    "module_id",
    "relationship_type",
    "parent_module_id",
    "parallel_group",
    "innovation_family",
    "selected_innovation_point",
    "selected_hypothesis_id",
    "selected_hypothesis",
    "biological_question",
    "active_claim",
    "discovery_status",
    "validation_status",
    "rescue_status",
    "plan_file",
    "result_file",
    "source_modes",
    "result_interpretation",
    "next_downstream_options",
    "user_decision",
    "status",
]

HYPOTHESIS_COLUMNS = [
    "module_id",
    "selected_innovation_point",
    "hypothesis_id",
    "rank",
    "hypothesis_name",
    "novelty",
    "evidence_strength",
    "feasibility",
    "causal_testability",
    "translational_value",
    "collision_risk",
    "risk_penalty",
    "total",
    "user_decision",
    "status",
    "co_plan_handoff",
]


def write_text(path: Path, content: str) -> None:
    if not path.exists():
        path.write_text(content, encoding="utf-8")


def write_csv(path: Path, columns: list[str]) -> None:
    if path.exists():
        return
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(columns)


def main() -> None:
    parser = argparse.ArgumentParser(description="Scaffold a Co-Paper project workspace.")
    parser.add_argument("--project", required=True, help="Project title")
    parser.add_argument("--out", required=True, help="Output project directory")
    parser.add_argument("--rounds", type=int, default=1, help="Number of round folders to create")
    args = parser.parse_args()

    out = Path(args.out).resolve()
    out.mkdir(parents=True, exist_ok=True)

    for folder in ["01_search", "02_modules", "manuscript"]:
        (out / folder).mkdir(exist_ok=True)

    for index in range(1, args.rounds + 1):
        round_dir = out / f"module_{index:02d}"
        for folder in ["debate", "plan", "scripts", "figures", "tables"]:
            (round_dir / folder).mkdir(parents=True, exist_ok=True)
        write_text(
            round_dir / "interpretation_and_next_module.md",
            "# Interpretation and Next Module\n\n- Module relationship: standalone / parallel / progressive_downstream / progressive_upstream\n- Result classification:\n- Discovery layer status:\n- Validation layer status:\n- Rescue status if mediator:\n- What can be claimed:\n- What cannot be claimed:\n- Downstream module options:\n- Upstream module options:\n- Parallel module options:\n- User decision:\n",
        )

    write_text(
        out / "project_state.md",
        f"# {args.project}\n\n- Created: {date.today().isoformat()}\n- Current stage: 01_search\n- Current module: TBD\n- Completed modules: 0\n- Current round: 0\n- Next decision: choose one innovation module from co-search\n",
    )
    write_text(out / "decision_log.md", "# Decision Log\n")
    write_csv(out / "module_ledger.csv", MODULE_COLUMNS)
    write_csv(out / "hypothesis_ledger.csv", HYPOTHESIS_COLUMNS)
    write_csv(out / "evidence_ledger.csv", EVIDENCE_COLUMNS)
    write_csv(out / "source_mode_ledger.csv", SOURCE_MODE_COLUMNS)
    write_text(out / "manuscript" / "virtual_result_rationale.md", "# 虚拟或假设结果解释\n\n如本项目使用虚拟或假设阳性结果，在此记录文献调研、公共数据可行性、创新性扫描、最接近既往工作、所选既可能成立又最有创新性的阳性结果轴、为什么不是直接重复，以及剩余不确定性。\n")
    write_text(out / "manuscript" / "full_manuscript.md", "# 中文全文初稿\n")

    print(f"Created Co-Paper project workspace: {out}")


if __name__ == "__main__":
    main()
