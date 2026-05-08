---
title: "Multi-Agent Research System (Anthropic)"
type: concept
created: 2026-04-25
updated: 2026-05-08
tags:
  - multi-agent
  - orchestration
  - research
  - evaluation
aliases:
  - Claude Research multi-agent
  - orchestrator-worker research
status: active
sources:
  - raw/articles/2026-05-08_anthropic-engineering_multi-agent-research-system.md
  - https://www.anthropic.com/engineering/multi-agent-research-system
related:
  - multi-agent-orchestration-architecture
  - agent-team-swarm
  - building-effective-agents
  - managed-agents
---

# Multi-Agent Research System (Anthropic)

AnthropicがClaude Research機能のために構築したマルチエージェントシステム。Orchestrator-workerパターンで、リードエージェントが並列サブエージェントを動的に生成・調整する。

## 性能

> Multi-agent system with Claude Opus 4 lead + Claude Sonnet 4 subagents **outperformed single-agent Claude Opus 4 by 90.2%** on internal research eval.

### BrowseCompでのトークン効果分析

- **トークン使用量だけで分散の80%を説明**
- ツール呼び出し回数 + モデル選択で95%説明
- Multi-agent: チャットの **15倍** のトークン消費（経済性には高価値タスクが前提）

## アーキテクチャ

```
User Query → Lead Agent (計画・戦略)
                ├── Subagent 1 (独立検索)
                ├── Subagent 2 (独立検索)
                └── Subagent N (独立検索)
                          ↓
                Lead Agent (結果統合)
                          ↓
                CitationAgent (引用検証)
                          ↓
                Final Answer
```

### 主要コンポーネント
- **Lead Agent**: クエリ分析→戦略策定→サブエージェント生成→結果統合。Memoryに計画を永続化（200Kトークン制限対策）
- **Subagents**: 並列独立検索。Interleaved Thinkingでツール結果を評価
- **CitationAgent**: 全クレームの出典を検証
- **Memory**: コンテキスト制限を超えた場合の計画保持

## プロンプトエンジニアリングの教訓

### 1. Think like your agents
シミュレーションでエージェントの段階的な動作を観察→失敗モードを直接発見

### 2. Teach the orchestrator how to delegate
各サブエージェントに: 目的・出力形式・ツール/ソース指示・明確なタスク境界が必要
「半導体不足を調査」→ 曖昧すぎて3体が重複作業

### 3. Scale effort to query complexity
- 単純事実確認: 1 agent, 3-10 tool calls
- 直接比較: 2-4 subagents, 10-15 calls
- 複雑リサーチ: 10+ subagents（明確な役割分担）

### 4. Let agents improve themselves
ツールテストエージェントがMCPツールを数十回使用→説明を書き換え→**タスク完了時間40%削減**

### 5. Start wide, then narrow down
短く広いクエリから始め、徐々に絞り込む（人間の専門家リサーチと同じ）

### 6. Parallel tool calling
- Lead agent: 3-5 subagentsを並列生成
- Subagents: 3+ツールを並列使用
- **複雑クエリのリサーチ時間を最大90%削減**

## 評価手法

### LLM-as-Judge ルーブリック
| 次元 | 評価内容 |
|------|---------|
| Factual accuracy | クレームはソースと一致するか |
| Citation accuracy | 引用は実際にクレームを裏付けるか |
| Completeness | 要求された全側面をカバーしているか |
| Source quality | 一次ソースを使っているか |
| Tool efficiency | 適切なツールを適切な回数使ったか |

単一LLMコールで0.0-1.0のスコア＋pass-fail判定が最も一貫性があった。

### 人間評価の価値
- 幻覚回答・システム障害・微妙なソース選択バイアスを発見
- 初期: SEO最適化コンテンツファームを学術PDFより優先 → ソース品質ヒューリスティック追加

## 本番信頼性の課題

- **状態保持の複雑性**: マイナーな障害がエージェント全体を脱線させる
- **Rainbow deployments**: 実行中のエージェントを壊さず徐々にトラフィック移行
- **同期実行のボトルネック**: リードエージェントがサブエージェント完了を待つ（非同期化で改善余地）

## サブエージェントのファイルシステム出力

> サブエージェントがツールを呼び出して外部システムに成果物を保存→軽量参照のみコーディネーターに返す。「传言ゲーム」を防止し、大規模出力のトークンコピーを回避。

## See Also

- [[multi-agent-orchestration-architecture]] — Multi-agent orchestration patterns
- [[concepts/agent-team-swarm]] — Agent team/swarm architecture
- [[concepts/managed-agents]] — Managed Agents platform
- [[concepts/building-effective-agents]] — Building effective agents
- [[concepts/carlini-c-compiler-agents]] — Carlini's parallel agent experiment
- [[concepts/eval-awareness-browsecomp]] — BrowseComp eval awareness
