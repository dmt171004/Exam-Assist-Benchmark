# Benchmark Report — Qwen3-VL-4B-Instruct Baseline

## Model

`/home/drnguyenvinh/Exam-Assistant/Bench_mark/models/qwen3_examassist_merged_4b_rslora_domain_v5`

## Dataset

`test-final_v3.jsonl`

Number of samples: **430**

- Answerable samples: **394**
- Unanswerable samples: **36**

## Main Results

### Answerable QA

| Metric | Value |
|---|---:|
| Answerable EM | 13.20% |
| Answerable Token F1 | 66.53% |
| Answerable ROUGE-L | 65.01% |
| Containment Accuracy | 42.89% |
| False Refusal Rate | 3.05% |

### Unanswerable QA

| Metric | Value |
|---|---:|
| Correct Refusal Rate | 94.44% |
| Hallucination Rate on Unanswerable | 5.56% |

### Overall

| Metric | Value |
|---|---:|
| Overall EM | 20.00% |
| Overall Token F1 | 68.87% |
| Overall ROUGE-L | 67.48% |
| Average Latency | 0.0283 sec/sample |
| Throughput | 35.32 samples/sec |

## Interpretation

This benchmark follows a SQuAD2.0 / ViQuAD2.0-style evaluation because the dataset contains both answerable and unanswerable questions.

For answerable samples, EM, Token F1, ROUGE-L, and Containment Accuracy measure answer quality. Containment Accuracy is useful when the model generates a complete sentence while the gold answer is a short span.

For unanswerable samples, Correct Refusal Rate measures whether the model correctly refuses to answer when the context does not contain the answer. Hallucination Rate measures cases where the model produces an answer despite the gold label being unanswerable.

## Output Files

- `qwen_predictions_fixed_metrics.jsonl`
- `qwen_predictions_fixed_metrics.csv`
- `qwen_summary_fixed_metrics.csv`
- `qwen_summary_fixed_metrics.json`
- `qwen_answerable_metrics.png`
- `qwen_unanswerable_behavior.png`
- `dataset_split.png`
- `qwen_answerable_f1_distribution.png`
