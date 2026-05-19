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

<div class="kicker">第29回LLM勉強会</div>

# Harness Engineering と AI Agent

## AI Agent を回すruntime境界の設計

Hermes Agent & LLM Wiki によるAI Topics自動追跡の事例
<br />

<div class="small">
2026年５月19日<br />
株式会社IVRy 稲村和樹　(Kazuki Inamura)
</div>

---

# 今日の主張

- AI Agent の実応用を支えている Harness Engineering が注目を浴びている。
- Harness の定義は揺れやすいが、その意義は次に集約される:
  - 1) AI Agentの実行を支える基盤として実用性を担保する役割
  - 2) LLMの能力獲得の足場としての役割
- また、発表者がAI界隈の情報収集に活用している Agent Harness 事例も紹介する。

---

# Agent Harnesses

2026年に入り、Agent Harness はcoding領域の外へと広がっている。代表例はClaude Code/Codexだが、オープンハーネスの利用も広がっている。

- Claude Code/Cowork
- Codex
- OpenClaw (uses the Pi SDK)
  - コアで叩かれる Pi それ自体もハーネス
- Hermes Agent
- etc.

---

# OpenClaw と Hermes Agent

25年末以降にかけての、個人向け汎用agentの爆発的普及。特に中国で盛ん。
メッセンジャーアプリ連携、定期実行、Skill拡張、記憶システムといった基本機能

1. OpenClaw: 汎用常駐agentとして爆発的に普及したgateway型ハーネス
2. Hermes Agent: Nous Research発の自己進化型ハーネス。OpenRouter appsで#1

爆発的普及に伴い、不注意なホスティングや悪意のあるSkillの使用による大規模な機密情報流出も発生。

NVIDIAやLLMプロバイダーが正式にサポートを主張。Open harness適合が競争軸に。

<!-- _footer: "https://www.china-briefing.com/news/china-agentic-ai-openclaw-boom/" -->

---

# 私の活用事例: LLM Wiki + Hermes Agent

課題: AI/Agent領域の日々のキャッチアップや知識の管理・検索が扱えなくなりつつあった。

Karpathyの **LLM Wiki** をAI/Agent領域の話題追跡・管理に適用している:

- `document -> raw/ -> wiki` (Agentic ETL)
  - rawは不変、wiki への書き込み・編集・クエリ処理はAgentが行う
  - 各種lintもAgentが行い、自動で保守される
- `q -> wiki -> answer` (Agentic RAG)
  - 知識の事前マップを構築することで、知識の取り出しを効率化

SNS / RSS / newsletter / paper といったsource streamを毎日自動で取り込む

<!-- _footer: "https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f" -->

---

# Hermes Agent が足している実行層

Hermes Agent はLLM Wikiを実運用可能な基盤に乗せる。

| Harnessパターン | AI Topicsでの効き方 |
|---|---|
| Scheduled (cron) | 人間の依頼待ちではなく、定期的にsource streamを処理 |
| File-based | Markdown / Code / Config をAgentが自己修正し、人間もreview可能 |
| Skill-backed | 成功手順と落とし穴を `llm-wiki` / ingestion skills に戻す |
| Validated (lint) | schema / index / tag / link / duplicate を継続検査 |
| Push Delivery | server側実行結果をmessage channelへ届ける |
| Git/Checkpoints | 差分管理、rollback、監査などを備える |

Hermes により、LLM Wikiは **作業が回り続ける　＆ 進化する runtime 環境** になる。

---

# 失敗traceを改善資産にする

Harness は成功を増やすだけでなく、失敗を繰り返さないようにするための足場となる。

| LLM Wikiでの失敗例 | Harness側の改善 |
|---|---|
| ページ重複 | 既存pageがないか先に確認 (`index.md`, `log.md`) |
| cron処理失敗 | script/configなどコード修正, AGENTS.md追記, Skill化 |
| タグが散らかる | pre-commit validator, tag taxonomy (`SCHEMA.md`) |
| skill爆発 | skill dedup, invocation metrics (`Curator`) |

<br />

<div class="small">
参考. Mitchell Hashimoto 氏の発言(2026/02)

> I don't know if there is a broad industry-accepted term for this yet, but I've grown to calling this **"harness engineering."** It is the idea that anytime you find an agent makes a mistake, you take the time to engineer a solution such that the agent never makes that mistake again.

</div>

<!-- _footer: "https://mitchellh.com/writing/my-ai-adoption-journey#step-5-engineer-the-harness" -->

---

# What is Harness?

Harness とは、モデルの外側で **観測→実行→検証→記憶** を閉じるruntime境界。

| 層 | 役割 | 例 |
|---|---|---|
| Model | 次に何を試すかを判断する | Claude, GPT, Gemini, local models |
| Harness | agentの作業を成立させる | prompt, tools, memory, skills, verification loop |
| Runtime | executionを継続・仲介する | lifecycle, scheduling, permission, observability |
| Task Environment | actionが作用する世界/infra | filesystem, bash, browser, GUI |

Runtime と Harness の境界は曖昧 (RuntimeをHarnessに含める向きもある)
開発者が主導するWorkflow中心の設計から、モデルが自律駆動するRuntime中心の設計へと推移。

---

![alt text](harness-bounded-contexts.png)

---

# Effective Harness: Harnessの意義

「観測→実行→検証→記憶」が同じruntimeでつながると、Agentのタスク遂行能力に効く。

- Reliability: test/lint/schema/screenshot で「やったつもり」を潰す
- Debuggability: trace で、何を見て何を実行しどこで失敗したかを追える
- Safety: model へのお願いではなく、 hooks/runtime policy で止める
- Continuity: memory/skills/file state/session が次回へ残る
- Ownership: Open harness では trace/memory/policy がユーザー所有

主に 流行っていた。Harness Engineering の前身といえる。

---

Context Engineering: 2025年中盤には Continuity に効く文脈のやりくりが盛んだった

![alt text](harness-context-eng.png)

<!-- _footer: "https://rlancemartin.github.io/2025/06/23/context_engineering/" -->

---

"Hidden Technical Debt in Machine Learning Systems" (NIPS 2015) のアナロジー

![alt text](harness-hidden-technical-debt.png)

<!-- _footer: "https://leehanchung.github.io/blogs/2026/04/24/hidden-technical-debt-agent-runtime/" -->

---

# Model Scaffold: モデルに能力を取り込む役割

Harness 価値の一部は最終的にモデル側へ吸収される (The Bitter Lesson)。

RL-harness lifecycle:
```
runtime上で半分うまく動くscaffoldを作る
  -> 成功/失敗trace, eval, rewardが集まる
  -> RL/post-trainingでモデル側に能力が内在化される
  -> 古いscaffoldを削り、より難しいscaffoldを足す
```

失敗をtraceに残し、個別的な要件はskillsやhooksに残すが、汎用的な能力は事後学習で吸収。
LLM ProviderにとってHarness Engineeringのもうひとつの戦略的核心はここだと考えられる。

<!-- _footer: "https://x.com/willccbb/status/2045956400770404422?s=20" -->

---

![alt text](harness-training-loop.jpg)

<!-- _footer: "https://addyosmani.com/blog/agent-harness-engineering/" -->

---

# まとめ

Harness Engineeringは、LLMの外側にある雑多な周辺機能ではない。
**モデルが実行を継続し、失敗し、検証され、次回へ持ち越すruntime境界** の設計である。

実用上はagentic codingに限らず、一般のナレッジワーカー業務にも自律実行可能な足場を与えている。

失敗traceを改善資産に変える営みに組み込まれることで、AI AgentやLLMの能力獲得の足場にもなっている。

---

# (参考) Harness and Environment

Harnessは「どの世界を操作するか」で信頼性が大きく変わる。

| Task Type | Environment | 複雑性 | なぜ効く/難しいか |
|---|---|---|---|
| Coding | filesystem / shell / git | Low | symbolic, stable, replayable, verifiable |
| Wiki | markdown / graph / schema | Low-Mid | file-basedだが、意味の検証が難しい |
| Browser | DOM / Web session | Medium | UI変化、ログイン、外部状態が絡む |
| Computer use | GUI / OS / pixels | High | action spaceが広く、検証も難しい |
| General | mixed environment | Variable | 複数環境を一貫して作業継続する困難 |

Coding agentが先に実用化した理由は、モデルだけでなく **環境が検証しやすかった** から。
複雑性が高い領域ほど、応用範囲を絞るなどして複雑性を下げる工夫が必要となりやすい。

---

# (参考) Open harness と Runtime ownership

Open harnessの争点は、単なるモデル差し替えではない。
**trace / memory / skills / policy をユーザーが所有し、次の改善に使える点**が重要。

| 観点 | Closed harness | Open harness |
|---|---|---|
| 例 | Claude Code, Codex | OpenCode, Pi, OpenClaw, Hermes |
| 学習 | vendorがtraceを集め、model/runtimeをco-design | userがfull-trace, skills, memoryを保持 |
| 強み | モデル適合が速い、UXが一貫 | portability, BYOK/local, 監査可能 |
| リスク | hidden orchestration, lock-in | safety/governanceを利用者が背負う |

---

# (参考) Framework/Runtime/Harness

|  | Framework | Runtime | Harness |
|---|---|---|---|
| 付加価値 | ・抽象化レイヤー<br>・各種インテグレーション | ・永続的実行 (durability) <br>・ストリーミング<br>・Human-in-the-Loop<br>・永続化(Persistence) | ・定義済みツール群<br>・定義済みプロンプト<br>・サブエージェント機能 |
| 利用場面 | ・素早くエージェント開発を始めたい<br>・チームの構築方法を標準化したい | ・低レベルでの細かな制御が必要<br>・長時間実行・ステートフルな実行 | ・より自律的なエージェントが必要<br>・複雑で非決定的なタスク<br>・**素早くエージェント活用を始めたい** |
| 製品例 | ・LangChain<br>・Vercel AI SDK<br>・OpenAI Agents SDK<br>・Google ADK | ・LangGraph<br>・Temporal<br>・Inngest | ・Deep Agents SDK<br>・Claude Agent SDK<br>・Manus |

LangChainの定義では、Runtime と Harness を区別してOSSを提供している。

<!-- _footer: https://docs.langchain.com/oss/python/concepts/products -->

