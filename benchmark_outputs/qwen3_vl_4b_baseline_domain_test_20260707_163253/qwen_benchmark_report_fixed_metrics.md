# Benchmark Report — Qwen3-VL-4B-Instruct Baseline

## Model

`/home/drnguyenvinh/Exam-Assistant/Bench_mark/models/Qwen3-VL-4B-Instruct`

## Dataset

`test-final_v3.jsonl`

Number of samples: **430**

- Answerable samples: **394**
- Unanswerable samples: **36**

## Main Results

### Answerable QA

| Metric | Value |
|---|---:|
| Answerable EM | 9.14% |
| Answerable Token F1 | 63.11% |
| Answerable ROUGE-L | 60.84% |
| Containment Accuracy | 34.52% |
| False Refusal Rate | 0.76% |

### Unanswerable QA

| Metric | Value |
|---|---:|
| Correct Refusal Rate | 72.22% |
| Hallucination Rate on Unanswerable | 22.22% |

### Overall

| Metric | Value |
|---|---:|
| Overall EM | 14.42% |
| Overall Token F1 | 63.87% |
| Overall ROUGE-L | 61.80% |
| Average Latency | 0.0483 sec/sample |
| Throughput | 20.68 samples/sec |

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
