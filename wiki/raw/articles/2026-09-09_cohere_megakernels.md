---
title: "Cohere's North Mini Code Megakernel Serving Engine"
source: "Cohere Blog"
url: "https://cohere.com/blog/megakernels"
scraped: "2026-09-09T06:00:03.393307+00:00"
lastmod: "2026-09-08"
type: "sitemap"
---

# Cohere's North Mini Code Megakernel Serving Engine

**Source**: [https://cohere.com/blog/megakernels](https://cohere.com/blog/megakernels)

Today, Cohere presents a serving engine for
North Mini Code
built around a decode megakernel: BF16 on a single H100, 1.25× - 1.41× faster than vLLM end-to-end. Explore the code behind the serving engine on
GitHub
.
Most LLM serving stacks still treat each forward pass as a sequence of kernels: launch QKV, wait; launch attention, wait; launch the MoE, wait. Each launch is fine on its own. The problem is the waiting in between. At small batch sizes, the GPU spends a surprising fraction of every decode step waiting rather than computing.
Autoregressive decoding, especially at lower batch sizes is fundamentally memory-bound. For every decode step, we move a large fraction of memory from HBM while relatively doing less compute. This means the correct question to ask is, how effectively can we use memory bandwidth and not the flops. Take North Mini Code which is a 30B model with 3.3B parameters active per token, which in BF16 means streaming 6.6 GB of weights during every decode step, plus roughly 0.5 GB of KV cache at 8K context. An H100 delivers 3.35 TB/s of bandwidth through HBM, putting the Speed-of-Light (SoL) at about 470 tok/s. vLLM serves this model at 185 tok/s, merely 39% of SoL.
Megakernels have been getting attention lately as the way to close that gap: instead of a hundred small kernels, run the entire forward pass as one persistent kernel. Starting from the pioneering work by
Hazy Research's "Look Ma, No Bubbles!"
, whose design we recap below, numerous follow-up works have been released, achieving various levels of speedup. Existing work has gone mainly in two directions: compilers that generate megakernels automatically, and standalone demos that measure decode speed at batch size 1.
We take one step further. This post presents what we believe is the first fully fledged serving system built around a decode megakernel. It supports everything a real server needs: continuous batching, paged attention, and ragged sequence lengths, all behind an OpenAI-compatible endpoint with tool calling. Point OpenCode at it and you can code with it.
On batch size 1, our megakernel reaches 292 tok/s, or 62% of SoL — 1.58× faster than vLLM. That margin holds across batch sizes and out to 256K of context, with no measurable loss of accuracy.
Image 1: Decode throughput of various context lengths at batch size 1. Megakernel consistently outperforms vLLM.
We also found that megakernels are much easier to write than their reputation suggests, so we include a recipe for porting kernels you already have into one. Ours is a single CUDA file: no compiler, no new programming paradigm, no exotic abstractions — just ordinary tiled GEMMs and ordinary paged attention, restructured to fit a single calling convention.
What is a Megakernel?
A GPU is roughly 100–150 independent processors, called SMs (streaming multiprocessors), that all run the same program — a
kernel
— on different pieces of data. A megakernel is a single persistent kernel that runs an entire forward pass: we launch exactly one threadblock per SM, and it stays resident for the entire decode step. Instead of receiving work from the driver, each block reads a
task list
— a list of small pieces of work it should execute, prepared on the host and sitting in global memory. Instead of kernel boundaries encoding the data dependencies, dependencies are expressed as explicit counters in global memory that tasks increment when they finish and spin on when they need an input.
The result is that the unit of scheduling shrinks from an entire operation to one tile of one operation, and the unit of synchronization shrinks from the whole GPU to the specific producers a task depends on.
Image 2: One decode step, from the host to the device. Instead of one kernel per operation, the host decomposes the step into tasks — one tile of one operation each — and distributes them round-robin over the SMs, so every SM gets its own task list in global memory. The order of most tasks are determined on host by the scheduler (see the scheduler section). Full attention and the MoE are the exception: their task counts depend on the live sequence lengths and on routing, so they go into shared work queues that any SM can pull from. We describe the details in the following sections.
Where the speedup comes from
Inference engines typically launch one kernel per operation — RMSNorm, QKV, attention, MoE, and so on — and most optimization effort goes into making each of those kernels as fast as it can be. That works well for training and prefill, where the workload is large compute-bound GEMMs and every kernel has enough work to saturate the SMs.
Decode is the opposite regime: it is bound by memory bandwidth and by latency. A decode step is mostly GEMVs with low arithmetic intensity, so its speed is determined by how fast weights can be streamed from HBM into shared memory. Anything that keeps weights from moving is lost time, and a kernel-per-operation approach has several places where they stop moving. Together those stalls account for most of the 61% of bandwidth that a typical inference engine leaves unused.
The simplest benefit comes from
reduced
launch and synchronization overhead
. Between two consecutive kernels, every SM must finish before any SM can start the next one, and the driver has to dispatch the next grid. For a decode step made of dozens of small kernels per layer, those gaps add up. A megakernel pays that cost once per step rather than once per operation. We list three more benefits that matter more for this model, in rough order of impact:
1. Reduce wave quantization
Suppose a kernel has 200 tiles of work to do and the GPU has 132 SMs. The first 132 tiles run in parallel; the remaining 68 run in a second wave while 64 SMs sit idle. The kernel takes two waves' worth of time to do 1.5 waves' worth of work, and the smaller the kernel, the worse that rounding gets. This is not something we can fix by dividing the work more evenly. GEMM tile shapes are constrained by the matrix dimensions and the kernel design, so the total tile count rarely lands on an exact multiple of the SM count.
Image 3: Wave quantization reduces GPU utilization.
In a megakernel there is no boundary to round up to: a tile whose inputs are ready starts on whichever SM is free. North Mini Code gains more from this than most architectures because it uses
parallel transformer layers
: attention and the MoE feed-forward are computed from the same normalized input and are rejoined only by a fused residual add + RMSNorm at the end of the layer, so neither attention nor the MoE needs each other's output.
Image 4: A parallel transformer layer used by North Mini Code.
With a megakernel, we can "backfill" the idle SMs with ready work. The parallel transformer layers allow us to perform backfilling in a more aggressive way: whenever possible, we
deterministically
place the tasks that are likely ready to run on the idle SMs. The detail of the placement is described in the task scheduler section. In the figure below, we compare an MoE decode layer run by a conventional serving stack and a megakernel.
Image 5: One MoE decode layer, the same operations in the same order, scheduled two ways. Top: one kernel per operation. Attention does not finish together due to wave quantization and hardware jitter. The barrier at the kernel boundary makes every SM wait for the last one (hatched). The same pattern repeats at each kernel boundary. Bottom: the megakernel. As each SM finishes its attention work it starts an MoE tile, so the same interval carries work instead of waiting. Drawn with 16 SMs and a few dozen tiles per operation so tasks stay visible; the real kernel has 132 SMs and thousands of tasks. Durations are illustrative and the time axis is relative.
2. Drop false dependencies
SMs do not always finish work at the same time, even when workload is identical. A kernel boundary is a full-grid barrier, so the slowest SM sets the pace for all of them. For example, if attention is split across 4 key/value groups and one group finishes early, that SM idles until the other three catch up, even though the data its next operation actually needs is already in memory. Fine-grained barriers drop the false dependency: O-proj for a given KV group starts as soon as
that group's
attention output lands. Similarly, an MoE down projection task can start whenever the up projection task of the corresponding expert is completed, without the need to wait for all experts’ up projection.
3. Weight prefetch
Weights are immutable — they do not depend on this step's activations at all. A task can therefore start streaming its weight tiles from HBM into shared memory
before
its activation dependency has been satisfied, which a kernel boundary would forbid. We use this most aggressively for the router and QKV projections, which prefetch their weights during the tail of the previous layer's O-proj, before RMSNorm has even run, to harvest bandwidth that would otherwise go unused.
Where we started
Our design borrows a lot of insight from the pioneering post on Hazy Research referenced earlier , which fused a Llama-3.2-1B forward pass into a single kernel and reached 78% of an H100's memory bandwidth at batch size 1, against roughly half that for vLLM and SGLang. Three of their ideas are crucial to us:
The “task interpreter” pattern on GPU.
Each SM walks a list of task descriptors prepared on the host and reused across forward passes. A controller warp reads the descriptor and dispatches the task to various on-device functions, each implementing one kind of operation. We describe our implementation of the idea in Figure 2 and 6.
Counter-based synchronization.
Dependency barriers are plain integers in global memory, zeroed before each step. A task increments one when it finishes and spins on one before it starts. We describe our implementation in detail in the Barriers section and Figure 7.
Overlap across task boundaries.
A task can start loading its weights while the previous task on the same SM is still storing its results.
What we have done differently
Our implementation differs from their megakernel in a few ways. Our GEMM implementation relies heavily on tensor core instruction, even for batch size 1 because we found that wgmma is slightly faster in our cases compared to CUDA core and reduces register pressure.
One other difference is that we do not use shared memory paging to implement weight prefetching. We initially experimented with shared-memory paging, which allows memory loads to begin before the previous task releases its buffers. In practice, though, the bookkeeping is complex, introduced a steady source of bugs, and had high overhead that outweighed the benefit. Every opcode instead gets its own warp-specialized pipeline with its shared memory layout statically at compile time, and we get the overlap from two cheaper places.
Between consecutive GEMM tasks of the same type.
An MoE GEMM task walks a list of tiles, and the pipeline carries its stage phases across the whole list instead of draining and refilling the pipeline at every tile boundary. Within the MoE GEMM, the next tile's weights are already in flight while the current tile is still on the tensor cores or epilogue. Because it is the same operation with the same shared memory layout, shared memory paging reduces to a simple multi-stage pipeline. This kind of prefetch shares the same spirit as persistent grouped GEMM kernels.
Inside the GEMM pipeline.
Weights are immutable, so the producer warp issues its weight-tile loads
before
the cross-SM wait for activations; in the pseudocode (Listings 1) shown later in the post,
prefetch_weight_tiles
sits above
wait_input_bars
. MoE down projection is one such example case: its expert weights start streaming from HBM while up/gate is still computing the hidden state that down will consume. Therefore a task blocked on its inputs is still moving bytes. The other example is QKV and router prefetching before RMS norm completion.
We also put substantial effort into scheduling. Most tasks follow a host-built static schedule that we can tune precisely; attention and MoE use local work stealing to balance the runtime-dependent work from continuous batching and routing. We return to this below.
One ABI for every operation
The entire megakernel can be seen as various smaller kernels stitched together by a common calling convention—each smaller kernel must be implemented with exactly 3 warp groups (each warp group has 4 warps) containing 8 consumer warps, 1 controller warp, 1 producer and 1 storer warps, where each warp is subjected to its own register requirement. Additionally, each smaller kernel must read its “parameters” from a fixed sized task descriptor. We feel this kind of convention is analogous to application binary interfaces (ABI) as in compilers and operating systems. We would use the term
“ABI”
to describe the convention throughout the post.
Let's take a GEMM as an example to understand how the ABI works.
Image 6: How one GEMM tile becomes work on an SM. The host divides the output into tiles and writes each one as a 32-int32 descriptor. On the device a controller warp reads the next descriptor and switches on its opcode — QKV, attention, O-proj, or any of the other fourteen — so the same SM can run different operations back to back. The 2×4 grid is illustrative; a real QKV at batch 1 is 80 tiles.
What keeps this writable by hand is that every operation, not just GEMM, obeys that ABI: what a task is, what shape it runs in, and how it signals that it is done. Once all operations follows the same ABI, assembling them into a megakernel becomes very manageable. The rest of this section unpacks those three things.
Tasks
The megakernel does not invent new operations. It takes the usual decode graph — QKV, attention, O-proj, router, MoE, residual/RMSNorm, LM head — and lowers it into a list of small tiled
tasks
. Sixteen opcodes cover the whole decode step:
Group
Opcodes
What one task does
Dense GEMMs
QKV_PROJ, O_PROJ, FFN_UPGATE_ACT, FFN_DOWN, LM_HEAD
One output tile of one matrix multiply, optionally one slice of a split-K reduction. QKV_PROJ also applies RoPE in-register in its epilogue; FFN_UPGATE_ACT fuses the SiLU-and-multiply in its epilogue.
Attention
ATTN_DECODE, ATTN_COMBINE, ATTN_DRAIN
ATTN_DECODE computes attention on partial KV slices; ATTN_COMBINE merges those partials into the real output. ATTN_DRAIN is used only for full attention layers. It s a claimer over dynamically generated work queue — see scheduling section later.
MoE routing
ROUTER_GEMM, ROUTER_TOPK, ROUTE_FINALIZE, MOE_GATHER
Score the 128 experts, compute top-k experts per token and generate MoE GEMM work queue.
MoE GEMMs
MOE_UPGATE_ACT_DRAIN, MOE_DOWN_DRAIN, MOE_COMBINE
The expert FFN, as claimers over the work queue generated by ROUTE_FINALIZE. MOE_COMBINE sums each token's 8 expert outputs, weighted by its router scores.
Join
ADD_RMSNORM
Add the attention and FFN branches back into the residual stream and normalize — the point where a layer's two parallel halves rejoin.
All the GEMM opcodes share one pipeline.
O-proj, the router, the dense FFN, the LM head, and both MoE expert GEMMs run the same warp-specialized body: the producer streams weight and activation tiles into a shared-memory stage ring, the consumers accumulate on tensor cores, the storer writes the output tile and arrives on a barrier. What changes per opcode is a short list of per-op details — which tensors, which barrier to wait on and which to signal, whether the epilogue fuses SiLU-and-multiply, whether the store is a split-K reduction. QKV is that same pipeline with RoPE applied in-register before writing back to HBM. The MoE drains are that same pipeline with a different way of picking the next tile: they claim work from a queue instead of reading the coordinates off the descriptor.
As a result, adding new GEMM task is a small edit rather than a new kernel. We do not rewrite the load/math/store loop, but only fill in those details.
The task descriptor
Each task descriptor is 32 int32 fields, written by the host encoder into a per-SM buffer. Field 0 is the opcode; the rest are op-specific: which layer, which output tile, which split-K slice, how many K-tiles to walk, and — the important part —
which barrier to wait on, what count to wait for, and which barrier to signal on completion
.
The device side is straightforward. One warp per block acts as a
controller
: it prefetches upcoming descriptors into a small shared-memory ring, so an SM never stalls on waiting for task descriptors. The other warps pop tasks off that ring and execute them.
The threadblock shape
Every task, regardless of opcode, runs under the same threadblock shape. 12 warps, organized as 3 warpgroups:
Warps
Role
Job
WG0 warp 0
Controller
Prefetch upcoming task descriptors into a shared-memory ring
WG0 warp 1
Producer
Issue TMA loads, initialize semaphores, wait on input barriers
WG0 warp 2
Storer
Issue TMA stores, signal output barriers
WG0 warp 3
Idle
Not used
WG1-2
Consumer
Actual computation
Most of it follows the standard producer/consumer warp-specialization pattern from a standalone Hopper GEMM. The megakernel's contribution is that every opcode — attention and RMSNorm included — uses this same shape, so an SM that just finished a QKV tile can run an attention slice next without changing how many warps it has or the role of each warp.
The roles are compile-time tags, not runtime branches. Each operation body is templated on the role so
if constexpr (role == PRODUCER)
deletes the unreachable code at compile time. That lets us write producer, consumer, and storer in one function, the way a normal GEMM is written, while each warp only keeps the path it actually runs.
The controller never enters that function. It has its own loop, whose only jobs are to prefetch the next descriptor into a small shared-memory ring and to tell the workers when a slot is ready. One small caveat is that workers cannot use
__syncthreads()
for synchronization between themselves— that would wait for the controller warp that runs independently of workers — so they join among themselves on a named barrier (
worker_sync
) that excludes the controller.
Here is an overview of a GEMM task implemented in the megakernel. If you have written a warp-specialized Hopper kernel, you would probably find the structure familiar. The MoE drain is that same task, called in a loop over tiles claimed from a queue.
def
gemm_task
(
task
):
# compute Y = X @ W
if
constexpr (role == producer):
prefetch_weight_tiles(task)
# optional, before the wait
wait_input_bars(task)
# cross-SM: my activations ready?
for
k
in
k_tiles(task):
tma_load_A_B(k)
# async copy HBM -> shared memory
signal_stage_ready(k)
# intra-block: stage k is loaded
elif
constexpr (role == consumer):
for
k
in
k_tiles(task):
wait_stage_ready(k)
wgmma(k)
# tensor-core MMA
epilogue_to_smem()
elif
constexpr (role == storer):
tma_store_Y()
# async copy shared memory -> HBM
arrive_output_bar(task)
# cross-SM: my tile is visible
worker_sync()
# all worker warps; excluding controller
def
moe_drain_task
(
task
):
while
True
:
tile_id = atomicAdd(n_claimed_tiles,
1
)
if
tile_id >=
len
(moe_workqueue)：
break
tile = moe_workqueue[tile_id]
gemm_task(tile)
def
controller_loop
(
tasks
):
for
i
in
range
(
len
(tasks)):
slot = ring[i % RING]
if
i >= RING:
wait(slot.done)
# workers finished with this slot
slot.task = load(tasks[i])
# prefetch the next descriptor
arrive(slot.ready)
# signal workers: you can start
def
worker_loop
():
for
i
in
range
(
len
(tasks)):
slot = ring[i % RING]
wait(slot.ready)
# descriptor is in shared memory
gemm_task(slot.task)
# or switch(opcode) onto another body
if
storer:
arrive(slot.done)
# slot is free for the next prefetch
Listings 1: We demonstrate how to implement a GEMM task in megakernel. The overall structure follows a standard warp specialized GEMM on Hopper.
The
if constexpr
branches are the compile-time tags from above, not a runtime switch. The two lines that would not appear in a standalone kernel are
wait_input_bars
and
arrive_output_bar
— the cross-SM counters carried in the descriptor.
prefetch_weight_tiles
sitting above the wait is the other optional megakernel-only move.
The controller stays one descriptor ahead of the workers without ever joining their barrier. Attention, routing, and the MoE drains fill in the same producer / consumer / storer slots; only the
switch (opcode)
in
worker_loop
changes. The friction of putting a kernel you already have into the megakernel is those two barrier calls plus this wrapping loop instead of a new programming model.
Barriers
As inspired by Hazy Research, our barriers are implemented as counters in global memory.
//
wait
: spin until enough upstream tasks have arrived
while
(*(volatile const uint32_t*)bar < target) {
__nanosleep(20);
}
__threadfence();
// arrive: publish my tile,
then
signal downstream tasks
fence.proxy.async;     // make async (TMA) stores visible first
__threadfence();       // make data computed by this SM visible to others
atomicAdd(bar, 1);
Listings 2: We implement barriers as counters in global memory. Waiting threads do a spin wait until dependency is satisfied.
That is the entire dependency mechanism. A task waits on a single
count
, not on a specific upstream task, which makes both signalling and waiting for dependencies cost O(1) time, regardless of fan-in and fan-out. The fences are crucial to ensure there is no data race across SMs that silently leads to data corruption.
How do you write a megakernel?
A megakernel sounds like a full rewrite. In practice, the ABI keeps the work contained: once an operation follows the common threadblock shape and descriptor format, it plugs into the megakernel as every other task. The performance-critical logic can be reused from existing kernels.
The recipe we would give someone starting from an existing kernel library:
Start from GEMM and attention kernels that are already competitive standalone.
A megakernel removes the glue
between
operations; it will not make a slow operation fast. Our implementation match cuBLAS and FlashAttention-3 on their own, using plain warp-specialized pipelines without TMA multicast or ping-pong scheduling.
Fit the kernel to the ABI.
Use exactly 8 consumer warps and at most 3 producer/storer warps. For a standard Hopper warp-specialized kernel, this mainly means splitting producer and consumer code into separate functions so per-warpgroup register limits take effect.
Add the barriers that express its data dependencies.
One GEMM tile or one KV group becomes one task. Downstream operations needs to carefully wait on the barriers to ensure data integrity.
Emit task descriptors into the global-memory task list
Tune task order and placement to achieve optimal throughput.
The hard part is step 3. A counting barrier releases when
N
threads arrive without checking
which
threads those were, so one opcode that arrives the wrong number of times can let warps drift onto different tasks and deadlock much later. Barrier accounting needs explicit invariants and careful testing.
A descriptor format, a block shape, and a counter protocol form the whole integration contract. That makes adding a new operation an engineering task with a clear boundary, rather than a new kernel architecture project.
The task scheduler: mapping tasks to SMs
After we implemented the megakernel itself, we need to determine how to assign tasks to each SM and in which order those tasks should be executed. This assignment is referred to as the
task schedule
. A task scheduler takes in the task graph and outputs the exact list of tasks for each SM to execute sequentially. In fact, we have a lot of freedom in designing the schedule. Fine grained barriers only ensure correctness of the megakernel by making sure a task begins only after its inputs are ready. We can shuffle tasks around as long as the schedule does not result in circular waits. While different schedules produce the same output, they change the throughput in a considerable way.
Our scheduler is mostly static, with dynamic work stealing for a few operations.
The static part: wave order and placement.
The host builds named waves for each layer (
qkv
,
router
,
attn
,
moe_up_drain
,
oproj
,
rmsnorm
, …), chooses an order, flattens them into one task list, and deals task
k
to SM
k mod 132
. The current order puts the router and route setup ahead of attention:
qkv → router → top-k → route setup → MoE gather → attention → MoE up/down → O-proj → RMSNorm
That ordering gives the MoE branch a head start, so it can schedule the computationally non-intensive routing with the heavier QKV GEMM to better utilize SMs. Beyond that simple picture, the effect of a schedule is hard to isolate. Changing one wave changes when its dependents become ready, which tasks share an SM, and how HBM bandwidth is allocated between tasks. Those choices interact across the whole layer.
Our experiments show that schedule matters. We ran two 8K input length, uniform-routing ablations that change only wave order.
Interleaved.
After attention begins, MoE up/down runs before attention combine. The rationale is to keep ready work from both branches available, so SMs spend less time waiting:
qkv → router → top-k → route setup → MoE gather
→ attention → MoE up/down → attention combine → MoE combine → O-proj → RMSNorm
Attention first.
Launch attention combine and O-proj before any MoE GEMM, while still allowing router to start early
qkv → router → top-k → route setup → MoE gather
→ attention → attention combine → O-proj → MoE up/down → MoE combine → RMSNorm
BS
Tuned Order (TOK/S)
Interleaved
Loss
Attention First
Loss
1
291
282
3%
236
19%
2
423
406
4%
364
14%
4
553
531
4%
509
8%
8
687
677
1%
642
7%
All of these schedules produce correct outputs. We also tried dependency-affinity placement: put a task on the same SM as a producer it depends on, hoping to reuse cache and reduce cross-SM handoffs. It slowed the kernel by 1–2%, so the released version uses naive round-robin placement. The table shows measured effects; a complete causal model for why one ordering or placement wins remains open.
The dynamic part: local work stealing for variable-sized work.
Full attention reads vastly different lengths of KV for each live request, and the router decides how many tokens each MoE expert receives. Those tile counts only become known during the step.
The split is deliberate. The static schedule fixes most of the task order and placement, giving us the control needed to tune performance — as the wave-order ablation above shows. Local work stealing handles only the load imbalance that the host cannot know ahead of time. The static task list reserves a fixed number of small
claimer
tasks; an
ATTN_DRAIN
or
MOE_*_DRAIN
claimer atomically steals the next item from its stage's shared queue and executes it until the queue is empty. Attention claimers steal attention tiles, and MoE claimers steal MoE tiles. The number of claimers controls parallelism, while the current attention queue reflects the live requests in the batch. This keeps the static schedule stable and balances the variable work without rebuilding the whole list on every batch change.
The following task graph below puts the static waves, fine-grained dependencies, and locally claimed stages in one view:
Image 7: One MoE decode layer as the kernel sees it. Attention is drawn as four KV-head because O-proj's split-K equals the KV head count, so each O-proj split depends on exactly one head's attention output — a ready head can enter O-proj while another head is still in QKV. Dashed cards are the locally claimed stages described above.
Other schedulers we tried
Early in the project, while targeting a dense model, we built several more sophisticated schedulers. One was a greedy, topology-aware scheduler that estimated each task's cost from its memory reads. We also tried a brute-force search that selected the best schedule from hundreds of random candidates. Both delivered about 10% more throughput than plain round-robin on that workload. MoE changed the problem: routing makes the amount and placement of its work dynamic, so those dense-model schedules did not transfer cleanly. We ultimately settled on the simpler round-robin with a tuned wave order, plus the local work stealing described above. Nevertheless, we plan to revisit those more complicated schedulers should the simple round-robin proven insufficient for megakernels running on Blackwell GPUs or narrower quantization types such as NVFP4 or FP8.
The serving engine around the kernel
The server has two long-lived host-side threads. A Python thread serves as the control plane: it accepts requests, runs prefill, and manages KV capacity and batches. A native C++ thread owns decode for maximum performance. These two threads operate in an interleaved manner: Python pauses C++ to prefill or change active batch size.
This handoff exists because the megakernel runs a task list built ahead of time: tile counts, barrier indices, and which slot a tile belongs to are already baked in. Python therefore parks decode before it admits, retires, or reshapes a batch, then C++ resumes with a schedule that matches the new batch size and context. The figure shows the state each side owns and how the schedule changes:
Image 8: At the start of a step, the C++ loop clears every scratch buffer and barrier counter the megakernel will use. It then takes the longest live request's context to choose a prebuilt schedule for the current batch size. That schedule fixes the GEMM tiles and other static work; neighboring context buckets reuse a schedule when their static task descriptor buffer is identical. Full-attention is the exception: C++ computes a per-request split count from the live lengths, uploads it, and the GPU reads it while draining the attention queue.
Python and C++ take turns
C++ owns the continuous decode loop: it updates KV positions, clears per-step state, selects the schedule, launches the megakernel, samples, and streams the resulting token. It repeats that loop while there are active requests. Python owns everything that changes the batch: accepting a request, running its prefill, assigning or evicting a slot, and switching to a smaller batch size.
The
park / resume
arrow is the handoff between those two owners:
# Python control plane
while
server_is_running:
request = wait_for_new_request()
decode_service.request_pause()
# C++ finishes its current decode step.
decode_service.wait_until_parked()
# GPU is now idle; C++ will not read batch state.
prefill(request)
# Ordinary prefill kernels populate its KV pages.
decode_service.admit_or_evict(request)
decode_service.switch_batch_size_if_needed()
decode_service.resume()
# C++ snapshots the new state and keeps decoding.
// C++ decode service
while
(!stop) {
if
(pause_requested || active_requests == 0) {
signal_parked();                  // Python may now mutate the batch.
wait_for_resume_or_admission();
continue
;
}
update_kv_page_tables();
clear_scratch_and_barriers();
select_schedule(max_live_context());
launch_megakernel();
sample_and_stream_tokens();
retire_finished_requests();
}
Parking is the ownership boundary for mutable batch state. Python changes per-request metadata, token buffers, KV page tables, and possibly the pointers for a new batch size while C++ waits. C++ snapshots that state only after resume, then owns it for the next decode step. This keeps the megakernel from observing a half-updated batch. The current trade-off is simple: prefill pauses decode, so the engine does not mix prefill and decode on the GPU yet. When no requests are active, C++ parks on its own and Python wakes it after an admission.
From the outside this is an OpenAI-compatible server with streaming, prefix caching, and tool calls.
Known limitations
These are limits of the current implementation, not of the design. We plan to fill them in.
No mixed prefill and decode.
A prefill pauses all decoding requests. For a workload of many very short requests, this hurts performance a bit.
Maximum batch size is 8.
This is a configuration limit, not an architectural limitation of the megakernel. The server
could
support larger batch sizes if needed but we haven't tuned the performance for larger batch sizes yet.
MK is decode only.
Prefill runs as ordinary PyTorch kernels.
Performance
Decode throughput
Setup.
All numbers are on a single H100 (132 SMs) running North Mini Code. The baseline is vLLM v0.24 with the FA3 attention backend and the Triton MoE backend, prefill disabled. Both engines decode against a synthetic KV cache so that the comparison isolates decode compute from prefill. We measure the decode throughput over 1K output tokens.
We report two benchmark settings, and the difference between them is quite informative.
Real checkpoint.
Both engines use the real North Mini Code weights, so the MoE expert distribution is the model's genuine, correlated routing.
Uniform routing.
vLLM runs with simulated uniform-random routing; the megakernel runs with random weights, which produces an approximately uniform expert distribution.
At 8K context, normalized to vLLM at each batch size:
Image 9: We compare megakernel vs vLLM decode throughput at 8K context. Megakernel gains more speedup under real expert distribution.
First, for uniform routing, the speedup is largest when there is most pipeline bubbles. At batch size 1, there is least work per request. As such a large fraction of GPU time is spent on pipeline bubbles and between kernel boundaries. As batch size grows, the fraction of pipeline bubbles to total time decreases, shrinking the gap.
Second, the speedup depends on the expert distribution. At batch size 8 the megakernel is 1.32× faster with the real expert distribution and 1.14× faster under uniform routing. Real requests often choose the same experts, leaving the active-expert set sparse. The MoE then does less total work, so pipeline bubbles make up a larger share of the step; those are the gaps where the megakernel can eliminate. Uniform routing spreads tokens across many experts, leaving more MoE work and fewer bubbles to recover. Synthetic uniform routing therefore understates megakernel speedup on real traffic, and we report it here as the harder case.
The advantage also holds across context lengths. We show BS=4 and BS=8 below.
Image 10: Megakernel’s speedup holds across different batch sizes and context length.
End-to-end serving
The microbenchmark isolates decode. This test runs the full server at batch size 8: real prompts enter through the API, prefill runs, requests finish at different times, and the server continually filling the batch. Each engine generates a slightly different number of tokens, so total wall time alone is not a fair comparison. We report both wall time and average decode throughput.
The end-to-end gain is 1.25× - 1.41× in average decode throughput, smaller than decode-only for two reasons: prefill still uses ordinary PyTorch kernels and pauses decoding, expert routing changes from batch to batch, and the active batch size varies during serving so the megakernel's speedup is not constant.
Benchmark
Engine
Total time (s)
Generated tokens
Avg decode throughput (tok/s)
Speedup
AIME 2025
MK
335
313,205
935
1.41×
vLLM
495
327,296
661
GPQA
MK
3,837
3,021,691
787
1.25×
vLLM
4,386
2,768,267
631
MMLU-Pro (CS subset)
MK
1,302
1,235,345
948
1.33×
vLLM
1,756
1,252,448
713
SciCode
MK
8,712
6,193,859
711
1.37×
vLLM
11,006
6,166,407
560
LiveCodeBench v6
MK
6,141
4,933,421
803
1.28×
vLLM
5,428
3,394,164
625
Accuracy
We also checked that the serving path preserves model quality. The table compares the megakernel server with the vLLM baseline on the following benchmarks:
Benchmark
MK
vLLM
SciCode
38.9% ± 1.6%
38.2%
LiveCodeBench v6
70.3% ± 1.1%
70.3%
We report the mean score and standard deviation over 7 runs. Our megakernel produced close score compared to the vLLM counterpart, confirming our kernel is accurate.
What we learned
Megakernel starts simple.
We did not need a compiler or a new programming model. Ordinary GEMM and attention kernels already do the hard math; wrapping them in one shared calling convention — the same warp roles, task format, and barrier protocol — is enough to assemble a megakernel by hand, one operation at a time.
Megakernel gains more speedup on MoE models under real traffic.
Real requests often hit the same experts, so MoE work is sparse and leaves more idle time for the megakernel to fill with other ready work.
Megakernel integrates nicely into a server.
Continuous batching and paged attention all work nicely with the megakernel. Decode stays on the GPU as one persistent kernel with a C++ host loop with a separate Python thread controlling the engine.
After the kernels are fast, the schedule is the rest of the speedup.
Which SM runs which tile, and in what order, is the other performance knob beyond kernel tweaks.
Next steps
The first question is how far this design extends beyond decode. Prefill has a very different shape, and mixed prefill/decode batches would require the scheduler to keep both workloads moving without interrupting latency-sensitive decoding.
We are also building a megakernel for RTX Blackwell (e.g. RTX Pro 6000 and RTX 50-series), with FP8 and FP4 quantization on the roadmap. This is a useful test of how much of the ABI and scheduling design survives a different GPU architecture and lower-precision kernels. We plan to release an RTX megakernel soon.
After that, we want to bring the same approach to datacenter Blackwell and multi-GPU inference. Tensor and expert parallelism introduce cross-device collectives, which add a new synchronization boundary and, potentially, more pipeline bubbles to be recovered by the megakernel.
Getting Started
Learn more about
North Mini Code
— Cohere’s first agentic coding model — and explore the code behind megakernels on
GitHub
.
Acknowledgements
We would like to thank Bharat Venkitesh for providing technical support throughout this work. We thank Stephen Jones, Brian Pharris, Vinod Grover, Frederic Bastien, Hua Huang and Disha Mehra from Nvidia for various insightful discussions. We thank Zewen Shen for some helpful discussions on evaluation and numerical accuracy. The design builds on ideas from Hazy Research's
Look Ma, No Bubbles!
and uses
ThunderKittens
tile primitives. Thanks also to the authors and maintainers of FlashAttention, PyTorch, Transformers, and vLLM.
Blog
Written By
Xiaochun Tong
Intern of Technical Staff, Foundations
Conway Zhu
Member of Technical Staff, Foundations
Donglu Wang
Member of Technical Staff, Foundations
Tags
AI for Developers
Research
Share
AI isn’t a shortcut.
It’s how business gets ahead.
Contact sales
