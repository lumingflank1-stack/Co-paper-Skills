#!/usr/bin/env python3
"""Create blank Co-Plan files for one planning round."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path


DATASET_COLUMNS = [
    "dataset_id",
    "source_database",
    "accession",
    "title",
    "species",
    "tissue_or_cell_type",
    "data_type",
    "comparison",
    "required_metadata",
    "download_status",
    "local_path",
    "analysis_role",
    "expected_signal",
    "minimum_success_condition",
    "notes",
]


def write_text(path: Path, content: str) -> None:
    if not path.exists():
        path.write_text(content, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Create Co-Plan template files.")
    parser.add_argument("--out", required=True, help="Output directory")
    args = parser.parse_args()

    out = Path(args.out).resolve()
    out.mkdir(parents=True, exist_ok=True)

    write_text(
        out / "selected_hypothesis.md",
        "# Selected Hypothesis\n\n- Selected module:\n- Co-Debate hypothesis ID and rank:\n- Selected hypothesis:\n- User selection reason:\n- Main alternative explanation:\n- Falsification criteria:\n- Evidence gaps:\n",
    )

    write_text(
        out / "analysis_plan.md",
        "# Analysis Plan\n\n## Active Claim\n\n## Input Data\n\n## Required Metadata\n\n## Preprocessing and QC\n\n## Main Comparison or Model\n\n## Covariates and Confounders\n\n## Decision Rules\n\n## Expected Tables\n\n## Expected Figures\n\n## Failure Modes\n",
    )
    write_text(
        out / "experiment_plan.md",
        "# Experiment Plan\n\n## Decisive Experiment\n\n- Model:\n- Samples:\n- Perturbation:\n- Rescue:\n- Stimulation:\n- Controls:\n- Time points:\n- Readouts:\n- Expected support result:\n- Falsification result:\n- Sample size logic:\n- Technical risks:\n- Backup plan:\n",
    )
    write_text(
        out / "virtual_result_prompt.md",
        "# Virtual Result Prompt\n\nYou are generating virtual planning data for manuscript drafting. Write downstream manuscript-facing prose in conventional Results style, and record virtual source status only in the report or source ledger unless visible labels are requested.\n\n- Research topic:\n- Active hypothesis:\n- Desired result mode: positive / negative / ambiguous / mixed\n- Assays to simulate:\n- Groups:\n- Replicates:\n- Expected direction:\n- Required tables:\n- Required figure summaries:\n- Source-status requirement: record virtual status in the report or source ledger; do not repeat labels in every table, figure caption, or result paragraph unless requested.\n",
    )
    write_text(out / "next_module_decision_rules.md", "# Next Module Decision Rules\n")
    write_text(out / "risks_and_controls.md", "# Risks and Controls\n")

    dataset_manifest = out / "dataset_manifest.csv"
    if not dataset_manifest.exists():
        with dataset_manifest.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.writer(handle)
            writer.writerow(DATASET_COLUMNS)

    print(f"Created Co-Plan templates: {out}")


if __name__ == "__main__":
    main()
