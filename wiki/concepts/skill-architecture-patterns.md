---
title: "Skill Architecture Patterns: Self-Authored vs Governed"
created: 2026-04-18
updated: 2026-04-18
type: concept
tags: [ai-agents, skill-management, hermes-agent, openclaw, architecture]
sources:
  - "https://x.com/elvis_/status/..."
---

# Skill Architecture Patterns: Self-Authored vs Governed

**Overview:** Comparative analysis of two fundamentally different approaches to agent skill management — Hermes Agent's self-authoring, maximalist skill system vs OpenClaw's governed, primitives-first approach.

**Analyst:** elvis (9-hour side-by-side source code analysis, April 2026)

## Two Philosophies

| Dimension | Hermes Agent (Nous Research) | OpenClaw (Steinberger) |
|-----------|------------------------------|------------------------|
| **Philosophy** | Batteries-included, Rails-style | Primitives-first, Linux-style |
| **Skill Authorship** | Self-authoring via prompt nudges | Explicit, user-governed |
| **Default Corpus** | 123+ bundled SKILL.md files | Baseline only, rare additions |
| **Growth Model** | Organic — agent creates skills autonomously | Bounded — new skills go to ClawHub first |
| **Product Thesis** | "Agent that knows 100+ things on day one" | "Exactly what you told it to do, nothing more" |

## Hermes Agent: Self-Improving Skills

### Mechanism

1. **Prompt Nudge:** System prompt instructs agent to consider saving a skill every N tool calls
2. **Background Review:** After task completion, automated scan identifies skill-worthy patterns
3. **Pre-Compression Flush:** Durable knowledge saved to disk before context compression kicks in
4. **Blunt Rule:** If existing skill covers this, patch it. Only create new if nothing matches.

### What Works

> "The agent self-improves by writing its own skills. I watched it create an `extract-social-testimonial` skill on its own — the kind of skill I never would have thought to create. First time seeing this worked like magic." — elvis

- **Emergent capability:** Agent discovers useful skills the developer never anticipated
- **Day-one productivity:** 123 bundled SKILL.md files covering GitHub PR workflows, Obsidian, Google Workspace, Linear, Notion, Typefully, Perplexity, deep research, Minecraft modpack servers, and more
- **Tool Gateway lock-in:** One subscription unlocks 300+ models, web scraping, browser automation, image generation, cloud terminal, text-to-speech — reinforcing the batteries-included thesis

### The Skill Explosion Problem

> "Real example: the agent wanted to read an image from my desktop. Tried browser read and vision skill, nothing worked. So it wrote a third `read-local-image` skill lol. These are 3 skills all adjacent to 'image + local filesystem + model can see it.'" — elvis

**Long-tail failure mode:**
- Agent excels at spotting "I should bottle this up"
- Agent struggles with "I already bottled this up three folders over"
- Corpus grows faster than it consolidates
- Result: brilliant skills, redundant skills, overlapping skills nobody remembers exist

**Net impact:** Over time, skill accumulation outpaces consolidation. The self-improvement loop has no upper bound on growth.

### Expected Resolution Path

elvis predicts this is a known product prioritization issue, not a fundamental flaw. Expected solutions:
1. Consolidation pass using invocation metrics
2. Stronger deduplication on skill creation
3. Skill usage analytics to identify dead/overlapping skills

## OpenClaw: Governed Primitives

### Five-Tier Skill Precedence

```
1. Workspace skills (highest priority)
2. User global skills
3. Managed skills
4. Bundled skills (baseline only)
5. Extra skills (lowest priority)
```

**Key property:** "When something breaks at 3am, you can trace it in one grep instead of guessing which skill the agent triggered."

### Discovery Bounds

- **Byte caps** on skill content
- **Candidate caps** on skill loading
- **Symlink rejection** for security
- **Verified file opens** only
- **Eligibility checks separate from discovery** — different agents can see different subsets

### Governance Policy

> "Bundled skills are baseline only. New skills go to ClawHub first. Core additions should be rare and require a strong product or security reason." — OpenClaw VISION.md

**Result:** The corpus doesn't rot because nothing gets added without user intention. Every skill must earn its spot.

### AGENTS.md Optimization Pattern

elvis combined OpenClaw's TOOLS.md with Vercel's AGENTS.md pattern:

> "Tool activation correctness is better on OpenClaw than Hermes for tasks where the agent has to pick the right CLI/API from ~50 options."

**Principle:** Explicit > Implicit. The agent doesn't decide "is this skill-worthy enough to load" — routing rules are already in the system prompt.

## Strategic Positioning Analysis

### Hermes: Product Positioning Masterclass

> "OpenClaw had the audience. The mindshare, the GitHub stars, the 'it's basically the standard now' energy. Look at what happened to everyone who tried to fight that fight head-on — nanoclaw, nullclaw, picoclaw, zeroclaw. All trying to out-OpenClaw OpenClaw. None got Hermes's traction." — elvis

**Hermes's winning move:** Don't compete on OpenClaw's board. Create a new game:
- Self-authoring instead of governed
- Bundled-by-default instead of primitives-only
- Maximalist on purpose
- Tool Gateway as ecosystem lock-in
- Every launch reinforces: "We are not the minimalist primitives company"

### OpenClaw: Foundational Stack Layer

> "@steipete gave the world a new layer in the stack and put a claw in everyone's hand. That's foundational work. You don't even need to use OpenClaw to benefit from OpenClaw — the patterns will show up in everything downstream for years." — elvis

OpenClaw's influence extends beyond direct usage. The governance patterns, precedence model, and explicit tool routing are becoming industry standards.

## Practical Decision Framework

| User Profile | Recommendation | Why |
|--------------|----------------|-----|
| Getting started quickly | **Hermes** | Opinionated defaults = productive on day one, low maintenance overhead |
| Need 100% control | **OpenClaw** | Legibility and scope control matter more than self-improvement |
| Building custom agents | **Both** | Steal patterns from each — OpenClaw for governance, Hermes for self-improvement |

## Key Insight

> "Both harnesses will do everything you want. Pick either, you'll be fine. But the more interesting question isn't which to pick — it's what you can learn from each." — elvis

The real value is in **pattern extraction**: understanding why Hermes's self-improving skills work for rapid iteration, why OpenClaw's governance works for production stability, and how to combine both approaches for maximum leverage.

## Related

- [[hermes-agent]] — Hermes Agent platform (self-authoring skills)
- [[peter-steinberger]] — OpenClaw creator
- [[teknium]] — Hermes Agent architect
- [[harness-engineering/system-architecture/agent-skills]] — Agent Skills / SKILL.md bundles
- [[anthropic-openclaw-conflict]] — Open-source vs platform risk debate
- [[harness-engineering]] — Harness Engineering framework
- [[harness-engineering/agentic-workflows/agent-first-design]] — Agent-first codebase design
- [[comparisons/hermes-vs-openclaw-architecture]] — Detailed architecture comparison

## Sources

- elvis analysis thread (April 2026) — 9-hour side-by-side source code study
- OpenClaw VISION.md — skill governance policy
- Vercel AGENTS.md optimization pattern — https://vercel.com/blog/agents-md
- Hermes Agent documentation — https://hermes-agent.nousresearch.com/docs/
