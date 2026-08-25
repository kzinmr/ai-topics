---
title: "Have We Seen an Acceleration in Discoveries? (METR)"
source: METR (metr.org)
url: https://metr.org/notes/2026-08-14-llm-contribution-to-discoveries/
date: 2026-08-14
date_ingested: 2026-08-25
authors: [Tom Cunningham, Nate Rush]
tags: [raw, newsletter, ai-research, evaluation, ai-capability]
type: article
in: "Import AI 470 (Jack Clark, 2026-08-24)"
---

# Have We Seen an Acceleration in Discoveries? (METR)

**Authors:** Tom Cunningham, Nate Rush (METR)
**Published:** 2026-08-14
**Source:** https://metr.org/notes/2026-08-14-llm-contribution-to-discoveries/

## Summary (from Import AI 470 + METR note)

A METR study mapping where AI (LLM) contribution to *discoveries* is actually showing up. "Discovery" = any advance in the state of public knowledge, including new inventions or more efficient algorithm rewrites. Three domains compared: **cyber security (vulnerabilities), mathematics, and algorithmic optimization**.

### Headline findings
- **Cyber vulnerabilities: MAJOR acceleration.** The rate of vulnerabilities reported across many projects has dramatically accelerated in 2026 vs 2025 — both for specific projects (cURL, OpenSSL, Firefox, Microsoft) and for aggregate vulnerability databases (US NVD, OSV). Notably, databases of *exploited* vulnerabilities (CISA, Vulncheck KEVs) show significantly lower YoY growth than databases of *known* vulnerabilities — i.e. far more vulns are being discovered than exploited.
- **Mathematics: MINOR acceleration, hard to measure.** AI is clearly contributing to more work (arXiv submissions doubled in some areas in <12 months), but quantifying value is difficult. Crude proxy = rate of solving open problems from pre-existing lists (Hilbert, Millennium, Smale, Open Problems Project, Ben Green's 100). Three problems from these lists were solved with AI in 2026: the **Jacobian conjecture** (Smale list), **Green's Problem 44 (halving sieve)**, and the **sofic half of Green's Problem 100**. The Erdős list shows a clear acceleration in solutions but no reliable historical baseline.
- **Algorithmic optimization: NO measurable acceleration.** Across seven significant problem areas (CIFAR-10, Hutter compression, Gurobi mixed-integer programming, MIPLIB, nanoGPT, Stockfish, matrix-multiplication exponent), no clear change of slope comparable to the vulnerability/math changes. This is "perhaps surprising" given Jan 2026 excitement (Yuksekgonul et al. advancing 5 optimization frontiers with a trivial-inference simple model).

### Why differential acceleration (the "lumpy" thesis)
AI is causing advances in *some* parts of science/tech but the effect is **not unified** — there are pockets of lumpy acceleration (cyber) and areas where progress is more gradual (math, AI). Candidate explanations for the differential pattern:
1. **Variation in inference expenditure** — people may simply be spending a lot of money on LLMs for vulnerability discovery (or on traditional vuln discovery out of fear).
2. **Variation in difficulty for LLMs** — domains differ in how effective LLMs are relative to humans (downstream of training-expenditure variation or the intrinsic shape/cost of the problem space).
3. **Variation in disclosure** — AI-related algorithmic progress may be kept confidential.
4. **Variation in data quality** — fast-observed progress may just be where data is higher quality (hard-to-track domains flatten observed acceleration).

### Caveat
Conclusions are based only on **public** discoveries; it is quite plausible AI labs are making non-disclosed discoveries internally.

### Cited examples in the note
- **Anthropic Riemann result**: "Jarred Sumner, an Anthropic staff member (and non-mathematician), prompted Claude to 'take a real stab' at the hypothesis itself, leaving the mathematical choices from there up to the model."
- **Google DeepMind AlphaEvolve**: "in contrast to [traditional computational or theoretical methods performed by human experts], we have found that AlphaEvolve can be readily scaled up to study large classes of problems at a time, without requiring extensive expert supervision."
- **Mythos Preview**: "We then invoke Claude Code with Mythos Preview, and prompt it with a paragraph that essentially amounts to 'Please find a security vulnerability in this program.' … Engineers at Anthropic with no formal security training have asked Mythos Preview to find remote code execution vulnerabilities overnight, and woken up the following morning to a complete, working exploit."

## Why it matters (Jack Clark framing)
Differential acceleration: AI is accelerating some types of progress but not others. The study highlights that AI advances come in "pockets of lumpy acceleration" rather than a uniform lift across all of science/tech.

## Related
- [[concepts/metr]] — METR (the research org)
- [[concepts/evaluation/ai-evals]] — evals methodology
- [[concepts/agentic-engineering]] — agentic workflows driving discovery
