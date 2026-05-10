---
title: "Training-Inference Parity in MoE Models: Where Numerics Drift"
source: "Fireworks AI Blog"
url: "https://fireworks.ai/blog/when-faster-not-identical-moe-numerics"
scraped: "2026-05-10T01:20:33.117077+00:00"
lastmod: "2026-04-10T18:08:52.000Z"
type: "sitemap"
---

# Training-Inference Parity in MoE Models: Where Numerics Drift

**Source**: [https://fireworks.ai/blog/when-faster-not-identical-moe-numerics](https://fireworks.ai/blog/when-faster-not-identical-moe-numerics)

DeepSeek V4 Pro is Live → Try it now.
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
Training-Inference Parity in MoE Models: Where Numerics Drift
Training-Inference Parity in MoE Models: Where Numerics Drift
Kernel fusions that are mathematically equivalent can still drift numerically. This draft walks through the parity bugs we hit across Kimi K2.5 serving and Qwen3.5-MoE training, plus the fixes that kept k3 near the noise floor.
PUBLISHED
3/10/2026
TRAINING REFERENCE
FUSED INFERENCE
SAME WEIGHTS + SAME INPUT, BUT A DIFFERENT REDUCTION ORDER
TP partial
outputs
NCCL ring
reduce-scatter
Standalone
RMSNorm
Reference logprobs
PER-CHUNK OWNERS
GPU0 owns chunk 0
GPU1 owns chunk 1
NCCL ORDER ROTATES
chunk 0: r0 + r3 + r2 + r1
chunk 1: r1 + r0 + r3 + r2
LOCAL BUFFERS
buffer 0
buffer 1
buffer 2
LAMPORT LOCAL ORDER
chunk 0: r0 + r1 + r2 + r3
chunk 1: r0 + r1 + r2 + r3
Scatter-write
HBM buffers
Local fixed-order
sum on every GPU
Fused RMSNorm
+ residual
Served logprobs
K3 DRIFT COMPOUNDS
In an LLM, KL compares the full next-token
probability vector from training and inference.
The top token can stay the same,
but probability moving across lower-ranked
tokens still makes KL grow.
KL MEASURES DISTRIBUTION MISMATCH, NOT JUST TOP-1 AGREEMENT
EXAMPLE TOKEN PROBABILITIES
same prompt, same decode position
training
inference
larger shift means larger KL
token
probability
0.0
0.1
0.2
0.3
0.4
top token
runner-up
alt token A
alt token B
training and inference can still agree on the top token,
while lower-ranked probabilities drift apart
On this page
Why This Matters
The Fundamental Issue: FP Addition Is Not Associative
Pitfall 1: All-Reduce Topology Differences
What it is
Why it's easy to miss
Pitfall 2: Fusing Communication with Computation
What it is
Why it's easy to miss
Pitfall 3: Multi-Operation Fusions in MoE
What it is
Measuring the Impact
Case Study: Qwen3.5-MoE Image-Token Drift
How we isolated it
The precise numerical mismatch
Lessons Learned
References
On this page
Why This Matters
The Fundamental Issue: FP Addition Is Not Associative
Pitfall 1: All-Reduce Topology Differences
What it is
Why it's easy to miss
Pitfall 2: Fusing Communication with Computation
What it is
Why it's easy to miss
Pitfall 3: Multi-Operation Fusions in MoE
What it is
Measuring the Impact
Case Study: Qwen3.5-MoE Image-Token Drift
How we isolated it
The precise numerical mismatch
Lessons Learned
References
When Faster ≠ Identical: Numerical Pitfalls in Serving MoE Models
Kernel fusions that are mathematically equivalent can still drift numerically. Here are the parity bugs we hit across both Kimi K2.5 serving and Qwen3.5-MoE training bring-up.
Why This Matters
When you train a model and serve it for inference, you expect them to agree. The same weights, the same input, the same output distribution. This
training–inference numerical parity
matters more than it sounds:
RLHF / GRPO reward integrity.
The reference model's logprobs anchor the KL penalty. If inference produces different logprobs than training for the same weights, the policy can exploit the gap without actually improving.
Reproducibility.
Numerical drift from kernel fusions is invisible — weights are identical, architecture looks the same, yet outputs diverge.
Customer trust.
Users fine-tune on our platform and expect the served result to match what training optimized for.
For dense models, parity is relatively easy.
Mixture-of-Experts models like Kimi K2.5, Qwen3.5-MoE, and DeepSeek V3 are harder.
With routed experts, shared expert pathways, and all-reduce communication twice per layer across deep stacks, there are many places where "mathematically equivalent" optimizations produce numerically different results.
This post catalogs the pitfalls we found. Each is a class of optimization that inference engines use for performance, but that can silently break numerical alignment. We found most of these while bringing up Kimi K2.5 on our serving stack, then saw the same failure mode again while debugging Qwen3.5-MoE. We will use FlashInfer and TRT-LLM style fused kernels as concrete examples.
The Fundamental Issue: FP Addition Is Not Associative
Every pitfall below reduces to one fact:
floating-point addition is not associative.
Even in FP32:
(a + b) + c  ≠  a + (b + c)
Each addition rounds the result to the nearest representable value. Different orderings produce different intermediate values, which get different rounding errors. The errors are tiny per operation, but they compound through 61 transformer layers — and MoE routing amplifies them (a small change in hidden state can flip which experts get selected, cascading through the rest of the network).
Pitfall 1: All-Reduce Topology Differences
What it is
In tensor-parallel inference, every linear layer's output must be summed across GPUs via
all-reduce
. This happens twice per layer: after the attention output projection, and after the MLP/MoE.
Training typically uses
NCCL
, which implements all-reduce as a
reduce-scatter
followed by an
all-gather
. In the reduce-scatter phase with a ring topology, the data is divided into chunks — one per GPU. Each chunk is accumulated as partial sums flow around the ring, starting from the GPU that "owns" that chunk. For 8 GPUs, this means different parts of the hidden vector see different summation orders:
NCCL ring reduce-scatter (8 GPUs):
  chunk 0 (owned by GPU0): r0 + r7 + r6 + r5 + r4 + r3 + r2 + r1
  chunk 1 (owned by GPU1): r1 + r0 + r7 + r6 + r5 + r4 + r3 + r2
  chunk 2 (owned by GPU2): r2 + r1 + r0 + r7 + r6 + r5 + r4 + r3
  ...each chunk starts from its owner, accumulates around the ring
NCCL RING REDUCE-SCATTER
LAMPORT LOCAL SUM
CHUNK OWNERSHIP ROTATES ON THE LEFT; LOCAL ORDER STAYS FIXED ON THE RIGHT
ONE EXAMPLE CHUNK: SAME VALUES, DIFFERENT FP32 ADDITION ORDER
training / NCCL reference
chunk ownership rotates with the ring
R0
R3
R2
R1
accumulated tensor
R0
ring order for this chunk
R0 -> R3 -> R2 -> R1
same chunk, rotating owner:
NCCL follows the ring, then reduces
inference / Lamport local sum
every GPU applies one fixed local order
R0
R0
R1
R2
R3
accumulated tensor
FP32 accumulation order
R0 -> R1 -> R2 -> R3
every GPU keeps one fixed local order
ROUNDING ORDER CHANGES
Both kernels compute the same exact sum in real arithmetic.
But fp32 addition is order-sensitive, so rotating the owner changes
which partial sums round first even when the exact sum is identical.
SAME SUM, DIFFERENT FP32 ACCUMULATION ORDER
All-Reduce Topology
NCCL rotates chunk ownership around the ring, while Lamport kernels sum in a uniform local order. Exact arithmetic agrees; floating-point accumulation does not.
Inference serving engines often replace NCCL with custom all-reduce kernels for lower latency. FlashInfer's
Lamport IPC kernel
(derived from TRT-LLM) uses a different approach: each GPU writes its data to all other GPUs' buffers via CUDA IPC, then every GPU reads all contributions locally and sums them in a fixed order:
Lamport kernel (all elements, on every GPU):
  every chunk:              r0 + r1 + r2 + r3 + r4 + r5 + r6 + r7
Both accumulate in FP32. Both produce the correct sum in exact arithmetic. But the
per-chunk rotation
in NCCL means different elements of the hidden vector see different addition orders, while the Lamport kernel uses a uniform
r0..r7
order for everything. Because FP addition is non-associative, these yield different results.
Why it's easy to miss
The outputs look correct. The model generates coherent text. The divergence is sub-0.001 in KL divergence. You only notice it when you compare logprobs token-by-token against a reference — which is exactly what RLHF reward computation does.
Pitfall 2: Fusing Communication with Computation
STANDALONE RMSNORM
FUSED WARP-SHUFFLE TREE
THE REDUCTION TREE CHANGES WHICH PARTIAL SUMS ROUND TOGETHER
SAME PARTIAL SUMS: DIFFERENT PAIRINGS FEED A DIFFERENT RSQRTF INPUT
training / standalone RMSNorm
the normalization kernel keeps its own block tree
a
b
c
d
a+b
c+d
sum(x^2)
(a + b) + (c + d)
first pairings: (a+b) and (c+d)
then one final reduction
inference / fused warp shuffle
the fused block layout changes the first pairings
a
b
c
d
a+c
b+d
sum(x^2)
(a + c) + (b + d)
first pairings: (a+c) and (b+d)
then one final reduction
RSQRTF INPUT DRIFTS
RMSNorm depends on one reduced scalar: sum(x^2).
If the tree changes, the rounding path to that scalar changes too,
so rsqrtf starts from a slightly different value.
THE NORMALIZATION SCALE DEPENDS ON THE REDUCTION TREE
RMSNorm Reduction Tree
Fusing communication and normalization changes the reduction tree itself, so the RMS scalar feeding rsqrtf is no longer rounded the same way.
What it is
In the unfused path, all-reduce and RMSNorm are two separate kernel launches with an HBM round-trip in between:
full_out = all_reduce(partial_out)              # kernel 1: writes result to HBM
normed, residual = rmsnorm(full_out, residual)  # kernel 2: reads from HBM
The fused path combines them into a single kernel. The all-reduce result stays in registers and flows directly into the normalization — no HBM round-trip, no second kernel launch.
The performance win is significant (saves ~3 TB/s HBM bandwidth per operation). But the fused kernel computes RMSNorm with a different thread layout than a standalone norm kernel would use.
To see why this matters, consider how RMSNorm computes the sum of squares across the hidden dimension. The hidden state is distributed across threads, and the partial sums must be reduced to a single scalar. GPU kernels do this with a
butterfly reduction
— each thread exchanges values with a partner via
__shfl_xor_sync
, halving the number of active participants at each step:
Step 1: thread 0 ↔ thread 16, thread 1 ↔ thread 17, ...  (mask=16)
Step 2: thread 0 ↔ thread 8,  thread 1 ↔ thread 9,  ...  (mask=8)
Step 3: thread 0 ↔ thread 4,  thread 1 ↔ thread 5,  ...  (mask=4)
Step 4: thread 0 ↔ thread 2,  thread 1 ↔ thread 3,  ...  (mask=2)
Step 5: thread 0 ↔ thread 1                                (mask=1)
This is a 5-step binary tree within each 32-thread warp. After that, warp-level results are combined across warps via shared memory (and on Hopper, across blocks in a cluster via cluster shared memory). The final value is fed to
rsqrtf
to produce the normalization scale.
The key insight:
a different block size means different elements land in different threads and warps
, so the butterfly pairs up different partial sums at each step. The intermediate additions happen in a different order, producing a different
rsqrtf
input — which then scales every element of the hidden state differently. The fused kernel's block size is dictated by the all-reduce's requirements, not by what's optimal for RMSNorm alone. (See
blockReduceSumV2
in trtllm_allreduce_fusion.cuh
for the implementation.)
For DeepSeek V3 / Kimi K2.5, this fusion runs on all 61 layers for the attention path, and is even more aggressive on the MoE path (Pitfall 3).
Why it's easy to miss
Same as Pitfall 1 — the fused kernel is "doing the same math." The divergence only shows up in careful logprob comparison.
Pitfall 3: Multi-Operation Fusions in MoE
UNFUSED MOE PATH
PERSISTENT FUSED KERNEL
SMALL GATE-SCORE DRIFT CAN CHANGE WHICH EXPERT ACTUALLY RUNS
router top-k
expert 1
expert 2
MoE finalize
NCCL all-reduce
+ standalone RMSNorm
TOKEN 0
TOKEN 1
TOKEN N
expert ordered
summation
Lamport all-reduce
next-block RMSNorm
+ residual
ROUTER DECISIONS CAN FLIP
MoE layers are extra brittle because
routing is discrete near the top-k cutoff.
A tiny score drift can flip the winner,
and the downstream path diverges much faster.
NEAR A TIE, SMALL NUMERICAL DRIFT CAN CHANGE THE EXECUTED EXPERT PATH
GATE SCORES NEAR TOP-K
training
inference
expert 1
0.51
0.49
expert 2
0.49
0.51
winner: expert 1
winner: expert 2
MoE Fusion Cascade
On MoE layers the errors stack faster because routing, expert finalize, all-reduce, and the next RMSNorm can collapse into one persistent kernel.
What it is
MoE layers have more operations to fuse than dense layers. At the end of each MoE block, FlashInfer's
MoE fusion kernel
combines
three
operations into one:
MoE finalize
— weighted sum of the top-8 expert outputs per token
All-reduce
— sum partial results across GPUs (Lamport IPC)
Next block's input RMSNorm
— normalize and add residual for the next transformer block
In the unfused path, each of these is a separate kernel with its own thread layout:
expert_out = moe_finalize(expert_outputs, weights)    # kernel 1
expert_out += shared_expert(x)                        # kernel 2
full_out = nccl_all_reduce(expert_out)                # kernel 3
normed = rmsnorm(full_out + residual)                 # kernel 4
The fused kernel does all of this in one shot. Each operation uses the thread layout dictated by the overall kernel design, not the layout each operation would choose independently.
This runs on
58 MoE layers
(layers 3–60), and the divergence compounds: a small difference in layer 3's output propagates through the attention and MoE computations of all subsequent layers. MoE routing is especially sensitive — a tiny change in hidden state can change which of the 256 experts get selected, creating a cascade.
Measuring the Impact
We measured divergence on Kimi K2.5 using
25 prompts, 200 generated tokens each
, comparing logprob distributions between a reference (all fusions disabled) and various configurations. Our metric is
k3
, a variant of KL divergence that is always non-negative and stable:
Configuration
Gen k3 (mean)
Pass (< 0.001)
All fusions disabled
0.000070
Yes
All-reduce fusions disabled, MLP fusion enabled
0.000193
Yes
The baseline (k3 = 0.000070) is the noise floor. The MLP weight-concatenation fusion alone raises k3 by ~2.7x. All configurations pass the k3 < 0.001 threshold, but for RLHF/GRPO — where the inference engine is the reference policy — minimizing k3 toward the noise floor is worth it.
Case Study: Qwen3.5-MoE Image-Token Drift
We saw the same class of issue again while bringing up Qwen3.5-MoE training with DeepEP expert parallelism. Text-token k3 stayed relatively small, but image-token k3 diverged sharply in bf16. The model weights were fine; the aggregation path was not.
For this comparison, the Hugging Face reference path was the official
Qwen/Qwen3.5-397B-A17B
model, implemented in Transformers as
Qwen3_5MoeForConditionalGeneration
.
QWEN 3.5-MOE CASE STUDY
IMAGE-TOKEN DRIFT
ONLY THE MOE AGGREGATION PATH CHANGES BETWEEN THESE RUNS
HF REFERENCE
index_add_: score fp32, accumulation bf16
casts each expert contribution before the sum
FIREWORKS BMM
sum in fp32, cast once at the end
text stays close, image tokens drift
DEEPEP COMBINE
score bf16, accumulation bf16
the image-token mismatch stays large
This isolates the bug to MoE aggregation precision.
Weights, norms, and the rest of the stack stay unchanged.
Only the cast and accumulation path changes
the measured drift.
MEASURED K3
TEXT
~0.005
IMAGE
~0.296
WHERE PRECISION DROPS
where the cast happens determines how much drift accumulates
fp32
bf16
HF reference
score
fp32
cast each
expert bf16
sum
bf16
Fireworks BMM
score
fp32
sum
fp32
cast once
bf16
DeepEP combine
score
bf16
multiply
bf16
sum
bf16
SWAP IN HF MOE BLOCKS
0.000 TEXT
0.000 IMAGE
AGGREGATION PRECISION IS THE BUG
HF rounds each expert contribution before accumulation.
Fireworks BMM delays that cast.
DeepEP also lowers score precision,
and that order change alone makes image-token drift spike.
SWAPPING ONLY THE MOE BLOCK COLLAPSES BOTH K3 METRICS TO ZERO
Qwen 3.5-MoE Parity
The Qwen3.5-MoE case study makes the same problem visible in practice: text k3 stays small while image-token k3 spikes when aggregation precision changes.
How we isolated it
We replaced only the MoE block at every layer with Hugging Face's reference implementation while keeping the rest of our stack unchanged: DeltaNet, GatedAttention, the fusion encoder, embeddings, and norms all stayed on the Fireworks path.
Configuration
text k3
image k3
Full Fireworks training path (standard MoE, bmm aggregation)
0.005
0.296
Replace MoE blocks with Hugging Face reference modules
0.000
0.000
That swap collapses both metrics to zero, which tells us the divergence is entirely inside MoE aggregation.
We also ran a per-layer reduced test: feed Hugging Face hidden states into each of our layers independently, then compare outputs layer-by-layer. Every layer was effectively clean in isolation. Image-token k3 only appeared after roughly 40 layers of tiny text-token deltas compounding through dense bidirectional attention.
The precise numerical mismatch
Hugging Face's reference path multiplies each expert output by a float32 routing weight, casts each expert contribution down to bf16, and accumulates in bf16 via
index_add_
.
# HF reference path
scored = expert_output_bf16 * score_float32
final.index_add_(0, token_idx, scored.to(torch.bfloat16))
Our standard Fireworks path instead keeps all eight expert contributions in float32, performs a batched weighted sum, then casts once at the end.
# Fireworks standard path
out = torch.bmm(scores_f32, all_expert_outputs.float()).to(torch.bfloat16)
DeepEP makes the gap larger again because
combine_tokens
casts routing scores from float32 to bf16 before the multiply and still sums in bf16.
Aggregation method
Score precision
Sum precision
Expected image k3
Hugging Face reference (
index_add_
)
float32
bf16
0.000
Fireworks standard (
bmm
)
float32
float32 -> bf16
~0.3
DeepEP combine kernel
bf16
bf16
>= 0.3
This is the same lesson as the rest of the post in a more painful setting: mathematically equivalent kernels can be numerically different enough to matter once the error compounds.
Lessons Learned
"Same math" does not mean "same bits."
Every pitfall above is mathematically equivalent to the reference path. The divergence comes purely from different FP accumulation orders — in all-reduce topology, in warp-shuffle reduction trees, in cuBLAS tiling heuristics. This is true even with FP32 accumulation.
MoE models are especially fragile.
The router's top-k selection means a tiny hidden-state change can flip expert assignments, creating a cascade through subsequent layers. Dense models don't have this amplification mechanism.
Measure with the right metric.
We use k3 (a KL divergence variant) with a threshold of 0.001. Without quantitative measurement, "the model generates reasonable text" is the best you can do — and it's not enough for RLHF.
Give users granular controls.
A single "disable all optimizations" flag is too coarse. RLHF users need fidelity; inference users need throughput. Per-fusion flags let each workload choose.
Compound effects dominate.
No single pitfall causes large divergence. But 61 layers of all-reduce topology differences + 58 layers of MoE finalize fusion + cuBLAS tiling differences in every MLP — the small per-layer errors add up.
References
FlashInfer
trtllm_allreduce_fusion.cuh
— Fused all-reduce + RMSNorm kernel
FlashInfer
trtllm_moe_allreduce_fusion.cuh
— Fused MoE finalize + all-reduce + RMSNorm kernel
Qwen3.5-MoE reference implementation
— Hugging Face Transformers implementation used as the reference path for the Qwen/Qwen3.5-397B-A17B case study
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
