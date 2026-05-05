---
title: "Crushing CPUs with 879 GB/s Reductions in CUDA"
url: "https://ashvardanian.com/posts/cuda-parallel-reductions/"
fetched_at: 2026-05-05T07:01:51.800379+00:00
source: "Ash Vardanyan"
tags: [blog, raw]
---

# Crushing CPUs with 879 GB/s Reductions in CUDA

Source: https://ashvardanian.com/posts/cuda-parallel-reductions/

GPU acceleration
can be trivial
for Python users.
Follow CUDA installation steps carefully, replace
import numpy as np
with
import cupy as np
, and you will often get the 100x performance boosts without breaking a sweat.
Every time you write magical one-liners, remember a systems engineer is making your dreams come true.
A couple of years ago, when I was giving a
talk
on the breadth of GPGPU technologies, I published a repo.
A repo with various cool GPGPU staff in
Vulkan
,
Halide
, and most importantly,
8x
implementations of
std::accumulate
in OpenCL.
I know what you are thinking:
Eight ways to sum numbers?! Are you 🌰s?!
Don’t worry!
We are now back with more!
No more OpenCL, no more
SyCL
.
This time we focus on
Parallel STL
,
SIMD
,
OpenMP
and, of course,
CUDA
,
CUB
and
Thrust
!
You can find all the sources
hosted on our
GitHub
.
Benchmarks were run with the newest stable versions of software available at the time: Ubuntu 20.04, GCC 10.3, CUDA Toolkit 11.6, Thrust 1.15, oneTBB 2021.5 and TaskFlow 3.3.
This article went through 2 updates.
First, the
OpenMP numbers
were corrected.
Later, I reflected on the results and came to a shocking conclusion.
It thematically belongs in the middle, but I
published it separately
to avoid spoilers and keep it chronological.
C++ and STL
#
The canonical serial solution for this problem in C and C++ would be:
1
2
3
float
sum
=
0
for
(;
begin
!=
end
;
++
begin
)
sum
+=
*
begin
;
For simple tasks like this, there is also an STL version.
Let’s put a sample an example with 1 GB worth of
float
numbers:
1
2
3
std
::
vector
<
float
>
numbers
(
1024
*
1024
*
256
);
std
::
fill
(
numbers
.
begin
(),
numbers
.
end
(),
1.f
);
auto
sum
=
std
::
accumulate
(
numbers
.
begin
(),
numbers
.
end
(),
0.f
);
Time for some trivia questions. What will be the sum?
Due to rounding errors, the result of sequential accumulation will be significantly less accurate than doing it in batches or parallel tree-like reductions.
To avoid it, you would need more memory.
One more
float
for the compensation part, as in the
Kahan summation
algorithm.
Or simply using a
double
for the accumulation.
The latter being equally fast on modern x86 chips and easier to implement:
5.2 GB/s
when accumulating into
float
, with a 93% error.
5.3 GB/s
when accumulating into
double
, with a 0% error.
SIMD: AVX2
#
We also implemented three
AVX2 SIMD
variants for intra-thread acceleration:
Naive 8x lane
float
accumulation.
Kahans 8x lane
float
accumulation.
Conversions and 4x lane
double
accumulation.
They all utilize heavy instructions, so some downclocking occurs, but performance is excellent, and rounding errors disappear in the last two variants.
The (1) and (3) SIMD code is trivial.
We will only post the Kahan version for clarity.
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
float
operator
()(
float
const
*
begin
,
float
const
*
end
)
noexcept
{
auto
it
=
begin
;
// SIMD-parallel summation stage
auto
sums
=
_mm256_set1_ps
(
0
);
auto
compensations
=
_mm256_set1_ps
(
0
);
auto
t
=
_mm256_set1_ps
(
0
);
auto
y
=
_mm256_set1_ps
(
0
);
for
(;
it
+
8
<
end
;
it
+=
8
)
{
y
=
_mm256_sub_ps
(
_mm256_loadu_ps
(
it
),
compensations
);
t
=
_mm256_add_ps
(
sums
,
y
);
compensations
=
_mm256_sub_ps
(
_mm256_sub_ps
(
t
,
sums
),
y
);
sums
=
t
;
}
// Cross-lane horizontal reduction
sums
=
_mm256_hadd_ps
(
sums
,
_mm256_permute2f128_ps
(
sums
,
sums
,
1
));
sums
=
_mm256_hadd_ps
(
sums
,
sums
);
sums
=
_mm256_hadd_ps
(
sums
,
sums
);
auto
sum
=
_mm256_cvtss_f32
(
sums
);
// Serial summation of the remainder
for
(;
it
!=
end
;
++
it
)
sum
+=
*
it
;
return
sum
;
}
Results on a single CPU core:
22.3 GB/s
naively accumulating
float
, with a 50% error.
10.9 GB/s
accumulation with Kahans method, with 0% error.
17.0 GB/s
accumulating as
double
s, with 0% error.
OpenMP
#
Not to be confused with OpenMPI,
Open Multi-Processing
is probably the oldest Multi-Threading (not Multi-Processing!) standard.
It has run on anything from desktops to supercomputers since 1997 and is widely supported by Fortran, C and C++ compilers.
Aside from the oldest
#pragma
s, they also support parallel reductions:
1
2
3
4
5
6
7
8
float
operator
()(
float
const
*
begin
,
float
const
*
end
)
noexcept
{
float
sum
=
0
;
size_t
const
n
=
end
-
begin
;
#pragma omp parallel for default(shared) reduction(+ : sum)
for
(
size_t
i
=
0
;
i
!=
n
;
i
++
)
sum
+=
begin
[
i
];
return
sum
;
}
We tried
every OpenMP reduction tutorial
but couldn’t make it work faster than the most basic serial version of
std::accumulate
.
Result:
5.4 GB/s
.
Update on OpenMP
#
After a few recommendations on
Reddit
, an issue with compilation flags was resolved.
At 100% CPU utilization OpenMP scored
51.5 GB/s
.
After that, we disabled dynamic scheduling with
omp_set_dynamic(0)
and reduced the number of threads, reaching the result of
80 GB/s
.
Parallel Algorithms
#
STL ships with
std::execution
policies since 17th edition.
Hope being, that multi-threaded
<algorithm>
s are easy to use and at least as good as average parallel code.
1
auto
sum
=
std
::
reduce
(
std
::
execution
::
par_unseq
,
numbers
.
begin
(),
numbers
.
end
(),
0.f
);
Result:
5.3 GB/s
.
Wait, it’s the same as we got for single-threaded code.
We forgot that GCC relies on Intel’s
Thread Building Blocks
to implement parallel algorithms.
Let’s update our
CMakeLists.txt
:
1
2
3
4
5
6
7
8
FetchContent_Declare
(
TBB
GIT_REPOSITORY
https://github.com/oneapi-src/oneTBB.git
GIT_TAG
v2021.5.0
)
FetchContent_Populate
(
TBB
)
include_directories
(
BEFORE
${
TBB_SOURCE_DIR
}
)
target_link_libraries
(
reduce_bench
TBB::tbb
)
Run again and hurray!
80 GB/s
in
std::execution::par
reductions.
87 GB/s
in
std::execution::par_unseq
reductions.
Now we are going somewhere!
Can we go there faster?
SIMD + Threads
#
If we take our AVX2 SIMD (#3) implementation and spawn 64x
std::threads
, whenever a new task comes, we can still go a little faster:
89 GB/s
.
In the best-case scenario, if we always had a thread-pool around, with ~20 idle threads, we could do even better, up to 200 GB/s.
Not more.
Not until
we switch
from DDR4 to DDR5 and from 8-channel to 12-channel RAM.
Extrapolating the
Hash-Table benchmarks
of Apple M1 Max laptops, we can expect massive boosts in DDR5-powered servers.
Sapphire Rapids may even get in-package High Bandwidth Memory, but for now, only GPUs have that!
Switching to GPUs
#
It would have been interesting to run the same OpenCL scripts on both CPUs and GPUs.
Unfortunately, we lost that opportunity about two years ago, when AMD
dropped support for OpenCL
in their CPU lineup.
As we are only limited to a GPU, we will skip OpenCL this time, assuming that, on average, its kernels are at least 30% slower than CUDA.
GPU Model
Size
Type
Bus
Bandwidth
3090
24 GB
GDDR6X
384 bit
936 GB/s
3090 Ti
24 GB
GDDR6X
384 bit
1'018 GB/s
A100
SXM4
80 GB
HBM2e
5120 bit
2'039 GB/s
Before starting our experiment, let’s determine our upper bound.
The A100 is a datacenter GPU, and 3090 Ti hasn’t reached the market yet, so we won’t get 1 TB/s this time around.
CUDA with SHFL
#
There is the old way “to CUDA” and the new way.
The old one uses just
__shared__
memory.
The post-Kepler method recommends using shuffles for thread scheduling.
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
__inline__
__device__
float
cu_reduce_warp
(
float
val
)
{
val
+=
__shfl_down_sync
(
0xffffffff
,
val
,
16
);
val
+=
__shfl_down_sync
(
0xffffffff
,
val
,
8
);
val
+=
__shfl_down_sync
(
0xffffffff
,
val
,
4
);
val
+=
__shfl_down_sync
(
0xffffffff
,
val
,
2
);
val
+=
__shfl_down_sync
(
0xffffffff
,
val
,
1
);
return
val
;
}
__global__
void
cu_reduce_warps
(
float
const
*
inputs
,
unsigned
int
input_size
,
float
*
outputs
)
{
float
sum
=
0
;
for
(
unsigned
int
i
=
blockIdx
.
x
*
blockDim
.
x
+
threadIdx
.
x
;
i
<
input_size
;
i
+=
blockDim
.
x
*
gridDim
.
x
)
sum
+=
inputs
[
i
];
__shared__
float
shared
[
32
];
unsigned
int
lane
=
threadIdx
.
x
%
warpSize
;
unsigned
int
wid
=
threadIdx
.
x
/
warpSize
;
sum
=
cu_reduce_warp
(
sum
);
if
(
lane
==
0
)
shared
[
wid
]
=
sum
;
// Wait for all partial reductions
__syncthreads
();
sum
=
(
threadIdx
.
x
<
blockDim
.
x
/
warpSize
)
?
shared
[
lane
]
:
0
;
if
(
wid
==
0
)
sum
=
cu_reduce_warp
(
sum
);
if
(
threadIdx
.
x
==
0
)
outputs
[
blockIdx
.
x
]
=
sum
;
}
This sample more or less repeats the CUDA tutorial but replaces the
deprecated
__shfl_down
with
__shfl_down_sync
in the first function.
Mouthful, compared to
std::accumulate
, but it gets the work done:
817 GB/s
💣💣
Thrust
#
Thrust might just be my favorite high-level library.
Generic enough to be considered an STL extension and full of intrguing technical solutions.
If you don’t want to write a custom kernel for a GPU, you can probably compose a multi-round alternative with Thrust.
1
thrust
::
reduce
(
numbers
.
begin
(),
numbers
.
end
(),
float
(
0
),
thrust
::
plus
<
float
>
());
The result:
743 GB/s
.
A 9% reduction, compared to the hand-written kernel, but hardly slow.
Those of us waiting for NVCC implementation of Parallel Algorithms will use it indirectly.
Others can use it directly or go one
paragraph
layer lower to CUB.
CUB
#
CUBs main benefit is stricter control over memory allocations.
Parallel and concurrent algorithms often require extra memory compared to serial analogues.
To keep the interface familiar and straightforward, Thrust may allocate temporary memory internally.
With CUB, you manage memory yourself and control the algorithm selection more explicitly, resulting in faster code but a much heavier codebase.
For example, you would typically call the same function twice.
First time only to estimate the needed temporary memory capacity.
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
float
operator
()(
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
{
// Reuse the following arrays
thrust
::
device_vector
<
float
>
gpu_inputs
(
b
,
e
);
thrust
::
device_vector
<
float
>
gpu_sums
(
1
);
thrust
::
host_vector
<
float
>
cpu_sums
(
1
);
thrust
::
device_vector
<
uint8_t
>
temporary
;
// CUB can't handle large arrays with over 2 billion elements!
assert
(
gpu_inputs
.
size
()
<
std
::
numeric_limits
<
int
>::
max
());
auto
num_items
=
static_cast
<
int
>
(
gpu_inputs
.
size
());
auto
ins
=
gpu_inputs
.
data
().
get
();
auto
outs
=
gpu_sums
.
data
().
get
();
// Determine temporary device storage requirements
cudaError_t
error
;
void
*
temps
=
nullptr
;
size_t
temps_size
=
0
;
error
=
cub
::
DeviceReduce
::
Sum
(
temps
,
temps_size
,
ins
,
outs
,
num_items
);
assert
(
error
==
cudaSuccess
);
// Allocate temporary storage, if needed
if
(
temps_size
>
temporary
.
size
())
temporary
.
resize
(
temps_size
);
temps
=
temporary
.
data
().
get
();
error
=
cub
::
DeviceReduce
::
Sum
(
temps
,
temps_size
,
ins
,
outs
,
num_items
);
assert
(
error
==
cudaSuccess
);
cudaDeviceSynchronize
();
cpu_sums
=
gpu_sums
;
return
cpu_sums
[
0
];
}
CUB provides shortcuts for the most common binary commutative operators: sum, min, max, argmin, argmax.
So instead of invoking
cub::DeviceReduce::Reduce
in this case, we run
cub::DeviceReduce::Sum
.
Result:
879 GB/s
🔥🔥🔥
CUB is an excellent library by itself - a huge productivity booster.
Especially the device-scale functions, like
DeviceHistogram
,
DevicePartition
,
DeviceRadixSort
,
DeviceRunLengthEncode
,
DeviceScan
.
Our internal on-GPU compression library, for example, has a multi-stage pipeline, where parts were initially written with Thrust.
Then accelerated with CUB and only in most important places, rewritten in raw CUDA.
Tensor Cores
#
This is one of those cases where
Tensor Cores
can’t help us much.
We can program the
wmma::
intrinsics in CUDA directly.
In that case, we can reshape the input array into a very long matrix and multiply it by small auto-generated matrices on the fly.
Every
wmma::fragment<wmma::matrix_b, 16, 16, 8, wmma::precision::tf32, wmma::row_major>
would contain mostly zeros, except the first column of ones.
Every warp would perform its reduction, accumulating 16²=256 numbers into a column of 16 sums.
One per row.
It’s a lot of wasted compute capacity, but given the insane efficiency of Tensor Cores, we could have gotten a slight improvement.
Still, assuming we have already reached
94% of theoretical memory bandwidth
, we are definitely in the red zone of diminishing returns.
Roundup
#
We repeated the benchmarks for every power-of-two array size between 32 MB and 4 GB.
If an image is worth a thousand words to you, enjoy!
Again, if you are curious to see how your CPU/GPU would compete, here is the
GitHub
link for these benchmarks.
It should be pretty easy to install if you have ever used CMake.
Intel is preparing its
Ponte Vecchio
GPU launch.
And AMD is trying to attract more customers for their
MI200
GPUs.
With all that action, we should expect more first-party HPC libraries, like Thrust and CUB.
Before then, we will keep reinventing the wheel, often implementing stuff from scratch and writing about it occasionally.
All to accelerate AI research and build the
fastest persistent DBMS
the world as ever seen 😉
