---
title: LLM Course Roadmap (Maxime Labonne)
type: concept
created: 2026-05-04
updated: 2026-05-04
status: Level2
tags: [curriculum, meta-knowledge, roadmap, llm-education]
aliases: [mlabonne-llm-course, llm-curriculum]
sources:
  - https://github.com/mlabonne/llm-course
  - https://packt.link/a/9781836200079
---

# LLM Course Roadmap

**Maxime Labonne** の LLM Course（GitHub 78.9k ⭐）が提示するLLM学習ロードマップを、既存のWiki概念にマッピングした**知識マップ**。これは個別の技術概念そのものではなく、LLM領域の知識を**どう体系的に学ぶか**というメタ知識であり、当Wikiにおけるカバレッジの把握や今後の拡充方針のためのナビゲーションツールとして機能する。

> **出典:** https://github.com/mlabonne/llm-course
> **書籍版:** [LLM Engineer's Handbook](https://packt.link/a/9781836200079) (Packt, 2024)

---

## 🛠️ 全体構造

LLM Courseは3層構造で構成される：

```
Part 1: LLM Fundamentals（前提知識）
    ↓
Part 2: The LLM Scientist（モデルの構築・訓練）
    ↓
Part 3: The LLM Engineer（アプリケーションへの応用）
```

各層について、当Wikiでのカバレッジを以下にマッピングする。

---

## 🧩 Part 1: LLM Fundamentals（前提知識）

LLMを理解するための前提知識。このパートは他の概念ページとして独立して存在することは少ないが、当Wikiの既存ページが前提とする知識群。

### 数学基礎

| 分野 | Wikiカバレッジ | 備考 |
|------|---------------|------|
| 線形代数（ベクトル・行列） | — | 前提知識として暗黙に想定 |
| 微分積分（勾配・最適化） | — | 同上 |
| 確率統計（ベイズ推定・仮説検定） | — | 同上 |

### Pythonエコシステム

| 分野 | Wikiカバレッジ | 備考 |
|------|---------------|------|
| NumPy / Pandas | — | ツール知識として暗黙に想定 |
| Matplotlib / Seaborn | — | 同上 |
| Scikit-learn | — | 同上 |

### ニューラルネットワーク基礎

| 分野 | Wikiカバレッジ | 備考 |
|------|---------------|------|
| レイヤー・重み・活性化関数 | — | 暗黙の前提 |
| 誤差逆伝播・最適化（AdamW） | — | 同上 |
| Transformerアーキテクチャ | [[concepts/transformer-architecture]] | カバー済み |
| Attention機構 | [[concepts/attention-mechanism-variants]] | カバー済み |

### NLP基礎

| 分野 | Wikiカバレッジ | 備考 |
|------|---------------|------|
| トークナイゼーション | — | 概念ページ未作成（[[concepts/llm-training-fundamentals]]で触れる程度） |
| TF-IDF / RNN / LSTM / GRU | — | 歴史的文脈として想定 |

> **カバレッジ率:** ~20%（前提知識はWikiのスコープ外だが、Transformer/Attentionは独立した概念としてカバー）

---

## 🧑‍🔬 Part 2: The LLM Scientist

モデルのアーキテクチャ、訓練、評価を扱う。当Wikiのコアトピックと最も重なる部分。

### セクション1: アーキテクチャと事前学習

| トピック | Wikiカバレッジ | 備考 |
|----------|---------------|------|
| Transformer進化（encoder-decoder → decoder-only） | [[concepts/transformer-architecture]] | GPT系decoder-onlyの変遷はカバー |
| Self-Attention機構 | [[concepts/attention-mechanism-variants]] | 各種attention variant含む |
| 大規模事前学習（Data/Pipeline/Tensor Parallel） | — | 分散訓練戦略の概念ページ未作成（[[concepts/fsdp-qlora]]で一部触れる） |

### セクション2: ポストトレーニングとファインチューニング

**Supervised Fine-Tuning (SFT)**

| トピック | Wikiカバレッジ | 備考 |
|----------|---------------|------|
| SFTの概要 | [[concepts/fine-tuning-post-training-overview]] | 体系的にカバー |
| PEFT（LoRA / QLoRA） | [[concepts/peft-lora-and-qlora]], [[concepts/qlora]], [[concepts/fsdp-qlora]] | 充実 |
| Axolotl | [[concepts/axolotl-fine-tuning-framework]] | カバー済み |
| Unsloth | [[concepts/unsloth-fast-fine-tuning]] | カバー済み |
| TRL（Transformer Reinforcement Learning） | [[concepts/trl-transformer-reinforcement-learning]] | カバー済み |

**Preference Alignment**

| トピック | Wikiカバレッジ | 備考 |
|----------|---------------|------|
| DPO（Direct Preference Optimization） | [[concepts/rlhf-dpo-orpo-kto-preference-optimization]] | DPO/ORPO/KTO包括的にカバー |
| PPO / GRPO | [[concepts/grpo-rl-training]] | GRPOはDeepSeek文脈で充実 |
| RLHF全体 | [[concepts/ai-safety-and-alignment]], [[concepts/ai-safety-alignment-rlhf-scalable-oversight-interpretability]] | カバー済み |

### セクション3: 評価と量子化

**Evaluation**

| トピック | Wikiカバレッジ | 備考 |
|----------|---------------|------|
| LLM-as-a-Judge | [[concepts/llm-as-judge]], [[concepts/llm-as-judge-evaluation-methodology-human-in-the-loop]] | 充実 |
| ベンチマーク（MMLU等） | [[concepts/open-llm-leaderboard]], [[concepts/llm-evaluation]], [[concepts/llm-evaluation-harness]], [[concepts/lighteval]] | 充実（lm-eval-harness含む） |
| Human Evaluation（Chatbot Arena） | [[concepts/ai-evals]] | 参照 |
| Agent評価 | [[concepts/evals-for-ai-agents]], [[concepts/evaluation-flywheel]], [[concepts/evaluation-coding-agents-mcp-automation-harness-engineering]], [[concepts/process-reward-models-agent-eval]] | 独自の深みあり |

**Quantization**

| トピック | Wikiカバレッジ | 備考 |
|----------|---------------|------|
| 量子化の基礎 | [[concepts/model-quantization]], [[concepts/model-quantization-for-local-llms]] | 充実 |
| GGUF | [[concepts/gguf-quantization]], [[concepts/local-llm]] | カバー済み |
| GPTQ / AWQ / EXL2 | [[concepts/turboquant]] | 一部 |
| HQQ | [[concepts/fsdp-qlora]]内で言及 | Mobius Labs / Dropbox文脈 |
| llama.cpp | [[concepts/local-llm/llama-cpp]] | カバー済み |

> **カバレッジ率:** ~70%（Wikiの強み領域と合致）

---

## 👷 Part 3: The LLM Engineer

プロダクション応用、RAG、エージェント、デプロイを扱う。当Wikiはエージェントに特化しているため、この領域のカバレッジは偏りがある。

### セクション1: RAG（Retrieval-Augmented Generation）

| トピック | Wikiカバレッジ | 備考 |
|----------|---------------|------|
| ベクトルストア（Chroma/Pinecone/Milvus） | — | 個別ツールページなし |
| LangChain / LlamaIndex | — | フレームワークページなし（エージェントフォーカスのため意図的欠落か） |
| Query Construction（Text-to-SQL） | — | 未カバー |
| Re-ranking | [[concepts/rags]], [[concepts/modern-retrieval-toolkit]] | 一部カバー |
| DSPy | [[concepts/multiple-representations-rag]]などで間接的に | 独立ページなし |
| グラフRAG | [[concepts/agentic-alternative-to-graphrag]], [[concepts/graph-db-overengineering-rag]] | 独自の深みあり |
| RAGatouille | [[concepts/ragatouille]] | カバー済み |

### セクション2: エージェントと自律性

| トピック | Wikiカバレッジ | 備考 |
|----------|---------------|------|
| Thought → Action → Observation ループ | [[concepts/agent-loop-orchestration]], [[concepts/agentic-scaffolding]], [[concepts/agents-scaffolding-composition-inference-scaling-hypothesis]] | 充実 |
| MCP（Model Context Protocol） | [[concepts/agent-communication-protocols]], [[concepts/agent-communication-standards]] | カバー済み |
| LangGraph / CrewAI / AutoGen | [[concepts/agent-orchestration-frameworks]] | 比較あり |
| マルチエージェント | [[concepts/agent-swarms]], [[concepts/agent-team-swarm]] | カバー済み |
| コーディングエージェント | [[concepts/agentic-coding]], [[concepts/agentic-engineering]], [[concepts/agentic-engineering-patterns]], [[concepts/claude-code-prompt-engineering-context-management-caching-agent-architecture]] | 非常に充実 |

### セクション3: デプロイとセキュリティ

| トピック | Wikiカバレッジ | 備考 |
|----------|---------------|------|
| Flash Attention | [[concepts/flashattention-pytorch-educational]], [[concepts/flashattention-pytorch-educational-implementation]] | カバー済み |
| Speculative Decoding | — | 概念ページ未作成 |
| vLLM | [[concepts/serving-llms-vllm]], [[concepts/vllm]] | カバー済み |
| TGI | [[concepts/inference/tgi]] | カバー済み（新規） |
| LM Studio / Ollama | [[concepts/ollama-local-llm-runner]], [[concepts/local-llm]] | カバー済み |
| MLC LLM（Edge） | — | 未カバー |
| Prompt Injection対策 | [[concepts/prompt-engineering-resilience-design-patterns]], [[concepts/resilient-prompt-engineering]], [[concepts/red-teaming-adversarial-eval]] | カバー済み |
| Garak（Red Teaming） | — | 個別ツールページなし |
| Langfuse（Observability） | [[concepts/evaluation-tools-langsmith-braintrust-arize-phoenix-inspect-ai]] | 間接的言及 |

> **カバレッジ率:** ~60%（エージェント領域は非常に充実、RAGとデプロイツールにギャップあり）

---

## 📊 総合カバレッジ評価

| パート | カバレッジ率 | ギャップ | 優先度 |
|--------|------------|---------|--------|
| Part 1: Fundamentals | ~20% | 前提知識はWikiのスコープ外。Transformer/Attentionのみカバー | 低 |
| Part 2: The Scientist | ~70% | 分散訓練戦略のページ不足。Speculative Decoding未カバー | 中 |
| Part 3: The Engineer | ~60% | LangChain/LlamaIndex、ベクトルDB、Edge推論にギャップ | 低〜中 |

### Key Gaps（概念ページ未作成のトピック）

1. **分散訓練戦略**（Data/Pipeline/Tensor Parallel）— [[concepts/fsdp-qlora]]でFSDPのみカバー
2. **Speculative Decoding** — 推論最適化の重要手法
3. **LangChain / LlamaIndex** — エージェントフォーカスゆえ意図的欠落だが、RAG文脈で参照される
4. **ベクトルDB**（Chroma / Pinecone / Milvus）— RAG基盤
5. **MLC LLM** — Edge推論フレームワーク
6. **Garak** — Red Teamingツール

---

## 🤖 LLM Course提供の自動化ツール

LabonneがCourseと併せて提供するColabノートブック群。当Wikiではツール自体のページはないが、一部は概念と紐づく。

| ツール | 目的 | 関連Wiki概念 |
|--------|------|-------------|
| [LLM AutoEval](https://github.com/mlabonne/llm-autoeval) | 自動評価パイプライン（RunPod） | [[concepts/llm-evaluation-harness]] |
| [LazyMergekit](https://colab.research.google.com/drive/1obulZ1ROXHjYLn6PPZJwRR6GzgQogxxb) | モデルマージのワンクリックColab | — |
| [LazyAxolotl](https://colab.research.google.com/drive/1TsDKNo2riwVmU55gjuBgB1AXVtRRfRHW) | クラウドファインチューニング | [[concepts/axolotl-fine-tuning-framework]] |
| [AutoQuant](https://colab.research.google.com/drive/1b6nqC7UZVt8bx4MksX7s656GXPM-eWw4) | GGUF/GPTQ/EXL2/AWQ/HQQ量子化 | [[concepts/model-quantization]] |
| [AutoAbliteration](https://colab.research.google.com/drive/1RmLv-pCMBBsQGXQIM8yF-OdCNyoylUR1) | モデルの検閲解除 | — |
| [AutoDedup](https://colab.research.google.com/drive/1o1nzwXWAa8kdkEJljbJFW1VuI-3VZLUn) | データセット重複除去 | — |

---

## 🔗 関連Wikiページ

- [[entities/maxime-labonne]] — 本コースの作成者
- [[concepts/fine-tuning-post-training-overview]] — ポストトレーニング全体像
- [[concepts/peft-lora-and-qlora]] — PEFT手法
- [[concepts/rlhf-dpo-orpo-kto-preference-optimization]] — 選好最適化
- [[concepts/agentic-engineering-patterns]] — エージェントエンジニアリング（Part 3に対応）
- [[concepts/llm-core]] — LLM基礎

---

> **このページはメタ知識（知識マップ）であり、LLM Courseのカリキュラム構造を当Wikiの既存概念にマッピングしたものである。個別の技術概念の解説は各リンク先を参照すること。**
