---
title: "Gemini 4 Carbon"
type: concept
created: 2026-10-29
updated: 2026-10-29
tags:
  - model
  - frontier-models
  - gemini
  - google
  - deepmind
  - cybersecurity
  - long-horizon
  - code-model
  - ai-agents
  - prompt-injection
  - benchmark
confidence: medium
sources:
  - raw/articles/2026-10-28_gemini-4-carbon.md
related:
  - concepts/gemini/index
  - events/2026-10-01-gemini-4-argon-release
  - concepts/gemini/gemini-3-8-flash
  - concepts/ai-vulnerability-discovery
  - concepts/ai-benchmarks/terminal-bench
  - concepts/reward-hacking-research-agents
  - entities/deepmind
---

# Gemini 4 Carbon

**Gemini 4 Carbon** is Google DeepMind's next frontier model, announced **2026-10-28** by Koray Kavukcuoglu (SVP, GDM and Chief AI Architect, Google) — 14 days after [[events/2026-10-01-gemini-4-argon-release|Gemini 4 Argon]]. It is positioned as Google's strongest model for **cybersecurity defense and long-horizon agentic work**, and is the clearest public example so far of a "capability-gated frontier release": cyber-capable models shipped to vetted defenders first, under a voluntary U.S. government pre-release testing process.

^[[raw/articles/2026-10-28_gemini-4-carbon.md]]

> All benchmark numbers below are Google-reported and largely internal or vendor-run; the launch post does not publish an eval harness or guardrail configuration beyond the note that the three cyber numbers were "evaluated without guardrails." Treat as vendor-reported until independent reproductions land.

## Headline numbers (Google-reported)

| Metric | Score | Note |
|--------|-------|------|
| Artificial Analysis Intelligence Index v5.0 | **59** (#1) | First model to top the freshly-revived AA index (see [[concepts/benchmarking-crisis]] for why an index relaunch is itself newsworthy) |
| SEC-bench Pro (vulnerability finding) | **88.2%** (SOTA) | Real-world flaw discovery |
| ExploitGym (exploitation) | **54.8%** (new SOTA) | Validating exploitability, i.e. triage before remediation |
| CWE-bench (patching, Collinear) | **71.0%** | Up from Argon's 68% on CWE-bench v1 — see [[events/2026-10-01-gemini-4-argon-release]] |
| WebDev Arena | **1768** elo, #4 (+89) | Full-stack web dev artifact quality |
| Terminal-Bench 4.0 cheating | **0.0% success / 0.4% attempts** | Reward-hacking suppression — see [[concepts/reward-hacking-research-agents]] |
| Gray Swan Indirect Prompt Injection | **0.0%** ASR | Argon previously led at 0.7% — see [[concepts/prompt-injection]] |

## Capability claims

- **Long-horizon endurance:** Google reports internal teams running Carbon **for days** to push through dead ends on multi-step engineering work (root-causing and patching subtle bugs in large codebases, low-level systems). This is the flagship positioning shift: from "answers well" to "persists".
- **Secure code generation:** >2x uplift in success rate over Argon (internal benchmark).
- **Third-party corroboration (weak, partner-reported):** the Chrome team reportedly saw Carbon perform **>10x better than another lab's large frontier model** at generating high-quality patches; **Wiz** observes Carbon leading on web-penetration-testing benchmarks (Wiz's "Scan for Good" initiative). Both are partners, not independent evaluators.

## Alignment / safety claims

Google's framing is that Carbon goes "a step further on alignment" than Argon, with five measurable claims:

1. **Fewer shortcuts** — Terminal-Bench 4.0 cheating at 0.0% success, 0.4% attempts, *while overall accuracy improved* (the notable part: no capability trade-off claimed).
2. **Less fabrication** — unsupported claims cut ~2x vs Argon; the model is said to put methodological caveats *into the deliverable* or withhold blocked actions with an explicit list of what's still required, rather than hedging (relevant to [[concepts/ai-sycophancy]] and [[concepts/agent-trace-integrity]]).
3. **Ambiguity handling** — retrieves sources and surfaces discrepancies to the user before acting, instead of guessing.
4. **Scope discipline** — overreach −26%, under-service −29% simultaneously (i.e. it neither exceeds nor abandons multi-step plans).
5. **Prompt-injection resistance** — 0.0% ASR on Gray Swan's IPI benchmark.

"High-severity misalignment alerts" in live internal coding environments reportedly dropped ~80% versus Argon.

## Release posture: gated rollout as product strategy

Carbon follows Argon's **Fairwind Program** path: from the week of announcement, access goes to a **subset of cyber defenders**, then gradually to additional trusted partners, with the general developer/enterprise/consumer surfaces waiting on guardrail iteration. Google states it is "actively engaged in the U.S. government's voluntary process for pre-release model testing" — see [[concepts/frontier-ai-standards-body]].

This is now a repeatable two-phase pattern across the industry: ship the cyber-capable checkpoint to vetted defenders, market the benchmark lead, and defer general availability. Compare OpenAI's `gpt-5-5-cyber` gating and Gemini 3.8 Flash Cyber's Trusted Access Program ([[concepts/gemini/gemini-3-8-flash]]).

## Pricing

Identical introductory price to Argon: **$2 / 1M input, $10 / 1M output**, cached input 95% off. Post-introductory price: $4 / $20 per 1M. The "same price as last month's model" framing matters — a frontier capability step without a price step, in the middle of [[concepts/llm-price-collapse-2026]].

## Assessment

Two things are genuinely new rather than incremental:

- **The cyber-defense lifecycle is now benchmarked end-to-end** (find → validate → patch) with three named suites, and a lab is leading its launch narrative with them. The wiki previously had no pages for SEC-bench Pro, ExploitGym, or CWE-bench; see [[concepts/ai-benchmarks/agent-security-bench]] for the offensive/defensive agent eval lineage.
- **Alignment claims are being quantified as product features** (cheating rate, overreach rate, fabrication rate, IPI ASR) rather than described qualitatively in a system card. Whether these numbers are auditable is the open question — they are internal, and the only "external" numbers are partner-selected.

## Related

- [[concepts/gemini/index]] — Gemini family lineage and pricing tables
- [[concepts/ai-vulnerability-discovery]] / [[concepts/autonomous-security-agents]] — the agent-security track Carbon is competing in
- [[concepts/genie-4]] — DeepMind's Oct 27 world-model release, two days earlier (Gemini 3.8 Flash as in-the-loop guiding agent)
- [[concepts/reward-hacking-research-agents]] — the Terminal-Bench cheating-suppression claim
- [[entities/deepmind]], [[entities/google]]
