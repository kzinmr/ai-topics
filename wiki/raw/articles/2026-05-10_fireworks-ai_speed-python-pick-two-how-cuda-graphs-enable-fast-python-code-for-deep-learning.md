---
title: "Speed, Python: Pick Two. How CUDA Graphs Enable Fast Python Code for Deep Learning"
source: "Fireworks AI Blog"
url: "https://fireworks.ai/blog/speed-python-pick-two-how-cuda-graphs-enable-fast-python-code-for-deep-learning"
scraped: "2026-05-10T01:21:10.611902+00:00"
lastmod: "2026-02-12T18:53:30.000Z"
type: "sitemap"
---

# Speed, Python: Pick Two. How CUDA Graphs Enable Fast Python Code for Deep Learning

**Source**: [https://fireworks.ai/blog/speed-python-pick-two-how-cuda-graphs-enable-fast-python-code-for-deep-learning](https://fireworks.ai/blog/speed-python-pick-two-how-cuda-graphs-enable-fast-python-code-for-deep-learning)

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
Speed Python Pick Two How Cuda Graphs Enable Fast Python Code For Deep Learning
Speed, Python: Pick Two. How CUDA Graphs Enable Fast Python Code for Deep Learning
PUBLISHED
8/29/2023
Table of Contents
Keeping Modern GPUs Busy: CPU/GPU Overlap
CPU Overheads — Where Does All The Time Go?
Feed the (GPU) Beast: Optimizing for CPU Overheads
CUDA Graphs
LLM Inference + CUDA graphs
Real-World CUDA Graphs: LLaMA v2 Inference
LLaMA2–7B + CUDA Graph Inference Performance Results
CUDA Graphs in the Fireworks Inference Platform
Conclusion
Appendix
Table of Contents
Table of Contents
Keeping Modern GPUs Busy: CPU/GPU Overlap
CPU Overheads — Where Does All The Time Go?
Feed the (GPU) Beast: Optimizing for CPU Overheads
CUDA Graphs
LLM Inference + CUDA graphs
Real-World CUDA Graphs: LLaMA v2 Inference
LLaMA2–7B + CUDA Graph Inference Performance Results
CUDA Graphs in the Fireworks Inference Platform
Conclusion
Appendix
Table of Contents
This is the second in a series of technical blog posts about the techniques we use for optimization of the high-performance
Fireworks Gen AI Platform
. See also the previous post about
Multi-Query Attention
.
This post explores how the explosion in GPU speed over the past several years has changed the landscape of performance optimization for deep learning workloads. We examine how the host CPU has become a bottleneck due to this trend and review several techniques for mitigating this. We highlight one technique — CUDA graphs — that balances performance with usability. We examine the effect of CUDA graphs on Large Language Model (LLM) inference workloads and show a
2.3x speedup on a LLaMAv2–7B inference workload
.
We show that the
Fireworks Inference Platform
uses CUDA graphs and other aggressive machine and service optimizations to provide best-in-class speed and efficiency for LLM serving.
Keeping Modern GPUs Busy: CPU/GPU Overlap
Contemporary deep learning programs are most often written in the Python language using PyTorch as a framework. PyTorch is fundamentally simple: a collection of pre-optimized
Tensor
operations that the user calls from a Python program. On the other hand, PyTorch has historically provided high performance for deep learning workloads, as described in the PyTorch
paper
. A key idea introduced in the PyTorch paper is the idea of
CPU/GPU overlap
: the CPU program dispatches work (kernels) for the GPU to execute, and so long as the CPU program runs faster than the GPU work, high performance is achieved.
A large batch-size training run with high CPU/GPU overlap
However, the claims made in the paper about CPU/GPU overlap have become less true over time as GPU speeds have increased at a breakneck pace. Let's examine floating point performance and memory bandwidth for GPU architectures over time:
•
GP100 (as evaluated in the PyTorch paper)
(2016) has 21
TFLOPS
half-precision and 730 GB/s memory bandwidth
•
V100
(2017) has 112 TFLOPS half-precision (TensorCores) and 900 GB/s memory bandwidth
•
A100
(2020) has 312 TFLOPS half-precision (TensorCores) and 1600–2000 GB/s memory bandwidth
•
H100
(2022) 989 TFLOPs half-precision (TensorCores) and 3350 GB/s memory bandwidth
NVIDIA GPU Performance Over Time
GPU half-precision floating point performance has increased
47x
and memory bandwidth has increased
4.6x
since the PyTorch paper was written. This speedup has profound implications on the ability of the CPU to stay ahead of the GPU and deliver maximum performance for deep learning workloads.
CPU Overheads — Where Does All The Time Go?
What exactly is the CPU doing when you run a PyTorch program? Several layers of overhead exist.
First, a PyTorch program has user-written logic that must be executed on the CPU. This logic includes metaprogramming, i.e. defining the structure of the network in Python code based on the hyperparameters. The simplest example of this is a loop over network layers. The best practice when writing PyTorch programs is to push this logic into Module construction so that this overhead is not incurred during model execution. Nonetheless, metaprogramming overheads still exist at runtime in most PyTorch programs.
Second, when calling PyTorch operations, several decisions must be made about which compute kernel to call on the device (GPU) based on properties like the device/dtype of the operands or whether
autograd
recording is enabled. These decisions are made by a component called the
dispatcher
running on the CPU. Although the dispatcher is written as highly-optimized C++, its execution still contributes to runtime overhead while executing a PyTorch program.
Third, GPU memory allocation contributes to runtime overhead. PyTorch uses a sophisticated
caching memory allocator
to alleviate much of this overhead, but runtime performance may still be negatively affected by allocator activities on the CPU when executing programs with small operations.
Finally, CUDA itself has overheads in the driver and kernel launch paths, which can slow down the CPU execution of the program.
Feed the (GPU) Beast: Optimizing for CPU Overheads
As GPUs get faster, CPU overheads become more of a problem when executing deep learning programs. Several techniques and tools have emerged to solve this problem.
A batch-size 1 inference run on a HuggingFace Transformers model with very poor CPU/GPU overlap
HuggingFace Transformers
is a ubiquitous codebase for language models based on the
Transformer
architecture. However, in practice, Transformers is not highly optimized for inference, as the Python code is written in a way that maximizes flexibility but incurs significant CPU overhead. On the other end of the spectrum is
FasterTransformer
(FT), written in highly optimized C++ to maximize performance. In practice, FT's optimized C++ code is quite hard to work with, slowing down the development of new features or adding new model architectures (e.g.
LLaMA
models are
not officially supported
).
Another approach to performance optimization is automatic code transformation via compilation.
Apache TVM
is an early example of this approach, which provided an end-to-end stack that compiled a high-level representation of a neural network down to native machine code (e.g. on GPU). However, converting from a flexible PyTorch program to TVM's high-level representation is non-trivial, especially when a program contains control flow (loops, branches) implemented in Python or when a program involves distributed operations. Dynamic shapes (Tensor shapes that change at runtime) introduce additional complications.
A newer approach is
[torch.compile](https://pytorch.org/tutorials/intermediate/torch_compile_tutorial.html)
, as released with PyTorch 2.0.
torch.compile
improves upon the usability of existing compilation stacks with
TorchDynamo
, a new front-end that automatically analyzes the Python bytecode of the program to extract sections of the program that can be compiled. However, this approach is not fool-proof, as arbitrary Python code can introduce
graph breaks
, which deoptimize the code and cause host-device synchronization. Additionally,
torch.compile
's support for dynamic shapes and distributed operations is still in development, and without it, the applicability of
torch.compile
to LLM inference workloads is limited. Further, support for arbitrary memory layout management and mutation as used in the
PagedAttention
approach is generally not supported by contemporary deep learning compilers. See the Appendix for details about our experiments with
torch.compile
on LLM inference.
Approaches to performance optimization represent various trade-offs between flexibility and speed
Each of the approaches presented has different trade-offs; However, we'd like to highlight one option that we believe balances usability and performance: CUDA graphs.
CUDA Graphs
In CUDA 10, NVIDIA introduced a feature called
CUDA graphs
. CUDA graphs provide a way to record the GPU kernels invoked by a program into a graph data structure and later replay the kernels stored in that graph without incurring the original program's CPU overhead. This approach can help improve the performance of a GPU program where a specific sequence of operations is called many times. In other words, the graph representation can be said to be a
specialized
representation of the program down to kernel dispatch, i.e. the sequence of kernels and the arguments used at trace time (including pointers to Tensor memory) are “baked in” to the graph. Thus, care is needed when recording a CUDA graph to ensure that kernel arguments remain the same across runs.
On top of the CUDA graph API, PyTorch introduced
support
for CUDA graphs from the Python API. The PyTorch CUDA graph API provides additional support for managing PyTorch allocator state to ensure the stability of Tensor allocations (and thus Tensor pointers) across runs.
CUDA graphs address all sources of CPU overhead highlighted above: user-written logic, PyTorch dispatcher logic, memory allocation overhead, and GPU driver/kernel overhead. In addition, the CUDA graphs API in PyTorch is relatively unintrusive so long as you can ensure that your program (or part of your program) conforms to a few
constraints
. This leads to easier to write and maintain code written in Python rather than in messy, optimized C++.
LLM Inference + CUDA graphs
When running inference on a decoder LLM (such as the GPT family of models), there are two computation phases: a
prefill
phase that consumes the prompt and an
incremental generation
phase that generates output tokens one by one. Given a high enough batch size or input length, prefill operates on a sufficiently high number of tokens in parallel that GPU performance is the bottleneck and CPU overheads do not impact performance. On the other hand, incremental generation is always executed with sequence length 1 and it is often executed with a small batch size (even 1), e.g. for interactive use cases. Thus, incremental generation can be limited by the CPU speed and thus is a good candidate for CUDA graphs.
Recall that CUDA graphs have several constraints, including a requirement for fixed shapes. Incremental generation has a fixed sequence length and can be run with a fixed batch size. However, the attention computation operates on the tokens processed so far, meaning this dimension increases by one with each step. These processed sequences are stored in a
KV-cache
. Here we present a code sample demonstrating incremental attention with KV-caching (reproduced from this blog
post
):
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
21
22
# N, h, and d_k are all fixed!
# Cached K and V values across iterations
K
=
torch
.
randn
(
N
,
h
,
.
.
.
,
d_k
)
V
=
torch
.
randn
(
N
,
h
,
.
.
.
,
d_k
)
# Single-step QKV values computed during sequence generation
Q_incr
=
torch
.
randn
(
N
,
h
,
1
,
d_k
)
K_incr
=
torch
.
randn
(
N
,
h
,
1
,
d_k
)
V_incr
=
torch
.
randn
(
N
,
h
,
1
,
d_k
)
# <...>
# Update KV-cache
K
=
torch
.
cat
(
[
K
,
K_incr
]
,
dim
=
-
2
)
V
=
torch
.
cat
(
[
V
,
V_incr
]
,
dim
=
-
2
)
# Compute attention (L is sequence length so far)
# \*\*\*\*L changes on each iteration!\*\*\*\*
logits
=
torch
.
matmul
(
Q_incr
,
K
.
transpose
(
2
,
3
)
)
# Output shape \[N, h, 1, L\]
softmax_out
=
torch
.
softmax
(
logits
/
math
.
sqrt
(
d_k
)
,
dim
=
-
1
)
# Output shape \[N, h, 1, L\]
attn_out
=
torch
.
matmul
(
softmax_out
,
V
)
# Output shape \[N, h, 1, d_k\]
While both the regular attention mechanism and the
PagedAttention
scheme undergo shape changes over iterations, the latter provides a unique advantage when integrating with CUDA graphs. From the perspective of kernel arguments, PagedAttention provides a level of indirection for Tensor addresses. The base pointers to the K and V caches remain consistent across iterations and are safe to preserve as kernel arguments. The set of cache locations the kernel operates on is stored in a buffer with a fixed location in GPU memory, and thus, pointers to specific K and V locations can be computed entirely within the kernel. As a result, the entire computation within the incremental generation step can be soundly recorded into a CUDA graph. To keep track of page mapping, PagedAttention uses a varying-size Tensor called
block_tables
, which would naïvely present issues for CUDA graphs. However, this Tensor can be cheaply padded since its elements are relatively small indices. A subset of the
block_tables
tensor is then used on each invocation. This design not only aligns well with the flexibility offered by PyTorch's coding environment, but it also ensures a runtime that's either equivalent or superior to FasterTransformers, all while maintaining code simplicity.
Since CUDA graphs are shape-specialized, special care must be taken when handling a changing batch size at runtime. When using CUDA graphs for multiple batch sizes, it's best to trace a separate graph for each batch size and dispatch to the appropriate one during runtime.
PyTorch's CUDA graphs support using a
memory pool
to encapsulate allocations used during trace time and use them (and crucially, their pointers) during runtime. When compiling for multiple batch sizes, instead of giving each graph its own memory pool, a single shared memory pool can be used. By compiling graphs in decreasing order of batch size, memory from the shared pool is reused, as smaller allocations can be serviced by larger allocated buffers from a previous iteration. This way, multiple batch sizes are supported without using excessive GPU memory.
Real-World CUDA Graphs: LLaMA v2 Inference
To demonstrate applying CUDA graphs in a real-world scenario, we modify the source code of the
LLaMA2
code as released by Meta research. A full diff can be found
here
. The changes required to enable CUDA graphs are rather minimal, consisting of some changes to how attention is implemented in the model and some infrastructural additions in the generation routines.
For modifications to attention, we modify the KV-cache handling to take the indices in which to write new values in a CUDA Tensor rather than a Python integer. We also modify attention to compute over the max sequence length but only compute softmax over the sequence positions <= the current time step. The changes are as follows:
Modifications made to attention to support CUDA graphs
To support this change, we refactor the generation of KV-cache indices and the attention mask. We generate the KV cache indices as a CUDA Tensor. We also augment mask generation to mask out sequence positions up to max_seq_len, in addition to traditional causal masking:
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
def
params_for_incremental_gen
(
self
,
tokens
:
torch
.
Tensor
,
prev_pos
:
int
,
cur_pos
:
int
,
device
:
torch
.
device
)
:
tokens_sliced
=
tokens
[
:
,
prev_pos
:
cur_pos
]
.
to
(
device
=
device
)
valid_seq_pos
=
torch
.
arange
(
prev_pos
,
cur_pos
,
device
=
device
)
mask
=
torch
.
full
(
(
1
,
1
,
1
,
self
.
params
.
max_seq_len
)
,
float
(
"-inf"
)
,
device
=
device
)
mask
[
:
,
:
,
:
,
:
valid_seq_pos
.
item
(
)
+
1
]
=
0.0
return
tokens_sliced
,
mask
,
valid_seq_pos
Note that these changes are correct but rather inefficient, as we compute attention over more sequence positions than we need to (up to
max_seq_len
). The PagedAttention approach addresses this issue, pushing KV-cache management into the kernels themselves while avoiding unnecessary computation. However, we show that even with this naïve approach, CUDA graphs present significant performance advantages over stock PyTorch code.
The infrastructure needed to compile the model for CUDA graphs in incremental generation is fairly simple and close to the examples in the PyTorch
documentation
. Some special care is taken to cache static inputs and outputs for further invocation, but otherwise, the code is
straightforward
:
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
21
22
23
24
25
26
def
_compile_model
(
self
,
tokens_sliced
:
torch
.
Tensor
,
mask
:
torch
.
Tensor
,
valid_seq_pos
:
torch
.
Tensor
)
:
assert
self
.
_cuda_graph
is
None
and
self
.
_compiled_inputs
is
None
and
self
.
_compiled_logits
is
None
,
"Already compiled the model"
self
.
_compiled_inputs
=
tuple
(
v
.
clone
(
)
for
v
in
(
tokens_sliced
,
mask
,
valid_seq_pos
)
)
s
=
torch
.
cuda
.
Stream
(
)
s
.
wait_stream
(
torch
.
cuda
.
current_stream
(
)
)
with
torch
.
cuda
.
stream
(
s
)
:
_
=
self
.
model
.
forward
(
*
self
.
_compiled_inputs
)
torch
.
cuda
.
current_stream
(
)
.
wait_stream
(
s
)
self
.
_cuda_graph
=
torch
.
cuda
.
CUDA graph
(
)
with
torch
.
cuda
.
graph
(
self
.
_cuda_graph
)
:
self
.
_compiled_logits
=
self
.
model
.
forward
(
*
self
.
_compiled_inputs
)
def
replay
(
tokens
,
mask
,
valid_seq_pos
)
:
self
.
_compiled_inputs
[
0
]
.
copy_
(
tokens
)
self
.
_compiled_inputs
[
1
]
.
copy_
(
mask
)
self
.
_compiled_inputs
[
2
]
.
copy_
(
valid_seq_pos
)
self
.
_cuda_graph
.
replay
(
)
return
self
.
_compiled_logits
return
replay
We'd also like to shout out Bram Wasti's technique for easy CUDA graph application via a Python
decorator
. Although this is not applicable in our non-trivial LLM inference case, this approach may still be applicable in many other cases, e.g. image model inference or training with fixed sizes.
LLaMA2–7B + CUDA Graph Inference Performance Results
We test the above approach for compiling LLaMA-2 with the 7B model variant under
batch_size=1
inference conditions. We implement a benchmark
harness
to measure inference performance with CUDA graphs disabled and enabled, respectively. We test on a single NVIDIA A100-SXM4–80GB GPU. We find that without CUDA graphs, LLaMA-7B inference executes at
30 tokens/sec
, but with CUDA graphs enabled it executes at
69 tokens/sec
for a
2.3x speedup
.
We find that this speedup is entirely explained by CPU overhead reduction. The baseline run is dominated by CPU execution — GPU compute kernels are waiting for the CPU to dispatch them. This can be seen from a performance profile:
Overall Timeline of Execution for Non-CUDA Graph Model
Detail View of Timeline of Execution for Non-CUDA Graph Model
In this timeline, the GPU (bottom timeline) spends most of its time idle, waiting for the CPU (top timeline) to issue work. On the other hand, CUDA graph execution shows tight kernel dispatch behavior, running long sequences of kernels at once:
Overall Timeline of Execution for Non-CUDA Graph Model
Detail View of Timeline of Execution for Non-CUDA Graph Model
In this timeline, the GPU is consistently performing work, as the CPU overhead has been skipped.
CUDA Graphs in the Fireworks Inference Platform
The
Fireworks Inference Platform
makes heavy use of CUDA graphs for all served models. We apply CUDA graphs and numerous other techniques (including
multi-query attention
and others) to provide the best inference performance in the industry. We support a growing number of
models
, including those in the LLaMA and StarCoder families, all with CUDA graphs and aggressive optimizations applied. Our Python-centric codebase with CUDA graphs allows us to get good performance while still retaining the flexibility and speed of development. This allows us to be on the cutting edge of AI development, e.g., enabling the latest models like Code Llama just
hours after their release
.
Try out models on our platform
today for free to see what kind of performance we can deliver for Large Language Models in your product.
Conclusion
In conclusion, the substantial advancements in GPU speed in recent years have significantly altered the field of performance optimization for deep learning workloads. As a result, the host CPU has emerged as a bottleneck in processing. To address this, we evaluated several techniques, with CUDA graphs being a method that combines significant performance improvement with code flexibility and usability. After studying the impacts of CUDA graphs on Large Language Model workloads, we conclude that it presents a compelling solution for performance optimization in the face of rapid GPU improvement and we use it extensively in the
Fireworks Generative AI Platform
.
Appendix
CUDA Graphs in PyTorch 2.0's torch.compile
While applying CUDA graphs is easier than rewriting an entire model in C++, it still requires a lot of care. New compilation techniques in PyTorch 2.0 (
torch.compile
) aim to simplify and automate this process in the long run. When invoked with
[mode='reduce-overhead'](https://pytorch.org/get-started/pytorch-2.0/#user-experience)
,
torch.compile
tries to apply CUDA graphs to the extracted graphs of PyTorch operations. Today, this technique works well on smaller programs or
computer vision models
. We ran into issues applying it to the reference Llama code used in this post:
•
Graph capture failed with
torch.inference_mode
annotations, but worked when replaced by
torch.no_grad
(which, however, doesn't optimize away all bookkeeping)
•
The LLaMA reference code uses tensor parallelism via explicit distributed operations in
fairscale
. They introduce graph breaks and eliminate any benefits from compilation. For evaluation, we removed distributed support, thus limiting applicability to a single GPU. Note that distributed collectives are
supported
with CUDA graphs on their own.
•
Positional embeddings in the LLaMA codebase are computed using complex numbers. As of stable PyTorch 2.0.1, they can't be captured by compilation. After switching to the latest PyTorch 2.1 nightly, which includes
the fix
, the capture succeeds but torchinductor still generates warnings about the quality of compiled kernels potentially being not optimal.
•
Beyond the LLaMA reference codebase, custom operations like PagedAttention require additional handling to be capturable by
torch.compile
.
After applying the above changes to the repo (see the
full diff
), we could run
torch.compile
successfully in a non-distributed setup for the LLaMA-7B model. Inference speed matches manual CUDA Graph application exactly at 69 token/s for batch size 1 on A100. Based on the profiler, the entire generation step gets wrapped in a single CUDA graph invocation. Interestingly, a few fusions from torchinductor don't seem to change inference speed. Though
torch.compile
provides similar performance benefits for non-distributed cases, the warm-up time for compilation is about 3 minutes, compared to sub-second initialization time for explicit CUDA graphs. We tried making
torch.compile
skip fused kernel generation and only apply CUDA graphs using
backend='cudagraphs'
, but it errored out.
torch.compile
may be a viable solution for LLM inference in the future, but for now, these optimizations require specific expertise that is not yet sufficiently automated.
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
