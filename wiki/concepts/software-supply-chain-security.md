---
title: "Software Supply Chain Security"
type: concept
aliases:
  - software-supply-chain-security
  - supply-chain-security
  - trusting-trust
created: 2026-04-25
updated: 2026-08-15
tags:
  - concept
  - security
  - supply-chain
  - software-engineering
  - compiler
sources:
  - raw/articles/research.swtch.com--nih--2cd8df91.md
  - https://research.swtch.com/nih
---

# Software Supply Chain Security

**Software Supply Chain Security** is the discipline of ensuring that the software you build and run — from the compiler and toolchain, through dependencies and build pipelines, to the final artifact — is trustworthy end to end. It is an old problem with a canonical founding document: Ken Thompson's 1983 Turing Award lecture **"Reflections on Trusting Trust"**, which demonstrated that a compiler can be subverted to insert a backdoor with no trace in source code. See [[concepts/ai-supply-chain-security]] for the AI/ML-era variant of the same problem.

## The Trusting Trust Problem

In October 1983, Ken Thompson chose supply chain security as the topic of his Turing Award lecture (published in Communications of the ACM as "Reflections on Trusting Trust"). The attack is built in three steps:

1. **Step 1 — Write a self-reproducing program (quine)**: a program that prints its own source code. The technique shows that a program's behavior can encode information that never appears in its source.
2. **Step 2 — Compilers learn**: when a compiler compiles itself, details can persist only in the compiler *binary*, not in the source. Thompson's example: the numeric values of C string escape sequences — the compiler "learns" the correct values from its own binary even if the source is changed.
3. **Step 3 — The login backdoor**: modify the compiler binary to insert a backdoor into the `login` program at compile time, leaving no trace in either the compiler source or the login source. The corrupted compiler reproduces the corruption in every compiler it compiles.

The attack works because **trust in the toolchain is bootstrapped**: the compiler you use today was compiled by a compiler, whose trust cannot be traced to source alone.

## The Actual Code: nih.a (2023)

For 40 years the canonical paper was read as a thought experiment — until Russ Cox asked Ken Thompson for the actual code. At the 2023 SCaLE keynote Q&A, Thompson revealed he still had it and that nobody had ever asked; Cox became the first person to receive `nih.a` ("not invented here"), the real attack code applying to the Research Unix V6 C compiler. Cox published it with a runnable V6 emulator (login `ken`/`ken`):

- The archive contains `x.c` (the `codenih` compiler hook called during preprocessing for each input line) and `rc` (the build recipe).
- The hook deliberately does nothing when `cc -p` (preprocessor-only mode) is used — a discovery-avoidance measure.
- Thompson's controlled-release story: he had the code "stolen" in a controlled way and tracked whether anyone found it; they broke it by accident but never identified or traced the backdoor.

The full walkthrough: [Running the "Reflections on Trusting Trust" Compiler](https://research.swtch.com/nih) by [[entities/russ-cox]] (2023-10-25).

## Implications and Countermeasures

- **Reproducible builds**: if a build is reproducible from source, a tampered toolchain becomes detectable by comparison — the closest practical answer to the trusting-trust problem.
- **Minimal bootstrapping**: reducing the toolchain trust base (e.g., bootstrap a C compiler from a tiny trusted seed) shrinks the attack surface.
- **SBOMs and dependency hygiene**: modern supply-chain practice (software bills of materials, lockfiles, provenance attestation) addresses the *dependency* dimension — a different layer from the compiler-binary attack, but the same underlying question: can you verify what you actually ran?
- **The AI-era extension**: release pipelines, CI/CD runners, and packaging infrastructure became the dominant attack surface in 2026 (see [[concepts/ai-supply-chain-security]] — Codex command injection, LiteLLM/Mercor breach, TanStack npm attack in [[concepts/openai/tanstack-supply-chain-2026]]).

## Related Concepts

- [[concepts/ai-supply-chain-security]] — AI/ML supply chain variant (release pipelines, model weights, agent infrastructure)
- [[entities/russ-cox]] — Author of the executable trusting-trust walkthrough
- [[concepts/compiler-construction]] — Compiler internals background for the attack
- [[concepts/openai/tanstack-supply-chain-2026]] — May 2026 npm supply chain attack response

## Sources

- [Running the "Reflections on Trusting Trust" Compiler (Russ Cox, Oct 2023)](https://research.swtch.com/nih) — raw: `raw/articles/research.swtch.com--nih--2cd8df91.md`
