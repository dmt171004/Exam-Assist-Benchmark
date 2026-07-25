# Benchmark Report — Qwen3-VL-4B-Instruct Baseline

## Model
`/home/drnguyenvinh/Exam-Assistant/Bench_mark/models/Qwen3-VL-4B-Instruct`

## Dataset
`data/test-final_v3.jsonl`

Number of samples: **430**
- Answerable samples: **430**
- Unanswerable samples: **0**

## Main Results

### Answerable QA
| Metric | Value |
|---|---:|
| Answerable EM | 0.00% |
| Answerable Token F1 | 13.54% |
| Answerable ROUGE-L | 11.30% |
| Containment Accuracy | 0.70% |


### Overall
| Metric | Value |
|---|---:|
| Overall EM | 0.00% |
| Overall Token F1 | 13.54% |
| Overall ROUGE-L | 11.30% |
| Average Generated Tokens | 105.53 |
| Average Latency | 0.1500 sec/sample |
| Throughput | 6.67 samples/sec |

## Interpretation
This benchmark follows a SQuAD2.0 / ViQuAD2.0-style evaluation because the dataset contains both answerable and unanswerable questions.

For answerable samples, EM, Token F1, ROUGE-L, and Containment Accuracy measure answer quality. Containment Accuracy is useful when the model generates a complete sentence while the gold answer is a short span.

For unanswerable samples, Correct Refusal Rate measures whether the model correctly refuses to answer. Hallucination Rate measures cases where the model produces an answer despite the gold label being unanswerable.

All metrics in this run are rule-based (no LLM-as-judge step).

## Output Files
- `qwen_predictions_fixed_metrics.jsonl`
- `qwen_predictions_fixed_metrics.csv`
- `qwen_summary_fixed_metrics.csv`
- `qwen_summary_fixed_metrics.json`
- `qwen_answerable_metrics.png`
- `dataset_split.png`
- `qwen_answerable_f1_distribution.png`
