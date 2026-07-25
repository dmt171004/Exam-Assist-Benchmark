# Benchmark Report — gpt-4o-mini (No-Context Direct QA)

## Model & Setup
- **Model:** `gpt-4o-mini`
- **Provider:** API
- **Evaluation Type:** No-Context (Direct Question Answering)
- **Dataset Path:** `data/test-final_v3.jsonl`

## Dataset Split
- Total samples: **430**
- Answerable samples: **394**
- Unanswerable samples: **36**

## Main Results

### Answerable Questions
| Metric | Value |
|---|---:|
| Answerable EM | 0.00% |
| Answerable Token F1 | 15.91% |
| Answerable ROUGE-L | 12.92% |
| Containment Accuracy | 1.02% |

### Overall Performance & Latency
| Metric | Value |
|---|---:|
| Overall EM | 0.00% |
| Overall Token F1 | 14.94% |
| Overall ROUGE-L | 12.14% |
| Average Latency | 1.9730 sec/sample |
| Throughput | 0.51 samples/sec |
| Total Time | 848.41 sec |

## Evaluation Methodology
This run evaluates the parametric knowledge of `gpt-4o-mini` directly via API without providing context documents.

- **Exact Match (EM), Token F1, ROUGE-L, Containment:** Evaluated against reference gold answers using standard rule-based NLP normalization.
- **Rule-based Evaluation:** Fast, reproducible execution without local LLM Judge overhead.

## Generated Output Files
- `predictions_no_context.jsonl`
- `predictions_no_context.csv`
- `summary_no_context.csv`
- `summary_no_context.json`
- `answerable_metrics.png`
- `dataset_split.png`
- `answerable_f1_distribution.png`
