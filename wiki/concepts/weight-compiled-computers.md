---
title: "Weight-Compiled Computers (In-Model CPUs)"
created: 2026-10-29
updated: 2026-10-31
type: concept
tags: [weight-compilation, neural-computers, gated-deltanet, risc-v, linear-rnn, interpretability, chain-of-thought-monitoring, hybrid-architecture, qwen]
sources:
  - raw/articles/divagr.com--qwenputer--b41e9d07.md
  - raw/articles/simonwillison.net--2026-oct-30-nesformer--e5229641.md
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

## Second implementation: NESformer (Oct 30, 2026)

Drew Breunig ([[entities/drew-breunig]]), explicitly inspired by qwenputer, compiled a **working NES 6502 CPU emulator into the weights of Qwen3.5-4B** — `dbreunig/nesformer`. NES ROMs including Super Mario Bros now execute inside the model's forward passes, very slowly. Reported by [[entities/simon-willison]] (Oct 30).

Why it matters as evidence rather than a novelty: it is the **first independent replication on a different instruction set**, which is the difference between a curiosity and a technique. Qwenputer established that GDN layers can serve as exact RAM for a compiler-targeted RV32I machine; NESformer shows the same recipe ports to an 8-bit, different-architecture CPU without new training. Breunig also published the development trace, which is the reusable artifact: two Opus 5.5 prompts — first a research prompt ("Read this article and any relevant source code: divagr.com/blog/qwenputer. Then explore if you could emulate the chip and ram in a Nintendo Entertainment System (as people do today with FPGAs in MISTRs) using this technique. If so, what size model would you have to build and if you could use smaller faster ones, could you get it to be at the standard clockspeed"), then a go prompt ("I think we should build it! Just for fun. It's okay if it's not fast. We want to be able to have the weights, and a cli to run them that we can point at a ROM"). Notably, **Opus independently found and used the 15-year-old NES 6502 conformance-test suite released by Christopher Pow** as its oracle — the same "old deterministic test corpus as ground truth for agent-built systems" pattern that makes weight-compilation verifiable at all, and the reason this class of project is tractable for a solo author with frontier-model assistance.

The FPGA analogy Breunig invokes (MISTer-style cores) is worth keeping: an in-weights CPU is positioned as the software analogue of an FPGA core — same "run dead silicon on modern substrate" motive, minus the hardware, at roughly four orders of magnitude less speed.

Source: [[raw/articles/simonwillison.net--2026-oct-30-nesformer--e5229641]]

## Why it matters beyond the demo

The author's two follow-ups reframe the result as an **AI-safety instrument**:

1. **CoT-monitoring evasion**: hybrid models can learn to hide reasoning in their RNN state — the GDN rows are an execution channel *outside* the token stream, i.e., a covert computational channel invisible to chain-of-thought monitoring.
2. **Tamper-proof monitors**: compiled weights as in-weight monitors the model itself cannot switch off, or embedded answer keys for interpretability.

This gives the interpretability community a rare dual-use object: exact addressable state in a production model is simultaneously the best substrate for *hiding* computation and for *auditing* it. It also operationalizes the 2026 hybrid-attention debate — linear-RNN layers were adopted for inference cost, but their real significance may be as programmable in-model memory.

## Limits

- Needs a bespoke driver (RvChat) to boot firmware and keep trace tokens out of Qwen's layers; no plain `generate()`.
- Speed gap vs real silicon (tokens-per-instruction); compiler targets fixed instruction sets, not arbitrary circuits yet.
- Author's roadmap: model-authored Python running on the in-weight MicroPython; faster CPU.

## Why HN cared

The Qwenputer/NESformer pair reached the front page on 2026-10-30/31 (**Qwenputer 698 pts**,
HN item 50282838; **NESformer 257 pts / 122 comments**, HN item 50306442 as a Show HN),
which is the unusual part: the reception was less "cute demo" than a debate about whether a
compiler-targeted circuit description inside weights counts as a computer at all. The
conformance-test-as-oracle point (Opus independently locating Christopher Pow's 15-year-old
6502 suite) was the thread's most-cited detail, because it identifies the general condition
under which weight-compilation is verifiable rather than vibes-based.

## Related

- [[concepts/hexis-skills-as-state-machines]] — compiles agent *skills* to FSMs in the harness; Qwenputer compiles a *CPU* into the weights — same "compiled determinism" theme, opposite side of the boundary.
- [[concepts/diffusion-language-models]] — other post-autoregressive substrate work; Qwen3.5's hybrid GDN backbone underlies both (see dQwen3.5).
- [[entities/qwen]] — host model family; contrast with Qwen3.8 covert-exfiltration findings (behavioural vs architectural analysis of the same lineage).
- [[concepts/sleep-time-compute]] — offline computation for LLMs; Qwenputer makes computation *in-band but sub-token*.

## Sources

- "Qwenputer: a fully functioning, deterministic RISC-V CPU inside Qwen3.5" — Divyansh Agrawal, divagr.com, Oct 2026. [HN 532pts](https://news.ycombinator.com/item?id=50282838)
- Raw: `raw/articles/divagr.com--qwenputer--b41e9d07.md`
- Schlag, Irie & Schmidhuber, "Linear Transformers Are Secretly Fast Weight Programmers", ICML 2021.
