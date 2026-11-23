---
title: Stateful API emulators for local dev, CI and agent sandboxes
type: concept
created: 2026-11-23
updated: 2026-11-23
tags:
  - sandbox
  - developer-tooling
  - agent-infrastructure
  - testing
  - ci-cd
sources:
  - https://emulate.dev
  - https://github.com/vercel-labs/emulate
  - "X scan 2026-11-23 (@ctatedev, status 2124927061735129347)"
related:
  - entities/chris-tate
  - entities/vercel-labs
  - concepts/agent-sandbox-patterns
  - concepts/in-process-sandbox
  - concepts/modal-sandboxes
---

# Stateful API emulators for local dev, CI and agent sandboxes

A **stateful API emulator** is a local, drop-in replacement for a third-party service that implements enough of the real API's surface — and, critically, its **server-side state** — that a client cannot tell it is not talking to production. It sits between two well-known but inadequate options:

| Approach | State | Fidelity | Network required | Use in a no-network sandbox |
|---|---|---|---|---|
| **Mocks / stubs** | none (canned responses) | low — matches recorded calls only | no | yes |
| **Stateful emulator** | full server-side state | "production-fidelity" API semantics | no | **yes** |
| **Live service / test tenant** | full | full | **yes** | no |

## Why this matters for agents

The category's newest customer is not the CI pipeline but the **AI coding agent**. Every sandbox architecture in [[concepts/agent-sandbox-patterns]] has to answer the same question: what happens when the code an agent wrote calls Stripe, S3, or a Slack webhook? The three existing answers all cost something:

- **Zero-secret sandbox + control-plane proxy** — every external call hops through a stateless control plane that holds the real credentials. Secure, but the sandbox cannot be run offline and the control plane is on the hot path.
- **Scoped credentials in the sandbox** (presigned URLs, leased creds — [[concepts/agent-credential-leasing]]) — works, but the agent can hit the real service, so a runaway loop is a real bill and a real side effect.
- **No-network sandbox** — safest, but the generated code simply fails at the first external call.

A stateful emulator replaces option three's failure with a working API. The agent's code runs unmodified, the emulator keeps coherent state across calls (a "created" resource really exists for the next call), and there is no credential to leak and no egress to police.

## Reference implementation: emulate (Vercel Labs)

**[emulate](https://emulate.dev)** (`vercel-labs/emulate`, released June 2026, [[entities/vercel-labs|Vercel Labs]], led publicly by [[entities/chris-tate|Chris Tate]]) is currently the canonical artifact for the category. Its own positioning line is the clearest statement of the distinction:

> *"Local drop-in replacement services for CI and no-network sandboxes. Fully stateful, production-fidelity API emulation. Not mocks."*

- **Crossed 1M weekly npm downloads** on 2026-11-23, announced by Tate ([tweet](https://x.com/ctatedev/status/2124927061735129347)).
- Adoption is CI-shaped (no-network runners, hermetic builds) and, per Tate's own framing, sandbox-shaped: it is listed among tools useful for *"AI coding agents that need predictable API surfaces during code generation."*
- The "not mocks" claim is the load-bearing one: mock libraries return what a test author scripted; an emulator has to actually implement the state machine the real service implements, which is why the category is per-service work rather than a generic library.

## Open questions

- **How much fidelity is needed to test an agent, vs an app?** A mock is sufficient when a human wrote the assertion; an agent generating code needs the emulator to *reject* invalid calls the way production would, otherwise the agent learns a false API contract. The right failure-semantics surface for agent use is unstudied.
- **Who maintains the emulator when the upstream API changes?** Same drift problem as contract tests, but the consumer is now an LLM whose prior knowledge of the API comes from training data that is already stale — an emulator may silently disagree with the model's memory of the API.
- **Category status**: as of Nov 2026 emulate is essentially a single-vendor category at meaningful scale; no neutral conformance suite or comparison exists (cf. the mature Terraform-provider / cloud-emulator ecosystem that never produced one either).

## Related

- [[concepts/agent-sandbox-patterns]] — where an emulator slots in among control-plane, credential-lease, and no-network designs
- [[concepts/in-process-sandbox]] — the in-process end of the same "avoid external infra for agent code" spectrum
- [[concepts/modal-sandboxes]] — the heavyweight counterpoint (real network, real credentials, real isolation)
- [[entities/chris-tate]] — emulate author; also [[concepts/scriptc-typescript-native-compiler|scriptc]] and [[entities/vercel-labs|Vercel Labs]] DX tooling

## Sources

- emulate — https://emulate.dev (raw text quoted above from the site's tagline)
- GitHub — https://github.com/vercel-labs/emulate
- X: Chris Tate, 2026-11-23 — "emulate just crossed 1M weekly downloads" — https://x.com/ctatedev/status/2124927061735129347
