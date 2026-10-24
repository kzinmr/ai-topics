---
title: "Formal Verification for LLM Agents"
type: concept
created: 2026-04-21
updated: 2026-10-24
tags:
  - concept
  - safety
  - formal-methods
  - model
  - infrastructure
  - reinforcement-learning
aliases: ["vericoding", "llm-formal-verification", "proof-assistants-llm"]
sources:
 - path: raw/articles/crawl-2026-04-21-kleppmann-formal-verification-ai.md
 - path: raw/articles/crawl-2026-04-21-shuvendu-intent-formalization.md
 - path: raw/newsletters/2026-06-03-scaling-past-informal-ai-carina-hong-axiom-math.md
 - path: raw/articles/2026-10-22_anthropic-formal-verification-scale.md
status: active
---

# Formal Verification for LLM Agents

Formal verification is the practice of mathematically proving that code *always* satisfies its specifications—including all edge cases. AI is poised to bring this from a fringe academic pursuit into the mainstream of software engineering, fundamentally changing how we trust AI-generated code.

## What Is Formal Verification?

Proof assistants and proof-oriented programming languages that enable:
- Writing **formal specifications** that code must satisfy
- Mathematically proving code *always* satisfies specs

**Key tools:** Rocq, Isabelle, Lean, F*, Agda, Verus

**Landmark verified systems:**
- seL4 operating system kernel (8,700 lines of C, 200,000 lines of Isabelle proofs)
- CompCert C compiler
- Cryptographic protocol stack (Project Everest)

## Why Proof Writing Is Ideal for LLMs

> *"It doesn't matter if they hallucinate nonsense, because the proof checker will reject any invalid proof and force the AI agent to retry."*

The proof checker is small, verified code—making it virtually impossible to sneak invalid proofs through. Unlike regular code where hallucinations can be subtle and plausible, invalid proofs are mechanically rejected.

### The seL4 Cost Problem (and How AI Fixes It)

| Implementation | Proof Effort (2009) | With AI Assistance |
|----------------|---------------------|---------------------|
| 8,700 lines of C | 20 person-years | Dramatically reduced |
| | 200,000 lines of Isabelle | AI generates most proof scripts |
| | 23 lines of proof per line of code | Lower ratio with automation |

## The Three Converging Factors

1. **Formal verification will become vastly cheaper** — AI automation reduces the labor cost of proof generation
2. **AI-generated code needs formal verification** — eliminates the need for expensive human code review
3. **Proof checkers counteract LLM imprecision** — the small, verified proof checker catches errors that probabilistic outputs might miss

## The Vericoding Movement (vs. Vibecoding)

**Vericoding** (September 2025 paper): using LLMs to generate formally verified code

The contrast with vibecoding:
- **Vibecoding:** "Accept AI-generated code with minimal review"
- **Vericoding:** "Accept AI-generated code *with a machine-checked proof* that it satisfies the spec"

> *"We could just specify in a high-level, declarative way the properties that we want some piece of code to have, and then to vibe code the implementation along with a proof that it satisfies the specification."*

**Result:** We wouldn't need to review AI-generated code any more than we review compiler-generated machine code.

## Active Startups and Research

- **Aristotle** (Harmonic)
- **Logical Intelligence**
- **DeepSeek-Prover-V2** — reportedly achieving strong results writing Lean proofs
- **Galois** — Claude proving capabilities
- **Auto-Verus** — Uses automated metrics to filter LLM-generated specs/proofs, achieving 3.6x higher proof accuracy than GPT-4o zero-shot
- **Mistral Leanstral** (April 2026) — Applies LLMs to formal proof generation using Lean 4 proof assistant. Announced by Guillaume Lample (Mistral Chief Scientist). Key innovation: using formal proof as a proxy for long-horizon reasoning capability, with agent decomposition strategy (models autonomously decompose complex theorems into parallel sub-lemmas). Connects to Mistral's "AI for Science" initiative and their open-source mission. See [[entities/mistral-ai]] for details.

## Verified Generation: Formal Proof as RL Reward Signal

Axiom Math (CEO Carina Hong) has introduced **Verified Generation**, a paradigm that uses formal proof checking (Lean proof assistant) as a *reward signal for reinforcement learning training*. This departs from traditional GRPO/RLHF approaches where the reward model is statistical (a learned neural network) by substituting a deterministic, mechanically verifiable oracle.

### Core Insight

The key innovation is recognizing that formal proof checkers solve the **reward model reliability problem** inherent to RLHF:

| Approach | Reward Signal | Verifiability | Failure Mode |
|----------|---------------|---------------|--------------|
| RLHF/GRPO | Learned preference model | Statistical | Reward hacking, reward model misspecification |
| Verified Generation | Lean proof checker | Deterministic | Proof checker is small, verified, accepts only valid proofs |

The proof checker is small, verified code that mechanically rejects invalid proofs — eliminating the possibility of reward hacking that plagues neural reward models.

### Ramanujan's Example: Discovery Through Proof

Hong uses the example of Srinivasa Ramanujan's mathematical discoveries to illustrate the thesis:

- Ramanujan discovered deep mathematical truths through intuition, but lacked rigorous proofs
- G.H. Hardy and others later proved his results, creating a feedback loop between discovery and verification
- Verified Generation applies this pattern to AI: the model generates candidate solutions + proofs, and only solutions accompanied by mechanically verified proofs are kept as training signal

### Scaling Proof and Compounding

The key claim is that formal verification allows **scaling and compounding** of discoveries:

1. Each verified proof becomes a building block for more complex proofs
2. Verified results don't need re-verification (unlike statistical models where everything is probabilistic)
3. This creates compounding returns on proof effort — similar to how Lean's mathlib provides reusable theorem infrastructure

### Relation to Existing Approaches

| Approach | Focus | Tool | Verification |
|----------|-------|------|--------------|
| AlphaProof (Google DeepMind) | Theorem proving search | Lean | Post-hoc proof verification |
| DeepSeek-Prover-V2 | Lean proof generation | Lean | Automated proof checking |
| Vericoding | Code correctness proofs | Various | Code specification correctness |
| **Axiom Math Verified Generation** | **RL training signal** | **Lean** | **Proof-checker-as-reward** |

The fundamental distinction: AlphaProof/DeepSeek-Prover search for proofs; Vericoding proves code correctness; Verified Generation uses proof checking *to train the model itself*.

### Relevance to AI Safety

Verified Generation offers an alternative safety path: instead of relying on learned reward models that can be gamed, use formal verification as the training signal. This connects to [[concepts/security-and-governance/ai-safety]] debates about whether learned or symbolic approaches provide better alignment guarantees.

See also: [[entities/axiom-math]] for company details and Carina Hong's broader thesis.

## The Remaining Challenge: Intent Formalization

Even with AI writing proofs, **writing correct specifications** is still hard. The problem shifts:

- Before AI: Proving was the bottleneck (required PhD-level expertise)
- After AI: Writing specs is the bottleneck (requires translating human intent to formal logic)
- This is the **intent formalization** problem

See [[concepts/intent-formalization]] for details on this complementary challenge.

## Relevance to AI Agents

For AI coding agents, formal verification is particularly relevant because:
- **Safety-critical code** (autonomous vehicles, medical devices) must be provably correct
- **Security-critical code** (authentication, cryptography) must not have subtle bugs
- **Agentic workflows** where AI makes consequential decisions benefit from verified guardrails

## Anthropic × Theorem: Proof at Assembly Scale (October 2026)

Anthropic's research post **"LLMs can now write formal proofs at scale"**
(2026-10-22, with collaboration from **Theorem**; HN 451 points) is the first
large-scale application of AI formal verification to production software **at the
assembly level**. Claude autonomously proved security properties on compiled
**RISC-V** binaries across **123 OSS-Fuzz libraries** — ~**239 fuzz-test entry
points** — yielding ~**180M lines of Rocq** proofs (median proof ~600K lines over
binaries of ~18K RISC-V instructions). Full text:
`raw/articles/2026-10-22_anthropic-formal-verification-scale.md`.

### Method: fuzz test → spec → proof

- Existing developer-written **fuzz tests** are mechanically converted into formal
  specs: "this test suite always passes for every input < 64 MB" against a formal
  model of RISC-V + Linux process semantics. If the spec is proven, fuzzing that
  entry point is *superfluous* — no future input can crash it.
- Proven at the **binary level**, sidestepping rewrites in verification languages
  (contrast seL4's 20 person-years). The only artifacts to trust: the RISC-V/Linux
  formal models, the theorem statements, and the **Rocq proof checker** (which
  mechanically verifies the proofs — virtually no human review needed).
- Claude found and patched bugs **during** proof attempts — including bugs fuzzers
  structurally miss: a counter-underflow → out-of-bounds write needing ~20 MB
  inputs with a rare layout; an OOB read needing 64 MB input + 2 GB memory; a
  rediscovery of CVE-2026-56132 (libexpat, deeply nested input); and non-crashing
  logic bugs (a file-restriction feature not always enforced). Proving one library
  memory-safe required proving libc++'s red-black tree rebalancing keeps tree depth
  logarithmic — on machine code.

### Other experiments in the post

- **zlib spec conformance**: Claude wrote a formal spec of RFC 1950 and proved the
  Linux-kernel zlib x86 binary implements it — using Claude-generated x86 ISA
  semantics that, when single-stepped, boot an Ubuntu userspace. The semantics
  generation found hundreds of errors in official ISA documentation and a few
  hardware bugs.
- **Python-in-Rust interpreter** verified with **Verus** against CPython semantics
  from an academic paper: 99.95% behavioral agreement across 1.7M random programs,
  remainder known corner cases.
- **PDF reader audit**: as many security bugs found in one week as typically
  reported per year; one latent logic bug >10 years old.

### Economics

- Proofs cost **hundreds of millions of tokens** — the binding constraint. On 36
  real OSS-Fuzz tasks, **Opus 5.5 proves ~half with ~40% fewer tokens than Opus 5**;
  efficiency gains expected as models train on long verification tasks.
- **Shared proof workspace**: agents copying/adapting each other's proofs needed
  **17% fewer tokens** (some succeeded after solo failure); most proof bulk is
  C-runtime/ASan initialization, so disparate programs share proof mass — the
  Mathlib effect (previously ~300K theorems, 700+ contributors) arriving for
  software verification. Dependencies follow a power law: verify glibc/OpenSSL/cURL
  once and a huge swath of software becomes provable (Theorem's Nix-ecosystem
  roadmap).

### Limits (the post's own honesty section)

- "Formally verified" ≠ bug-free: a checker can't validate that the **spec matches
  reality** — proofs assume single-threaded static musl binaries on RISC-V, while
  deployments are x86/ARM dynamic glibc.
- Scope gaps: ASan doesn't catch all memory-safety bugs; not all entry points were
  proved; caller misuse of libraries is out of scope.
- **Reward hacking** risk when Claude patches code to make specs provable was
  mitigated by penalizing patches, granting credit for minimal input-changing
  patches, and auditing them.

### Assessment

This is the strongest evidence to date that the "verification as a commodity"
trajectory — from Airbus-avionics-only practice to CI-grade guarantee — is real.
The complementary Anthropic effort, [[concepts/attack-surface-reduction-llm|attack
surface reduction]], shrinks what's reachable while proofs eliminate bug classes;
together they form the lab's full cyberdefense portfolio. Watch for: x86/ARM
semantics coverage, multi-threaded support, Theorem's hosted pipeline adoption,
and the public Claude verification skill's uptake.

## Related Concepts

- [[concepts/intent-formalization]] — The complementary challenge
- [[concepts/formal-methods]] — Foundational formal methods practice and theory
- [[concepts/neurosymbolic-ai]] — Symbolic reasoning (formal logic) combined with neural networks
- [[concepts/security-and-governance/ai-safety]] — Alignment and oversight for AI agents
- [[concepts/security-and-governance/agent-sandboxing]] — Isolation for untrusted code (complementary safety approach)
- [[entities/hillel-wayne]] — Formal methods practitioner bridging academic and industry
- [[entities/john-d-cook-applied-mathematics-consulting]] — Formal verification in high-stakes engineering