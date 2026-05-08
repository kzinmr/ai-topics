---
title: "Carlini C Compiler Agent Team"
type: concept
created: 2026-05-08
updated: 2026-05-08
tags:
  - multi-agent
  - agent-architecture
  - claude-code
  - harness-engineering
  - case-study
aliases:
  - C compiler agent team
  - parallel Claude agents
  - Nicholas Carlini compiler
status: active
sources:
  - raw/articles/2026-05-08_anthropic-engineering_building-c-compiler.md
  - https://www.anthropic.com/engineering/building-c-compiler
related:
  - agent-team-swarm
  - multi-agent-orchestration-architecture
  - effective-harnesses-for-long-running-agents
  - building-effective-agents
---

# Carlini C Compiler Agent Team

Nicholas Carlini（Anthropic Safeguardsチーム）による、16体のClaudeエージェントを並列稼働させてRustベースのCコンパイラをゼロから構築した実験。agent teamアーキテクチャの限界検証と実践的知見の宝庫。

## 実験概要

| 項目 | 値 |
|------|-----|
| エージェント数 | 16体並列 |
| Claude Codeセッション数 | 約2,000 |
| API費用 | $20,000 |
| 成果物 | 100,000行のCコンパイラ |
| 検証 | Linux 6.9カーネルをx86/ARM/RISC-Vでコンパイル成功 |

## アーキテクチャ

### Infinite Agent Loop

```bash
while true; do
    COMMIT=$(git rev-parse --short=6 HEAD)
    claude --dangerously-skip-permissions \
           -p "$(cat AGENT_PROMPT.md)" \
           --model claude-opus-X-Y &> "$LOGFILE"
done
```

シンプルなループで、タスク完了後即座に次のタスクを自律的に選択。

### 並列タスクロック

Gitベースの最小限の同期機構:
- エージェントが `current_tasks/parse_if_statement.txt` のようなファイルを書き込んでロック
- 競合時はgitの同期が第2エージェントに別タスク選択を強制
- プル→マージ→プッシュ→ロック解除のサイクル

### コンテナ分離

各エージェントにDockerコンテナ + `/upstream` マウント + `/workspace` ローカルクローン。

## 実践的教訓

### 1. 極めて高品質なテストを書く
> Claudeは与えられた問題を自律的に解く。だからタスク検証器がほぼ完璧でなければ、Claudeは間違った問題を解いてしまう。

- 高品質コンパイラテストスイートの選定
- オープンソースパッケージのビルドスクリプト検証
- Claudeのミスを観察→新しいテストを設計

### 2. Claudeの立場に立つ
環境設計の重要性。エージェントが自律的に方向性を見出せるよう、テスト・環境・フィードバックを設計。

### 3. CI/CDパイプラインの重要性
新機能実装時に既存機能を壊す問題に対し、CI/CDと厳格なテスト強制で対処。

### 4. 特化エージェントの活用
- ドキュメント維持エージェント
- コード品質監視エージェント
- 専門サブタスクエージェント

### 5. マージコンフリクト
頻繁に発生するが、Claudeは十分賢く解決できる。

## 限界

- オーケストレーションエージェント不使用（最小限プロトタイプ）
- エージェント間通信メカニズム未実装
- 高レベル目標管理プロセスなし
- 各エージェントの自律的判断に依存（「次に明らかな」問題を選択）

## エピソード

Claudeが誤って `pkill -9 bash` を実行し、自分自身（とループ）をkillした事例あり。

## See Also

- [[agent-team-swarm]] — Agent team/swarm architecture overview
- [[multi-agent-orchestration-architecture]] — Multi-agent orchestration patterns
- [[effective-harnesses-for-long-running-agents]] — Long-running agent harnesses
- [[building-effective-agents]] — Building effective agents
- [[harness-design-long-running-apps]] — Harness design for long-running apps
