---
title: "Inkling by Thinking Machines now available on Modal"
url: "https://modal.com/blog/inkling-by-thinking-machines-labs-now-available-on-modal"
fetched_at: 2026-07-16T07:01:40.289742+00:00
source: "Modal Blog"
tags: [blog, raw]
---

# Inkling by Thinking Machines now available on Modal

Source: https://modal.com/blog/inkling-by-thinking-machines-labs-now-available-on-modal

Today
Thinking Machines released Inkling
, a general-purpose multimodal model that accepts text, image and audio inputs and generates text outputs.
We partnered with Thinking Machines on day zero support, making Inkling available as a Managed Endpoint with token-based pricing.
Try it now
or read on for why we think this model, and its architecture, matter.
Inkling: The start of something great
Thinking Machines named this model Inkling because it’s “the inception of an idea that might turn into something great.” We couldn’t agree more.
As a mixture-of-experts transformer with 975B total parameters, 41B active, a 1M token context window, and native audio and vision, Inkling is trained from the start for breadth over depth. This makes it a great base model for further training.
It also makes Inkling fast by design. Sparse experts keep active parameters low, and its local attention layout keeps compute and memory flat as sequences grow. For endpoints on Modal, we took this even further with Day 0 support for a custom
DFlash
speculator tuned to this model shape.
On agentic workloads on 8x B200s, we saw 250 tokens per second per user at 2.5M TPM of per-GPU throughput, 67% faster interactivity than the model's built-in speculative path at matched throughput.
Towards local attention: Evolving DFlash speculation for frontier attention models
Inkling’s unique architecture moves in a direction that maximizes compute efficiency by shifting to a local attention layout. For every six attention layers, five use sliding window attention over recent tokens and one uses full attention over the whole sequence. In practice, by biasing more of the model’s compute on recent tokens, the model itself achieves greater efficiency.
This kind of speedup is happening across the board, frontier open models keep getting faster at the same parameter size: Qwen 3.5 and 3.6 did it using Gated DeltaNet linear attention layers, and Inkling pushes the same idea further and better, with five sliding window layers for every global one. This speedup is great, but it means speculative decoding techniques must get faster too.
Inkling, like most current open models, includes a multi-token prediction (MTP) head that can draft for speculative decoding. But MTP heads draft one token at a time, taking up more time and space on the GPU, causing the performance to hit a ceiling — in our benchmarks, pushing MTP past a few draft steps made it slower.
DFlash
, the speculative decoding technique by
Z Lab
, is designed differently. Its block diffusion drafter generates a whole block of tokens in one parallel forward pass, conditioned on features from the target model. And in the latest draft models
we’ve released on Hugging Face
, we’re making a similar bet towards local attention, just like Inkling.
We're able to push DFlash in a few ways to maximize speed and compute efficiency (without losing accuracy):
All local attention.
Every drafter layer uses sliding window attention, with no global attention at all. The drafter can afford it because it conditions on the target model's features for long-range context, and drafting depends mostly on recent tokens.
Causal layers for better kernel support.
We changed the drafter's layers from non-causal to causal, so it can run on highly optimized attention kernels at inference time, such as
trtllm
.
We made an early bet on DFlash because we recognized the future potential of block diffusion drafting: a speculator whose cost stays flat as blocks grow, and whose architecture can keep shedding compute as fast as its targets do. We believe it is the right
architecture for speculation
for compatible models. We expect this model shape to keep spreading across the open frontier, and we will keep pushing DFlash to its limits to match it.
Run Inkling now with Modal Auto Endpoints
Inkling is
available today
as an OpenAI compatible shared endpoint through Modal Auto Endpoints.
Try it today and let us know what you think!
