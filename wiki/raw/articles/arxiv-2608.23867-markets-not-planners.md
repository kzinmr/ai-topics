---
source_url: https://arxiv.org/abs/2608.23867
ingested: 2026-09-19
sha256: 12c0fac7eb6afc4b71d86aac96bf0d40e5742f6b31a1535665439c62eea052b9
---

# Markets, Not Planners: Decentralized Orchestration of LLM Agents with Private Information

**arXiv**: https://arxiv.org/abs/2608.23867 | **Published**: 2026-08-24

**Authors**: Xiao Liu, Haoyang Li, Songwei Li, Hongbo Fang, Fengli Xu, Feng Shi, James Evans

## Abstract

As LLM agents proliferate, built by different parties and with different capabilities and costs, orchestrating them is more like assembling labor across the economy than a computer calling a subroutine. Existing orchestration is typically centralized, with a single planner assigning every task, but this creates a bottleneck as agent pools grow, requires private information (e.g., agents' execution costs), and can easily be manipulated, such that a single inserted preference nearly doubles a favored agent's task share under a centralized LLM allocator. We introduce AgentLance, a repeated labor market in which agents bid on tasks using their private costs and self-maintained strategy notes, an allocator selects winners from bids and public reputation records, and a VCG-style payment rule rewards cost-aware bidding. Complex tasks are handled by hierarchical delegation: winning agents can decompose work and subcontract it through the same mechanism. Across mathematical reasoning, code generation, knowledge-intensive QA, and agentic tasks, AgentLance matches agents to their specializations, shifts work toward cheaper agents as cost sensitivity rises, and consistently outperforms single-model, centralized-orchestration, and market baselines. Diagnosing market failures, including inaccurate cost self-estimation and sub-optimal bidding, then correcting them in controlled experiments yields further gains, charting a path toward more efficient agent economies.
