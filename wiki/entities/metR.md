---
title: METR
type: entity
created: 2026-08-25
updated: 2026-08-25
tags:
  - lab
  - ai-research
  - research-lab
  - evaluation
url: https://metr.org/
sources:
  - https://metr.org/notes/2026-08-14-llm-contribution-to-discoveries/
---

# METR (Model Evaluation & Threat Research)

**METR** is an independent research lab focused on evaluating AI capability, safety, and the pace of AI-driven progress. It publishes empirical studies on how quickly AI systems are advancing across domains and how that translates to real-world utility — a key resource for the [[concepts/evaluation/ai-evals]] and [[concepts/ai-safety]] conversations.

METR has contributed to several benchmark and evaluation threads in this wiki (e.g. RE-Bench, the RAM relative-adoption metric, and Epoch AI × METR long-horizon programming benchmarks).

## Key 2026 Output

### "Have We Seen an Acceleration in Discoveries?" (Aug 14, 2026)
Tom Cunningham & Nate Rush published a study mapping where LLM contribution to *discoveries* (any advance in the state of public knowledge) is actually showing up, comparing three domains: **cyber security, mathematics, and algorithmic optimization**. The headline is **differential acceleration** — lumpy, domain-specific acceleration rather than a uniform lift:

- **Cyber vulnerabilities: major acceleration** — reported-vulnerability rate "dramatically accelerated" in 2026 vs 2025 across cURL, OpenSSL, Firefox, Microsoft, and aggregate DBs (US NVD, OSV). Databases of *exploited* vulns (CISA, Vulncheck KEVs) grow far slower than *known* vulns → discovery is outpacing exploitation.
- **Mathematics: minor acceleration, hard to measure** — three problems from curated open-problem lists solved with AI in 2026 (Jacobian conjecture from Smale's list; Green's Problem 44 "halving sieve"; the sofic half of Green's Problem 100); arXiv submissions doubled in some areas in <12 months.
- **Algorithmic optimization: no measurable acceleration** — no clear slope change across CIFAR-10, Hutter compression, Gurobi MIP, MIPLIB, nanoGPT, Stockfish, and the matrix-multiplication exponent.

Candidate explanations: variation in inference expenditure, variation in LLM difficulty per domain, variation in disclosure (confidentiality of AI progress), and variation in data quality. Conclusions are based on **public** discoveries only.

→ Full details: [[concepts/ai-discovery-acceleration]]

## Why it matters
METR's differential-acceleration framing (some domains accelerate, others don't) is a recurring theme in frontier-lab and policy discussion — it undercuts both "AI accelerates everything uniformly" and "AI hasn't accelerated anything" narratives. See also [[concepts/scaling-laws]] and [[concepts/intelligence-explosion]].

## Related Pages
- [[concepts/ai-discovery-acceleration]] — the differential-acceleration finding
- [[concepts/evaluation/ai-evals]] — evaluation methodology
- [[concepts/recursive-self-improvement]] — RSI
- [[concepts/ai-safety]] — AI safety

## Sources
- METR note: [Have We Seen an Acceleration in Discoveries?](https://metr.org/notes/2026-08-14-llm-contribution-to-discoveries/) (Cunningham & Rush, 2026-08-14)
- Discussed in Import AI 470 (Jack Clark, 2026-08-24)
