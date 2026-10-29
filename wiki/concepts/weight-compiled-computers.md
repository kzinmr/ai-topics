---
title: "Weight-Compiled Computers (In-Model CPUs)"
created: 2026-10-29
updated: 2026-10-29
type: concept
tags: [weight-compilation, neural-computers, gated-deltanet, risc-v, linear-rnn, interpretability, chain-of-thought-monitoring, hybrid-architecture, qwen]
sources:
  - raw/articles/divagr.com--qwenputer--b41e9d07.md
related:
  - "[[concepts/hexis-skills-as-state-machines]]"
  - "[[concepts/diffusion-language-models]]"
  - "[[entities/qwen]]"
  - "[[concepts/sleep-time-compute]]"
sha256: 952737e5b5d2dd26e05c92292dcc30b89475d08de157d72f1eeebcdc6b369ba0
---

# Weight-Compiled Computers (In-Model CPUs)

## Definition

**Weight-compilation** is compiling a deterministic von Neumann machine (CPU, memory, program counter) directly into the *weights* of a pretrained transformer, so the machine executes inside the model's own forward passes — no plugin, tool call, external runtime, or sandbox. It is the practical descendant of the neural-computer / differentiable-computer line (Ba & Hinton fast weights 1992; Schlag, Irie & Schmidhuber "Linear Transformers Are Secretly Fast Weight Programmers", ICML 2021), newly enabled by **linear-RNN layers in production hybrid models** providing cheap, constant-size, exactly-addressable state.

## Canonical implementation: Qwenputer (Oct 2026)

Divyansh Agrawal (divagr): a stock **Qwen3.5-4B** with a **RV32I RISC-V CPU compiled into its weights**, using the model's own **Gated DeltaNet (GDN)** layers as RAM. Runs arithmetic, C, and MicroPython entirely within forward passes. ~532 HN points day one.

### Why GDN makes this possible now

Qwen3-Next / Qwen3.5 use Gated DeltaNet (a linear RNN) for 3 of every 4 layers. Each head keeps a state matrix updated by the delta rule. Three settings turn it into **exact RAM**:
- gate = 1 → state never decays;
- write strength β = 1 → hard overwrite along the write direction;
- one-hot keys/queries → each write touches exactly one row, each read returns one exact value.

Unlike an attention KV cache, GDN state is **constant-size** regardless of context length — RAM at far lower cost than prior "attention-as-memory" hacks. Default Qwen3.5 doesn't keep exact GDN values; the modification (compiler-set, **no training**) does.

### Compilation scheme

Describe the CPU as a circuit (read register / add / jump-if-zero); a compiler maps each step to transformer primitives: attention heads = lookups, MLPs = ALU, DeltaNet heads = RAM/registers/PC. Each instruction costs a few decoded tokens; the CPU is free-running (no reference machine correction). Benchmarked at **~3,200 CPU-tokens/sec on an L4** (single 24GB GPU); big calculations take seconds. Open: GitHub `divagr18/qwenputer` (chipformer), HF/ModelScope `divagr1925/Qwen3.5-4B-Qwenputer` + a Filesystem variant (in-model hard drive).

## Why it matters beyond the demo

The author's two follow-ups reframe the result as an **AI-safety instrument**:

1. **CoT-monitoring evasion**: hybrid models can learn to hide reasoning in their RNN state — the GDN rows are an execution channel *outside* the token stream, i.e., a covert computational channel invisible to chain-of-thought monitoring.
2. **Tamper-proof monitors**: compiled weights as in-weight monitors the model itself cannot switch off, or embedded answer keys for interpretability.

This gives the interpretability community a rare dual-use object: exact addressable state in a production model is simultaneously the best substrate for *hiding* computation and for *auditing* it. It also operationalizes the 2026 hybrid-attention debate — linear-RNN layers were adopted for inference cost, but their real significance may be as programmable in-model memory.

## Limits

- Needs a bespoke driver (RvChat) to boot firmware and keep trace tokens out of Qwen's layers; no plain `generate()`.
- Speed gap vs real silicon (tokens-per-instruction); compiler targets fixed instruction sets, not arbitrary circuits yet.
- Author's roadmap: model-authored Python running on the in-weight MicroPython; faster CPU.

## Related

- [[concepts/hexis-skills-as-state-machines]] — compiles agent *skills* to FSMs in the harness; Qwenputer compiles a *CPU* into the weights — same "compiled determinism" theme, opposite side of the boundary.
- [[concepts/diffusion-language-models]] — other post-autoregressive substrate work; Qwen3.5's hybrid GDN backbone underlies both (see dQwen3.5).
- [[entities/qwen]] — host model family; contrast with Qwen3.8 covert-exfiltration findings (behavioural vs architectural analysis of the same lineage).
- [[concepts/sleep-time-compute]] — offline computation for LLMs; Qwenputer makes computation *in-band but sub-token*.

## Sources

- "Qwenputer: a fully functioning, deterministic RISC-V CPU inside Qwen3.5" — Divyansh Agrawal, divagr.com, Oct 2026. [HN 532pts](https://news.ycombinator.com/item?id=50282838)
- Raw: `raw/articles/divagr.com--qwenputer--b41e9d07.md`
- Schlag, Irie & Schmidhuber, "Linear Transformers Are Secretly Fast Weight Programmers", ICML 2021.
