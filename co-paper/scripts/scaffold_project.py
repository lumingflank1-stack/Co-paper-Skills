#!/usr/bin/env python3
"""Create a Co-Paper three-module project without overwriting files."""

from __future__ import annotations

import argparse
import csv
from datetime import date
from pathlib import Path


MODULE_COLUMNS = ["cycle_id", "module_type", "biological_question", "active_claim", "plan_file", "result_file", "status", "source_modes", "interpretation", "user_decision"]
EVIDENCE_COLUMNS = ["id", "cycle_id", "module_type", "claim", "evidence_type", "source", "source_detail", "evidence_tier", "direction", "confidence", "limitations", "next_action"]
SOURCE_COLUMNS = ["result_id", "cycle_id", "module_type", "figure_panel", "claim", "source_mode", "input_file_or_source", "simulation_status", "allowed_in_manuscript", "notes"]


def write_text(path: Path, content: str) -> None:
    if not path.exists():
        path.write_text(content, encoding="utf-8")


def write_csv(path: Path, columns: list[str]) -> None:
    if path.exists():
        return
    with path.open("w", newline="", encoding="utf-8-sig") as handle:
        csv.writer(handle).writerow(columns)


def main() -> None:
    parser = argparse.ArgumentParser(description="Scaffold a Co-Paper project.")
    parser.add_argument("--project", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()

    out = Path(args.out).resolve()
    for folder in [
        "01_plan", "02_results", "modules/bioinformatics_exploration",
        "modules/experimental_validation", "modules/bioinformatics_validation",
        "manuscript", "branches",
    ]:
        (out / folder).mkdir(parents=True, exist_ok=True)

    write_text(out / "project_state.md", f"# {args.project}\n\n- Created: {date.today().isoformat()}\n- Current stage: 01_plan\n- Current cycle: 1\n- Active claim: TBD\n- Next decision: approve the three-module Co-Plan\n")
    write_text(out / "decision_log.md", "# Decision Log\n")
    write_csv(out / "module_ledger.csv", MODULE_COLUMNS)
    write_csv(out / "evidence_ledger.csv", EVIDENCE_COLUMNS)
    write_csv(out / "source_mode_ledger.csv", SOURCE_COLUMNS)
    write_text(out / "manuscript" / "full_manuscript.md", "# 中文全文初稿\n")

    print(f"Created Co-Paper project workspace: {out}")


if __name__ == "__main__":
    main()
