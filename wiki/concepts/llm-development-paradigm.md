---
title: LLM Development Paradigm
created: 2026-05-19
updated: 2026-05-19
type: concept
tags: [training, post-training, alignment, dpo, rlhf, synthetic-data, scaling, peft, fine-tuning, llm, benchmark, evaluation]
aliases: [two-stage training, pre-training post-training pipeline]
sources:
  - raw/papers/2024-07-23_2407.21783_llama-3-herd-of-models.md
related:
  - entities/llama-3.md
  - concepts/scaling-laws.md
  - concepts/grpo-rl-training.md
  - concepts/dpo-alignment.md
---

# LLM Development Paradigm（LLM開発パラダイム）

**LLM Development Paradigm** は、大規模言語モデル（LLM）の開発を **事前学習（Pre-training）→ 事後学習（Post-training）** の二段階で行う標準的手法。2024年の Llama 3 論文で体系的に確立され、その後のほぼすべてのフロンティアモデル開発の基礎となっている。

## 二段階パラダイム

```
┌─────────────────────┐     ┌──────────────────────────────────┐
│  Stage 1: Pre-training │ ──→ │  Stage 2: Post-training            │
│  - Next-token prediction│     │  - SFT (Supervised Fine-Tuning)    │
│  - 15T+ tokens           │     │  - Rejection Sampling              │
│  - 3.8×10²⁵ FLOPs       │     │  - DPO / RLHF                      │
│  - Raw internet data     │     │  - High-quality curated data       │
└─────────────────────┘     └──────────────────────────────────┘
```

### Stage 1: 事前学習（Pre-training）

**目的**: 次のトークン予測を通じて、インターネットスケールの知識・パターン・推論能力を獲得する。

| 要素 | 内容 |
|------|------|
| 目的関数 | 次のトークン予測（causal language modeling） |
| データ規模 | 15T+ トークン（2024年水準） |
| データソース | Web、書籍、コード、学術論文、多言語データ |
| 計算量 | 10²⁵ FLOPs 級 |
| アーキテクチャ | Transformer（密 or MoE） |
| 成果物 | Base model（指示追従不可、安全性未調整） |

**データエンジニアリングの重要性**: Llama 3 が示したように、データ構成の最適化（一般知識 50%、数学/推論 25%、コード 17%、多言語 8%）が性能を決定的に左右する。重複除去、品質フィルタリング、ドメイン別パイプラインが不可欠。

### Stage 2: 事後学習（Post-training）

**目的**: 指示追従、安全性、特定能力（コーディング、ツール使用、推論）を付与し、人間の選好にアライメントする。

標準的なサブステージ（Llama 3 方式）:

1. **Reward Model 学習**: 人間の選好データで報酬モデルを学習
2. **SFT (Supervised Fine-Tuning)**: 高品質な指示-応答ペアでファインチューニング
3. **Rejection Sampling**: プロンプトごとに複数出力を生成し、RM で最良を選択して学習
4. **DPO (Direct Preference Optimization)**: 選好ペア（chosen vs rejected）から直接ポリシーを最適化
5. **最終モデル平均化**: 複数チェックポイントの重み平均（モデルスープ）

**データ品質 > 量**: SFT では品質が重要、DPO では量も有効。コード・推論タスクでは合成データが特に効果的。

## 発展と派生

Llama 3（2024年7月）以降、このパラダイムは様々な方向に発展した：

### 強化学習の復権
- Llama 3 は DPO のみ（PPO 不使用）だったが、**DeepSeek-R1**（2025年1月）は [[concepts/grpo-rl-training|GRPO]] を用いた強化学習で推論能力を飛躍的に向上
- RLVR（Verifiable Rewards）、RLHF の発展形が続々登場

### テスト時スケーリング
- 事前学習・事後学習に加え、**推論時の計算リソース割り当て**（chain-of-thought、多数決、自己改善）が第三の段階として注目
- OpenAI o1/o3、DeepSeek-R1 が代表的

### マルチモーダル拡張
- Llama 3 の実験で示された「言語モデル凍結 + adapter 学習」パターンが広く採用
- GPT-4V、Gemini、Qwen-VL などが追随

### ポストトレーニングの効率化
- [[concepts/lora-peft|LoRA/QLoRA]] などの PEFT 手法で事後学習コストを削減
- 蒸留による小規模モデルへの能力転移

## 2024年時点での位置づけ

2024年、Llama 3 論文がランドマークとされた理由：

1. **体系化**: それまで断片的だった開発手法を、再現可能な単一パイプラインとして統合
2. **オープン性**: クローズドモデルに匹敵する性能をオープンソースで達成し、再現・検証を可能に
3. **スケーリング則の実践**: データ構成の最適化をスケーリング則で定量的に行う手法を確立
4. **信頼性データ**: フロンティア学習の運用実態（466回の中断）を公開

## 関連ページ

- [[entities/llama-3.md]] — Llama 3 モデル詳細
- [[concepts/scaling-laws.md]] — スケーリング則
- [[concepts/grpo-rl-training.md]] — GRPO / 推論 RL
- [[concepts/dpo-alignment.md]] — DPO アライメント
