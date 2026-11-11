---
title: "AlphaProof Code: Formal Verification of Signal's Protocol"
type: concept
created: 2026-11-11
updated: 2026-11-11
tags:
  - formal-verification
  - google
  - deepmind
  - gemini
  - security
  - anthropic
  - ai-agents
  - formal-methods
  - open-source
confidence: high
sources:
  - https://deepmind.google/blog/introducing-alphaproof-code/
  - raw/articles/2026-11-11_deepmind_alphaproof-code-signal.md
  - https://news.ycombinator.com/item?id=50439193
---

# AlphaProof Code: Formal Verification of Signal's Protocol

On **November 10, 2026**, Google DeepMind announced **AlphaProof Code**, an agentic framework that guided AI agents to mathematically prove key security properties of the *actual shipped code* underlying the Signal cryptographic protocol — described as a "grand challenge" of software security. Claimed to be the first time AI has formally verified a widely deployed cryptographic protocol at this depth, and the first time the implementation (not just the design) of such a protocol has been formally verified by any method (HN 647pts).

Distinct from [[concepts/alpha-proof-nexus]] (the May 2026 Erdős-problem math line): AlphaProof Code targets **software security assurance**, not theorem proving for open math problems. Both share the agentic-Lean paradigm.

## How it works

- **Multi-LLM agentic framework** that splits formal verification like a research team: human experts decide *what* to prove; a group of AI agents does the proving.
- Researchers collaborated with a mix of models to translate Signal's security goals into formal mathematical specifications, **with human experts reviewing every specification**.
- Agents powered by **Gemini Carbon** (cf. [[concepts/gemini/gemini-4-carbon]]) generated **over 6 million lines of Lean** proofs.
- Agents then audited the proofs and flagged only **~1% of the codebase** for a second human look; Lean automatically checks everything else.
- **Negative test**: reintroducing two real, previously-fixed bugs into an isolated fork produced machine-checked proofs that the buggy versions were *insecure* — evidence the system discriminates correct from buggy code.
- Total elapsed time: **four weeks**, versus historically years for expert teams.
- Artifacts are **open-sourced** for community use.

## Signal endorsement

Signal CTO Ehren Kret: "Using AI agents to translate live code into valid Lean theorems is a major breakthrough. As AI-driven security threats grow, rigorously verifying the Signal protocol implementation gives us even greater confidence in our code's privacy guarantees." Verified properties include forward/post-compromise protection of messages.

DeepMind positions the technique as a complement to automated defense agents like **CodeMender** (Oct 2025), targeting "agent-driven cyber threats", and names medical-device firmware and power-grid software as next application domains.

**Authors**: Swarat Chaudhuri, Andrew Ferraiuolo, Anton Kovsharov, Tej Chajed, Sam Schlesinger, Karn Seth, Jonathan Katz, Charles Sutton, Pushmeet Kohli.

## HN discussion highlights (item 50439193, 647pts)

- [p-e-w] "It's nothing short of amazing that a huge codebase like Signal's is apparently not only secure in a practical sense, but secure even in a strict formal sense."
- [xrisk] (on the recurring halting-problem objection) "lean has no relation to the halting problem; you can think of it as a language that allows proofs to be encoded as code, and the compiler that runs that code as knowing how to enforce mathematical constraints appropriately."
- [sebzim4500] "The halting problem does imply that there exist programs which are entirely correct that Lean will never be able to prove the correctness of, but this is not really relevant in practice."
- [lifeisloving / booty] side debate: whether OS-level complexity (much less verifiable than protocol code) limits the assurance claim, and whether US government Signal forks change the threat model.

## Assessment

The claim is vendor-published but unusually checkable: Lean-checkable artifacts are open-sourced, and the negative-control bug injection addresses the "LLM proofs are vibes" objection directly. The credible caveat, voiced in-thread, is scope — proving key properties of cryptographic protocol code ≠ verifying the whole product or its runtime environment.

## Related

- [[concepts/alpha-proof-nexus]] — sibling DeepMind agentic-Lean line (math, not software)
- [[concepts/formal-verification-llm-agents]] — broader formal-verification-with-agents landscape
- [[concepts/neurosymbolic-ai]] — neural-for-hypothesis / symbolic-for-proof framing
- [[entities/deepmind]] — Google DeepMind
- [[concepts/claude/mythos-glasswing]] — the other 2026 frontier-lab security program (discovery-side, vs. this verification-side)
