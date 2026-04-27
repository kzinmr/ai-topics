# GenericAgent: A Token-Efficient Self-Evolving LLM Agent

**Source:** arXiv:2604.17091 (cs.CL)
**Retrieved:** 2026-04-27
**Authors:** Jiaqing Liang et al. (17 authors, Fudan University)
**Published:** 18 Apr 2026
**Peer Review:** ❌ arXiv-only (not peer-reviewed)

## Core Thesis

Long-horizon performance is determined not by context length, but by how much decision-relevant information is maintained within a finite context budget.

## Four Key Components

1. **Minimal Atomic Tool Set** – Avoids tool proliferation. Only essential, non-redundant tools are exposed.
2. **Hierarchical On-Demand Memory** – Default: small, high-level view; deeper details fetched only when needed, preserving context budget.
3. **Self-Evolution Mechanism** – Verified past trajectories converted into reusable SOPs (Standard Operating Procedures) and executable code.
4. **Context Truncation & Compression Layer** – Maintains high information density during long executions by trimming/compressing low-value content.

## Key Performance

- Outperforms leading agent systems across: task completion, tool use efficiency, memory effectiveness, self-evolution capability, web browsing
- Uses significantly fewer tokens and interactions than competitors
- Continues to evolve over time

## Key Insight

Main innovation is shifting focus from context length to **information density per token** — maximizing decision-relevant signal inside a fixed context window. Achieved through tool minimalism, smart memory hierarchy, trajectory-derived knowledge, and dynamic compression.

## Additional Info

- Code: https://github.com/lsdefine/GenericAgent
- License: CC BY 4.0
- 17 co-authors
