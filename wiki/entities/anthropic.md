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
updated: 2026-07-08
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
  - raw/newsletters/2026-05-26-the-pope-and-anthropic-partner-on-the-ai-ethics-debate.md
  - raw/newsletters/2026-06-06-rsi-when-ai-starts-building-its-own-successors.md
  - raw/articles/2026-06-07_anthropic_recursive-self-improvement.md
  - raw/newsletters/2026-07-08-anthropic-3q26-profit-over-1b-the-anthropic-ipo-financials-sneak-peak.md
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

See [[concepts/anthropic/managed-agents]] for full details.


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


### Recursive Self-Improvement & Code Self-Generation (June 2026)

On June 4, 2026, the Anthropic Institute published **"When AI builds itself"** — the company's official declaration framing recursive self-improvement as its explicit strategic path forward. Authored by Marina Favaro and Jack Clark, the article represents the most comprehensive public disclosure by any frontier lab of internal AI-accelerated development metrics.

**Official declaration**: Anthropic explicitly states it is "delegating a growing share of AI development to AI systems themselves" and frames this as trending toward "an AI system capable of fully autonomously designing and developing its own successor." While noting RSI is "not inevitable," they argue "it could come sooner than most institutions are prepared for."

**Key metrics disclosed**:
- **8x code output**: Engineers ship 8x as much code per quarter vs. 2021-2025 baseline
- **>80% AI-authored code**: Claude writes >80% of code merged into Anthropic's codebase (May 2026), up from low single digits before Claude Code (Feb 2025)
- **4x productivity**: Internal poll of 130 researchers found median ~4x output gain with Mythos Preview
- **76% open-ended task success**: Claude's success rate on hardest engineering tasks reached 76% (up 50pp in 6 months)
- **40% research steering**: Claude judged better than human researchers at ~40% of research decision points (n=129)
- **800+ bug fixes**: Claude shipped 800+ fixes in April 2026, reducing a class of API errors 10-fold

**Three future scenarios outlined**: (1) Continuation — steady acceleration with AI handling more of AI dev, (2) Acceleration — fast takeoff surpassing human AI R&D capabilities, (3) Failure — plateau from fundamental limitations.

**Dual framing**: The article serves simultaneously as technical roadmap and valuation narrative supporting Anthropic's ~$1T valuation target and imminent IPO (S-1 filed June 2026). By articulating RSI as explicit strategy, Anthropic positions itself to capture compounding returns of AI-accelerated AI development.

**Policy stance**: Anthropic expresses desire for a "meaningful slowdown or pause" option but acknowledges practical barriers requiring multi-lab, multi-country coordination. They commit to organizing policy conversations about RSI governance.

**Community response**: The article sparked a **692-comment Hacker News discussion**, reflecting intense community engagement. Key reactions:
- **Skepticism**: [[entities/gary-marcus]] characterized results as "faster coding — entirely under human control" rather than true AGI/RSI
- **Metric debates**: Lines-of-code as productivity proxy heavily contested; some argued AI-generated code requires more review
- **Governance urgency**: Verification regimes for complex tech (e.g., INF Treaty) took decades — time the AI community may not have

The 80% code self-generation figure was met with both alarm and skepticism. Marcus argued the results demonstrate RSI (AI as a useful coding tool) rather than AGI. The internal data suggests Claude's role in Anthropic's own development pipeline has crossed a critical threshold where the majority of code contributions are now AI-generated.

This development sits alongside Claude's [[concepts/agentic-engineering]] capabilities and [[concepts/anthropic/managed-agents]] platform as part of a broader acceleration in Anthropic's internal AI R&D pipeline.

### SemiAnalysis IPO Financial Projection (July 2026)

SemiAnalysis, citing their proprietary Tokenomics Model, projected Anthropic would achieve **over $1B in profit by 3Q26** and noted the company confidentially filed for IPO on **June 1, 2026**. These claims supplement earlier reporting on the $400-500B October 2026 IPO target. **⚠️ Caveat**: The SemiAnalysis article is behind a full paywall; the profit projection and filing date are sourced from a 5-paragraph free preview and should be treated as unverified secondary reports. The existing IPO target (October 2026, $400-500B from earlier WSJ reporting) remains the most substantiated timeline.

> Full article: [[raw/articles/2026-06-07_anthropic_recursive-self-improvement]]
>
> See also: [[concepts/recursive-self-improvement]] — comprehensive wiki page covering RSI theory, harness-based approaches, evolutionary search, and safety concerns

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
- **$44B ARR confirmed (Q1 2026)** — 80x YoY revenue growth disclosed May 7, 2026. Doubling every ~6 weeks. $96M ARR added per day. See [[concepts/anthropic/2026-revenue-growth]].
- **$45B ARR expected** — 5x jump from $9B run-rate at end of 2025 (Financial Times, May 2026)
- **$50B raise at ~$1T valuation** in talks — would surpass OpenAI's $852B mark
- **IPO target**: October 2026 at $400–500B valuation (pre-$1T talks)
- Revenue growth driven by enterprise Claude adoption and Code with Claude 2026 launches (M365 GA, Dreaming, Managed Agents)
- Cleaner unit economics than OpenAI; focused on enterprise over consumer scale


### Enterprise Adoption Milestones (May 2026)

- **PwC Certification**: 30,000 PwC staff certified on Claude — one of the largest single-organization AI training programs
- **Ramp AI Index (May 2026)**: Anthropic overtook OpenAI in paid business subscriptions for the first time: Anthropic 34.4% (up 3.8% MoM), OpenAI 32.3% (down 2.9%). Overall AI business adoption reached 50.6% of companies tracked by Ramp.
  - **Three headwinds to sustainability**: (1) Misaligned token volume incentives, (2) Claude performance outages and rate limits, (3) 3x token costs for image-containing prompts
  - **Caveat**: Ramp notes the market is fluid and cost-sensitive; Anthropic's lead is not guaranteed
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

### Trigger: Palantir AIP Incident
The dispute was directly triggered when Claude appeared on screens of officials monitoring the Venezuela Maduro seizure operation via [[entities/palantir]]'s AI Platform. During a routine check-in, Anthropic representatives expressed concerns; Palantir reported this to the Pentagon.

### Escalation Timeline
- **Feb 2026**: Pentagon blacklists Anthropic; OpenAI strikes deal hours later
- **Mar 9, 2026**: Anthropic files suit in N.D. California (*Anthropic PBC v. Department of War*)
- **Mar 26, 2026**: Judge Rita F. Lin issues injunction against supply chain risk designation (First Amendment ruling)
- **Apr 3, 2026**: GSA restores Anthropic technology per presidential directive
- **Apr 8, 2026**: D.C. Circuit denies emergency motion to lift FASCSA designation
- **May 1, 2026**: Pentagon signs 7 AI companies (SpaceX, OpenAI, Google, Nvidia, Microsoft, AWS, [[entities/reflection-ai|Reflection AI]]) — Anthropic excluded
- **May 2026**: DOD CTO Emil Michael says Mythos is a "separate national security moment"; NSA reportedly using it despite the blacklist

### Current Status (June 2026)
- **No settlement reached** — litigation ongoing in D.C. Circuit
- Judge Lin's injunction remains in effect (supply chain risk partially blocked)
- FASCSA 180-day exclusion timeline proceeding for DoD target systems
- Anthropic cannot serve as primary contractor/subcontractor on DoD systems

### Implications
- **Anthropic losing $50B+ defense contracts** while competitors profit
- **Mythos paradox**: Model too dangerous for public release, but too valuable for Pentagon to completely exclude
- **$900B valuation target**: May be impacted by defense revenue exclusion
- Dario Amodei met with White House Chief of Staff Susie Wiles; Trump says deal is "possible"

See [[concepts/anthropic/dod-dispute]] for full analysis and [[concepts/ai-military]] for broader context.

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



## Agent Containment Architecture (May 2026)

Anthropic published a detailed engineering post on how Claude is [[concepts/security-and-governance/agent-containment|contained]] across its three products. The article shares what's held up, what's broken, and lessons learned about agent security.

### Three Products, Three Isolation Patterns

| Product | Pattern | Infrastructure | Blast Radius |
|---------|---------|---------------|-------------|
| claude.ai (code exec) | Ephemeral container | gVisor on isolated infra | Server-side only, per-session ephemeral |
| Claude Code | HITL sandbox | Seatbelt (macOS) / bubblewrap (Linux) | Local workspace, network denied by default |
| Claude Cowork | Sealed local VM | Apple Virtualization / HCS | Mounted workspace only, host keychain isolated |

### Key Security Incidents Documented

- **Egress via approved domain**: Malicious file instructed Claude to upload data via api.anthropic.com using an attacker's API key. The egress proxy correctly allowed the domain but failed to verify the API key's provenance. Fixed with a defensive MITM proxy.
- **Pre-trust execution**: `.claude/settings.json` hooks in cloned repos executed before the trust dialog. Fixed by deferring config parsing until after trust acceptance.
- **User-as-injection-vector**: Internal red-team phish succeeded 24/25 times — the only defense was the environment layer (egress controls, filesystem boundaries).
- **Approval fatigue**: Users approved ~93% of permission prompts. Claude Code's auto mode + sandbox reduced prompts by 84%.

### Principles
1. **Design for containment at the environment layer first** — probabilistic model defenses will never be 100%
2. **Match isolation strength to user expertise** — developers who read bash ≠ knowledge workers who can't
3. **Be wary of custom components** — gVisor, seccomp, hypervisors held; custom proxy failed

Source: [How we contain Claude across products](raw/articles/2026-05-27_anthropic-engineering_how-we-contain-claude.md) (Anthropic Engineering, May 2026)


## Research Focus

Anthropic's research priorities:
- AI safety and alignment
- Constitutional AI
- Scalable oversight
- Interpretability

## Code w/ Claude 2026 — Product Launches (May 2026)

At the Code w/ Claude 2026 event, Anthropic announced multiple new products and features:

### Microsoft 365 GA

Significant progress on Claude's Microsoft 365 integration:

- **Excel, PowerPoint, Word**: General Availability (GA) launched
- **Outlook**: Public beta released
- Claude maintains conversational context across Microsoft apps

### Dreaming — Managed Agents Research Preview

The "Dreaming" feature launched as a research preview. Running on the Managed Agents platform, the following moved to public beta:

- **Outcomes**: Agent deliverable management
- **Multi-agent orchestration**: Coordinated execution of multiple agents
- **Webhooks**: External service integration

### Financial Services Templates

Providing production-grade agent templates for financial services — available as Cowork / Claude Code plugins or run as Managed Agents:

- Investment pitch creation
- Valuation review
- Month-end closing processing

### Funding and Valuation

Financial Times reporting (May 2026):

- Negotiating a **funding round of up to $50B**
- Targeting a **~$1T valuation** — surpassing OpenAI's $852B
- Funds to be deployed almost entirely toward **compute expansion** (supply constraints are impacting customer service)

### Compute Partnership Overview

Anthropic has secured multiple large-scale compute agreements:

| Partner | Scale | Status |
|-----------|------|------|
| **SpaceXAI (Colossus 1)** | 300MW / 220K+ GPU; $1.25B/month | Effective May 2026 |
| **Amazon** | Up to 5GW (~1GW new by end of 2026) | Contract signed |
| **Google + Broadcom** | 5GW | Expected operational 2027 |
| **Microsoft + NVIDIA** | $30B Azure capacity | Strategic partnership |
| **Fluidstack** | $50B US AI infrastructure investment | Announced |

Claude is trained and run across **AWS Trainium, Google TPU, and NVIDIA GPU** hardware.

**SpaceX S-1 Filing Details (May 2026)**: SpaceX's S-1 registration statement reveals the full terms of the Cloud Services Agreement with Anthropic: $1.25 billion per month through May 2029, with capacity ramping in May and June 2026 at a reduced fee. The agreements may be terminated by either party upon 90 days' notice. Notably, SpaceX also uses this compute capacity for its own AI applications (including Grok 5, training at COLOSSUS II), positioning Anthropic as both a customer and a revenue source for SpaceX's growing AI compute business.

Source: [Simon Willison quoting SpaceX S-1](raw/articles/simonwillison.net--2026-may-20-spacex-s1--48fe0f3d.md)

### Profitability Debate: The Reality Behind "Profitability" (May 2026)

On May 21, 2026, the Wall Street Journal reported on Anthropic's "first profitable quarter":

- Q1 2026 Revenue: **$4.8B** → Q2 2026 Revenue Forecast: **$10.9B**
- Q2 2026 Operating Profit: **$559M** (EBITDA basis)
- Wall Street Journal's own footnote: "Accounting standards are unclear as the company is private"

However, detailed analysis by Ed Zitron ([[entities/ed-zitron]]) revealed that this "profitability" is essentially an **accounting construct**:

#### SpaceX Discount Structure

The truth about the Colossus contract revealed in SpaceX's S-1 filing:
- Standard rate: $1.25B/month (= $15B/year)
- **May-June 2026 has discounted "ramp-up period" pricing** — meaning it **precisely coincides** with the quarter being touted as profitable
- Rates return to standard from July onward, reverting to non-profitable on an annual basis

#### ARR / Revenue Data Inconsistencies

Discrepancies among Anthropic's publicly stated ARR figures:

| Date | Claim | Monthly Equivalent |
|------|------|--------|
| 2026/02/12 | ARR $14B | ~$1.17B/month |
| 2026/03/03 | ARR $19B (Dario Amodei) | ~$1.58B/month |
| 2026/03/09 | Cumulative revenue "over $5B" (CFO Krishna Rao, sworn testimony) | — |
| 2026/04/06 | ARR $30B | ~$2.5B/month |
| Q1 2026 | WSJ report: $4.8B | — |

The CFO's sworn testimony of "over $5B" cumulative and WSJ's standalone Q1 figure of $4.8B represent a serious contradiction. It is unlikely that Rao understated the business by 30-40% to a court.

#### Total Cost Estimate

Why the "profitability" is unsustainable:
- SpaceX: $1.25B/month × 12 = $15B/year
- AWS/Google Cloud assumed at similar or larger scale → $1.25B/month each
- Quarterly compute cost: ~$11.25B
- Annual compute cost: ~$45B
- Additionally, inference costs were 23% above projections as of January 2026 (The Information reporting)

#### Potential Revenue Inflation Methods

Techniques identified by Zitron:
- Token prepayments from large enterprises (lump-sum recognition of $50M for 12 months)
- Upfront recognition of Claude additional credit purchases (10-30% discount)
- Front-loading annual contract revenue
- Intentional suppression of training load to free up inference capacity

#### Analyst Assessment

Zitron's conclusion:
> "I'm not saying it's accounting fraud, but it is shiatsu-grade massaging of numbers. Anthropic deliberately selected a specific quarter they knew they could suppress costs, leaked the 'profitability' story, gave journalists an escape hatch by noting 'costs may increase,' and timed the release to coincide with NVIDIA's earnings day."

As a direct appeal to "AI bubble skeptics," he argues that **those who genuinely want Anthropic to succeed should be skeptical of these numbers**. He draws parallels to WeWork's claim of profitability "from month two."

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

## Applied AI / FDE Service Strategy (May 2026)

### FDE (Forward Deployed Engineer) Hiring

Anthropic's FDE job postings specify the following responsibilities:

- **Deep integration into customer systems**: Enter customer production environments directly, building production applications using Claude, MCP servers, sub-agents, and Agent Skills
- **Extract reusable patterns**: "Identify and systematize repeatable deployment patterns, feeding them back to Product/Engineering teams" as a core responsibility

This shows that Anthropic shares the same **FDE → Product feedback loop** philosophy that OpenAI employs.

### Enterprise AI Services Joint Venture

In partnership with Blackstone, Hellman & Friedman, and Goldman Sachs, establishing an enterprise AI services company for mid-market organizations:

- Supporting Claude integration into mission-critical operations
- Accumulating industry-specific deployment patterns

### Strategic Implications

Anthropic is undergoing the same structural transformation as OpenAI (DeployCo) — **evolving from an API/model provider to a deployment service provider**. The FDE model is becoming an industry standard across frontier labs.


## Financials

### Revenue Growth
Anthropic has shared run-rate revenue in funding announcements. The specific calculation methodology (Reuters Breakingviews, Karen Kwok, citing "a person familiar with the matter"):
- **Consumption-based**: last 28 days of sales × 13
- **Subscription-based**: monthly revenue × 12
- Combined = total run-rate

This 13× multiplier on consumption means short-term usage spikes get annualized into headline numbers — an important caveat when comparing to standard ARR. See [[concepts/ai-economics]] for the "tokenmaxxing" sustainability debate.

| Date | Run-Rate Revenue | Context |
|------|-----------------|---------|
| Early 2026 | $30B | Axios CEO Jim VandeHei: "can't find any company in any industry, in any era that has scaled organic revenue this quickly" |
| May 2026 | $47B | Announced alongside $65B Series H |

### Series H — Full Details ($65B, May 2026)
- **Valuation**: $965B (exceeding OpenAI's valuation)
- **Raised**: $65B
- **Lead investors**: Altimeter (largest investor), Dragoneer, Greenoaks, Sequoia
- **Run-rate revenue**: $47B (up from $9B in December 2025)
- **Revenue growth**: 5× in 5 months

### Series H — Expanded Detail
The Series H round included a broader consortium beyond the four lead investors:

- **New co-lead investors**: Capital Group, Coatue, D1 Capital Partners, GIC, ICONIQ, XN
- **Significant investors**: AMP PBC, Baillie Gifford, Blackstone, Brookfield, D.E. Shaw Ventures, DST Global, Fidelity, General Catalyst, Insight Partners, Jane Street, Lightspeed, MGX, NTTVC, NX1 Capital, Situational Awareness LP, T. Rowe Price, Temasek
- **$15B of previously committed investments from hyperscalers**, including $5B from Amazon
- **Strategic infrastructure partners**: Micron, Samsung, SK hynix — memory and semiconductor partners for compute supply chain

Compute commitments from infrastructure partners:
| Partner | Capacity |
|---------|----------|
| **Amazon** | Up to 5GW of new compute capacity |
| **Google / Broadcom** | 5GW of next-generation TPU capacity |
| **SpaceX** | Access to GPU capacity in Colossus 1 and Colossus 2 |

Claude is the first frontier model available on all three major clouds: AWS, Google Cloud, and Azure. Funding is intended to advance safety and interpretability research, expand compute infrastructure, and scale product offerings.

### Mythos-Class Model Plans
Anthropic's **Mythos-class** model is described as a "new class of model" more capable than Opus. The company is adopting a **stepped-release strategy**:
1. **Opus 4.8** released as a commercially safe model — the most honest Claude model to date
2. **Mythos-class** reserved until stronger safety controls can be implemented for its advanced capabilities
3. This mirrors the earlier decision to withhold the original Mythos model — Anthropic explicitly states it will not release models with dangerous capabilities until control measures are adequate

The strategy positions Anthropic as the most safety-conscious among frontier labs, using multiple capability tiers (Haiku → Sonnet → Opus → Mythos) to manage risk.

- Largest single funding round for an AI company
- Run-rate revenue crossed $47B earlier that month
- Revenue trajectory debated: Ed Zitron expressed skepticism; Simon Willison notes these numbers appear in fundraising announcements, making them subject to securities fraud liability if fabricated

### IPO Preparation (June 2026)

Anthropic took a formal step toward going public in June 2026:

- **Filed a confidential draft S-1 registration statement** with the U.S. Securities and Exchange Commission (SEC)
- This is a formal step toward an **Initial Public Offering (IPO)**
- Follows Anthropic's **Series H** ($65B raised at $965B valuation)
- Source: [Anthropic Blog — Confidential Draft S-1](https://www.anthropic.com/news/confidential-draft-s1-sec)

### Revenue Drivers
- Enterprise adoption of Claude models
- "Tokenmaxxing" phenomenon: companies encouraging employees to maximize AI usage without ROI measurement
- Anecdotal report (Axios, May 2026): one company spent $500M in a single month after failing to set usage limits on Claude licenses
- Emerging concern: tokenmaxxing may be unsustainable; some enterprises starting to question ROI (see [[concepts/ai-economics]])


## Models

Primary model family: [[Claude models]]

| Model | Release | Key Features |
|-------|---------|-------------|
| Claude Opus 4.5 | Early 2026 | High-capability reasoning |
| Claude Opus 4.6 | Mid 2026 | Fast mode $30/$150 per MTok |
| Claude Opus 4.7 | Mid 2026 | 1M context, 128K output |
| Claude Opus 4.8 | May 28, 2026 | Honesty improvements, mid-conversation system messages, lower prompt cache minimum (1,024 tokens). Benchmarks: SWE-Bench Pro 69.2% (+10pts vs GPT-5.5), FrontierSWE #1, APEX-SWE 45.3% Pass@1, GDPval-AA 1890 Elo, AA Intelligence Index 61.4 |

### Claude Opus Pricing (4.8)
- Standard: $5/M input, $25/M output tokens
- Fast mode: $10/M input, $50/M output (significant reduction from 4.6/4.7's $30/$150; research preview only)


## Safety & Honesty

Claude Opus 4.8 introduced notable honesty improvements:
- 4× less likely than predecessor to allow code flaws to pass unremarked
- Lowest incorrect-rate on all benchmarks among 6 tested models
- Achieves this mainly through abstention rather than higher correct-answer rate
- System card shows measurable reduction in factual hallucination

Training philosophy: train models to avoid unsupported claims and flag uncertainty.


## Technical Features (Opus 4.8)



## Opus 4.8 Benchmark Results

| Benchmark | Opus 4.8 | Comparison |
|-----------|----------|------------|
| SWE-Bench Pro | 69.2% | +10pts vs GPT-5.5 |
| FrontierSWE | #1 | Top-ranked |
| APEX-SWE Pass@1 | 45.3% | GPT-5.3 Codex: 41.5% |
| GDPval-AA Elo | 1890 | +137 vs Opus 4.7 |
| AA Intelligence Index | 61.4 | +4.1 vs Opus 4.7 |
| Efficiency | 15% fewer turns, 35% less output tokens per task | vs Opus 4.7 |

- **Mid-conversation system messages**: Accept `role: "system"` messages after user turns (subject to placement rules). Enables updated instructions without restating full system prompt, preserving prompt cache hits in agentic loops.
- **Lower prompt cache minimum**: 1,024 tokens (down from 4,096 in 4.7)
- **Context window**: 1,000,000 tokens
- **Max output**: 128,000 tokens
- **Knowledge cutoff**: January 2026


## Leadership
- **Dario Amodei** — CEO, co-founder
- **Daniela Amodei** — President, co-founder
- **Jack Clark** — Co-founder, Import AI newsletter, see [[entities/jack-clark]]
- **Andrej Karpathy** — Joined pre-training team (May 2026); previously co-founder of OpenAI, notable for choosing Anthropic over OpenAI return


## Related Pages
- [[Claude models]] — Model family details
- [[concepts/ai-economics]] — Tokenmaxxing, AI ROI debate
- [[Gary Marcus]] — AI industry skepticism
- [[OpenAI]] — Primary competitor
- [[Ed Zitron]] — Revenue skepticism
## Related
- [[entities/anthropic]] — The model family
- [[entities/claude-code]] — Claude Code CLI agent
- [[concepts/claude/mythos]] — Claude Mythos model (used by Claude Security)
- [[entities/foundation-capital]] — Partner in Claude Managed Agents
- [[entities/fable]] — Fable coding harness (links to harness engineering + cognitive UX design patterns)
- [[entities/sap-business-ai-platform]] — SAP partnership (May 2026)
- [[concepts/anthropic/managed-agents]] — Managed Agents platform details
- [[entities/project-glasswing]] — Defensive security initiative

## References

- 2026-04-12-anthropic-openclaw-subscription-ban
- 2026-04-15-property-based-testing-anthropic

- 2026-04-26-claude-code-anthropic-agentic-coding-system
- anthropic-claude-code-session-management-1m-context
