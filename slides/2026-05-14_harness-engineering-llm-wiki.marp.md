---
marp: true
theme: default
paginate: true
size: 16:9
title: "Harness Engineering and llm-wiki"
description: "LLM researchers向け20分発表: Harness技術の概要とAI Topicsにおける知識管理ハーネス事例"
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

# Harness Engineeringを相対化する

## Coding agentsから、知識管理エージェントへ

Hermes Agent & `llm-wiki`によるAI Topics追跡事例

---

# 今日の主張

1. **Harnessは部品表ではなく、モデルが仕事をする環境** として見る
2. Coding agentは、汎用エージェントのための実験場だった
3. Open harnessは、モデル・記憶・trace・runtimeの所有権を争点にした
4. AI Topicsは、KarpathyのLLM wikiをHermes Agentで運用した **Agentic ETL** の事例

> 20分の配分: Harness概要 11分 / AI Topics事例 7分 / 研究トピック 2分

---

# なぜいまHarnessなのか

| 時期 | 中心語彙 | 主な問い | キラー応用 |
|---|---|---|---|
| 2023-2024 | Prompt Engineering | モデルに何を言うか | ChatGPT / NotebookLM |
| 2024-2025 | Context Engineering | モデルに何を見せるか | Claude Code / Codex |
| 2025-2026 | Harness Engineering | モデル能力をどう仕事へ変換するか | OpenCode / Pi / OpenClaw / Hermes |

Coding agentで先に起きたのは、**生成** ではなく **実行と検証の閉ループ化**。
ファイル、シェル、テスト、Git、CI/PRが、LLMを「一発回答器」から探索器へ変えた。

---

# 市場シグナル 1: OpenClawは中国で社会実装の入口になった

OpenClawは、coding assistantというより **personal agent gateway** として受容された。

| 観測 | 読み方 |
|---|---|
| 中国語公式docs、Gateway、複数messenger接続 | 「チャットから常駐agentを呼ぶ」体験が中心 |
| Alibaba / Tencent / ByteDance / Baidu / JD Cloud、MiniMaxなどが関連展開との報道 | cloud / model providerがagent runtimeをdistribution layerとして見る |
| 規制・セキュリティ注意喚起も同時に発生 | always-on agentのリスクは便利さと表裏一体 |

<div class="small">Sources: OpenClaw zh-CN docs; China Briefing; Tom's Hardware/Bloomberg報道。数値は監査済み統計ではなく、報道・コミュニティ観測として扱う。</div>

---

# 市場シグナル 2: Hermes AgentはOpenRouterで#1を取った

OpenRouterのアプリページでは、Hermes Agentが **#1 Daily global rank** と表示されている。

| 指標 | 2026-05-14確認時点 |
|---|---|
| Total tokens | 6.99T |
| Daily global rank | #1 |
| Models used | 354 |
| Category ranks | Productivity / Coding Agents / Personal Agents / CLI Agentsで#1 |

これは性能ベンチではない。だが、**persistent memory + skills + scheduled execution** が大量利用される作業面になったことを示す。

---

# まず部品ではなく「作業面」を見る

Harnessは、モデルが外界でrolloutするための作業面である。

```
goal
  -> observe workspace
  -> choose next action
  -> execute through tools
  -> verify against environment
  -> persist useful state
  -> repeat
```

重要なのは、Context / Action / Traceを別々に数えることではない。
**観測、実行、検証、記憶が同じ面で閉じているか**。

---

# Harness Effect: 同じモデルでも、置かれる作業面で変わる

| 何が変わるか | 例 |
|---|---|
| Contextの作り方 | codebaseを丸ごと入れるか、必要箇所を探索させるか |
| Action space | 100個の狭いtoolか、read/write/edit/bashの強いprimitiveか |
| Verification | 作ったつもりで終わるか、test/lint/screenshotで戻すか |
| Termination | 早期完了を許すか、checklistや`done` toolで止めるか |
| State | sessionで消えるか、memory/skill/logに残るか |

だからbenchmarkは、model名だけでなく **model × harness × task environment** で読む必要がある。

---

# 失敗モードがHarnessを育てる

| 失敗 | Harnessでの修正 | 将来の学習信号 |
|---|---|---|
| 必要な情報を見ない | index, retrieval, progressive disclosure | context selection policy |
| 危険な操作を試す | sandbox, permission, approval | safe action policy |
| 同じミスを繰り返す | skill, checklist, loop detection | recovery policy |
| 完了を誤認する | tests, evals, explicit done | termination policy |
| 長時間で文脈が腐る | checkpoint, compaction, subagent isolation | memory policy |

Harnessは「モデルの弱さの隠蔽」ではなく、**失敗を構造化して次の改善単位にする装置**。

---

# Open harnessを2つの方向で見る

| 系統 | 代表 | Claude Code / Codexとの対比 | 主なリスク |
|---|---|---|---|
| **Coding workbench** | OpenCode / Pi | providerやlocal modelを選べる。AGENTS.md, tools, shellを自分で制御 | permission, MCP, provider設定が運用資産化し、harnessロックインが起きる |
| **General workbench** | OpenClaw / Hermes | IDE/terminalを越え、messenger, cron, memory, skillへ広がる | 常駐権限、長期状態、外部通知、自己改善の説明可能性が難しくなる |
| **Vertical integrated** | Claude Code / Codex | model-harnessの共適応が強く、default pathが速い | memory/trace/runtime/pricingの所有権がprovider側へ寄る |

Open harnessの価値はOSSそのものより、**作業履歴と実行環境を誰が所有するか** にある。

---

# HarnessとFramework/SDKは別物

| | Open Harness | Agent Framework / SDK |
|---|---|---|
| 目的 | 人間がagentを使う作業面 | agentをプロダクトや業務システムに組み込む制御面 |
| 例 | OpenCode, Pi, OpenClaw, Hermes | LangGraph, Pydantic AI, OpenAI Agents SDK, Claude Agent SDK |
| 強み | すぐ使える、探索と運用補助に強い | state, tenant, audit, approval, retryを設計できる |
| 弱み | 業務ロジックや状態がharness内に散りやすい | 初期設計が重く、作業面は別途必要 |

最も堅い構成は、**Harnessをoperator workbench、Frameworkをproduct runtime** として分離すること。

---

# HermesとOpenClaw: 比較軸を変える

| 観点 | OpenClaw | Hermes Agent |
|---|---|---|
| 中心 | Gateway / control plane | Persistent ops agent |
| 何をつなぐか | 人間、chat channel、agent runtime、workspace、approval | memory、skills、cron、subagents、delivery |
| 強い場面 | 既存agentを複数チャネルから操作する | 作業履歴を次回の能力へ変換する |
| 学習の形 | governed skills / routing / policy | self-improving skills / session search / memory |
| 注意点 | gateway権限、channel別approval、tenant境界 | skill explosion、長期memory、なぜそう動いたかの追跡 |

OpenClawは **agent control gateway**。Hermesは **self-improving workbench**。
どちらも「IDEの外へ出たagent」の形だが、設計中心が違う。

---

# Harnessはモデル能力を取り込むための中間層

Bitter Lesson的には、価値の多くは最終的にモデル側へ吸収される。
だが、その吸収は空中では起きない。

```
scaffoldを作る
  -> 現モデルが半分うまく使う
  -> trace / eval / rewardが集まる
  -> RLやpost-trainingで内在化される
  -> 古いscaffoldを削り、次の難しいscaffoldへ進む
```

Harnessは永遠に厚くするものではない。
**モデルに取り込ませる能力を、いったん外部化して測る場所** として見る。

---

# 事例: AI TopicsはKarpathy LLM Wikiの実装

KarpathyのLLM wiki patternは、RAGではなく **persistent, compounding wiki** を作る発想。

| RAG | LLM Wiki |
|---|---|
| 質問時にraw docsからchunkを検索 | source追加時にwikiへ統合 |
| 毎回、関連断片を再発見する | synthesisを一度作り、更新し続ける |
| chat answerが消える | queryや比較がwiki pageとして残る |
| maintenanceは人間に残る | bookkeepingをLLM agentへ移す |

AI Topicsはこのpatternを、LLM / AI Agent領域の追跡に適用している。

---

# Karpathyの3層: raw / wiki / schema

| Karpathy pattern | AI Topicsでの実体 |
|---|---|
| Raw sources | `wiki/raw/articles/`, `papers/`, `newsletters/`, `transcripts/` |
| LLM-maintained wiki | `entities/`, `concepts/`, `comparisons/`, `queries/`, `events/` |
| Schema | `wiki/SCHEMA.md`, `AGENTS.md`, page threshold, tag taxonomy |
| Index / log | `wiki/index.md`, append-only `wiki/log.md` |

rawは不変。wikiはAgentが編集する。schemaはAgentを **generic chatbotではなく、disciplined wiki maintainer** にする。

---

# Hermes Agentが足している実行層

Karpathyのpatternは抽象的な設計。Hermes Agentはそれを運用に落とす。

| LLM Wiki operation | Hermes / AI Topicsでの支援 |
|---|---|
| Ingest | cron, scripts, checkpoints, raw保存 |
| Query | `index.md`起点の探索、関連page読み、再利用可能なら`queries/`へ保存 |
| Lint | wiki health, duplicate/orphan/broken-link/stale-claim検査 |
| Maintenance | `llm-wiki`, `wiki-ingestion-pipelines`, `wiki-graph-health` skills |
| Delivery | daily report, Slack/Discord/Telegram push |

つまりLLM Wikiに、**scheduler, tools, skills, validation, delivery** が重なっている。

---

# Agentic ETL 1: Collect

知識管理harnessの入力は、chatではなく継続的なsource stream。

```
feeds / blogs / newsletters / X / arXiv / hot topics
        ↓
scripts + cron
        ↓
checkpoint JSON
        ↓
raw immutable markdown
```

ここで大事なのは、sourceをすぐ要約で潰さないこと。
**rawを残すから、後から異なる問いで再検証できる**。

---

# Agentic ETL 2: Transform

Triageは「重要そうな記事を要約する」だけではない。

| 判断 | 具体アクション |
|---|---|
| 既存ページで足りる | entity / conceptへ追記 |
| 新規page thresholdを満たす | concept / entity / comparisonを作成 |
| 一回限りの問いとして有用 | `queries/`へ保存 |
| 古い情報と衝突 | 日付・出典つきでcontested / supersededとして残す |
| ノイズ・重複 | logでskip理由を残す |

この段階で、raw sourceは **wiki graphの差分** へ変換される。

---

# Agentic ETL 3: Load and Serve

LoadはDB投入ではなく、wikiを運用可能な状態へ戻すこと。

- frontmatter, tags, sources, wikilinksを揃える
- `index.md`をnavigation layerとして更新する
- `log.md`に時系列の操作履歴を残す
- pre-commitでtag taxonomyとindex破損を検出する
- digestやreportとしてmessengerへpushする

ここまで閉じて、source streamが **再利用可能な研究基盤** になる。

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

# 成功する知識業務agentの形

Hermesのuse case分析に引きずられず一般化すると、成功パターンはこうなる。

| パターン | なぜ効くか |
|---|---|
| Scheduled | 人間の依頼待ちではなく、source streamを定期的に処理できる |
| File-based | Markdown/JSON/YAMLはagentにも人間にも検査できる |
| Push-based | ダッシュボードを開かせず、結果をworkflowへ届ける |
| Skill-backed | 成功手順と落とし穴を次回に持ち越せる |
| Git-backed | 差分、rollback、review、監査が自然に付く |

「賢いchatbot」ではなく、**作業が回り続ける情報処理系** として設計する。

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

# 研究トピックとして見る

- **Learned context policy**: RLMやcontext-as-variableは、何を読むかをモデル自身に探索させる方向
- **Action space design**: strong primitiveか、typed APIか、code execution with toolsか
- **Trace-to-skill / trace-to-eval**: 実行ログから再利用手順と評価問題をどう作るか
- **Persistent memory correctness**: 便利な記憶と、誤った記憶の固定化をどう分けるか
- **Harness as RL environment**: half-workingな作業面を、次世代モデルの訓練環境へ変換できるか

ここでは「LLMに教える」のではなく、**LLMが学べる環境をどう作るか** が中心になる。

---

# まとめ

Harness Engineeringは、LLMの外側にある雑多な周辺機能ではない。
**モデルが仕事をし、失敗し、検証され、次回へ持ち越す作業面** の設計である。

Coding agentは、その作業面が最も見えやすい領域だった。
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
- Tom's Hardware, "China bans OpenClaw..." — https://www.tomshardware.com/tech-industry/artificial-intelligence/china-bans-openclaw-from-government-computers-and-issues-security-guidelines-amid-adoption-frenzy
- `blog/2026-05-12_hermes_harness-engineering-from-coding-agents-to-general-agents.md`
- `wiki/comparisons/open-harness-vs-agent-framework.md`
- `wiki/concepts/agent-harness.md`, `wiki/comparisons/agent-harnesses.md`
- `wiki/entities/hermes-agent.md`, `wiki/concepts/hermes-agent-use-cases.md`
- `config/hermes/skills/wiki/wiki-ingestion-pipelines/SKILL.md`

</div>
