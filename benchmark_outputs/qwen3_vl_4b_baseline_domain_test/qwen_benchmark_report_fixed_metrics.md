# Benchmark Report — Qwen3-VL-4B-Instruct Baseline

## Model

`/home/drnguyenvinh/Exam-Assistant/Bench_mark/models/Qwen3-VL-4B-Instruct`

## Judge Model (local)

`/home/drnguyenvinh/Exam-Assistant/Bench_mark/models/Qwen3-8B`

## Dataset

`data/test-final_v3.jsonl`

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
| False Refusal Rate | 0.51% |

### Unanswerable QA

| Metric | Value |
|---|---:|
| Correct Refusal Rate | 61.11% |
| Hallucination Rate on Unanswerable | 22.22% |

### Overall

| Metric | Value |
|---|---:|
| Overall EM | 13.49% |
| Overall Token F1 | 62.94% |
| Overall ROUGE-L | 60.87% |
| Average Latency | 0.0483 sec/sample |
| Throughput | 20.71 samples/sec |

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
