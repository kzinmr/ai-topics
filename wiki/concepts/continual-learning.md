---
title: "Continual Learning — Continuous Improvement in AI Systems"
type: concept
aliases:
  - continual-learning
  - lifelong-learning-ai
  - incremental-learning
created: 2026-04-27
updated: 2026-04-27
tags:
  - concept
  - ai-agents
  - machine-learning
  - continual-learning
status: complete
description: "AIエージェントとモデルの継続的学習 — モデル、ハーネス、コンテキストの3層で学習するフレームワーク。"
---

# Continual Learning — 継続的学習

## 3層学習フレームワーク

AI agentは3層で継続的に学習できる（@hwchase17, 2026-04-24）:

### 1. Model Layer — モデル層
モデルの重み自体を更新する。SFT（Supervised Fine-Tuning）、RL（強化学習/GRPO）などの手法を使用。

**中心的課題: 壊滅的忘却 (Catastrophic Forgetting)**
モデルを新しいデータやタスクで更新すると、以前知っていたことが劣化してしまう。これはオープンな研究問題。

**実例:** OpenAI CodexモデルはCodexエージェントのために訓練されている。理論的にはユーザー毎にLoRAを持つことも可能だが、実際にはエージェントレベルで大部分が行われる。

### 2. Harness Layer — ハーネス層
エージェントを動かすコードと、常にharnessに含まれる指示・ツール。

**Meta-Harness: End-to-End Optimization of Model Harnesses**
エージェントがループで動作している状態でタスクを実行→評価→ログをファイルシステムに保存→コードエージェントでtracesを分析しharnessコードの変更を提案。

理論的にはユーザー毎に異なるコードハーネスを学習することも可能だが、実際にはエージェントレベルで大部分が行われる。

### 3. Context Layer — コンテキスト層
harnessの外側に位置する設定情報（指示、スキル、ツール）。一般的に「メモリ」として言及される。

harness内にも同様のタイプのコンテキストが存在する（ベースシステムプロンプト、スキル）。区別は、それがharnessの一部か設定の一部か。

**更新レベル:**
- **エージェントレベル** — エージェントが永続的な「メモリ」を持ち、自身の設定を時間とともに更新（例: OpenClawのSOUL.md）
- **テナントレベル** — 各テナント（ユーザー、組織、チーム）が独自のコンテキストを持つ（例: HexのContext Studio、DecagonのDuet、SierraのExplorer）
- **混合** — エージェントレベル、ユーザーレベル、組織レベルのコンテキスト更新を組み合わせ可能

**更新方法:**
- **オフラインバッチ処理** — 直近のtracesを実行して洞察を抽出しコンテキストを更新（OpenClawの「dreaming」に相当）
- **ホットパス実行** — エージェントがコアタスクに取り組んでいる最中に自身でメモリを更新（またはユーザーがプロンプトで指示）

**別の次元:** 明示的な更新か、暗黙的な更新か。ユーザーがエージェントに記憶を促しているのか、それともharness自体のコア指示に基づいてエージェントが記憶しているのか。

## Classical MLにおけるContinual Learning

古典的なML文献における継続的学習の試み:

- Self-distillation
- Real-time RL
- Memory scaffolds
- Replay methods
- Regularization
- Gradient projections
- KL penalties
- On-policy data
- その他多数

これらの多くは「正しい問題を解こうとしていない」という批判（@carnot_cyclist, 2026-04-24）:

> "We are not short of attempts at achieving continual learning — self-distillation, real-time RL, memory scaffolds, replay methods, regularization, gradient projections, KL penalties, on-policy data, and countless more. My complaint with a lot of these is that they are not even trying to solve the right problem."

 principledでambitiousな定義を試みている — 古典ML文献とディスコースの両方に根ざした。

## References

- [Continual learning for AI agents](../raw/articles/2040467997022884194_continual-learning-for-ai-agents.md) (2026-04-24, @hwchase17) — 3-layer learning framework
- [Defining Continual Learning](../raw/articles/2041479655035679163_defining-continual-learning.md) (2026-04-24, @carnot_cyclist) — Principled definition of continual learning

## Related Concepts

- [[concepts/harness-engineering]] — 3層学習の文脈
- [[concepts/cognitive-debt]] — コンテキスト層の更新と関係
- [[concepts/multi-agent-consensus-patterns]] — 複数エージェントでの継続的学習