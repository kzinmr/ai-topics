---
title: "TensorRT-LLM — NVIDIA Inference Optimization Engine"
type: concept
created: 2026-05-01
updated: 2026-05-01
tags:
  - concept
  - inference
  - nvidia
  - tensorrt
  - optimization
status: L1
aliases:
  - tensorrt-llm
  - nvidia-tensorrt
  - trt-llm
sources: []
related:
  - "[[concepts/inference/_index]]"
  - "[[concepts/inference/vllm]]"
  - "[[concepts/inference/sglang]]"
  - "[[concepts/serving-llms-vllm]]"
  - "[[concepts/kv-cache]]"
  - "[[concepts/ai-infrastructure-engineering/gpu-vram-fundamentals]]"
  - "[[concepts/ai-infrastructure-engineering/model-serving-autoscaling]]"
  - "[[concepts/ai-infrastructure-engineering/_index]]"
---

# TensorRT-LLM — NVIDIA Inference Optimization Engine

> NVIDIAが提供するLLM推論最適化エンジン。Triton Inference Serverと統合し、NVIDIA GPU（特にH100/B200）で最高の推論パフォーマンスを実現する。vLLMに対し、より低レイヤーのハードウェア最適化が可能。

## Why This Matters

TensorRT-LLMはNVIDIA GPUで**絶対的な最低レイテンシ**と**最高のハードウェア効率**を目指す。vLLMが汎用性とコミュニティ駆動の進化を重視するのに対し、TensorRT-LLMはNVIDIA GPUの機能（FP8 Transformer Engine、NVLink最適化、SM占有率チューニング）を最大限活用する。

## Outline

### 1. Architecture Overview

- **TensorRT Compiler**: モデルグラフを最適化されたCUDAカーネルにコンパイル
- **プラグインシステム**: FlashAttention, MoE, FP8推論の専用カーネル
- **重みのみの量子化**: INT4/INT8/FP8/Float32対応
- **KV Cache量子化**: INT8 KV Cacheによるメモリ削減
- **In-flight batching**: vLLMのcontinuous batchingに相当
- **Paged KV Cache**: vLLMのPagedAttentionに相当
- **Speculative Decoding**: 標準サポート（Medusa, Eagle対応）

### 2. Key Optimizations

| 機能 | 説明 | 効果 |
|------|------|------|
| **FP8 Quantization** | Transformer Engine活用 | H100/B200: 2x vs FP16 |
| **INT4 AWQ** | Activation-aware weight quantization | 4xメモリ削減、高品質維持 |
| **In-flight Batching** | 動的なバッチ管理 | vLLM同等のスループット |
| **PagedAttention** | 仮想メモリ型KV Cache管理 | メモリ断片化削減 |
| **Speculative Decoding** | Draftモデル+Targetモデル | 2-4xレイテンシ改善 |
| **Multi-GPU TP/PP** | Tensor/Pipeline Parallel | 大規模モデル対応 |
| **CUDA Graph Capture** | 完全なCUDA Graphキャプチャ | カーネル起動オーバーヘッド削減 |
| **SM Partitioning** | MIGに代わるGPUパーティショニング | 高効率マルチテナンシー |

### 3. vLLM vs TensorRT-LLM Comparison

| 観点 | vLLM | TensorRT-LLM |
|------|------|-------------|
| **開発元** | UC Berkeley (コミュニティ) | NVIDIA |
| **GPU最適化** | 汎用CUDA | NVIDIA専用、各世代に最適化 |
| **モデルサポート** | 広い（HF Hub経由） | 限定的（各モデル毎のビルド） |
| **コンパイル** | 不要（JIT/Fallback） | 必要（TensorRT IRビルド） |
| **Triton統合** | C API経由 | ネイティブ統合 |
| **デプロイ複雑性** | 低（pip install） | 高（Dockerビルド必須） |
| **ピークスループット** | 高い | 非常に高い |
| **最低レイテンシ** | 低い | 非常に低い |
| **コミュニティ** | 活発（広範なコントリビューター） | NVIDIA主導 |
| **ライセンス** | Apache 2.0 | NVIDIA Proprietary |

### 4. Deployment Patterns

- **Triton Inference Server + TensorRT-LLM backend**: 標準的な構成
- **Single GPU**: FP4/INT4量子化で1GPU内に70Bモデル
- **Multi-GPU**: TP/PPで分散、NVLinkが効果的
- **Multi-Node**: InfiniBand接続によるクラスタ推論
- **Mixed Models**: Tritonによるマルチモデル管理

### 5. Performance Benchmarks (概算)

| モデル | GPU | Engine | スループット (tok/s) | レイテンシ (ms/tok) |
|--------|-----|--------|---------------------|-------------------|
| LLaMA-2 70B (FP16) | 1x H100 | vLLM | ~1200 | ~25ms |
| LLaMA-2 70B (FP16) | 1x H100 | TRT-LLM | ~1500 | ~20ms |
| LLaMA-2 70B (FP8) | 1x H100 | TRT-LLM | ~2800 | ~10ms |
| GPT-175B (FP16) | 8x H100 | TRT-LLM | ~5000 | ~8ms |
| Nemotron-4 340B | 8x B200 | TRT-LLM | ~8000 | ~7ms |

*(注: 実測値はワークロードと設定によって大きく変動)*

### 6. When to Use TensorRT-LLM

#### ✅ 適しているケース
- NVIDIA GPUクラスタで最高のスループットが必要
- レイテンシSLOが厳しい（< 50ms P99）
- Triton Inference Server既存環境
- 推論コストの最小化が最優先
- CUDAカーネルレベルのチューニングが可能なチーム

#### ❌ 適さないケース
- 多様なモデルを頻繁に切り替える（ビルド時間）
- オープンソースの透明性が必要
- 小規模チーム（運用コストが高い）
- vLLMで十分なスループットが出ている
- Nvidia GPU以外（AMD, Intel, Apple Silicon）

### 7. Integration with Ecosystem

- **Triton Inference Server**: 標準backendとして統合
- **NVIDIA NIM**: コンテナ化されたマイクロサービス
- **Kubernetes + GPU Operator**: 自動デプロイ
- **NVIDIA AI Enterprise**: エンタープライズサポート
- **NeMo / Megatron-LM**: トレーニングからのシームレスなエクスポート

## Key Resources

- [TensorRT-LLM GitHub](https://github.com/NVIDIA/TensorRT-LLM)
- [Triton Inference Server](https://github.com/triton-inference-server/server)
- [NVIDIA NIM](https://build.nvidia.com/explore/reasoning)
- [NVIDIA GPU Operator](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/)

## Related Pages

- [[concepts/inference/_index]] — Inference engine comparison
- [[concepts/inference/vllm]] — vLLM (primary competitor)
- [[concepts/inference/sglang]] — SGLang (agent-optimized)
- [[concepts/serving-llms-vllm]] — vLLM serving patterns
- [[concepts/ai-infrastructure-engineering/gpu-vram-fundamentals]] — NVIDIA GPU capabilities
- [[concepts/ai-infrastructure-engineering/model-serving-autoscaling]] — Production serving infrastructure
- [[concepts/ai-infrastructure-engineering/_index]] — Parent page

## TODO

- [ ] Add detailed FP8/FP4 quantization benchmark results
- [ ] Add Triton Inference Server integration config examples
- [ ] Add Docker build process walkthrough
- [ ] Add multi-node TP/PP configuration guide
- [ ] Add speculative decoding support details (Eagle3, Medusa)
- [ ] Add TensorRT model format (.engine) build optimization tips
- [ ] Add benchmark methodology and caveats (prompt length, batch size effects)
