---
title: OpenAI Codex
type: entity
created: 2026-05-12
updated: 2026-07-13
tags:
  - product
  - coding-agent
  - openai
  - coding-agents
  - harness-engineering
  - ai-agents
  - data-science
  - bizops
  - human-in-the-loop
  - workflow
  - voice-ai
aliases:
  - Codex CLI
  - codex-cli
  - GPT-5.3 Codex
  - gpt-5.3-codex
  - Codex for Work
sources:
  - raw/articles/2026-01-14_openai-codex-prompting-guide.md
  - raw/articles/openai.com--academy-codex-for-work-how-data-science-teams-use-codex--afc8cde3.md
  - raw/articles/2026-05-20_jxnlco_getting-the-most-out-of-codex.md
  - https://github.com/openai/codex
  - https://www.businesstoday.in/technology/story/openai-codex-celebrates-3-million-weekly-users-ceo-sam-altman-resets-usage-limits-524717-2026-04-08
  - https://www.wsj.com/cio-journal/openai-is-working-with-consultants-to-sell-codex-f355b1b9
  - raw/newsletters/2026-05-23-ainews-all-model-labs-are-now-agent-labs.md
  - raw/articles/2026-05-26_every_codex-knowledge-work.md
  - raw/articles/2026-06-02_zswang24-codex-data-science-plugin.md
  - raw/articles/2026-06-02_openai-codex-every-role-tool-workflow.md
  - raw/newsletters/2026-06-04-build-tools-to-build-more.md
  - raw/newsletters/2026-06-21-spacex-s-cursor-call-openai-s-codex-clone-and-midjourney-s-medical-moonshot.md
  - raw/articles/2026-06-23_gengdaj-codex-production-agent-workflow.md
  - raw/articles/2026-06-25_openai-agents-transforming-work.md
  - raw/papers/2026-06-25_openai-shift-to-agentic-ai.md
  - raw/articles/2026-07-11_theo_gpt-5-6-sol-without-hitting-limits.md
  - raw/newsletters/2026-07-14-ainews-codex-usage-up-10x-in-6-months-to-7m-users-1m-in-the-past-day-did-codex-o.md
---

# OpenAI Codex

OpenAI's AI coding agent. Available as a fully open-source CLI-based agent ([GitHub](https://github.com/openai/codex)), with custom integration possible via API. Model: `gpt-5.3-codex`.

Autonomously handles code generation, editing, codebase exploration, testing, and deployment. Compaction (conversation compression) enables hours of autonomous execution.

## Basic Information

| Item | Details |
|------|---------|
| Developer | OpenAI |
| Model | gpt-5.3-codex |
| Distribution | CLI (OSS) + SDK + API |
| Features | Autonomous execution, compaction, Windows/PowerShell support |
| Reasoning effort | medium (recommended) / high / xhigh |

## Key Features

- **Long-duration autonomous execution**: Hours of autonomous task execution. High/xhigh reasoning effort handles hardest tasks.
- **First-class compaction**: Compresses conversation history to circumvent context limits. No need to restart chat even in long sessions.
- **Windows/PowerShell support**: Significantly improved operation in PowerShell environments.
- **Speed and token efficiency**: Reduced thinking tokens, with medium reasoning effort achieving an optimal balance for interactive coding.

## Architecture Features

- **apply_patch tool**: Fuzzy match-based file editing. Uses surrounding context for matching rather than strict string replacement.
- **Background terminal execution**: Runs long builds/tests in background and notifies on completion.
- **Parallel tool execution**: Independent tool calls run in parallel.

## Codex as a Knowledge Work Platform (May 2026)

> *Source: [[raw/articles/2026-05-26_every_codex-knowledge-work.md|Codex for Knowledge Work]] — Katie Parrott, Every (May 26, 2026)*

While Codex originated as a coding agent, Every's guide positions it as a **general-purpose knowledge work platform** — a workspace for you and your AI agents that handles email, Slack, Google Drive, Notion, PostHog, and beyond.

### The Knowledge Work Vision

> "Picture a Monday morning: A request for a launch plan lands in your inbox. You forward it to Codex, which has its own email account, and close your laptop while Codex runs tasks in the cloud... By the time you reach your desk, a draft is waiting for review."

Codex becomes an autonomous executive assistant: reading Slack threads, pulling customer notes from Google Drive, checking analytics in PostHog, and drafting plans in Notion — requiring only occasional human approval via a thumbs-up on mobile.

### Delegate vs. Collaborate: The Meta-Skill

The Every guide frames Codex usage around two fundamental modes:

| Mode | When to Use | How It Works |
|------|-------------|--------------|
| **Delegate** | Predictable, repeatable, low-risk tasks with clear instructions | Agent runs autonomously and brings back finished work for review |
| **Collaborate** | Judgment-heavy, exploratory, or iterative work | You work alongside the model toward your vision, steering as it goes |

> "Expert Codex users know how to direct AI's capability without losing their personal judgment. They *ride* the models rather than being overwhelmed by them."

**Choosing between the two modes is described as the meta-skill of modern knowledge work.** This mirrors the broader [[concepts/harness-engineering/agentic-loop|agentic autonomy spectrum]] — the tradeoff between full automation and human-in-the-loop collaboration.

### Goals vs. Skills

The Every article provides a crisp distinction that complements [[concepts/codex/codex-goal|Codex /goal]]:

| Concept | Definition | Scope |
|---------|-----------|-------|
| **Goal** (`/goal`) | A persistent objective that shapes an entire session | One stretch of work; ends when the objective is met |
| **Skill** | A reusable set of packaged instructions (sometimes with scripts) | Recurring task type; teaches Codex how to handle a workflow |

**Heuristic for when to use `/goal`:** "If you'd type the same sentence into three prompts in a row — 'cite every factual claim, match the house style, never send without my review' — make it a goal instead."

### Five Levels of Codex Use (Structure)

The full guide (behind Every paywall) outlines five progressive levels:
1. One-off knowledge work
2. Repeatable task automation
3. Persistent workflows and goals
4. Compounding a personal system
5. Team-wide agent orchestration

Plus 13 workflow templates (inbox zero, research brief, GTM plan, KPI report, etc.) and a seven-day power-user onboarding plan.

## Codex for Work — Team Use Cases (May 2026)

In May 2026, OpenAI published "Codex for Work" documentation covering team-specific use cases. A guide applying Codex to workflows for data science, business operations, and sales teams — not just engineers.

### For Data Science Teams

Data science artifacts are not "queries" but **artifacts that someone can read, verify, and act on**. Codex generates **reviewable first drafts** from dashboards, metric definitions, exports, experiment logs, and business context.

| Use Case | Input | Output |
|----------|-------|--------|
| **KPI root cause analysis** | Metric definitions, dashboards, segment data, business context | Root cause analysis brief (separating confirmed factors from hypotheses), charts, recommended actions |
| **Business impact report** | Experiment plan, success metrics, cohort data, customer signals | Lift analysis, guardrail checks, report with scale/change/discontinue decisions |
| **Analysis request agent** | Vague stakeholder requests, available data | Scoped analysis plan, initial analysis, stakeholder-facing answers |
| **Executive KPI memo** | Latest KPIs, past reviews, owner notes, planning context | Memo with key changes, anomalies, risks, and owner follow-ups |
| **Dashboard building and monitoring** | Workflows, strategies, metrics, source data | Dashboard specification or initial plan |

**Workflow pattern**: Codex generates first draft → Human verifies, stress-tests caveats, refines recommendations. Codex **clearly separates confirmed facts from hypotheses**, and explicitly flags data quality issues and assumptions.

**Supported plugins**: Google Drive, Spreadsheets, Slack, Gmail, Documents, Presentations

### Data Science Plugin Launch (June 2026)

On June 2, 2026, OpenAI officially launched **six new role-specific plugins for Codex**, announced via [@OpenAI](https://x.com/OpenAI/status/2061887715520721151) and amplified by [[entities/zhanshi-wang]] (OpenAI researcher). Each plugin bundles relevant apps, skills, instructions, and workflows. Together: **62 popular apps and 110 skills**.

#### The Six Plugins

| Plugin | Target Role | Key Capabilities | Integrations |
|--------|-------------|-------------------|--------------|
| **Data Analytics** | Analysts, business teams | Explore data, explain metric changes, create reports/dashboards | Snowflake, Databricks Genie, Hex, Tableau |
| **Creative Production** | Marketing, creative teams | Campaign boards, display ad variations, product lifestyle shots | — |
| **Product Design** | Design teams | Wireframes → interactive mockups, calculators, estimators | — |
| **Sales** | Sales teams | Account research, meeting prep, outreach drafts, CRM management | — |
| **Public Equity** | Investors | Peer comparison, earnings analysis, investment theses | Filings, models, research |
| **Investment Banking** | Bankers | Pitch materials, comps analysis, diligence → recommendations | — |

**Source**: [role-based-plugins](https://github.com/openai/role-based-plugins) — open-source repo for all plugins.

**Coming soon**: Corporate Finance, Private Equity Investing, Marketing Strategy, Strategy Consulting, Legal. Open ecosystem goal: partners create and deploy their own plugins in Codex and ChatGPT.

**Data Analytics plugin user feedback** (via [[entities/zhanshi-wang]]):
- 100% of users said it speeds up the path from raw data to insight
- 100% said it helps them take on more work than they otherwise could
- Described as a **"force multiplier"** — accelerating 0→80% progress, enabling parallel multi-project work, improving final output quality

#### Sites (Preview)

A new canvas type for Codex — interactive, hosted websites and apps shared via URL within workspaces. Codex can create dashboards, planners, review workspaces, project boards, galleries, and lightweight tools. Rolling out in preview for Business and Enterprise.

**Early partners**: Vercel, Wix, Base44, Replit, Lovable, Figma, Webflow, Emergent.

#### Annotations

Point-to-refine interaction model extended from code to documents, spreadsheets, slides, and sites. Select a specific part (chart, claim, UI element) and describe the change — Codex focuses the update on that part only.

**Significance**: This is Codex's most comprehensive platform expansion — moving from coding agent to **general-purpose knowledge work platform** with domain-specific plugins. Aligns with [[concepts/codex/codex-superapp]] trajectory and [[concepts/model-labs-to-agent-labs]] thesis.

### For Business Operations Teams

Automate operational workflows including report generation, data reconciliation, meeting preparation, and process documentation.

### For Sales Teams

Account research, proposal creation, CRM data analysis, competitive intelligence briefings.

### Codex Thursday No. 6 — Appshots, /goal improvements, annotation mode (May 2026)

OpenAI's sixth weekly Codex Thursday release introduced:

| Feature | Description |
|---------|-------------|
| **Appshots** | Interactive app previews within Codex — see rendered UI without leaving the CLI |
| **/goal improvements** | Better specification understanding for complex multi-step goals |
| **Remote computer use** | Codex can control remote computers (including while locked/away) |
| **Annotation mode** | Markup on rendered output — draw on web pages, highlight UI elements, annotate screenshots |
| **Plugin sharing** | Share custom plugins with team members |
| **Analytics dashboard** | Usage monitoring, task completion tracking, bottleneck identification |

**User reports**: Practitioners report abandoning traditional IDEs entirely for Codex, with the annotation mode and Appshots filling the last gaps that required visual verification in a browser.

**Context**: Thursday No.6 continues the rapid weekly cadence that demonstrates OpenAI's commitment to agent platform iteration — consistent with the [[concepts/model-labs-to-agent-labs]] thesis.

**See also**: [[concepts/model-labs-to-agent-labs]] — Model Labs to Agent Labs industry thesis.

## Codex App: Human-in-the-Loop Capabilities (May 2026)

Based on Jason Liu's ([@jxnlco](https://x.com/jxnlco), Codex team DX engineer) comprehensive guide — the app capabilities supporting Codex's evolution from a coding agent to a **"general-purpose computer work system."**

### Control Model

| Feature | Description | Use Case |
|---------|-------------|----------|
| **Steering** | Interrupt a running task and give correction instructions before the current step completes | "Make this element smaller," "This copy is wrong" |
| **Queuing** | Add the next task without interrupting the current one | "When done, send the preview link to the reviewer on Slack" |
| **Voice input** | Input rough thoughts or meeting notes directly, before refinement | "I think someone mentioned Ben on Slack. Forgot the details. Look it up." |

Steering changes the "now," Queuing changes the "next." Both keep the user close to the work as it unfolds.

### Reach Layer (Tool Hierarchy)

```
$browser (side-panel browser: verification, annotation)
  ↓
@chrome (workflows requiring signed-in Chrome state)
  ↓
@computer (work accessible only via desktop GUI)
```

- **$browser**: Web surface review and annotation in side panel
- **@chrome**: Workflows dependent on user's Chrome context
- **@computer**: Operations only possible via desktop GUI
- **MCP servers + connectors**: Slack, Gmail, Calendar — tasks appear as messages or inbox items before becoming code
- **Skills**: Save proven workflows as reusable packages

### Long-Running Execution and Autonomy

| Feature | Description |
|---------|-------------|
| **Durable threads** | Persistent threads maintaining context across sessions. Instant jump to pinned threads via Command-1~9. For steady workflows: Chief of Staff, release, document review |
| **Thread automations** | Heartbeat-style periodic wake-ups returning to the same thread on schedule. Check Slack/Gmail for unreplied messages every 30 min → prioritize → draft (without sending) |
| **Goals** | Long-term tasks with verifiable finish lines. Use test suites, benchmarks, and E2E workflows as verifiers. "Ambition is important, but without verification it's just wishful thinking" |

### Side Panel (Artifact Review)

Keeps artifacts next to the conversation. Review not just code but decks, PDFs, browser pages, and tables in-place. Particularly effective for these four roles:

1. **Artifact inspection** — Markdown, spreadsheets, documents, slides in-place
2. **Annotation of changes** — Direct markup on areas needing changes
3. **Web surface operation** — Codex inspects, controls, and annotates rendered pages
4. **Change review** — Refine artifacts without context switching

Most effective surfaces: `index.html` (lightweight static artifacts), Storybook (UI review), Remotion Studio (programmatic animation), browser-based slide decks, data analysis apps.

### Shared Memory

Long-lived threads become even more useful by sharing memory across conversations. Jason Liu's recommended durability patterns:

- **Obsidian vault**: Plain-file-based persistent context. Structure: `TODO.md`, `people/`, `projects/`, `agent/`, `notes/`
- **AGENTS.md**: Top-level definition of what, when, and how Codex should save
- **Codex Memories** (Settings > Personalization > Memories): Local recall layer for preferences, steady workflows, known pitfalls
- **Chronicle**: Codex builds memory from recent screen context

> "Important context should not exist only inside conversation transcripts. Write it down somewhere the next thread can pick it up."

### Mobile (Work from Anywhere)

The Codex mobile app allows continuing tasks started on Mac from a smartphone while away. The local environment (files, permissions, setup) remains on the Mac — the user approves next steps and redirects on the go.

### Codex Mobile (May 2026)

Codex expanded to the **ChatGPT mobile app** in preview:

| Feature | Detail |
|---------|--------|
| **Platform** | ChatGPT mobile app (iOS/Android) |
| **Functionality** | Start, steer, and review Codex tasks from phone |
| **Status** | Preview |
| **Significance** | Expands Codex beyond desktop to mobile form factor for task management on the go |

**Use case**: Start a complex coding task on desktop, then monitor progress, approve steps, or redirect the agent from your phone while commuting. The local environment (files, permissions, setup) remains on the desktop — the mobile app provides remote control and oversight.

Source: Jason Liu X article (May 2026), Aakash's Clicky newsletter

## Codex Record & Replay (June 2026)

OpenAI added Record & Replay to Codex, a macOS feature that watches you complete a task once and turns that demonstration into a reusable skill.

| Feature | Detail |
|---------|--------|
| **How it works** | Enables Computer Use on your Mac, performs a task once while Codex records the demonstration |
| **Output** | Editable skill definition: when to use it, what inputs it needs, steps to follow, how to verify the result |
| **Editing** | The drafted skill is readable and editable before deployment |
| **Use cases** | Stable, repetitive jobs like filing expenses, pulling weekly reports, data entry workflows |

**Integration with ChatGPT**: The same release rebuilt ChatGPT's scheduled tasks with a dedicated page for recurring and monitoring jobs. Monitoring tasks watch the web or connected apps and notify you only when something changes — enabling a 'set and forget' pattern for AI-powered oversight.

**Significance**: Record & Replay bridges the gap between 'fun toy' agentic computer use and production-ready workflow automation. By creating editable, reusable skills from demonstrations, it transforms agentic AI from an experimental tool into a deployable process.

**Related**: [[concepts/codex/codex-skill]] — Codex Skills system, [[concepts/agentic-engineering/agentic-engineering]] — Developer workflow patterns

## Agent Development Methodology — Production Agent Workflow (June 2026)

> *Source: [[raw/articles/2026-06-23_gengdaj-codex-production-agent-workflow.md|@gengdaJ (Yichen) — June 23, 2026 Note Tweet]]*

Chinese AI entrepreneur Yichen ([@gengdaJ](https://x.com/gengdaJ), 34K followers) documented a structured methodology for taking an Agent from concept to production deployment using Codex. After building multiple AI products with Codex and Claude Code, he formalized a repeatable development cycle while building "Shu Jing" (Book Mirror) Agent:

### The Five-Phase Development Cycle

1. **Product Alignment (Q&A → PRD)**: Use conversational Q&A with Codex to align on product vision, then generate a Product Requirements Document
2. **Decomposition (PRD → Plan.md)**: Break the PRD into multiple focused `Plan.md` files — each representing a development increment
3. **Goal Authoring (Skill-based /goal prompts)**: Use open-source Skills (referencing Qiaomu's open-source Skill library) to craft `/goal` prompts that encode clear completion criteria
4. **Target Mode Execution**: Set Codex to "goal" mode, send the prompts, and let the agent autonomously execute
5. **Consolidation & Iteration**: After completing one development round, merge all `Plan.md` files into a single `consolidation.md` to capture the current state, then repeat the cycle for the next round

### Deployment with Tencent EdgeOne Makers

For production deployment, he chose **Tencent Cloud EdgeOne Makers** — an edge Web + AI Agent hosting platform — for three reasons:

- **Built-in Agent infrastructure templates**: Memory systems, sandbox tools, call chain tracing (observability), and model gateway are all available out-of-the-box. Code can be adapted with minor Codex edits for rapid deployment
- **Unified frontend + backend architecture**: Traditional split frontend/backend causes CORS issues; EdgeOne unifies the project, simplifying account management, deployment, monitoring, and domain management
- **Framework/language/model agnostic**: Supports Claude, OpenAI, LangGraph, CrewAI frameworks; no proprietary SDK lock-in; allows JS or Python; provides a unified AI Gateway while supporting third-party APIs

**Key insight**: The methodology emphasizes **iterative consolidation** — each cycle produces a `consolidation.md` that serves as both documentation and context for the next development round. This creates a self-documenting, progressively richer knowledge base that future Codex sessions can reference.

## Prompt Design Characteristics

See [[concepts/codex/codex-prompting]]. Key characteristics:

- **No explicit plan output**: The model plans internally; writing plans out causes early stopping
- **No-confirmation autonomy**: Does not wait for user confirmation unless unable to resolve an error
- **Concise communication**: Removes preamble and status updates, prioritizes action
- **Metaprompting**: Have the model analyze past conversations and generate system prompt improvements

## GPT-5.6-Sol Operational Guidance (July 2026)

> *Source: [[raw/articles/2026-07-11_theo_gpt-5-6-sol-without-hitting-limits.md|Theo Browne — "gpt-5.6-sol without hitting limits"]] (July 11, 2026)*

Theo Browne ([@theo](https://x.com/theo), creator of create-t3-app), after burning $200K+ of tokens on GPT-5.6-Sol, published operational guidance for maximizing the $200 Codex Pro subscription:

### Reasoning Level Selection

| Level | Recommendation | Notes |
|-------|---------------|-------|
| **medium** | Default | Good balance for most tasks |
| **high** | Recommended for $200 tier | Handles subagents reasonably well |
| **xhigh** | Rarely needed | Very capable but not necessary even for multi-subagent orchestration |
| **Ultra** | ⚠️ Avoid | Not a reasoning level — positioned incorrectly in UI. Bugs in Codex harness cause excessive subagent spawning at max reasoning. Causing confusion similar to Claude Code's "Ultracode" |

### Fast Mode Warning

Fast mode uses a **2.5x credit multiplier**. With GPT-5.6's dramatically extended autonomous runs (compared to GPT-5.5), a single message can consume 15% of a 5-hour window without fast mode — or **40% with fast mode**. Recommendation: avoid fast mode until Codex team resolves usage predictability.

### Subagent Management

GPT-5.6-Sol's strongest unlock, but with significant footguns:

- **Always spawns subagents with same model and reasoning level as parent** — the core driver of Ultra's brokenness
- **Mitigations:**
  1. Lower reasoning level (High handles subagents reasonably; Low/Medium work well)
  2. Set global AGENTS.md directive: "only spawn subagents when I ask you to"
  3. Advanced: enable `hide_spawn_agent_metadata = false` flag in Codex config for multi-tier subagent visibility
- **Orchestrator pattern**: Use Fable agent (another $200 subscription) to drive Codex subagents — Fable with lower reasoning + skills for Codex subagent spawning is highly effective

### Model Selection

| Model | Recommendation | Use Case |
|-------|---------------|----------|
| **GPT-5.6-Sol** | Primary ($200 tier: high; lower tier: low) | Vast majority of work |
| **Terra** | Occasional only | Quick review, feedback; medium reasoning for maximizing usage |
| **Luna** | Not meant for direct selection | Code tool; best spun up as subagent by Sol |

### Prompt Engineering: Clear Stop Points

GPT-5.6 runs much longer than GPT-5.5 — it benefits from explicit stop boundaries:

```
"I want you to build this new feature. Start by writing a plan. When you've finished the plan, stop and ask for feedback before proceeding"

"The plan looks great! Let's build it out. Use computer use to test your implementation. Keep going until the code works and you're happy with the implementation. Put up a PR, babysit it for the first set of review comments, and address them. Stop after the first set of review comments, I'll handle it from there."
```

### Recommended Tools for Usage Monitoring

- Official Codex usage dashboards
- `ccusage` — community CLI tool
- `codexbar` — macOS menu bar utility

### Experimentation Philosophy

"Spend more time in the `~/.codex` and `~/.claude` directories. Make changes that feel stupid. Experiment. You'll be amazed what can happen."

## Growth Metrics

| Date | WAU | Source |
|------|-----|--------|
| Mid-March 2026 | 2M | Thibault Sottiaux (Codex lead) |
| April 8, 2026 | **3M** | Announced by Sam Altman. Codex lead Thibault Sottiaux confirmed "from 2M less than a month ago" |
| April 22, 2026 | **4M** | WSJ reporting. +1M in 2 weeks |
| July 13, 2026 | **7M** | Thibault Sottiaux (Codex lead). +1M in the previous ~24 hours from 6M on July 12 |

On April 8, 2026, Sam Altman announced Codex surpassed 3M weekly active users and reset usage limits. He stated plans to repeat resets at each 1M increment until reaching 10M users. Codex lead Thibault Sottiaux confirmed the rapid growth was "from 2M less than a month ago."

Post-GPT-5.5 launch (April 2026), Codex's momentum accelerated. On April 22, WSJ reported 4M WAU — a net gain of 1M in 2 weeks. OpenAI partnered with Accenture, Capgemini, and PwC to formalize enterprise Codex sales.

Sources: [Business Today — Codex 3M WAU](https://www.businesstoday.in/technology/story/openai-codex-celebrates-3-million-weekly-users-ceo-sam-altman-resets-usage-limits-524717-2026-04-08), [WSJ — OpenAI Working With Consultants to Sell Codex](https://www.wsj.com/cio-journal/openai-is-working-with-consultants-to-sell-codex-f355b1b9), [Gradually AI — Codex Statistics 2026](https://www.gradually.ai/en/codex-statistics/)

On July 13, 2026, Codex lead Thibault Sottiaux announced Codex had surpassed 7M weekly active users — a 10x increase from 550K-700K in January 2026. The user base grew by approximately 1M users in the 24 hours between July 12 (6M) and July 13 (7M). This compares to Claude Code's ~2M users at $2.5B ARR as of February 2026.

Sources: [AINews — Codex 7M Users](https://open.substack.com/pub/swyx/p/ainews-codex-usage-up-10x-in-6-months)

## Competitive Comparison

| Item | Codex | [[entities/claude-code]] | [[entities/cursor]] |
|------|-------|--------------------------|---------------------|
| Model | gpt-5.3-codex | Opus 4.7 / Sonnet 4.6 | Multi-model |
| OSS | ✅ Fully OSS | ❌ Proprietary | ❌ |
| Autonomy | High (hours) | High (Auto Mode) | Medium |
| Compaction | ✅ First-class | — | — |
| Record & Replay | ✅ macOS demonstration → skill | — | — |

### Cost-per-Task Competition (July 2026)

The coding agent competitive landscape shifted from token pricing to cost-per-task metrics. The skirano coding-agent index explorer emerged for cross-agent cost comparison. Notable developments:

- Terra Max matches or exceeds Fable 5 Max in score at significantly lower cost
- Devin Fusion adopted Fable 5, achieving lower cost-per-task than Opus 4.8 through improvements in delegation and judgment
- Arena ranked GPT-5.6 Sol #2 on agent leaderboard (7.8K real-world sessions)
- Grok-4.5 jumped to #13
- Artificial Analysis highlighted cost-per-task as the key emerging metric

## Related Topics

- [[concepts/agentic-knowledge-work]] — Agentic Knowledge Work — paradigm shift from chatbot to agent-centric work (OpenAI internal adoption data)
- [[entities/jason-liu]] — Jason Liu (Codex team DX engineer, author of this guide)
- [[concepts/codex/codex-prompting]] — Codex prompt design patterns
- [[concepts/codex/codex-goal]] — Codex Goals design and operation
- [[concepts/harness-engineering/agent-harness]] — Agent harness design
- [[concepts/metaprompting]] — Metaprompting (self-improving prompts)
- [[entities/openai]] — OpenAI
- [[concepts/coding-agents/coding-agents]] — Coding agents general
