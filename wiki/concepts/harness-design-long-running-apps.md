---
title: "Harness Design for Long-Running Apps — Anthropic's Multi-Agent Architecture"
status: draft
created: 2026-04-13
source: "https://www.anthropic.com/engineering/harness-design-long-running-apps"
author: "Prithvi Rajasekaran (Anthropic Labs)"
tags: [harness-design, multi-agent, gan-loop, context-reset, sprint-contracts, evaluator-pattern]
related: [harness-engineering, context-engineering, agent-team-swarm, claude-memory]
---

# Harness Design for Long-Running Apps — Anthropic's Multi-Agent Architecture

Anthropic Labs（Prithvi Rajasekaran）による長期自律エージェントの実践設計。**GAN-inspiredループ**（Generator ↔ Evaluator）をフルスタック開発にスケールさせたアーキテクチャ。

## 核心的問題: なぜナイーブな実装は失敗するのか

長期自律エージェントは一貫して2つの失敗モードで劣化：

### 1. Context Anxiety & Window Limits

> "Context resets—clearing the context window entirely and starting a fresh agent, combined with a structured handoff that carries the previous agent's state and the next steps—addresses both these issues. This differs from compaction, where earlier parts of the conversation are summarized in place... A reset provides a clean slate, at the cost of the handoff artifact having enough state for the next agent to pick up the work cleanly."

**Anthropicの解決策**: 
- **Compaction**ではなく**Context Reset**を推奨
- 会話をその場で要約するのではなく、完全に新しいエージェントで再開
- ハンドオフ成果物に十分な状態を含めることで次のエージェントがクリーンに引き継げる

### 2. Self-Evaluation Bias

LLMは自身の中間的な出力に自信過剰になる傾向。生成と評価を分離することが重要。

## Multi-Agent Architecture: GAN-Inspired Loop

| エージェント | 役割 | 主要設計選択 |
|-------------|------|-------------|
| **Planner** | 1-4文のプロンプトを野心的な製品スペックに拡張 | 早期の技術的過 especificaciónを回避。製品コンテキストとAI機能統合に集中 |
| **Generator** | 機能の反復的構築 | スプリント(v1)または連続実行(v2)。構造化成果物で状態ハンドオフ |
| **Evaluator** | QA、グレーディング、フィードバック | **Playwright MCP**でライブ・インタラクティブテスト。コーディング前に「スプリントコントラクト」を交渉 |

**通信パターン**: ファイルベース状態転送。エージェントはファイルを読み書きしてセッション間でコンテキストを維持。

## Sprint Contracts（ Anthropic独自のメモリパターン）

```
Generatorがスコープと成功基準を提案
         ↓
Evaluatorがレビュー
         ↓
合意に達するまで交渉
         ↓
コーディング開始→評価→フィードバック→修正
```

**メモリシステムとしての意義**:
- 会話内ではなく**ファイルにコントラクトを保存**
- 各スプリントが独立したコンテキストで実行可能
- 状態が外部化されているため、エージェント再起動後も継続可能

## Harness Evolution: Opus 4.5 → 4.6

モデル能力向上に伴い、ハーネスの複雑さを体系的に削減：

| 要素 | Opus 4.5 | Opus 4.6 |
|------|----------|----------|
| スプリント | 必須 | 削除可能 |
| コンテキストリセット | 必須 | 削除可能 |
| Evaluator | 継続的フィードバック | エンドオブランまたは条件付き使用 |
| 理由 | 厳格な構造がないと一貫性維持不能 | 長期コンテキスト・計画・デバッグ能力が向上 |

> **重要ルール**: Evaluatorはタスクがモデルの信頼できる単独実行能力を超える場合にのみ負荷分散される。そうでなければオーバーヘッド。

## パフォーマンス比較

| ハーネスタイプ | タスク | 時間 | コスト | 結果 |
|---------------|--------|------|--------|------|
| **Solo Agent** | Retro Game Maker | 20分 | $9 | コアゲームプレイ破綻、 poor UI |
| **Full Harness (v1)** | Retro Game Maker | 6時間 | $200 | ポリッシュUI、動作する物理、16機能スペック/10スプリント |
| **Updated Harness (v2)** | Browser DAW | ~4時間 | $124.70 | 機能アレンジメントビュー、ミキサー、トランスポート、AIエージェント駆動 |

## メモリシステム設計との関係

### Anthropic vs ChatGPT vs Claude（Shlok Khemaniの分析との接続）

| 設計要素 | Anthropic Harness | Claude Memory | ChatGPT Memory |
|---------|-------------------|---------------|----------------|
| **状態保存** | ファイルベース（スプリントコントラクト） | CLAUDE.md + .agent/ | 独自データベース |
| **セッション管理** | Context Reset（新規エージェント） | ステートレス（毎回全コンテキスト） | ステートフル（メモリ永続化） |
| **評価分離** | Evaluatorエージェント（独立） | 自己評価（プロンプト内） | 自己評価（プロンプト内） |
| **スケーラビリティ** | モデル能力向上でハーネス簡素化 | ファイルシステムに依存 | データベーススキーマに制限 |

### 重要な洞察

1. **Context Reset > Compaction** — Anthropicは会話内要約より新規エージェント起動を推奨
2. **File-Based State Transfer** — セッション間状態はファイルで保持（ClaudeのCLAUDE.mdと同一パターン）
3. **Evaluator Isolation** — 生成と評価を分離することで自己評価バイアスを回避
4. **Model-Capacity-Driven Simplification** — モデルが向上すればハーネスは単純化できる（Over-Engineeringの回避）

## Sources

- [Harness Design for Long-Running Application Development](https://www.anthropic.com/engineering/harness-design-long-running-apps) — Prithvi Rajasekaran, Anthropic Labs, Mar 24, 2026
