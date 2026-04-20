---
title: "Anthropic Managed Agents"
created: 2026-04-09
updated: 2026-04-13
tags: [concept, agent-team-swarm, anthropic, platform, managed-agents]
related: [agent-team-swarm, harness-engineering, ai-agent-engineering]
sources:
  - https://claude.com/blog/claude-managed-agents
  - https://www.anthropic.com/engineering/managed-agents
  - https://platform.claude.com/docs/en/managed-agents/quickstart
---

# Anthropic Managed Agents

**Source:** Anthropic Claude Blog + Engineering Blog + Platform Docs (April 2026)
**Status:** Public Beta on Claude Platform
**Related:** [[Agent Team / Swarm]], [[Harness Engineering]], [[meta-harness]]

---

## Core Value Proposition

Anthropic Managed Agentsは、**AI Agentのプロトタイプから本番運用までを10倍速く**実現するプラットフォーム。インフラ構築（サンドボックス、認証、権限管理、チェックポイント、エラーリカバリー）をClaudeに委譲し、開発者はタスク定義・ツール・ガードレールの設計に集中できる。

---

## Architecture: Brain/Hands/Sessionの分離

Anthropic Engineering Blog「[Scaling Managed Agents: Decoupling the brain from the hands](https://www.anthropic.com/engineering/managed-agents)」の中核テーゼ:

> Agent harnesses inevitably encode assumptions about current model limitations. As AI capabilities improve, these assumptions become obsolete.

初期設計ではSession・Harness・Sandboxが単一コンテナに結合（「ペット」）。現在の設計では以下の3要素を完全に分離（「家畜」）:

| 要素 | 役割 | 分離のメリット |
|---|---|---|
| **Brain** | Claude + Harness | ステートレス → 水平スケール可能 |
| **Hands** | Sandbox/Tools | 必要時にプロビジョニング、失敗時は再作成 |
| **Session** | Event Log（永続化） | コンテキストウィンドウ外の状態管理 |

### Key Interfaces

```
Sandbox Execution:  execute(name, input) → string
Container Lifecycle: provision({resources})
Harness Recovery:   wake(sessionId) → reboot stateless harness
                    getSession(id) → retrieve durable event log
                    emitEvent(id, event) → append to session
Context Query:      getEvents() → fetch positional slices
```

### メタ・ハーネス哲学

> "We're opinionated about the shape of these interfaces, not about what runs behind them."

Managed Agentsは**メタ・ハーネス**（[[meta-harness]]参照）として設計されている。特定の実装には意見を持たず、インターフェース境界だけを厳格に定義する。

---

## Security: Credential Isolation

- **Git Integration**: アクセストークンはSandbox初期化時にコンテナに直接注入。Claudeはトークンに触らずにpush/pull実行
- **Custom Tools (MCP)**: OAuthトークンはセキュアボールトに保管。セッション固有トークンでプロキシ経由呼び出し
- **構造的セキュリティ境界**: Sandboxにクレデンシャルが一切到達しない

---

## Multi-Agent Coordination (Research Preview)

- **Agentが他のAgentをspawn**して複雑なワークフローを並列化
- **Self-Evaluation & Iteration**: 成功基準を定義すると、Claudeが自律的に評価・改善を繰り返す
- 内部テストにおいて、標準プロンプトループ比較で**最大10ポイント**の成果向上（特に難易度の高い課題で顕著）

---

## Session vs Context Window

長時間タスクはClaudeのコンテキストウィンドウを超える。従来の解決策（圧縮・トリミング）は不可逆な保持/破棄判断を強制する問題があった。

**Sessionを外部コンテキストとして分離**することで:
- 永続的・照会可能なストレージを保障
- Harnessが任意のコンテキスト変換（キャッシュ最適化、将来のコンテキストエンジニアリング）を担当
- ストレージ層を壊さずに将来のモデル能力進化に対応

---

## Performance Impact

| Metric | Improvement | Reason |
|---|---|---|
| TTFT p50 | ~60% 削減 | 推論即時開始、Sandboxは必要時のみ |
| TTFT p95 | >90% 削減 | 同上 |
| Horizontal Scale | Many Brains | ステートレスHarnessが並列実行可能 |
| Tool Context | Many Hands | 複数の実行コンテキストを横断的に操作 |

---

## API Quickstart

**必須ヘッダー:** `anthropic-beta: managed-agents-2026-04-01`

```python
# 1. Agent作成
agent = client.beta.agents.create(
    name="Coding Assistant",
    model="claude-sonnet-4-20260401",
    system="You are a helpful coding assistant.",
    tools=[{"type": "agent_toolset_20260401"}]
)

# 2. Environment作成
environment = client.beta.environments.create(
    name="prod-env",
    config={"type": "cloud", "networking": {"type": "restricted"}}
)

# 3. Session開始
session = client.beta.sessions.create(
    agent=agent.id,
    environment_id=environment.id
)

# 4. イベントストリーミング
with client.beta.sessions.events.stream(session.id) as stream:
    for event in stream:
        match event.type:
            case "agent.message": ...
            case "agent.tool_use": ...
            case "session.status_idle": ...
```

---

## Pricing

- Claude Platformの標準トークンレート
- **+$0.08/セッション時間**（active runtime）

---

## Enterprise Adoption

| 企業 | ユースケース | 引用 |
|---|---|---|
| **Notion** | Custom Agents（プライベートアルファ） | 「オープンエンドな複雑なタスクを委任可能に」 — Eric Liu, PM |
| **Rakuten** | Slack/Teams向けエンタープライズAgent | 「1週間で専門Agentをデプロイ」 — Yusuke Kaji, GM AI for Business |
| **Asana** | プロジェクト内AIチームメイト | 「開発を大幅に加速」 — Amritansh Raghav, CTO |
| **Sentry** | Seer debugging + Claude patch agent | 「数月ではなく数週で出荷」 — Indragie Karunaratne |
| **Atlassian (Jira)** | ワークフロー統合開発Agent | 「サンドボックス、セッション、権限管理を自動化」 — Sanchan Saxena, SVP Product |

---

## Related

- [[Agent Team / Swarm]] — 複数Agent協調の上位概念
- [[Harness Engineering]] — 単一Agentの実行環境設計
- [[meta-harness]] — インターフェース中心の設計哲学
- [[OpenAI Symphony]] — 競合のAgent Teamオーケストレーター
- [[Dark Factory Software Factory]] — 完全自律開発の最先端事例

---

## Sources

- [Claude Blog: Claude Managed Agents](https://claude.com/blog/claude-managed-agents) (2026-04-08)
- [Anthropic Engineering: Scaling Managed Agents](https://www.anthropic.com/engineering/managed-agents) (2026-04)
- [Platform Docs: Get started with Claude Managed Agents](https://platform.claude.com/docs/en/managed-agents/quickstart) (2026-04)
- Raw articles: `wiki/raw/articles/claude-managed-agents-20260408.md`
