---
title: "Shopify"
created: 2026-05-20
updated: 2026-05-20
type: entity
tags: [company, shopify, ai-adoption, ai-coding, ai-agents, agentic-engineering, coding-agents, claude-code, github-copilot, cursor, mcp, llm-proxy, vibe-coding, infrastructure, developer-experience, internship, career, leadership, product, platform]
sources: [raw/articles/2026-05-20_zodchiii_shopify-claude-code-setup.md, raw/articles/2026-05-20_pragmatic-engineer_farhan-thawar-shopify-ai.md]
---

# Shopify

Shopify is a global e-commerce platform and one of the most aggressive adopters of AI-first engineering. With 23,000 engineers and a stated goal of **90% autonomous coding by Q3 2026**, Shopify has emerged as a leading case study in enterprise AI transformation. Led by CEO [[entities/tobi-lutke]] and Head of Engineering [[entities/farhan-thawar]], the company standardized on an internal LLM proxy and multi-agent AI workflows.

## AI-First Engineering Culture

Shopify's engineering culture is built on the principle that AI is not optional — it is expected:

- **No token spending limits**: Zero cost caps on AI token usage per engineer/team. Engineers who spend more are celebrated and investigated for best practices.
- **Expensive models encouraged**: CTO Mikey tells engineers: *"If you don't pay personally for O1 Pro or Gemini Ultra, you are crazy."*
- **Time ratio flipped**: Engineers now spend **70% on strategy** (mapping user flows, validating market demand, choosing architecture) and only **30% on execution**, since AI handles most coding.
- **Estimated ~20% productivity gain** — not from writing more code, but from testing 10 approaches instead of 2, faster prototyping, and higher-fidelity deliverables.
- **"Not a swim lane company"**: Engineers are "curious problem solvers" expected to span product and engineering boundaries.
- **Tobi Lütke's AI memo**: Internal document setting AI expectations across the company.

## LLM Proxy Architecture

Instead of standardizing on one AI tool, Shopify standardized the **infrastructure layer underneath**:

- Built an **internal LLM proxy** that routes every AI request through a single gateway
- [[entities/claude-code]], [[entities/github-copilot]], [[entities/cursor-ai]] all flow through the same infrastructure
- Provides: **privacy protection, token tracking, cost analytics, model routing**
- Enables swapping models without changing any engineer's workflow
- **Key insight for smaller teams**: Build the infrastructure so you can experiment with multiple tools while keeping control of costs and data

## AI Tool Adoption History

| Year | Tool | Context |
|------|------|---------|
| 2021 | [[entities/github-copilot]] | First company outside GitHub to deploy Copilot; negotiated direct with GitHub's CEO for 2 years free in exchange for feedback |
| ~2024 | [[entities/cursor-ai]] | Adopted ~1 year before May 2026; interestingly, Cursor growth happens outside engineering — finance, sales, support teams vibe-code MCP servers without engineer help |
| 2025–2026 | [[entities/claude-code]] | Primary AI coding tool; engineers run multiple parallel agents for different parts of the codebase |
| 2026 | Devin, Gumloop | Experimenting with additional AI coding tools |

## Parallel Agents & Extended Critique Loops

Shopify engineers run **multiple Claude Code agents simultaneously** — one refactors the auth module while another writes tests and a third updates documentation. The engineer reviews outputs, discards failures, and merges successes.

For complex architectural decisions, engineers use **extended critique loops** where a single agent generates, critiques, revises, and re-critiques its own output before delivering a final version with confidence levels.

## Internal AI Toolkit (MCP)

In April 2026, Shopify released an **open-source MCP server** (`@shopify/dev-mcp`) connecting [[entities/claude-code]] to live Shopify documentation, GraphQL API schemas, and store operations. This gives agents:

- Search current Shopify docs (not stale training data)
- Validate GraphQL queries against live schemas
- Execute store operations through Shopify CLI
- Create products, manage metafields, modify themes
- Run bulk operations with natural language

Non-engineering teams (finance, sales, support) are independently building MCP servers for Salesforce, Google Calendar, Gmail, and Slack.

## CLAUDE.md as Team Infrastructure

Shopify treats `CLAUDE.md` as **team infrastructure committed to git** and shared across all 23,000 engineers. It defines stack (Ruby on Rails, React, GraphQL, MySQL), commands, architecture, and rules (never bypass Sorbet type checking, all new code must have type signatures). **Critical constraint**: keep it under 60 lines — beyond that, you pay for every line on every turn with degraded performance.

## Guardrails & Permissions

Agents operate with strict guardrails:

| Allowed | Denied |
|---------|--------|
| Read, Glob, Grep, LS, Edit | Read `**/.env*` (secrets) |
| `dev test`, `dev style` (test/lint) | `git push` (can't push to remote) |
| `git status`, `git diff`, `git add` | `dev deploy` (can't deploy to production) |
| `git commit` | `bin/rails db:drop`, `rm -rf` |

Default mode: **acceptEdits**. Human stays in the loop for anything irreversible.

## 1,000 Interns Program

Shopify expanded from ~25 interns per term to **1,000 interns** (~350 per term, ~10% of engineering):

- **Hypothesis**: Interns are "AI reflexive" — they grew up with LLMs and change internal culture
- **"The secret weapon"**: Company learns more from interns than interns learn from the company
- Internship may become the **only entry-level path** into Shopify engineering
- Interns inject AI-native thinking throughout the organization through osmosis

## GSD: Internal Project Management

Shopify built its own project management tool called **GSD** ("Get Stuff Done") instead of using Jira or Linear:

- **Philosophy**: "First you make the tool, then the tool makes you"
- AI now **auto-generates weekly project updates** from PRs and Slack conversations
- Engineering managers get dashboards: focus time, meeting load, **AI adoption rates**

## Coding Interviews for Directors+

All engineering director and VP hires must pass **coding interviews**:

- Candidates pair-program with [[entities/farhan-thawar]]
- AI tools are allowed and **encouraged** — tests ability to discern good AI-generated code from bad
- "If they don't use a co-pilot, they usually get creamed by someone who does"
- Ensures leadership is technically literate in the AI era

## Key Engineering Metrics

- **23,000 engineers** racing toward 90% autonomous coding by Q3 2026
- **2nd largest MySQL fleet** outside Meta
- Core Ruby and MySQL contributors
- Non-engineers building production MCP servers independently

## See Also

- [[entities/farhan-thawar]] — Head of Engineering driving the AI transformation
- [[entities/tobi-lutke]] — Shopify CEO, creator of River AI coding agent
- [[entities/claude-code]] — Primary AI coding tool in Shopify's stack
- [[entities/cursor-ai]] — AI code editor adopted alongside Claude Code
- [[entities/gergely-orosz]] — Interviewed Thawar on The Pragmatic Engineer podcast
- [[entities/anthropic]] — AI lab partnership for tooling insights
