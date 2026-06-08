---
title: "Evals vs Monitoring Debate"
type: concept
created: 2026-05-28
updated: 2026-05-28
tags:
  - evaluation
  - methodology
  - controversy
  - infrastructure
aliases:
  - evals-are-dead
  - evals-vs-ab-testing
  - thoughts-on-evals
sources:
  - raw/articles/2025-09-05_ben-hylak_thoughts-on-evals.md
  - https://www.raindrop.ai/blog/thoughts-on-evals/
  - raw/articles/2026-05-28_ben-hylak_how-to-eval-ai-agents.md
related:
  - "[[concepts/agent-evaluation-methodology]]"
  - "[[concepts/probabilistic-era-software]]"
  - "[[concepts/raindrop]]"
  - "[[entities/ben-hylak]]"
  - "[[entities/ankur-goyal]]"
  - "[[entities/gian-segato]]"
---

# Evals vs Monitoring Debate

A defining intellectual conflict in AI evaluation: **offline evals** (pre-ship testing of prompts, models, and agent behaviors) versus **production monitoring** (observing real-world behavior with signals and A/B experiments). The debate crystallized in September 2025 when [[entities/ben-hylak|Ben Hylak]] (Raindrop) published a point-by-point rebuttal to [[entities/ankur-goyal|Ankur Goyal]]'s (Braintrust) claim that **"evals are the future."**

> "When we blur definitions, we blur decisions. If you strip away the jargon, you have the two levers engineers have always used to understand change: testing changes before shipping, and measuring what actually happens after shipping. Which one matters more? The answer is the same it has always been: the one that tells you the truth." — Ben Hylak

## The Two Positions

| Dimension | **Evals Position** (Ankur Goyal / Braintrust) | **Monitoring Position** (Ben Hylak / Raindrop) |
|---|---|---|
| **Core claim** | Evals are the future of AI product optimization | Production truth > offline evals for agent products |
| **What matters** | Systematic quality measurement before shipping | What actually happens to real users after shipping |
| **Analogy** | Unit tests / Test-Driven Development | Sentry / Datadog — monitoring, not testing |
| **Key argument** | A/B testing is slow, expensive, and insufficient for AI | Evals are adversarially selected; they only catch what you already know |
| **Personalization** | Evals enable personalized software | Personalization makes evals impossible (millions of user-specific tests needed) |
| **Speed claim** | "Test dozens of variations and see what works immediately" | "Minutes to deploy, hours to get answers" with A/B tests |
| **Tool** | Braintrust (eval platform) | Raindrop (agent monitoring) |

## The 6 Definitions Problem

Hylak identified a fundamental ambiguity: the word "eval" has at least **6 distinct meanings**, making the debate slippery:

1. **Known input, no validator** — Human review needed
2. **Known input, known output, deterministic validator** — String contains X
3. **Known input, expected output, LLM judge** — LLM decides if correct
4. **Known input, human-aligned LLM judge** — Score joke funny, etc.
5. **Frontier model evals** — Aspirational, for unsolved capabilities
6. **Online evals** — Any of 1-4 run on sampled production data

> "Technically, A/B tests are just a type of 'online evals.' But when people talk about 'evals' in the context of LLMs, they're usually tests."

## Claim-by-Claim Breakdown

### Claim 1: "Evals are the future"

**Hylak's rebuttal:** Test-Driven Development is declining in favor of monitoring. Software once shipped on CD-ROMs (bugs took years to fix); now bugs can be resolved in minutes. AI products are even less deterministic — models deprecate faster than anything in software history. There is no such thing as "stable." Speed of iteration matters above all.

> "When building an AI product, speed matters — this is more true than any industry in history."

### Claim 2: "Evals measure how good your product is"

**Hylak's rebuttal:** You wouldn't brag about unit test pass rates. Evals are **adversarially selected** — you add a failure case after you already found it, so the eval set becomes a collection of known issues. The real measure is production performance.

The core problem: evals only test what you can imagine. Production reveals what you can't. [[entities/gian-segato|Gian Segato]] (Replit's founding data scientist, now Anthropic research) confirmed that eval datasets "by definition constantly lag behind" actual user behavior — a key argument from his essay *Building AI Products In The Probabilistic Era* (see [[concepts/probabilistic-era-software]]).

> "The agents are too much to test. But not too much to monitor."

**Raindrop's alternative:** **Semantic signals** (custom tiny models trained to detect problematic patterns like looping, forgetting context, wrong language) combined with **manual signals** (thumbs up/down, deployment rates, regeneration). This creates a comprehensive view of good/bad, broken down by use case and model — essentially Hamel Husain's "error analysis" at scale.

### Claim 3: "Evals are good for rapid iteration"

**Hylak's rebuttal:** Ankur's logic is self-contradictory. He claims A/B testing is expensive because variants are hard to create, then immediately describes how AI can auto-generate 20 variants or update every 30 minutes — without explaining why this wouldn't work for A/B testing. "Weeks for results" is a straw man; A/B tests can yield answers in hours.

The critical distinction: **A/B tests on Braintrust ≠ A/B tests on Raindrop.** Braintrust's A/B tests measure latency. Raindrop tracks semantic signals and intent changes — answering *"How does X change how my agent behaves?"* with ground-truth signals from production.

> "Imagine GPT-5 drops. With Raindrop, you can route 1% of your users to GPT-5 and instantly see how it impacts frustration… With evals, you're stuck debugging old evals and trying to discover all of the new, unpredictable problems you haven't yet made evals for."

### Claim 4: "Evals for Personalized Software"

**Hylak's rebuttal:** Personalization is the **strongest rebuttal** against eval obsession. If models adapt tone/brevity/behavior per user, you'd need millions of user-specific evals — extremely expensive, slow, and still insufficient because each personalization introduces new bug surface.

The alternative: ~100 smoke-test cases to catch known regressions, then ship to a small user sample and monitor for negative signals (anomalies, user struggle, failures), cluster patterns, measure impact.

> "Or you can write 10,000,000 evals. Your choice."

## Where They Agree

Despite the heated rhetoric, both positions share common ground:

- **Evals have value** — Hylak acknowledges evals as "useful sanity checks" for preventing regressions; Raindrop itself uses a custom eval platform
- **Both are needed** — The real question is emphasis and where the truth lives, not whether evals should exist at all
- **Error analysis is fundamental** — Both cite Hamel Husain's methodology
- **Customers use both** — Many Raindrop customers also use Braintrust (as a data warehouse and prompt manager)

## Resolution: Complementary, Not Competing

The most productive framing treats evals and monitoring as **complementary layers** in the [[concepts/agent-evaluation-methodology|agent evaluation lifecycle]]:

| Phase | Tool | Approach |
|---|---|---|
| **Pre-ship** | Evals (Braintrust, LangSmith) | Golden cases, regression tests, smoke tests |
| **Post-ship** | Monitoring (Raindrop, Sentry) | Semantic signals, A/B experiments, error analysis |
| **Continuous** | Both | Evals lock in production-learned lessons; monitoring discovers new ones |

> "The truth increasingly lives in production." — but evals are the memory of bugs you refuse to reintroduce.

## Timeline

| Date | Event |
|---|---|
| Aug 2025 | Ankur Goyal speaks at AI Engineer World's Fair on "The Future of Evals" |
| Aug 2025 | Braintrust blog post claims "A/B testing is no longer sufficient… the future is evals" |
| Sep 5, 2025 | Ben Hylak publishes "Thoughts on Evals" — point-by-point rebuttal |
| May 2026 | Hylak publishes *How to Evaluate AI Agents* guide, incorporating the debate's lessons into the floor raising framework |

## Further Reading

- **[Thoughts on Evals](https://www.raindrop.ai/blog/thoughts-on-evals/)** — Ben Hylak's original rebuttal (Sep 2025)
- **[How to Evaluate AI Agents](https://www.howtoeval.com/)** — Hylak's 2026 guide synthesizing the debate's lessons
- **[Your AI Product Needs Evals](https://hamel.dev/blog/posts/eval-tools/)** — Hamel Husain on error analysis
- **[Replit's A/B Testing Blog](https://blog.replit.com/ai-ab-testing)** — Founding engineer on why eval datasets lag behind production
- **[[concepts/probabilistic-era-software]]** — Gian Segato's ontological framework: why deterministic playbooks break with AI
- **[[concepts/agent-evaluation-methodology]]** — Full lifecycle framework incorporating both perspectives
