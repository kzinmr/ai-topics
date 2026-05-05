---
title: "NumPy vs BLAS: Losing 90% of Throughput"
url: "https://ashvardanian.com/posts/numpy-vs-blas-costs/"
fetched_at: 2026-05-05T07:01:50.440579+00:00
source: "Ash Vardanyan"
tags: [blog, raw]
---

# NumPy vs BLAS: Losing 90% of Throughput

Source: https://ashvardanian.com/posts/numpy-vs-blas-costs/

Downloaded over 5 Billion times
, NumPy is the most popular library for numerical computing in Python.
It wraps low-level HPC libraries like BLAS and LAPACK, providing a high-level interface for matrix operations.
BLAS is mainly implemented in C, Fortran, or Assembly and is available for most modern chips, not just CPUs.
BLAS is fast, but bindings aren’t generally free.
So, how much of the BLAS performance is NumPy leaving on the table?
TLDR:
up to 90% of throughput is lost
on 1536-dimensional OpenAI Ada embeddings, more on shorter vectors.
SimSIMD
can fix that, at least partly.
We aren’t going to cover the basics of NumPy or BLAS.
We won’t cover BLAS level 2 or 3 for vector-matrix and matrix-matrix operations, only level 1 vector-vector dot-products.
We have already shown how
pure Assembly dot-products can be over 2,000x faster than Python
.
We have also demonstrated how
bindings across 10 programming languages work
.
Instead, let’s jump into benchmark results.
Baseline Benchmarks
#
I wrote
2 benchmark scripts
:
one in Python
and
one in C++
using
Google Benchmark
.
In short, we are benchmarking the following interfaces against their BLAS counterparts:
1
2
3
4
5
6
7
8
9
import
numpy
as
np
a
=
np
.
random
.
rand
(
1536
)
b
=
np
.
random
.
rand
(
1536
)
np
.
dot
(
a
.
astype
(
np
.
float64
),
b
.
astype
(
np
.
float64
))
# cblas_ddot
np
.
dot
(
a
.
astype
(
np
.
float32
),
b
.
astype
(
np
.
float32
))
# cblas_sdot
np
.
dot
(
a
.
astype
(
np
.
float16
),
b
.
astype
(
np
.
float16
))
# no analog
np
.
dot
(
a
.
astype
(
np
.
float64
)
.
view
(
np
.
complex128
),
b
.
astype
(
np
.
float64
)
.
view
(
np
.
complex128
))
# cblas_zdotu_sub
np
.
dot
(
a
.
astype
(
np
.
float32
)
.
view
(
np
.
complex64
),
b
.
astype
(
np
.
float32
)
.
view
(
np
.
complex64
))
# cblas_cdotu_sub
They directly compare NumPy’s default PyPi distribution with the same underlying OpenBLAS library used from the C layer.
For profiling, I chose the
c7g
instances on AWS, powered by Arm-based Graviton 3 CPUs with Scalable Vector Extensions (SVE) - variable-width SIMD Assembly instructions - my favorite example of convergence between CPUs and GPUs.
AWS Graviton 3 CPUs are an excellent baseline for the new wave of energy-efficient supercomputers and clouds.
Arm also powers
Fugaku
, the fastest supercomputer until 2022, which also supports SVE.
Nvidia Grace CPUs are also based on Arm,
Neoverse N2
cores to be precise.
They also support SVE instructions and already power
Isambard 3
supercomputer in Bristol, one of the greenest in the world.
Similarly, Microsoft Azure is rolling out its Cobalt CPUs, and the
Ampere One
is gaining adoption.
Numeric Type
OpenBLAS in C
OpenBLAS in NumPy
Slowdown
float64
¹⁵³⁶
1,693 K
479 K
3.53 x
float32
¹⁵³⁶
6,568 K
752 K
8.73 x
float16
¹⁵³⁶
_
173 K
-
complex128
⁷⁶⁸
1,706 K
469 K
3.64 x
complex64
⁷⁶⁸
2,980 K
632 K
4.71 x
complex32
⁷⁶⁸
-
-
-
The benchmarks were run on a single thread, resulting in dot-product operations per second.
In this case, NumPy is 3.53x to 8.73x slower than the underlying BLAS library for 1536-dimensional real and 768-dimensional complex vectors.
The smaller you make the vectors, the more significant the slowdown.
The slowdown comes from multiple sources:
Dynamic dispatch - as Python is a dynamic language, locating the dot symbol may involve several lookup tables and function calls,
Type checking - as Python is a dynamically typed language, the native implementation of dot must check the argument types, check if they are compatible,
Memory allocations - NumPy has to allocate memory for the result and then free it.
We can partly mitigate that.
SimSIMD
#
In the v4 release of SimSIMD, I’ve added complex dot products.
SimSIMD now also supports half-precision complex numbers,
not supported by NumPy
or most BLAS implementations, but
considered for CuPy
.
Looking at hardware-accelerated dot-products specifically, this is how SimSIMD and NumPy compare in terms of functionality:
NumPy
SimSIMD
Real Types
float16
,
float32
,
float64
float16
,
float32
,
float64
Complex Types
complex64
,
complex128
complex32
,
complex64
,
complex128
Backends
Come from BLAS
NEON, SVE, Haswell, Skylake, Ice Lake, Sapphire Rapids
Compatibility
35 wheels on
PyPi
105 wheels on
PyPi
The library also contains
benchmarks against OpenBLAS
, which I’ve used in this article.
First, I’ve profiled the C layer, looking for ways to supersede OpenBLAS and comparing auto-vectorization with explicit SIMD kernels.
Numeric Type
OpenBLAS in C
Serial C Code
SimSIMD in C
Improvement
float64
¹⁵³⁶
1,693 K
861 K
2,944 K
+ 73.9 %
float32
¹⁵³⁶
6,568 K
1,248 K
5,464 K
- 16.8 %
float16
¹⁵³⁶
_
845 K
10,500 K
complex128
⁷⁶⁸
1,706 K
1.264 K
2,061 K
+ 20.8 %
complex64
⁷⁶⁸
2,980 K
1,335 K
3,960 K
+ 32.9 %
complex32
⁷⁶⁸
-
881 K
7,138 K
The comparison wasn’t possible for half-precision representations.
In the remaining 4 cases, SimSIMD won 3 times and lost once.
Patches for the lost case are more than welcome 🤗
Putting all together, this is how SimSIMD and NumPy compare when used in Python:
Numeric Type
NumPy in Python
SimSIMD in Python
Improvement
float64
¹⁵³⁶
479 K
753 K
+ 57.2 %
float32
¹⁵³⁶
752 K
1,215 K
+ 61.6 %
float16
¹⁵³⁶
173 K
1,484 K
+ 757.8 %
complex128
⁷⁶⁸
469 K
737 K
+ 57.1 %
complex64
⁷⁶⁸
632 K
1,011 K
+ 60.0 %
complex32
⁷⁶⁸
-
1,173 K
In all cases but one, the SimSIMD improvements over NumPy can be attributed to the quality of the binding layer, the BLAS wasn’t the bottleneck.
NumPy could have been just as fast as SimSIMD, if it had a better binding layer.
In half-precision, however, the NumPy doesn’t call BLAS, and as a result, it’s 8x slower than SimSIMD.
Assuming how often
numpy.inner
,
numpy.dot
, and
numpy.vdot
are used, I’ll call this a win.
So if you want to make your pipelines -
pip install simsimd
😉
Replicating the Results
#
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
# Clone the repos and install BLAS
$ sudo apt install libopenblas-dev
$ git clone https://github.com/ashvardanian/SimSIMD.git
$
cd
SimSIMD
# To run C benchmarks for dot products
$ cmake -DCMAKE_BUILD_TYPE
=
Release -DSIMSIMD_BUILD_BENCHMARKS
=
1
-B build_release
$ cmake --build build_release --config Release
$ build_release/simsimd_bench --benchmark_filter
=
"dot.*(serial|blas|sve)"
# To run Python benchmarks
$ pip install numpy scipy scikit-learn
$ python python/bench.py
Appending 1: C++ Benchmark Logs
#
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
37
38
39
40
41
42
43
- Arm NEON support enabled:
true
- Arm SVE support enabled:
true
- x86 Haswell support enabled:
false
- x86 Skylake support enabled:
false
- x86 Ice Lake support enabled:
false
- x86 Sapphire Rapids support enabled:
false
- Compiler supports F16:
true
- Benchmark against CBLAS:
true
2024-03-13T05:58:15+00:00
Running build_release/simsimd_bench
Run on
(
4
X
2100
MHz CPU s
)
CPU Caches:
L1 Data
64
KiB
(
x4
)
L1 Instruction
64
KiB
(
x4
)
L2 Unified
1024
KiB
(
x4
)
L3 Unified
32768
KiB
(
x1
)
Load Average: 0.12, 0.23, 0.31
***WARNING*** Library was built as DEBUG. Timings may be affected.
----------------------------------------------------------------------------------------------------------
Benchmark                                                Time             CPU   Iterations UserCounters...
----------------------------------------------------------------------------------------------------------
dot_f32_blas_1536d/min_time:10.000/threads:4          38.2 ns
152
ns
91962500
abs_delta
=
0
bytes
=
80.7067G/s
pairs
=
6.56793M/s
relative_error
=
0
dot_f64_blas_1536d/min_time:10.000/threads:4
149
ns
590
ns
23714404
abs_delta
=
0
bytes
=
41.6305G/s
pairs
=
1.69395M/s
relative_error
=
0
dot_f32c_blas_1536d/min_time:10.000/threads:4         84.0 ns
336
ns
41723636
abs_delta
=
0
bytes
=
36.6258G/s
pairs
=
2.98061M/s
relative_error
=
0
dot_f64c_blas_1536d/min_time:10.000/threads:4
147
ns
586
ns
23884736
abs_delta
=
0
bytes
=
41.9479G/s
pairs
=
1.70687M/s
relative_error
=
0
vdot_f32c_blas_1536d/min_time:10.000/threads:4        84.1 ns
336
ns
41718708
abs_delta
=
0
bytes
=
36.6236G/s
pairs
=
2.98043M/s
relative_error
=
0
vdot_f64c_blas_1536d/min_time:10.000/threads:4
147
ns
586
ns
23895620
abs_delta
=
0
bytes
=
41.9427G/s
pairs
=
1.70665M/s
relative_error
=
0
dot_f16_sve_1536d/min_time:10.000/threads:4           23.9 ns         95.2 ns
146982384
abs_delta
=
119.209u
bytes
=
64.5152G/s
pairs
=
10.5005M/s
relative_error
=
158.405u
dot_f32_sve_1536d/min_time:10.000/threads:4           45.9 ns
183
ns
76501512
abs_delta
=
0
bytes
=
67.1458G/s
pairs
=
5.46434M/s
relative_error
=
0
dot_f64_sve_1536d/min_time:10.000/threads:4           85.0 ns
340
ns
41207148
abs_delta
=
0
bytes
=
72.3747G/s
pairs
=
2.94493M/s
relative_error
=
0
dot_f16c_sve_1536d/min_time:10.000/threads:4          35.1 ns
140
ns
99915388
abs_delta
=
817.418u
bytes
=
43.8583G/s
pairs
=
7.1384M/s
relative_error
=
1094.91u
vdot_f16c_sve_1536d/min_time:10.000/threads:4         35.1 ns
140
ns
99876424
abs_delta
=
446.2u
bytes
=
43.915G/s
pairs
=
7.14763M/s
relative_error
=
609.749u
dot_f32c_sve_1536d/min_time:10.000/threads:4          63.2 ns
253
ns
55436532
abs_delta
=
0
bytes
=
48.6621G/s
pairs
=
3.96013M/s
relative_error
=
0
vdot_f32c_sve_1536d/min_time:10.000/threads:4         63.1 ns
252
ns
55614928
abs_delta
=
0
bytes
=
48.8208G/s
pairs
=
3.97305M/s
relative_error
=
0
dot_f64c_sve_1536d/min_time:10.000/threads:4
122
ns
485
ns
28866668
abs_delta
=
0
bytes
=
50.6679G/s
pairs
=
2.06168M/s
relative_error
=
0
vdot_f64c_sve_1536d/min_time:10.000/threads:4
122
ns
485
ns
28876568
abs_delta
=
0
bytes
=
50.686G/s
pairs
=
2.06242M/s
relative_error
=
0
dot_f16_serial_1536d/min_time:10.000/threads:4
297
ns
1183
ns
11832888
abs_delta
=
0
bytes
=
5.19258G/s
pairs
=
845.147k/s
relative_error
=
0
dot_f32_serial_1536d/min_time:10.000/threads:4
201
ns
801
ns
17471224
abs_delta
=
0
bytes
=
15.3362G/s
pairs
=
1.24806M/s
relative_error
=
0
dot_f64_serial_1536d/min_time:10.000/threads:4
291
ns
1161
ns
12059628
abs_delta
=
0
bytes
=
21.1718G/s
pairs
=
861.482k/s
relative_error
=
0
dot_f64c_serial_1536d/min_time:10.000/threads:4
198
ns
791
ns
17704468
abs_delta
=
0
bytes
=
31.0815G/s
pairs
=
1.26471M/s
relative_error
=
0
dot_f32c_serial_1536d/min_time:10.000/threads:4
187
ns
749
ns
18696188
abs_delta
=
0
bytes
=
16.4102G/s
pairs
=
1.33546M/s
relative_error
=
0
dot_f16c_serial_1536d/min_time:10.000/threads:4
284
ns
1135
ns
12337624
abs_delta
=
0
bytes
=
5.41538G/s
pairs
=
881.409k/s
relative_error
=
0
Appending 2: Python Benchmark Logs
#
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
- Vector dimensions:
1536
- Vectors count:
1000
- Hardware capabilities: serial, neon, sve
- SimSIMD version: 4.0.0
- SciPy version: 1.11.3
- scikit-learn version: 1.4.1.post1
- NumPy version: 1.26.0
-- NumPy BLAS dependency: openblas64
-- NumPy LAPACK dependency: openblas64
|
Datatype
|
Method
|
Ops/s
|
SimSIMD Ops/s
|
SimSIMD Improvement
|
|
:-------
|
:--------------------
|
------:
|
------------:
|
------------------:
|
|
`
f64
`
|
`
scipy.cosine
`
|
40,362
|
690,516
|
17.11 x
|
|
`
f32
`
|
`
scipy.cosine
`
|
31,097
|
1,138,570
|
36.61 x
|
|
`
f16
`
|
`
scipy.cosine
`
|
14,631
|
1,393,120
|
95.21 x
|
|
`
i8
`
|
`
scipy.cosine
`
|
39,489
|
1,473,040
|
37.30 x
|
|
`
f64
`
|
`
scipy.sqeuclidean
`
|
154,574
|
718,487
|
4.65 x
|
|
`
f32
`
|
`
scipy.sqeuclidean
`
|
176,013
|
1,180,098
|
6.70 x
|
|
`
f16
`
|
`
scipy.sqeuclidean
`
|
47,537
|
1,411,140
|
29.69 x
|
|
`
i8
`
|
`
scipy.sqeuclidean
`
|
121,854
|
1,416,866
|
11.63 x
|
|
`
f64
`
|
`
numpy.dot
`
|
478,866
|
752,517
|
1.57 x
|
|
`
f32
`
|
`
numpy.dot
`
|
752,299
|
1,214,928
|
1.61 x
|
|
`
f16
`
|
`
numpy.dot
`
|
172,994
|
1,484,285
|
8.58 x
|
|
`
i8
`
|
`
numpy.dot
`
|
511,496
|
1,571,563
|
3.07 x
|
|
`
f32c
`
|
`
numpy.dot
`
|
631,648
|
1,010,783
|
1.60 x
|
|
`
f64c
`
|
`
numpy.dot
`
|
468,782
|
737,116
|
1.57 x
|
|
`
f32c
`
|
`
numpy.vdot
`
|
610,647
|
1,032,112
|
1.69 x
|
|
`
f64c
`
|
`
numpy.vdot
`
|
437,204
|
749,826
|
1.72 x
|
|
`
f64
`
|
`
scipy.jensenshannon
`
|
15,597
|
38,129
|
2.44 x
|
|
`
f32
`
|
`
scipy.jensenshannon
`
|
15,436
|
234,427
|
15.19 x
|
|
`
f16
`
|
`
scipy.jensenshannon
`
|
8,381
|
213,824
|
25.51 x
|
|
`
f64
`
|
`
scipy.kl_div
`
|
49,725
|
61,399
|
1.23 x
|
|
`
f32
`
|
`
scipy.kl_div
`
|
47,714
|
464,078
|
9.73 x
|
|
`
f16
`
|
`
scipy.kl_div
`
|
36,418
|
422,291
|
11.60 x
|
|
`
b8
`
|
`
scipy.hamming
`
|
836,733
|
11,655,827
|
13.93 x
|
|
`
b8
`
|
`
scipy.jaccard
`
|
395,086
|
10,229,237
|
25.89 x
|
