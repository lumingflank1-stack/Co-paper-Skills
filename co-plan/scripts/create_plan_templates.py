#!/usr/bin/env python3
"""Create blank Co-Plan files for one three-module evidence cycle."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path


DATASET_COLUMNS = [
    "dataset_id", "module", "source_database", "accession", "species",
    "tissue_or_cell_type", "data_type", "comparison", "required_metadata",
    "download_status", "local_path", "analysis_role", "independent_from",
    "minimum_success_condition", "notes",
]

CLAIM_COLUMNS = [
    "claim_id", "claim", "exploration_source", "experimental_test",
    "bioinformatics_validation", "independence_check", "rescue_required",
    "minimum_evidence", "status",
]


def write_text(path: Path, content: str) -> None:
    if not path.exists():
        path.write_text(content, encoding="utf-8")


def write_csv(path: Path, columns: list[str]) -> None:
    if path.exists():
        return
    with path.open("w", newline="", encoding="utf-8-sig") as handle:
        csv.writer(handle).writerow(columns)


def main() -> None:
    parser = argparse.ArgumentParser(description="Create Co-Plan three-module templates.")
    parser.add_argument("--out", required=True, help="Output directory")
    args = parser.parse_args()

    out = Path(args.out).resolve()
    out.mkdir(parents=True, exist_ok=True)

    write_text(out / "research_question_and_claim.md", "# Research Question and Claim\n\n- Field/disease/context:\n- Molecule/intervention:\n- Active claim:\n- Main alternative:\n- Falsification boundary:\n")
    write_text(out / "integrated_three_module_plan.md", "# Integrated Three-Module Plan\n\n## Bioinformatics Exploration\n\n## Experimental Validation\n\n## Bioinformatics Validation\n\n## Integrated Decision Rules\n")
    write_text(out / "bioinformatics_exploration_plan.md", "# Bioinformatics Exploration Plan\n\n## Discovery question\n\n## Data and QC\n\n## Contrast and model\n\n## Candidate prioritization\n\n## Figures\n\n## Decision rules\n")
    write_text(out / "experimental_validation_plan.md", "# Experimental Validation Plan\n\n## Model and groups\n\n## Perturbation\n\n## Phenotype and molecular readouts\n\n## Direct interaction or mechanism\n\n## Controls and rescue\n\n## Decisive test\n\n## Decision rules\n")
    write_text(out / "bioinformatics_validation_plan.md", "# Bioinformatics Validation Plan\n\n## Independent or orthogonal data\n\n## Replication target\n\n## Robustness and specificity\n\n## Clinical or external validation\n\n## Independence check\n\n## Decision rules\n")
    write_text(out / "decision_rules.md", "# Decision Rules\n\n- Strong support:\n- Partial support:\n- Neutral:\n- Contradictory:\n- Not interpretable:\n")
    write_text(out / "risks_controls_and_rescue.md", "# Risks, Controls, and Rescue\n")
    write_text(out / "data_download_priority.md", "# Data Download Priority\n")
    write_text(out / "co_result_handoff.md", "# Co-Result Handoff\n\n- Active claim:\n- Exploration status:\n- Experimental validation status:\n- Bioinformatics validation status:\n- Rescue status:\n- Source modes:\n")
    write_csv(out / "claim_module_map.csv", CLAIM_COLUMNS)
    write_csv(out / "exploration_dataset_manifest.csv", DATASET_COLUMNS)
    write_csv(out / "validation_dataset_manifest.csv", DATASET_COLUMNS)

    print(f"Created Co-Plan templates: {out}")


if __name__ == "__main__":
    main()
