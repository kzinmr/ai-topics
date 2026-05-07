---
title: "Napkin Math For Finetuning"
presenter: Jonathan Whitaker (@johnowhitaker)
type: slides
source: https://docs.google.com/presentation/d/1Ye_6zeatCWkq-fx8A--yK34uwU8oC2YQtMSTV1DgkSI/edit?slide=id.p
date_ingested: 2026-05-07
tags:
  - fine-tuning
  - training
  - memory
  - compute
  - napkin-math
  - gpu
  - lora
  - quantization
---

# Napkin Math For Finetuning

Presentation by Jonathan Whitaker (@johnowhitaker)

## Slide 1: Title

Napkin Math For Finetuning
Jonathan Whitaker | @johnowhitaker

## Slide 2: Questions

- What affects performance when fine tuning?
- How can I make it faster?
- When should I use LoRA? Quantization? GC? CPU Offloading?
- What's the cheapest option?
- What's the most accurate?
- What hardware should I use (cheapest? fastest?)
- How will changing [X] affect the training time?
- What batch size / context length / … is best?
- How do I figure out what settings to use

## Slide 3: Links

- https://johnowhitaker.dev
- https://github.com/AnswerDotAI/fsdp_qlora/blob/main/benchmarks_03_2024.md — Benchmarks for FSDP+QLoRA used in example
- https://github.com/huggingface/transformers/issues/25572#issuecomment-1687749561 — Someone showing math for activations
- https://docs.google.com/presentation/d/1Ye_6zeatCWkq-fx8A--yK34uwU8oC2YQtMSTV1DgkSI/edit?usp=sharing — These slides
- https://pytorch.org/tutorials/intermediate/optimizer_step_in_backward_tutorial.html — More use of memory viz + an under-rated technique

## Slide 4: The Good News / The Bad News

| Good News | Bad News |
|-----------|----------|
| We know how these models work | Implementation details differ |
| We can do the maths | The maths can get hard |
| We can do experiments | "I don't know what I'm doing!!!" ← us, soon ;) |

## Slide 5: It's going to be OK!

## Slide 6: The Plan

1. Intro (done ✅)
2. What happens during training/finetuning?
3. Value of running experiments
4. A small code example: instrumenting a 'training step'
5. Napkin math live-mathing to estimate memory use
6. A case study
7. Questions (ask throughout too!)

## Slide 7: Training Neural Networks (Conceptual)

- We feed some data… → Through a model… → To get an answer
- We measure how good it is.
- Then update the model…

## Slide 8: On Computers (GPU Wealth Spectrum)

- **GPU Rich** — node → node → node (multi-GPU)
- **GPU middle class** — CPU → CPU RAM → GPU → GPU RAM
- **GPU Poor** — Single GPU or CPU-only

## Slide 9: Training Neural Networks (Memory Details)

- The model takes up space
- Data takes up space
- The intermediate results (activations) take up space
- (storing gradients — more space)
- (optimizer state — more space)
- Forward pass: crunching lots of numbers
- Backward pass: tracing gradients to find out how to update

## Slide 10: What takes up time?

1. **Crunching the numbers** ← compute
2. **Copying data around** ← memory bandwidth

> Keep an eye on these two aspects.

## Slide 11-12: Why are we copying data around?

CPU ↔ CPU RAM ↔ GPU ↔ GPU RAM data transfers. Data movement between CPU and GPU (host-to-device, device-to-host) and between nodes in multi-GPU setups.

## Slide 13: Goal: keep the GPU fed

Minimize idle GPU time — maximize utilization by ensuring data and compute are always ready.

## Slide 14: Tricks at our disposal

| Technique | What it does |
|-----------|-------------|
| **Flash attention and fancy kernels** | Reducing intermediates and VRAM↔HBM with 'fused kernels', changing complexity |
| **Gradient Checkpointing (Activation Checkpointing)** | Reducing memory usage in exchange for a little more compute |
| **CPU Offloading** | Storing some things on the CPU to free up GPU RAM for more data |
| **LoRA** | Only training some parameters → less gradients, small optimizer state |
| **Quantization** | Reduces the space needed for weights (etc) but needs a little compute to dequantize |

## Slide 15: Running Experiments

> Change one thing at a time, see what it does.
> (Thank you Modal for making it easy to test on H100s!)
> Will 2x batch size give 2x speedup?

## Slide 16: A Simple Example

Training a model on one GPU:
- Forward Pass
- Backward Pass
- Effect of batch size
- Effect of context length
- Memory: constant vs scaling with data?
- Compute: how does it scale?

## Slide 17: A Case Study — 'Compute Bound' vs 'Memory Bound'

## Slide 18: Questions?
