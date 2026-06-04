# Agent vs RLM: Fundamental Differences (a1zhang Framework)

## Core Distinction
*"Agents are designed based on human/expert intuition on how to break down a problem. RLMs are designed based on the principle that LMs should decide how to break down a problem."*
— Alex L. Zhang (a1zhang), MIT

## Comparison Matrix
| Dimension | Traditional Agents | RLM |
|---|---|---|
| Design philosophy | Human designs workflow | Model builds structure at runtime |
| Context handling | Static injection into prompt | Variables in REPL environment |
| Decomposition unit | Task decomposition | Context decomposition |
| Topology | Fixed (pre-defined graph/pipeline) | Dynamic/emergent |
| Scaling axis | Model capability improvement | Recursion depth × test-time compute |
| Context rotation | Inevitable | Fundamentally avoided |
| Cost | Accumulates with longer execution | Proportional to task complexity |
| Debuggability | High (fixed structure) | Low (model-dependent decisions) |

## Scaffolds Evolution
CoT → ReAct → RLM:
- CoT: Scale reasoning depth
- ReAct: Scale tool usage
- RLM: Scale context manipulation (recursion depth as new dimension)

## Performance
RLM(GPT-5-mini) achieves ~91% accuracy on BrowseComp-Plus (1000 documents, 10M+ tokens), outperforming GPT-5 direct (~40%) at ~half the cost.

## Sources
- [RLM Blog Post (Oct 2025)](https://alexzhang13.github.io/blog/2025/rlm/)
- [RLM Paper (arXiv:2512.24601)](https://arxiv.org/abs/2512.24601)
- [Language Models will be Scaffolds (Feb 2026)](https://alexzhang13.github.io/blog/2026/scaffold/)
- [Mitchell Gordon's Taxonomy](https://mitchgordon.me/tools/2026/01/14/taxonomy-of-agent-architectures.html)
