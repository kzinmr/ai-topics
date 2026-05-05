---
title: "Beyond OpenMP in C++ & Rust: Taskflow, Rayon, Fork Union 🍴"
url: "https://ashvardanian.com/posts/beyond-openmp-in-cpp-rust/"
fetched_at: 2026-05-05T07:01:49.771825+00:00
source: "Ash Vardanyan"
tags: [blog, raw]
---

# Beyond OpenMP in C++ & Rust: Taskflow, Rayon, Fork Union 🍴

Source: https://ashvardanian.com/posts/beyond-openmp-in-cpp-rust/

TL;DR: Most C++ and Rust thread-pool libraries leave significant performance on the table - often running 10× slower than
OpenMP
on classic fork-join workloads and
micro-benchmarks
.
So I’ve drafted a minimal ~300-line library called
Fork Union
that lands within 20% of OpenMP.
It does not use advanced
NUMA
tricks; it uses only the C++ and Rust standard libraries and has no other dependencies.
Update (Sep 2025): Since the
v2 release
, Fork Union supports NUMA and Huge Pages, as well as
tpause
,
wfet
, and other “pro” features.
Check the
README for details
.
OpenMP
has been the industry workhorse for coarse-grain parallelism in C and C++ for decades.
I lean on it heavily in projects like
USearch
, yet I avoid it in larger systems because:
Fine-grain parallelism
with independent subsystems doesn’t map cleanly to OpenMP’s global runtime.
Portability
of the C++ STL and the Rust standard library is better than OpenMP.
Meta-programming
with OpenMP is a pain - mixing
#pragma omp
with templates quickly becomes unmaintainable.
So I went looking for ready-made thread pools in C++ and Rust — only to realize
most of them implement asynchronous task queues, a much heavier abstraction than OpenMP’s fork-join model
.
Those extra layers introduce what I call the four horsemen of low performance:
Locks & mutexes
with syscalls in the hot path.
Heap allocations
in queues, tasks, futures, and promises.
Compare-and-swap
(CAS) stalls in the pessimistic path.
False sharing
unaligned counters thrashing cache lines.
With today’s dual-socket AWS machines pushing 192 physical cores, I needed something leaner than
Taskflow
,
Rayon
, or
Tokio
.
Enter
Fork Union
.
Benchmarks
#
Hardware: AWS Graviton 4 metal (single NUMA node, 96× Arm v9 cores, 1 thread/core).
Workload:
“ParallelReductionsBenchmark”
- summing single-precision floats in parallel.
In this case, just one cache line (
float[16]
) per core—small enough to stress synchronization cost of the thread pool rather than arithmetic throughput of the CPU.
In other words, we are benchmarking kernels similar to:
1
2
3
4
5
6
7
8
9
#include
<array>
float
parallel_sum
(
std
::
array
<
float
,
96
*
16
>
const
&
data
)
{
float
result
=
0.0f
;
#pragma omp parallel for reduction(+:result)
// Not how we profile OpenMP
for
(
std
::
size_t
i
=
0
;
i
<
data
.
size
();
++
i
)
result
+=
data
[
i
];
return
result
;
}
Google Benchmark
numbers for the C++ version of Fork Union, compared to OpenMP,
Taskflow
, and allocating 96×
std::thread
objects on-demand, are as follows:
1
2
3
4
5
6
7
8
9
PARALLEL_REDUCTIONS_LENGTH
=
1536
build_release/reduce_bench
-----------------------------------
Benchmark           UserCounters...
-----------------------------------
std::threads        bytes/s
=
3.00106 MB/s
tf::taskflow        bytes/s
=
76.2837 MB/s
av::fork_union      bytes/s
=
467.714 MB/s
openmp              bytes/s
=
585.492 MB/s
I’ve cleaned up the output, focusing only on the relevant rows and the reduction throughput.
Criterion.rs
numbers for the Rust version of Fork Union, compared to
Rayon
,
Tokio
, and Smol’s
Async Executors
, are as follows:
1
2
3
4
5
6
$
PARALLEL_REDUCTIONS_LENGTH
=
1536
cargo +nightly bench -- --output-format bencher
test
fork_union ... bench:  5,150 ns/iter
(
+/- 402
)
test
rayon ... bench:      47,251 ns/iter
(
+/- 3,985
)
test
smol ... bench:       54,931 ns/iter
(
+/- 10
)
test
tokio ... bench:     240,707 ns/iter
(
+/- 921
)
The timing methods used in those two executables are different, but the relative observations should hold.
Spawning new threads is obviously too expensive.
Most reusable thread pools are still 10x slower to sync than OpenMP.
OpenMP isn’t easy to compete with and still outperforms Fork Union by 20%.
This clearly shows, how important it is to chose the right tool for the job.
Don’t pick an asynchronous task pool for a fork-join blocking workload!
Four Horsemen of Performance
#
This article won’t be a deep dive into those topics.
Each deserves its own article and a proper benchmark, with some good ones already available and linked.
Locks and Mutexes
#
Unlike the
std::atomic
, the
std::mutex
update may result in a system call, and it can be expensive to acquire and release.
Its implementations generally have 2 executable paths:
the fast path, where the mutex is not contended, where it first tries to grab the mutex via a compare-and-swap operation, and if it succeeds, it returns immediately.
the slow path, where the mutex is contended, and it has to go through the kernel to block the thread until the mutex is available.
On Linux, the latter translates to a
“futex” syscall
and an expensive
context switch
.
In Rust, the same applies to
std::async::atomic
and
std::sync::Mutex
.
Prefer the former when possible.
Memory Allocations
#
Most thread-pools use classes like
std::future
,
std::packaged_task
,
std::function
,
std::queue
,
std::conditional_variable
.
In Rust land, there will often be a
std::Box
,
std::Arc
,
std::collections::VecDeque
,
std::sync::mpsc
or even
std::sync::mpmc
.
Most of those, I believe, aren’t unusable in Big-Data applications, where you always operate in memory-constrained environments:
Raising a
std::bad_alloc
exception when there is no memory left and just hoping that someone up the call stack will catch it is not a great design idea for Systems Engineering.
The threat of having to synchronize ~200 physical CPU cores across 2-8 sockets and potentially dozens of NUMA nodes around a shared global memory allocator practically means you can’t have predictable performance.
As we focus on a simpler
concurrency
parallelism model, we can avoid the complexity of allocating shared states, wrapping callbacks into some heap-allocated “tasks”, and a lot of other boilerplates.
Less work = more performance.
Atomics and CAS
#
Once you get to the lowest-level primitives on concurrency, you end up with the
std::atomic
and a small set of hardware-supported atomic instructions.
Hardware implements it differently:
x86 is built around the “Total Store Order” (TSO)
memory consistency model
and provides
LOCK
variants of the
ADD
and
CMPXCHG
. These variants act as full-blown “fences” — no loads or stores can be reordered across them. This makes atomic operations on x86 straightforward but heavyweight.
Arm, on the other hand, has a “weak” memory model and provides a set of atomic instructions that are not fenced and match the C++ concurrency model. It offers
acquire
,
release
, and
acq_rel
variants of each atomic instruction — such as
LDADD
,
STADD
, and
CAS
— which allow precise control over visibility and order, especially with the introduction of
“Large System Extension” (LSE)
instructions in Armv8.1-A.
A locked atomic on x86 requires the cache line in the Exclusive state in the requester’s L1 cache.
This would incur a coherence transaction (Read-for-Ownership) if another core had the line.
Both Intel and AMD handle this similarly.
It makes
Arm and Power much more suitable for lock-free programming
and concurrent data structures, but some observations hold for both platforms.
Most importantly, “Compare and Swap” (CAS) is costly and should be avoided at all costs.
On x86, for example, the
LOCK ADD
can easily take 50 CPU cycles
.
It is 50x slower than a regular
ADD
instruction but still easily 5-10x faster than a
LOCK CMPXCHG
instruction.
Once the contention rises, the gap naturally widens, further amplified by the increased “failure” rate of the CAS operation when the value being compared has already changed.
That’s why, for the “dynamic” mode, we resort to using an additional atomic variable rather than more typical CAS-based implementations.
Alignment
#
Assuming a thread pool is a heavy object anyway, nobody will care if it’s a bit larger than expected.
That allows us to over-align the internal counters to
std::hardware_destructive_interference_size
or
std::max_align_t
to avoid false sharing.
In that case, even on x86, where the entire cache will be exclusively owned by a single thread, in eager mode, we end up effectively “pipelining” the execution, where one thread may be incrementing the “in-flight” counter while the other is decrementing the “remaining” counter.
Others are executing the loop body in between.
Comparing APIs
#
Fork Union
#
Fork Union has a straightforward goal, so its API is equally clear.
There are only 4 core interfaces:
for_each_thread
- to dispatch a callback per thread, similar to
#pragma omp parallel
.
for_each_static
- for individual evenly-sized tasks, similar to
#pragma omp for schedule(static)
.
for_each_slice
- for slices of evenly-sized tasks, similar to nested
#pragma omp for schedule(static)
.
for_each_dynamic
- for individual unevenly-sized tasks, similar to
#pragma omp for schedule(dynamic, 1)
.
They all receive a C++ lambda or a Rust closure and a range of tasks to execute.
The construction of the thread pool itself is a bit trickier than typically in standard libraries, as “exceptions” and “panics” are not allowed.
So, the constructor can’t perform any real work.
In C++, the
try_spawn
method can be called to allocate all the threads:
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
#include
<fork_union.hpp>
// `fork_union_t`
#include
<cstdio>
// `stderr`
#include
<cstdlib>
// `EXIT_SUCCESS`
namespace
fun
=
ashvardanian
::
fork_union
;
int
main
()
{
fun
::
fork_union_t
pool
;
if
(
!
pool
.
try_spawn
(
std
::
thread
::
hardware_concurrency
()))
{
std
::
fprintf
(
stderr
,
"Failed to fork the threads
\n
"
);
return
EXIT_FAILURE
;
}
pool
.
for_each_thread
([
&
](
std
::
size_t
thread_index
)
noexcept
{
std
::
printf
(
"Hello from thread # %zu (of %zu)
\n
"
,
thread_index
+
1
,
pool
.
count_threads
());
});
return
EXIT_SUCCESS
;
}
As you may have noticed, the lambdas are forced to be
noexcept
and can’t return anything.
This is a design choice that vastly simplifies the implementation.
In Rust, similarly, the
try_spawn
method can be used:
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
#![feature(allocator_api)]
use
std
::
error
::
Error
;
use
fork_union
::
ForkUnion
;
fn
main
()
->
Result
<
(),
Box
<
dyn
Error
>>
{
let
pool
=
ForkUnion
::
try_spawn
(
4
)
?
;
pool
.
for_each_thread
(
|
thread_index
|
{
println!
(
"Hello from thread #
{}
(of
{}
)"
,
thread_index
+
1
,
pool
.
count_threads
());
});
Ok
(())
}
Assuming Rust has no function overloading, there are a few alternatives:
try_spawn
- to spawn a thread pool with the main allocator.
try_spawn_in
- to spawn a thread pool with a custom allocator.
try_named_spawn
- to spawn a thread pool with the main allocator and a name.
try_named_spawn_in
- to spawn a thread pool with a custom allocator and a name.
Rayon
#
Rayon is the go-to Rust library for data parallelism.
It suffers from the same core design issues as every other thread pool I’ve looked at on GitHub, but it’s fair to say that at the high level, it provides outstanding coverage for various parallel iterators!
As such, there is
an open call to explore similar “Map-Reduce” and “Map-Fork-Reduce” patterns in Fork Union
to see if they can be implemented efficiently.
1
2
3
4
5
6
7
use
rayon
::
prelude
::
*
;
fn
sum_of_squares
(
input
:
&
[
i32
])
->
i32
{
input
.
par_iter
()
// <-- just change that!
.
map
(
|&
i
|
i
*
i
)
.
sum
()
}
The default
.par_iter()
API of Rayon,
at the start of the README.md
, is not how I’ve used it in “Parallel Reductions Benchmark”.
To ensure that we are benchmarking the actual synchronization cost of the thread pool, I’ve gone directly to the underlying
rayon::ThreadPool
API:
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
pub
fn
sum_rayon
(
pool
:
&
rayon
::
ThreadPool
,
data
:
&
[
f32
],
partial_sums
:
&
mut
[
f64
])
->
f64
{
let
cores
=
pool
.
current_num_threads
();
let
chunk_size
=
scalars_per_core
(
data
.
len
(),
cores
);
// Defined elsewhere
let
partial_sums_ptr
=
partial_sums
.
as_mut_ptr
()
as
usize
;
// Pointers aren't safe to pass around
pool
.
broadcast
(
|
context
:
rayon
::
BroadcastContext
<
'_
>|
{
let
thread_index
=
context
.
index
();
let
start
=
thread_index
*
chunk_size
;
if
start
>=
data
.
len
()
{
return
;
}
let
stop
=
std
::
cmp
::
min
(
start
+
chunk_size
,
data
.
len
());
let
partial_sum
=
sum_unrolled
(
&
data
[
start
..
stop
]);
unsafe
{
ptr
::
write
(
// Cast back to a pointer:
(
partial_sums_ptr
as
*
mut
f64
).
add
(
thread_index
),
partial_sum
,
);
}
});
partial_sums
.
iter
().
copied
().
sum
()
}
Taskflow
#
Taskflow is one of the most popular C++ libraries for parallelism.
It has many features, including async execution graphs on CPUs and GPUs.
The most common example
looks like this:
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
#include
<taskflow/taskflow.hpp>
int
main
()
{
tf
::
Executor
executor
;
tf
::
Taskflow
taskflow
;
auto
[
A
,
B
,
C
,
D
]
=
taskflow
.
emplace
(
// create four tasks
[]
()
{
std
::
cout
<<
"TaskA
\n
"
;
},
[]
()
{
std
::
cout
<<
"TaskB
\n
"
;
},
[]
()
{
std
::
cout
<<
"TaskC
\n
"
;
},
[]
()
{
std
::
cout
<<
"TaskD
\n
"
;
}
);
A
.
precede
(
B
,
C
);
// A runs before B and C
D
.
succeed
(
B
,
C
);
// D runs after  B and C
executor
.
run
(
taskflow
).
wait
();
return
0
;
}
Despite being just an example, it clearly shows how different Taskflow’s core objectives are from OpenMP and Fork Union.
It is still probably mainly used for simple static parallelism, similar to our case without complex dependencies and the
taskflow
can be reused.
Here is how “Parallel Reductions Benchmark” wraps Taskflow:
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
27
28
29
30
31
32
33
34
35
36
template
<
typename
serial_at
=
stl_accumulate_gt
<
float
>>
class
taskflow_gt
{
float
const
*
const
begin_
=
nullptr
;
float
const
*
const
end_
=
nullptr
;
std
::
size_t
const
cores_
=
0
;
tf
::
Executor
executor_
;
tf
::
Taskflow
taskflow_
;
struct
alignas
(
128
)
thread_result_t
{
double
partial_sum
=
0.0
;
};
std
::
vector
<
thread_result_t
>
sums_
;
public
:
taskflow_gt
()
=
default
;
taskflow_gt
(
float
const
*
b
,
float
const
*
e
)
:
begin_
{
b
},
end_
{
e
},
cores_
{
total_cores
()},
executor_
{
static_cast
<
unsigned
>
(
cores_
)},
sums_
{
cores_
}
{
auto
const
input_size
=
static_cast
<
std
::
size_t
>
(
end_
-
begin_
);
auto
const
chunk_size
=
scalars_per_core
(
input_size
,
cores_
);
for
(
std
::
size_t
thread_index
=
0
;
thread_index
<
cores_
;
++
thread_index
)
{
taskflow_
.
emplace
([
this
,
input_size
,
chunk_size
,
thread_index
]
{
std
::
size_t
const
start
=
std
::
min
(
thread_index
*
chunk_size
,
input_size
);
std
::
size_t
const
stop
=
std
::
min
(
start
+
chunk_size
,
input_size
);
sums_
[
thread_index
].
partial_sum
=
serial_at
{
begin_
+
start
,
begin_
+
stop
}();
});
}
}
double
operator
()()
{
executor_
.
run
(
taskflow_
).
wait
();
return
std
::
accumulate
(
sums_
.
begin
(),
sums_
.
end
(),
0.0
,
[](
double
acc
,
thread_result_t
const
&
x
)
noexcept
{
return
acc
+
x
.
partial_sum
;
});
}
};
Only the
operator()
method is timed, leaving the construction costs out of the equation.
Conclusions & Observations
#
Fork Union shows that a lean, 300-line fork-join pool can sit within ~20% of OpenMP, while more functional pools trail by an order of magnitude.
That margin will shift as more workloads, CPUs, and compilers are tested, so treat today’s numbers as directional, not gospel.
There may still be subtle memory-ordering bugs lurking in Fork Union, but the core observations should hold:
dodge mutexes, dynamic queues, likely-pessimistic CAS paths, and false sharing — regardless of language or framework
.
Rust is still new territory for me.
The biggest surprise is the
missing allocator support in
std::collections
on the stable toolchain.
Nightly’s
Vec::try_reserve_in
helps, but until stable lands, ergonomic custom allocation remains tricky.
The machinery exists in C++, yet most projects ignore it — so the culture needs to catch up.
PS: Spot dubious memory-ordering?
Open an issue
.
Want to close the remaining 20% gap?
Happy forking 🤗
