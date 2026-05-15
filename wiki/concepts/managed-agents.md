---
title: "Managed Agents (Anthropic)"
type: concept
created: 2026-04-25
updated: 2026-05-15
tags:
  - architecture
  - anthropic
  - infrastructure
aliases:
  - Claude Managed Agents
  - decoupled agent architecture
status: active
sources:
  - raw/articles/2026-05-08_anthropic-engineering_managed-agents.md
  - https://www.anthropic.com/engineering/managed-agents
  - raw/articles/martinalderson.com--posts-managed-agents-are-the-new-lambda--f9db9fb9.md
  - https://martinalderson.com/posts/managed-agents-are-the-new-lambda/
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


## ベンダーロックインと自己ホスティング戦略 (Martin Alderson, May 2026)

[[entities/martin-alderson|Martin Alderson]] は管理エージェントを **AWS Lambda のアナロジー** で分析。Lambda がサーバーレス革命だったように、管理エージェントは強力だが「スティッキー（移行困難）」だと警告。

### エージェントハーネスの交換可能性

すべてのエージェントハーネス（Claude Code, Codex, OpenCode, Pi）は同じプリミティブを持つ：
- プロンプト + コンテキスト + ツール → 出力 + ログ

この基本構造の共通性により、ハーネス間の切り替えは比較的容易。しかし管理エージェント製品にデータとワークフローが埋め込まれると、その容易さは失われる。

### Anthropic 料金変更の影響 (May 2026)

Anthropic は 2026年5月、**非対話モード**の Claude Code 利用（管理エージェント・CI/CD パイプラインを含む）をサブスクリプショントークン枠から除外。実質 **5-20倍の値上げ** となり：
- **OpenAI Codex への移行圧力**が発生（OpenAI は現状、全ツール・全モードでサブスクリプション枠使用を許可）
- 開発者の価格感応性が企業の大規模購買決定に波及するパターンに注目

### 自己ホスティングの実践

```bash
# 本質的には Docker コンテナでハーネスを実行するだけ
docker run ... opencode --model <any-provider> --prompt "..."
```

利点:
- **モデルプロバイダ非依存**: 数分で Anthropic → OpenAI → Google → DeepSeek に切り替え可能
- **既存インフラ内でセキュア**: 自社 VPC・IAM・監査ログの枠内で運用
- **組織的コンピテンス構築**: エージェントプリミティブの知識を外部委託しない

### フロンティアラボの独占戦略リスク

> *"I have a strong gut feeling the frontier labs are going to start introducing new models and capabilities that are ONLY available on their managed agent platforms."*

新モデル・新機能が管理エージェントプラットフォーム限定で提供され始めた場合、セルフホスティング戦略は根本的に揺らぐ。現時点では様子見が賢明だが、動向を注視する必要がある。

## See Also


- [[concepts/building-effective-agents]] — Building effective agents
- [[concepts/effective-harnesses-for-long-running-agents]] — Long-running agent harnesses
- [[multi-agent-research-system]] — Multi-agent research system
- [[concepts/agent-team-swarm]] — Agent team/swarm architecture
- [[concepts/carlini-c-compiler-agents]] — Carlini's parallel agent experiment
