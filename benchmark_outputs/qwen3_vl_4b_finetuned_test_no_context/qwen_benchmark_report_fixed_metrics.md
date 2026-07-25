# Benchmark Report — Qwen3-VL-4B-Instruct Baseline

## Model
`/home/drnguyenvinh/Exam-Assistant/Bench_mark/models/qwen3_examassist_merged_4b_rslora_domain_v3`

## Dataset
`data/test-final_v3.jsonl`

Number of samples: **430**
- Answerable samples: **430**
- Unanswerable samples: **0**

## Main Results

### Answerable QA
| Metric | Value |
|---|---:|
| Answerable EM | 19.07% |
| Answerable Token F1 | 67.27% |
| Answerable ROUGE-L | 65.96% |
| Containment Accuracy | 27.67% |


### Overall
| Metric | Value |
|---|---:|
| Overall EM | 19.07% |
| Overall Token F1 | 67.27% |
| Overall ROUGE-L | 65.96% |
| Average Latency | 0.0289 sec/sample |
| Throughput | 34.56 samples/sec |

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
