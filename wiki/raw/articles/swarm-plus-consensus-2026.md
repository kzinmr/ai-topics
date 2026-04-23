---
title: SWARM+: Scalable and Resilient Multi-Agent Consensus for Fully-Decentralized Data-Aware Workload Management
category: other
status: active
---

# SWARM+: Scalable and Resilient Multi-Agent Consensus for Fully-Decentralized Data-Aware Workload Management

**Source:** arXiv:2603.19431v1 (cs.DC)
**Authors:** Komal Thareja, Krishnan Raghavan, Anirban Mandal, Ewa Deelman
**Published:** March 2026
**URL:** https://arxiv.org/html/2603.19431v1

---

## Problem: Centralized Orchestrator Failures

Distributed scientific workflows span heterogeneous compute clusters, edge resources, and geo-distributed data repositories. Current centralized orchestrators create:

- **Single points of failure**
- **Scalability bottlenecks** (O(n²) communication complexity)
- **Poor adaptability** to changing resource availability

## Solution: SWARM+ Three-Layer Architecture

```
┌─────────────────────────────────────────────────────────┐
│ Hierarchical Multi-Agent Layer
│ Level 1: CoordinatorAgents (job delegation)
│ Level 0: ResourceAgents (local job execution)
├─────────────────────────────────────────────────────────┤
│ Consensus Layer
│ Three-phase protocol: Proposal → Prepare → Commit
├─────────────────────────────────────────────────────────┤
│ Selection Layer
│ Cost-based candidate selection with data-awareness
└─────────────────────────────────────────────────────────┘
```

### Multi-Agent Layer (Two-Level Hierarchy)

- **Level 0 (ResourceAgents)**: Maintain local resource state (CPU, RAM, GPU, disk, DTN), select jobs from local pool, execute jobs
- **Level 1 (CoordinatorAgents)**: Aggregate child state, handle job delegation, route selections to appropriate groups

Aggregation functions reduce per-check communication from O(m) to O(1):
```python
C_max = max(c∈children c.capacity)
Aggregated_DTN = Union of children's DTN endpoints with quality scores
```

### Consensus Layer (Three-Phase Protocol)

1. **Proposal Phase**: Agent broadcasts `<PROPOSAL, p, j, a_i, c>` where p=proposal ID, j=job, c=computed cost
2. **Prepare Phase**: Agents validate feasibility, broadcast `<PREPARE, p, j, a_i, a_k>` until quorum reached
3. **Commit Phase**: After prepare quorum, broadcast `<COMMIT, p, j, a_i, a_k>`

**Adaptive Quorum Formula:**
```
q(t) = ⌈(n_live(t) + 1) / 2⌉
```

### Selection Layer (Cost Function)

```
feasible(a,j) = ∧(r∈R)(a.r_available ≥ j.r_req) ∧ conn_feasible(a,j)
cost(a,j) = Σ(w_r · u_r(a,j)) + Σ penalty_p(a,j)
```

Where `u_r(a,j) = j.r_req / a.r_available` (utilization fraction)

**Connectivity Penalty:**
```
P_conn = 1 + β · (1 - s̄)
```
Where `s̄` = average DTN connectivity score [0,1], β = penalty factor (default 1.0)

## Resilience Mechanisms

### Multi-Signal Failure Detection

| Method | Detection Latency | Robustness |
|--------|-------------------|------------|
| **gRPC-based** | 13.8ms ± 1.6ms | Fast but may detect false positives |
| **Redis-based** | 54.2s ± 0.5s | Slower but robust against transient issues |

### Automatic Job Reselection
- Failed agent's jobs reset to pending and re-enter selection
- Jobs in prepare/commit states exceeding timeout also reset

### Adaptive Quorum
- Automatically adjusts to `n_live` agents
- Enables consensus under degraded conditions
- Preserves safety (no conflicting assignments) and liveness (continued progress)

## Evaluation Results

| Metric | SWARM | SWARM+ | Improvement |
|--------|-------|--------|-------------|
| Mean Selection | 40.03s | 1.20s | **97.0%** |
| P95 Selection | 85.47s | 1.54s | **98.2%** |

## Key Insights for AI Agent Systems

1. **Hierarchical consensus scales to 1000+ agents** — O(n²) → O(log n) complexity
2. **Adaptive quorum** enables consensus under partial failures
3. **Data-aware job placement** considers network connectivity, not just compute capacity
4. **Multi-signal failure detection** combines fast (gRPC) and robust (Redis) approaches

## Relevance to AI Agent Orchestration

While SWARM+ targets scientific workflows, its patterns apply to AI agent teams:
- **Hierarchical coordination** = Supervisor/Worker patterns at scale
- **Consensus protocol** = Agreement on task assignment and state
- **Adaptive quorum** = Dynamic team membership (agents joining/leaving)
- **Failure detection + reselection** = Self-healing agent systems

See [[concepts/multi-agent-consensus-patterns]] for the wiki concept page.