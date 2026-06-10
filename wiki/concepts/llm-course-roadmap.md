---
title: LLM Course Roadmap (Maxime Labonne)
type: concept
created: 2026-05-04
updated: 2026-05-04
status: Level2
tags:
  - curriculum
  - methodology
  - education
aliases: [mlabonne-llm-course, llm-curriculum]
sources:
  - https://github.com/mlabonne/llm-course
  - https://packt.link/a/9781836200079
---

# LLM Course Roadmap

A **knowledge map** mapping the LLM learning roadmap presented in **Maxime Labonne's** LLM Course (GitHub 78.9k ⭐) to existing Wiki concepts. This is not a specific technical concept itself, but meta-knowledge about **how to systematically learn** the LLM domain, serving as a navigation tool for understanding coverage gaps and guiding future expansion of this Wiki.

> **Source:** https://github.com/mlabonne/llm-course
> **Book Edition:** [LLM Engineer's Handbook](https://packt.link/a/9781836200079) (Packt, 2024)

---

## 🛠️ Overall Structure

The LLM Course consists of three layers:

```
Part 1: LLM Fundamentals
    ↓
Part 2: The LLM Scientist (Model Building & Training)
    ↓
Part 3: The LLM Engineer (Application & Deployment)
```

Below is the coverage mapping for each layer within this Wiki.

---

## 🧩 Part 1: LLM Fundamentals

Prerequisite knowledge for understanding LLMs. This part rarely exists as independent concept pages, but it forms the assumed knowledge base for this Wiki's existing pages.

### Math Foundations

| Topic | Wiki Coverage | Notes |
|------|---------------|------|
| Linear Algebra (vectors, matrices) | — | Implicitly assumed as prerequisite |
| Calculus (gradients, optimization) | — | Same as above |
| Probability & Statistics (Bayesian, hypothesis testing) | — | Same as above |

### Python Ecosystem

| Topic | Wiki Coverage | Notes |
|------|---------------|------|
| NumPy / Pandas | — | Implicitly assumed as tool knowledge |
| Matplotlib / Seaborn | — | Same as above |
| Scikit-learn | — | Same as above |

### Neural Network Foundations

| Topic | Wiki Coverage | Notes |
|------|---------------|------|
| Layers, weights, activation functions | — | Implicit assumption |
| Backpropagation, optimization (AdamW) | — | Same as above |
| Transformer Architecture | [[concepts/transformer-architecture]] | Covered |
| Attention Mechanism | [[concepts/attention-mechanism-variants]] | Covered |

### NLP Foundations

| Topic | Wiki Coverage | Notes |
|------|---------------|------|
| Tokenization | — | No concept page (mentioned briefly in [[concepts/llm-training-fundamentals]]) |
| TF-IDF / RNN / LSTM / GRU | — | Assumed as historical context |

> **Coverage Rate:** ~20% (prerequisite knowledge is outside Wiki scope, but Transformer/Attention are covered as independent concepts)

---

## 🧑‍🔬 Part 2: The LLM Scientist

Covers model architecture, training, and evaluation. The area with the most overlap with this Wiki's core topics.

### Section 1: Architecture & Pre-training

| Topic | Wiki Coverage | Notes |
|----------|---------------|------|
| Transformer Evolution (encoder-decoder → decoder-only) | [[concepts/transformer-architecture]] | Covers GPT-style decoder-only evolution |
| Self-Attention Mechanism | [[concepts/attention-mechanism-variants]] | Includes various attention variants |
| Large-Scale Pre-training (Data/Pipeline/Tensor Parallel) | — | No concept page for distributed training strategies (partially covered in [[concepts/fsdp-qlora]]) |

### Section 2: Post-Training & Fine-Tuning

**Supervised Fine-Tuning (SFT)**

| Topic | Wiki Coverage | Notes |
|----------|---------------|------|
| SFT Overview | [[concepts/fine-tuning-post-training-overview]] | Systematically covered |
| PEFT (LoRA / QLoRA) | [[concepts/peft-lora-and-qlora]], [[concepts/qlora]], [[concepts/fsdp-qlora]] | Rich coverage |
| Axolotl | [[concepts/axolotl-fine-tuning-framework]] | Covered |
| Unsloth | [[concepts/unsloth-fast-fine-tuning]] | Covered |
| TRL (Transformer Reinforcement Learning) | [[concepts/trl-transformer-reinforcement-learning]] | Covered |

**Preference Alignment**

| Topic | Wiki Coverage | Notes |
|----------|---------------|------|
| DPO (Direct Preference Optimization) | [[concepts/rlhf-dpo-orpo-kto-preference-optimization]] | Comprehensive coverage of DPO/ORPO/KTO |
| PPO / GRPO | [[concepts/grpo-rl-training]] | GRPO well-covered in DeepSeek context |
| RLHF Overall | [[concepts/ai-safety-and-alignment]], [[concepts/ai-safety-alignment-rlhf-scalable-oversight-interpretability]] | Covered |

### Section 3: Evaluation & Quantization

**Evaluation**

| Topic | Wiki Coverage | Notes |
|----------|---------------|------|
| LLM-as-a-Judge | [[concepts/llm-as-judge]], [[concepts/llm-as-judge-evaluation-methodology-human-in-the-loop]] | Rich coverage |
| Benchmarks (MMLU, etc.) | [[concepts/open-llm-leaderboard]], [[concepts/llm-evaluation]], [[concepts/llm-evaluation-harness]], [[concepts/ai-benchmarks/lighteval]] | Rich (incl. lm-eval-harness) |
| Human Evaluation (Chatbot Arena) | [[concepts/ai-evals]] | Reference |
| Agent Evaluation | [[concepts/evals-for-ai-agents]], [[concepts/evaluation-flywheel]], [[concepts/evaluation-coding-agents-mcp-automation-harness-engineering]], [[concepts/process-reward-models-agent-eval]] | Unique depth |

**Quantization**

| Topic | Wiki Coverage | Notes |
|----------|---------------|------|
| Quantization Basics | [[concepts/model-quantization]], [[concepts/model-quantization-for-local-llms]] | Rich coverage |
| GGUF | [[concepts/gguf-quantization]], [[concepts/local-llm]] | Covered |
| GPTQ / AWQ / EXL2 | [[concepts/turboquant]] | Partial |
| HQQ | Mentioned in [[concepts/fsdp-qlora]] | In Mobius Labs / Dropbox context |
| llama.cpp | [[concepts/local-llm/llama-cpp]] | Covered |

> **Coverage Rate:** ~70% (aligns with Wiki's strength areas)

---

## 👷 Part 3: The LLM Engineer

Covers production applications, RAG, agents, and deployment. Since this Wiki is focused on agents, coverage in this area is uneven.

### Section 1: RAG (Retrieval-Augmented Generation)

| Topic | Wiki Coverage | Notes |
|----------|---------------|------|
| Vector Stores (Chroma/Pinecone/Milvus) | — | No individual tool pages |
| LangChain / LlamaIndex | — | No framework pages (possibly intentionally absent due to agent focus) |
| Query Construction (Text-to-SQL) | — | Not covered |
| Re-ranking | [[concepts/rags]], [[concepts/modern-retrieval-toolkit]] | Partially covered |
| DSPy | Indirectly via [[concepts/multiple-representations-rag]] etc. | No independent page |
| Graph RAG | [[concepts/agentic-alternative-to-graphrag]], [[concepts/graph-db-overengineering-rag]] | Unique depth |
| RAGatouille | [[concepts/ragatouille]] | Covered |

### Section 2: Agents & Autonomy

| Topic | Wiki Coverage | Notes |
|----------|---------------|------|
| Thought → Action → Observation Loop | [[concepts/agent-loop-orchestration]], [[concepts/agentic-scaffolding]], [[concepts/agents-scaffolding-composition-inference-scaling-hypothesis]] | Rich coverage |
| MCP (Model Context Protocol) | [[concepts/agent-communication-protocols]], [[concepts/agent-communication-standards]] | Covered |
| LangGraph / CrewAI / AutoGen | [[concepts/agent-orchestration-frameworks]] | Compared |
| Multi-Agent | [[concepts/agent-swarms]], [[concepts/agent-team-swarm]] | Covered |
| Coding Agents | [[concepts/agentic-coding]], [[concepts/agentic-engineering]], [[concepts/agentic-engineering-patterns]], [[concepts/claude-code-prompt-engineering-context-management-caching-agent-architecture]] | Very rich |

### Section 3: Deployment & Security

| Topic | Wiki Coverage | Notes |
|----------|---------------|------|
| Flash Attention | [[concepts/flashattention-pytorch-educational]], [[concepts/flashattention-pytorch-educational-implementation]] | Covered |
| Speculative Decoding | — | No concept page |
| vLLM | [[concepts/serving-llms-vllm]], [[concepts/vllm]] | Covered |
| TGI | [[concepts/inference/tgi]] | Covered (new) |
| LM Studio / Ollama | [[concepts/ollama-local-llm-runner]], [[concepts/local-llm]] | Covered |
| MLC LLM (Edge) | — | Not covered |
| Prompt Injection Defense | [[concepts/prompt-engineering-resilience-design-patterns]], [[concepts/resilient-prompt-engineering]], [[concepts/red-teaming-adversarial-eval]] | Covered |
| Garak (Red Teaming) | — | No individual tool page |
| Langfuse (Observability) | [[concepts/evaluation-tools-langsmith-braintrust-arize-phoenix-inspect-ai]] | Indirect mention |

> **Coverage Rate:** ~60% (agent area is very rich, gaps in RAG and deployment tools)

---

## 📊 Overall Coverage Assessment

| Part | Coverage Rate | Gaps | Priority |
|--------|------------|---------|--------|
| Part 1: Fundamentals | ~20% | Prerequisites outside Wiki scope. Only Transformer/Attention covered | Low |
| Part 2: The Scientist | ~70% | Missing distributed training strategies page. Speculative Decoding not covered | Medium |
| Part 3: The Engineer | ~60% | Gaps in LangChain/LlamaIndex, vector DBs, Edge inference | Low-Medium |

### Key Gaps (Topics Without Concept Pages)

1. **Distributed Training Strategies** (Data/Pipeline/Tensor Parallel) — Only FSDP covered in [[concepts/fsdp-qlora]]
2. **Speculative Decoding** — Important inference optimization technique
3. **LangChain / LlamaIndex** — Intentionally absent due to agent focus, but referenced in RAG context
4. **Vector DBs** (Chroma / Pinecone / Milvus) — RAG infrastructure
5. **MLC LLM** — Edge inference framework
6. **Garak** — Red Teaming tool

---

## 🤖 Automation Tools Provided by the LLM Course

Colab notebooks provided by Labonne alongside the Course. This Wiki doesn't have tool-specific pages, but some are linked to concepts.

| Tool | Purpose | Related Wiki Concept |
|--------|------|-------------|
| [LLM AutoEval](https://github.com/mlabonne/llm-autoeval) | Automated evaluation pipeline (RunPod) | [[concepts/llm-evaluation-harness]] |
| [LazyMergekit](https://colab.research.google.com/drive/1obulZ1ROXHjYLn6PPZJwRR6GzgQogxxb) | One-click model merge Colab | — |
| [LazyAxolotl](https://colab.research.google.com/drive/1TsDKNo2riwVmU55gjuBgB1AXVtRRfRHW) | Cloud fine-tuning | [[concepts/axolotl-fine-tuning-framework]] |
| [AutoQuant](https://colab.research.google.com/drive/1b6nqC7UZVt8bx4MksX7s656GXPM-eWw4) | GGUF/GPTQ/EXL2/AWQ/HQQ quantization | [[concepts/model-quantization]] |
| [AutoAbliteration](https://colab.research.google.com/drive/1RmLv-pCMBBsQGXQIM8yF-OdCNyoylUR1) | Model uncensoring | — |
| [AutoDedup](https://colab.research.google.com/drive/1o1nzwXWAa8kdkEJljbJFW1VuI-3VZLUn) | Dataset deduplication | — |

---

## 🔗 Related Wiki Pages

- [[entities/maxime-labonne]] — Creator of this course
- [[concepts/fine-tuning-post-training-overview]] — Post-training overview
- [[concepts/peft-lora-and-qlora]] — PEFT methods
- [[concepts/rlhf-dpo-orpo-kto-preference-optimization]] — Preference optimization
- [[concepts/agentic-engineering-patterns]] — Agentic engineering (corresponds to Part 3)
- [[concepts/llm-core]] — LLM foundations

---

> **This page is meta-knowledge (a knowledge map) that maps the LLM Course curriculum structure to this Wiki's existing concepts. For explanations of individual technical concepts, refer to the linked pages.**
