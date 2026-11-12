---
title: AI Discovery Acceleration (METR Differential Acceleration)
type: concept
created: 2026-08-25
updated: 2026-11-12
tags:
  - ai-research
  - evaluation
  - ai-in-science
  - mathematics
  - cybersecurity
sources:
  - raw/articles/2026-08-14_metr_have-we-seen-an-acceleration-in-discoveries.md
  - https://metr.org/notes/2026-08-14-llm-contribution-to-discoveries/
---

# AI Discovery Acceleration (METR Differential Acceleration)

**"Differential acceleration"** is METR's finding (Cunningham & Rush, 2026-08-14) that AI is **not** accelerating all of science/technology uniformly. Instead, advances come in **lumpy pockets**: some domains (cyber security) are accelerating sharply, while others (algorithmic optimization) show little or no measurable change. This nuance is a recurring theme in frontier-lab and policy discussion — it undercuts both "AI accelerates everything" and "AI hasn't accelerated anything" narratives.

## Three-Domain Comparison

| Domain | Finding | Evidence |
|--------|---------|----------|
| **Cyber security (vulnerabilities)** | **MAJOR acceleration** | Reported-vuln rate "dramatically accelerated" 2026 vs 2025 — cURL, OpenSSL, Firefox, Microsoft; aggregate DBs (US NVD, OSV). *Exploited*-vuln DBs (CISA, Vulncheck KEVs) grow far slower → **discovery outpacing exploitation** |
| **Mathematics** | **MINOR acceleration, hard to measure** | 3 curated-list problems solved with AI in 2026 (Jacobian conjecture — Smale list; Green's Problem 44 "halving sieve"; sofic half of Green's Problem 100); arXiv submissions doubled in some areas in <12 months; Erdős list shows clear but un-baselineable acceleration |
| **Algorithmic optimization** | **NO measurable acceleration** | No slope change across CIFAR-10, Hutter compression, Gurobi MIP, MIPLIB, nanoGPT, Stockfish, matrix-multiplication exponent — despite Jan 2026 excitement (Yuksekgonul et al.) |

## Why Differential? (Candidate Explanations)
METR lists four drivers for the lumpy pattern:
1. **Variation in inference expenditure** — money poured into LLM-based vulnerability discovery (or traditional vuln discovery out of fear).
2. **Variation in LLM difficulty per domain** — some problem shapes are intrinsically easier/costlier for LLMs.
3. **Variation in disclosure** — AI-related algorithmic progress may be kept confidential.
4. **Variation in data quality** — fast-observed progress may just be where data is higher quality; hard-to-track domains flatten observed acceleration.

**Caveat:** findings are based on **public** discoveries only; labs may be making non-disclosed internal progress.

## Cited Examples
- **Anthropic / Riemann**: Jarred Sumner (non-mathematician, Anthropic) "prompted Claude to 'take a real stab' at the hypothesis itself."
- **Google DeepMind AlphaEvolve**: "readily scaled up to study large classes of problems at a time, without requiring extensive expert supervision."
- **Mythos Preview**: Claude Code prompted with "find a security vulnerability in this program" → overnight RCE exploit with no formal security training.

## Why it matters
- **Policy / capability forecasting**: acceleration is domain-specific, so "time horizon to AGI" or "when will X be solved" estimates must be domain-conditional.
- **Security**: the exploited-vs-known vulnerability gap means the attack surface is growing faster than defenders are patching — a [[concepts/security-and-governance/ai-safety]] and [[concepts/cybersecurity]] concern.
- **Evals methodology**: measuring "discovery" velocity requires domain-appropriate baselines (pre-existing problem lists, record-setting benchmarks), not a single universal metric.

## Case study: 48 agents "rediscover" an unmapped Maya site (Nov 2026)

Pietro Miotti, a Google engineer, published *"My AI Agents (Re)discovered a Maya Site in 72 Hours"* (Nov 11; HN 999 pts / 369 c) — currently the most-cited example of agents producing a *discovery-shaped* result in the sciences, and also the most instructive about how such claims degrade.

What happened: after reading about Bingham's accidental finding of Machu Picchu, he brainstormed with Gemini/ChatGPT/Claude/Grok, which all suggested lidar. He pointed **48 agents at ~1,200 km² of public NASA lidar strips over Maya jungle, converted to images, and had them visually screen for pyramids, platforms and plazas** — "no special model or classifier involved: the agents literally looked at the pictures, following a precise guide." They flagged many village-shaped candidates, then cross-checked literature and archives and reported one major unregistered village: a cliff-edge hilltop with a levelled plaza, an 8–12 m oval pyramid, a raised courtyard and a possible reservoir. INAH checked its register and replied that **no archaeological site is registered at that location**. Total elapsed time from idea to official government reply: under 72 hours.

The correction, added the same day: the site **had already been mapped in Estrada-Belli et al. 2025** — the agents missed it in the literature, so they *rediscovered* rather than discovered it; it was only absent from the INAH register. The author's own update leads with this.

Thread value: (a) [traches] separates the defensible core (LIDAR is measured data; human-made structures are visible; the state said "not registered") from the speculative gloss (what kind of site it was); (b) [runarberg] surfaced the prior-discovery link (HN item 50453616); (c) [chirau] and [eks39x] flag the verification asymmetry — a non-archaeologist submitting to a national authority after "only chatting with the agents," and the social difficulty of experts contradicting "a Google engineer and his 48 agents"; (d) [myrmidon] gives the steelman — manually combing thousands of km² of lidar against existing site registers was never realistic for PhD students, "LLMs have turned this into low-hanging fruit"; (e) [piltdownman] warns the academic response may be gatekeeping, citing the Dead Sea Scrolls monopoly.

Methodological lesson for this page: the *screening* step was genuinely agentic and genuinely scarce (48 patient visual reviewers), and the *literature-check* step is exactly where the failure occurred — the same reliability split seen in citation-quality studies. Discovery claims should be graded per-stage, not holistically.
## Related Pages
- [[entities/metR]] — the publishing lab
- [[concepts/evaluation/ai-evals]] — evaluation methodology
- [[concepts/scaling-laws]] — scaling dynamics
- [[concepts/intelligence-explosion]] — time-horizon / AGI forecasting
- [[concepts/recursive-self-improvement]] — RSI
- [[concepts/cybersecurity]] — vulnerability discovery vs exploitation

## Sources
- [METR — Have We Seen an Acceleration in Discoveries?](https://metr.org/notes/2026-08-14-llm-contribution-to-discoveries/) (Cunningham & Rush, 2026-08-14)
- Raw article: `raw/articles/2026-08-14_metr_have-we-seen-an-acceleration-in-discoveries.md`
- Discussed in Import AI 470 (Jack Clark, 2026-08-24)
