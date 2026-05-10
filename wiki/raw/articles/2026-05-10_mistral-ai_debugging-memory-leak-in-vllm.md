---
title: "Heaps do lie: debugging a memory leak in vLLM."
source: "Mistral AI Blog"
url: "https://mistral.ai/news/debugging-memory-leak-in-vllm"
scraped: "2026-05-10T01:21:01.488803+00:00"
lastmod: "2026-04-23T09:54:51.288Z"
type: "sitemap"
---

# Heaps do lie: debugging a memory leak in vLLM.

**Source**: [https://mistral.ai/news/debugging-memory-leak-in-vllm](https://mistral.ai/news/debugging-memory-leak-in-vllm)

Heaps do lie: debugging a memory leak in vLLM.
Engineering
Jan 21, 2026
By Mathis Felardos
A few months ago, our team investigated a suspected memory leak in vLLM. At first, we thought the issue would be easy to spot, something confined to the upper layers of the codebase. But the deeper we looked, the more complex it became. This article kicks off our new Engineering Deep Dive series, where we’ll share how we tackle technical investigations and build solutions at Mistral AI.
The issue first appeared during pre-production testing of disaggregated serving with one of our
frontier models
. Memory usage was climbing steadily, but only under specific conditions: with vLLM, with our
model Mistral Medium 3.1
, and graph compilation enabled. There were no crashes or errors, just a slow linear increase in system memory of 400 MB per minute on production-like traffic.  After a few hours, that would lead to an "out of memory" state.
What followed was a methodical hunt, starting from high-level Python tools and descending into kernel-level tracing, until we finally uncovered the true source. Here’s how we tracked it down, and what it revealed about the hidden risks of dependencies layers in today’s software.
Not the kind of trending upwards graph we like to see on Grafana
A leak that played hide and seek
.
Initially, our approach followed a standard troubleshooting path: we aimed to isolate the source of the leak by replicating the issue on a smaller model, with fewer production optimizations activated. But after trying different settings and models we couldn’t reproduce that on another setup. The error was only present on a Prefill/Decode disaggregated setup with NIXL.
Given the central role Prefill/Decode (P/D) disaggregation plays in our story, let us walk you through the high-level mechanisms of how this inference setup works. P/D Disaggregated splits the processing of a query into two phases, processed by different instances:
First the router sends a “prefill request” (by setting
max_tokens=1
and by setting an empty set of KV Transfer metadata) to a prefill vLLM instance to compute the KVCache of the request.
On completion, the router transfers KVCache metadata alongside a “decode request” to a decode vLLM instance.
KVCache transfer is initiated through NIXL and token generation happens on the decode vLLM instance by using and extending the transferred KVCache.
The leak was only observed on the decode side of this disaggregated setup, strongly suggesting that KV Cache transfer through NIXL was the root cause of the leak. In our setup
NIXL
relies on
UCX
(Unified Communication X), a high-performance communication library designed for data exchange in distributed systems. UCX enables optimized data transfer over a large set of technologies, including
Infiniband
, a low-latency, high-throughput interconnect technology commonly used in HPC and data centers.
Overview of a P/D Disaggregated serving deployment.
For the remainder of our investigation, we worked in this setup and started with Python memory profiling tools to pinpoint the source of the leak.
We tried Memray and Guppy 3, but neither showed a leak and everything they allowed us to observe was normal. Attempting to use GDB made the entire process crash. Our vLLM setup was also too heavy for tools like Valgrind, making it impractically slow or even impossible to use.
It was clear that a more powerful tool was required to track the leak. But before investing more time, we decided to be sure that this leak was reproducible by others. We reached out to the vLLM team by opening an
issue on their GitHub repository
, which helped confirm we weren't the only ones seeing this issue and a deeper investigation was warranted.
Counting mallocs and frees with Heaptrack.
In order to better track what was happening, we turned to
Heaptrack
: a memory profiler that overrides memory operations like
malloc
or
free
and records these events alongside stack traces.
Millian Wolf, the creator of Heaptrack, has written an excellent introductory
blog post
to get you started with the tool. It’s a two-step process: first run the program with tracing, then interpret the data dumps.
In order to track the allocations confined in the worker process of vLLM, we set
LD_PRELOAD
to
libheaptrack_preload.so
through vLLM to ensure this library is loaded before any other and overrides the behaviours of memory allocating functions, providing us with the data dump.
We were then able to visualize this data through
heaptrack_interpret
:
$ git
clone
https://github.com/KDE/heaptrack.git
$
cd
heaptrack && mkdir build &&
cd
build && cmake .. && sudo make install
# Setting LD_PRELOAD=/path/to/libheaptrack_preload.so creates a temporary file named heaptrack.<pid>, here the pid is 2028233
$ /usr/
local
/lib/heaptrack/libexec/heaptrack_interpret < heaptrack.2028233 | gzip > heaptrack.vllm.2028233.gz
Heaptrack provides a detailed, interactive graph of all heap allocations, down to the function level. We can track every
malloc
and
free
, with a clear breakdown of the memory usage.
The memory usage shown with Heaptrack of our vLLM worker
At this point, one might question: where is the memory leak? Indeed, the only visible memory increase was due to a lazy NIXL initialization.
To validate that the leak was indeed happening in this set-up, we ran a vLLM benchmark and created two Heaptrack snapshots using
heaptrack_interpret
: one at the beginning and one near the end. Although the heap memory itself remained stable, the
peak resident memory (RSS)
, which we will cover in the next section, differed between the two snapshots. This discrepancy was visible in Heaptrack’s summary tab.
Peak RSS discrepancy in Heaptrack: Before (1) and after (2) benchmark
This meant the leak was happening outside the heap, and so not part of the memory that Heaptrack analyzes. We needed to change tools to track allocations outside of the heap.
Beyond the heap: understanding resident memory and system allocations.
To understand why Heaptrack couldn’t detect the leak, we first need to clarify what the
Resident Set Size (RSS)
actually includes. RSS represents the portion of a process’s memory held in RAM, and it contains more than just the heap. Specifically, it includes:
The heap
is traditionally managed using the legacy
sbrk
and
brk
system calls, which adjust or set the program’s break address, the pointer marking the end of the heap segment.
The stack
, which stores local variables and function call frames.
Anonymous memory mappings
, which are regions of memory allocated directly via the
mmap
system call without a file backing. These are often used by custom allocators or by
malloc
for larger blocks of memory. The addresses of anonymous mappings usually reside
between the heap address space and the stack address space
, in a region known as the
memory mapping segment
.
While
malloc
can use
sbrk
for small allocations, modern implementations typically prefer using
mmap
with anonymous mappings since it’s more flexible and lets you allocate huge pages (memory pages of 2MB or 1GB depending on your setup).
Heaptrack only hooks into glibc's
malloc
and
free
functions. This means it can track all traditional heap and anonymous mapping allocated by
malloc
directly, but it misses memory allocated through direct
mmap
calls or other system-level mechanisms outside of glibc's control.
Fortunately, all isn’t lost when it comes to tracking what was happening. The
/proc
filesystem is a special folder in Linux that serves as a
kernel API
, exposing a virtual interface to interact with running processes, and provides real-time access to process details, such as:
/proc/<pid>/fd
, which lists all open file descriptors for a process.
/proc/<pid>/maps
, which shows a detailed map of the process’s memory regions, including heap, stack, shared libraries, and anonymous mappings.
And many more (a simple
ls
in
/proc/<pid>/
lists what is available).
To continue our investigation, we used the
pmap
command, which reads
/proc/<pid>/maps
and presents memory usage in a human-readable format. Our goal was to track changes in memory regions over time, so we ran:
$ watch -n 1
"pmap -X
$pid
| (head -n 2 && tail -n +3 | sort -k7 -nr)"
This command runs
pmap
every second to display extended memory information for a specified PID, skips the header, and sorts the output by memory size, allowing us to focus on the largest memory regions.
With this command, we observed an interesting pattern: only some anonymous memory mappings were growing over time, and their start addresses were changing. The size of these allocations became huge over time while most others were simply not moving.
The memory pages listed by our
pmap
command, sorted by RSS size, made it easy to spot suspicious allocations. The orange dot highlights an example.
This behavior is characteristic of
mremap
, a system call used to
resize or relocate existing memory regions
without freeing them. Unlike
realloc
, which operates within the heap and relies on glibc's memory management,
mremap
works at a lower level and is often used by custom allocators, libraries, or even manual memory management code to dynamically adjust memory layouts.
This pattern could also result from repeated cycles of
munmap
followed by
mmap
, where memory is freed and reallocated but the total usage continues to grow, either due to
fragmentation, leaks in custom allocators, or improper resizing logic.
In our case, the changing addresses and growing size strongly suggested that memory was being reallocated but never properly released.
This was our first concrete indication that the leak wasn’t in the heap but in anonymous
memory regions being resized without proper release.
Tracing the leak with BPFtrace.
Our investigation had narrowed the leak down to raw
mmap
or
mremap
calls, but we needed to confirm which one was responsible. Our first attempt was to use
LD_PRELOAD
with a
custom small C library
that logged every
mmap
and
mremap
call, since Heaptrack wasn’t doing it, hoping to intercept the ones we cared about. However, this approach had limitations:
not all
mmap/mremap
go through glibc
. Our custom hooks saw some allocations but they didn't match the addresses leaking in our
pmap
output. The leaking regions were still growing, untracked by our
LD_PRELOAD
hook. This suggested that those allocations were made by manually doing a syscall or that another hooking mechanism was in place.
To get a full picture, we turned to
BPFtrace
, a tool for real-time tracing of system calls and kernel events. It relies on the Linux kernel’s
eBPF virtual machine
, which executes lightweight, pre-validated bytecode attached to tracepoints or probes, enabling safe and low-overhead analysis. BPFtrace is also used by some Kubernetes tools to detect anomalous or dangerous behaviors in clusters, such as unauthorized access or resource abuse, all without risking kernel stability.
We also considered using
strace
, but its reliance on
PTRACE
made it too slow to effectively analyze the issue at this stage. Instead, we wrote a BPFtrace script to log
every
mmap
and
mremap
call
with their arguments and stack traces, including calls that don't go through glibc. Here’s is the script we wrote with
Le Chat
’s help:
tracepoint:syscalls:sys_enter_mmap /pid == (uint64)
$1
/ {
printf
(
"Stack trace:\n%s\n"
, ustack(perf));
printf
(
"PID/TID: %d %d | "
, pid, tid);
printf
(
"ENTER mmap(addr=%p, len=%d, prot=%d, flags=%d, fd=%d, off=%d)\n"
,
args->addr, args->len, args->prot, args->flags, args->fd, args->off);
}
tracepoint:syscalls:sys_exit_mmap /pid == (uint64)
$1
/ {
printf
(
"PID/TID: %d %d | "
, pid, tid);
printf
(
"EXIT mmap: ret=%p\n"
, args->ret);
}
tracepoint:syscalls:sys_enter_munmap /pid == (uint64)
$1
/ {
printf
(
"PID/TID: %d %d | "
, pid, tid);
printf
(
"ENTER munmap(addr=%p, len=%d)\n"
, args->addr, args->len);
}
tracepoint:syscalls:sys_exit_munmap /pid == (uint64)
$1
/ {
printf
(
"PID/TID: %d %d | "
, pid, tid);
printf
(
"EXIT munmap: ret=%d\n"
, args->ret);
}
tracepoint:syscalls:sys_enter_mremap /pid == (uint64)
$1
/ {
printf
(
"PID/TID: %d %d | mremap"
, pid, tid);
printf
(
"old_addr=%p, old_len=%d, new_len=%d, flags=%d, new_addr=%p)\n"
,
args->addr, args->old_len, args->new_len, args->flags, args->new_addr);
}
tracepoint:syscalls:sys_exit_mremap /pid == (uint64)
$1
/ {
printf
(
"PID/TID: %d %d | "
, pid, tid);
printf
(
"EXIT mremap: ret=%p\n"
, args->ret);
}
We ran the script as root with this command by replacing
$pid
with the PID of the vLLM worker process that was leaking according to
pmap
:
bpftrace /host/script_bpftrace.txt $pid > out_$pid.txt
Basically, this script:
Traces
mmap
,
munmap
and
mremap
system calls as they enter the kernel.
Prints the thread ID, call type, requested address, and length.
Prints the
user-space stack trace (
ustack
in BPFtrace)
to identify where the call originated.
Here is an example output of this script:
Stack trace:
7ffff7d6b88d syscall+29 (/usr/lib/x86_64-linux-gnu/libc.so.6)
PID/TID: 441359 441359 | ENTER mmap(addr=(nil), len=151552, prot=3, flags=34, fd=-1, off=0)
PID/TID: 441359 441359 | EXIT mmap: ret=0x7fd8a78ee000
Snippet of the output of the BPFtrace script. The
syscall+29
is important.
At this stage, let’s synthesize the information we’ve collected:
pmap
showed us the suspiciously-growing allocations and their base addresses.
BPFtrace allowed us to understand that these addresses were obtained with
mmap
calls, not
mremap
. This was surprising to us, as
mremap
sounded like the ideal suspect for a memory allocation that kept on growing.
Even more intriguing, the calls originated from
syscall+29
aka
glibc's raw syscall wrapper
, that lets users perform a raw syscall through an API like:
syscall(SYS_mmap, ...)
This represented significant progress, but further investigation was required. While BPFtrace showed us the user stack trace of the system call itself (
ustack
in their documentation), it only gave us the first element of the user call stack, not the full user-space context leading to the allocation. We could see where the
mmap
was called, but not the previous callers. That information would have been essential to us, so we tried to understand why we could not get it, and initially thought it was linked to
frame pointers being disabled
in our setup, and decided to investigate in that direction.
For context, frame pointer is a feature that stores the return address of function calls in a register or memory location, enabling tools to reconstruct the full call stack. Frame pointers were historically disabled as an optimization for most libraries, as they added minor overhead, but modern distributions have begun re-enabling them since the performance gains are now negligible compared to the debugging benefits.
Sadly, switching from Ubuntu 22.04 LTS to Ubuntu 24.04 LTS (which has frame pointers enabled for native libraries) wasn’t enough. This suggested that an already optimized Python dependency, that disabled frame pointers, was the culprit.
We pondered the situation for a while: which Python package could be doing such direct syscalls, by-passing the usual standard library calls? At this stage, we had two potential culprits:
UCX (Unified Communication X)
, a high-performance communication library used for accelerated networking and RDMA (Remote Direct Memory Access). UCX is a dependency of NIXL, which vLLM uses for disaggregated serving. UCX is known for its low-level memory optimizations, including custom memory allocators.
PyTorch
, which performs its own memory management and optimizations, often bypassing standard allocators for performance. PyTorch’s custom allocations and JIT compilation could also be responsible for the leak.
With both suspects on the table, we needed a way to dig deeper. At this stage we turned to GDB automation instead.
GDB automation to the rescue.
Using GDB earlier in the investigation wasn’t feasible for a simple reason: GDB attaches to an entire process. With vLLM, attaching GDB to the main process would halt all workers, making it impossible to observe the leak in real time. Since the leak didn’t cause a crash, and memory dumps were impractical due to the sheer size of the process. We were stuck.
However, from our BPFtrace logs, we noticed that every leaking
mmap
call originated from the same address. Like we said in the previous section, this address didn’t point to
mmap
directly, but it was inside glibc’s the
syscall
thin-wrapper. This function bypasses glibc’s usual
mmap
wrapper, which explains why our
LD_PRELOAD
hooks missed it earlier. We tried to use
LD_PRELOAD
to intercept the glibc’s
syscall
, but strangely it wasn’t working either… leaving us with almost no way to trace these calls dynamically.
Since the leaking calls always came from the same
syscall
instruction, we could automate GDB to break only when that specific address was hit. Here’s how we did it:
We set a
conditional breakpoint
on the
syscall
address, triggering only if the system call number matched
SYS_mmap
.
We temporarily broke at the exit of the
mmap
system call to inspect the return value, which is the allocated address, and printed the full stack trace.
We dumped all available context in one go: the return address, the call stack, and any other relevant registers or memory.
We ran this conditional script
for a few seconds during the benchmark
and compared the captured return addresses with our
pmap
monitoring to confirm whether they matched the known leaking regions.
Here is the script, which can be run through
gdb -x gdb_script.txt
:
# Attach to the process
attach 2199304
# Open a log file for output
set
logging file syscall_output.txt
set
logging on
# Set a conditional breakpoint on syscall for rdi == 9 (mmap)
break
syscall
if
$rdi
== 9
# Commands for the syscall breakpoint
commands
silent
# Set a temporary breakpoint at the return point
tbreak *0x00007ffff7d9525d
# Commands for the temporary breakpoint
commands
$bpnum
+ 1
silent
set
$ret_val
=
$rax
bt
printf
"Syscall returned: rax = 0x%012lx\n"
,
$ret_val
continue
end
continue
end
# Run the process
continue
This approach gave us two major benefits:
We captured the full user-space stack trace at the moment of allocation, something BPFtrace couldn’t reliably provide.
We could also cross-reference the returned addresses with our
pmap
output to confirm whether they matched the leaking regions.
In short, we turned GDB into a targeted, non-intrusive observer, breaking only when the leak occurred, printing everything we needed, and letting the process continue. This finally allowed us to connect the dots between the
mmap
calls and the growing anonymous regions we’d seen in
pmap
.
The first stack trace showed Python (line
#5
) invoking
mmap
through UCX (line
#4
), which was unexpected since Python, in normal circumstances, should call the glibc’s
mmap
directly.
#0  syscall () at ../sysdeps/unix/sysv/linux/x86_64/syscall.S:29
#1  0x00007ffc61759ac2 in ucm_orig_mmap_syscall () from /.venv/lib/python3.12/site-packages/.nixl.mesonpy.libs/plugins/../../nixl.libs/libucm-e091ff91.so.0.0.0
#2  0x00007ffc61753bd1 in ?? () from /.venv/lib/python3.12/site-packages/.nixl.mesonpy.libs/plugins/../../nixl.libs/libucm-e091ff91.so.0.0.0
#3  0x00007ffc61753e3b in ucm_event_dispatch () from /.venv/lib/python3.12/site-packages/.nixl.mesonpy.libs/plugins/../../nixl.libs/libucm-e091ff91.so.0.0.0
#4  0x00007ffc61754009 in ucm_mmap () from /.venv/lib/python3.12/site-packages/.nixl.mesonpy.libs/plugins/../../nixl.libs/libucm-e091ff91.so.0.0.0
#5  0x0000000000674ac0 in _PyMem_ArenaAlloc (_unused_ctx=<optimized out>, size=<optimized out>) at ../Objects/obmalloc.c:138
...
Even more confusing was the second stack trace, where Python (line
#8
) was calling
munmap
through UCX (line
#7
), yet somehow triggering an
mmap
allocation (line
#1
) in the process:
#0  syscall () at ../sysdeps/unix/sysv/linux/x86_64/syscall.S:38
#1  0x00007ffc60f58ac2 in ucm_orig_mmap_syscall () from /.venv/lib/python3.12/site-packages/.nixl.mesonpy.libs/plugins/../../nixl.libs/libucm-e091ff91.so.0.0.0
#2  0x00007ffc60fae47c in ?? () from /.venv/lib/python3.12/site-packages/.nixl.mesonpy.libs/plugins/../../nixl.libs/libucs-311e600f.so.0.0.0
#3  0x00007ffc60f9b9c4 in ucs_mpool_grow () from /.venv/lib/python3.12/site-packages/.nixl.mesonpy.libs/plugins/../../nixl.libs/libucs-311e600f.so.0.0.0
#4  0x00007ffc60f9bbf5 in ucs_mpool_get_grow () from /.venv/lib/python3.12/site-packages/.nixl.mesonpy.libs/plugins/../../nixl.libs/libucs-311e600f.so.0.0.0
#5  0x00007ffc60fafe2c in ?? () from /.venv/lib/python3.12/site-packages/.nixl.mesonpy.libs/plugins/../../nixl.libs/libucs-311e600f.so.0.0.0
#6  0x00007ffc60f52e3b in ucm_event_dispatch () from /.venv/lib/python3.12/site-packages/.nixl.mesonpy.libs/plugins/../../nixl.libs/libucm-e091ff91.so.0.0.0
#7  0x00007ffc60f5313b in ucm_munmap () from /.venv/lib/python3.12/site-packages/.nixl.mesonpy.libs/plugins/../../nixl.libs/libucm-e091ff91.so.0.0.0
#8  0x0000000000607d15 in _PyThreadState_PopFrame (tstate=0xba6ac8 <_PyRuntime+459656>, frame=<optimized out>) at ../Python/pystate.c:2992
...
This was unexpected, as
munmap
is intended to free memory, not allocate it. Seeing an
mmap
call during a
munmap
operation within UCM (the memory management module of UCX) suggested something was going wrong in UCX's memory pool management.
Identifying the role of UCX’s memory hooks.
We shared these findings with the vLLM team, who helped validate and refine our understanding of the issue. Together, we discovered that UCX uses a
mmap hooking mechanism
to optimize memory operations for InfiniBand, including pre-caching data for transfers (a feature called Registration Cache, or RCache). Memory management for InfiniBand is often expensive due to the need for hardware-level memory registration.
However, this mechanism intercepts
all
mmap
calls by default
, not just those related to UCX or InfiniBand operations. This broad interception explains why our earlier attempts to trace allocations using our
LD_PRELOAD
based
mmap
hook failed: UCX
dynamically patches
the
Global Offset Table (GOT) entries
used by applications to call functions like
mmap
and
munmap
. That's why it was bypassing our earlier hooks entirely. We also found that this hooking mechanism
is automatically disabled
when Valgrind is detected, which would have prevented us from using Valgrind for deeper analysis.
The GOT is a data structure used by the dynamic linker to resolve function calls in dynamically linked libraries. When a program starts, the dynamic linker populates the GOT with the actual addresses of functions, such as
mmap
, from shared libraries.
Modifying the GOT at runtime is generally considered bad practice because it can introduce instability, make debugging harder, and break assumptions other parts of the program or libraries rely on. But UCX does this for a good reason. Indeed, UCX does this to manage its Registration Cache, which tracks "registered" (or "pinned") memory. This is memory that has been pinned in place, ensuring its virtual-to-physical address mapping remains fixed. This allows network adapters to transfer data directly between the network fabric and RAM without CPU involvement, which is critical for performance but requires careful handling, as registered memory is a limited resource.
Solving the issue.
Now that we knew that the
mmap
hooking mechanism was in play, we realized that it was actually good news since we could disable it entirely by setting this environment variable
UCX_MEM_MMAP_HOOK_MODE=none
. It successfully disabled this behavior,
which resolved the memory leak without impacting performance.
The
mmap
hooks are useful when sending various memory chunks over RDMA, but in vLLM use case, we only need to handle
one large, contiguous memory region
: the entire vLLM KVCache Manager memory. NIXL only needed to register the memory once for its transfers. Therefore, in the vLLM use case, disabling the hooking mechanism was safe and had no negative impact on disaggregated serving performance.
After discussing this with the UCX team, we learned that UCX does not immediately free memory when
munmap
is called. Instead, it moves the region to an invalidation queue for later cleanup. This queue is managed by UCX’s memory pool, which dynamically expands to accommodate more entries as needed. As a result, memory regions accumulated without being released, and the growing queue required additional allocations, explaining why
mmap
was called during
munmap
operations. As an alternative solution to the memory leak setting the environment variable
UCX_RCACHE_MAX_UNRELEASED=1024
(the default value is
inf
) limits the number of unreleased memory regions in the queue, forcing UCX to initiate cleanup once the threshold is reached.
The thing is, this should not have happened in the first place. NIXL and vLLM were indeed
calling
the
ucp_worker_progress()
function that should have triggered the memory pool cleanup. Why it was not triggered in this specific edge case is still not clear. But it showed that setting a default value of
UCX_RCACHE_MAX_UNRELEASED
to infinity was not correct. The UCX and NIXL team decided to change this behavior
for a future NIXL release
. In the meantime, we merged a
fix
in the vLLM repository to help the community avoid running into the same leak.
A summary of the investigation.
The investigation in brief:
We noticed a
rapidly-growing memory leak in our production setting
when deploying one of our frontier models with disaggregated serving.
We attempted to trim down the environment and get a minimal reproducer. Unfortunately,
the bug only reproduced on a complex setup, with a large model, and disaggregation enabled.
We turned into Memray, Guppy 3, and Heaptrack to analyze the leak.
Nothing obvious came of these tools.
However, we noticed something peculiar in Heaptrack’s metrics.
The resident memory was unusually large
, so we decided to dig in that direction.
Leveraging
pmap
, we were able to see
RSS allocations that kept on growing, with their associated base pointers.
We wanted to get more clues about who was doing those calls. With a bit of scripting and the use of BPFtrace,
we found that the leaks originated from
mmap
calls.
Even with our best efforts, we were not able to collect full stack traces (that would have allowed us to pin-point the culprit call site), but
that led us to believe that the syscalls were made by a heavily optimized package.
Thanks to the gathered information, we were able to
set up very specific GDB breakpoints that would only be triggered by the offending calls.
We found that
UCX was performing those calls.
While the purpose of the calls is legitimate: improve performance for InfiniBand transfers, it created ever-growing allocations in the RSS and
prevented us from deploying disaggregated serving for days.
Knowing the source of the leak, the work-around was easy to find:
setting
UCX_MEM_MMAP_HOOK_MODE=none
fixed our issue.
We discussed that
investigation in the vLLM repository
and merged
a patch for the community
.
What we learned.
Modern software stacks are built on top of layers of dependencies, each adding complexity and potential points of failure. While these abstractions greatly enhance programmers’ productivity, it doesn’t fully insulate them from underlying issues in the stack. That’s why it’s essential to be prepared to dig deep when debugging. However, doing so in these environments is rarely straightforward, especially when performance optimizations introduce subtle edge cases. UCX is a great example of this. Its design prioritizes performance, but the way it intercepts
mmap
calls can create hard-to-trace risks. This experience demonstrated once more how challenging it can be to diagnose issues in deeply interconnected systems.
This investigation also shows the importance of transparency and collaboration when navigating performance-critical dependencies. We’re grateful for the collaboration with the
vLLM
,
NIXL
and
UCX
teams in confirming and addressing this behavior. Their expertise was critical in reaching a resolution, and we look forward to continuing our work together.
We extend our gratitude to the following individuals for their assistance and collaboration in resolving this issue:
Robert Shaw
(Red Hat, vLLM and llm-d Maintainer)
Will Eaton
(Red Hat, vLLM and llm-d Maintainer)
Nicolò Lucchesi
(Red Hat, vLLM and llm-d Maintainer)
Mikhail Brinskii
(NVIDIA, NIXL Maintainer)
Leonid Genkin
(NVIDIA, UCX Maintainer)
Nathan Bellalou
(NVIDIA, UCX and NIXL Maintainer)
We Are Hiring
Interested in tackling challenges like these? Join us at
Mistral AI
and help shape the future of AI infrastructure. We’re always looking for talented engineers and researchers to collaborate on cutting-edge projects.
Share this article
More from Mistral AI
News
Models
AI Services
