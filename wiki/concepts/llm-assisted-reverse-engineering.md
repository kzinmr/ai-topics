---
title: "LLM-Assisted Reverse Engineering"
created: 2026-11-19
updated: 2026-11-19
type: concept
tags:
  - reverse-engineering
  - security
  - coding-agents
  - agent-skills
  - developer-tooling
  - ai-in-science
status: L3
confidence: medium
aliases: [AI-assisted reverse engineering, LLM RE, agent-assisted RE]
sources:
  - raw/articles/2026-11-18_slowchronicle.com_llm-assisted-reverse-engineering.md
  - https://news.ycombinator.com/item?id=50553225
---

# LLM-Assisted Reverse Engineering

**LLM-assisted reverse engineering** is the 2026-practitioner workflow of pointing a coding agent at a binary and letting it drive the disassembly/decompilation/reconstruction loop, with the human providing domain judgment and dedicated **agent skills**. A practitioner write-up ("Slow Chronicle", by *ioma8*, ~20 years of hardware/software hacking) that hit Hacker News on 2026-11-18 (223 points) describes the workflow as now mostly autonomous: "What I basically do nowadays is just point the agent at the binary to be analysed and use my set of dedicated agent skills. Rest usually takes care of itself."

## The tool stack

The article's reference stack pairs a cheap-but-capable model with RE-native tooling exposed to the agent via MCP/CLI:

| Tool | Role |
|---|---|
| DeepSeek harness + DeepSeek v4.1 Flash | Primary agent/model — chosen for being "super performant, fast and cheap"; occasional Codex (Luna/Terra) for harder cases |
| **Ghidra + MCP bridge** | Market-leading free disassembler/decompiler; the MCP bridge lets agents drive it directly |
| **radare2 + kuna** | CLI disassemblers/decompilers — less capable than Ghidra but much faster and arguably *more agent-friendly* |

The notable cost argument: for bulk binary triage the author prefers a cheap open model (DeepSeek Flash) over frontier models, reserving expensive frontier reasoning for the hard steps — a [[concepts/model-routing|routing pattern]] applied to a security-research workload.

## The workflow

1. **Identify** binary type, platform, build config → select the appropriate decompiler.
2. **Decompile / disassemble** via the agent driving Ghidra (or radare2 for speed).
3. **Reason & reconstruct** semantics with the LLM, guided by **custom agent skills** the author wrote specifically for RE tasks ([[concepts/agent-skills|SKILL.md pattern]]).
4. **Human in the loop** for the parts that need decades-of-experience judgment; the agent handles the mechanical reading of assembly.

The author's framing is that AI didn't change *what* is done in RE so much as *who does the tedious part* — the expert still steers, but the 2026 speedup over manual analysis is large.

## Why it matters / controversy

- Demonstrates [[concepts/agent-skills|agent skills]] turning a general coding agent into a domain specialist (RE), rather than needing a bespoke RE product.
- Sits adjacent to active policy fights: Anthropic's Oct 2026 usage-policy enforcement blocked legitimate ML/security reverse-engineering work (video-game RE refusals), so the practitioner-momentum side matters contextually. See [[concepts/frontier-model-usage-policy-enforcement-2026-10]].
- Agent-driven Ghidra (via MCP) is an early concrete instance of [[concepts/computer-use|computer-use / tool-using agents]] in a specialist security workflow rather than a generic desktop demo.

**Confidence caveat:** single practitioner's report of their own workflow; speedup and tool preferences are anecdotal, not benchmarked.

## Related pages

- [[concepts/reverse-engineering]] — general RE concept page
- [[concepts/agent-skills]] — the SKILL.md mechanism used to specialize the agent
- [[concepts/frontier-model-usage-policy-enforcement-2026-10]] — policy friction for RE workloads
- [[concepts/computer-use]] — tool-using agents driving desktop/CLI apps
