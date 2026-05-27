---
title: OpenAI Codex
type: entity
created: 2026-05-12
updated: 2026-05-27
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

**Choosing between the two modes is described as the meta-skill of modern knowledge work.** This mirrors the broader [[concepts/agentic-loop|agentic autonomy spectrum]] — the tradeoff between full automation and human-in-the-loop collaboration.

### Goals vs. Skills

The Every article provides a crisp distinction that complements [[concepts/codex-goal|Codex /goal]]:

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

## Prompt Design Characteristics

See [[concepts/codex-prompting]]. Key characteristics:

- **No explicit plan output**: The model plans internally; writing plans out causes early stopping
- **No-confirmation autonomy**: Does not wait for user confirmation unless unable to resolve an error
- **Concise communication**: Removes preamble and status updates, prioritizes action
- **Metaprompting**: Have the model analyze past conversations and generate system prompt improvements

## Growth Metrics

| Date | WAU | Source |
|------|-----|--------|
| Mid-March 2026 | 2M | Thibault Sottiaux (Codex lead) |
| April 8, 2026 | **3M** | Announced by Sam Altman. Codex lead Thibault Sottiaux confirmed "from 2M less than a month ago" |
| April 22, 2026 | **4M** | WSJ reporting. +1M in 2 weeks |

On April 8, 2026, Sam Altman announced Codex surpassed 3M weekly active users and reset usage limits. He stated plans to repeat resets at each 1M increment until reaching 10M users. Codex lead Thibault Sottiaux confirmed the rapid growth was "from 2M less than a month ago."

Post-GPT-5.5 launch (April 2026), Codex's momentum accelerated. On April 22, WSJ reported 4M WAU — a net gain of 1M in 2 weeks. OpenAI partnered with Accenture, Capgemini, and PwC to formalize enterprise Codex sales.

Sources: [Business Today — Codex 3M WAU](https://www.businesstoday.in/technology/story/openai-codex-celebrates-3-million-weekly-users-ceo-sam-altman-resets-usage-limits-524717-2026-04-08), [WSJ — OpenAI Working With Consultants to Sell Codex](https://www.wsj.com/cio-journal/openai-is-working-with-consultants-to-sell-codex-f355b1b9), [Gradually AI — Codex Statistics 2026](https://www.gradually.ai/en/codex-statistics/)

## Competitive Comparison

| Item | Codex | [[entities/claude-code]] | [[entities/cursor]] |
|------|-------|--------------------------|---------------------|
| Model | gpt-5.3-codex | Opus 4.7 / Sonnet 4.6 | Multi-model |
| OSS | ✅ Fully OSS | ❌ Proprietary | ❌ |
| Autonomy | High (hours) | High (Auto Mode) | Medium |
| Compaction | ✅ First-class | — | — |

## Related Topics

- [[entities/jason-liu]] — Jason Liu (Codex team DX engineer, author of this guide)
- [[concepts/codex-prompting]] — Codex prompt design patterns
- [[concepts/codex-goal]] — Codex Goals design and operation
- [[concepts/agent-harness]] — Agent harness design
- [[concepts/metaprompting]] — Metaprompting (self-improving prompts)
- [[entities/openai]] — OpenAI
- [[concepts/coding-agents]] — Coding agents general
