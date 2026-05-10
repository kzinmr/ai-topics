---
title: "Serving DeepSeek-V4: why million-token context is an inference systems problem"
url: "https://www.together.ai/blog/serving-deepseek-v4-why-million-token-context-is-an-inference-systems-problem"
fetched_at: 2026-05-10T07:00:44.187598+00:00
source: "Together AI Blog"
tags: [blog, raw]
---

# Serving DeepSeek-V4: why million-token context is an inference systems problem

Source: https://www.together.ai/blog/serving-deepseek-v4-why-million-token-context-is-an-inference-systems-problem

Benchmark tables miss the main point of DeepSeek-V4: the important change is architectural. V4 turns million-token context into a serving-systems problem.
The model supports a 1M-token context window through a hybrid attention design that compresses context before key-value (KV) storage, mixes compressed and local attention paths, and changes how prefix reuse works. Those choices reduce KV pressure, but the savings only matter if the inference engine can manage the resulting cache layouts, recover local state, batch requests effectively, and choose endpoint profiles that match the workload.
This post focuses on the serving implications of V4's Compressed Sparse Attention (CSA) / Heavily Compressed Attention (HCA) / Sliding Window Attention (SWA) attention design, based on Together's early bring-up work on NVIDIA HGX B200. V4 also includes other architecture and training changes, including Manifold-Constrained Hyper-Connections (mHC) residual connections and Muon optimizer choices, but those are outside the main scope here.
V4 compresses the token axis of KV cache
Autoregressive inference stores prior context in KV cache. During decode, each new token generated reads from and attends to that stored state. The cache grows with sequence length:
KV cache  ∝  layers × tokens × kv_heads × head_dim × bytes
At long context, KV cache hits serving twice. It caps concurrency because each active request occupies memory, and it lowers throughput because decode has to read stored context every step. V4 matters because it attacks both sides of that problem: fewer cache entries to store and fewer cache entries to move through attention.
On NVIDIA Blackwell, that cache pressure maps directly to serving economics. Long-context inference depends on keeping enough KV resident for concurrency while preserving memory bandwidth for decode. V4’s token-axis compression makes that tradeoff more favorable: the engine has more room to batch requests, reuse prefixes, and keep long-context workloads inside an efficient serving regime.
Recent model architectures have reduced different terms in the  product above. Group Query Attention (GQA) reduces KV heads. Multi-Head Latent Attention (MLA) compresses KV into a latent representation. FP8, MXFP4, and NVFP4 reduce bytes per element. DeepSeek-V3.2 sparse attention reduced how much KV had to be read during decode, while the full cache still had to stay resident.
DeepSeek-V4 targets the token axis. It compresses context before KV storage.
That is the important shift.
Under a vanilla BF16 multi-head attention calculation, a 70B-class model can require megabytes of KV cache per token. The exact coefficient depends on layer count, KV heads, head dimension, and precision. At 1M tokens, the cache becomes impractical for a single request. V4's token-axis compression, combined with MLA-style head compression and low-precision KV, reduces the per-request cache footprint enough to make very long context materially more practical.
In early bring-up, V4’s serving capacity was governed less by the compressed CSA / HCA cache and more by how the engine handled SWA state. A full-SWA implementation actually had a higher per-token KV footprint than our V3 path — roughly 3.8 KB per token versus 3.4 KB — because the engine was storing the full sliding-window state.
The practical gain came from cache policy. By keeping only the SWA states most likely to be reused, we increased total KV-cache capacity on a single NVIDIA HGX B200 node from roughly 1.2M tokens to 3.7M tokens with minimal changes. That is the main serving lesson: V4’s architecture creates the opportunity for long-context efficiency, but the realized capacity depends on how the inference engine stores, recomputes, and evicts the different cache types.
The practical win extends beyond full 1M-token requests. It makes 200K–500K-token workloads more concurrent and less fragile, because the engine has more KV budget to work with before memory pressure forces eviction or limits batching. Earlier million-token-context models still left major serving challenges around memory, concurrency, and cost. V4 moves that range closer to an actual workload when the serving policy matches the cache layout.
V4 requires multiple KV-cache layouts
Many existing serving paths assume something close to a single KV cache layout: one cache object per layer per token, the same shape across the stack. V4 requires three different cache types, mixed across layers.
Compressed Sparse Attention (CSA) compresses context with stride 4, but each compressed entry is built from a slightly wider receptive field. In V4's configuration, each entry summarizes an 8-token neighborhood, so adjacent compressed entries overlap at the boundaries. When a query selects 128 compressed entries, it is selecting summaries of local neighborhoods rather than isolated token positions. That gives CSA a finer-grained path into selected regions of the million-token prefix while still reducing the stored cache footprint.
Heavily Compressed Attention (HCA) uses the same compression idea but with stride 128. At a 1M-token context length, that reduces the cache from 1M token positions to roughly 8K compressed entries. That is the key difference from CSA: the compressed cache is small enough that the model can attend over it densely instead of selecting a top-k subset. HCA gives the model a coarse global read over the whole context, while CSA gives it a finer sparse read over selected regions.
Sliding Window Attention (SWA) preserves the local path. The window is short, around 128 tokens, and keeps recent context exact.
Across the stack, the engine has to manage CSA compressed state, HCA compressed state, SWA local state, and short uncompressed tail states used by the CSA and HCA compressors. These objects have different sizes, lifetimes, and read patterns.
New attention kernels are only part of the work. The harder serving problem is memory management: batching requests, evicting cache pages, reusing prefixes, and keeping decode throughput stable while different parts of the model depend on different kinds of stored state.
Prefix caching becomes a storage policy
Prefix caching usually starts with a simple rule: shared prefix, shared KV. With V4, the question becomes: which cache?
A shared prefix contains CSA state, HCA state, SWA state, and the uncompressed tail states used by the CSA and HCA compressors. CSA and HCA are compact enough to store efficiently. SWA is exact local state, which makes it more expensive to store for long prefixes, especially once the cache tier moves beyond GPU memory.
The DeepSeek paper describes three SWA strategies.
The first stores the full SWA cache. Reuse is simple because the engine can restore the complete prefix state directly, but storage and write bandwidth grow quickly.
The second stores periodic SWA checkpoints. The engine saves state every K tokens and recomputes the gap on a cache hit.
The third recomputes SWA on hit. The engine stores compressed CSA / HCA state and rebuilds the SWA path when a prefix is reused. The cost is bounded by window size times layer count. With a 128-token window and 61 layers, that is roughly 8K tokens of recompute. Against a 1M-token prefix, that trade can make sense.
In our current V4 bring-up, we use the first strategy: storing the full SWA cache. This keeps prefix reuse straightforward and avoids adding recompute complexity while the rest of the serving path is still maturing. The tradeoff is higher cache footprint, which makes cache policy and eviction behavior more important as context length and concurrency increase.
V4 turns prefix caching into a policy decision across cache objects: store CSA and HCA, decide how to handle SWA, and evict each type according to its own cost.
V4 performance is regime-dependent
V4's gains show up first where KV cache dominates.
Long-context, decode-heavy workloads spend much of their time reading cache. V4's compressed cache layout reduces that pressure.
Short-context, prefill-heavy workloads hit a different path. CSA top-k selection, HCA compressed reads, and SWA introduce operations outside mature dense-attention kernel paths. Kernel maturity matters. Precision format matters too: V4 uses MXFP4 for MoE weights, which has different performance characteristics than NVFP4 on NVIDIA Blackwell GPUs. That makes short-context prefill especially sensitive to kernel maturity, while long-context decode benefits more directly from KV-cache reduction.
That creates a regime split. Long-context workloads benefit from V4's cache savings early. Short-context workloads depend more on kernel bring-up and prefill optimization. This is typical for a new architecture: the first implementation establishes correctness; the next iterations close the gap to hardware efficiency.
Together is continuing V4 kernel work across the prefill and decode paths.
Developers should benchmark V4 in their actual regime. A 1M-context coding agent and a short-context chat assistant exercise different parts of the serving stack.
The same weights need different serving profiles
V4 widens the gap between workload shapes.
Long-context agents benefit most directly from the architecture. They read large amounts of cache during decode, so V4's compressed KV layout, larger tensor-parallel configurations, batching, and prefix reuse all matter. This is the regime where the model's long-context design should show up first.
Coding agents over shared repositories are related, but the serving problem is more prefix-heavy. The same project files, repository state, or task scaffolds may repeat across requests, so cache tiering and SWA recompute policy become first-order choices. The bottleneck includes both long context and repeated-context reuse.
Short chat sits at the other end of the spectrum. These workloads do not benefit much from million-token cache compression, and they expose prefill latency, small-batch overhead, and kernel maturity instead. Serving them well may require smaller tensor-parallel groups, minimal batching delay, and kernels tuned for the short-context path.
RL rollouts care about a different unit of economics: cost per long trajectory. They may share serving machinery with long-context agents, but the optimization target is experiment throughput, how many long-horizon rollouts can be generated per training budget, rather than single-request latency alone.
The same weights can serve all of these workloads. Each performs best under a different endpoint configuration. Together is evaluating endpoint profiles with different batching, parallelism, and cache policies.
What to benchmark before moving to V4
Million-token serving matters most for systems that accumulate state over long tasks: coding agents, research agents, and other longer horizon tasks. For these workloads, the cost model often shifts from price per token toward cost per completed trajectory.
Before moving traffic to V4, benchmark four things: context-length regime, prefix reuse, cache policy, and endpoint profile.
For long-context agents, measure cache hit rate, decode throughput, and cost per completed task. Time-to-first-token captures only part of the picture.
For short chat, compare latency at your real context lengths and batch sizes. V4's long-context gains may not appear in short-chat latency first.
For shared-prefix workloads, test SWA full-store against recompute-on-hit. Prefix length, cache-tier latency, and reuse frequency determine the answer.
For RL rollouts, calculate cost by trajectory length and number of rollouts per experiment, not by token price alone.
For mixed traffic, expect tradeoffs. One endpoint can serve mixed workloads, but a profile-specific endpoint will usually perform better once the workload shape is clear.
Quality still has to be measured. Longer context creates more room for useful state, retrieval noise, compression artifacts, and latency. It also changes compaction strategy: builders get more control over when to preserve raw state, summarize, or reset.
Conclusion
DeepSeek-V4's efficiency is a system property. The architecture reduces KV pressure by compressing along the token axis, but the serving engine has to manage the cache types, prefix policies, kernel paths, and endpoint profiles that follow from that choice.
This is also where full-stack co-design matters. The model changes the cache layout. The inference engine changes memory management and prefix policy. The kernels adapt to new attention and precision paths. The NVIDIA Blackwell platform determines how much of that work turns into realized throughput, concurrency, and cost-per-token gains.
Running V4 is the starting point. Turning its architectural savings into lower latency, higher concurrency, and cheaper long-context workloads requires cache-policy work, kernel work, and workload-specific serving profiles. The next step is measurement: per-token KV footprint, context-length throughput curves, prefix-cache policy impact, and endpoint profiles for different traffic shapes. We'll publish those numbers as the V4 kernels and cache policies mature.
FAQ
What is DeepSeek-V4's context window?
DeepSeek-V4 supports a 1M-token context window. It achieves this through a hybrid attention design that compresses context before key-value (KV) storage, mixes compressed and local attention paths, and changes how prefix reuse works. The architectural change is what makes million-token context viable as a serving workload.
What is Compressed Sparse Attention (CSA) in DeepSeek-V4?
CSA compresses context with stride 4, where each compressed entry summarizes an 8-token neighborhood, so adjacent entries overlap at the boundaries. Queries select roughly 128 of these compressed entries, giving the model a fine-grained sparse path into selected regions of the prefix while reducing the stored cache footprint.
What is Heavily Compressed Attention (HCA)?
HCA uses the same compression mechanism as CSA but with stride 128. At a 1M-token context, this reduces the cache from 1M positions to about 8K compressed entries, which is small enough that the model attends densely over all of it. HCA provides a coarse global read, while CSA provides a fine sparse read over selected regions.
How does DeepSeek-V4 reduce KV cache size compared to earlier models?
DeepSeek-V4 compresses along the token axis of KV cache. Earlier techniques reduced different terms in the cache product: Group Query Attention reduces KV heads, Multi-Head Latent Attention compresses the head dimension, and FP8/MXFP4/NVFP4 reduce bytes per element. DeepSeek-V3.2 reduced how much cache had to be read at decode while keeping the full cache resident. V4 reduces the number of stored token entries themselves.
Why does serving DeepSeek-V4 require multiple KV cache layouts?
The model uses three attention paths (CSA, HCA, and Sliding Window Attention) mixed across layers. Each produces cache objects with different sizes, lifetimes, and read patterns. The inference engine has to manage all three concurrently per request, which makes memory management, eviction, and prefix reuse harder than under a single-cache design.
How does prefix caching work with DeepSeek-V4?
Prefix caching becomes a per-cache-type policy decision. CSA and HCA state are compact enough to store. SWA state is exact local state and grows expensive at long prefixes. The DeepSeek paper describes three options: store full SWA, store periodic checkpoints, or recompute SWA on cache hit. Recompute-on-hit is bounded by window size times layer count, roughly 8K tokens of recompute against a 1M-token prefix.
What workloads benefit most from DeepSeek-V4?
Long-context, decode-heavy workloads benefit first, including coding agents, research agents, and RL rollouts that accumulate state over long tasks. For these, the cost model shifts from price-per-token toward cost-per-completed-trajectory. Short-context chat workloads see smaller gains because they expose prefill latency and kernel maturity more than KV cache pressure.
Should I move short-chat traffic to DeepSeek-V4?
Benchmark first. V4's gains show up where KV cache dominates. Short-context, prefill-heavy workloads exercise newer kernel paths (CSA top-k selection, HCA dense reads, MXFP4 MoE weights) that are still maturing. Compare latency at your real context lengths and batch sizes before switching. Long-context agents and short chats may need different endpoint profiles even on the same weights.
Why did Together pick the NVIDIA HGX B200 to serve DeepSeek V4?
NVIDIA HGX B200 lines up with the parts of DeepSeek V4 that dominate serving cost: KV-cache pressure during long-context decode and MoE weight bandwidth during prefill. Blackwell’s
inference performance
lets a single HGX B200 node hold V4's compressed CSA / HCA / SWA cache layouts resident across many concurrent long-context requests, and its native MXFP4 support matches the format DeepSeek ships for V4's MoE weights — so we run the model's quantization end-to-end without a re-cast step. Together's HGX B200 deployment inherits the same MXFP4 path and KV-compression headroom, which is why we picked it as the launch platform for V4.
