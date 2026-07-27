---
title: "AI Adoption Failures and Enterprise AI Psychosis"
created: 2026-07-26
updated: 2026-07-26
type: concept
tags:
  - ai-adoption
  - ai-critic
  - company
  - ai-organization
  - technology-criticism
  - ai-commentary
  - coordination
  - game-theory
sources:
  - raw/articles/ludic.mataroa.blog--blog-ai-mania-is-eviscerating-global-decision-making--bc68f656.md
---

# AI Adoption Failures and Enterprise AI Psychosis

A concept describing the systemic dynamics where organizations become unable to make rational decisions about AI adoption due to a combination of hype, fear, coordination failures, and misaligned incentives. The term "AI psychosis" (attributed to Mitchell Hashimoto) captures the phenomenon where companies undergo organizational-level irrational behavior around AI investment.

## Origin

The concept was articulated in detail by the anonymous author of ludic.mataroa.blog in "AI Mania Is Eviscerating Global Decision-Making" (July 2026), a widely-shared essay linked from [[entities/daringfireball]]. The author, a consultant with extensive enterprise sales experience across 300+ professional conversations, describes observing near-universal AI project failure alongside intensifying organizational pressure to adopt AI.

Mitchell Hashimoto (of HashiCorp and Ghostty fame) provided the framing quote:

> "I strongly believe there are entire companies right now under heavy AI psychosis and it's impossible to have rational conversations with them about it."

## Key Dynamics

### 1. The Failure Rate Problem

The author reports observing **0% success rate** across all AI projects in a year and half — not just projects they participated in, but also projects observed in passing during unrelated engagements. The failure is often not about AI capabilities per se, but about:

- Companies being "terminally bad at running software projects effectively"
- AI projects inheriting all normal failure modes **plus** additional risk from methodological novelty
- Very few companies being mature enough at shipping software to absorb the extra risk

Common failure patterns include:
- **Internal chatbots**: No employee uptake because companies have low-quality documentation; LLMs can only surface what's been written down
- **Customer-facing chatbots**: Poor consumer experiences; metrics gamed to hide failures
- **Metric avoidance**: Project leaders carefully avoid tracking whether tools are being used at all

### 2. Heresy Dynamics

In organizations with 500+ employees, continued employment increasingly requires "repeated professions of belief in the transformative power of AI." This manifests as:

- **Religious profession**: Non-technicians making declarations of faith about AI's transformative power, often unable to name a single concrete change
- **AI-washing**: Engineers lying about using LLMs when their professional judgment says the tools aren't appropriate — "they just do the work the same way they have for decades and say Claude did it"
- **Token leaderboards**: Employees measured on AI API spend, leading to gaming — setting LLMs to prompt themselves in loops while the engineer watches Netflix
- **Firing heretics**: The only people fired are those who express visible doubt; no one is fired for gaming the metrics

### 3. The Demo Trap

AI demonstrations create an irresistible sales dynamic. Even when explicitly caveated as "not production-ready," demos of AI querying company data trigger buying frenzies that sweep aside all other considerations. The author describes:

> "It was like a dark and terrible force seized control of their limbs, plunged their hands into their own chests, and presented their still-beating credit cards to us in grim supplication."

The team was forced to stop demonstrating AI capabilities entirely because the response was too irrational to ethically sell into.

### 4. The Executive Coordination Problem

A game-theoretic trap prevents honest communication about AI gains:

- If an executive admits AI gains are not plausible, they undermine their customer executives' credibility (who claimed 100x productivity)
- This risks enterprise contract cancellations and personal termination
- Every vendor is in the same position — pointing guns at each other, nobody wanting to defect first
- S&P 500 board members express the same anxiety: "investing this early seems like risk without much upside" but positions are contingent on demanding AI investment

This creates a **coordination problem** where:
- Mutual cooperation (honesty) preserves jobs
- Defection (admitting truth) risks being fired
- Without coordination mechanism, everyone continues the charade

### 5. AI-Native Purity Testing

Organizations now require all initiatives to include AI alignment regardless of appropriateness:

- Database migrations are rebranded as "AI-driven" when the AI component is trivial
- Hiring policies require demonstrating AI use before requesting headcount
- Funding requests are denied or delayed until sufficiently "AI enough"
- The author's assessment: "a substantial component of the AI projects are actually non-AI projects with an AI element slapped on after the fact to pass the purity test"

## Structural Analysis

The dynamics create a self-reinforcing cycle:

```
Hype → Executive pressure → Mandated adoption → Failure → Cover-up → More hype
         ↑                                                           |
         └───────────────────────────────────────────────────────────┘
```

The author identifies this as **distributed government by assassination** — the least sensible recommendations go totally unchallenged because challenging them is career-ending.

## Comparison with Historical Parallels

| Aspect | AI Hype (2024-2026) | Blockchain Hype (2017-2021) | Cloud Hype (2010-2015) |
|--------|--------------------|-----------------------------|----------------------|
| Heresy dynamics | Severe — employment contingent on belief | Moderate — skepticism tolerated | Mild — "cloud-first" was flexible |
| Failure rate | Very high (reported 0%) | High but acknowledged | Moderate, many genuine wins |
| Executive honesty | Near-impossible (coordination trap) | Somewhat possible | Generally honest |
| Metric gaming | Pervasive (token leaderboards) | Common (TVL gaming) | Less prevalent |
| Duration of capture | Ongoing | ~4 years | ~5 years |

## Relevance to AI/LLM Ecosystem

This concept is important for understanding:

- **Why enterprise AI sales cycles behave differently** from normal technology procurement
- **Why AI vendor revenue may not reflect actual value creation** — customers buying under organizational pressure rather than rational evaluation
- **The gap between public AI productivity claims and reality** — especially from publicly traded companies
- **Why [[concepts/coding-agents]] adoption may be healthier than enterprise chatbot adoption** — developer tools face more rational evaluation because the users are technical

## Criticism and Nuance

The essay acknowledges several counterpoints:

- Some companies **are** seeing genuine gains — the author's 0% rate may reflect selection bias (they're called in when things go wrong)
- The coordination problem means some executives making absurd claims are "not as dull as they might seem" — they're in genuinely fraught political environments
- The author and Thomas Ptacek ("My AI Skeptic Friends Are All Nuts") agree on the core point even while disagreeing on AI utility: "people are being really, really stupid about this"
- Vibe coding has genuine value for non-technical people building tools — the criticism is about its misapplication to expert contexts

## Related

- [[concepts/ai-assisted-development]] — the productive alternative to both blind adoption and pure skepticism
- [[concepts/enterprise-ai-scaling-patterns]] — patterns for actually succeeding with enterprise AI
- [[entities/antirez-com]] — "Being Linux Torvalds" provides a constructive framework for AI-assisted programming (the programmer as orchestrator)
- [[concepts/vibe-coding]] — the specific AI usage pattern that becomes pathological when applied inappropriately
