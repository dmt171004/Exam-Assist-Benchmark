"""
Aggregate benchmark summaries into a single comparison table.

Outputs
-------
benchmark_outputs/
    benchmark_comparison.csv
    benchmark_comparison.xlsx
    benchmark_comparison.md
"""

from pathlib import Path

import pandas as pd
import re

# ==========================================================
# CONFIG
# ==========================================================

ROOT = Path(__file__).resolve().parent

# Input
BENCHMARK_OUTPUT_DIR = ROOT / "benchmark_outputs"

# Output
REPORT_OUTPUT_DIR = ROOT / "benchmark_reports"

SUMMARY_FILENAME = "qwen_summary_fixed_metrics.csv"

REPORT_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


# ==========================================================
# UTILITIES
# ==========================================================

def infer_method(folder_name: str) -> str:
    name = folder_name.lower()

    if "baseline" in name:
        return "Baseline"

    if "finetuned(qlora)" in name or "(qlora)" in name:
        return "QLoRA"

    if re.search(r"rs\d+", name):
        return "RSLoRA"

    if "lora" in name:
        return "LoRA"

    return "Unknown"


def infer_version(folder_name: str) -> str:
    """
    Extract LoRA rank/version.

    baseline -> "-"
    qlora    -> "r=8" (or "-" if you don't want to show rank)
    rs8      -> "r=8"
    rs16     -> "r=16"
    rs32     -> "r=32"
    """
    name = folder_name.lower()

    if "baseline" in name:
        return "-"

    if "(qlora)" in name:
        return "r=8"      # hoặc "-" nếu QLoRA là baseline

    m = re.search(r"rs(\d+)", name)
    if m:
        return f"r={m.group(1)}"

    return "-"


def shorten_model(model_path: str) -> str:
    return Path(model_path).name

# ==========================================================
# MAIN
# ==========================================================

summary_files = sorted(BENCHMARK_OUTPUT_DIR.rglob(SUMMARY_FILENAME))

if not summary_files:
    raise FileNotFoundError(
        f"No '{SUMMARY_FILENAME}' found under:\n{BENCHMARK_OUTPUT_DIR}"
    )

print(f"Found {len(summary_files)} benchmark summaries.\n")

records = []

for summary_file in summary_files:

    print(f"Reading: {summary_file.relative_to(ROOT)}")

    df = pd.read_csv(summary_file)

    if df.empty:
        print("  -> Skip (empty file)")
        continue

    row = df.iloc[0]

    folder_name = summary_file.parent.name

    records.append(
        {
            # ==================================================
            # Model Information
            # ==================================================
            "Model": shorten_model(row["model"]),
            "Method": infer_method(folder_name),
            "Version": infer_version(folder_name),

            # ==================================================
            # Accuracy
            # ==================================================
            "Overall EM": row["overall_em"],
            "Overall F1": row["overall_f1"],
            "ROUGE-L": row["overall_rouge_l"],

            # ==================================================
            # Grounding
            # ==================================================
            "Containment": row["answerable_containment"],


            # ==================================================
            # Safety
            # ==================================================
            "False Refusal": row["false_refusal_rate_answerable"],
            "Correct Refusal": row["correct_refusal_rate_unanswerable"],
            "Hallucination": row["hallucination_rate_unanswerable"],

            # ==================================================
            # Efficiency
            # ==================================================
            "Latency (s)": row["avg_latency_sec"],
            "Throughput (samples/s)": row["throughput_samples_per_sec"],
        }
    )

comparison = pd.DataFrame(records)

if comparison.empty:
    raise RuntimeError("No benchmark summaries were successfully loaded.")



# ==========================================================
# Sort
# ==========================================================

method_order = {
    "Baseline": 0,
    "LoRA": 1,
    "QLoRA": 2,
    "RSLoRA": 3,
    "Unknown": 99,
}

comparison["__order"] = (comparison["Method"].map(method_order).fillna(99))

comparison = (comparison.sort_values(by=["__order", "Version", "Model"],ignore_index=True,).drop(columns="__order"))

# ==========================================================
# Round numeric columns
# ==========================================================

numeric_columns = comparison.select_dtypes(include="number").columns

comparison[numeric_columns] = (comparison[numeric_columns].round(4))

# ==========================================================
# EXPORT
# ==========================================================

csv_path = REPORT_OUTPUT_DIR / "benchmark_comparison.csv"
xlsx_path = REPORT_OUTPUT_DIR / "benchmark_comparison.xlsx"
md_path = REPORT_OUTPUT_DIR / "benchmark_comparison.md"

comparison.to_csv(csv_path, index=False)

comparison.to_excel(xlsx_path, index=False)

with open(md_path, "w", encoding="utf-8") as f:
    f.write(comparison.to_markdown(index=False))

print("=" * 60)
print("Benchmark comparison generated")
print(csv_path)
print(xlsx_path)
print(md_path)
print("=" * 60)

# ==========================================================
# VISUALIZATION
# ==========================================================

import matplotlib.pyplot as plt


def build_display_name(row: pd.Series) -> str:
    """
    Build a concise display name for plots.
    """

    if row["Method"] == "Baseline":
        return "Baseline"

    return f'{row["Method"]}-{row["Version"].lower()}'


comparison["Display"] = comparison.apply(build_display_name, axis=1)


def save_comparison_chart(
    df: pd.DataFrame,
    metrics: list[str],
    title: str,
    ylabel: str,
    filename: str,
):
    """
    Save grouped bar chart with value labels.
    """

    plot_df = df.set_index("Display")[metrics]

    ax = plot_df.plot(
        kind="bar",
        figsize=(10, 6),
        width=0.8,
    )

    # ------------------------------------------------------
    # Figure style
    # ------------------------------------------------------

    ax.set_title(
        title,
        fontsize=15,
        fontweight="bold",
        pad=15,
    )

    ax.set_xlabel("")
    ax.set_ylabel(ylabel, fontsize=12)

    ax.set_xticklabels(
        plot_df.index,
        rotation=0,
        fontsize=11,
    )

    ax.grid(
        axis="y",
        linestyle="--",
        alpha=0.35,
    )

    ax.legend(
        frameon=True,
        fontsize=10,
    )

    # ------------------------------------------------------
    # Add value labels
    # ------------------------------------------------------

    for container in ax.containers:

        labels = []

        for bar in container:

            height = bar.get_height()

            if pd.isna(height):
                labels.append("")
            else:
                labels.append(f"{height:.2f}")

        ax.bar_label(
            container,
            labels=labels,
            padding=3,
            fontsize=9,
        )

    # ------------------------------------------------------
    # Make room for labels
    # ------------------------------------------------------

    ymax = plot_df.max().max()

    ax.set_ylim(0, ymax * 1.18)

    plt.tight_layout()

    plt.savefig(
        REPORT_OUTPUT_DIR / filename,
        dpi=300,
        bbox_inches="tight",
    )

    plt.close()


# ==========================================================
# Accuracy & Grounding
# ==========================================================

save_comparison_chart(
    comparison,
    metrics=[
        "Overall EM",
        "Overall F1",
        "ROUGE-L",
        "Containment",
    ],
    title="Accuracy and Grounding Comparison",
    ylabel="Score (%)",
    filename="accuracy_comparison.png",
)


# ==========================================================
# Safety
# ==========================================================

save_comparison_chart(
    comparison,
    metrics=[
        "False Refusal",
        "Correct Refusal",
        "Hallucination",
    ],
    title="Safety Comparison",
    ylabel="Rate (%)",
    filename="safety_comparison.png",
)


# ==========================================================
# Inference Efficiency
# ==========================================================

save_comparison_chart(
    comparison,
    metrics=[
        "Latency (s)",
        "Throughput (samples/s)",
    ],
    title="Inference Efficiency Comparison",
    ylabel="Value",
    filename="efficiency_comparison.png",
)

print("\nVisualization generated:")
print(REPORT_OUTPUT_DIR / "accuracy_comparison.png")
print(REPORT_OUTPUT_DIR / "safety_comparison.png")
print(REPORT_OUTPUT_DIR / "efficiency_comparison.png")