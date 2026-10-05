---
title: "Harness Tax"
created: 2026-10-04
updated: 2026-10-05
type: concept
tags:
  - concept
  - harness-taxonomy
  - harness-engineering
  - coding-agents
  - ai-agents
  - cost-optimization
  - token-economics
  - agent-economics
  - evaluation
sources:
  - raw/articles/2026-09-16_arena-ai_harnesstax-coding-agents-harness-tax.md
aliases:
  - harness-tax
  - HarnessTax
---

# Harness Tax

**Harness tax** is the hidden cost premium paid when a coding agent's [[concepts/harness-engineering/agent-harness|harness]] (system prompt, tool schemas, scaffolding) consumes tokens and adds overhead without improving task success. Two independent usages have converged on the term:

1. **Colloquial origin** — Portkey engineer Siddharth Sambharia's April 2026 post ["The Harness Tax: The Dead Weight Inside Your Coding Agent"](https://portkey.ai/blog/the-harness-tax/): Claude Code used 83k tokens to write a Fibonacci script where Pi used 8k. Same task, same output — the difference is harness dead weight.
2. **Formal study** — **HarnessTax** (Pan et al., UC Berkeley / Sky Computing Lab, Sept 2026), the first systematic cross-harness cost/success evaluation, published as an Arena.ai research post with a public site at [harnesstax.github.io](https://harnesstax.github.io/) and promised profiling traces.

## HarnessTax study (Pan et al., 2026)

**Setup:** 21 model–harness pairs (7 models × Claude Code / Codex CLI / Pi), 30 randomly sampled tasks each from SWE-bench Lite and Terminal-Bench 2.0, 3 runs per task, high-effort native configs, capped at 100 agent turns. Cost computed from a fixed direct-API price list (Sept 1, 2026) applied identically across harnesses; 95% CIs via 10,000 bootstrap resamples. Network blocked and web tools disabled for SWE-bench Lite. Kimi K3 accessed via Fireworks AI.

### Finding 1: Harness affects cost more than correctness

- Same model, similar success rate, **up to 5× different cost**.
- Claude Fable 5: 97.8% solve rate in Claude Code vs 96.7% in both Codex and Pi — but Claude Code costs ~2× Pi ($1.33 vs $0.67).
- Geometric-mean cost ratios: Claude Code ≈ **2.0× Pi and 1.6× Codex** on SWE-bench Lite; **1.5× Pi** on Terminal-Bench 2.0.
- Average harness effect on success: **±2%** (SWE-bench Lite), **±5%** (Terminal-Bench 2.0).
- GPT-5.6 Luna = lowest cost on both benchmarks; Kimi K3 (open-weight) near the Pareto frontier.

### Finding 2: A simple harness can be competitive

- **Pi reaches the Pareto frontier on both benchmarks with only four tools** (read, write, edit, bash) — supporting the [[concepts/coding-agents/minimal-coding-agent|minimal coding agent]] and [[concepts/harness-commoditization|harness commoditization]] theses with hard cost data.
- Turn counts are similar (Fable 5: 15.4 vs 15.3 turns per attempt in Pi vs Claude Code) — the tax is **spending per turn**, not extra turns.
- **The tax begins at the first model call**: Claude Code's mean initial context is **>10× Pi's** (longer instructions, larger tool schemas).

### Finding 3: Models perform outside their provider's harness

- An *alternative* harness achieved the highest observed success in **9 of 12** model×benchmark comparisons (six Anthropic/OpenAI models × two benchmarks).
- Sonnet 4.6: 68.9% in Codex vs 66.7% in Claude Code (SWE-bench Lite, similar cost). GPT-5.6 Sol: 83.3% in Pi vs 78.9% in Codex on Terminal-Bench 2.0, at half the cost ($0.42 vs $0.76).
- Implication: model capability is **generalizable across harnesses**; provider co-optimization ("GPT-5-Codex optimized for Codex") does not guarantee the best pairing.

## Limitations (per the authors)

Two open-source benchmarks the models may have seen in training; turn definitions differ across harnesses; results may differ on other workloads. Richer harness features may still pay off for other models/settings.

## Related "tax" concepts

The Harness Tax is one of several quantified agent-overhead concepts:

| Concept | Overhead measured | Source |
|---|---|---|
| **Harness Tax** | Cost delta across harnesses at equal success | Arena.ai / Portkey |
| [[concepts/harness-engineering/agent-execution-tax\|Agent Execution Tax]] | Wasted inference from structured-output failures | Fireworks AI |
| Hidden technical debt of agent harnesses ([[entities/hanchunglee]]) | Long-run maintenance cost of harness complexity | Lee Hanchung |

## Why it matters

- **For users**: accepting a coding agent's default harness without comparison means paying an invisible premium; [[concepts/ai-coding-cost-optimization|cost optimization]] should include harness selection.
- **For benchmarking**: model evaluations should report cost × success **across harnesses**, not per-provider scaffolding only — see [[concepts/coding-agents/evaluation-coding-agents|evaluating coding agents]] and [[concepts/coding-agent-harness-design-study|the harness design ablation study]] (Fan et al.), which independently found bash-capable models do fine with minimal tool interfaces at lower cost.
- **For harness design**: complexity should be an *empirical trade-off*, not a default; the authors envision harnesses that adapt cost/structure as tasks unfold.

## Independent corroboration (Unreal Agent, Sept 2026)

[[concepts/unreal-agent]] — a third-party harness built on the thesis "the harness must not waste the model's context" — reaches **84.0 on Terminal-Bench 2.1 / 72.7 DeepSWE with the same GPT-6 Sol xhigh** model that Codex scores 79.3 / 69.4 with. Same weights, +4.7 pt and +2.1 pt, attributed to tool-call architecture rather than prompt tuning. Two independent measurements bracket the same conclusion from opposite sides: HarnessTax measures **cost at equal success**, Unreal measures **success at equal cost**. At fixed model weights the harness is the variable worth ablating.

## See also

- [[concepts/harness-engineering/agent-harness]] — what a harness is
- [[concepts/harness-commoditization]] — thesis that harness differentiation is disappearing
- [[concepts/coding-agents/minimal-coding-agent]] — the 4-tool minimal pattern
- [[entities/pi]] — the minimal open-source harness used in the study
- [[concepts/bitter-lesson-harnessing]] — "let the model do it" argument
- [[entities/arena-ai]] — sponsor/publisher of the study
