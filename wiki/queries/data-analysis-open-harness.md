---
title: "データ分析に適したOpen Harnessはあるか？"
created: 2026-05-14
updated: 2026-05-14
type: query
tags:
  - query
  - agent-harness
  - data-science
  - ai-agents
  - coding-agents
sources:
  - comparisons/open-harness-vs-agent-framework
  - concepts/data-analysis-agents
  - concepts/cognition-ai-data-analyst
  - concepts/agent-harness
related:
  - concepts/data-analysis-agents
  - concepts/cognition-ai-data-analyst
  - comparisons/open-harness-vs-agent-framework
  - concepts/agent-harness-comparison
---

# データ分析に適したOpen Harnessはあるか？

> **質問**: データ分析に適したHarness、特にOpen Harnessには何があるか？
> **質問者**: kzinmr（Discord #hermes-topic-manager, 2026-05-14）
> **回答要旨**: データ分析専用の真のOpen Harnessはまだ発展途上。現状は汎用coding harness（OpenCode/Pi）にDB MCP connectorを付けて使うのが最も「Open」な選択肢。

---

## 前提: 「Open Harness」の定義

まず、本Wikiで「Open Harness」が指す範囲を確認する（[[comparisons/open-harness-vs-agent-framework]] より）：

| 分類 | Open Harness | Agent Framework / Runtime |
|---|---|---|
| **投資対象** | 人間がAI Agentを**使う**ための操作面 | AI Agentを**システムに組み込む**制御面 |
| **主な利用者** | 開発者、運用者、個人、少人数チーム | プロダクト開発チーム、業務システムチーム |
| **代表的ツール** | OpenClaw, Hermes Agent, OpenCode, Pi | LangGraph, Pydantic AI, OpenAI Agents SDK, Claude Agent SDK |
| **評価軸** | Operator Workbench Readiness | Untrusted Product Runtime Readiness |

**ポイント**: Open Harnessは「すぐ使える完成品」であり、Frameworkは「組み立てが必要な部品」。データ分析の文脈でもこの区別が重要。

---

## 選択肢マトリクス

### A. 汎用Coding Harnessをデータ分析に転用する

| Harness | データ分析適性 | モデル自由度 | 主な制約 |
|---|---|---|---|
| **OpenCode** | ★★★★☆ | 75+プロバイダ | default permissive（hardened config推奨）。MCP/custom toolsでDB接続。モデル選択の自由度が最大 |
| **Pi** | ★★★★☆ | 20+プロバイダ + ローカル（MLX/GGUF） | 最小オーバーヘッド（<1K system prompt）。extensionでDBツール追加。Anthropic wallあり |
| **Claude Code** | ★★★☆☆ | Anthropicモデルのみ | MCPでDB接続可能。subscription $20/mo。Anthropic wall |
| **Codex CLI** | ★★★☆☆ | GPT-5.5推奨 + custom providers（DeepSeek等） | Apache-2.0 OSS。MCP dual対応。サブエージェントで分割可能 |
| **Aider** | ★★★☆☆ | BYOM（全モデル） | トークン効率最良（Claude Codeの1/4.2）。Git-first設計 |

**共通の課題**: これらはコード生成向けに設計されているため、データ分析タスクでは「SQL生成→実行→検証→可視化」のループを自分で組む必要がある。MCP DB connectorを追加すれば最低限のDB接続は可能だが、スキーマ探索や意味的曖昧性の解決はハーネス側で提供されない。

### B. データ分析特化エージェント / 製品

| ツール | アプローチ | Open Harnessか？ |
|---|---|---|
| **Cognition DANA / Devin** | SWE agentのデータ分析特化persona。MCPでRedshift/Snowflake/BQに接続。Knowledge設定でチーム共有。DANA専用persona（`/dana`）。エンドツーエンド（データ異常→コード原因→修正PR） | ❌ 製品型Closed Harness |
| **OpenAI社内Data Agent** | GPT-5.2 + Codex pipeline crawling + 6層context grounding（Table Usage → Human Annotation → Codex Enrichment → Institutional Knowledge → Memory → Runtime Context）。600+PB, 70k+ datasets | ❌ 内製Bespoke（非公開） |
| **Hex Technologies** | Agentic Notebooks — polyglot（SQL/Python/R）notebookにAI agent組み込み | ❌ 製品型Notebook Harness |
| **OpenAI Agents SDK（2026年4月進化版）** | Configurable memory + sandbox-aware orchestration + filesystem tools + MCP。Open Harnessに近づきつつある | △ Frameworkからの進化中 |

### C. データ分析エージェントのアーキテクチャ分類

データ分析エージェントの設計空間は、2つの軸で整理できる（[[concepts/data-analysis-agents]] より）：

|  | Approach A: Internal Bespoke | Approach B: SWE as Data Analyst |
|---|---|---|
| **代表** | OpenAI社内Data Agent | Cognition DANA / Devin |
| **コア洞察** | "データの意味はパイプラインコードの中にある" | "SWE Agentの方がSQL専用ツールより良いアナリスト" |
| **文脈** | 6層のgrounding context | コードベース全文検索 + git履歴 |
| **検証** | Evals API golden SQL pairs | 最終SQL + Metabase playground link |

---

## 結論

### 現状のベストプラクティス

```
個人/小規模なデータ分析:
  Pi または OpenCode + MCP DB connector
  → モデル自由、BYOK、permission設定でread-onlyに制限可能

チーム共有のデータ分析workbench:
  OpenClaw + OpenCode backend
  → Slack/Discordから自然言語でDB問い合わせ、gatewayで制御

製品化/SaaSとしてのデータ分析agent:
  Agent Framework (LangGraph / Pydantic AI) が適切
  → tenant isolation, audit, SLA, 状態管理が必要なため
```

### 未解決の課題

1. **データ分析専用の真のOpen Harnessはまだ存在しない** — Cognition DANAは強力だがClosed。HexはNotebook製品
2. **汎用coding harnessの転用には限界がある** — スキーマ探索、意味的曖昧性の解決、検証ループは自前実装が必要
3. **OpenAI Agents SDKの進化**は、FrameworkからOpen Harness方向への収束を示唆しているが、まだ発展途上
4. **MCPによるDB接続の標準化**は進んでいるが、データ分析ワークフロー全体（discovery → schema understanding → query → verify → visualize → report）をカバーするharnessは不在

### Karpathyの洞察との整合

> "good answers can be filed back into the wiki as new pages"

本query自体がその実践例：このQ&Aは、[[comparisons/open-harness-vs-agent-framework]] の投資対象分類と [[concepts/data-analysis-agents]] のアーキテクチャ分析を横断し、**データ分析×Open Harness**という未カバーの交差点を可視化した。

---

## 関連ページ

- [[concepts/data-analysis-agents]] — AIデータ分析エージェントの包括的概念
- [[concepts/cognition-ai-data-analyst]] — Devinをデータ分析エージェントにする設計
- [[comparisons/open-harness-vs-agent-framework]] — Open Harness対Agent Frameworkの本質的差異
- [[concepts/agent-harness]] — Agent Harnessの概念定義
- [[concepts/agent-harness-comparison]] — 9ハーネス比較ポータル
