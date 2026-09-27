---
title: "Hitting a billion tokens per minute on one GPU by combining a query planner and an inference engine"
url: "https://modal.com/blog/quail-billion-tpm"
fetched_at: 2026-09-27T10:01:14.830037+00:00
source: "Modal Blog"
tags: [blog, raw]
---

# Hitting a billion tokens per minute on one GPU by combining a query planner and an inference engine

Source: https://modal.com/blog/quail-billion-tpm

I see it as a point on the LLM pareto optimal curve in a regime that had a large revealed latent demand (no thinking, single token, low latency acceptable intelligence) that was under-invested into because of a race to higher intelligence.
-
Karpathy-san, on Jev
While everyone and their cousin is loudly building coding agents and chatbots, there’s a quieter inference revolution going on in the backend. Simple LLM transformations of data can be incredibly powerful, provided the cost-performance is good enough — just scroll social media and catch a few of the eye-popping,
hack-inspiring
demos of
TypeSafe AI’
s
Jev
model.
Jev implements these transformations at what you might call the “JSON layer”, Web-style interfaces between clients and services.
AI-SQL
implements it at the analytic SQL layer, at the interface between business intelligence and the database:
Different inference applications produce different
inference workloads
, and AI-SQL is no exception. A query like the one above might produce millions of sequences of thousands of tokens — RIP your token budget. These queries often require much less than frontier intelligence, so small open-weights models can crush. But naïvely delivering these sequences directly to an inference engine optimized for agentic inference through interfaces for arbitrary user-controlled requests is inherently and massively inefficient.
So we built an inference engine to fix this: the
QUery-Aware Inference Layer
(Quail). On one multi-join query where planning is particularly important, Quail hits over a billion tokens processed per minute per H100 GPU (TPM/GPU), >10x faster than our vLLM baseline on the same hardware. On Modal, that comes out to under 6¢ per billion tokens.
On
our newly-released benchmark for AI-SQL queries
, Quail runs 1.84x faster than vLLM, geometrically averaged over tasks -- including two queries we designed to demonstrate areas for future improvement in AI-SQL inference.
You can take it for a spin on Modal right now:
In this blog, we’ll give a quick overview of the problem we’re solving and how Quail works today. Spoilers: the big win is that with a structured query in hand, you can order requests to better cache (and evict) KV. This requires a slight revision of
Hydragen
-style
cascade attention
. Large numbers of small requests for small models can also incur lots of
host overhead
, aka have low
GPU utilization
, which can be avoided when you know the structure of the requests ahead of time.
This was a collaboration between inference researchers at Modal and database researchers Carnegie Mellon University’s
Full Stack Data Lab
— call it a “mixture of experts”. We’re sharing what we did because we’d like to make this work more “expert-parallel”, as it were. We believe this is only the beginning for open source performance engineering at the intersection of inference and databases — two of the most important applications of computing.
In this post, we’ll focus more on considerations for inference engineers. You can read more, from a database engineer’s perspective, at
the Full Stack Data Lab blog
. You can also check out the code for Quail
here
or the docs
here
. And if you run AI-SQL queries at scale and are interested in improving performance and cutting costs,
get in touch with us
.
What are AI Functions and AI-SQL?
First, a bit more background on the workload.
This is emphatically
not
prompting AI systems to produce SQL based on natural language inputs — that’s
NL2SQL
. That looks a lot like a traditional chatbot or coding agent workload, so existing inference engines work well.
It’s actually the other way around! In AI-SQL, we use an extension of SQL to programmatically produce (and consume) prompts for AI systems. Prompts are constructed from database entries and produce tables.
Like this:
AI-SQL is primarily used inside of business intelligence (BI) platforms to help data scientists and stakeholders ask more “fuzzy” questions of their semi-structured data, like documents and free-text fields.
There’s not a standard (yet), but major managed analytical database platforms have their own flavor:
Snowflake Cortex AI-SQL
,
Databricks AI Functions
,
BigQuery AI functions
.
Unlike the rest of SQL, this problem actually needs GPUs.
Consider the following plan for a query over the
BioDEX dataset
, which selects reports of serious adverse events in response to drugs that include both a neurological and a cardiovascular component:
If these were normal filters and joins, say based on string matching and logical equality, there’d be no good reason to use a high-throughput numerical accelerator like a GPU, even though this is an analytical query, which seems “throughput-y”. This may be obvious to some, but let’s step through the logic anyway.
Each byte loaded from durable storage to memory (or from memory to registers) would need at most a handful of arithmetic/logic operations to implement comparisons. GPUs are designed for workloads with high
arithmetic intensity
— many operations per byte loaded. And the latest GPUs have most of their
arithmetic bandwidth
in specialized hardware for large matrix multiplications, aka
Tensor Cores
. Normal filtering/joining requires no large matrix multiplications.
But this query plan uses
AI_FILTER
and
AI_JOIN
, which instead pass the inputs through a large language model. An LLM is a sequence of numerical operations, the bottleneck for which is large matrix multiplications. Each byte loaded from durable storage will be subject to on the order of billions of operations before a byte is written to storage.
Why is this interesting to inference engineers?
Most inference engineering these days is focused on one workload shape in particular: iterative construction of long input sequences by users and tool calls external to the inference service. This is the shape of workloads from chatbots and agents — and of “rollout” inference during the reinforcement learning runs that fine-tune models to be chatbots or agents.
Don’t get us wrong, this is very important work! We’ve written about our approach to it
here
. But for the hardcore inference engineer, it’s honestly starting to feel a little… played out.
There’s also some work on ultra low-latency inference where speed matters as much as intelligence. We’ve written about our techniques for this
here
. In general, these workloads use structured outputs/tool-calling. They end up as something like the “OLTP” of inference, slotting into other computer applications more easily than open-ended agents. The recent popularity of Jev demonstrates the importance of these workloads — and that we are still so early!
AI-SQL workloads haven’t gotten so much attention — yet — but we think they are interesting for inference engineers for a number of fundamental reasons, quite outside their importance to applications. Most intriguingly, they are an incredible fit for transformers (because they enable “perfect” KV cache use) and for transformers-on-GPUs (because they don’t require decode).
Manage a KV cache without all the regrets.
In typical inference, requests are client-controlled and arbitrary. This causes
no end of pain
. But in AI-SQL inference, clients only control SQL queries, which create many requests, and the combined query planner/inference engine has substantial control over the processing of those requests.
This makes it particularly easy to operate a cache that amortizes more work. For instance, we know exactly when any cache entry is no longer needed, so we can fearlessly evict it. We also know quite a bit about what the cache demand will look like, since we get an entire query plan’s worth of requests up front.
And we badly need caching for Transformers, because their forward passes are naïvely quadratic in the sequence length. We can exchange that for linear time and linear storage with KV caching.
KV caches can be tricky to operate for agent workloads, because the time between accesses is completely unknown. But for an AI-SQL query, we control the inference engine requests and so can anticipate future accesses and apply optimizations like prefetching. And furthermore, because we are oriented to token throughput, we care less about latency to retrieve KV entries. This makes, for instance, operating a multi-tier KV cache much more feasible.
Look, mom, no decode!
Sequence model inference is split into two phases: “prefill”, when most of the KV cache is generated, and “decode” phase when most of the output tokens are generated.
Decode is kind of a pain. GPUs aren’t particularly good at it. Decode has low
arithmetic intensity
so even though GPUs provide lots of
memory bandwidth
, it’s tricky to keep the
arithmetic bandwidth
saturated.
Agentic applications skew heavy on the decode — even though there are more input tokens than output tokens, the decode is so much slower that it takes most of the time. This problem is so bad that inference service deployments are often forced to adopt complex solutions like cross-node prefill-decode disaggregation just to get acceptable perf.
But not
all
tokens are generated during decode. The final “prefill” forward pass during input sequence processing emits a prediction for a single token.
And for Boolean classification of a sequence, aka
AI.IF
, a single token is all you need — literally.
This matters because
AI.IF
isn’t a sideshow. It’s how joins are implemented in AI-SQL (
JOIN ON AI.IF
). With a bit of cleverness in prompt construction,
AI.CLASSIFY
can be mapped onto a single token as well, for a number of classes up to the size of the vocabulary (we’ve left that one for future work!).
Presently, we don’t take much advantage of this, except in what we
don’t
implement:
Separate prefill and decode phases (let alone disaggregation), because there is no decode
Sampling, because there are no generated tokens, only probabilities
CUDA Graph capture, because prefills have long enough durations that launch overhead is negligible, even for small models on big GPUs
Speculative decoding
, because that accelerates decodes of more than one token
But we anticipate deeper opportunities to optimize prefill-only inference!
Quail jointly optimizes a SQL query and an inference workload.
With the shape of the SQL problem and the inference problem in hand, let’s now quickly walk through the architecture of Quail, with a focus on the query planner and execution engine.
Architecture overview
You may not have noticed yet, but building databases is easy now (see
Stonebraker & Pavlo, 2024
or
this talk on Apache DataFusion by Andrew Lamb
). Specifically, analytical databases are much easier to build because many key components are standardized with extensible open source implementations. And composing open source components is now mad easy, thanks to coding agents.
The key components are, in order from external interface to internal implementation details, the SQL parser, the query planner, the execution engine, and the storage engine.
SQL Parser
. We use
the Python
sqlglot
library by
@tobymao
, which has
snowflake
and
bigquery
dialects. AI-SQL is handled via “anonymous” expressions, aka punted to the query planner.
Query Planner.
This part is substantively custom, since it is the meat of the work. We describe it below. We use
Substrait
to serialize query plans for benchmarking.
Execution Engine.
We forked off of vLLM’s implementation for model forward passes, then modified the kernels as described below (mostly writing Triton to get kernel fusion). We didn’t add full SQL execution support yet, but that’s a fairly straightforward addition with DataFusion.
Storage Engine.
We use
pyarrow
to manage the columnar Arrow format. This an analytical workload, which is write-once/read-many, aka “filesystems on easy mode”. We assume this is fetched up front from object storage like S3 or a distributed filesystem like
Modal Volumes
.
Designing a query planner for an inference engine
The query planner takes a logical plan based on parsing the SQL query and transforms that plan — both across equivalent logical plans and into “physical” plans with concrete operations. The design space for query planners is humongous. They are, after all, essentially compilers!
But our problem set is restricted to filters and joins, and within that we were further able to mostly use well-known techniques. We do predicate push-down past joins, filter ordering based on selectivity a la
Hellerstein and Stonebraker
, and join ordering with dynamic programming on deep trees as in
the classic 1976 System R paper
. That’s a very terse overview — more details on the database side on the Full Stack Data Lab blog
here
!
Here, we’ll briefly touch on the Transformer inference/GPU-centric contributions, in the cost model and join ordering algorithm. Specifically, Quail adds speed-of-light estimation to the cost model and KV-awareness to the join order search.
KV-aware join-order search
Join ordering is classically based on “divide-and-conquer” dynamic programming. At a high level: select the optimal choice at one step, then search for the optimal sub-plan with that choice fixed.
Our case is not quite as simple as normal join ordering. We additionally track KV state from previous plans just in case what looked like a bad option at first turns out to be useful for a later join that can re-use its KV.
During search, we maintain multiple candidates. We eliminate plans only if a new candidate plan has fewer tokens, fewer attention pairs, and fewer cached tokens — it has been “dominated”, in the Pareto sense. We then select the final plan by applying the speed-of-light cost estimate, described below.
Join ordering is hard! We expect there to be substantial improvements to this technique, and we’d love to work on them with you.
Pessimistically estimating the speed of light
Like most databases, our hardware-based cost estimates are fairly crude. We use
Williams, Waterman, & Patterson’s “roofline model”
of throughput-oriented hardware to estimate the “speed-of-light” based on hardware
peak rates
, which has its limitations (cf last paragraph in
our GPU Performance Glossary entry on performance bottlenecks
).
But crude doesn’t mean ineffective! For one, the SoL model was a critical tool for sanity checking results while iterating. For another, it errs on the side of over-estimating peak performance, rather than missing at random or under-estimating. Compare it to the north star: you can never reach it, but it still helps you head north.
Detailed code is
here
, but the cost model something like this:
The calculation is based only on the subset of modules that are high poles in the tent for the target workloads: per-token attention projections and MLP/MoE layers and cross-token attention calculations.
In principle this must be done once per model, but in practice models share a lot of operators. We’ve found that contemporary coding agents are quite good at reading a Hugging Face config and generating a reasonable cost model in this setup — though their output often needs a vibe check. For another application of roofline-SoL-based cost modeling, see
our speculative decoding speedup estimator
.
An inference engine as an execution engine
Once a final physical plan has been selected, it must be implemented by the execution engine.
But before thinking too much about the GPU side of things, it is important to
get the CPU out of the way
. Anyone who has worked on high-performance storage or networking will be familiar with the basic beats here.
In this case, we have lots of sequences (millions) and a small model (billions of parameters) on a big GPU (H100), which is outside of the design space for most tokenizer backends. We used
Gigatoken
from our friend Marcel Rød at Stanford. Side note: this work happens in the query planner, but then gets re-used at execution time. We store token IDs in memory-mapped Arrow files, the same basic technology in our storage engine.
Going down to the GPU layer: we started from the model forward pass implementations in vLLM and then rewrote them with a few custom optimizations. We’re very grateful to be able to build on the work of the community here!
The kernels we use for the core matmul and attention operations are standard:
DeepSeek’s DeepGEMM
and
Dao et al.’s Flash Attention 3
. These kernels are quite good at high-throughput/prefill-only inference.
The speed-of-light cost model only considers these operations, but there are many others in the forward pass. Their runtimes are in principle negligible, but there are a lot of them and they add up, including host overhead to launch those kernels.
The standard technique here is to combine several smaller kernels into one, aka
kernel fusion
. Luckily it is quite easy now to author a custom kernel in
OpenAI’s Triton
— especially with coding agent assistance and a reference implementation! We fuse the add-RMSNorm with fp8 quantization and we fuse the per-head query/key RMSNorm with rotary embeddings.
We do need to “wrap” FlashAttention in some custom logic. In the join of A and B, many suffix documents from B attend to the same anchor from A. Naïvely mapped onto FlashAttention, that gives you many replications of the anchor during execution.
We avoid this by doing a “recursive” or “combination of partials” attention calculation for joins.
First, we attend from all suffix queries to the anchor, a kind of “cross-attention”. Suffixes then attend to themselves, and results are finally merged with LSE-rescaling, a la
Dao et al.’s flash decoding
. Suffixes’ KV are not written to cache — we’re doing zero decode, and we never do (N>2)-way joins, so we don’t need them!
This is very similar to
Flash Infer’s cascade attention
or
Scaly/Hazy’s Hydragen
. It also looks like
tree attention
, but for the special case of a depth-one tree. We have the same motivation as in those techniques: shared re-use of prefixes. But because we know the shared prefixes ahead of time, we can skip a lot of complexity.
Additionally, we make one optimization at the model layer. Because we’re only doing filters and joins, we only need the model to output probabilities for truthy and falsy tokens. That means our vocabulary only has 8 options — an extreme case of structured outputs. This is known at engine boot time, so we just drop those columns from the model’s language-modeling head entirely, cutting the final unembedding matmul from vocab size x latent size to 8 x latent size.
What is the future of inference engines?
Finally, if you run AI-SQL queries and are interested in improving performance and cutting costs,
get in touch with us
.
We’ve
worked
a
lot
on
SGLang
and built our own custom engines, including Quail, and this has led to us having some
opinions
about where the field is going. This is both a critical time for inference engine work, because these systems are new (years old, not decades), and for software engineering as a whole, because coding agents are changing the constraints on research and development. A few notes on this below.
This is only the beginning for optimized AI-SQL inference.
There are many obvious additional optimizations for Quail and AI-SQL workloads. We could produce better plans and we’re still short of the speed-of-light for the plans we execute.
Here’s a quick
flag-planting list so we can Schmidhuber anyone who implements them
list of things we’d love to see more work on:
1. Add more tiers to the KV cache.
We only cache KV values in the GPU HBM. But there are more storage layers, and great caches are always multi-layer. Systems like
LMSYS Org’s HiCache
help manage multi-layer caches.
We’ve used it for the workload class it is designed for
, chatbot/agent inference, but we didn’t apply it here.
Because this workload is quite different, we expect there to be room to improve existing caching systems. In particular, we both know more about and have more control over request ordering, so we can more directly manage the cache, and we are substantively insensitive to latency, so we benefit from even higher, slower tiers of storage, especially with striping. Perhaps we might feed our LLM from tapes?
2. Optimize across queries.
We also only cache KV values during the lifetime of a request. We don’t toss Bloom filters or zone maps in the trash so why do it with KV cache? GPU HBM is too precious to do this, but higher cache tiers are much cheaper.
3. Support larger-than-memory datasets.
As evinced by the success of
antirez’s Redis
and
Mühleisen and Raasveldt’s DuckDB
, you can build a useful database system without a backing durable store. And inference is so computationally intense that dataset sizes are often smaller.
But that’s not an excuse to stop at in-memory processing! Because the KV representation is so much larger than the stored representation, applying this technique will also benefit from tiered KV caching.
4. Radix index for better sharing.
In our benchmark suite, we fall behind vLLM on one case: processing a dataset of agent traces. We added this benchmark specifically because we wanted to demonstrate that our system, as we initially constructed it, was making a trade-off, rather than somehow being universally better than existing engines with far more engineering effort.
In particular, the agent benchmark can be mapped into agent serving — simply store all session histories in the database, then
SELECT
those histories with a new input message and run
AI_COMPLETE
. This creates a lot of cross-document prefix sharing that our current system can’t model or take advantage of.
But we could still make Quail’s performance better here! For instance, we might construct a radix tree index over documents and then look for KV cache re-use opportunities.
5. Better overlap across kernels.
We stuck to relatively simple kernel-level techniques like fusion in Triton, and we know we’re still short of the speed of light. A common cause of shortfall there is overhead or insufficient re-use of resources across kernels. A
throughput-oriented megakernel a la Hazy Research
or even just
CUDA programmatic dependent launch
would improve overlap and might improve performance.
6. On-the-fly fine-tuning.
Lastly, something much more speculative. In modern analytical databases, operators are often optimized mid-execution, e.g. with specialization and JIT compilation — see
Umbra’s “Flying Start” compiler
. These optimized modules are then swapped in to the query mid-execution.
We might similarly “compile” faster models via quantization, pruning, distillation, and similar techniques, run concurrently with the query and then swapped in once accuracy reaches acceptable levels. And ML training can indeed be operationalized to this degree! See
Anil et al.’s “On the Factory Floor” paper
.
Vibe-coded inference engines with a shared core.
We did most of this work by prompting coding agents. The hard part was no longer execution on ideas, but problem definition and result measurement — taste and quality assurance.
Is this where software engineering and systems research is going? We don’t know, but it seems likely to us! Whatever happens, it will be weird, and it will require the kind of thoughtful attention to working habits, to community structure, and to incentives
that has been recently admirably demonstrated by the mathematics community
.
More narrowly, we are very aware that there has been a recent efflorescence of custom inference engines, where the engine is developed with a narrower workload or set of workloads in mind. The
VibeServe agentic development system from the SyFI lab
demonstrates that this authoring process can even be generalized, subject to properly defined baselines and goals.
We expect this trend to continue, but we don’t expect all code for inference systems to be written from scratch per application just yet. There is too much benefit from open source collaboration — operational simplicity, increased velocity, “given enough eyeballs, all bugs are shallow”. Coding agents change some of the coefficients, but we don’t think they eliminate the cooperative equilibrium strategy that drives open source contribution.
Instead, we think the inference world will soon look a bit more like databases post-
DataFusion
: a reusable “core” that is expressive enough to absorb new techniques but controlled enough to provide guarantees. For a proof-of-concept, see
ekzhang’s tweet about an agent-extensible inference engine
.
Existing inference engines like vLLM and SGLang might also be adapted to serve better as that core — see the
nano-vllm
and
mini-sglang
projects.
Acknowledgements
We thank
Joe Barrow
of Adobe and the team at
DoubleWord
, especially
Fergus Finn
, for reviewing and providing feedback on this work.
