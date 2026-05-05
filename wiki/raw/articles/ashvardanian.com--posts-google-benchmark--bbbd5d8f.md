---
title: "Mastering C++ with Google Benchmark ⏱️"
url: "https://ashvardanian.com/posts/google-benchmark/"
fetched_at: 2026-05-05T07:01:51.896880+00:00
source: "Ash Vardanyan"
tags: [blog, raw]
---

# Mastering C++ with Google Benchmark ⏱️

Source: https://ashvardanian.com/posts/google-benchmark/

There are only two kinds of languages:
the ones people complain about
and the ones nobody uses.
–
Bjarne Stroustrup
, creator of C++.
Very few consider C++ attractive, and only some people think it’s easy.
Choosing it for a project generally means you care about the performance of your code.
And rightly so!
Today, machines can process
hundreds of Gigabytes per second
, and we, as developers, should all learn to saturate those capabilities.
So, let’s look into a few simple code snippets and familiarize ourselves with
Google Benchmark
(GB) - the most famous library in the space using incrementally complex examples.
For the impatient ones, here is the
source code on GitHub
.
That repo also has the results for AMD EPYC 7302 and Threadripper PRO 3995WX CPUs with
-O1
and
-O3
builds.
Math Micro-Ops
#
Every benchmark has the following structure.
You define the operation, but GB decides how often to run it.
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
#include
<benchmark/benchmark.h>
namespace
bm
=
benchmark
;
static
void
i32_addition
(
bm
::
State
&
state
)
{
int32_t
a
,
b
,
c
;
for
(
auto
_
:
state
)
c
=
a
+
b
;
}
BENCHMARK
(
i32_addition
);
Compile it with
-O3
, run, result:
0 ns
.
Thanks for your attention, that’s all 😅
Unfortunately, no operation runs this fast on the computer.
On a 3 GHz CPU, you would perform 3 Billion ops every second.
So, each would take 0.33 ns, not 0 ns.
The compiler just optimized everything out.
Cost of Random Generators
#
What will happen if we mutate the addition arguments between loop iterations?
1
2
3
4
5
static
void
i32_addition_random
(
bm
::
State
&
state
)
{
int32_t
c
=
0
;
for
(
auto
_
:
state
)
c
=
std
::
rand
()
+
std
::
rand
();
}
__25ns__looks better than zero, but something doesn’t add up.
If the addition is a single hardware instruction, why did it take ~100 cycles?
There are
BMI2 bit-manipulation assembly instructions
with such runtime on AMD Zen and Zen 2 chips, but not the addition.
1
2
3
4
5
static
void
i32_addition_semi_random
(
bm
::
State
&
state
)
{
int32_t
a
=
std
::
rand
(),
b
=
std
::
rand
(),
c
=
0
;
for
(
auto
_
:
state
)
bm
::
DoNotOptimize
(
c
=
(
++
a
)
+
(
++
b
));
}
Here is the pattern we often use in benchmarking.
There are better approaches for something as small as an addition, but it is good enough to make a point.
Initialize randomly before evaluation, then mutate.
Your mutations can be regular and predictable.
They just shouldn’t be expensive.
We also apply the
DoNotOptimize
function to force the compilation of that useless line.
This run took
0.7ns
per iteration or around 2 cycles.
The first cycle was spent incrementing
a
and
b
on different ALUs of the same core, while the second was performed the final accumulation.
1
2
BENCHMARK
(
i32_addition_random
)
->
Threads
(
8
);
BENCHMARK
(
i32_addition_semi_random
)
->
Threads
(
8
);
Now, let’s run those benchmarks on 8 threads.
The
std::rand
powered function took 12'000 ns, while our latest variant remained the same.
Like many other
libc
functions, it depends on the global state and uses mutexes to synchronize concurrent access to global memory.
Here is its
source in glibc
:
1
2
3
4
5
6
7
8
long
int
__random
(
void
)
{
int32_t
retval
;
__libc_lock_lock
(
lock
);
(
void
)
__random_r
(
&
unsafe_state
,
&
retval
);
__libc_lock_unlock
(
lock
);
return
retval
;
}
weak_alias
(
__random
,
random
)
Slow Trigonometry in LibC and STL and Fast Math
#
Let’s say you want to compute the sine of a floating-point number.
The standard has
std::sin
for that, but there is a different way.
We can approximate the result with the
Taylor-Maclaurin series
, taking the first three components of the expansion.
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
static
void
f64_sin
(
bm
::
State
&
state
)
{
double
argument
=
std
::
rand
(),
result
=
0
;
for
(
auto
_
:
state
)
bm
::
DoNotOptimize
(
result
=
std
::
sin
(
argument
+=
1.0
));
}
static
void
f64_sin_maclaurin
(
bm
::
State
&
state
)
{
double
argument
=
std
::
rand
(),
result
=
0
;
for
(
auto
_
:
state
)
{
argument
+=
1.0
;
result
=
argument
-
std
::
pow
(
argument
,
3
)
/
6
+
std
::
pow
(
argument
,
5
)
/
120
;
bm
::
DoNotOptimize
(
result
);
}
}
Pretty simple.
Here is the result:
51 ns
for the
std::sin
.
27 ns
for the Maclaurin series with
std::pow
.
Can we do better?
Of course, we can.
Raising to a power
x
is a
generic operation
.
In other words, likely slow.
Let’s unfold the expression manually:
1
2
3
4
5
6
7
8
9
static
void
f64_sin_maclaurin_powless
(
bm
::
State
&
state
)
{
double
argument
=
std
::
rand
(),
result
=
0
;
for
(
auto
_
:
state
)
{
argument
+=
1.0
;
result
=
(
argument
)
-
(
argument
*
argument
*
argument
)
/
6.0
+
(
argument
*
argument
*
argument
*
argument
*
argument
)
/
120.0
;
bm
::
DoNotOptimize
(
result
);
}
}
Result:
2.4 ns
, or 10x improvement!
The compiler will handle redundant operations, but it cannot freely reorder them.
In math, addition and multiplication are associative for real numbers but not in programming.
The order of operands will affect the result, so the compiler has its hands cuffed.
Let’s set them free!
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
[[gnu::optimize("-ffast-math")]]
static
void
f64_sin_maclaurin_with_fast_math
(
bm
::
State
&
state
)
{
double
argument
=
std
::
rand
(),
result
=
0
;
for
(
auto
_
:
state
)
{
argument
+=
1.0
;
result
=
(
argument
)
-
(
argument
*
argument
*
argument
)
/
6.0
+
(
argument
*
argument
*
argument
*
argument
*
argument
)
/
120.0
;
bm
::
DoNotOptimize
(
result
);
}
}
If you are not familiar with the modern C++ attributes, here is the older GCC version:
__attribute__((optimize("-ffast-math")))
.
Here, we advise GCC to apply extra flags when compiling the scope of this specific function.
This is one of my favorite tricks for rapid benchmarking without having to change
CMakeLists.txt
.
Result:
0.85 ns
.
For those interested, GCC has a
separate manual
for the complete list of available floating-point math optimizations.
The
-ffast-math
is a shortcut for
-funsafe-math-optimizations
, a shortcut for
-fassociative-math
.
In our specific case, with that many chained multiplications, the ordering may change under/overflow behavior, as stated in the “Transformations” section.
Integer Division
#
We have just accelerated a floating-point trigonometric function by a factor of
60x
from 51 ns to less than a nanosecond!
Can we do the same for integer division, the slowest integer arithmetical operation?
To a certain extent, yes.
1
2
3
4
5
static
void
i64_division
(
bm
::
State
&
state
)
{
int64_t
a
=
std
::
rand
(),
b
=
std
::
rand
(),
c
=
0
;
for
(
auto
_
:
state
)
bm
::
DoNotOptimize
(
c
=
(
++
a
)
/
(
++
b
));
}
This variant runs in
3.3 ns
, or 10x longer than addition.
But what if we divide by a constant, not a mutating value?
In that case, we must ensure the compiler knows that our denominator remains constant!
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
static
void
i64_division_by_const
(
bm
::
State
&
state
)
{
int64_t
money
=
2147483647
;
int64_t
a
=
std
::
rand
(),
c
;
for
(
auto
_
:
state
)
bm
::
DoNotOptimize
(
c
=
(
++
a
)
/
*
std
::
launder
(
&
money
));
}
static
void
i64_division_by_constexpr
(
bm
::
State
&
state
)
{
constexpr
int64_t
b
=
2147483647
;
int64_t
a
=
std
::
rand
(),
b
;
for
(
auto
_
:
state
)
bm
::
DoNotOptimize
(
c
=
(
++
a
)
/
b
);
}
The above functions only differ because the first involves some shady
money
launder
ing 😅
The compiler fails to trace the origins of
money
, so it can’t replace it with shifts and multiplications.
How big is the difference:
3.3 ns
vs
0.5 ns
!
Hardware Acceleration without Intrinsics
#
Most of the examples in this article are abstract, but this happened to me a couple of months ago.
1
2
3
4
5
[[gnu::target("default")]]
static
void
u64_population_count
(
bm
::
State
&
state
)
{
auto
a
=
static_cast
<
uint64_t
>
(
std
::
rand
());
for
(
auto
_
:
state
)
bm
::
DoNotOptimize
(
__builtin_popcount
(
++
a
));
}
Compilers have special intrinsics,
like
__builtin_popcount
.
Those are high-performance routines shipped with the compiler and aren’t portable.
Those differ from
Intel
or ARM intrinsics, which are hardware-specific and compiler-agnostic.
These are hardware-agnostic and compiler-specific.
1
2
3
4
5
[[gnu::target("popcnt")]]
static
void
u64_population_count_x86
(
bm
::
State
&
state
)
{
auto
a
=
static_cast
<
uint64_t
>
(
std
::
rand
());
for
(
auto
_
:
state
)
bm
::
DoNotOptimize
(
__builtin_popcount
(
++
a
));
}
I forgot to pass the
-mpopcnt
flag in the first variant, and the compiler silently continued.
When you want to be specific - explicitly trigger the
popcnt
instruction
.
The cost of this mistake was:
1.9 ns
and
0.3 ns
, or over 6x!
Broader Logic and Memory
#
Data Alignment
#
Compute may be expensive, but memory accesses always are!
The more you miss your CPU caches, the more you waste time!
1
2
3
4
5
6
constexpr
size_t
f32s_in_cache_line_k
=
64
/
sizeof
(
float
);
constexpr
size_t
f32s_in_cache_line_half_k
=
f32s_in_cache_line_k
/
2
;
struct
alignas
(
64
)
f32_array_t
{
float
raw
[
f32s_in_cache_line_k
*
2
];
};
Let’s illustrate it by creating a cache-aligned array with 32x
float
s.
That means 2x 64-byte cache lines worth of content.
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
static
void
f32_pairwise_accumulation
(
bm
::
State
&
state
)
{
f32_array_t
a
,
b
,
c
;
for
(
auto
_
:
state
)
for
(
size_t
i
=
f32s_in_cache_line_half_k
;
i
!=
f32s_in_cache_line_half_k
*
3
;
++
i
)
bm
::
DoNotOptimize
(
c
.
raw
[
i
]
=
a
.
raw
[
i
]
+
b
.
raw
[
i
]);
}
static
void
f32_pairwise_accumulation_aligned
(
bm
::
State
&
state
)
{
f32_array_t
a
,
b
,
c
;
for
(
auto
_
:
state
)
for
(
size_t
i
=
0
;
i
!=
f32s_in_cache_line_half_k
;
++
i
)
bm
::
DoNotOptimize
(
c
.
raw
[
i
]
=
a
.
raw
[
i
]
+
b
.
raw
[
i
]);
}
Now we run two benchmarks.
Both perform the same logical operations - 8x
float
additions and 8x stores.
But the first took
8 ns
and the second took
4 ns
.
Our benchmark ends up being dominated by the cost of the split-load or the lack of memory alignment, in other words.
Cost of Branching
#
The
if
statement and seemingly innocent ternary operator
(condition ? a : b)
can have a high-performance impact.
It’s especially noticeable when conditional execution happens at the scale of single bytes, like in text processing, parsing, search, compression, encoding, etc.
Don’t forget that every
for
statement is, in reality, just a combination of an
if
and
goto
.
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
uint64_t
checksum
=
0
;
for
(
size_t
i
=
0
;
i
!=
string
.
size
();
++
i
)
checksum
+=
string
[
i
];
// Is identical to:
uint64_t
checksum
=
0
;
size_t
i
=
0
;
checksum_iteration
:
if
(
i
!=
string
.
size
())
{
checksum
+=
string
[
i
];
++
i
;
goto
checksum_iteration
;
}
The CPU has a
branch-predictor
, one of the silicon’s most complex parts.
It memorizes the most common
if
statements to allow “speculative execution”.
In other words, start processing the job
i + 1
before finishing the job
i
.
Those branch predictors are very powerful, and if you have a single
if
statement on your hot-path, it’s not a big deal.
But most modern programs are almost entirely built on
if
statements.
To estimate the cost of those, let’s generate some
random_values
, iterate through them and pick different branches depending on the value of
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
static
void
cost_of_branching_for_different_depth
(
bm
::
State
&
state
)
{
auto
count
=
static_cast
<
size_t
>
(
state
.
range
(
0
));
std
::
vector
<
int32_t
>
random_values
(
count
);
std
::
generate_n
(
random_values
.
begin
(),
random_values
.
size
(),
&
std
::
rand
);
int32_t
variable
=
0
;
size_t
iteration
=
0
;
for
(
auto
_
:
state
)
{
// Loop around to avoid out-of-bound access.
// For power-of-two sizes of `random_values` the `(++iteration) & (count - 1)`
// is identical to `(++iteration) % count`.
int32_t
random
=
random_values
[(
++
iteration
)
&
(
count
-
1
)];
bm
::
DoNotOptimize
(
variable
=
(
random
&
1
)
?
(
variable
+
random
)
:
(
variable
*
random
));
}
}
BENCHMARK
(
cost_of_branching_for_different_depth
)
->
RangeMultiplier
(
4
)
->
Range
(
256
,
32
*
1024
);
Up to 4096 branches will be memorized on most modern CPUs, but anything beyond that would work slower.
Running the benchmark, I end up with
2.9 ns vs. 0.7 ns
, so on average, 10 cycles are wasted when you have 2 random branches.
This means the cost of branch mis-prediction is around 20 CPU cycles.
Advanced Google Benchmark Features
#
GB packs a lot of little-known functionality.
Let’s take a more complex workload to understand it - sorting.
What’s wrong with the following benchmark?
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
static
void
sorting
(
bm
::
State
&
state
)
{
auto
count
=
static_cast
<
size_t
>
(
state
.
range
(
0
));
auto
include_preprocessing
=
static_cast
<
bool
>
(
state
.
range
(
1
));
std
::
vector
<
int32_t
>
array
(
count
);
std
::
iota
(
array
.
begin
(),
array
.
end
(),
1
);
for
(
auto
_
:
state
)
{
if
(
!
include_preprocessing
)
state
.
PauseTiming
();
// Reverse order is the most classical worst case,
// but not the only one.
std
::
reverse
(
array
.
begin
(),
array
.
end
());
if
(
!
include_preprocessing
)
state
.
ResumeTiming
();
std
::
sort
(
array
.
begin
(),
array
.
end
());
bm
::
DoNotOptimize
(
array
.
size
());
}
}
BENCHMARK
(
sorting
)
->
Args
({
3
,
false
})
->
Args
({
3
,
true
});
BENCHMARK
(
sorting
)
->
Args
({
4
,
false
})
->
Args
({
4
,
true
});
We are benchmarking the
std::sort
, the most used
<algorithm>
.
Array sizes are fixed at 3 and 4 elements in different benchmarks.
Each runs twice:
with
std::reverse
preprocessing time
included
.
with
std::reverse
preprocessing time
excluded
.
One took
227 ns
and another took
9 ns
.
Which is which?
The answer is different from what common sense suggests.
The Cost of Timing in Google Benchmark
#
Aside from the primary operation in question -
std::sort
, we also do some pre-processing.
That pre-processing code is isolated with
state.*Timing()
functions, and often, people use those without realizing the actual cost.
1
2
3
4
5
6
7
8
9
static
void
upper_cost_of_pausing
(
bm
::
State
&
state
)
{
int32_t
a
=
std
::
rand
(),
c
=
0
;
for
(
auto
_
:
state
)
{
state
.
PauseTiming
();
++
a
;
state
.
ResumeTiming
();
bm
::
DoNotOptimize
(
c
+=
a
);
}
}
This took
213 ns
.
Those things look tiny when processing gigabytes, but you will run your benchmark on a small input one day.
Plan ahead to extract an unaffected asymptotic curve, as we will do later.
Asymptotic Complexity and Sorting
#
GB also packs functionality for complexity analysis.
Those come in handy when you analyze scaling.
Most of us assume that
std::sort
uses
Quicksort
, at least for significant inputs.
But what if the input is ginormous?
There is the
Parallel STL
!
In GCC, those procedures are directed towards
Intel’s oneTBB
, which will use many threads to sort your numbers.
The underlying algorithm would almost certainly be a linear-time Radix sort on GPUs.
But what’s the complexity of oneTBB’s implementation on the CPU?
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
template
<
typename
execution_policy_t
>
static
void
super_sort
(
bm
::
State
&
state
,
execution_policy_t
&&
policy
)
{
auto
count
=
static_cast
<
size_t
>
(
state
.
range
(
0
));
std
::
vector
<
int32_t
>
array
(
count
);
std
::
iota
(
array
.
begin
(),
array
.
end
(),
1
);
for
(
auto
_
:
state
)
{
std
::
reverse
(
policy
,
array
.
begin
(),
array
.
end
());
std
::
sort
(
policy
,
array
.
begin
(),
array
.
end
());
bm
::
DoNotOptimize
(
array
.
size
());
}
state
.
SetComplexityN
(
count
);
state
.
SetItemsProcessed
(
count
*
state
.
iterations
());
state
.
SetBytesProcessed
(
count
*
state
.
iterations
()
*
sizeof
(
int32_t
));
}
This short benchmark logs more information than just the runtime per iteration.
Aside from the built-in
SetItemsProcessed
and
SetBytesProcessed
you can add anything else:
1
state
.
counters
[
"temperature_on_mars"
]
=
bm
::
Counter
(
-
95.4
);
I then run this benchmark with a couple of different policies and on numerous sizes:
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
BENCHMARK_CAPTURE
(
super_sort
,
seq
,
std
::
execution
::
seq
)
->
RangeMultiplier
(
8
)
->
Range
(
1l
<<
20
,
1l
<<
32
)
->
MinTime
(
10
)
->
Complexity
(
bm
::
oNLogN
);
BENCHMARK_CAPTURE
(
super_sort
,
par_unseq
,
std
::
execution
::
par_unseq
)
->
RangeMultiplier
(
8
)
->
Range
(
1l
<<
20
,
1l
<<
32
)
->
MinTime
(
10
)
->
Complexity
(
bm
::
oNLogN
);
GB will take the heavy burden of fitting and comparing our results against the suggested complexity curve.
From those experiments,
NlgN
fits best, as seen in the output.
Algorithm
Result
super_sort/seq/1048576/min_time:10.000
…
super_sort/seq/2097152/min_time:10.000
…
super_sort/seq/16777216/min_time:10.000
…
super_sort/seq/134217728/min_time:10.000
…
super_sort/seq/1073741824/min_time:10.000
…
super_sort/seq/4294967296/min_time:10.000
…
super_sort/seq/min_time:10.000_BigO
1.78 NlgN
super_sort/seq/min_time:10.000_RMS
41 %
Another thing to note here is the missing
UseRealTime
.
Without it the “CPU Time” is used by default.
If you were to sleep your process, the “CPU Time” would stop growing.
Random Interleaving
#
GB provides Random Interleaving for benchmarks with high run-to-run or order-depend variance.
To enable it:
pass the
--benchmark_enable_random_interleaving=true
flag,
optionally specify non-zero repetition count
--benchmark_repetitions=1
,
optionally decrease the per-repetition time
--benchmark_min_time=0.1
.
In a few cases, enabling this flag will save you some pain.
One example is when dealing with CPUs with variable frequency with “Turbo Boost” like features that scale CPU frequency to a higher license.
In that such case your CPU may accelerate from 2 GHz to 3 GHz, but will only sustain that frequency for a few seconds.
So, if you run multiple compute-heavy benchmarks, the first one will work better, and the rest will work worse.
Another scenario is when you are working with large static arrays of data preserved from benchmark to benchmark; the first one will be slow, and the others will be fast if the data has been cached in the CPU.
Hardware Performance Counters
#
Most chips, including CPUs, include hardware performance counters.
Those gather stats that your benchmarking toolkit may be able to collect.
In GB
, those counters are implemented via
libpmf
(PMF).
PMF, however, is only available on Linux, and only some kernels support it.
“Windows Subsystem for Linux” users are out of luck, but if you are running on an original kernel, it will only take one extra argument and
sudo
privileges to access:
1
$ sudo ./build_release/tutorial --benchmark_perf_counters
=
"CYCLES,INSTRUCTIONS"
More often, however, I’d see people call GB through the infamous Linux
perf
utility.
It will expose a lot more functionality, such as
taskset
, to control the availability of different CPU cores.
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
$ sudo perf stat taskset 0xEFFFEFFFEFFFEFFFEFFFEFFFEFFFEFFF ./build_release/tutorial --benchmark_filter
=
super_sort
Performance counter stats
for
'taskset 0xEFFFEFFFEFFFEFFFEFFFEFFFEFFFEFFF ./build_release/tutorial --benchmark_filter=super_sort'
:
23048674.55 msec task-clock
#   35.901 CPUs utilized
6627669
context-switches
#    0.288 K/sec
75843
cpu-migrations
#    0.003 K/sec
119085703
page-faults
#    0.005 M/sec
91429892293048
cycles
#    3.967 GHz                      (83.33%)
13895432483288
stalled-cycles-frontend
#   15.20% frontend cycles idle     (83.33%)
3277370121317
stalled-cycles-backend
#    3.58% backend cycles idle      (83.33%)
16689799241313
instructions
#    0.18  insn per cycle
#    0.83  stalled cycles per insn  (83.33%)
3413731599819
branches
#  148.110 M/sec                    (83.33%)
11861890556
branch-misses
#    0.35% of all branches          (83.34%)
642.008618457 seconds
time
elapsed
21779.611381000 seconds user
1244.984080000 seconds sys
In Closing
#
GB has a lot of functionality we haven’t touched, which is listed in their
single-page user guide
.
You can take all the discussed codes from this article
on GitHub
and extend them to include more functionality, but that’s just the peak of the iceberg.
We haven’t touched on system calls and communications with external devices, where you would need
eBPF
to effectively trace calls from almost inside the kernel.
If you want to go deeper, check out the following repos I maintain 🤗
