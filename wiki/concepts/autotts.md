---
title: AutoTTS (Agent-Discovered Test-Time Scaling)
created: 2026-05-25
updated: 2026-05-25
type: concept
tags:
  - concept
  - test-time-scaling
  - ai-agents
  - coding-agents
  - lab
  - optimization
  - inference
  - reasoning
  - self-improving
  - recursive-self-improvement
sources: [raw/articles/2026-05-24_autotts-claude-code-discovers-scaling.md, https://the-decoder.com/researchers-let-claude-code-discover-ai-scaling-algorithms-that-humans-probably-wouldnt-have-designed/]
---

# AutoTTS (Agent-Discovered Test-Time Scaling)

**AutoTTS** is a research method where a coding agent (Claude Code) automatically discovers test-time scaling algorithms instead of relying on human-designed rules. Developed by researchers from UMD, UVA, WUSTL, UNC, Google, and Meta (May 2026).

## Core Idea

Test-time scaling (TTS) improves LLM performance by spending more compute per response — running multiple solution paths in parallel, extending chain-of-thought, etc. Traditionally, humans hand-craft the rules for when to branch, prune, or double-down on paths.

AutoTTS flips this: **humans design the search environment, the agent discovers the algorithm.**

## Method

1. **Pre-generate solution paths** for benchmark tasks — no live model calls during search
2. **Claude Code iterates**: reviews past attempts, identifies weaknesses, writes new control algorithms in code
3. Each algorithm exposes only **one high-level controller** that sets all internal thresholds
4. **Full run logs** help the agent understand where earlier attempts wasted compute
5. Search cost: **$40, 160 minutes**

## Discovered Algorithm

The agent-built controller uses a counter-intuitive strategy:

1. **Monitors confidence shifts** over multiple rounds (not just final accuracy)
2. If confidence **barely budges** → opens more solution paths
3. If confidence **climbs quickly** → skips opening new paths
4. Solution paths whose **interim result aligns with majority** → receive extra compute
5. Divergent paths are only dropped if they keep heading wrong **over several rounds**

> "The authors call this kind of coordination something that would've been nearly impossible to design by hand."

## Results

- **~70% token reduction** vs standard self-consistency (64 parallel answers + majority vote) at same accuracy
- Transfers to **different model** (DeepSeek-R1-Distill-Llama-8B) and **non-math benchmark** (GPQA-Diamond)
- Outperforms established human-designed methods on AIME and HMMT

## Critical Design Choices

| Component | Without It |
|---|---|
| Single high-level controller | Agent uses extreme shortcuts that tank accuracy on new tasks |
| Detailed run logs | Algorithm uses more compute with worse accuracy |

## Context

- **Related work**: FunSearch, AlphaEvolve, ADAS — all use LLMs as program searchers. AutoTTS is the first to apply this to test-time scaling
- **Broader trend**: Meta's hyperagents, HuggingFace's 2024 small-model-via-TTS work
- **Meta-level shift**: Human ingenuity moves upstream to create fertile search environments; complex control algorithms emerge automatically

## Limitations

- Only handles width/depth trade-offs; cannot handle tree searches
- Quality depends on the coding agent used (open-source alternatives untested)

## Related

- [[concepts/test-time-scaling|Test-Time Scaling]]
- [[concepts/chain-of-thought|Chain of Thought]]
- [[concepts/recursive-self-improvement|Self-Improving AI]]
- [[entities/claude-code|Claude Code]]
- [[concepts/coding-agents/coding-agents|Coding Agents]]
- [[concepts/recursive-self-improvement|Recursive Self-Improvement]]
