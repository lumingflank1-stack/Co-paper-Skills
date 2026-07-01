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
    "figure_panel",
    "claim",
    "source_mode",
    "input_file_or_source",
    "simulation_status",
    "allowed_in_manuscript",
    "notes",
]


def write_text(path: Path, content: str) -> None:
    if not path.exists():
        path.write_text(content)


def write_csv(path: Path, columns: list[str]) -> None:
    if path.exists():
        return
    with path.open("w", newline="") as handle:
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

    for folder in ["01_search", "02_distill", "03_topics", "04_plan", "manuscript"]:
        (out / folder).mkdir(exist_ok=True)

    for index in range(1, args.rounds + 1):
        round_dir = out / f"round_{index:02d}"
        for folder in ["plan", "scripts", "figures", "tables"]:
            (round_dir / folder).mkdir(parents=True, exist_ok=True)
        write_text(
            round_dir / "interpretation_and_revision.md",
            "# Interpretation and Revision\n\n- Result classification:\n- What can be claimed:\n- What cannot be claimed:\n- Next step:\n",
        )

    write_text(
        out / "project_state.md",
        f"# {args.project}\n\n- Created: {date.today().isoformat()}\n- Current stage: 01_search\n- Selected literature class: TBD\n- Selected topic: TBD\n- Current round: 0\n- Next decision: choose literature search scope\n",
    )
    write_text(out / "decision_log.md", "# Decision Log\n")
    write_csv(out / "evidence_ledger.csv", EVIDENCE_COLUMNS)
    write_csv(out / "source_mode_ledger.csv", SOURCE_MODE_COLUMNS)
    write_text(out / "manuscript" / "virtual_result_rationale.md", "# 虚拟或假设结果解释\n\n如本项目使用虚拟或假设阳性结果，在此记录文献调研、公共数据可行性、创新性扫描、最接近既往工作、所选既可能成立又最有创新性的阳性结果轴、为什么不是直接重复，以及剩余不确定性。\n")
    write_text(out / "manuscript" / "full_manuscript.md", "# 中文全文初稿\n")

    print(f"Created Co-Paper project workspace: {out}")


if __name__ == "__main__":
    main()
