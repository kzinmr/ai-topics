---
title: Autoreason
type: concept
created: 2026-04-27
updated: 2026-04-27
status: L2
sources: [https://github.com/NousResearch/autoreason, https://x.com/SHL0MS/status/2043415274196435325]
tags: [reasoning, self-refinement, multi-agent, karpathy, nousresearch, subjective-domains, auto-research]
aliases: [auto-reason]
---

# Autoreason

SHL0MS（@SHL0MS）とHermes Agent（NousResearch）が共同開発した、**主観的ドメインにおける自己改善（self-refinement）の自動化手法**。KarpathyのAutoResearchを主観的評価分野へ拡張した。

## Core Problem

反復的な自己改善（critique-and-revise）は3つの構造的欠陥により失敗する:

1. **Prompt Bias（プロンプトバイアス）**: モデルは批評を求められると、欠陥を捏造しがち
2. **Scope Creep（スコープクリープ）**: 各反復で出力が制御不能に拡張する
3. **Lack of Restraint（自制心の欠如）**: モデルは「変更不要」と出力しない

## Methodology

各反復で**3つの競合バージョン**を生成し、**文脈孤立な新鮮なエージェント**による**盲検Borda投票**で採点する。「何もしない」は常に第一級オプション。

| バージョン | 説明 |
|-----------|------|
| **A** | 変更なしの incumbent（現状維持） |
| **B** | 敵対的 revision（批評に基づく改訂） |
| **AB** | AとBの synthesis（統合） |

```
Task Prompt → Incumbent A
                  ↓
        ┌─── Critic (fresh agent) ───→ Critique
        │
        ├─── Author B (fresh agent) ──→ Revision (B)
        │
        └─── Synthesizer (fresh) ─────→ Synthesis (AB)
                  ↓
          Judge Panel (3 fresh agents, Borda count)
                  ↓
              Winner → new A  (or converge if A wins k=2 times)
```

**設計上の重要ポイント**:
- 3人のjudgeが最適な収束速度（1人はノイズ多、7人は3倍の収束）
- BとABの両方が必要。いずれか欠けるとトーナメントが崩壊
- Length-controlled評価でも4タスク中3勝

## Key Results

| Finding | Detail |
|---------|--------|
| **42/42 perfect sweep** | Haiku 3.5 + autoreasonが3タスクで完全Borda全勝; 全ベースラインは単一パスより劣化 |
| **77% vs 73%** | Sonnet 4.6 in 150 CodeContests problems (private-test): autoreason vs single-pass |
| **40% vs 31%** | Haiku 3.5 autoreason vs best-of-6 sampling (matched compute) |
| **Haiku 4.5: transition point** | 60% private accuracyでgains消失 — generation-evaluation gapの収束を示唆 |
| **Refinement destroys weak models** | Critique-and-reviseはHaiku 3.5の出力を15パスで59-70%削減 |
| **Code scaling curve** | Haiku 3.5 (40%) → Haiku 4.5 (60%) → Sonnet 4 (64%) → Sonnet 4.6 (77%) |

## Repository

[NousResearch/autoreason](https://github.com/NousResearch/autoreason)
- `paper/` — LaTeXソース、図表、PDF
- `tasks/` — 課題プロンプト（5 open-ended, 3 constrained）
- `human_eval/` — 人間評価用盲検資料
- `experiments/` — 実験ランナー、結果、アブレーション

## Citation

```bibtex
@article{shl0ms2026autoreason,
  title={Autoreason: Self-Refinement That Knows When to Stop},
  author={SHL0MS and Hermes Agent},
  year={2026},
  url={https://github.com/NousResearch/autoreason}
}
```

## Significance

Autoreasonは、**「自己改善の自動化」を主観的評価分野へ初めて適用**した研究。従来のベンチマークベース手法では対応できない「美的判断」「文才」「デザイン」などの主観的ドメインにおいて、構造的に失敗するcritique-and-reviseの代わりに、Borda投票による競合選択アプローチを提供する。「Do nothing」を第一級オプションにすることで、不要な劣化を防ぐ設計が特徴。

KarpathyのAutoResearch（自動研究手法）の自然な拡張であり、LLMによる研究・創作プロセスの自動化の重要なマイルストーン。

## Related Concepts

- [Karpathy's AutoResearch](https://karpathy.github.io/2025/04/28/self-play-benchmark.html)
- [Agent Disagreement (Agreement Bug)](agreement-bug.md)
- [Multi-Agent Systems](multi-agent-systems.md)
