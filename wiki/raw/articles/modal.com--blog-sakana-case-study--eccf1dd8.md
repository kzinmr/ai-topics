---
title: "Launching a trillion-parameter model at Sakana AI"
url: "https://modal.com/blog/sakana-case-study"
fetched_at: 2026-10-29T10:01:28.306135+00:00
source: "Modal Blog"
tags: [blog, raw]
---

# Launching a trillion-parameter model at Sakana AI

Source: https://modal.com/blog/sakana-case-study

Deploying a ~1-trillion parameter Mixture-of-Experts (MoE) model for API inference is a classic systems challenge. At full FP16 or BF16 precision, the memory footprint requires very large clusters. Standard post-training quantization (PTQ) recipes shrink that footprint but can degrade model quality, especially for non-English models, where the usual quantization calibration datasets don’t capture language register or tool-calling behavior.
Ahead of the launch of
Sakana Namazu
, a ~1T parameter model optimized for Japanese business context, live web search, and code execution, Modal's forward deployed engineering team worked directly with Sakana AI to get their model running on Modal.
We tuned NVFP4 quantization for Japanese language retention and trained a custom speculative draft model on raw token streams. This ran on Modal’s global GPU pool so Sakana could launch their public API without committing to reserved capacity.
Here’s how we optimized the serving stack down to the kernel level.
Quantization without compromise
A ~1T-parameter model at full precision has an enormous GPU memory footprint. Serving it economically at production-scale essentially requires quantization. However, quantization carries a risk. Compression methods are usually validated on English benchmarks, so a model can pass the standard checks while losing the capabilities that set it apart.
Working together, Modal was able to serve Sakana Namazu on NVFP4, the lower-precision format built for NVIDIA Blackwell GPUs, cutting memory and increasing throughput.
Rather than applying an off-the-shelf quantization recipe, Modal's Forward Deployed Engineering team started by measuring how Sakana Namazu's weights responded to compression under NVFP4 numerics, then built the approach around what they found:
Selective expert quantization:
Only the routed experts, which hold the bulk of the parameters, were quantized. Attention, the router, and the shared experts stayed at higher precision (BF16).
Domain-representative calibration data:
Calibration ran on conversations following Sakana Namazu's style, weighted heavily toward Japanese, so that every single one of the model's
23,040 experts
saw representative traffic before its scales were fixed.
The outcome was a model that matched Sakana's production checkpoint on Japanese instruction following, within the noise floor of the
Sakana's own published benchmarks
, while running at NVFP4 speed and memory.
A draft model trained on Sakana Namazu's representative traffic
Speculative decoding is a technique to speed up generation by having a small draft model guess several tokens ahead and the main model verify them in one step. The more of those guesses the main model accepts, the faster each request runs. As we’ve said before,
speculation is all you need.
Generic draft models are trained on generic text, so they guess Sakana Namazu's Japanese business register poorly (yielding acceptance rates under 40%). Modal's team trained a
custom DFlash
draft model on Sakana Namazu's representative traffic instead.
The key implementation detail was training on the exact token IDs the model produced, not on text that had been decoded and re-tokenized. The two look identical on the page, but re-tokenizing destroys exact token boundary alignments inside tool calls, JSON schemas, and the model's reasoning markers. That gap costs token acceptance. Modal built the capture path so that raw token IDs flowed directly from production into a training corpus of more than 30 billion tokens. Here are the results:
+25% increase
in speculative token acceptance rate over a generic draft model
~35% drop
in per-token decode latency
~40% more traffic per replica
before queue latencies start to climb, letting Sakana serve launch-day demand with fewer GPUs
Since launch, more improvements have been made to the drafter. The first version was trained before Sakana Namazu had served a single public request, so it learned from representative traffic rather than the real thing. Once production traffic was flowing, Modal’s team trained a second drafter from scratch on roughly 1M real requests.
It uses DFlash2, a newer architecture that holds up better when customers sample at nonzero temperatures, which covers most of Sakana Namazu’s traffic. To measure it, we ran two identical copies of Sakana Namazu’s serving setup, one with each drafter. We then replayed 1,000 held-out requests through both, using the sampling settings Sakana’s customers actually send. The new drafter had never seen these requests during training. Average acceptance length (how many drafted tokens the main model accepts per step) rose from 3.51 to 5.01, a 43% gain, and p99 latency fell from 68s to 52s.
Performance work over new engine releases
Serving stacks move fast, and each release changes kernels, scheduling, and numerics in ways that only show up under production traffic. Modal and Sakana worked together to test and benchmark these changes and safely deploy them to Sakana’s workloads, A/B testing them on the same hardware and the same batch of requests.
The biggest gains came from:
Removing a CPU–GPU synchronization stall in the speculative decoding loop.
Each decode step had been pausing while the CPU read back results from the GPU. Eliminating that wait cut GPU idle time per step by >90%.
Routing NVFP4 mixture-of-experts math to faster kernels.
Newer kernel paths for the expert matrix multiplies, which account for about 60% of each decode step, shortened step time and, as a side effect of tighter numerics, raised draft acceptance by 9% with the same draft model.
Caching prefill dispatch and expert runner setup.
Work that had been repeated on every request was done once and reused, which mostly benefited time to first token.
Correctness across GPUs
Sakana Namazu runs across four GPUs with tensor parallelism, and speculative decoding adds a subtlety: every GPU has to agree on which drafted tokens were accepted. Modal instrumented the verification step across ranks, found a rare path where they could disagree, and made acceptance a single shared decision. The result was a class of rare stalls eliminated entirely, with no change to output quality.
The team also extended speculative decoding to structured output. Sakana Namazu's API customers rely on JSON-schema responses for tool use, and Modal made grammar-constrained generation work inside the speculative path so those requests get the same speedup with zero schema violations.
Smarter router across replicas and autoscaling
After launch, Modal enabled its in-house
KV-aware router
on Sakana's deployment without requiring any code changes on Sakana's side.
Rather than distributing requests evenly, the router sends each request to the replica most likely to already have its prompt prefix cached while balancing load as replicas scale up and down.
The impact was immediate in the tail latencies. Time-to-first-token (TTFT) spikes that had reached several minutes disappeared, per-replica queues fell to near zero, and end-to-end tail latency improved, while per-token decode speed remained unchanged.
Managing capacity planning with on-demand GPUs
Moving a mission-critical workload onto new infrastructure is a hard sell for any frontier AI lab. To secure the amount of GPUs needed often requires a long-term contract or steep reservation.
Since the new commercial API service for Sakana Namazu hadn’t received any requests yet, this path would’ve been risky. Modal allowed them to elastically scale to meet the demand generated during launch, without worrying about over-provisioning or slow autoscaling.
“For Sakana Namazu, we needed the flexibility to scale GPU capacity up or down without compromising model quality. Modal gave us that flexibility, and their engineers worked directly with us to address the performance changes introduced by quantization.”
Masaya Ohagi
Applied Research Engineer
What this means beyond Sakana Namazu
Sakana Namazu now runs in production on infrastructure that was co-optimized around it: NVFP4 quantization tuned for Japanese retention, a speculative draft model trained on Sakana's raw token streams, and serverless capacity that scales dynamically with launch demand instead of a reservation signed months in advance.
As one of Japan's leading AI labs, Sakana's research team is now exploring additional workloads on Modal beyond the original API.
We’re excited to see what Sakana ships next!
