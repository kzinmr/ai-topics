---
title: "Inference — LLM推論エンジン比較"
type: concept
aliases:
  - inference-engines
  - llm-inference
tags:
  - concept
  - inference
  - mlops
  - local-llm
  - serving
status: active
description: "LLM推論の3大エンジン: llama.cpp (ローカルCPU/GPU), vLLM (サーバー高スループット), SGLang (エージェント最適化)"
created: 2026-04-09
updated: 2026-04-24
sources:
  - "https://github.com/ggml-org/llama.cpp"
  - "https://github.com/vllm-project/vllm"
  - "https://github.com/sgl-project/sglang"
related:
  - "[[concepts/inference/llama-cpp]]"
  - "[[concepts/inference/vllm]]"
  - "[[concepts/inference/sglang]]"
  - "[[concepts/local-llm]]"
  - "[[concepts/inference-speed-development]]"
  - "[[concepts/gguf-quantization]]"
  - "[[concepts/serving-llms-vllm]]"
---

# Inference — LLM推論エンジン

LLM推論を最適化するための3大エンジンとその使い分け。

## 3大エンジン比較

| | **llama.cpp** | **vLLM** | **SGLang** |
|---|---|---|---|
| **開発元** | Georgi Gerganov (→ Hugging Face) | UC Berkeley / vLLM team | LMSYS Org (→ PyTorch) |
| **主要ターゲット** | ローカル/エッジ | サーバー/API | エージェント/RAG |
| **KV Cache** | 標準 | PagedAttention | RadixAttention (prefix共有) |
| **フォーマット** | GGUF専用 | HuggingFace | HuggingFace |
| **Hardware** | CPU, Apple Silicon, GPU | NVIDIA/AMD GPU | NVIDIA, AMD, Intel, **CPU対応** |
| **Structured Output** | ❌ | ❌ | ✅ xgrammar (ネイティブ) |
| **最大特徴** | 軽量・ローカル動作 | 高スループット・連続バッチ | 長い共有プレフィクスのキャッシュ |
| **2026年動向** | Hugging Face入り (Feb 2026), Speculative Checkpointing | 大規模デファクト | PyTorch入り (Mar 2025), RL rollout backend |

## 使い分け指針

### llama.cpp を選ぶ場合
- **ローカル/エッジ推論** — CPUやApple Siliconで動かしたい
- **GGUFモデル** — 量子化モデルを使用
- **軽量デプロイ** — 依存関係を最小限に
- **コンシューマーハード** — Mac, ラップトップ, Raspberry Pi
- Ollama, LM Studio, text-generation-webui の基盤エンジン

### vLLM を選ぶ場合
- **サーバー/APIデプロイ** — 高スループットが必要
- **マルチLoRA** — 複数のファインチューンモデルを同時に
- **連続バッチ** — 複数の同時リクエストを効率的に
- **本番環境のデファクト** — 最も実績がある

### SGLang を選ぶ場合
- **エージェントワークロード** — システムプロンプト/ツール定義が長い
- **RAGパイプライン** — 共有コンテキストが多い
- **構造化出力** — JSON Schema/regex制約付き生成
- **RLトレーニング** — フロンティアモデルのrollout backend
- **prefill-decode分離** — 高度なスケーリング

## 最新の最適化技術

### Speculative Checkpointing (llama.cpp, Apr 2026)
- VRAM使用量を最大40%削減
- トークンスループットを最大20%向上
- 推論中のメモリ状態管理を根本的に再設計

### RadixAttention (SGLang)
- リクエスト間で共通プレフィックスをツリー型KVキャッシュとして共有
- エージェントループで3-5倍のスループット向上
- シシステムプロンプト、ツール定義、few-shot例を1回計算して再利用

### PagedAttention (vLLM)
- 仮想メモリのページング概念をKVキャッシュ管理に応用
- メモリの断片化を解消し、スループットを最大化
- 24x throughput vs. HuggingFace Transformers (claim)

## 100K Stars (llama.cpp, Mar 2026)

Georgi Gerganov:
> "Now that 90% of the code worldwide is being written by AI agents, I predict that within 3-6 months, 90% of all AI agents will be running locally with llama.cpp 😄"

## 業界統合動向

| 日付 | イベント | 影響 |
|------|---------|------|
| 2025-03 | SGLang → PyTorch エコシステム入り | フレームワークの公式サポート |
| 2026-02 | llama.cpp → Hugging Face 入社 | モデル配布層と推論層の統合 |
| 2026-04 | Speculative Checkpointing マージ | ローカル推論の性能大幅向上 |

## 関連概念

- [[concepts/inference/llama-cpp]] — llama.cpp詳細
- [[concepts/inference/vllm]] — vLLM詳細
- [[concepts/inference/sglang]] — SGLang詳細
- [[concepts/gguf-quantization]] — 量子化フォーマット
- [[concepts/local-llm]] — ローカルLLMエコシステム
- [[concepts/inference-speed-development]] — 推論速度最適化
