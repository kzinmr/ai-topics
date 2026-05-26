---
title: "Forward Deployed Engineering (FDE)"
created: 2026-05-18
updated: 2026-05-25
tags:
  - company
  - strategy
  - ecosystem
  - enterprise-ai
sources:
  - raw/newsletters/2026-05-17-anthropic-pulls-away-openai-strikes-back-and-google-s-gemini-rising.md
  - raw/articles/2026-05-20_varick_forward-deployed-engineering-101.md
  - raw/articles/2026-05-25_saas-fde-ai-agent-era_career-strategy.md
---

# Forward Deployed Engineering (FDE)

## Overview

Forward Deployed Engineering (FDE) is the emerging industry paradigm where frontier AI labs embed engineers directly into enterprise customer environments to build custom AI solutions, rather than selling model API access alone. As models commoditize, the **deployment layer becomes the new moat**.

> "Every AI lab is becoming Palantir." — The Signal, May 2026

## The Shift from API Sales to Service Delivery

In 2025-2026, all three major frontier labs made structural moves toward the FDE model:

| Lab | FDE Initiative | Scale | Details |
|-----|---------------|-------|---------|
| **OpenAI** | "The Deployment Company" JV | $4B raise, $10B pre-money | Tomoro providing 150 FDEs; backed by TPG, Bain Capital, SoftBank, 19 investors |
| **Anthropic** | Blackstone/Goldman Sachs JV | $1.5B | Claude-powered enterprise deployment systems; Blackstone, Hellman & Friedman, Goldman Sachs each contributing $300M |
| **Google** | Internal hiring | Hundreds of FDEs | Building deployment engineering teams alongside Gemini model development |

## Why FDE Is Emerging Now

1. **Model commoditization**: GPT-5.5, Claude Opus 4.7, Gemini 3.1 are converging on capability — differentiation shifts to integration
2. **Enterprise complexity**: Real-world deployment requires understanding legacy systems, compliance, and organizational workflows that models alone can't navigate
3. **Revenue scale**: Service delivery generates far higher per-customer revenue than API tokens
4. **Lock-in**: FDE relationships create switching costs that model quality alone cannot

## Relationship to AI Services Joint Ventures

FDE is the operational model behind the wave of AI services joint ventures. See [[concepts/ai-services-joint-ventures]] for the financial structure comparison.

## The FDE Job: Audit → Evals → Deployment

Varick's practical FDE guide (May 2026) breaks the FDE role into three phases:

### 1. Audit
Go on-site with customers and map each team's workflow. Three principles for deciding **what should/shouldn't be automated**:
| Condition | Decision |
|------|------|
| Rule-based but inputs vary (email→PDF→images) + tool calls needed | Use **Agent** |
| Both rules and inputs are predictable | **Code** is faster and cheaper |
| Pattern recognition + domain expertise needed | Keep **Manual** |

Key points:
- **Target high-frequency, high-volume automation** — An agent that runs 5 times a month won't generate ROI
- **Don't overuse AI** — Most automation needs a series of tool calls + one LLM orchestration pass

### 2. Evals
Multi-million dollar AI deployments require evidence that they work:
1. **Trace human steps and score AI at each step**: Humans don't solve problems in one shot. Verify AI decisions at each checkpoint
2. **Start with a few excellent examples to establish criteria**: Define "perfect answers" with humans and evaluate agents against that baseline

### 3. Deployment
- **Avoid large-scale data migration**: Build APIs on top of existing data layers (SharePoint/DB), then place the model as orchestrator on top
- Create a **sandbox execution environment** within customer infrastructure for safe testing
- **Start small**: Begin with a bug detection → investigation → ticket creation Agent, then add code fix / PR creation capabilities after success
- **Start with minimal autonomy and gradually grant permissions**

## How to Become an FDE (30-Day Roadmap)

Varick's 30-day roadmap:

| Checkpoint | Days | Content |
|----------------|------|------|
| CP1 | Day 7 | Agent loop, tool calling, guardrails (input validation, max step limits, output filtering), context window vs external memory trade-offs, audit trails |
| CP2 | Day 14 | Structured output (always JSON), demo→production breakage (see Agents 102), checkpoints (save state every N steps → resumable) |
| CP3 | Day 21 | Retry logic + exponential backoff, cost optimization (cheaper models for cheap subtasks, caching, max tokens), golden dataset (20 real queries + manual labels), multi-agent pipelines |
| CP4 | Final week | Full review + explain aloud + tie to business metrics |

**3 Successful Backgrounds**: Consultants, Product Managers, Software Engineers.
- **Consultant/PM**: Have the data→ROI conversion ability. Supplement engineering experience gaps with a portfolio (production-ready Agent, RAG pipeline, Eval framework, MCP)
- **SWE**: Communication is paramount. Must be able to translate what you build into business value

> **Critical Skill**: "Can you explain what AI can and cannot do to non-technical decision-makers?" Without this, you cannot become an FDE.

## FDE-SaaS Synthesis: The Most Valuable Position

### The False "FDE vs SaaS" Dichotomy

Framing FDE and SaaS as opposing axes is dangerous binary thinking. The winning position is neither pure FDE nor pure SaaS. It is **the ability to rapidly convert patterns discovered by FDEs in the field into reusable product and platform primitives**.

### Direction Set by Industry Leaders

- **OpenAI FDE Job Requirements**: "Codify practical patterns into tools, playbooks, and building blocks"
- **Anthropic FDE Job Requirements**: "Identify and codify repeatable deployment patterns, provide feedback to Product/Engineering"

A top-level FDE is not someone who "can build anything for any customer." It is someone who can **discover requirements only visible from the field and convert them into reusable abstractions**.

### Most Valuable Career Titles

| Title | Characteristics |
|----------|------|
| **Forward Deployed Product Engineer** | Balance of FDE field sense + product building |
| **AI Agent Platform Engineer** | Design and generalize the agent infrastructure itself |
| **Agentic Product Engineer** | Embed autonomous agents into products |
| **Applied AI Product Engineer** | Lead products in applied AI domains |

### Positions to Avoid

- **Pure FDE**: Heavy consulting weight, little time for product building. Even if you codify field patterns, there's no mechanism for reuse
- **Traditional SaaS Developer**: Only builds shared screens and features. Falls behind the paradigm shift of the AI agent era

### Action Plan

| Timeline | Action |
|------|-----------|
| **3 months** | Start FDE-like work in your current role. Pick one customer workflow, build an Agent, measure impact |
| **6 months** | Expand to 2-3 customers. Identify common vs divergent patterns, find seeds for reusable abstractions |
| **12 months** | Decide — stay if your current employer embraces the FDE-product synthesis model; otherwise move to the FDE/Applied AI side |

> Those who stand at the boundary between FDE and SaaS are the rarest and most valuable positions in the AI agent era.

## Open Questions

- Does FDE scale linearly with headcount, or can tooling make it self-service?
- Will FDE become a permanent organizational function or a transitional phase before models handle integration autonomously?
- How does this affect the open-source AI ecosystem, where no FDE layer exists?

## See Also

- [[concepts/ai-services-joint-ventures]] — Joint venture structures for AI service delivery
- [[entities/openai]] — OpenAI's Deployment Company strategy
- [[entities/anthropic]] — Anthropic's enterprise JV
- [[entities/google]] — Google's compute advantage and enterprise push
