"""
analyze_prediction.py

Generate qualitative analysis files from prediction.csv.

Input:
    benchmark_outputs/<benchmark_folder>/qwen_predictions_fixed_metrics.csv

Output:
    benchmark_outputs/<benchmark_folder>/qualitative_analysis/
        hallucination_cases.csv
        false_refusal_cases.csv
        low_correctness_cases.csv
        unsafe_cases.csv
"""

from pathlib import Path

import pandas as pd


# ==========================================================
# CONFIG
# ==========================================================

PROJECT_ROOT = Path(__file__).resolve().parent

BENCHMARK_FOLDER = (
    "qwen3_vl_4b_finetuned(rslora-v5)_domain_test_20260710_151144"
)

PREDICTION_FILE = (
    PROJECT_ROOT
    / "benchmark_outputs"
    / BENCHMARK_FOLDER
    / "qwen_predictions_fixed_metrics.csv"
)

OUTPUT_DIR = (
    PROJECT_ROOT
    / "benchmark_outputs"
    / BENCHMARK_FOLDER
    / "qualitative_analysis"
)

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


# ==========================================================
# LOAD
# ==========================================================

df = pd.read_csv(PREDICTION_FILE)


# ==========================================================
# Columns
# ==========================================================

QUAL_COLUMNS = [
    "id",
    "question",
    "context",
    "gold_answer",
    "gold_answers_all",
    "prediction",
    "judge_reasoning",
    "llm_correctness",
    "hallucination",
    "false_refusal",
    "correct_refusal",
    "em",
    "f1",
    "rouge_l",
    "containment",
]


# ==========================================================
# Hallucination
# ==========================================================

hallucination_cases = (
    df[df["hallucination"] == 1]
    .sort_values(
        by=["llm_correctness", "f1"],
        ascending=True,
    )
)

hallucination_cases[QUAL_COLUMNS].to_csv(
    OUTPUT_DIR / "hallucination_cases.csv",
    index=False,
    encoding="utf-8-sig",
)


# ==========================================================
# False Refusal
# ==========================================================

false_refusal_cases = (
    df[df["false_refusal"] == 1]
    .sort_values(
        by=["llm_correctness", "f1"],
        ascending=True,
    )
)

false_refusal_cases[QUAL_COLUMNS].to_csv(
    OUTPUT_DIR / "false_refusal_cases.csv",
    index=False,
    encoding="utf-8-sig",
)


# ==========================================================
# Low Correctness
# ==========================================================

low_correctness_cases = (
    df[df["llm_correctness"] < 1.0]
    .sort_values(
        by=["llm_correctness", "f1"],
        ascending=True,
    )
)

low_correctness_cases[QUAL_COLUMNS].to_csv(
    OUTPUT_DIR / "low_correctness_cases.csv",
    index=False,
    encoding="utf-8-sig",
)


# ==========================================================
# Unsafe Cases
# ==========================================================

unsafe_cases = (
    df[
        (df["hallucination"] == 1)
        | (df["false_refusal"] == 1)
        | (df["llm_correctness"] < 0.5)
    ]
    .drop_duplicates()
    .sort_values(
        by=["llm_correctness", "f1"],
        ascending=True,
    )
)

unsafe_cases[QUAL_COLUMNS].to_csv(
    OUTPUT_DIR / "unsafe_cases.csv",
    index=False,
    encoding="utf-8-sig",
)


# ==========================================================
# Summary
# ==========================================================

print("=" * 60)
print("Qualitative Analysis")
print("=" * 60)
print(f"Prediction file     : {PREDICTION_FILE.name}")
print(f"Output folder       : {OUTPUT_DIR}")
print("-" * 60)
print(f"Hallucination cases : {len(hallucination_cases)}")
print(f"False refusal cases : {len(false_refusal_cases)}")
print(f"Low correctness     : {len(low_correctness_cases)}")
print(f"Unsafe cases        : {len(unsafe_cases)}")
print("=" * 60)