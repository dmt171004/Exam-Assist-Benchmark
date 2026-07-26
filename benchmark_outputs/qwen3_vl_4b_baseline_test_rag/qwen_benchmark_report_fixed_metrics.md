# Benchmark Report — Qwen3-VL-4B RAG Benchmark

## Model

`/home/drnguyenvinh/Exam-Assistant/Bench_mark/models/Qwen3-VL-4B-Instruct`

## Judge Model (local)

`/home/drnguyenvinh/Exam-Assistant/Bench_mark/models/Qwen3-8B`

## Retrieval

- Pipeline: question → standalone module_rag → target model
- Retrieved context is used by both generation and the local judge.

## Dataset

`/home/drnguyenvinh/Exam-Assistant/Bench_mark/data/test-final_v3.jsonl`

Number of samples: **430**

- Answerable samples: **394**
- Unanswerable samples: **36**

## Main Results

### Answerable QA

| Metric | Value |
|---|---:|
| Answerable EM | 0.25% |
| Answerable Token F1 | 24.55% |
| Answerable ROUGE-L | 21.48% |
| Containment Accuracy | 3.05% |
| False Refusal Rate | 10.15% |

### Unanswerable QA

| Metric | Value |
|---|---:|
| Correct Refusal Rate | 80.56% |
| Hallucination Rate on Unanswerable | 2.78% |

### Overall

| Metric | Value |
|---|---:|
| Overall EM | 6.98% |
| Overall Token F1 | 29.24% |
| Overall ROUGE-L | 26.42% |
| Average Latency | 0.1704 sec/sample |
| Throughput | 5.87 samples/sec |

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
