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

## LLM Wikiを回すruntime境界の設計

Hermes Agent & LLM Wiki によるAI Topics自動追跡の事例

---

# 今日の主張

私は **AI Topics** というLLM Wikiを、Hermes Agentで運用している。

- 毎日source streamを取り込む
- raw sourceを保存し、wiki pageへ合成する
- schema / index / tag / link を検証する
- Slack / Discord / Telegramへ配信する

この知識管理を成立させている外側の実行境界を、ここでは **Harness** と呼ぶ。

> 20分の配分: AI Topics事例 8分 / Harness抽象化 7分 / Scaffoldと含意 5分

---

# Why Harness: OpenClaw / Hermes が示したこと

2025-2026に、HarnessはIDE/terminalの外へ広がった。

| Signal | 何が起きたか | 含意 |
|---|---|---|
| OpenClaw | 中国でpersonal agent gatewayとして普及 | chatから常駐agentを呼ぶ体験が広がった |
| OpenClaw ecosystem | model provider がruntime distributionに注力 | modelだけでなくharness適合が競争軸に |
| Hermes Agent | OpenRouter appsで#1 Daily global rank | memory + skills + scheduled executionが大規模利用 |
| Security incidents | 不注意なagent hostingで情報流出 | runtime governanceがより重要に |

Harnessは「coding assistant」から、**personal / organizational runtime** へ移動している。

---

# 個人的な課題: AI関連情報のキャッチアップコスト

AI/Agent領域のsource streamは、人手の管理だけではもはや追いつかない。

| 作業 | 人間だけでやると何が起きるか |
|---|---|
| Collect | SNS / blog / paper / newsletter が流れて消える |
| Synthesize | 読んだ断片が再利用可能な概念にならない |
| Retrieve | 「前に読んだ話」が都度再発見になる |
| Maintain | stale claim / duplicate / tag sprawl が蓄積する |
| Deliver | 価値ある更新が人間の手作業待ちになる |

必要なのは、Chatbotではなく **source streamを研究可能なwikiへ変換し続ける仕組み**。

---

# 事例: AI Topics = LLM Wiki + Hermes Agent

AI Topicsでは、KarpathyのLLM Wiki patternをAI/Agent領域の追跡に適用している。

```
SNS / RSS / newsletter / paper
  -> raw/            不変のsource material
  -> wiki/           concepts, entities, comparisons, queries
  -> validation      schema, tags, links, duplicate, stale claims
  -> delivery        reports, Slack, Discord, Telegram
```

ポイントは、回答を毎回生成することではなく、**知識がファイルシステム上で複利的に育つ**こと。

---

# Karpathy の LLM WikiとRAG

- RAG
  - `q -> documents(chunks) -> synthesized answer`
  - 回答は都度再発見され、知識はステートレスに近い

- LLM Wiki
  - `document -> raw/ -> wiki` (Agentic ETL)
  - `q -> wiki -> answer` (Cached Agentic RAG)
  - 有用回答や頻出質問は `queries/` 以下に保存して再利用

rawは不変。wikiはAgentが編集する。schemaは人間とAgentの共有契約になる。

---

# Hermes Agent が足している実行層

Karpathyのpatternは抽象的な設計。Hermes Agentはそれを運用に落とす。

| パターン | AI Topicsでの効き方 |
|---|---|
| Scheduled | 人間の依頼待ちではなく、定期的にsource streamを処理 |
| File-based | Markdown / Code / Config をAgentが自己修正し、人間もreview可能 |
| Skill-backed | 成功手順と落とし穴を `llm-wiki` / ingestion skills に戻す |
| Validated | schema / index / tag / link / duplicate を継続検査 |
| Push Delivery | server側実行結果をmessage channelへ届ける |
| Git-backed | 差分管理、rollback、review、監査を備える |

Harness により、LLM Wikiは **作業が回り続ける runtime 環境** になる。

---

# What is Harness?

Harnessとは、モデルの外側で **観測→実行→検証→記憶** を閉じるruntime境界。

| 層 | 役割 | 例 |
|---|---|---|
| Model | 次に何を試すかを判断する | Claude, GPT, Gemini, local models |
| Harness | agentの作業を成立させる | prompt, tools, memory, skills, verification loop |
| Runtime | executionを継続・仲介する | lifecycle, scheduling, safety, observability |
| Environment | actionが作用する世界 | repo, browser, GUI, wiki graph, sandbox |

Workflow-centric framework は制御フローを人間が明示的に書く。
Runtime-centric framework (Harness) では、モデルが探索し、runtimeが継続・制約・検証する。

---

# Effective Harness

「観測→実行→検証→記憶」が同じruntimeでつながると、Agentのタスク遂行能力に効く。

| 意義 | 何が可能になるか |
|---|---|
| Reliability | test/lint/schema/screenshot で「やったつもり」を潰す |
| Debuggability | trace で、何を見て何を実行しどこで失敗したかを追える |
| Safety | model へのお願いではなく、 hooks/runtime policy で止める |
| Continuity | memory/skills/file state/session が次回へ残る |
| Ownership | Open harness では trace/memory/policy がユーザー所有 |

Harnessの有無で著しい能力向上が確認される: [TODO] 事例

---

# Harness and Environment

Harnessは「どの世界を操作するか」で信頼性が大きく変わる。

| Task Type | Environment | 複雑性 | なぜ効く/難しいか |
|---|---|---|---|
| Coding | filesystem / shell / git | Low | symbolic, stable, replayable, verifiable |
| Wiki | markdown / graph / schema | Low-Mid | file-basedだが、意味の検証が難しい |
| Browser | DOM / Web session | Medium | UI変化、ログイン、外部状態が絡む |
| Computer use | GUI / OS / pixels | High | action spaceが広く、検証も難しい |
| General | mixed environment | Variable | 複数環境を一貫して作業継続する困難 |

Coding agentが先に実用化した理由は、モデルだけでなく **環境が検証しやすかった** から。
LLM Wikiもこの性質を利用している。

---

# Open harness と Runtime ownership

Open harnessの争点は、単なるモデル差し替えではない。
**trace / memory / skills / policy をユーザーが所有し、次の改善に使える点**。

| 観点 | Closed harness | Open harness |
|---|---|---|
| 例 | Claude Code, Codex | OpenCode, Pi, OpenClaw, Hermes |
| 学習 | vendorがtraceを集め、model/runtimeをco-design | userがfull-trace, skills, memoryを保持 |
| 強み | モデル適合が速い、UXが一貫 | portability, BYOK/local, 監査可能 |
| リスク | hidden orchestration, lock-in | safety/governanceを利用者が背負う |

Open harnessでは、失敗ログ・skill・validation ruleがユーザー側に残る。

---

# 失敗モードを改善資産にする

Harnessは成功を増やすだけでなく、失敗を次回の実行条件へ変換する。

| AI Topicsでの失敗 | Harness側の改善 |
|---|---|
| duplicate page | `index.md`と`log.md`を先に読む、既存page優先 |
| unsupported claim | raw source pathをfrontmatterと本文に残す |
| tag sprawl | `SCHEMA.md` taxonomy、pre-commit validator |
| stale checkpoint | checkpoint recovery skill、script再実行手順 |
| skill explosion | skill dedup、invocation metrics、consolidation pass |

この意味で、traceは単なるログではない。
**eval set / reward設計 / skill更新 / post-training data** の候補になる。

---

# Model Scaffold: モデルに能力を取り込む役割

LLM ProviderにとってのHarness Engineeringの戦略的な核心はここにある。

Bitter Lesson的には、Harness価値の一部は最終的にモデル側へ吸収される。

```
runtime上で半分うまく動くscaffoldを作る
  -> 成功/失敗trace, eval, rewardが集まる
  -> skill / guardrail / validation ruleに戻す
  -> あるいはRL/post-trainingでモデル側に能力が内在化される
  -> 古いscaffoldを削り、より難しいscaffoldを足す
```

AI Topicsでの運用改善も、RLは任意だが同じ小さなループ:
失敗をtraceに残し、skillやschemaに戻し、次回のAgentを少し賢くする。

---

# まとめ

Harness Engineeringは、LLMの外側にある雑多な周辺機能ではない。
**モデルが実行を継続し、失敗し、検証され、次回へ持ち越すruntime境界** の設計である。

AI Topicsでは、KarpathyのLLM wiki patternをHermes Agent(+git)で継続自律実行可能な形に運用している。
これはRAG chatbotではなく、**source streamを研究可能なwikiへ変換し続けるAgentic ETL**。

Harness Engineeringは、coding agentから一般の知識業務に広がりつつある。
失敗traceを改善資産に変えられる任意の領域が、Harness Engineeringの対象になる。

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
