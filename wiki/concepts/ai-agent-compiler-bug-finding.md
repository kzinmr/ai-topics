---
title: "AI Agent Compiler Bug Finding"
created: 2026-05-28
updated: 2026-05-28
type: concept
tags: [concept, coding-agents, ai-agents, verification, testing, software-engineering]
sources:
  - raw/newsletters/2026-05-28-finding-miscompiles-for-fun-not-profit.md
  - https://open.substack.com/pub/semianalysis/p/finding-miscompiles-for-fun-not-profit
---

# AI Agent Compiler Bug Finding

The use of AI coding agents (Claude, Codex) to systematically find miscompilation bugs and vulnerabilities in compiler backends — a new paradigm demonstrated by Justin Lebar (SemiAnalysis contractor, ex-Google/Waymo/OpenAI compiler engineer) in May 2026. Represents the first empirical demonstration that "things that were impossible five months ago are now 'just' Very Expensive."

## Background

Justin Lebar — a compiler engineer with experience on CUDA in clang, XLA:GPU, Triton, and OpenAI hardware — systematically applied AI agents to compiler bug detection across three compiler backends, achieving remarkable results in each case.

## Key Results

### Fuzzing NVIDIA ptxas (Closed-Source Compiler)

- **Method**: Vibe-coded a fuzzer using ChatGPT Pro (cost ~$200/month for capacity); generated random PTX programs, ran through ptxas end-to-end
- **Results**: 40 miscompiled programs found in 3 days, ~80 reproducers within a week
- **Why it worked**: The LLM handled test-case alteration, minimization, instruction selection, and safety checks autonomously. "It was the difference between ChatGPT 5.2 and 5.5. I vibe-coded this entire fuzzer, never looking at a line of code."
- **Cost**: ~$200/month (ChatGPT Pro, exceeded quota) + ~$1,000 for Opus pay-per-token mode (a few days)
- **Limitation**: Closed-source = can't fix bugs directly, only work around them; no instrumentation possible

### Fuzzing LLVM AMDGPU Backend (Open-Source)

- **Same approach**: Same fuzzer, same bug discovery rate as ptxas
- **Cost advantage**: Open-source allows immediate application of patches — 5 bugs already fixed by AMD
- **Model comparison**: "I didn't notice a difference in quality between Opus 4.7 and ChatGPT 5.5"

### Static Bug-Finding via Code Reading Agents

- **Method**: Spawn 50 Claude subagents at a time to read LLVM source and find bugs directly
- **Results**:
  - AMDGPU backend: one bug every **4 minutes**
  - x86 backend: almost **2 bugs per minute**
  - No signs of slowing before stopping
- **Cost**: **> $10,000** in a few hours (Claude pay-per-token, fast mode off)
- **Severity**: Agent-found bugs less severe on average than fuzz-found bugs, but one exception:
  - LLVM turns an **atomic store into two non-atomic stores** — silent data corruption risk (~1% probability, extremely hard to root-cause)
  - This single bug alone could cause >$10K in damage

## Key Takeaways

1. **Impossible → Very Expensive**: What was impossible 5 months ago is now achievable with sufficient token budget
2. **Budget = Access to Possibility Space**: Companies without large inference budgets operate in a smaller solution space; the gap is growing
3. **Token Cost > Human Salary**: SemiAnalysis spent an order of magnitude more on tokens than on Lebar's pay that day. "This was the first time in my career that I delivered less value to my employer than my AI did."
4. **Future implications**: How much will labs be willing to spend in 6 months? What about those who can't?

## Related Tools

- **FuzzX**: Open-source repository on GitHub ([SemiAnalysisAI/FuzzX](https://github.com/SemiAnalysisAI/FuzzX/)) containing bugs found by Codex and Claude (both fuzzing and static analysis)

## Related Concepts

- [[concepts/coding-agents]] — The coding agents used for this work
- [[concepts/agent-verification]] — Verification of agent outputs
- [[concepts/inference]] — The cost of inference at scale
- [[entities/semianalysis]] — SemiAnalysis funded this research
- [[concepts/vibe-coding]] — Vibe-coding approach used for the fuzzer

## Open Questions

- Can the code-reading agent approach be applied to closed-source compilers by reading assembly?
- How much will token costs drop within 6 months, making this accessible to smaller teams?
- What other domains (beyond compilers) could benefit from the "spawn subagents to read source and find bugs" pattern?
