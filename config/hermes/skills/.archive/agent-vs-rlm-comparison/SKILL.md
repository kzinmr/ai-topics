---
name: agent-vs-rlm-comparison
category: mlops
description: Framework comparing traditional AI agents vs RLM (Recursive Language Models) across key architectural dimensions — decomposition, topology, scaling, context handling.
tags: [agents, RLM, architecture, alex-zhang, mit, context-decomposition]
---

# Agent vs RLM: Fundamental Differences (a1zhang Framework)

## Core Distinction

> *"Agents are designed based on human/expert intuition on how to break down a problem. RLMs are designed based on the principle that LMs should decide how to break down a problem."*
> — Alex L. Zhang (a1zhang), MIT

The decision of **how to decompose** moves from human → model.

## Comparison Matrix

| Dimension | Traditional Agents (ReAct/Multi-Agent) | RLM (Recursive Language Model) |
|---|---|---|
| Design philosophy | Human designs workflow | Model builds structure at runtime |
| Context handling | Static injection into prompt | Variables in REPL environment |
| Decomposition unit | Task decomposition | **Context decomposition** |
| Topology | Fixed (pre-defined graph/pipeline) | Dynamic/emergent (model decides) |
| Scaling axis | Model capability improvement | Recursion depth × test-time compute |
| Context rotation | Inevitable (larger window → worse performance) | Fundamentally avoided |
| Cost | Accumulates with longer execution | Proportional to task complexity |
| Debuggability | High (fixed structure) | Low (model-dependent decisions) |

## Key Concepts

### Context vs Task Decomposition
- **Agents**: Decompose tasks ("research → analyze → report")
- **RLM**: Decompose context — model selectively extracts relevant portions via code operations (`grep`, slicing) within REPL

### Scaffolds Evolution
CoT → ReAct → RLM:
- CoT: Scale reasoning depth
- ReAct: Scale tool usage
- RLM: Scale context manipulation (recursion depth as new dimension)

### Context Rot Avoidance
RLM avoids context rot by never feeding full context to root LM. Only relevant chunks are passed to sub-LMs, maintaining clean short contexts even for 10M+ token documents.

### Performance
RLM(GPT-5-mini) achieves ~91% accuracy on BrowseComp-Plus (1000 documents, 10M+ tokens), outperforming GPT-5 direct (~40%) at ~half the cost.

## Sources
- [RLM Blog Post (Oct 2025)](https://alexzhang13.github.io/blog/2025/rlm/)
- [RLM Paper (arXiv:2512.24601)](https://arxiv.org/abs/2512.24601)
- [Language Models will be Scaffolds (Feb 2026)](https://alexzhang13.github.io/blog/2026/scaffold/)
- [Mitchell Gordon's Taxonomy](https://mitchgordon.me/tools/2026/01/14/taxonomy-of-agent-architectures.html)

## Related
- Wiki entity: a1zhang (Alex L. Zhang)
- Concepts: RLM, agent architectures, test-time compute, context decomposition
