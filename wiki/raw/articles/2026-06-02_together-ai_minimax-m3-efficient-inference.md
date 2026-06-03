---
title: "Serving MiniMax-M3 for efficient inference: Unlocking 1M-Token Context and Multimodality Without Regrets"
source: "https://www.together.ai/blog/serving-minimax-m3-for-efficient-inference-unlocking-1m-token-context-and-multimodality-without-regrets"
date_published: "2026-06-02"
date_ingested: "2026-06-03"
type: raw_article
tags: [minimax, inference, multimodal, long-context, together-ai]
---

# Serving MiniMax-M3 for efficient inference: Unlocking 1M-Token Context and Multimodality Without Regrets

**Source:** <https://www.together.ai/blog/serving-minimax-m3-for-efficient-inference-unlocking-1m-token-context-and-multimodality-without-regrets>
**Published:** 2026-06-02
**Description:** (no desc)

Serving MiniMax-M3 for efficient inference: Unlocking 1M-Token Context and Multimodality Without Regrets

⚡️ FlashAttention-4: up to 1.3× faster than cuDNN on NVIDIA Blackwell →

Introducing Together AI's new look →

🔎 ATLAS: runtime-learning accelerators delivering up to 4x faster LLM inference →

⚡ Together GPU Clusters: self-service NVIDIA GPUs, now generally available →

📦 Batch Inference API: Process billions of tokens at 50% lower cost for most models →

🪛 Fine-Tuning Platform Upgrades: Larger Models, Longer Contexts →

All blog posts

Inference

Published

6/2/2026

Serving MiniMax-M3 for efficient inference: Unlocking 1M-Token Context and Multimodality Without Regrets

Authors

Yubo Wang, Michael Granado, Connor Li, Jue Wang, Brian Mak, Wei Gong, Hiral Jasani, Yineng Zhang, Dan Fu

Table of contents

40+ Models Chosen for Production...40+ Models Chosen for Production...40+ Models Chosen for Production...

Together AI is the preferred cloud partner for MiniMax M3.

Together AI will host the open-weights model as a developer endpoint upon its public release.

Our Inference and Kernel teams delivered

significant engineering breakthroughs to serve M3 efficiently

, including key optimizations such as a KV-Block-Major sparse attention kernel, a novel paged attention integration for MSA, highly optimized index scoring kernel and a Rust-based multimodal preprocessing gateway, resulting in

81–125% throughput improvements

across different concurrency levels.

Serving

MiniMax M3 at scale in production validates Together AI as the go-to inference platform

for models that push the frontier on the hard systems problems that make real-world deployment possible.

MiniMax launched their latest state-of-the-art model M3 and Together AI is excited to be the preferred cloud partner, enabling MiniMax to efficiently serve M3 in production at scale. Once MiniMax M3 is released as an open weights model over the coming few days, Together AI will also host the model as an endpoint for developers directly. Behind that scale is the exceptional work of our Inference and Kernel teams, who drove deep performance optimizations and ensured production-grade reliability for a model that pushes the frontier: 1M-token context window, native multimodality, and an architecture that demands serious engineering to serve efficiently. In this post, we'll walk through how we made it happen. Congratulations to the MiniMax team on a landmark model launch and continued innovation.

MiniMax M3 is an all-in-one model that brings together state-of-the-art coding performance, agentic workflow support, and native multimodal reasoning. On top of these capabilities, it is also designed to support 1M context while being highly economically friendly to serve. This makes it a good fit for real-world tasks where long documents, codebases, tool use, images, and iterative reasoning often appear together and heavy in context. Compared to the previous generation, serving M3 imposes more challenges as new capabilities require optimizations on  more dimensions including sparse attention computation, larger KV cache management, multimodal processing, etc.

Architecture / Characteristics

The most novel architectural change in M3 is MiniMax Sparse Attention (MSA), which is designed to address the attention-computation bottleneck seen in MiniMax M2.7. Its block-sparse attention mechanism caps the maximum number of tokens each query can attend to, reducing the cost of long-context processing and making much longer context windows practical. This brings a speed up of more than 9x in the prefilling stage and more than 15x in the decoding stage.

In essence, MSA’s calculation is composed of two parts: a score calculation to determine the most relevant K blocks to attend to for each KV group, and then dense attention between the query token and those blocks. This design preserves expressiveness along the KV-group dimension while still putting a limit on the maximum number of KV tokens a query token attends to. The attention computation itself no longer scales as N^2 with context length, thus making it very suitable for long context workload.

We measured the kernel execution time breakdowns under agentic-style traffic shape(60k prefix cache) under concurrency of 8 on B200. MSA significantly lowers the wall time percent of the actual attention computation per iteration.

A separate kernel execution breakdown under agentic-style traffic with 60K prefix cache, concurrency 8, and NVIDIA B200 showed that MSA significantly reduces the wall-time percentage spent in attention computation per iteration.

Besides the attention architecture change, M3 is also shipped with multimodal support with a vision component and new image and video preprocessing functionalities.

Given these fundamental changes, Together AI worked closely with MiniMax’s engineering team to tackle the new emerging challenges. Some major challenges include:

Though MiniMax sparse attention computation itself is highly efficient, supporting 1M context length is still challenging from an engineering perspective.

Video and image processing are natively more complicated than text tokenization.

Optimizations

KV-Block-Major Sparse Attention

During prefill, attention computation can still be a big factor for long context input, as for each token, we need to calculate Selected

Block

KV Head Group

Tokens

. The nature of the block sparse attention allows multiple queries to attend to the same key-value blocks. Thus, if we iterate each query to calculate attention with key-value blocks, we are duplicating the KV movement from HBM to SRAM on GPU. Iterating over the key-value group in the outer loop and calculating attention between query tokens  in the inner loop allows better arithmetic intensity as KV cache is moved only once.

To achieve this, we need to reorganize the mapping from {q, kv block} into {kv block, q} and reimplement the attention kernel. Because we are calculating only partial O output for the kv block, we need a final “reduction” based on the Log-Sum-Exp to rescale output O and sum. The process is as follows:

Integrate MSA with Paged Attention

In modern inference engines, paged attention is often used to manage KV cache context for requests. The majority of highly optimized attention kernels are written with a fixed set of page size support. The blocker that stops us from using these kernels is that the selected blocks differ across KV groups.

At Together AI, we propose a new way to integrate MiniMax Sparse Attention into the engine. During decode, we first build a page table based on the selected blocks, flatten the KV-group dimension into the batch dimension, and leverage the strided view of a KV cache tensor to provide the attention kernel with the pointer needed to retrieve the KV page. The trick is the stride: page addresses advance by D to choose a virtual page start, while tokens advance by Hkv * D. That deinterleaves one physical tensor into per-head pages, so each flattened row can now use a different page table.

This design unblocked us to use the existing attention kernels that support GQA without having to rewrite a new one that supports sparse attention from scratch. Because the selected blocks for each query is limited, the kernels to find mapping between blocks to pages are with very low overhead. This design gives us 5% improvement on the decode throughput.

Decode Index Scoring Kernel Optimization

For decode, MSA moves a large part of the cost out of dense attention and into the score/top-k indexer. For every decode query, the engine compares the query-side index vector against candidate key-side index vectors, reduces each 128-token KV block to a single score, and keeps only the top blocks for the real attention kernel. This scan is on the critical path for every generated token, and at long context lengths the number of candidate blocks grows with context length. Decode scoring has a small-query-index, long-key-index shape. It is tempting to treat a batch of decode queries as one larger GEMM, but the score/indexing step is not just a dense matrix multiply: each request and K group has its own candidate block range, masking, per-block reduction, and top-k boundary. Concatenating queries together would still leave a ragged gather-and-reduce problem around the GEMM, while forcing padding and extra bookkeeping onto the critical path. Our optimized path therefore uses an

AB-swapped HMMA layout

: the 128-token key-index block becomes the MMA M dimension, while the query side is padded only into the smaller

dimension. The kernel stages 128-token K indexes with asynchronous copies, prefetches the next page, computes dot products in bfloat16 with HMMA, and reduces each page to one block score.

Multimodal Preprocessing at the Gateway

SMG (Serving Model Gateway) is a Rust-based model gateway that sits between the OpenAI-compatible API and the inference engine. Beyond routing and tokenization, SMG takes on a role that is particularly important for multimodal models: it performs all vision preprocessing on the CPU before the request reaches the GPU worker.

Image and video inputs need a fair amount of CPU work before they are useful to a vision encoder: downloading, decoding, frame sampling, resizing, and converting into patch tensors. Doing this inside the inference engine ties up resources that should be spent on generation. SMG handles all of it in the gateway instead, so by the time the request hits the GPU, the tensors are ready to go.

For M3, this means: fetch the video, pull frames out with FFmpeg, pick a subset based on FPS (Frames Per Second), resize and normalize, then patchify with the temporal dimension baked in. What comes out is a flat patch tensor and a small grid metadata tensor, packed into a gRPC message. The worker just runs the vision encoder directly — no preprocessing on its end.

Also, SMG's multimodal pipeline is structured around Rust traits that separate model-specific preprocessing logic from the pipeline plumbing. Adding M3 multimodal support meant implementing these traits with M3-specific constants; the pipeline itself did not change. The same architecture applies to the majority of open source models with vision capability, and generalizes across inference engine runtimes.

Performance Results

Since receiving the MiniMax M3 weights and model architecture, we strived to improve the inference performance. We have reached 81% - 125% increase on various concurrency levels on common agentic shape traffic.

Future Work

New architecture brings in new infrastructure and engineering challenges. At Together AI, our goal is to provide the best inference performance. A few topics that we are actively working on regarding to M3 are:

1. The sparse attention architecture introduces more smaller kernels, for example, topk over kv blocks, remapping q-kv mapping into kv-q, etc. There are more kernel fusion opportunities. Our Kernel Agent Research team is actively developing agents that write production-grade kernels.

2. CPU cache offloading of k-index and actual kv cache can now be disaggregated. We are working on loading full k-index and load kv cache on-demand based on the topk selection.

Next Steps

Join the waitlist to get notified when M3 open weights are available on Together AI

Check out the deep dive from MiniMax model designers and the Together inference team.
