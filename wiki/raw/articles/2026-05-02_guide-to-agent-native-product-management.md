# A Guide to Agent-native Product Management

**Source:** https://every.to/guides/ai-product-management-guide
**Retrieved:** 2026-05-02
**Publication:** Every

## Core Thesis

The transformation of product management (PM) through LLMs and "agentic" capabilities. Introduces **Compound Engineering**, an agent-agnostic plugin designed to automate the routine drudgery of PM work—such as writing tickets, querying SQL, and manual reporting—allowing PMs to focus on strategy and user interaction.

## 1. The Shift: From Execution to Planning

The traditional software development lifecycle (SDLC) has shifted from a 20/80 planning-to-execution ratio to **80% planning and 20% execution**.

- **The New Workflow:** Plan → Ship → Review → Repeat.
- **The Agent's Role:** PM work now happens via conversation (e.g., with Claude Code). The "conversation is the work."
- **Tooling:** Use the Compound Engineering plugin to install specific skills

## 2. Skill: `ce:strategy`

Uses an agent-led interview to build a `strategy.md` file based on Richard Rumelt's *Good Strategy Bad Strategy*.

### Key Components:
1. **Target Problem:** A recurring, expensive pain point.
2. **Approach:** A specific "guiding policy" or unique angle for the solution.
3. **Who it's for:** Focused personas (*Crossing the Chasm* philosophy).
4. **Key Metrics:** 3–5 S.M.A.R.T. metrics.
5. **Tracks:** 2–4 multi-month initiatives.

## 3. Skill: `ce:product-pulse`

The "Pulse" is the quantitative window into product health, generated on demand by the agent.

### Four Pillars:
- **Headlines:** Bullet points summarizing critical data.
- **Usage:** Engagement counts, conversions, deltas.
- **System Performance:** Latency p50/p95/p99, top error signatures.
- **Followups:** 1–5 actionable items or anomalies.

### Data Integration via MCP (Model Context Protocol):
- **Analytics:** PostHog, Mixpanel, Amplitude.
- **Tracing:** Datadog, Sentry, Logfire.
- **Payments:** Stripe, Paddle.
- **Database:** Read-only connections for custom queries.

## 4. Agent-Native Shipping

PMs should stop writing manual tickets and use agents to manage the "Ship" phase.

- **No More Tickets:** Use `/ce:ideate`, `/ce:brainstorm`, `/ce:plan`
- **Agent-Managed Backlogs:** Connect agent to GitHub Issues or Linear via MCP.
- **Simplified Statuses:** Now / Next / Later and In Progress / Done.

## 5. The Qualitative Balance

Agents handle data; humans handle qualitative feedback:
- **Direct User Interaction:** Conspicuous email addresses in-product, 15-min call booking links.
- **Feedback Platforms:** Canny or Featurebase (with MCPs).

## Summary of Benefits

- **Memory:** Saved pulse reports in `~/pulse-reports/` create searchable history.
- **Grounding:** `strategy.md` aligns all agent skills to the core mission.
- **Focus:** PM work reduced to: dreaming up features, design thinking, user conversations.
