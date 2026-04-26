---
title: "George Hotz (geohot)"
tags: [- person]
created: 2026-04-24
updated: 2026-04-24
type: entity
---

# George Hotz (geohot)

**Projects:** comma.ai (Founder/CEO), tinygrad (Creator), tiny corp (Founder)  
**GitHub:** [github.com/geohot](https://github.com/geohot)  
**Blog:** [geohot.github.io](https://geohot.github.io/) — "the singularity is nearer"  
**Notable:** First to iPhone-unlock (2007), first to PS3-root (2010)

## Overview

George Hotz (geohot) is a hacker, entrepreneur, and software engineer best known for being the first person to carrier-unlock the iPhone and hack the PlayStation 3. He founded **comma.ai** in 2015 to build open-source advanced driver assistance systems (ADAS), competing with Tesla's autonomous driving efforts. He also created **tinygrad**, a minimalist deep learning framework, and founded **tiny corp** to support it.

Hotz is known for his irreverent, contrarian style and his belief that most software is bloated, most AI research is overcomplicated, and that elegant minimal solutions will ultimately win.

## Core Ideas

### The Bitter Lesson Applied to Software

Hotz extends Rich Sutton's "Bitter Lesson" beyond AI to software engineering itself. His thesis: **simple solutions that leverage raw computation will beat complex, hand-optimized ones**. This applies to:

- **tinygrad**: A deep learning framework in ~15,000 lines that replaces PyTorch + CUDA + complex build systems
- **comma.ai**: End-to-end neural net driving vs. the traditional perception-planning-control pipeline

> "The bitter lesson is that the best approach is the one that leverages computation, not the one that encodes human knowledge."

### Commoditizing Compute

Hotz believes compute should be a commodity, not a moat. His work at tiny corp is explicitly aimed at **democratizing AI training**:

- tinygrad runs on any hardware (GPU, CPU, custom accelerators)
- It has minimal dependencies — essentially pure Python
- The goal: make training large models accessible to anyone, not just companies with massive infrastructure budgets

> "We're building the tools so that you don't need a $100M compute budget to train a competitive model."

### Openpilot and the Open-Source ADAS Revolution

comma.ai's flagship product, **openpilot**, is an open-source driver assistance system that works in many car makes and models. Hotz's philosophy:

- **Open source everything** — the community improves the system faster than any closed team could
- **Data-driven approach** — collect real driving data, train neural nets on it, iterate
- **Challenge Tesla** — prove that a small team with open-source tools can compete with a massive corporate effort

> "The best way to make self-driving cars is to just drive. Collect data, train models, ship updates. Everything else is a distraction."

### Anti-Bloat and Minimalism

Hotz is a vocal critic of software bloat. His key arguments:

- **Most software is 10-100x larger than it needs to be** due to layers of abstraction, legacy compatibility, and over-engineering
- **tinygrad proves this** — a full deep learning framework in ~15k lines vs. PyTorch's millions
- **The solution**: strip away abstractions, understand the fundamentals, rebuild from first principles

> "Software has lost its way. We've built towers of abstraction on towers of abstraction, and nobody understands the whole system anymore. tinygrad is my attempt to show that you don't need all that."

### AI Infrastructure as the Real Bottleneck

Hotz argues that the biggest constraint on AI progress isn't model architecture or algorithms — it's **infrastructure**:

- **Compute access** is concentrated in a few companies (OpenAI, Google, Meta, Anthropic)
- **Training pipelines** are opaque and proprietary
- **The solution**: open-source tools that let anyone train and deploy models

His work on tinygrad and comma.ai's training infrastructure is aimed at breaking this bottleneck.

### Contrarian Views on AI Safety

Unlike many AI researchers, Hotz is **skeptical of AI safety concerns**:

- He views most AI safety research as "solving problems that don't exist yet"
- He believes the real risk is **concentration of AI power** in a few companies, not superintelligence
- He advocates for **open-source AI** as the best defense against centralized control

> "The people worried about AI safety are worried about the wrong thing. The real danger is that a few companies control all the AI."

## Key Quotes

> "The bitter lesson is that the best approach is the one that leverages computation, not the one that encodes human knowledge."

> "We're building the tools so that you don't need a $100M compute budget to train a competitive model."

> "The best way to make self-driving cars is to just drive. Collect data, train models, ship updates."

> "Software has lost its way. We've built towers of abstraction on towers of abstraction."

> "The people worried about AI safety are worried about the wrong thing. The real danger is that a few companies control all the AI."

## Recent Themes (2023–2026)

- **tinygrad maturity** — Moving from a proof-of-concept to a production-ready deep learning framework
- **comma.ai openpilot adoption** — Growing user base and community contributions to the open-source ADAS system
- **AI infrastructure democratization** — Advocating for open-source tools that break compute monopolies
- **Anti-bloat software engineering** — Proving that minimal, elegant solutions can compete with complex systems
- **Contrarian AI safety views** — Skepticism toward centralized AI governance and alignment research
- **tiny corp expansion** — Building a small team to continue developing open-source AI infrastructure
- **OpenAI response (Apr 2026)** — Published "OpenAI is nothing without its people" as a response to Sam Altman's blog, arguing for open-source AI and against "neofeudalism" of closed labs
- **Molochian tragedy of the commons** — Fears not "great men" but the accumulation of small self-interested decisions that degrade collective outcomes
- **Closed Source AI = Neofeudalism (Mar 2026)** — Argued that API access without weight sharing is feudalism; "Science never credits the first guy who came up with an idea, it credits the guy who published"
- **Every minute you aren't running 69 agents (Mar 2026)** — Walked back hype rhetoric: "AI is not a magical game changer, it's simply the continuation of exponential progress"
- **Two Worlds (Mar 2026)** — Capability vs. value distinction: "AI can keep getting better super fast, but the value of anything it produces by itself is low"
- **zappa: AI-powered mitmproxy (Apr 2026)** — Vibe-coded an AI proxy using GPT-5.4 that intercepts web traffic via mitmproxy, routes it through Qwen (Cerebras API), strips ads/popups/enshittification, and returns clean pages. Advocates for shipping as a browser extension with customizable prompts, and making it agentic with per-site state. "Don't fall for AI browser crap that's marketed to you, that's just them wanting to control your attention better. You need an AI you can trust to fight back!"

## Related

- [[john-carmack]] — Also skeptical of mainstream AI approaches; focused on efficiency and practical results
- [[grant-slatton]] — AI alignment and technocapital; contrasting views on AI governance and open-source
- [[jayden-milne]] — AI culture and society; Hotz is more infrastructure-focused, Milne more culture-focused
-  — Open-source ADAS company competing with Tesla's FSD
-  — Minimalist deep learning framework
-  — Rich Sutton's essay that heavily influences Hotz's philosophy

## Sources

- geohot.github.io blog — "the singularity is nearer"
- comma.ai / openpilot documentation and releases
- tinygrad GitHub repository and documentation
- Various podcasts and interviews (2023–2025)
- Hacker News discussions on tinygrad and comma.ai
