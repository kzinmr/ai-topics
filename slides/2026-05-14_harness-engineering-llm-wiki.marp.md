---
marp: true
theme: default
paginate: true
size: 16:9
title: "Harness and AI Agent"
description: "Harness Engineeringの概要とLLM Wikiを使った自動知識管理の事例紹介"
style: |
  section {
    font-family: "Hiragino Sans", "Yu Gothic", "Noto Sans CJK JP", "Helvetica Neue", sans-serif;
    background: #fbfaf4;
    color: #18241f;
    padding: 54px 66px;
    letter-spacing: 0;
  }
  h1, h2, h3 {
    color: #10251c;
    letter-spacing: 0;
  }
  h1 {
    font-size: 42px;
    line-height: 1.18;
  }
  h2 {
    font-size: 34px;
    line-height: 1.2;
  }
  p, li {
    font-size: 25px;
    line-height: 1.46;
  }
  ul, ol {
    margin-top: 0.5em;
  }
  strong {
    color: #b45f06;
  }
  code {
    background: #efe7d0;
    color: #243326;
    border-radius: 4px;
    padding: 0.04em 0.24em;
  }
  table {
    font-size: 19px;
    border-collapse: collapse;
  }
  th {
    background: #17352b;
    color: #fffaf0;
  }
  td, th {
    padding: 0.42em 0.55em;
  }
  blockquote {
    border-left: 8px solid #c47f2c;
    color: #31423a;
    background: #f2ead8;
    padding: 0.4em 0.8em;
  }
  section.lead {
    background: #10251c;
    color: #fffaf0;
  }
  section.lead h1,
  section.lead h2,
  section.lead h3 {
    color: #fffaf0;
  }
  section.lead strong {
    color: #f1b35d;
  }
  section.section {
    background: #26372f;
    color: #fffaf0;
  }
  section.section h1,
  section.section h2 {
    color: #fffaf0;
  }
  .kicker {
    font-size: 18px;
    color: #b45f06;
    font-weight: 700;
    text-transform: uppercase;
  }
  .small {
    font-size: 18px;
    line-height: 1.38;
  }
  .grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 22px;
  }
  .box {
    border: 1.5px solid #d5c8ac;
    border-radius: 8px;
    padding: 18px 20px;
    background: #fffdf7;
  }
  .box h3 {
    margin-top: 0;
    font-size: 24px;
  }
  .big {
    font-size: 30px;
  }
  .mono {
    font-family: "SFMono-Regular", Menlo, Consolas, monospace;
    font-size: 20px;
    line-height: 1.35;
  }
---

<!-- _class: lead -->

<div class="kicker">LLM researchers / 20 min</div>

# Harness Engineering と AI Agent

## Coding agentsから、知識管理エージェントへ

Hermes Agent & `llm-wiki`によるAI Topics自動追跡の事例

---

# 今日の主張

1. **Harness / Runtimeは、モデルが実行を続ける制御層** として見る
2. Coding agentは、汎用エージェントのための実験場だった
3. Open harnessは、モデル・記憶・trace・runtimeの所有権を争点にした
4. AI Topicsは、KarpathyのLLM wikiをHermes Agentで運用した **Agentic ETL** の事例

> 20分の配分: Harness概要 11分 / AI Topics事例 7分 / 研究トピック 2分

---

# Why Harness?

| 時期 | 中心語彙 | 主な問い | キラー応用 |
|---|---|---|---|
| 2023-2024 | Prompt Engineering | 指示補完/RAG | ChatGPT / NotebookLM |
| 2024-2025 | Workflow-centric | 強い制御設計/ReActを補強 | LangChain / LangGraph |
| 2025 | Context Engineering | Tool密統合/長期実行の安定 | Claude Code / Codex |
| 2025-2026 | Harness Engineering | Coding能力の普及/汎用化や自律進化へ | Pi / OpenClaw / Hermes Agent |

Coding agentで先に起きたのは、**生成** から **実行と検証の閉ループ化** へのジャンプ

タスク実行の主導権が、開発者(workflow-centric)からエージェント(Runtime-centric)へ推移

- [Dec 19, 2024] Building effective agents (Anthropic)
- [Jun 23, 2025] Context Engineering for Agents (Lance Martin)
- [Nov 26, 2025] Effective harnesses for long-running agents (Anthropic)
- [Feb 11, 2026] Harness engineering: leveraging Codex in an agent-first world (OpenAI)

---

# 2025後半: OpenClaw の中国における爆発的普及

OpenClawは、coding assistantというより **personal agent gateway** として受容

- 「チャットから常駐agentを呼ぶ」体験が中心 (always-on / multi message channels)
- cloud / model providerがagent runtimeをdistribution layerとして展開
  - NVIDIAやAlibaba, Tencent, ByteDance, MiniMax, Moonshot.ai, Z.AI, etc.
- 不注意なホスティングによるセキュリティインシデントも同時に発生

---

# 2026前半: Hermes Agent は OpenRouter #1　に

OpenRouter (apps) で、Hermes Agent (Nous Research) が **#1 Daily global rank** に
(26/5/15時点)
- Total tokens: 6.98T
- #Models used: 354
- Category ranks: Productivity / Coding Agents / Personal Agents / CLI Agents で#1

**persistent memory + skills + scheduled execution** を持つ実行環境が大量利用され始めたシグナル。

- https://openrouter.ai/apps/hermes-agent

---

# What is an Agent Harness?

Harness とは Agent の仕事を成立させる部品とユーザー公開面を差した概念。

モデルの進化に伴い、Agent価値の重心は **Prompt → Workflow → Runtime** へと推移:

- Workflow-centric Framework   <- LangGraph, Pydantic AI
- Agent Harness / Runtime 製品  <- Claude Code, Codex, Pi, OpenClaw, Hermes　Agent
- Task Environment             <- Shell, Browser, Computer, Filesystem
- Model API                    <- Claude, GPT, Gemini

| 層 | Core question | 例 |
|---|---|---|
| **Workflow Framework** | 実行を明示的に制御 | graph, state machine, nodes, edges, HITL |
| **Harness** | agentは何を試みるか | prompt, tool choice, memory, skills, verification loop |
| **Runtime** | executionはどう継続するか | lifecycle, tool mediation, state continuity, scheduling, safety, observability |
| **Task Environment** | actionが作用する世界は何か | repo, browser, GUI, wiki graph, eval sandbox |

---

# Runtime-centric shift: 制御フローの所有者が変わる

Agent loopは昔から書けた(ReAct)。差分は **誰がcontrol flowの正当性を担保するか**。

| | Workflow-centric | Runtime-centric |
|---|---|---|
| Primary | developer-authored graph | model-driven runtime loop |
| Control | developer decides what happens next | model decides; runtime mediates |
| State | graph-managed, explicit | runtime-managed, across turns/sessions |
| Best for | deterministic business logic, audit | open-world execution, exploration |

モデルが tool continuation, retry adaptation, context tracking, failure recovery を維持可能に

orchestration DSL から execution semantics の整備へ

---

# Harness types: Environment entropy で難度が変わる

Harnessは「どの世界を操作するか」で信頼性が大きく変わる。

| Type | Primary environment | Entropy | 例 |
|---|---|---|---|
| Coding | filesystem / shell / git | Low | Claude Code, Codex, OpenCode, Pi |
| Browser | DOM / Web session | Medium | Browser Use, OpenClawの一部 |
| Computer use | GUI / OS / pixels | High | Operator, GUI agents |
| General | mixed environment | Variable | OpenClaw, Hermes Agent |

Coding agentが先に実用化した理由は、モデルだけでなく **環境がsymbolic, stable, replayable, verifiable** だったから。

---

# Open harness: Runtime ownershipの問題

Open harnessの価値は **runtime portability**

| 軸 | Closed Harness | Open Harness |
|---|---|---|
| 例 | Claude Code, Codex | OpenCode, Pi, OpenClaw, Hermes |
| 強み | model × runtimeのco-design / co-training | runtime visibility, portability, BYOK/local |
| 弱み | hidden orchestration, provider lock-in | safety & governance は利用者責任 |
| 資産 | vendor 側の trace, memory, tuning | user 側の full-trace, skills, memory, ... |

※ Claude/OpenAI Agents SDKは単なるLLM call abstractionではなく、reactive tool loopやevent streamを内蔵した **opinionated mini runtime** と見るのが近い。

---

# Effective Harness: 実行境界が閉じることの意味

「観測→実行→検証→記憶」が同じruntime境界でつながると、Agentのタスク遂行能力に効く。

| 意義 | 何が可能になるか |
|---|---|
| Reliability | test/lint/schema/screenshot で「やったつもり」を潰す |
| Debuggability | trace で、何を見て何を実行しどこで失敗したかを追える |
| Safety | model へのお願いではなく、 hooks/runtime policy で止める |
| Continuity | memory/skills/file state/session が次回へ残る |
| Ownership | Open harness では trace/memory/policy がユーザー所有 |

実行境界が閉じることで、モデルの一貫した能力獲得へも寄与する。

---

# Model Scaffold: モデルに能力を取り込む役割

Bitter Lesson的には、Harness価値の多くは最終的にモデル側へ吸収される。
Harness で誘導したエージェントの使用履歴から、能力をモデルに取り込むことができる。

```
runtime上で半分うまく動くscaffold(harness)を作る
  -> trace / eval / rewardが集まる
  -> RLやpost-trainingで内在化される
  -> 古いscaffoldを削り、新たなscaffold、そしてモデル能力を強化する
```

LLMプロバイダーの狙い(Moat)はここだと考えられるし、中華AIがOpenClawへの調整をサポートする背景でもある。

---

# 事例: LLM Wiki + Hermes Agent による知識管理

- 日々のSNSなどに流入する膨大なAI知見: 読む・書く・取り出す、の労力がやばい
- => Karpathy の LLM wiki pattern により、 **persistent, compounding wiki** を作る
- => Hermes Agent により、継続的に実行・保守可能な基盤を整備

ai-topics/ project ではこのpatternを、LLM / AI Agent領域の追跡に適用している。

---

# Karpathyの3層: raw / wiki / schema

- RAG: q -> documents (chunks) -> synthesized answer
  - 回答は都度再発見し、ステートレス
  - documents の設計は固定的・保守はプログラム的
- LLM Wiki
  - document -> raw/ -> wiki (LLMが合成: concepts/entities/ etc.)
  - q -> wiki -> answer (有用回答・頻出質問なら queries/ 以下に回答を保存・再利用)

rawは不変。wikiはAgentが編集する。

---

# Hermes Agent が足している実行層

Karpathyのpatternは抽象的な設計。Hermes Agentはそれを運用に落とす。

| LLM Wiki operation | Hermes / AI Topicsでの支援 |
|---|---|
| Ingest | cron, scripts, checkpoints, raw保存 |
| Query | `index.md`起点の探索、関連page読み、再利用可能なら`queries/`へ保存 |
| Lint | wiki health, duplicate/orphan/broken-link/stale-claim検査 |
| Maintenance | `llm-wiki`, `wiki-ingestion-pipelines`, `wiki-graph-health` skills |
| Delivery | daily report, Slack/Discord/Telegram push |

LLM Wikiに、**scheduler, tools, skills, validation, delivery** が重なる形。

---

# Hermes Agent が効いているアーキテクチャパターン

| パターン | なぜ効くか |
|---|---|
| Scheduled | 人間の依頼待ちではなく、定期的に処理できる |
| File-based | Markdown/Code/Config を自己拡張修正可能・人手管理も可能 |
| Push Delivery | server側実行結果をmessage channel (mobile) へ届ける  |
| Skill-backed | 抽象的要件でも成功手順と落とし穴を改善可能/モデル学習の迂回 |
| Git-backed | 差分管理、rollback、review、監査を備える (filesystemベースでも) |

"RAG-based chatbot" ではなく、**作業が回り続けるランタイム環境 （Harness）** として設計。

---

# Coding agentとknowledge workflowは同型

| Coding agent | Knowledge workflow |
|---|---|
| repoを読む | raw sourceと既存wikiを読む |
| code diffを書く | wiki diffを書く |
| test/lintを回す | schema/index/tag/linkを検証する |
| PR / commitで残す | log / git / reportで残す |
| 失敗からskillを書く | ingest失敗や重複回避をskillへ戻す |

違うのは対象物だけ。
**閉ループで作業し、traceから次の手順を改善する** という構造は同じ。

---

# 失敗モードを改善資産にする

| AI Topicsでの失敗 | 具体の修正 |
|---|---|
| duplicate page | `index.md`と`log.md`を先に読む、既存page優先 |
| unsupported claim | raw source pathをfrontmatterと本文に残す |
| tag sprawl | `SCHEMA.md` taxonomy、pre-commit validator |
| stale checkpoint | checkpoint recovery skill、直接script再実行手順 |
| skill explosion | skill dedup、invocation metrics、consolidation pass |

将来的には、これらのtraceは単なる運用ログではなく、**reward設計・eval set・RL/post-training data** になり得る。

---

# まとめ

Harness Engineeringは、LLMの外側にある雑多な周辺機能ではない。
**モデルが実行を継続し、失敗し、検証され、次回へ持ち越すruntime境界** の設計である。

Coding agentは、そのruntime境界が最も見えやすい領域だった。
OpenClawやHermesは、その構造をIDE/terminalの外へ広げた。

AI Topicsでは、KarpathyのLLM wiki patternをHermes Agentのscheduler、skills、memory、validationで運用している。
これはRAGではなく、**継続的にsource streamを研究可能なwikiへ変換するAgentic ETL**。

---

# 参考資料

<div class="small">

- Karpathy, "LLM Wiki" — https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
- OpenRouter, "Hermes Agent" — https://openrouter.ai/apps/hermes-agent
- OpenClaw zh-CN docs — https://docs.openclaw.ai/zh-CN
- China Briefing, "China Agentic AI OpenClaw Boom" — https://www.china-briefing.com/news/china-agentic-ai-openclaw-boom/
- `blog/2026-05-12_hermes_harness-engineering-from-coding-agents-to-general-agents.md`
- `wiki/comparisons/open-harness-vs-agent-framework.md`
- `wiki/concepts/agent-harness.md`, `wiki/concepts/agent-runtime.md`
- `wiki/concepts/runtime-opinionated-sdk.md`, `wiki/comparisons/agent-harnesses.md`
- `wiki/entities/hermes-agent.md`, `wiki/concepts/hermes-agent-use-cases.md`
- `config/hermes/skills/wiki/wiki-ingestion-pipelines/SKILL.md`

</div>
