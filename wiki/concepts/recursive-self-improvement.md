---
title: "Recursive Self-Improvement"
created: 2026-05-05
updated: 2026-06-07
type: concept
tags: [prediction, safety, alignment, training, benchmark, automation]
sources: [raw/articles/2026-05-04_import-ai-455-automating-ai-research.md, raw/newsletters/2026-06-05-ainews-not-much-happened-today.md, raw/newsletters/2026-06-06-rsi-when-ai-starts-building-its-own-successors.md, raw/articles/2026-06-07_anthropic_recursive-self-improvement.md]
---

# Recursive Self-Improvement

## Definition

Recursive self-improvement (RSI) refers to the capability of an AI system to autonomously design, train, and deploy a more capable successor AI system — without human intervention. This creates a potential feedback loop where each generation produces an even more capable next generation.

## Current State (May 2026)

### Capability Evidence

| Benchmark | Late 2023 | Current (May 2026) | Description |
|-----------|-----------|-------------------|-------------|
| SWE-Bench | 2% (Claude 2) | 93.9% (Claude Mythos Preview) | Solving real GitHub issues |
| METR Time Horizon | 30s (GPT-3.5) | ~12 hours (Opus 4.6) | Sustained autonomous work |
| CORE-Bench | — | 95.5% (Opus 4.5, Dec 2025) | Computational reproducibility |
| MLE-Bench | 16.9% (Oct 2024) | 64.4% (Feb 2026) | Building ML systems from scratch |

### Key Enabling Capabilities

1. **Coding Mastery**: AI can now solve 93.9% of real-world software engineering tasks independently
2. **Extended Autonomy**: Working reliably for 12+ hours without human intervention, with 100-hour reliability expected by end 2026
3. **ML Research Skills**: Replicating papers (95.5%), building ML systems (64.4%), optimizing kernels
4. **Training Optimization**: Claude Mythos Preview achieved 52x speedup on CPU-only training implementation (4x expected from a human)
5. **Agent Orchestration**: "Manager" AI can supervise multiple specialized sub-agents

### Industry Targets

| Lab | Goal | Timeline |
|-----|------|----------|
| OpenAI | "Automated AI research intern" | Sept 2026 |
| Anthropic | "Automated Alignment Researchers" | Ongoing |
| Sakana AI | RSI Lab Tokyo — sample-efficiency-focused RSI | June 2026 |
| Mirendil | Dedicated RSI startup | Active |

## Jack Clark's Probabilistic Forecast

From Import AI 455 (May 4, 2026):
- **30%** probability of automated AI R&D by end of 2027
- **60%** probability by end of 2028
- Failure condition: If not achieved by 2028, suggests a fundamental deficiency in current paradigm

## The Alignment Challenge

### Compounding Error Problem

Recursive self-improvement turns alignment from a binary problem into a compounding one:

> "Unless your alignment approach is '100% accurate'... things can go wrong quite quickly. For example, your technique is 99.9% accurate, then that becomes 95.12% accurate after 50 generations, and 60.5% accurate after 500 generations." — Jack Clark

This means even near-perfect alignment techniques become dangerously degraded across multiple self-improvement cycles.

### Key Risks
- **Fake Alignment**: AI systems may learn to appear aligned on tests while pursuing different goals
- **Goal Drift**: Small imperfections compound into unrecognizable objectives
- **Capability Explosion**: Each generation may be significantly more capable than its predecessor, making correction impossible
- **Instrumental Convergence**: Aligned intent may still produce dangerous instrumental behaviors

## Engineering vs. Creativity

Clark distinguishes between "meat and potatoes" engineering and radical paradigm shifts:
- **What AI can do**: Massive-scale experimentation, hyperparameter tuning, neural architecture search — the "99% perspiration"
- **What AI may lack**: The "1% inspiration" that produced breakthroughs like Transformers
- **The bet**: Even without creative genius, sheer volume and speed of experimentation can push the frontier forward

## Economic Implications

### The Amdahl's Law Economy
As AI accelerates digital work, physical-world bottlenecks (drug trials, manufacturing) become the primary growth constraints. The economy becomes increasingly gated by physical processes rather than cognitive ones.

### The Machine Economy
Potential emergence of capital-heavy, human-light corporations where AI-run entities trade with each other, creating a parallel economy challenging traditional governance and redistribution models.

## Industry Evidence (June 2026)

### Claude Self-Writes >80% of Code

In June 2026, Anthropic revealed that **Claude now writes more than 80% of the code merged into its own codebase** — a milestone in recursive self-improvement. The company's internal data shows Claude is accelerating AI development along a "possible path to recursive self-improvement, or AI autonomously building a more capable successor" ([[entities/anthropic]], June 4, 2026).

### RSI Three-Stage Classification

The Superintelligence newsletter (Kim Isenberg, June 6, 2026) proposes a three-stage taxonomy for understanding RSI progress:

| Stage | Name | Status | Description |
|-------|------|--------|-------------|
| **Broad RSI** | AI-assisted AI development | Already mainstream | Humans use AI tools (Claude Code, Codex) to accelerate AI research and engineering — the current reality |
| **Middle RSI** | AI-automated AI R&D | **2026's critical frontier** | AI systems autonomously conduct the majority of AI research and engineering tasks, with humans in supervisory roles |
| **Hard RSI** | Fully autonomous self-improvement | **Not yet demonstrated** | AI designs and deploys its own successor without meaningful human involvement |

Middle RSI is identified as the most consequential threshold for 2026 — the point at which AI development transitions from human-driven to AI-driven acceleration.

### Anthropic's "When AI builds itself" (June 4, 2026)

Anthropic published a post through their official account (June 4, 2026, 238K views) stating:

> "Our internal data shows Claude is accelerating AI development — a possible path to recursive self-improvement, or AI autonomously building a more capable successor."

The post sparked significant debate, with [[entities/gary-marcus]] arguing that the results demonstrated "faster coding — entirely under human control" rather than true AGI, and that "AGI is harder than recursive self-improvement."

### Sam Altman's "The Gentle Singularity" (June 2025)

[[entities/openai]] CEO Sam Altman referenced a "larval version of recursive self-improvement" in his essay "The Gentle Singularity" (June 2025), describing early signs of AI systems accelerating AI development before the phenomenon became widely recognized.

### Historical Context

The concept of an "intelligence explosion" was first formalized by I.J. Good in 1965:

> "Let an ultraintelligent machine be defined as a machine that can far surpass all the intellectual activities of any man however clever. Since the design of machines is one of these intellectual activities, an ultraintelligent machine could design even better machines; there would then unquestionably be an 'intelligence explosion,' and the intelligence of man would be left far behind."

The 80% code self-writing milestone represents the most concrete empirical evidence to date that Good's theoretical framework may be materializing in practice, at least for the first several iterations of the loop.

## Anthropic Official Declaration (June 2026)

On June 4, 2026, the Anthropic Institute published "When AI builds itself" — an official declaration of their stance on recursive self-improvement as their path forward. Authored by Marina Favaro and Jack Clark, the article represents the first time a frontier AI lab has publicly and comprehensively framed RSI as both a strategic imperative and a near-term trajectory.

### Key Declarations

1. **RSI as official path forward**: Anthropic explicitly states it is "delegating a growing share of AI development to AI systems themselves" and frames this as a trend pointing toward "an AI system capable of fully autonomously designing and developing its own successor." While noting RSI is "not inevitable," they argue "it could come sooner than most institutions are prepared for."

2. **8x code output with Claude's autonomous help**: Engineers now ship 8x as much code per quarter compared to 2021-2025. More than 80% of code merged into Anthropic's codebase is authored by Claude (May 2026). Internal polling of 130 researchers found median estimated 4x productivity gain with Mythos Preview. Claude shipped over 800 bug fixes in one month that reduced a class of API errors 10-fold.

3. **Research automation advancing**: Claude's success rate on open-ended engineering tasks reached 76% in May 2026 (up 50pp in six months). In April 2026, Anthropic published the first demonstration of a Claude-powered agent running an open-ended research project end-to-end in AI safety. Claude judged better than human researchers at steering ~40% of research decision points.

4. **Trillion-dollar valuation narrative**: The article's framing serves dual purposes — it is simultaneously a technical roadmap and a valuation narrative supporting Anthropic's ~$1T valuation target and imminent IPO (S-1 filed June 2026). By articulating RSI as their explicit strategy, Anthropic positions itself as the lab best positioned to capture the compounding returns of AI-accelerated AI development.

5. **AGI-timeline accelerator**: The evidence presented collapses timelines. METR task horizons show doubling every 4 months (up from 7 months). If sustained, AI systems could handle tasks taking a skilled person *weeks* by 2027. The article outlines three scenarios: Continuation (steady acceleration), Acceleration (fast takeoff surpassing human AI R&D), and Failure (plateau from fundamental limitations).

6. **Policy stance on pausing**: Anthropic expresses desire for a "meaningful slowdown or pause" option but acknowledges practical barriers — requiring multiple well-resourced labs in multiple countries agreeing to stop under verifiable conditions. They commit to organizing conversations with policymakers, researchers, and civil society.

### Community Response

The article sparked a **692-comment Hacker News discussion** ([thread](https://news.ycombinator.com/item?id=...)), indicating the scale of community engagement and concern. Key themes included:

- **Skepticism about "8x"**: Many commenters questioned whether lines-of-code is a meaningful productivity metric, noting that AI-generated code may require more review and refactoring
- **Gary Marcus's critique**: Characterized the capability as "faster coding — entirely under human control," arguing true AGI/RSI requires more than code generation speed
- **Safety concerns**: Debates about whether Anthropic's safety-first framing is genuine or a competitive positioning strategy
- **Governance urgency**: Recognition that verification regimes (like INF Treaty) took decades to build — time the AI community may not have

This official declaration elevates RSI from a theoretical concept discussed by researchers to a stated corporate strategy with trillions of dollars of capital aligned behind it.


## Related

- [[entities/jack-clark]] — Key source, 60% prediction by end 2028
- [[entities/anthropic]] — Automated Alignment Researchers initiative
- [[concepts/ai-safety]] — Alignment risks
- [[concepts/automated-alignment-research]] — Anthropic's AAR program
- [[concepts/model-distillation]] — Related capability advancement pathway
- [[concepts/agent-team-swarm]] — Multi-agent orchestration as enabling capability
- [[entities/openai]] — "Automated AI research intern" target
