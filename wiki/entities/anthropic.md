---
title: "Anthropic"
type: entity
aliases: [anthropic]
tags:
  - entity
  - model
  - anthropic
  - ai-agents
  - safety
status: complete
description: "AI safety-focused company behind Claude. Launched Claude Managed Agents for enterprise deployment. Also released Claude Code CLI agent and Promptfoo for prompt testing."
created: 2026-04-27
updated: 2026-05-26
sources: [
  "raw/newsletters/2026-05-17-anthropic-pulls-away-openai-strikes-back-and-google-s-gemini-rising.md",
  "https://x.com/RLanceMartin/status/2041927992986009773",
  "raw/articles/openai-is-cooking-the-anthropic-sweep-and-spacex-courts-cursor.md",
  "raw/newsletters/2026-04-26-openai-is-cooking-the-anthropic-sweep-and-spacex-courts-cursor.md",
  "raw/articles/2026-04-28-anthropic-claude-creative-coalition.md",
  "raw/articles/2026-04-30-anthropic-claude-security-public-beta.md",
  "raw/newsletters/2026-05-03-gemini-gets-to-work-claude-s-big-pull-and-openai-unchained.md",
  "raw/articles/2026-05-01_pentagon-seven-ai-deals-anthropic-excluded.md",
  "raw/articles/2026-05-04_techcrunch-anthropic-openai-jv.md",
  "raw/articles/2026-05-04_anthropic-enterprise-ai-services.md",
  "raw/articles/2026-05-05_reuters-openai-anthropic-jv-acquisitions.md",
  - raw/articles/2026-05-06_simon-willison_code-w-claude-2026.md
  - raw/newsletters/2026-05-15-codex-goes-everywhere.md
  - raw/articles/2026-05-18_sap-anthropic-claude-business-ai-platform.md
  - raw/newsletters/2026-05-19-can-i-get-my-agents-on-the-phone.md
  - raw/articles/wheresyoured.at--anthropics-profitability-swindle--d54ac6ec.md
  - raw/articles/2026-05-25_saas-fde-ai-agent-era_career-strategy.md
]
related: []
---


# Anthropic

## Overview

**Type:** AI Company
**Founded:** 2021
**Focus:** AI safety, constitutional AI, Claude language models, Claude Code
**Key Products:** Claude (LLM), Claude Code (CLI agent), Claude Managed Agents, Promptfoo

## Claude Managed Agents (Apr 2026)

Anthropic launched Claude Managed Agents — a platform for deploying autonomous AI agents in enterprise environments. Key features:
- Enterprise security and compliance (SOC2, HIPAA readiness)
- Governance and auditability for agent actions
- Integration with existing enterprise systems
- Foundation Capital partnership for go-to-market

### Memory Stores

Claude Managed Agents now supports persistent **memory stores** (April 2026):
- Memory stored as files (editable, exportable, auditable, versionable, rollback via API) — not a black-box vector store
- Mounted at `/mnt/memory/<store-name>/` in agent containers
- Multiple agents can access the same memory store with real-time sync
- Concurrency handling prevents agents from overwriting each other's updates
- Memories can be exported via the API
- Files are interpretable and sharable

The filesystem-as-memory approach was validated through [DavidSHershey's Claude Plays Pokémon experiment](https://x.com/DavidSHershey), showing that later models (Opus 4.6) learn to organize memory files much more effectively than earlier ones (Sonnet 3.5).

See [[concepts/claude-managed-agents]] for full details.


### Ed Zitron's Profitability Critique (May 2026)

[[entities/ed-zitron]] critically analyzed WSJ reporting that Anthropic was "about to have its first profitable quarter" (Q2 2026). Key findings in Zitron's analysis:

- **SpaceX discount**: Anthropic's deal with SpaceX for Colossus-1/2 includes a reduced fee during May–June ramp-up, artificially depressing compute costs. Full $1.25B/month payments start July. The "profit" is a temporary artifact of this discount.
- **Revenue inconsistencies**: Anthropic's ARR claims ($14B Feb → $19B Mar → $30B Apr) are difficult to reconcile with CFO Krishna Rao's sworn testimony (Mar 9) stating revenues "exceeding $5 billion to date."
- **Prepayment booking**: Zitron argues Anthropic likely books enterprise token prepayments ($50M+ for 12-month deals) as immediate revenue before compute delivery, inflating numbers.
- **Total compute cost estimate**: With SpaceX ($1.25B/mo) + Google/Amazon/Microsoft deals, estimated compute spend is ~$3.75B/month ($45B/year) — wiping out any real profitability.
- **Context**: This is consistent with Zitron's broader [[concepts/ai-bubble-thesis]], arguing Anthropic's economics depend on circular capital flows from hyperscaler investors who also bill them for compute.

### Live Artifacts in Cowork

Anthropic introduced **live artifacts** in Cowork mode (Apr 2026):
- Dashboards and trackers stay connected to apps/files
- Pulls fresh data on reopen — persistent live views

### Consumer Connectors

Claude now integrates with 15 new everyday consumer apps:
Booking.com, Resy, Spotify, Audible, Instacart, AllTrails, Thumbtack, TurboTax, Uber, and more.
Directory now exceeds **200 connectors** total.

### Claude Design (Apr 2026)

Anthropic launched **Claude Design**, an AI-driven design tool focused on marketing assets and brand creation:
- Requires importing design systems first (fonts, colors, components) — aligns with Google's proposed **Design MD** standard
- **Strengths**: Marketing assets, landing pages, brand kits, content-to-slides workflows
- **Weaknesses**: Complex product UX and app components (struggles with reasoning under rigid constraints)
- **Signature style tell**: Overuses italicized serif fonts on landing pages
- **Iteration speed**: 5–10 minute generation cycles per tweak vs. Figma's instant feedback
- Represents Anthropic's expansion beyond language models into creative tooling
- GPT Image 2.0 + Codex integration makes standalone design tools like Claude Design potentially redundant

### Creative Coalition (Apr 2026)

Anthropic launched **9 connectors** for professional creative tools, positioning Claude as a hub for creative and professional workflows:

| Connector | Functionality |
|-----------|--------------|
| **Adobe for Creativity** | 50+ Creative Cloud tools (Photoshop, Premiere, Express) for design workflows |
| **Autodesk Fusion** | Natural language control for 3D modeling and engineering design |
| **Blender** | MCP-based connector; Python API natural-language interface; Anthropic donated to Blender Foundation |
| **Affinity by Canva** | Batch image adjustments, layer renaming, file export automation |
| **SketchUp** | Room/furniture descriptions → 3D model starting points |
| **Ableton** | Product documentation for Live and Push (music production) |
| **Splice** | Royalty-free sample catalog search within Claude |
| **Resolume** | Real-time VJ/live visual artist control (Arena/Wire) |

- Built on **MCP (Model Context Protocol)** — interoperable with other LLMs
- Educational partnerships: RISD, Ringling College, Goldsmiths University
- Part of Anthropic's enterprise expansion strategy alongside Managed Agents

### Claude Security (Public Beta, Apr 2026)

Anthropic launched **Claude Security** in public beta for Enterprise customers, powered by **Claude Opus 4.7**:

- **Deep Code Reasoning**: Traces data flows, reads source code, examines file interactions — beyond pattern matching
- **Vulnerability Insights**: Confidence ratings, severity/impact assessment, reproduction steps
- **Targeted Patching**: Generates fix instructions; open and apply directly in Claude Code on the Web
- **Workflow Integration**: Scheduled scans, directory targeting, CSV/Markdown exports, webhooks to Slack/Jira
- **Ecosystem Partners**: CrowdStrike, Microsoft Security, Palo Alto Networks, SentinelOne, TrendAI, Wiz
- **Services Partners**: Accenture, BCG, Deloitte, Infosys, PwC

### Claude Security Performance

- **Claude Mythos** found **271 zero-day vulnerabilities in Firefox** in one sweep — ~4× what Mozilla patched in all of 2025
- Early users report moving from "scan to applied patch" in a single sitting
- Multi-stage validation pipelines reduce false positives

### Market Position (May 2026)

Anthropic leads enterprise AI adoption with strong market metrics:
- **40%** of enterprise LLM spend (surpassing OpenAI)
- **54%** of enterprise coding market share
- **$44B ARR confirmed (Q1 2026)** — 80x YoY revenue growth disclosed May 7, 2026. Doubling every ~6 weeks. $96M ARR added per day. See [[concepts/anthropic-2026-revenue-growth]].
- **$45B ARR expected** — 5x jump from $9B run-rate at end of 2025 (Financial Times, May 2026)
- **$50B raise at ~$1T valuation** in talks — would surpass OpenAI's $852B mark
- **IPO target**: October 2026 at $400–500B valuation (pre-$1T talks)
- Revenue growth driven by enterprise Claude adoption and Code with Claude 2026 launches (M365 GA, Dreaming, Managed Agents)
- Cleaner unit economics than OpenAI; focused on enterprise over consumer scale


### Enterprise Adoption Milestones (May 2026)

- **PwC Certification**: 30,000 PwC staff certified on Claude — one of the largest single-organization AI training programs
- **Ramp AI Index**: Anthropic-powered businesses show 34.4% AI adoption vs. 32.3% for non-Anthropic — indicating measurable productivity advantage
- **Four Fronts of AI Competition**: Anthropic published a paper identifying the 4 dimensions of AI competition (models, deployment, trust, economics)

### Colossus 1 — Memphis 300MW Deployment

Anthropic's **Colossus 1** compute cluster in Memphis provides 300MW / 220K+ GPU capacity, operational as of May 2026. This is part of the SpaceXAI partnership and represents Anthropic's largest dedicated training infrastructure.


### Gates Foundation Partnership (May 2026)

Anthropic and the **Bill & Melinda Gates Foundation** announced a **4-year, $200 million** partnership to develop AI solutions for global health, education, and agriculture. The collaboration focuses on public-interest AI applications in low-resource settings. While significant for AI-for-good narrative, the direct technical wiki value is limited — reference-level addition.

> Source: [Gates Foundation press release](https://www.gatesfoundation.org/ideas/media-center/press-releases/2026/05/ai-anthropic-partnership) (May 2026)

### $1.5B Services Joint Venture (May 2026)

Anthropic partnered with Blackstone, Hellman & Friedman, and Goldman Sachs to form an **unnamed JV** focused on developing Claude-powered systems tailored to specific organizational operations:

| Detail | Value |
|--------|-------|
| **Total Raise** | $1.5B ($300M each from main participants) |
| **Focus** | Claude-powered enterprise deployment systems |
| **Significance** | Part of broader industry shift from model APIs to service delivery |
| **Context** | See [[concepts/ai-services-joint-ventures]] for full comparison with OpenAI's $4B Deployment Company |

### Anthropic Orbit (Leaked, May 2026)

**Orbit** is a rumored proactive assistant from Anthropic that synthesizes data from enterprise tools without explicit prompts:

- **Integration scope**: Slack, Gmail, GitHub, Figma, and other workplace tools
- **Proactive mode**: Auto-generates briefings and summaries from ingested data
- **Positioning**: Counter to ChatGPT Pulse (OpenAI's proactive assistant)
- **Status**: Leaked/discussed in Superintel newsletter (May 2026); not officially announced

### Code w/ Claude 2026 (May 2026)

At Anthropic's Code w/ Claude 2026 event, several Managed Agents features were announced:

| Feature | Status | Description |
|---------|--------|-------------|
| **Multi-agent orchestration** | Public beta | Create fleets of agents to solve complex tasks in parallel |
| **Outcomes** | Public beta | Define success criteria; Claude iterates autonomously until achieved ("Ralph loop" style) |
| **Dreaming** | Research preview | Claude inspects past sessions, identifies missed opportunities, self-improves overnight |

**Other announcements**:
- **Adviser strategy**: Opus provides advice on demand to smaller models (Sonnet) — "frontier model quality at 5x lower cost"
- **Rate limits**: Doubled Claude Code 5-hour limit for Pro, Max, Enterprise customers
- **API volume**: 17x year-on-year growth
- Dianne Na Penn emphasized "design for the next model" — build things that don't quite work today

Source: Simon Willison's [live blog](https://simonwillison.net/2026/May/6/code-w-claude-2026/)

### Claude Code

Anthropic's CLI coding agent (see [[entities/claude-code]]). A terminal-based agent that can:
- Read, write, and edit code
- Run commands
- Understand codebases at scale
- Operate via CLAUDE.md configuration

## Claude

Claude is Anthropic's flagship language model series. Key versions referenced in recent discussions:
- **Claude Opus** — Most capable
- **Claude Sonnet** — Balanced capability and speed
- **Claude Haiku** — Fast, efficient


### Claude for Small Business — 15 Workflows (May 2026)

Anthropic announced **15 ready-to-run workflows** for small business applications inside QuickBooks, PayPal, HubSpot, Canva, and Docusign — at **no extra cost** to existing Claude subscriptions:

| Use Case | Platform | Description |
|----------|----------|-------------|
| **Accounting** | QuickBooks | Invoice reconciliation, expense categorization |
| **Payments** | PayPal | Transaction dispute handling, refund processing |
| **CRM** | HubSpot | Lead enrichment, pipeline management automation |
| **Design** | Canva | Brand-consistent asset generation |
| **Documents** | Docusign | Contract review, signature workflow automation |

- **Market rationale**: Small businesses represent 44% of US GDP — a strategic segment often overlooked by enterprise-first AI companies
- **Competitive positioning**: Differentiator against OpenAI Codex, which targets enterprise and developer markets
- **Additional integration**: Claude Cowork + MCP connectors to Westlaw and Everlaw for legal workflows

Source: Aakash's Clicky newsletter (May 2026)

### KPMG x Anthropic Global Alliance (May 2026)

KPMG and Anthropic announced a **global alliance** embedding Claude Cowork and Claude Managed Agents inside **KPMG Digital Gateway**:

| Detail | Value |
|--------|-------|
| **Scope** | Global alliance embedding Claude in KPMG's delivery platform |
| **Initial Focus** | Tax, legal, and private-equity work |
| **Workforce** | 276,000 KPMG professionals gain access to Claude |
| **Significance** | Largest single-enterprise AI deployment by workforce size to date |

This represents a major milestone for enterprise AI adoption — KPMG is one of the Big Four accounting firms with global reach across tax, audit, and advisory. The partnership gives Anthropic direct access to enterprise client workflows through the KPMG channel.

Source: Superintel Google I/O newsletter (May 2026)

## Mythos Breach (Apr 2026)

Anthropic's internal "too dangerous to release" model **Mythos** was accessed on launch day by four individuals in a private Discord. The group:
- Guessed the endpoint URL from naming conventions + a Mercor breach leak
- Used a contractor's legitimate evaluation credentials
- Used the model to build simple websites (not malicious purposes, but the access was unauthorized)

The incident highlights risks of: inference endpoint discoverability, credential sharing among contractors, and naming convention predictability.

## Pentagon Blacklisting (Feb–May 2026)

Anthropic was designated a **"supply chain risk"** by the Pentagon in February 2026 — the first time an American company has received this label — after refusing the "any lawful use" clause in defense contracts. Anthropic objected citing concerns about:
- **Autonomous lethal weapons**: Claude models could potentially pilot drones or make targeting decisions
- **Domestic mass surveillance**: "Lawful use" could extend to monitoring U.S. citizens

### Escalation Timeline
- **Feb 2026**: Pentagon blacklists Anthropic; OpenAI strikes deal hours later (Altman: "opportunistic and sloppy")
- **Mar 2026**: Anthropic sues in San Francisco and Washington D.C. to reverse blacklisting
- **Apr 2026**: [[entities/claude-mythos|Mythos]] demonstrated finding 271 Firefox zero-days; White House reopens discussions
- **May 1, 2026**: Pentagon signs 7 AI companies (SpaceX, OpenAI, Google, Nvidia, Microsoft, AWS, [[entities/reflection-ai|Reflection AI]]) — Anthropic excluded
- **May 2026**: DOD CTO Emil Michael says Mythos is a "separate national security moment"; NSA reportedly using it despite the blacklist

### Implications
- **Anthropic losing $50B+ defense contracts** while competitors profit
- **Mythos paradox**: Model too dangerous for public release, but too valuable for Pentagon to completely exclude
- **$900B valuation target**: May be impacted by defense revenue exclusion
- Dario Amodei met with White House Chief of Staff Susie Wiles; Trump says deal is "possible"

See [[concepts/ai-military]] for broader context.

## Claude Cowork Philosophy — Felix Rieseberg (May 2026)

Felix Rieseberg, Engineering Lead for Claude Cowork and Claude Code Desktop at Anthropic, demonstrated his personal Claude workflow in a deep-dive interview. Key philosophical and practical contributions:

- **Go one abstraction layer up**: Rather than micromanaging Claude's every step, Rieseberg describes his work in high-level goals and lets Claude figure out the implementation. This is the core principle behind Claude Cowork's "background agent" model.
- **Email as personal database**: Uses email as an unstructured inventory/system-of-record, with Claude Cowork extracting structured data from it on demand — a pragmatic alternative to building a custom database.
- **Live Artifacts**: Creates dashboards that auto-update from connected apps (Jira, Salesforce, Google Sheets), turning static documents into live operational tools.
- **Model selection strategy**: Uses Claude Sonnet for most daily tasks (faster, cheaper) and switches to Claude Opus for hard reasoning problems — a model-routing approach optimized for cost.
- **The real barrier is psychological**: The hardest part of adopting AI is unlearning 20 years of assuming "computers can't do this." Rieseberg argues the bottleneck is human, not technical.

### Hardware Prototyping Culture

Rieseberg hacked a $20 hardware "Claude buddy" device as a proof-of-concept — demonstrating Anthropic's internal culture of rapid, playful experimentation with AI integration.

See also: [[concepts/agentic-engineering]] section on [[concepts/agentic-engineering/context-window-management|context window management]] and [[concepts/agentic-engineering/red-green-tdd|Red/Green TDD pattern]].


### Jack Clark's Predictions (May 2026)

Anthropic co-founder Jack Clark made several bold forecasts at an Oxford University lecture:

- **Nobel-worthy AI discovery**: An AI system working with humans will achieve this within 12 months
- **Bipedal robots for tradespeople**: Within 2 years, robots will assist skilled tradespeople
- **AI-only companies**: Within 18 months, companies run solely by AI will generate millions in revenue
- **Self-designing AI**: By end of 2028, AI will design next-generation AI systems
- **Claude Mythos warning**: Clark noted that Claude Mythos is "surprisingly capable at exploiting cybersecurity vulnerabilities," underscoring the need for safety research

Source: Superintel newsletter via Anthropic co-founder Oxford lecture (May 2026).


## Research Focus

Anthropic's research priorities:
- AI safety and alignment
- Constitutional AI
- Scalable oversight
- Interpretability

## Code w/ Claude 2026 — Product Launches (May 2026)

Anthropic は Code w/ Claude 2026 イベントで複数の新製品・機能を発表した：

### Microsoft 365 GA

Claude の Microsoft 365 統合が大幅に進展：

- **Excel, PowerPoint, Word**: 一般提供（GA）開始
- **Outlook**: パブリックベータ公開
- Microsoft アプリ間で Claude が会話コンテキストを保持

### Dreaming — Managed Agents 研究プレビュー

「Dreaming（夢想）」機能が研究プレビューとしてローンチ。Managed Agents プラットフォーム上で動作し、以下がパブリックベータに移行：

- **Outcomes**: エージェントの成果物管理
- **Multi-agent orchestration**: 複数エージェントの協調実行
- **Webhooks**: 外部サービス連携

### 金融サービス向けテンプレート

Cowork / Claude Code のプラグインとして、または Managed Agents として本番実行可能な金融サービス用エージェントテンプレートを提供：

- 投資ピッチ作成
- バリュエーションレビュー
- 月末決算処理

### 資金調達と評価額

Financial Times 報道（2026年5月）：

- **最大$50Bの資金調達**を協議中
- **評価額$1T近辺**を目標 — OpenAI の $852B を上回る
- 調達資金はほぼ全額**計算資源の拡大**に充当予定（供給制約が顧客サービスに影響を与えている）

### 計算資源パートナーシップの全体像

Anthropic は複数の大規模計算資源契約を締結：

| パートナー | 規模 | 状況 |
|-----------|------|------|
| **SpaceXAI (Colossus 1)** | 300MW / 220K+ GPU; $1.25B/month | 2026年5月発効 |
| **Amazon** | 最大5GW（2026年末までに~1GW新規） | 契約締結済み |
| **Google + Broadcom** | 5GW | 2027年稼働開始予定 |
| **Microsoft + NVIDIA** | $30B Azure容量 | 戦略的パートナーシップ |
| **Fluidstack** | $50B 米国AIインフラ投資 | 発表済み |

Claude は **AWS Trainium、Google TPU、NVIDIA GPU** の複数ハードウェアで訓練・実行されている。

**SpaceX S-1 Filing Details (May 2026)**: SpaceX's S-1 registration statement reveals the full terms of the Cloud Services Agreement with Anthropic: $1.25 billion per month through May 2029, with capacity ramping in May and June 2026 at a reduced fee. The agreements may be terminated by either party upon 90 days' notice. Notably, SpaceX also uses this compute capacity for its own AI applications (including Grok 5, training at COLOSSUS II), positioning Anthropic as both a customer and a revenue source for SpaceX's growing AI compute business.

Source: [Simon Willison quoting SpaceX S-1](raw/articles/simonwillison.net--2026-may-20-spacex-s1--48fe0f3d.md)

### 収益性論争: 「黒字化」の実態 (May 2026)

2026年5月21日、Wall Street Journal が Anthropic の「初の黒字四半期」報道を掲載:

- Q1 2026 売上: **$4.8B** → Q2 2026 売上予測: **$10.9B**
- Q2 2026 営業利益: **$559M** (EBITDAベース)
- ウォールストリートジャーナル自身が脚注: 「非公開企業のため会計基準は不明」

しかし、Ed Zitron（[[entities/ed-zitron-s-where-s-your-ed-at]]）の詳細分析により、この「黒字化」は本質的に**会計上の演出**であることが明らかに:

#### SpaceX 割引の構造

SpaceX S-1 提出書類に開示された Colossus 契約の真実:
- 通常料金: $1.25B/月（= $15B/年）
- **May-June 2026 は「立ち上げ期間」として割引料金** — つまり黒字化を謳う四半期と**完全に一致**
- 7月以降は通常料金に戻り、年間計算では非黒字に戻る見込み

#### ARR / 収益データの矛盾

Anthropic が公表してきた ARR 数字間の不整合:

| 日付 | 主張 | 月換算 |
|------|------|--------|
| 2026/02/12 | ARR $14B | ~$1.17B/月 |
| 2026/03/03 | ARR $19B (Dario Amodei) | ~$1.58B/月 |
| 2026/03/09 | 累積収益「$5B超」(CFO Krishna Rao, 宣誓供述) | — |
| 2026/04/06 | ARR $30B | ~$2.5B/月 |
| Q1 2026 | WSJ 報道: $4.8B | — |

CFO の宣誓供述における「$5B超」と WSJ の Q1 単独 $4.8B という数字は深刻な矛盾をはらむ。Rao が裁判所に対して自社ビジネスを 30-40% 過小に申告したとは考えにくい。

#### 総費用の試算

「黒字化」が持続不可能である理由:
- SpaceX に $1.25B/月 × 12 = $15B/年
- AWS/Google Cloud も同規模以上と仮定 → 各 $1.25B/月
- 四半期あたり計算資源コスト: ~$11.25B
- 年間計算資源コスト: ~$45B
- 加えて2026年1月時点で推論コストが予想比23%高い (The Information 報道)

#### 追加的な収益水増しの可能性

Zitron が指摘する手法:
- 大口企業からのトークン前払い（12ヶ月分の$50Mを一括計上）
- Claude 追加クレジット購入の前払い計上（10-30%割引）
- 年間契約の前倒し計上
- 訓練負荷の意図的な抑制による推論余力確保

#### アナリストの評価

Zitron の結論:
> 「会計不正とは言わないが、数字の指圧級マッサージ（shiatsu-grade massaging）ではある。Anthropic はコストを抑制できると知っている特定の四半期を選んで『黒字』をリークし、ジャーナリストに『コストは増加する可能性がある』という逃げ道を与え、NVIDIA 決算発表日に合わせてリリースした」

「AIバブル懐疑派」への直接的な呼びかけとして、**真にAnthropicの成功を願うなら、むしろこの数字に懐疑的であるべき**と主張。WeWork の「2ヶ月目から黒字」主張との類似性を指摘。

Source: [Ed Zitron — Anthropic's "Profitability" Swindle](raw/articles/wheresyoured.at--anthropics-profitability-swindle--d54ac6ec.md)



### Stainless Acquisition — SDK/MCP Platform (May 2026)

Anthropic acquired **Stainless**, a SDK/MCP server platform company:

| Detail | Value |
|--------|-------|
| **Target** | Stainless — builds SDKs for API-first companies |
| **Notable customer** | OpenAI also used Stainless SDK |
| **Post-acquisition** | Stainless service shutting down; technology integrating into Anthropic |
| **Significance** | Vertical integration: Anthropic now owns the SDK layer for its API ecosystem |

Stainless specialized in generating high-quality SDKs from API specifications. Its acquisition gives Anthropic direct control over the developer experience layer — the tools developers use to interact with Claude's API and MCP servers.

Combined with Claude Managed Agents' **Self-Hosted Sandboxes + MCP Tunnels** (launched same week), this represents a pattern of aggressive vertical integration across the entire agent stack: models → SDKs → sandboxes → deployment.

### SAP Business AI Platform (May 2026)

At SAP Sapphire 2026, Anthropic and SAP announced plans to embed Claude as a primary reasoning and agentic engine across SAP's AI-enabled portfolio, powering Joule and Joule agents via the [[entities/sap-business-ai-platform]]. Claude connects to the platform to coordinate tasks across SAP S/4HANA, SuccessFactors, and Ariba via MCP. Christian Klein (SAP CEO) and Daniela Amodei (Anthropic president) jointly announced the partnership.

Key focus industries: public sector, healthcare, education, life sciences, utilities.

## Applied AI / FDE サービス戦略 (2026年5月)

### FDE (Forward Deployed Engineer) 採用

Anthropic の FDE 求人要項では、以下の責務が明示されている：

- **顧客システムへの深い入り込み**：顧客の本番環境に直接入り、Claude、MCPサーバー、サブエージェント、Agent Skills を活用した本番アプリケーションを構築
- **再利用可能なパターンの抽出**：「反復可能なデプロイメントパターンを特定・体系化し、Product/Engineering チームにフィードバックする」ことが中核的責務

これは、OpenAI が採用しているのと同じ **FDE → Product フィードバックループ** の哲学を Anthropic も共有していることを示している。

### エンタープライズ AI サービス合弁会社

Blackstone、Hellman & Friedman、Goldman Sachs とのパートナーシップにより、中堅企業向けのエンタープライズ AI サービス会社を設立：

- 重要業務への Claude 組み込みを支援
- 業界特化型のデプロイメントパターンを蓄積

### 戦略的意味

Anthropic は OpenAI（DeployCo）と同じ構造的転換を進めている — **API/モデルプロバイダーからデプロイメントサービスプロバイダーへの進化**。FDE モデルはフロンティアラボ全体で業界標準となりつつある。

## Related
- [[entities/anthropic]] — The model family
- [[entities/claude-code]] — Claude Code CLI agent
- [[entities/claude-mythos]] — Claude Mythos model (used by Claude Security)
- [[entities/foundation-capital]] — Partner in Claude Managed Agents
- [[entities/sap-business-ai-platform]] — SAP partnership (May 2026)
- [[concepts/claude-managed-agents]] — Managed Agents platform details
- [[concepts/project-glasswing]] — Defensive security initiative

## References

- 2026-04-12-anthropic-openclaw-subscription-ban
- 2026-04-15-property-based-testing-anthropic

- 2026-04-26-claude-code-anthropic-agentic-coding-system
- anthropic-claude-code-session-management-1m-context
