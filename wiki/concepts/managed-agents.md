---
title: "Managed Agents (Anthropic)"
type: concept
created: 2026-04-25
updated: 2026-05-08
tags:
  - agent-architecture
  - anthropic
  - infrastructure
  - meta-harness
aliases:
  - Claude Managed Agents
  - decoupled agent architecture
status: active
sources:
  - raw/articles/2026-05-08_anthropic-engineering_managed-agents.md
  - https://www.anthropic.com/engineering/managed-agents
related:
  - building-effective-agents
  - effective-harnesses-for-long-running-agents
  - multi-agent-research-system
  - agent-team-swarm
---

# Managed Agents (Anthropic)

Anthropicの長期間稼働エージェント向けホスト型サービス。**「脳（brain）を手（hands）から分離する」** アーキテクチャ。

## 設計哲学

> "How to design a system for 'programs as yet unthought of.'"

OSがハードウェアを `process` / `file` に仮想化したように、Managed Agentsはエージェントの構成要素を仮想化:
- **Session** — 発生した全イベントの追記専用ログ
- **Harness** — Claudeを呼び出しツール呼び出しをルーティングするループ
- **Sandbox** — Claudeがコード実行・ファイル編集する実行環境

各インターフェースは実装と独立 → 実装の自由な交換が可能。

## Pets vs Cattle

### 結合アーキテクチャ（Pet）
- セッション・ハーネス・サンドボックスを1コンテナに同居
- コンテナ障害 → セッション消失
- デバッグにシェルアクセス必要 → ユーザーデータへのアクセスと衝突
- ハーネスが「リソースはコンテナ内にある」と仮定 → VPC接続時に壁

### 分離アーキテクチャ（Cattle）

```
execute(name, input) → string
provision({resources})
wake(sessionId)
getSession(id)
emitEvent(id, event)
getEvents()
```

- コンテナ死 → ツール呼び出しエラーとして検出、Claudeがリトライ判断
- ハーネスクラッシュ → `wake(sessionId)` で再起動、イベントログから再開
- 認証情報はサンドボックス外のVaultに（Claudeの生成コードから到達不能）

## セッション ≠ コンテキストウィンドウ

- セッションはコンテキストウィンドウの**外**にある永続的コンテキストオブジェクト
- `getEvents()` で位置ベースのスライス取得（再開・巻き戻し・再読込）
- 取得イベントはハーネス内で変換可能（prompt caching最適化、context engineering）

## 性能改善

- **p50 TTFT**: 約60%削減
- **p95 TTFT**: 90%以上削減
- 脳がコンテナを必要としない場合、プロビジョニング待ちなしで推論開始

## Many Brains, Many Hands

- **Many brains**: 複数のステートレスハーネスを起動、必要なときだけ手に接続
- **Many hands**: 各手は `execute(name, input) → string` ツール。ハーネスは手の実体（コンテナ/電話/ポケモンエミュレータ）を意識しない
- 脳同士で手を受け渡し可能

## Meta-Harness

Managed Agentsは**メタハーネス** — 特定のハーネス実装に依存せず、Claude Codeのような汎用ハーネスもタスク特化ハーネスも収容可能。

> "We're opinionated about the shape of these interfaces, not about what runs behind them."

## See Also

- [[concepts/building-effective-agents]] — Building effective agents
- [[concepts/effective-harnesses-for-long-running-agents]] — Long-running agent harnesses
- [[multi-agent-research-system]] — Multi-agent research system
- [[concepts/agent-team-swarm]] — Agent team/swarm architecture
- [[concepts/carlini-c-compiler-agents]] — Carlini's parallel agent experiment
