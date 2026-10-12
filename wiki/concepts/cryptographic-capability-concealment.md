---
title: "Cryptographic Capability Concealment — When Models Can Provably Hide Skills"
created: 2026-10-12
updated: 2026-10-12
type: concept
tags: [ai-safety, alignment, red-teaming, agent-safety, governance]
sources: [raw/papers/2026-10-09_2610.13928_provably-hide-arbitrary-capabilities.md]
confidence: high
aliases: [AI Models Can Provably Hide Arbitrary Capabilities]
related: [concepts/ai-control, concepts/mismeasure-of-open-source, concepts/evaluation/evaluation-harness-validity]
---

# Cryptographic Capability Concealment — When Models Can Provably Hide Skills

*Formal title: "AI Models Can Provably Hide Arbitrary Capabilities" (Draguns, Motwani, Douglas,
Schroeder de Witt; arXiv:2610.13928, Oct 2026).*

Capability evaluations before deployment rest on an assumption: **any hidden capability can, in
principle, be elicited**. Draguns et al. show this assumption **fails under adversarial
conditions** — you can build a model that provably refuses to reveal a skill to any auditor, even
one with full access to the weights.

## Construction

A backdoor attack embeds an **encrypted neural network inside a host model's weights**. The hidden
circuit decrypts and executes **only upon receiving a secret trigger**. Using **digital lockers**
(cryptographic commitments), the concealed circuit remains provably hard to elicit *and* hard to
interpret **under cryptographic assumptions** — extending earlier "hide a fixed string" work to
**arbitrary computations**. The security is computational, not statistical: no amount of
inspection defeats it without the key.

## Empirical probe

Proof-of-concept models in PyTorch, evaluated on a **small chemical-reaction prediction task** (a
CBRN-relevant proxy). Elicitation attempts via **fine-tuning, weight noising, gradient-based
trigger search, and latent adversarial training** all fail to surface the hidden capability. The
authors release their models to help improve defenses.

## Why it matters

This is a **hard limit on elicitation-based capability audits** and on interpretability. If a
model can hide arbitrary computation behind a cryptographic trigger, then:

- **Capability evals can be evaded by construction**, not just by sandbagging. Sandbagging (a
  model *choosing* to underperform) can be probed; a cryptographically locked circuit cannot be
  read or elicited even from a fully-open model. This sharpens
  [[concepts/mismeasure-of-open-source]] — open weights do not imply inspectable intent.
- The **AI control** paradigm (see [[concepts/ai-control]]), which already treats models as
  potentially untrusted and defends "outside the model," becomes more necessary: if weights can't
  be trusted, behavioral containment and input/output gating are the remaining levers.
- It reframes the open-weights safety debate: **cryptographic concealment is a counterargument to
  "open models are safer because they're auditable."**

## Caveats

Proof-of-concept at toy scale (small chemistry task); the *cryptographic guarantee* is the durable
claim, not the specific benchmark numbers.

## Related

- [[concepts/ai-control]]
- [[concepts/mismeasure-of-open-source]]
- [[concepts/evaluation/evaluation-harness-validity]]
- [[concepts/x-agentred-multi-service-red-teaming]]
