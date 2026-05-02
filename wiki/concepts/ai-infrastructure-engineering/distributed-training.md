---
title: "Distributed Training — DDP / FSDP / DeepSpeed"
type: concept
created: 2026-05-01
updated: 2026-05-01
tags:
  - concept
  - training
  - fsdp
  - deepspeed
  - ddp
  - infrastructure
status: L1
aliases:
  - distributed-training
  - ddp-fsdp-deepspeed
  - 3d-parallelism
  - model-parallelism
sources: []
related:
  - "[[concepts/pytorch-fsdp-distributed-training]]"
  - "[[concepts/fine-tuning/pytorch-fsdp]]"
  - "[[concepts/fine-tuning/peft-lora-qlora]]"
  - "[[concepts/llm-inference]]"
  - "[[concepts/ai-infrastructure-engineering/gpu-vram-fundamentals]]"
  - "[[concepts/ai-infrastructure-engineering/_index]]"
---

# Distributed Training — DDP / FSDP / DeepSpeed

> 大規模言語モデル（LLM）の分散学習に必要な並列化戦略の包括的ガイド。DDP（Data Distributed Parallel）からFSDP（Fully Sharded Data Parallel）、DeepSpeed ZeROまで、メモリ効率と計算効率のトレードオフを理解する。

## Why This Matters

単一GPUで学習できるモデルサイズにはVRAMの物理的限界がある。70BモデルをBF16で学習するには140GB以上のVRAMが必要で、これは現存する最大の単一GPU（B200: 144GB）でもギリギリ。分散並列化は必須であり、正しい戦略の選択が学習コストと時間に直結する。

## Outline

### 1. 並列化の基本次元（3D Parallelism）

```
                     Data Parallel
                    /      |      \
         Tensor Parallel    |    Pipeline Parallel
                    \      |      /
                 Expert Parallel (MoE only)
```

| 方式 | 分割対象 | 通信量 | 主なユースケース |
|------|---------|--------|-----------------|
| **Data Parallel (DDP)** | データ | 小（勾配のみ） | モデルが1GPUに収まる場合 |
| **FSDP (ZeRO-based)** | パラメータ+勾配+optimizer | 中（シャード通信） | モデルが1GPUに収まらない場合 |
| **Tensor Parallel** | テンソルの次元 | 大（全アクティベーション） | 単一ノード内、NVLink高速 |
| **Pipeline Parallel** | Transformerレイヤー | 小（アクティベーション境界のみ） | モデルが大きすぎる場合 |
| **Expert Parallel** | MoEの専門家 | 中（all-to-all） | MoEモデル専用 |

### 2. Data Distributed Parallel (DDP)

- 各GPUが完全なモデルコピーを持ち、異なるデータシャードを処理
- 順伝播・逆伝播を独立実行後、勾配をall-reduceで同期
- **制限**: モデル全体が単一GPU VRAMに収まる必要がある
- **Pros**: 実装がシンプル、通信オーバーヘッドが小さい
- **Cons**: VRAM消費が大きい（70Bモデルでは不可）

### 3. Fully Sharded Data Parallel (FSDP)

- モデルパラメータ・勾配・optimizer状態を全GPUでシャーディング
- 各forwardパスで必要なパラメータだけをall-gatherで収集（**unshard**）
- 計算後は再びシャードを破棄
- `sharding_strategy` の3段階:
  - `NO_SHARD` = DDP相当
  - `SHARD_GRAD_OP` = optimizer状態のみシャード
  - `FULL_SHARD` = パラメータ+勾配+optimizer全てシャード（ZeRO-3相当）

**FSDPのトレードオフ**:
- メモリ節約: 〜70%（70Bモデルで140GB → 2.5GB/GPU @ 64GPU）
- 通信オーバーヘッド: ほぼ一定でスケールに強い
- CPUオフロード: さらにメモリ削減可能（ただし10〜30倍低速）

### 4. DeepSpeed ZeRO (ZeRO-1/2/3)

Microsoft DeepSpeedの3段階最適化:

| Stage | Shard対象 | メモリ削減 | 通信量 | いつ使うか |
|-------|-----------|-----------|--------|-----------|
| **ZeRO-1** | Optimizer statesのみ | 4x | 小 | optimizer状態が支配的な場合 |
| **ZeRO-2** | Optimizer + Gradients | 8x | 中 | デフォルト推奨 |
| **ZeRO-3** | Optimizer + Gradients + Parameters | メモリ集約型モデル専用 | 大（all-gather per layer） | モデルがVRAMに収まらない場合 |

**DeepSpeed追加機能**:
- **ZeRO-Offload**: optimizer状態をCPU/NVMeにオフロード
- **ZeRO-Infinity**: モデル全体をCPU/NVMeに置き、必要なレイヤーのみGPUにロード
- **Mixture of Experts (MoE)**: DeepSpeed-MoEによるエキスパート並列
- **Autotuning**: 自動的な並列化戦略の選択

### 5. Pipeline Parallelism

- Transformerの異なるレイヤー群を別GPUに配置
- 各GPUは担当レイヤーの計算のみを行う
- **問題**: パイプラインのバブル（アイドル時間）をどう最小化するか
- **解決策**: GPipe（マイクロバッチ分割）、1F1B（One-Forward-One-Backward）

### 6. Tensor Parallelism

- 単一のテンソル演算（例: アテンションのQKV）をGPU間で分割
- Megatron-LMスタイル: row/column parallel分割
- **設定**: ノード内（NVLink接続必須）、高い通信帯域幅が必要

### 7. 戦略選択ガイド

| モデルサイズ | 推奨戦略 | 理由 |
|-------------|---------|------|
| ≤ 7B | DDP or FSDP NO_SHARD | 単一GPUに収まる、シンプルで高速 |
| 7B-30B | FSDP FULL_SHARD | メモリ効率とスケーラビリティのバランス |
| 30B-100B | FSDP + Tensor Parallel | モデルが大きくTPで縮退次元を削減 |
| 100B+ (Dense) | FSDP + TP + PP (3D) | 3次元最適化が必須 |
| MoE (100B+) | FSDP + TP + EP | Expert Parallelが追加次元 |

### 8. 実用的な設定例

- **70B model / 8x H100 (80GB)**:
  - FSDP FULL_SHARD + CPU Offload → 可能（ただし遅い）
  - FSDP + TP=2 → 効率的（各GPU内のシャードが小さくなる）
  
- **7B model / 4x A100 (40GB)**:
  - FSDP FULL_SHARD or DDP → 両方可能
  - LoRA/QLoRAでさらに効率化

- **DeepSpeed ZeRO-3 + Offload**:
  - 1台のコンシューマーGPUでも70Bモデルのfine-tuningが理論上可能
  - 速度はH100の約1/30

## Related Pages

- [[concepts/pytorch-fsdp-distributed-training]] — Stub → FSDP詳細
- [[concepts/fine-tuning/pytorch-fsdp]] — FSDP fine-tuning specifics
- [[concepts/fine-tuning/peft-lora-qlora]] — PEFT方法との組み合わせ
- [[concepts/fine-tuning/trl]] — TRL training with distributed configs
- [[concepts/ai-infrastructure-engineering/gpu-vram-fundamentals]] — GPU VRAM制約の基礎
- [[concepts/ai-infrastructure-engineering/_index]] — Parent page

## Skills Reference

- `pytorch-fsdp` — FSDP distributed training setup
- `axolotl` — Axolotl fine-tuning with FSDP configs
- `fine-tuning-with-trl` — TRL with distributed backends

## Key Resources

- [PyTorch FSDP Documentation](https://pytorch.org/docs/stable/fsdp.html)
- [DeepSpeed Documentation](https://www.deepspeed.ai/)
- [Megatron-LM](https://github.com/NVIDIA/Megatron-LM)
- [NVIDIA NCCL Documentation](https://developer.nvidia.com/nccl)

## TODO

- [ ] Add concrete FSDP config snippets (sharding_strategy, limit_all_gathers)
- [ ] Add DeepSpeed ZeRO config example (ds_config.json)
- [ ] Add 3D parallelism topology diagram
- [ ] Add benchmark comparison: DDP vs FSDP vs DeepSpeed for same model
- [ ] Add NCCL performance tuning tips (NVLink vs PCIe)
- [ ] Add CPU/NVMe Offload performance benchmarks
- [ ] Add DeepSpeed-MoE specific guidance
