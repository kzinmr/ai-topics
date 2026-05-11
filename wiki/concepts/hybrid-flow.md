---
title: "HybridFlow (veRL)"
type: concept
aliases:
  - hybrid-flow
  - verl
created: 2026-05-08
updated: 2026-05-08
tags:
  - reinforcement-learning
  - fine-tuning
  - training
  - framework
  - infrastructure
  - architecture
  - ray
sources:
  - raw/articles/2025-06-02_verl-readthedocs_hybrid-flow-programming-guide.md
---

# HybridFlow (veRL)

> **HybridFlow** は、LLM の RLHF/GRPO トレーニングにおいて、**制御フロー（単一プロセス）と計算フロー（マルチプロセス）を分離する**アーキテクチャパターン。**veRL**（VolcEngine RL）はそのオープンソース実装。コントローラは Ray 上の単一プロセスとして動作し、WorkerGroup を通じてマルチ GPU の計算ワーカーと透過的にやり取りする。

## 背景と動機

### RL はなぜ特別なデータフロー問題なのか

深層強化学習（DRL）は通常のニューラルネットワーク訓練と根本的に異なる：

| 次元 | ニューラルネット訓練 | 強化学習 |
|------|---------------------|---------|
| **ノード** | 演算子（+/-/matmul/softmax） | 高レベル操作（rollout/model forward） |
| **エッジ** | テンソル移動 | データ移動 |

RL は **2階層のデータフロー問題** になる：

1. **Control Flow（制御フロー）**：RL アルゴリズムのコアロジック。PPO では「rollout → advantage計算 → training」の順序を定義
2. **Computation Flow（計算フロー）**：ニューラルネットワークの計算そのもの（forward/backward/optimizer）

LLM 以前の DRL ではモデルサイズが小さく、全処理が単一プロセスで完結していた。しかし LLM 時代の計算フロー（分散訓練）はマルチプロセス必須であり、設計上の選択を迫られる。

### 2つの設計選択

| アプローチ | 統一マルチコントローラ | **分離フロー（veRLの選択）** |
|-----------|----------------------|---------------------------|
| 方式 | 制御フローもマルチプロセス化し計算と同居 | 制御フローは単一プロセス、計算のみマルチプロセス |
| 利点 | 通信オーバーヘッド最小、最適性能 | 計算バックエンドの再利用が容易、新しいRLアルゴリズムの実装がシンプル |
| 欠点 | 制御と計算が密結合、FSDP→Megatron切り替えで両方作り直し | コントローラ⇔ワーカー間でデータ通信オーバーヘッド |

veRL は **柔軟性と再利用性を優先** し、分離フローを採用。GRPO, PPO, DPO などのアルゴリズムを、FSDP, Megatron, TorchTitan などのバックエンドから独立して実装できる。

## アーキテクチャ

```
┌─────────────────────────────────┐
│  Controller (単一プロセス)        │
│  ┌───────────────────────────┐  │
│  │  PPO/GRPO Main Loop       │  │
│  │  (ray_trainer.py)         │  │
│  └───────────────────────────┘  │
│           │  ▲                  │
│    データ送信 │ データ収集         │
│           ▼  │                  │
└──────────┬──┴───────────────────┘
           │
    ┌──────┴──────────────────────┐
    │  WorkerGroup (プロキシ層)     │
    │  - データ分割/分配/収集/結合    │
    └──────┬──────────────────────┘
           │
    ┌──────┼──────────────────────┐
    │      │       │              │
    ▼      ▼       ▼              ▼
┌────┐ ┌────┐ ┌────┐         ┌────┐
│W[0]│ │W[1]│ │W[2]│  ...    │W[N]│
│GPU0│ │GPU1│ │GPU2│         │GPUN│
└────┘ └────┘ └────┘         └────┘
   ActorRolloutRef / Critic / Reward
```

**主要コンポーネント**:

- **Controller（Driver）**: `main_task` として Ray 上で単一プロセス実行。RL アルゴリズムのメインループを担う。推奨：Ray クラスタのヘッドノードには配置しない（メモリ消費大）
- **WorkerGroup**: リモートワーカー群のプロキシ。データの分割・分配・収集・結合を透過的に処理
- **Worker**: GPU 上で実行される計算ユニット。`ActorRolloutRefWorker`, `CriticWorker`, `RewardWorker`
- **ResourcePool**: ワーカーが配置される GPU リソース集合

### 3つの WorkerGroup（PPO の場合）

| WorkerGroup | 役割 | 特徴 |
|------------|------|------|
| **ActorRolloutRef** | Actor（方策モデル）、Rollout（生成）、Reference（参照ポリシー） | 同一 GPU 上に colocate。Actor+Rollout 同居で NCCL 高速重み転送、Actor+Ref 同居で効率的 LoRA PPO |
| **Critic** | 価値関数モデル | 独立した GPU グループ |
| **Reward** | 報酬モデル（モデルベース報酬 + ルールベース報酬の合成可） | `RewardManager` でカスタマイズ可能。トークンレベル報酬を返す |

## プログラミングモデル：`@register` デコレータ

veRL の核心的イノベーションは **`@register` デコレータ**による透過的分散実行。

### 分散実行の3ステップを隠蔽

従来、コントローラがワーカーを呼び出すには以下の定型コードが必要だった：

```python
# 従来の手動分散
data_dp_lst = data.split(dp_size)           # 1. データ分割
output_dp_lst = []
for i, worker in enumerate(actor_rollout_ref_wg):
    output_future = worker.generate_sequences.remote(data_dp_lst[i])  # 2. 分配
    output_dp_lst.append(output_future)
output = torch.cat(ray.get(output_dp_lst), dim=0)  # 3. 収集・結合
```

veRL では `@register` がこれを隠蔽：

```python
# ワーカー側の定義
@register(dispatch_mode=Dispatch.DP_COMPUTE_PROTO)
def generate_sequences(data):
    ...

# コントローラ側 — まるでローカル関数のように呼べる
output = actor_rollout_ref_wg.generate_sequences(data)
```

`Dispatch.DP_COMPUTE_PROTO` は：
1. 入力をデータ並列サイズに分割
2. 各ワーカーに対応チャンクを分配
3. 出力を収集し連結

入力/出力は `DataProto`（`verl/protocol.py`）である必要がある。

### PPO メインループ（実コードに近い疑似コード）

```python
for prompt in dataloader:
    # すべての WorkerGroup 呼び出しが @register で透過化
    output       = actor_rollout_ref_wg.generate_sequences(prompt)
    old_log_prob = actor_rollout_ref_wg.compute_log_prob(output)
    ref_log_prob = actor_rollout_ref_wg.compute_ref_log_prob(output)
    values       = critic_wg.compute_values(output)
    rewards      = reward_wg.compute_scores(output)

    # advantage 計算はコントローラプロセス上で直接実行
    advantages = compute_advantages(values, rewards)

    # データを統合して更新
    output = output.union(old_log_prob, ref_log_prob, values, rewards, advantages)
    actor_rollout_ref_wg.update_actor(output)
    critic.update_critic(output)
```

**重要なポイント**：
- コントローラのコードは **単一プロセスのように読める**
- 計算バックエンド（FSDP/Megatron/TorchTitan）を切り替えても制御コードは変更不要
- WorkerGroup と ResourcePool のマッピングを変えるだけで配置を柔軟に変更可能

## コードベース構成

```
verl/
  trainer/
    main_ppo.py          # エントリポイント（main_task）
    ppo/ray_trainer.py   # PPOアルゴリズムのメインループ
  workers/
    protocol.py          # DataProto インターフェース
    engine_workers.py    # ActorRolloutRefWorker / TrainingWorker
    engine/              # 計算バックエンド
      fsdp/              # FSDP / FSDP2
      megatron/          # Megatron-LM
      torchtitan/        # TorchTitan
      veomni/            # veOmni
    rollout/             # 推論バックエンド
      vllm/              # vLLM (>= v0.7 SPMD)
      sglang_rollout/    # SGLang
      hf_rollout.py      # HuggingFace TGI
  utils/
    dataset/             # SFT/RM/RL データセット
    reward_score/        # ルールベース報酬関数（GSM8K, MATH 等）
  models/
    llama/               # Llama, DeepSeek, Mistral の Megatron 実装
    transformers/        # Ulysses 並列統合（Llama, Qwen 等）
```

### サポートするエンジンとバックエンド

| カテゴリ | バックエンド | 用途 |
|---------|------------|------|
| 訓練エンジン | FSDP, Megatron-LM, TorchTitan, veOmni | Actor/Critic の分散訓練 |
| 推論バックエンド | vLLM, SGLang, HuggingFace TGI | Rollout（生成） |

## トレードオフと制限

### 分離フローの代償

- **データ通信オーバーヘッド**：コントローラ ⇔ ワーカー間のデータ転送が都度発生。特に巨大なバッチや長いシーケンスで顕在化
- **コントローラのメモリ**：全ワーカーの出力を集約するため、コントローラプロセスに大きなメモリが必要

### 統一マルチコントローラが適するケース

- 制御フローが固定で変更不要な場合
- データ転送オーバーヘッドが致命的な超大規模訓練
- 特定のバックエンドに完全にロックインしている場合

### veRL が適するケース

- **新しい RL アルゴリズム（GRPO, RPG 等）を迅速に試したい**研究用途
- 複数の計算バックエンド（FSDP, Megatron, TorchTitan）を比較・切り替えたい場合
- Rollout バックエンド（vLLM, SGLang）の切り替え実験
- 異なる GPU 配置戦略を試したい場合

## エコシステムにおける位置づけ

| フレームワーク | アプローチ | 特徴 |
|-------------|----------|------|
| **veRL (HybridFlow)** | 制御/計算分離、Ray ベース | 柔軟性重視、マルチバックエンド |
| **TRL** | HuggingFace 統合、単一プロセス寄り | 使いやすさ重視、FSDP 連携 |
| **DeepSpeed-Chat** | DeepSpeed 密結合、ZeRO 最適化 | 性能重視、Megatron 連携 |
| **OpenRLHF** | Ray ベース、シンプル実装 | veRL より軽量、学習用途向け |

veRL は **DeepSeek-R1 の GRPO 訓練**に使用されたことで注目を集め、現在 RLHF/GRPO 訓練のデファクトスタンダードの一つとなっている。

### Anyscale比較（2025-07）における位置づけ

Anyscaleの10ライブラリ比較では、Verlは「成熟度・パフォーマンスで最も信頼できる選択肢」と評価。12.9k ⭐、351 contributorsとTRLに次ぐコミュニティ規模。

| 側面 | Verl | 競合 |
|------|------|------|
| 成熟度 | 高い（ByteDance、12.9k ⭐） | TRL (15.3k ⭐)に次ぐ |
| 拡張性 | FSDP+Megatron、複数推論エンジン | slime (Megatron+SGLang固定)より柔軟 |
| 環境/エージェント | 🚧 RFC段階、tool-calling経由 | SkyRL, RAGEN: ✅ フル環境対応 |
| Async | 🚧 RFC段階 | AReaL, slime: ✅ ネイティブ非同期 |
| エコシステム | RAGENなど派生ライブラリ多数 | TRL → Verifiers、Verl → RAGEN |

**VeRLベースの派生**: [[concepts/ragen|RAGEN]]（環境インターフェース追加）、hybrid-flowの制御/計算分離パターンは他ライブラリの設計にも影響。

→ 全RLライブラリ比較: [[comparisons/open-source-rl-libraries-comparison]]

## 関連ページ

- [[concepts/grpo-rl-training]] — veRL で実装される主要アルゴリズム
- [[concepts/fine-tuning/rlhf-dpo-preference]] — RLHF と DPO の全体像
- [[concepts/fine-tuning/trl]] — HuggingFace TRL との比較
- [[entities/deepseek]] — DeepSeek-R1 の GRPO 訓練に veRL を使用
- [[concepts/fine-tuning/grpo-rl-training]] — GRPO アルゴリズムの詳細

## 参考

- [HybridFlow 論文](https://arxiv.org/abs/2409.19256v2) — Chi Zhang et al.
- [veRL GitHub](https://github.com/volcengine/verl)
- [veRL 公式ドキュメント](https://verl.readthedocs.io/)
