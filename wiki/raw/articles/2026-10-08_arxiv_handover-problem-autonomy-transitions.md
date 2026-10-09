---
source_url: https://arxiv.org/abs/2610.10352
ingested: 2026-10-08
sha256: 36a1933927c57b67a952a2ca319d5fd055429820cee915323377c3337f012f59
---

# The Handover Problem: Governing Autonomy Transitions in Human-AI Collaboration

- **arXiv:** arXiv:2610.10352
- **Authors:** Vicente Pelechano, Antoni Mestre, Manoli Albert, Miriam Gil
- **Published:** 2026-10-07
- **Source URL:** https://arxiv.org/abs/2610.10352

## Abstract

Human-machine systems rarely operate at a fixed level of AI autonomy. As operators and AI systems collaborate over time, control must shift: the AI can take on more responsibility when collaboration is stable, maintain its current role when evidence is ambiguous, or return control to the human when conditions deteriorate. Existing work on adaptive automation, supervisory control, trust in automation, and deskilling explains parts of this problem, but provides no auditable, multi-signal criterion for governing when autonomy should change across multi-cycle workflows. We formalise this challenge as the Handover Problem: deciding, at each operational cycle, whether to escalate, maintain, or revert AI autonomy while keeping the process reversible, recoverable, and auditable. We introduce the Handover Readiness Score (HRS), a transparent composite measure that integrates four signal dimensions: operator readiness, human-AI trust, learning stability, and operational performance. It is combined with a hysteresis-based transition policy that requires sustained positive evidence before increasing autonomy but reverts promptly when conditions worsen. Across software engineering and manufacturing domains, the HRS and hard safety guards address complementary failure regimes: guards enforce immediate corrective action when a single indicator breaches a critical threshold, while the HRS detects the slow, multi-signal erosion of operator readiness that no individual guard can observe. The framework establishes autonomy handover as a governance problem requiring explicit, composite, and auditable criteria. This provides a conceptual and formal foundation that adaptive automation research has not previously provided.
