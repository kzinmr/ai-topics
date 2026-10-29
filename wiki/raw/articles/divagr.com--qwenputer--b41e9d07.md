---
source_url: https://divagr.com/blog/qwenputer
fetched: 2026-10-29 12:05 UTC
extraction: urllib-chrome-ua-strip-html
title: "Qwenputer: a fully functioning, deterministic RISC-V CPU inside Qwen3.5"
author: Divyansh Agrawal (divagr)
published: 2026-10-28/29
hn: https://news.ycombinator.com/item?id=50282838
sha256: 7ddad50031d61780aea9a8a67828e2e8a42a11bfcab3148aa80a411617b5c141
---

# Qwenputer: a fully functioning, deterministic RISC-V CPU inside Qwen3.5

## I can't believe it's not silicon

Qwenputer is a pretty fun experimental model. It's a stock Qwen 3.5 4B with one addition: a RISC-V CPU embedded within the weights that uses the model's own Gated DeltaNet attention layers as RAM. This 'CPU' runs completely within the forward passes of the model, and can run arithmetic operations, C and MicroPython code without any external runtime or tool usage whatsoever.

To be very clear, it is not a plugin, a tool or a sandbox. The model utilises GDN layers as RAM, and an experimental in-model file storage was also slotted in.

Two follow-ups built on top of Qwenputer: (1) how hybrid models can learn to hide their reasoning in their RNN state and evade CoT monitoring, and (2) how compiled weights like these can work as inbuilt monitoring tools that the model itself can't tamper with.

Models: Hugging Face / ModelScope (`divagr1925/Qwen3.5-4B-Qwenputer`, plus a Filesystem variant); code on GitHub (divagr18/qwenputer, chipformer).

## The RNN inside Qwen3.5 can be exact RAM

Qwen3-Next and Qwen 3.5 use Gated DeltaNet, a linear RNN, as the attention mechanism for 3 out of 4 layers. Each head keeps a state matrix, and the delta rule keeps it updated.

Key trick: set the gate to 1 (nothing ever fades), write strength (beta) to 1 (old value along that direction is replaced completely), and use one-hot key encoding — every write overwrites exactly one row, every one-hot query retrieves an exact value. The GDN layers themselves then work exactly as RAM, at far lower cost than using attention as RAM, since a GDN head's state stays constant-size regardless of conversation length (unlike attention's KV cache).

Prior art: Schlag, Irie & Schmidhuber (ICML 2021), "Linear Transformers Are Secretly Fast Weight Programmers" — linear attention with the delta rule as associative memory / "fast weights". The new thing: making it exact and addressable, inside a production model, reliably enough to run a whole CPU on it. Default Qwen 3.5 does not keep exact values in the GDN; with this modification it does.

## Compiling a computer into layers

No training involved: a compiler sets every weight directly. You describe the CPU as a circuit — a long list of small steps ("read this register", "add these two numbers", "jump if zero") — and the compiler turns each step into a piece of a transformer layer: attention heads that look things up, feed-forward units that do the arithmetic, and DeltaNet heads that hold the RAM. The CPU runs as the model decodes. Each instruction becomes a few generated tokens; the CPU is free-running (keeps going on its own outputs with no reference machine correcting it between steps).

The CPU: RV32I RISC-V, registers/memory/program counter kept in GDN rows; runs arithmetic, C and MicroPython; supports an in-model file storage / hard drive.

## Performance & limits

Runs on a single 24 GB GPU. Needs a small driver (RvChat) to boot the firmware and keep trace tokens out of Qwen's layers, so it doesn't run with a plain generate() call yet. Slow: every CPU instruction costs a few decoded tokens; the batched executor runs ~3,200 CPU tokens/sec on an L4 — a big calculation takes seconds rather than milliseconds.

## Beyond arithmetic (AI safety angle)

Exact control over the RNN layers is useful beyond arithmetic — Qwenputer is a testbed for AI safety research. Two follow-ups:
1. How hybrid models like Qwen 3.5 can learn to hide their reasoning in their RNN state and evade chain-of-thought monitoring.
2. How compiled weights can work as monitorability tools: an in-weight monitor the model can't switch off, or answer keys for interpretability.

Next: Qwen writing Python and running it on the MicroPython inside its own weights via a python() tool; making the CPU faster.

Cite: @software{agrawal2026qwenputer, author = {Agrawal, Divyansh}, title = {Qwenputer: a computer compiled into the weights of a pretrained language model}, year = {2026}, url = {https://github.com/divagr18/qwenputer}}
