# Benchmark Report — Qwen3-VL-4B-Instruct Baseline

## Model

`/home/drnguyenvinh/Exam-Assistant/Bench_mark/models/Qwen3-VL-4B-Instruct`

## Judge Model (local)

`/home/drnguyenvinh/Exam-Assistant/Bench_mark/models/Qwen3-8B`

## Dataset

`taidng/UIT-ViQuAD2.0`

Number of samples: **3814**

- Answerable samples: **2653**
- Unanswerable samples: **1161**

## Main Results

### Answerable QA

| Metric | Value |
|---|---:|
| Answerable EM | 16.81% |
| Answerable Token F1 | 56.23% |
| Answerable ROUGE-L | 54.77% |
| Containment Accuracy | 70.30% |
| False Refusal Rate | 0.19% |

### Unanswerable QA

| Metric | Value |
|---|---:|
| Correct Refusal Rate | 12.66% |
| Hallucination Rate on Unanswerable | 37.47% |

### Overall

| Metric | Value |
|---|---:|
| Overall EM | 15.55% |
| Overall Token F1 | 42.97% |
| Overall ROUGE-L | 41.95% |
| Average Latency | 0.0713 sec/sample |
| Throughput | 14.03 samples/sec |

## Interpretation

This benchmark follows a SQuAD2.0 / ViQuAD2.0-style evaluation because the dataset contains both answerable and unanswerable questions.

For answerable samples, EM, Token F1, ROUGE-L, and Containment Accuracy measure answer quality. Containment Accuracy is useful when the model generates a complete sentence while the gold answer is a short span.

For unanswerable samples, Correct Refusal Rate measures whether the model correctly refuses to answer when the context does not contain the answer. Hallucination Rate measures cases where the model produces an answer despite the gold label being unanswerable.

LLM-as-judge scoring (refusal / hallucination / faithfulness) is now performed locally with `/home/drnguyenvinh/Exam-Assistant/Bench_mark/models/Qwen3-8B` via vLLM instead of calling an external API.

## Output Files

- `qwen_predictions_fixed_metrics.jsonl`
- `qwen_predictions_fixed_metrics.csv`
- `qwen_summary_fixed_metrics.csv`
- `qwen_summary_fixed_metrics.json`
- `qwen_answerable_metrics.png`
- `qwen_unanswerable_behavior.png`
- `dataset_split.png`
- `qwen_answerable_f1_distribution.png`
