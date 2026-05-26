---
title: "Vibe Coding"
type: concept
aliases:
  - vibe-coding
created: 2026-04-12
updated: 2026-05-26
tags:
  - concept
  - agentic-engineering
status: draft
sources:
  - "https://simonwillison.net/2026/Feb/23/agentic-engineering-patterns/"
  - "https://simonwillison.net/guides/agentic-engineering-patterns/"
  - "raw/articles/2025-04-27_karpathy-vibe-coding-menugen.md"
---

# Vibe Coding

A development style defined by Simon Willison as **"coding where you pay no attention to the code at all, using an LLM to write code."**

## Definition

> *"I think of vibe coding using its original definition of coding where you pay no attention to the code at all, which today is often associated with non-programmers using LLMs to write code."*

## Comparison with Agentic Engineering

| Dimension | Vibe Coding | Agentic Engineering |
|-----------|-------------|---------------------|
| User | Non-programmers | Professional engineers |
| Engagement | Never looks at code | Amplifies existing knowledge with agents |
| Testing | Often skipped | Required (Red/Green TDD) |
| Goal | Make working code quickly | Balance quality and speed |
| Cognitive debt | Tends to be high | Intentionally reduced |

## Challenges of Vibe Coding

### Cognitive Debt
> "When we lose track of how code written by our agents works we take on cognitive debt."

When code we wrote but don't understand accumulates, future feature additions and maintenance become difficult.

### Solutions
- [[concepts/harness-engineering/agentic-workflows/linear-walkthroughs]] — Have the agent generate code explanations
- [[concepts/interactive-explanations]] — Understand algorithms through interactive animations
- [[concepts/agentic-manual-testing]] — Execute and verify behavior

## The Value of Vibe Coding

Simon himself does not deny the value of Vibe Coding. Rather, he notes that **even a ~40 minute vibe coding toy project can become an opportunity to explore new ecosystems.**

> "Even a ~40 minute vibe coded toy project can become an opportunity to explore new ecosystems and pick up some interesting new tricks."

## Practical Cases

### Xe Iaso: Building a Sponsor Panel with Vibe Coding (March 2026)

### Karpathy: MenuGen (April 2025) — The Original Vibe Coding Case Study

Karpathy's own **MenuGen** (menugen.app) is the project that coined the term "vibe coding." 100% built via Cursor + Claude 3.7 -- Karpathy provided high-level direction without writing code directly. A production app with Clerk auth, Stripe payments, OpenAI OCR, and Replicate image generation.

**Post-mortem insights:**

| Insight | Detail |
|---------|--------|
| **80/20 Trap** | Local prototype was fast, but deploying a real app was a "painful slog." Felt 80% done but was closer to 20% |
| **API Hallucination** | OpenAI OCR -> LLM hallucinated deprecated APIs; Replicate -> heavy rate limiting + out-of-date docs |
| **Vercel Debugging** | Required "pushing fake debugging commits" to force redeploys |
| **Clerk Auth** | Claude hallucinated ~1000 lines of deprecated code; needed custom domain, DNS, Google Cloud Console OAuth config |
| **Stripe Logic Error** | Claude matched payments to users via email (wrong -- Stripe email != Google OAuth email). Karpathy caught it |
| **LLM Gaslighting** | When corrected, LLM "thanks me... and tells me it will do it correctly in the future, which I know is just gaslighting" |
| **No State** | Skipped database (Supabase) and queues (Upstash) as "too much bear" -- app prone to timeouts |

**Four demands from Karpathy for the vibe coding era:**
1. **Batteries-Included Platforms** -- "opposite of Vercel Marketplace" pre-configuring domain, auth, payments, DB
2. **LLM-Friendly Services** -- docs in Markdown, configs via CLI/curl, not web UIs: "Don't talk to a developer... Instruct and empower their LLM."
3. **Simpler Stacks** -- Considering HTML/CSS/JS + Python FastAPI over "serverless multiverse"
4. **Apps as Prompts** -- Questioning if apps should be standalone products or "Artifacts" generated on-the-fly

> Source: [[entities/karpathy-writings]] | Raw: raw/articles/2025-04-27_karpathy-vibe-coding-menugen.md

[Xe Iaso](https://xeiaso.net/blog/2026/vibe-coding-sponsor-panel/)'s experience report on building a conference sponsor panel with Claude Code using vibe coding provides practical insights. This project was born from the urgency of "I really want to ship this before surgery."

#### Background: The GraphQL Swamp

Go and GraphQL don't go well together, and Xe had long described "Go and GraphQL are like oil and water." The `shurcooL/graphql` library requires struct-tag-based reflection query generation, and code generation tools produce massive boilerplate. GitHub's removal of the GraphQL Explorer made things worse, making interactive schema exploration impossible. Previously, this "GraphQL swamp" had derailed every attempt.

#### Workflow

1. **Start with dummy data** — Rapid UI prototyping with mockups before actual JSON structure is decided
2. **Skills-as-Context pattern** — Write requirements as skills (instructions), and the agent assembles them to generate code
3. **Iterative refinement** — Feedback → fix cycle with each verification, reaching production quality in one day
4. **Replace with real data** — Once prototype stabilizes, swap in actual sponsor data

#### Specific Skill Content

Xe prepared four agent skills (stored in `.claude/skills/`) and loaded them into Claude Code's context:

| Skill | Content |
|-------|---------|
| `templ-syntax` | Go HTML template library Templ syntax (expressions, conditionals, loops) |
| `templ-components` | Reusable component patterns (props, children, composition) |
| `templ-htmx` | Notes on combining Templ with HTMX (attribute rendering, event handling) |
| `templ-http` | How to properly integrate Templ into `net/http` handlers (routing, data passing, request lifecycle) |

Templ is a library rarely included in LLM training data; without skills, it generated code full of hallucinations. Loading the skills resulted in most generated Templ code **compiling on the first pass**.

> *"Think of it like giving someone a cookbook instead of asking them to invent recipes from first principles."*

#### Parallel Work Pattern

While the agent team proceeded with code generation, Xe worked in parallel on:
- Provisioning OAuth credentials in GitHub Developer Settings
- Creating a Neon PostgreSQL database
- Setting up a Tigris bucket (for sponsor logo storage)
- Providing credentials to the agent immediately when needed

**By parallelizing ops work and code generation**, Xe achieved a zero-wait-time development flow.

#### Tech Stack

| Component | Technology | Reason |
|-----------|-----------|--------|
| Backend | Go | Existing knowledge and site foundation |
| HTML Rendering | Templ | Avoids `html/template` constraints |
| Interactions | HTMX | Simple pages don't need React |
| Database | PostgreSQL (Neon) | Managed, zero ops overhead |
| Authentication | GitHub OAuth | Integration with sponsor API |
| Sponsor Data | GitHub Sponsors GraphQL API | Direct integration |
| Image Storage | Tigris | Plug and play |

#### Results

- Traditional "scaffolding" that would take a week was **completed in one day**
- GraphQL code uses raw query strings + manual JSON parsing — quality "not ready for code review," but **it works**
- Trade-off: "Beautiful but unpublished" vs "Ugly but published" — pre-surgery delivery was the priority
- Sponsor panel is live at `sponsors.xeiaso.net`

#### Limitations and Challenges

- **Org sponsorships not supported**: Org sponsor schema differs from individual, requiring separate auth flow
- **Code quality**: Raw JSON parsing, functional but uninspired variable names, and some spots lacking error context
- **Not suitable for security-critical systems**: Not a target for vibe coding when line-by-line audit is needed
- **Planned rewrite in 6 months**: First, it's important that it exists

#### Lessons

- **Skills as code**: The division of labor — humans write instructions (skills), agents write code — is effective, especially essential for libraries underrepresented in training data
- **Mockup → real data migration** is a pattern well-suited to vibe coding
- **Narrower scope** yields higher success rates (focus on specific UI components)
- **Parallel ops + code generation** eliminates wait time
- Projects repeatedly derailed by "correct methods" are prime candidates for vibe coding

### Tim Sh: Self-hosting a Vibe Coded App (April 2026)

[Tim Sh](https://timsh.org/why-you-should-self-host/) recommends self-hosting vibe-coded apps, drawing on 5 years of deploying 50+ services. This is presented as a suitable operational model especially for indie developers and vibecoders with limited budgets and no backups.

#### Problems with Traditional Cloud PaaS

| Problem | Details |
|---------|---------|
| **Unpredictable usage-based billing** | Starts free/cheap but suddenly expensive with traffic spikes (see "Serverless Horrors") |
| **High abstraction level** | PaaS is "level 50" abstraction — can't understand what's happening inside, hard to debug when problems arise |
| **Over-provisioned scalability** | Most apps don't need "1K→1M user" scaling; a fixed server is sufficient |

#### Recommended Setup: Coolify + Hetzner VPS

| Element | Details |
|---------|---------|
| **Server** | Hetzner VPS (€8/month: 3 vCPU, 4GB RAM, 80GB SSD) |
| **PaaS Layer** | Coolify (open-source self-hosted PaaS) |
| **Deploy** | Docker Compose-based, auto-deploy via GitHub integration |
| **Network** | Automatic reverse proxy (Traefik) + Let's Encrypt SSL |
| **Notifications** | Telegram notifications (lifesaver for deploy/error alerts) |

Hetzner's €8/month plan offers roughly **3.5x cost difference** compared to Digital Ocean's equivalent spec (~$30/month).

#### Significance for Vibe Coders

- **Local vibecoded app → production** in 15 minutes: `localhost:8080` → `https://sub.domain.com`
- Deployable just by having the LLM generate Docker Compose (ask Cursor/Claude Code)
- No usage-based billing — no charges when traffic is zero
- "Freedom of abstraction": Choose your preferred abstraction level — from Coolify's one-click deploy (PaaS equivalent), to raw Docker Compose, to a single Python script + systemd timer
- Operable at less than the cost of a monthly lunch

> *"You have your own (vibecoded) app and a very cheap server, and you get from localhost:8080 to https://sub.domain.com in 15 minutes. It feels great."*

#### Suitable User Profiles

- **Vibecoder / Indie developer**: Starting from zero budget, wants to operate on their own
- **Startup CTO**: Wants to set up company tools and infrastructure at low cost
- **However**, apps with guaranteed explosive growth (10x users/day) may still be better suited to traditional serverless

## Tim O'Reilly's Perspective: CHOP Paradigm and Historical Context

Tim O'Reilly (O'Reilly Media founder) positioned [[entities/tim-oreilly|Vibe Coding]] in his February 2025 article "[The End of Programming as We Know It](https://www.oreilly.com/radar/the-end-of-programming-as-we-know-it/)" as the latest wave in the long history of programming abstraction.

> Source: [raw/articles/2025-02-04_oreilly-end-of-programming.md](2025-02-04_oreilly-end-of-programming.md)

### Historical Evolution of Abstraction

| Era | Abstraction Level | Result |
|-----|-------------------|--------|
| Early days | Machine code → Assembly | Reduced demand for hardware engineers |
| High-level languages | Fortran, COBOL, C, Java | More programmers, expanding demand |
| OS revolution | Hardware drivers → API | Focus on application development |
| Web & Cloud | Stripe, Google Maps API | Birth of the "Internet OS" |
| AI era (CHOP) | Natural language → Code | Programmers = managers of digital coworkers |

### CHOP (Chat-Oriented Programming)

O'Reilly named the current paradigm **CHOP (Chat-Oriented Programming)**. Natural language prompts become the primary interface, replacing code writing.

> *"The human programmers are their managers. There are now hundreds of thousands of programmers doing this kind of supervisory work. They are already living in a world where the job is creating and managing digital co-workers."*

### Jevons Paradox and Expanding Programming Demand

O'Reilly cites economist William Jevons' paradox — just as coal efficiency increased coal consumption, making programming more efficient with AI will **increase, not decrease**, demand for software.

### The 70% Problem (Addy Osmani)

[[entities/addy-osmani]] introduced this concept in O'Reilly's article. AI can handle the first 70% of a project (scaffolding, documentation generation), but the remaining 30% requires "hard-won engineering wisdom" — neglecting this causes the "house of cards code" to collapse under real-world pressure.

| Phase | AI's Role | Human's Role |
|-------|-----------|--------------|
| First 70% | Scaffolding, documentation, prototyping | Direction setting, requirements definition |
| Final 30% | Limited (edge cases are difficult) | Engineering judgment, architecture decisions, quality assurance |

### A New Role: Agent Engineer

O'Reilly foresees the emergence of a new specialization: the **Agent Engineer**, focused on encoding business policies and processes into AI agents. This parallels how React developers specialized in frontend architecture.

### Need for Agent Infrastructure Protocols

O'Reilly advocates for standardized protocols for agents (analogous to HTTPS for the web):
1. Attribution of actions to specific agents/users
2. Design of inter-agent interactions
3. Detection and remediation of harmful actions

This was a pioneering framework that later materialized as standards like MCP (Model Context Protocol), ACP (Agent Communication Protocol), and A2A.

> *"Computer science is about systematic thinking, not writing code."* — Mehran Sahami, Stanford CS Chair (quoted in O'Reilly article)

## Related Concepts

- [[concepts/agentic-engineering]] — Contrasting development style
- [[concepts/cognitive-debt]] — Major risk of Vibe Coding
- [[concepts/harness-engineering/agentic-workflows/linear-walkthroughs]] — Method for repaying cognitive debt
- [[concepts/claude-code-tips]] — Claude Code setup guide
- [[concepts/self-hosting-ai-development]] — Self-hosting vibe-coded apps
- [[concepts/mcp]] — Inter-agent communication protocol (materialization of O'Reilly's protocol standardization vision)

## References

- [[entities/simon-willison]] — Proponent of Vibe Coding vs Agentic Engineering
- [[entities/xeiaso-net]] — Xe Iaso (author of practical case study)
- [[entities/tim-oreilly]] — Proponent of the CHOP paradigm, historical context of programming abstraction
- [[entities/addy-osmani]] — The 70% Problem, Conductor → Orchestrator framework
