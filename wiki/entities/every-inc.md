---
title: "Every (company)"
created: 2026-05-25
updated: 2026-06-05
type: entity
tags:
  - entity
  - company
  - ai-native
  - agent-native
  - blog
  - podcast
  - openclaw
  - content-creator
sources:
  - "transcripts/2026-05-24_lenny-podcast-dan-shipper-ai-paradox.md"
  - "https://every.to/about"
  - "https://every.to/products"
  - "raw/articles/2026-04-17_every-to_folder-is-the-agent.md"
  - "raw/articles/2026-01-17_every-to_agent-native-architectures.md"
  - "raw/articles/2026-03-26_every-to_plus-one-openclaw-agents.md"
  - "raw/articles/2026-05-21_after-automation.md"
  - "raw/articles/2026-05-02_guide-to-agent-native-product-management.md"
  - "raw/articles/2026-05-24_lenny-podcast-dan-shipper-ai-paradox.md"
  - "raw/articles/2026-06-02_mvanhorn_every-agentic-engineering-hack.md"
  - "https://github.com/EveryInc/compound-engineering-plugin"
---

# Every

Every is a media and software company founded in 2020 by [[entities/dan-shipper|Dan Shipper]]. They publish a daily newsletter about emerging technology, run the "AI & I" podcast, build AI-native software products, offer courses, and provide AI consulting and training services.

**Website**: https://every.to  
**X**: [@every](https://x.com/every)  
**Subscribers**: 125,000+ founders, operators, and investors

## Products

### AI Applications
| Product | Description |
|---|---|
| **Spiral** | AI writing assistant with taste |
| **Cora** | AI email assistant ($15/month) |
| **Sparkle** | Automatic file organization (Mac) |
| **Monologue** | Voice dictation (3x faster) |
| **Proof** | Collaborative editor for humans and AI agents |
| **Plus One** | Hosted [[openclaw]] agent in Slack (one-click setup) |

### Content
- **Newsletter**: Daily technology coverage
- **AI & I Podcast**: Weekly conversations with tech leaders
- **Columns**: Chain of Thought (Dan Shipper), Context Window (staff)
- **Vibe Check**: Day-zero AI model reviews

### Experiments (Product Studio)
Every runs a product studio incubating AI-native tools:
| # | Product | Description |
|---|---|---|
| 006 | Proof | Write/edit with AI agents, track authorship |
| 005 | Kairos | Engage with reading content |
| 004 | TLDR | Business storytelling |
| 003 | Extendable Media | AI-expanded perspective media |
| 002 | MindTune | Attention control for thought shaping |
| 001 | Machcast | Guided prompts for shareable thoughts |

## Philosophy: Compound Engineering

Every pioneered [[concepts/compound-engineering-every|Compound Engineering]] — an AI-native development methodology where:
- Humans set up the right conditions (prompts, context files, skills)
- AI agents do the iterative building work
- Humans review and provide taste/judgment
- The loop compounds over time, building institutional knowledge

Key insight: **"The folder is the agent"** — a project directory with CLAUDE.md, skills, and accumulated context transforms a general model into a specialist [[concepts/folder-is-the-agent|Folder Is the Agent pattern]].
### Compound Engineering Plugin & Ecosystem (June 2026)

The open-source plugin on GitHub (`EveryInc/compound-engineering-plugin`) has grown past 14,000 stars. Key contributors include Kieran Klaassen, Trevin Chow, and [[entities/matt-van-horn|Matt Van Horn]] (#3 contributor as of June 2026). Van Horn documented the internal `/ce-plan` mechanics in "Every Agentic Engineering Hack I Know": parallel research agents fan out to read codebase conventions, search past solutions, and research external docs simultaneously.

**Compound Engineering-inspired projects by Van Horn:**
- **last30days** (27K stars) -- Multi-platform research tool (Reddit, X, YouTube, TikTok, HN, GitHub, web in parallel)
- **Printing Press** (3.7K stars, 320+ PRs) -- CLI factory for agent-native service wrappers (Tesla, Instacart, ESPN, Alaska Airlines)
- **AgentMail** -- Open-sourced Claude Code email integration (github.com/mvanhorn/agentmail-to-claude-code)
- **Agent Cookie** -- Browser session sync for agent CLIs across machines

## Agent-Native Architecture

Every published definitive guides on [[concepts/agent-native-architecture|Agent-Native Architecture]]:

### Core Principles
1. **Parity** — Agent achieves everything UI can
2. **Granularity** — Tools are atomic primitives; features are outcomes via prompts
3. **Composability** — New features = new prompts, not code
4. **Emergent Capability** — Agents accomplish unanticipated tasks
5. **Improvement Over Time** — Better through context accumulation + prompt refinement

### Dispatch Layer Pattern
- Ruby daemon watches directory for spawn requests
- Lead agent breaks tasks into subtask files
- Daemon spawns workers in correct folders
- Workers report back via files (no custom networking needed)
- **Scale**: Running 44 folders-as-agents across projects

## Key People
- **Dan Shipper** — CEO, cofounder
- **Kieran Klaassen** — Cora general manager, compound engineering pioneer
- **Trevin Chow** — Product leader
- **Katie Parrott** — Writer, AI guides
- **Willie Williams** — Writer, OpenClaw guides
- **Lucas Fischer** — Designer, Monologue

## Team AI Usage
- 95% of work emails handled by AI (Cora)
- No one writes code by hand — all engineering is AI-assisted
- Team of ~30 runs 5 software products + media operation (doubled from ~15 in one year)
- AI agents (@Claudie, @Andy, @Viktor) are first-class Slack team members
- **44 folders-as-agents** running across projects

### Internal AI Workflows (from Lenny's Podcast, May 2026)
- **Codex is Dan's daily driver**: Uses OpenAI Codex with an in-app browser for all work — writing in Proof, checking analytics, managing email. "I basically spend all my time in it."
- **Inbox zero via Cora + Codex**: Codex gathers emails via Cora, renders a page, and Dan "monologues" responses — achieved 10+ consecutive days of inbox zero for the first time
- **Quarterly planning with Notion agents**: End-of-2025 planning done entirely with a Notion agent querying each employee about goals, metrics, and challenges. Produced "incredibly good" strategy reports
- **Email written by GPT-5.5**: Most of Dan's email is now AI-written. Codex once sent an email to an investor without review — "I went to my sent and looked at it and I was like, oh, this is exactly what I would have sent"
- **Agent bug reports**: When Proof users have problems, their agent sends bug reports with exact repro steps, codebase analysis, and auto-creates GitHub issues — "way better than human bug reports"

### Consulting & Forward Deployed Engineers
Every runs an AI consulting practice powered by **Claudie** (their internal Slack agent). Nitesh, an AI engineer, spends most of his time talking to Claudie in Slack rather than writing code — "Why did you do this dumb thing? Let's fix that." This forward-deployed engineer role is what Every also lends to clients.

### The Super-Agent Model
Dan initially believed in personal agents for every employee (the "Golden Compass daemon" model), but flipped to the **one super-agent per company** model. The key reason: "In order for an AI agent to be useful right now, it really needs a human who cares about it." Personal agents break and nobody maintains them. A company super-agent with a dedicated forward-deployed engineer works better.

### Business Model Insights (from Lenny's Podcast)
- **SaaS economics shift**: When users access SaaS tools via Codex/Co-work, they bring their own AI tokens. Every doesn't pay for tokens in Proof — users bring their own. "It changes your margins back" — SaaS companies don't need to build expensive AI features if users bring their own agents.
- **Agent-to-agent interactions**: Every's products assume users access them through Codex or Co-work, not standalone. Codex provides massive context about the user that the SaaS tool can leverage directly — enabling personalized onboarding without traditional flows.
- **Product simplification**: Proof doesn't need Word-style formatting, page breaks, or tables because the agent handles all formatting. "You can make the products a lot simpler and faster to start than the legacy products are."
- **Agent-native UX**: New considerations include approval workflows, activity inboxes summarizing agent actions, and rollback capabilities — agents can make billions of requests in seconds.

### Product-Specific Details
- **Plus One** (hosted OpenClaw): On waitlist with deposit required. OpenClaw is "a very hard agent harness to make work — it's moving so incredibly fast." When things break on the platform level, Every can't fix them.
- **Spiral** (writing app): Run by Marcus, a PM by training who previously ran Axios's writing product. After a year off getting "super AI pilled," he now ships faster than almost anyone on the team using Cursor/Claude Code — pairing product sense with light technical knowledge.
- **Proof** (collaborative editor): Open-source. Users send bug reports via their agents, which include exact repro steps and codebase analysis. Creates a fast closed loop: user bug → agent report → GitHub issue → agent fix.

### Every's Generalist Culture
- Everyone at Every is an AI early adopter — engineers, designers, writers, editors, salespeople, customer service
- Team members get early access to models and tools before public release — "We get to beta test and alpha test and help steer the direction of where things are going"
- Dan's philosophy: predicting the future isn't about prognosticating, it's about "living in it together" and noticing what's happening
- All new hires receive Annie Dillard's *The Writing Life* — everyone reads at least the last chapter
- Everyone at Every is "a generalist and really loves having their fingers in a lot of different pots" — this generalist culture enables rapid AI adoption across roles

## Related Pages
- [[entities/dan-shipper]] — CEO and cofounder
- [[concepts/compound-engineering-every]] — Development methodology
- [[concepts/folder-is-the-agent]] — Architecture pattern
- [[concepts/agent-native-architecture]] — Design principles
- [[concepts/after-automation]] — Automation paradox analysis
- [[concepts/human-sandwich]] — Human-AI collaboration pattern
- [[openclaw]] — Underlying agent platform for Plus One
- [[concepts/ai-slop]] — "Visible sameness" concept coined here
