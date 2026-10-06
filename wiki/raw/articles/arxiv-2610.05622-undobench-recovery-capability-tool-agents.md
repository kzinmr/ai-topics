---
source_url: https://arxiv.org/abs/2610.05622
ingested: 2026-10-06
sha256: b9661c53c222c056052a7ffd8ff8347cc1e856c8978f08f7085e437c5815cb74
---

# UndoBench: Separating Task Competence from Recovery Capability in Tool-Using AI Agents

arXiv:2610.05622 | Published 2026-10-04

**Authors:** Dolly Sah, Tanmay Sah, Harshul Jain, Tanya Sah

## Abstract

Tool-using AI agents are increasingly deployed across enterprise software systems, yet widely used benchmarks primarily evaluate nominal task completion, conflating baseline planning competence with operational fault recovery. We introduce UndoBench, a benchmark spanning 36 base workflows and 36 fault scenarios across 8 enterprise domains, decoupling task competence from recovery capability via counterfactual paired trials under identical seeds alongside wire-level effect-history and environment-state oracles. On 12 held-out TEST workflows across two open-weight models, two frameworks, and three recovery paradigms (5,760 executions / 2,880 paired trials) in the frozen lost-acknowledgment study, nominal competence reached 83.54% while conditional recovery success rate (CRSR) fell to 46.72%, with naive retry producing duplicate external effects in 53.33% of trials. Extensions to commercial API models reproduced this competence-recovery separation. Evaluations across complementary execution boundaries show that recovery is phase-dependent: before mutation, methods perform similarly without duplicate effects among capable trials; during partial mutation, naive retry, per-call idempotency, and zero-privilege journaling collapse on the evaluated composite workflows; after commit but before acknowledgment, verification and server-side idempotency substantially improve safety. These findings demonstrate that evaluating nominal completion alone masks critical, phase-dependent recovery vulnerabilities in autonomous agents.
