---
title: "Optimizing MiniMax M3 Sparse Attention on NVIDIA Blackwell"
source: "Fireworks AI Blog"
url: "https://fireworks.ai/blog/kernel-optimization-for-minimax-m3-on-nvidia-blackwell"
scraped: "2026-07-11T06:00:41.685679+00:00"
lastmod: "2026-07-10T20:40:16.000Z"
type: "sitemap"
---

# Optimizing MiniMax M3 Sparse Attention on NVIDIA Blackwell

**Source**: [https://fireworks.ai/blog/kernel-optimization-for-minimax-m3-on-nvidia-blackwell](https://fireworks.ai/blog/kernel-optimization-for-minimax-m3-on-nvidia-blackwell)

GLM 5.2 Fast is available! Opus-level intelligence at open-source rates. No contracts, pay per token. Start building.
Platform
Models
Developers
Pricing
Training
Partners
Resources
Company
Log In
Get Started
Blog
Kernel Optimization For Minimax M3 On Nvidia Blackwell
Optimizing MiniMax M3 Sparse Attention on NVIDIA Blackwell
PUBLISHED
7/10/2026
Table of Contents
1. The algorithm and the kernel design space
2. The KV-outer kernel
3. Optimizations
4. Differences from open-source MSA
5. Results
Acknowledgements
Appendix: the I/O cost model
Table of Contents
Explore us in AI tools
ChatGPT
Claude
Grok
Perplexity
CoPilot
Gemini
Table of Contents
1. The algorithm and the kernel design space
2. The KV-outer kernel
3. Optimizations
4. Differences from open-source MSA
5. Results
Acknowledgements
Appendix: the I/O cost model
Table of Contents
Summary:
Attention drives most compute and memory costs in long-context inference. Sparse attention, as used in
MiniMax M3
, reduces this by having each query attend only to the top 16 most relevant 128-token KV blocks. Implementing this efficiently is difficult, however; the sparse selection is data-dependent and varies by request, leading to irregular memory access patterns that often negate the theoretical speedup.
The Fireworks AI Performance team built a Blackwell (SM100) kernel for M3 sparse attention that closes most of that gap. It uses a KV-stationary execution path — a research idea brought up by the MiniMax team in the
Minimax Sparse Attention paper
— that loads each selected KV block once in the outer loop and attends every query that chose it in the inner loop. With this schedule fixed, performance optimization focuses on two critical areas: reducing gathered-load/scattered-store memory traffic and improving load balancing across SMs. Our implementation addresses both challenges, achieving the following results on a single B200 (fp8):
•
Attention Kernel Efficiency:
Reaches throughput of ~980 TFLOP/s at ~4.1 TB/s HBM bandwidth. This represents a
1.9–2.4×
speedup over a query-stationary baseline (FlashInfer) and a
~1.6×
improvement over MiniMax’s open-source MSA kernel.
•
Full Module Performance:
Including index mapping and combination stages, the module delivers
1.18–1.43×
gains over the baseline and
1.32–1.41×
gains over open-source MSA.
Figure [above-dark]: Fireworks KV-outer E2E sparse attention module achieves a 1.18–1.43× speedup over a query-stationary baseline (FlashInfer) and a 1.32–1.41× speedup over MiniMax's open-source MSA kernels. Figure [above-light]: Fireworks KV-outer main attention kernel reaches throughput of ~980 TFLOP/s at ~4.1 TB/s HBM bandwidth, achieving 1.6× speedup over Minimax's open-source MSA kernel (compared to the baseline FlashAttention-4).
1. The algorithm and the kernel design space
M3 sparse attention
M3 attention is blockwise sparse on top of grouped-query attention (GQA): the KV sequence is partitioned into fixed 128-token blocks, a lightweight index branch scores those blocks and selects the topK (= 16) highest-scoring blocks for each GQA group, and a main branch then computes exact attention over only the selected blocks. Shapes: Hq = 64, Hkv = 4 (GQA factor Hq/Hkv = 16), D = 128, block = 128. The algorithm and the KV-stationary execution idea are from MiniMax (
paper
,
MSA kernels
).
Q-outer vs KV-outer
A traditional dense FlashAttention-style kernel (e.g. FlashAttention4, aka FA4) loops Q-outer / K-inner: one threadblock owns a 128-row Q tile and streams all KV through it at a 128×128 MMA. (128 is the common block/tile size we use as the running example; other block sizes are valid.) As a result each KV load is shared across the tile’s 128 Q tokens, and the MMA runs at a large, efficient 128×128 tile.
Sparsity, on the other hand, admits two kernel structures:
•
Q-outer (query-stationary).
Keep Q-outer/K-inner; each query reads only its selected KV blocks. The M dimension collapses to the GQA factor (16), so the MMA tile is
16×128
— decode-shaped, and naturally served by, e.g., a FlashInfer decode attention kernel. Tensor cores are underfed, and a KV block selected by M queries is read M times repeatedly.
•
KV-outer (KV-stationary).
Invert the map: for each (kv_head, kv_block), gather the queries that selected it, load the KV block once, and run a full
128×128
tile, emitting one partial (O_partial, m, l) per (query, kv_block). So each Q token writes up to topK (= 16) partial-O blocks, which a following combine kernel LSE-merges into its final output. Full tiles; each KV block read once.
Figure: kernel scheduling comparison between FA4 (dense), Q-outer (sparse) and KV-outer (sparse).  Left: FA4 (dense); compute: efficient, 128x128 MMA; load: efficient, each KV block is shared by 128 Q tokens; store: efficient, O is stored once.  Middle: Q-outer (sparse); compute: inefficient, 16 (MQA factor) x128 MMA; load: inefficient, each KV block is loaded by multiple Q tokens separately; store: efficient, O is stored once.  Right: KV-outer (sparse); compute: efficient, 128x128 MMA; load: okay, each Q block is shared by 128 KV tokens via gathered read; store: inefficient, partial-O is stored 16 (topk) times.
I/O analysis: sparse Q-outer vs sparse KV-outer crossover
While Section 4.2 of the Minimax Sparse Attention paper analyzes the FLOPs/IO tradeoffs between Q-outer and KV-outer approaches, it overlooks the fact that most data movement occurs within the L2 cache rather than global memory, necessitating a distinct analytical approach.
The two structures are bound by different memories.
Q-outer is L2-bandwidth bound
(re-reads hit L2);
KV-outer is HBM-bandwidth bound
(each block read once, but ≤topK partials are written per query and re-read in combine). A simple bandwidth roofline (B200 at ~24 TB/s L2 and ~7.4 TB/s HBM, from measured peak numbers; data fp8, partial-O bf16) gives the crossover:
KV-outer is faster than Q-outer when nsb / N < 2.85
— i.e. under reuse, the prefill regime.
where nsb is the number of distinct selected KV blocks and N the number of query tokens. The bound is conservative: it assumes Q-outer hits L2, valid only while selected KV fits in L2 (nsb < ~3,200); past that Q-outer spills to HBM and the gap widens. The full derivation — per-design HBM vs L2 traffic, the byte accounting, and the binding-resource argument — is in the
appendix
.
In production nsb / N is usually below 2.85 — especially at long context, where many queries select overlapping blocks and reuse is high — so KV-outer is more efficient than the Q-outer algorithm in this case.
2. The KV-outer kernel
The kernel has four stages:
Index build
— invert the per-query selection into a (kv_head, kv_block) → queries CSR map.
Scheduler
— partition (kv_head, kv_block, query) work into balanced splits.
Sparse attention main kernel
— KV-stationary, persistent; emits partials (O_partial, m, l).
Combine
— LSE-merge each query’s partials into the final output.
Sparse attention kernel pipeline design
The sparse attention main kernel is warp-specialized:
load
(K/V via TMA, Q via cp.async gather),
MMA
(QK + PV on tcgen05), two
softmax
warpgroups, and an
output
path (evacuate the PV accumulator, store partials). Because each CTA owns a single KV block, there is one online-softmax step and no cross-block correction/rescale — the stage a dense FA4 kernel needs to fold each K tile into a running O.
Figure: kernel pipeline design comparison between FA4 and KV-outer. Top: Q-outer, store O only happens at the end; Bottom: KV-outer, store O happens for every tile, load and store have higher latency
The KV-outer algorithm has more I/O cost. FA4 stores O once at the end; KV-outer writes partial-O on every tile, which is more expensive than FA4’s in-register O rescale. The load side is heavier too: queries arrive as a gather rather than a contiguous read. Load and store are the optimization targets.
3. Optimizations
Attention store optimization: from attn scattered writes to combine gathered read
The attention kernel writes partial-O in contiguous blocks instead of scattered writes; the combine kernel does gathered loads. A KV-outer CTA serves a scattered set of queries, so the natural store would scatter each partial back to its query’s slot. But scattered writes inside the attention kernel are instruction-latency-sensitive and easily stall the whole pipeline. The combine kernel, by contrast, is memory-bandwidth bound and far less sensitive to load-instruction latency, so a gather costs little there. We therefore let the attention kernel write partial-O in contiguous, tile-ordered blocks (a single bulk-TMA pass, pure address arithmetic), and build an index from (q_idx, kv_head, top-i) → (kv_block_idx, offset_in_kv_block) that the combine kernel gathers through.
Attention load optimization: 3-warp gathered reads
Queries are gathered by 3 warps via cp.async, head-packed, with the index read overlapped. The gather lands directly in the swizzled MMA-A layout. Packing each query’s GQA-head group into one “box” yields one index read per query-group instead of per row, and the Q index gather is overlapped with the previous tile’s Q load (a one-tile software pipeline).
Attention pipeline optimization: delete the softmax→store sync
The softmax warpgroup writes out the (m, l) stats (row max and row sum) directly. Since O is never rescaled in the KV outer attention kernel, the store warpgroup no longer depends on the softmax warpgroup — it just evacuates the raw PV accumulator — which shortens the pipeline.
Load-balanced split-Q scheduling + persistent kernel
A heavy KV block is split across CTAs by a deterministic, atomic-free scheduler. A single on-device kernel flattens all (kv_head, kv_block, query) work into one sequence and assigns each CTA a contiguous slice. The attention kernel is persistent (grid ≈ #SMs), overlapping each block’s store with the next block’s load.
D2H elimination: fixed per-request shapes
The selected-block count and the KV-block→Q-token mapping are dynamic shapes that vary per layer. Reading them back to size kernel grids would force a device-to-host (D2H) copy on every layer. We instead fix all tensor shapes per request — aligned to q_len, max_kv_blocks, num_splits — and skip the padded compute; with the persistent kernel, the scheduler always outputs a fixed N × num_sms work items. The result: no D2H sync.
C++ AOT dispatch backend
The kernels are AOT-exported per config and driven from a C++ op. KV-outer is several small kernels, and launching each from Python/CuTe-DSL adds host-side overhead between launches that makes up most of the end-to-end (wall-clock) latency even though the GPU work is small. Dispatching the precompiled kernels from a C++ op removes that launch overhead, and is useful in cases where CUDA graphs are hard to apply.
4. Differences from open-source MSA
Our kernel follows MiniMax’s KV-outer design, but the kernel itself was written independently, before MSA was public — so the two are separate implementations of the same idea rather than a before/after of one codebase. The comparison here is a rough study of the two implementations.
The major difference is in the attention kernel’s load and store paths. On the store side, open-source MSA scatters each partial to its (query, rank) slot inside the attention epilogue and normalizes it there, while we store partial outputs tile-ordered and raw and defer the scatter and normalization to the combine kernel. The two also organize warps differently: MSA uses a single shared 4-warp Q-load/epilogue warpgroup for both the query load and the output store, whereas we use separate warps — a 3-warp cp.async gather for the load, a 4-warp group for the tmem→rmem→smem evacuation of the PV accumulator, and a single TMA store per Q block for the final write.
5. Results
Attention-kernel throughput and HBM bandwidth.
We compare three backends on a single B200 (fp8): Q-outer (FlashInfer), MSA (MiniMax’s open-source kernel), and our KV-outer kernel. Across every shape and reuse level, KV-outer leads in attention-kernel throughput — peaking near
980 TFLOP/s
, roughly
1.9–2.4× the Q-outer (FlashInfer) baseline and ~1.6× open-source MSA
. KV-outer (and MSA, also KV-stationary) are HBM-bound, while the query-stationary baseline is L2-bound and barely touches HBM.
Figure: attention-kernel TFLOPs and mem-bw comparison between 3 backends. Top: attention kernel tflops. Bottom: deduped HBM bandwidth (each tensor counted once, without duplicate KV reads for Q-outer or duplicate Q reads for KV-outer).
Figure: attention-kernel TFLOPs and mem-bw for long-context. With the number of selected KV blocks fixed, KV-outer achieves similar perf across different KV lengths.
E2E attention module perf comparison.
The module-latency breakdown shows where the time goes inside an attention module. The attention kernel is the largest share, and KV-outer shrinks it the most. In full-module device time KV-outer is
1.18–1.43× over the FlashInfer Q-outer baseline
and
1.32–1.41× over open-source MSA
— more modest than the attention-kernel gain alone, because the index mapping, scheduling, and combine stages take non-trivial time relative to the main attention kernel.
Figure: E2E attention module latency breakdown and comparison across 3 backends
Acknowledgements
Thanks to the MiniMax team for the MiniMax Sparse Attention algorithm and for helpful discussion. The kernel is built on the FlashAttention4 CuTe-DSL SM100 kernel, and was developed with the help of Claude Code and Cursor.
Appendix: the I/O cost model
This expands the crossover from §1. The model is a pure bandwidth roofline: count the bytes each design moves, divide by the bandwidth of the memory it is bound by, and compare.
1
2
3
4
5
6
7
8
9
10
11
definitions
N
=
query tokens
nsb
=
distinct selected KV blocks
topK
=
16
(
selected blocks per query
)
Hq
=
16
,
D
=
128
,
block
=
128
;
data fp8
(
1
B
)
,
partial
-
O bf16
(
2
B
)
BW_L2
=
24
TB
/
s
,
BW_HBM
=
7.4
TB
/
s
(
measured peak
,
B200
)
;
usable L2 ≈
100
MB
per
-
tensor
bytes
Q row
=
O row
=
Hq·D
=
2
,
048
B
/
query
KV block
(
K
+
V
)
=
2
·block·D
=
32
,
768
B
/
block
partial
-
O
=
topK·Hq·D·
2
=
65
,
536
B
/
query
Each design has two latency estimates:
deduped HBM traffic
(every tensor moved once, ÷ HBM BW) and
non-deduped L2 traffic
(counting re-reads, ÷ L2 BW). The actual latency is the larger of the two, and tells us which resource binds.
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
Q
-
outer
HBM
(
dedup
)
:
N·
(
Q
+
O
)
+
nsb·
(
K
+
V
)
=
4
,
096
·N
+
32
,
768
·nsb
latency
=
(
4
,
096
·N
+
32
,
768
·nsb
)
/
7.4
=
553
·N
+
4
,
428
·nsb
L2
(
re
-
read
)
:
N·
(
Q
+
O
)
+
N·topK·
(
K
+
V
)
=
528
,
384
·N
latency
=
528
,
384
·N
/
24
=
22
,
016
·N
while
KV fits L2
(
nsb
<
~
3
,
200
)
,
L2 latency
>
HBM latency  ⇒  L2
-
bw bound
KV
-
outer
HBM
(
dedup
)
:
N·
(
Q
+
O
+
partial
-
O
)
+
nsb·
(
K
+
V
)
=
69
,
632
·N
+
32
,
768
·nsb
latency
=
(
69
,
632
·N
+
32
,
768
·nsb
)
/
7.4
=
9
,
410
·N
+
4
,
428
·nsb
L2
(
re
-
read
)
:
N·topK·Q
+
2
·N·partial
-
O
+
N·O
+
nsb·
(
K
+
V
)
=
165
,
888
·N
+
32
,
768
·nsb
latency
=
(
165
,
888
·N
+
32
,
768
·nsb
)
/
24
=
6
,
912
·N
+
1
,
365
·nsb
HBM latency
>
L2 latency
(
always
)
⇒  HBM
-
bw bound
roofline comparison
(
each at its binding resource
)
Q
-
outer
(
L2
)
=
22
,
016
·N
KV
-
outer
(
HBM
)
=
9
,
410
·N
+
4
,
428
·nsb
KV
-
outer faster
:
22
,
016
·N
>
9
,
410
·N
+
4
,
428
·nsb  ⇒  nsb
/
N
<
2.85
Caveats.
(1) The bound is conservative — it gives Q-outer a perfect L2 hit; beyond L2 capacity Q-outer is HBM-bound and slower, so KV-outer wins earlier than 2.85. (2) Bandwidth-only — tensor-core and combine compute are not modeled, and the crossover scales with the measured L2:HBM ratio. (3) KV-outer is only moderately HBM-bound (its L2 latency is ~0.7× its HBM latency), so a stricter max(L2, HBM) model would nudge the crossover slightly below 2.85.
Explore us in AI tools
ChatGPT
Claude
Grok
Perplexity
CoPilot
Gemini
Platform
AI Native
Enterprise
Customers
Use Cases
Code Assistance
Conversational AI
Agentic Systems
Search
Multimodal
Enterprise RAG
Developers
Model Library
Docs
CLI
API
Changelog
Pricing
Serverless
On-Demand
Fine Tuning
Enterprise
Partners
Cloud and Infrastructure
Consulting and Services
Technology
Fireworks for Startups
Resources
Blog
Demos
Cookbooks
Company
Leadership
Investors
Careers
Trust Center
© 2026 Fireworks AI, Inc. All rights reserved.
