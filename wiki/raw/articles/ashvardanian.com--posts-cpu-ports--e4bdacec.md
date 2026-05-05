---
title: "Hiding x86 Port Latency for 330 GB/s/core Reductions 🫣"
url: "https://ashvardanian.com/posts/cpu-ports/"
fetched_at: 2026-05-05T07:01:49.658433+00:00
source: "Ash Vardanyan"
tags: [blog, raw]
---

# Hiding x86 Port Latency for 330 GB/s/core Reductions 🫣

Source: https://ashvardanian.com/posts/cpu-ports/

For High-Performance Computing engineers, here’s the gist:
On Intel CPUs, the
vaddps
instruction (vectorized
float
addition) executes on ports 0 and 5.
The
vfmadd132ps
instruction (vectorized fused
float
multiply-add, or FMA)
also
executes on ports 0 and 5.
On AMD CPUs, however, the
vaddps
instruction takes ports 2 and 3, and the
vfmadd132ps
instruction takes ports 0 and 1.
Since FMA is equivalent to simple addition when one of the arguments is 1, we can drastically increase the throughput of addition-heavy numerical kernels.
Every few years, I revisit my old projects to look for improvements and laugh at my younger self.
Great experience!
Totally recommend it!
While refactoring the mess that was my
ParallelReductionsBenchmark
, I found an interesting optimization opportunity.
The throughput of an
AVX-512
kernel running at
211 GB/s
on a single
AMD Zen 4
core on AWS can be further improved to reach
330 GB/s!
Sadly, this doesn’t apply to Intel.
What Are CPU Ports and Latency Hiding?
#
In the x86 world, CPU instructions are broken down into micro-ops, then dispatched to specialized ports for integer, floating-point, or load/store tasks.
In a way, you can think about CPU ports as the next level of parallelism after SIMD registers, where the same or different instructions can be executing simultaneously.
The cryptic notation, such as
1*p15+1*p23,
shows how many micro-ops go to each port on different microarchitectures.
This means the instruction is first dispatched to port 1 or 5, then continues on port 2 or 3.
Effective “port balancing” is crucial for saturating available bandwidth and hiding latency.
For those interested, tools like
uops.info
or
Agner Fog’s optimization guides
compile this information for various CPU vendors and generations, saving you from diving into unstructured vendor- and generation-specific PDFs.
The number of ports and capabilities vary significantly between CPU models and vendors.
Intel Ice Lake ports
AMD Zen 4 ports
AES ops like
AESENC (XMM, XMM)
0
0, 1
CRC ops like
CRC32 (R32, R32)
1
N/A on uops.info
Aligned loads like
VMOVDQA64 (ZMM, M512)
2, 3
0, 1, 2, 3
Adding bytes like
VPADDB (ZMM, ZMM, ZMM)
0, 5
0, 1, 2, 3
Adding
doubles like
VADDPD (ZMM, ZMM, ZMM)
0, 5
2, 3
FMA
like
VFMADD132PS (ZMM, ZMM, ZMM)
0, 5
0, 1
Check out
VSCATTERQPS (VSIB_ZMM, K, YMM)
for a truly complex port signature.
According to
uops.info
, it looks like
2*p0+1*p0156+8*p49+8*p78
on
Ice Lake
, while on Zen 4, it’s
2*FP12+3*FP123+3*FP23+18*FP45
.
Old AVX-512 Kernel
#
Below is my old AVX-512 kernel designed for large input arrays aligned to at least 64 bytes.
I’m using
non-temporal loads
, which are generally recommended when handling large volumes of data in a streaming fashion.
This prevents CPU cache pollution with data that will soon be evicted without reuse.
The kernel traverses the input array in two directions - forward and reverse.
Modern CPUs easily predict both traversal patterns and prefetch accordingly.
Pulling data from different ends helps keep the
TLB
caches warm.
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
class
avx512_f32streamed_t
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
public
:
avx512_f32streamed_t
()
=
default
;
avx512_f32streamed_t
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
noexcept
:
begin_
(
b
),
end_
(
e
)
{}
float
operator
()()
const
noexcept
{
auto
it_begin
=
begin_
;
auto
it_end
=
end_
;
__m512
acc1
=
_mm512_setzero_ps
();
// Accumulator for forward direction
__m512
acc2
=
_mm512_setzero_ps
();
// Accumulator for reverse direction
// Process in chunks of 16 floats in each direction
for
(;
it_end
-
it_begin
>=
32
;
it_begin
+=
16
,
it_end
-=
16
)
{
acc1
=
_mm512_add_ps
(
acc1
,
_mm512_castsi512_ps
(
_mm512_stream_load_si512
((
void
*
)(
it_begin
))));
acc2
=
_mm512_add_ps
(
acc2
,
_mm512_castsi512_ps
(
_mm512_stream_load_si512
((
void
*
)(
it_end
-
16
))));
}
// Combine the accumulators
__m512
acc
=
_mm512_add_ps
(
acc1
,
acc2
);
float
sum
=
_mm512_reduce_add_ps
(
acc
);
//! Not an instruction, but fine with GCC & Clang
while
(
it_begin
<
it_end
)
sum
+=
*
it_begin
++
;
return
sum
;
}
};
A common suggestion for my libraries (mainly
StringZilla
and
SimSIMD
) is to
unroll the loops
.
I generally oppose this idea in naive kernels like these.
While you might gain a few points in synthetic micro-benchmarks, you’ll consume more
L1i
instruction cache, potentially hurting other parts of your program - and likely getting no improvements in return.
Check out how poorly the unrolled
f32unrolled
variants perform in the end.
New AVX-512 Kernel
#
The new kernel is similar but uses more registers!
It employs 4 independent accumulators and a dedicated register of
1.0f
values.
As before, the
_mm512_add_ps
intrinsic (mapping to
vaddps zmm, zmm, zmm
instruction) is called twice in the loop body.
Additionally, we use the
_mm512_fmadd_ps
intrinsic (mapping to
vfmadd132ps zmm, zmm, zmm
) twice in the loop.
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
class
avx512_f32interleaving_t
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
public
:
avx512_f32interleaving_t
()
=
default
;
avx512_f32interleaving_t
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
(
b
),
end_
(
e
)
{}
float
operator
()()
const
noexcept
{
auto
it_begin
=
begin_
;
auto
it_end
=
end_
;
__m512
acc1
=
_mm512_setzero_ps
();
// Accumulator for forward direction addition
__m512
acc2
=
_mm512_setzero_ps
();
// Accumulator for reverse direction addition
__m512
acc3
=
_mm512_setzero_ps
();
// Accumulator for forward direction FMAs
__m512
acc4
=
_mm512_setzero_ps
();
// Accumulator for reverse direction FMAs
__m512
ones
=
_mm512_set1_ps
(
1.0f
);
// Process in chunks of 32 floats in each direction
for
(;
it_end
-
it_begin
>=
64
;
it_begin
+=
32
,
it_end
-=
32
)
{
acc1
=
_mm512_add_ps
(
acc1
,
_mm512_castsi512_ps
(
_mm512_stream_load_si512
((
void
*
)(
it_begin
))));
acc2
=
_mm512_add_ps
(
acc2
,
_mm512_castsi512_ps
(
_mm512_stream_load_si512
((
void
*
)(
it_end
-
16
))));
acc3
=
_mm512_fmadd_ps
(
ones
,
_mm512_castsi512_ps
(
_mm512_stream_load_si512
((
void
*
)(
it_begin
+
16
))),
acc3
);
acc4
=
_mm512_fmadd_ps
(
ones
,
_mm512_castsi512_ps
(
_mm512_stream_load_si512
((
void
*
)(
it_end
-
32
))),
acc4
);
}
// Combine the accumulators
__m512
acc
=
_mm512_add_ps
(
_mm512_add_ps
(
acc1
,
acc2
),
_mm512_add_ps
(
acc2
,
acc3
));
float
sum
=
_mm512_reduce_add_ps
(
acc
);
while
(
it_begin
<
it_end
)
sum
+=
*
it_begin
++
;
return
sum
;
}
};
On AMD Zen 4 CPUs,
acc1
and
acc2
execute on ports 2 and 3, while
acc3
and
acc4
run on ports 0 and 1.
Benchmarks
#
For the environment, I used an AWS
m7a.metal-48xlarge
instance with 192 cores across 2 sockets.
The code is compiled with GCC 14.2 on Ubuntu 24.04.
For context, each core has 32 KiB of L1 and 1024 KiB of L2 data cache on that machine.
With tiny arrays, like 1024 floats, we don’t need to touch RAM.
The numbers exceed RAM throughput and reflect ALU throughput, exceeding 330 GB/s for the newest latency-hiding variant:
1
2
3
4
5
Benchmark                                                          Time             CPU    Iterations UserCounters...
--------------------------------------------------------------------------------------------------------------------
avx512/f32/streamed/min_time:10.000/real_time                    19.4 ns         19.4 ns
724081506
bytes/s
=
211.264G/s
avx512/f32/unrolled/min_time:10.000/real_time                    15.1 ns         15.1 ns
934282388
bytes/s
=
271.615G/s
avx512/f32/interleaving/min_time:10.000/real_time                12.3 ns         12.3 ns
1158791855
bytes/s
=
332.539G/s
For a much larger dataset of 268,435,456 floats coming from RAM, the throughput is lower, but we still see a 56% improvement over the baseline:
1
2
3
4
5
Benchmark                                                               Time             CPU   Iterations UserCounters...
-------------------------------------------------------------------------------------------------------------------------
avx512/f32/streamed/min_time:10.000/real_time
57275577
ns
57274822
ns
239
bytes/s
=
18.7469G/s
avx512/f32/unrolled/min_time:10.000/real_time
45038995
ns
45038427
ns
310
bytes/s
=
23.8403G/s
avx512/f32/interleaving/min_time:10.000/real_time
36912750
ns
36912281
ns
383
bytes/s
=
29.0886G/s
When running on multiple cores, we’re only as fast as we are lucky!
Performance depends on core affinity to the target memory region, which is controlled by the Linux kernel.
1
2
3
4
5
Benchmark                                                               Time             CPU   Iterations UserCounters...
-------------------------------------------------------------------------------------------------------------------------
avx512/f32/streamed/std::threads/min_time:10.000/real_time
9736048
ns
9538167
ns
1446
bytes/s
=
110.285G/s
avx512/f32/unrolled/std::threads/min_time:10.000/real_time
8402737
ns
8278814
ns
1664
bytes/s
=
127.785G/s
avx512/f32/interleaving/std::threads/min_time:10.000/real_time
8200623
ns
8140023
ns
1694
bytes/s
=
130.934G/s
The next addition to ParallelReductionsBenchmark will likely be a lower-level thread pool, replacing
std::thread
with POSIX API to control core affinity.
While I’m working on something else right now, if you want to collaborate -
that task
is up for grabs along with a few other “good first issues” 🤗
It’s uncommon to find operations as basic as addition where we can hide latency.
It’s less uncommon with higher-level operations involving complex logic that can be implemented in multiple ways.
My favorite example is
Pete Cawley’s CRC32 implementation
, which combines the hardware-accelerated CRC instruction (issued via
_mm_crc32_u64
) with the carryless multiply instruction (issued via
_mm_clmulepi64_si128
).
I’ve just linked it to my
less_slow.cpp
tutorial
, and I recommend checking it out!
