---
title: "Instruction Hierarchy"
type: concept
created: 2026-04-30
updated: 2026-04-30
tags:
  - llm-safety
  - prompt-injection
  - instruction-hierarchy
  - openai
sources: []
---

# Instruction Hierarchy

大規模言語モデルにおける**命令階層（Instruction Hierarchy）**は、異なるソースからの指示の優先順位を定義するフレームワーク。OpenAI による IH-Challenge ベンチマークで体系的研究がなされた。

## 定義

OpenAI Model Spec が定義する優先順序:

| 優先度 | ソース | 信頼度 |
|--------|--------|--------|
| 1 (最優先) | System | 最も信頼 |
| 2 | Developer | 高信頼 |
| 3 | User | 中間 |
| 4 (最優先度下) | Tool | 最も低信頼 |

下位優先度の指示は、上位優先度の制約と矛盾する場合に従わない。この設計によりプロンプトインジェクションへの耐性が向上する。

## IH-Challenge

OpenAI が 2026年4月に公開した RL 訓練用データセット。設計原理:

1. **Instruction-following-simple** — 指示の忠実性を単純に評価
2. **Objectively gradable** — Pythonスクリプトのみで評価可能
3. **No trivial shortcuts** — 高い報酬を得るための簡単な回避策がない

**GPT-5 Mini-R** の結果:

| 評価 | GPT-5-Mini | GPT-5 Mini-R | Δ |
|------|------------|--------------|---|
| Gandalf Password (dev-user) | 0.98 | 1.00 | +0.02 |
| TensorTrust (sys-user) | 0.86 | 0.94 | +0.08 |
| System <> User Conflict | 0.84 | 0.95 | +0.11 |
| Developer <> User Conflict | 0.83 | 0.95 | +0.12 |

能力低下なし（GPQA, AIME, 選好ベンチマークで検証済み）。

## 利点

- **Safety steerability**: カテゴリ別の system プロンプトで拒否率を向上、有用性低下なし
- **Prompt injection robustness**: CyberSecEval 2 等で大幅改善
- **Overrefusal回避**: 複雑な指示・主観的判断なし

## Limitations

- OpenAI 独自実装
- 他モデルとの互換性未検証
- "Gandalf" などの既知の攻撃に依存

## Related

- [[concepts/prompt-injection]]
- [[concepts/rlhf]]
- [[concepts/chain-of-thought]]
- [[openai]] — 開発元
- [[concepts/gandalf]] — 脆弱性ベンチマーク

## Sources

- [OpenAI — Improving instruction hierarchy in frontier LLMs](https://openai.com/index/instruction-hierarchy-challenge/) (Apr 2026)
- [arXiv:2603.10521 — Instruction Hierarchy Paper](https://arxiv.org/abs/2603.10521)
- [IH-Challenge on Hugging Face](https://huggingface.co/datasets/openai/ih-challenge)
- [openai-is-cooking-the-anthropic-sweep-and-spacex-courts-cursor.md](../raw/articles/openai-is-cooking-the-anthropic-sweep-and-spacex-courts-cursor.md)
