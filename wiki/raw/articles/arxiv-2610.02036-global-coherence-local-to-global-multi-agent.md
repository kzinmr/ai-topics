---
source_url: https://arxiv.org/abs/2610.02036
arxiv_id: 2610.02036
ingested: 2026-10-03
sha256: 55582c5f834d32712c29e924b4ce228aaf54a77eba25fa8e467cc5da81137e46
---

# Global Coherence: When Every Agent Is Right and the Team Is Still Wrong — A Local-to-Global Semantic Foundation for Multi-Agent Collaboration

**arXiv:** 2610.02036  |  **Submitted:** 2026-10-01
**Authors:** Xin Heng
**URL:** https://arxiv.org/abs/2610.02036

## Abstract

AI agents can each make locally valid decisions yet jointly produce an invalid result. We call this the global coherence problem: a failure of shared state, not merely of model intelligence. Our Observation-Aliasing Impossibility Theorem gives the exact boundary. A policy can guarantee a valid action exactly when all worlds producing the same observation share an admissible action. If k indistinguishable worlds require pairwise-disjoint actions, the best randomized worst-case success is 1/k; more reasoning, roles, messages, or samples cannot recover the missing distinction. A stronger model can reason better within its context, but it cannot see beyond it. We then give local-to-global runtime semantics X = (H, C, G, F; D): topology H records overlapping scopes; category C governs state-changing actions; groupoid G retains reversible translations; sheaf F tests whether local views glue into one world; and minimal history D keeps only distinctions that alter legal futures. Models propose; the harness owns shared state and governs commit. Nine studies test both the failure and its boundary. On a controlled revision benchmark, the same frontier model scores 40/40 when the deciding event is visible; when it is hidden, tested arms score 12--17/40, consistent with chance (1/3); restoring one authoritative fact returns 40/40. On TeamBench, ordinary teams exceed a shared budget in 5/5 runs, a visible live count leaves 4/5 violations, and commit enforcement leaves 0/5. In tau2-bench Telecom, current-state checks score 0.07 after silent reverts, while the harness scores 1.00. Where a conventional solver already owns the complete relevant state, it ties the harness as predicted. The counterintuitive conclusion is that local intelligence cannot substitute for missing global state.
