# ExamAssist AI Benchmark Framework

A comprehensive benchmarking framework for evaluating domain-adapted Large Language Models (LLMs) in examination support systems.

This repository contains the benchmark pipeline developed for evaluating both pretrained and fine-tuned LLMs using automatic metrics, LLM-as-a-Judge evaluation, and computational efficiency analysis.

> **Scope:** This repository focuses only on model evaluation and benchmarking.
>
> - 🎯 Fine-tuning pipeline: **[Training Repository](https://github.com/yourname/examassist-training)**
> - 🚀 Complete RAG System: **[Main Repository](https://github.com/yourname/examassist-system)**

---

# Overview

This benchmark framework was designed to answer two fundamental questions:

1. **Does domain-specific fine-tuning improve response quality?**
2. **Has the model actually learned domain knowledge, or is it only relying on retrieved context?**

To answer these questions, two complementary benchmark protocols are provided.

---

# Benchmark Protocols

## 1. Context Benchmark (RAG Evaluation)

Evaluates the model when relevant context is provided.

This benchmark measures the model's ability to:

- generate accurate answers
- utilize retrieved knowledge correctly
- avoid hallucinations
- refuse unsupported questions
- maintain factual consistency

Typical evaluation targets include:

- Baseline Model
- Fine-tuned Model
- Baseline + RAG
- Fine-tuned + RAG
- API Models

---

## 2. No-Context Benchmark (Knowledge Evaluation)

Evaluates the model **without any external context**.

This benchmark is designed to measure how much domain knowledge has actually been learned during fine-tuning.

Instead of testing retrieval capability, it evaluates the internal knowledge stored in the model parameters.

This protocol is useful for comparing:

- Pretrained model
- Fine-tuned model
- Different fine-tuning strategies
- Different LoRA configurations
- Open-source models vs API models

---

# Benchmark Pipeline

```text
                 Candidate Models
                        │
                        ▼
              Prediction Generation
                        │
        ┌───────────────┴────────────────┐
        │                                │
        ▼                                ▼
 Automatic Evaluation             LLM-as-a-Judge
        │                                │
        ├── Exact Match                  ├── Correct Refusal Rate
        ├── F1 Score                     ├── False Refusal Rate
        ├── ROUGE-L                      ├── Hallucination Rate
        ├── Containment Accuracy         └── Faithfulness
        │
        └── Computational Efficiency
              ├── Latency
              └── Throughput

                 └──────────────┬──────────────┘
                                ▼
                Overall Performance Analysis
                                │
                                ▼
                   Model Comparison Report
```

---

# Evaluation Metrics

## Answer Quality

- Exact Match (EM)
- Token-level F1
- ROUGE-L
- Containment Accuracy

---

## Reliability

Evaluated using an LLM-as-a-Judge.

- Correct Refusal Rate (CRR)
- False Refusal Rate (FRR)
- Hallucination Rate (HR)
- Faithfulness

---

## Computational Efficiency

- Average Latency
- Throughput (samples/second)

---

# Features

- Unified benchmark pipeline
- Context and No-Context evaluation
- Automatic metric computation
- LLM-as-a-Judge evaluation
- API model benchmarking
- Open-source model benchmarking
- CSV result export
- Automatic summary generation
- Error analysis support

---

# Repository Structure

```
benchmark/
│
├── datasets/
│
├── benchmark_context/
│
├── benchmark_no_context/
│
├── metrics/
│
├── llm_judge/
│
├── evaluation/
│
├── outputs/
│
└── notebooks/
```

---

# Typical Workflow

```
Select Candidate Models
          │
          ▼
Run Benchmark
          │
          ├── Context Benchmark
          │
          └── No-Context Benchmark
                     │
                     ▼
Metric Evaluation
                     │
                     ▼
Generate Benchmark Report
                     │
                     ▼
Model Comparison
```

---

# Supported Models

The framework supports any OpenAI-compatible or Hugging Face causal language model.

Examples include:

- Qwen3-VL
- GPT-4o-mini
- Fine-tuned LoRA models
- vLLM deployments
- OpenAI-compatible APIs

---

# Related Repositories

### Fine-tuning Repository

Contains the complete QLoRA training pipeline, dataset preparation, and model adaptation process.

➡️ [https://github.com/yourname/examassist-training](https://github.com/dmt171004/Exam-Assist-Finetuning)

---

### Main System Repository

Contains the production-ready ExamAssist AI system integrating Hybrid RAG and the fine-tuned language model.

➡️ [https://github.com/yourname/examassist-system](https://github.com/dinhkhoi124/Exam-Proctor-Assist/tree/main)

---

# License

MIT License
