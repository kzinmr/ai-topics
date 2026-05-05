---
title: "SciPy distances... up to 200x faster with AVX-512 & SVE 📏"
url: "https://ashvardanian.com/posts/simsimd-faster-scipy/"
fetched_at: 2026-05-05T07:01:51.368547+00:00
source: "Ash Vardanyan"
tags: [blog, raw]
---

# SciPy distances... up to 200x faster with AVX-512 & SVE 📏

Source: https://ashvardanian.com/posts/simsimd-faster-scipy/

Over the years, Intel’s 512-bit
Advanced Vector eXtensions
(AVX-512) stirred extensive discussions. While introduced in 2014, it wasn’t until recently that CPUs began providing comprehensive support. Similarly,
Arm Scalable Vector Extensions (SVE)
, primarily designed for Arm servers, have also started making waves only lately. The computing landscape now looks quite different with powerhouses like Intel’s
Sapphire Rapids
CPUs,
AWS Graviton 3
, and
Ampere Altra
entering the fray. Their arrival brings compelling advantages over the traditional AVX2 and NEON extensions:
These enhancements shine in the latest
SimSIMD release
.
This library now boasts:
Speeds up to 200x faster than SciPy and NumPy,
Compatibility with NEON, SVE, AVX2, and AVX-512 extensions,
Support for Inner Product, Euclidean, Angular, Hamming, Jaccard distances, and
Acceptance of
f32
,
f16
,
i8
, and binary vectors.
If this sparks your interest, go ahead and
pip install simsimd
. The library is available for both public and commercial projects under the Apache 2.0 license. For those keen on delving deeper into the mechanics behind these advancements, understanding how AVX-512 and SVE make SIMD code cleaner, and how the accelerate half-precision AI and Machine Learning workloads, continue reading!
Appendix contains
performance benchmarks
for:
Apple M2 Pro
4th Gen Intel Xeon Platinum (8480+)
AWS Graviton 3
“Tails of the past”: The Significance of Masked Loads
#
Think of NEON as a container that’s always 128 bits wide, while AVX is a wider container at 256 bits. But real-world data can come in all sorts of sizes, and this sometimes causes complications, especially when we’re not just working with standard math libraries.
For tasks like measuring the distance between dense data points, manually guiding the computer can be 2-5 times faster than letting it figure things out on its own.
For trickier tasks, like processing strings of text or handling varying bit rates, manually guiding can be even 20-50 times faster.
Now, with this in mind, you might expect to see a piece of code from
StringZilla
. But this isn’t just about speed—it’s also about writing neat and concise code. One thing that bothers me is splitting a piece of code into three parts because the data doesn’t fit perfectly.
However, if you’re not chasing the absolute best speed, you can simplify it to two parts. Just skip the beginning and use a more flexible approach in the main body of the code. With tools like NEON and AVX, making this kind of distance calculation might look like this:
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
__attribute__
((
target
(
"avx2,fma"
)))
simsimd_f32_t
simsimd_avx2_f32_l2sq
(
simsimd_f32_t
const
*
a
,
simsimd_f32_t
const
*
b
,
simsimd_size_t
n
)
{
__m256
d2_vec
=
_mm256_set1_ps
(
0
);
simsimd_size_t
i
=
0
;
for
(;
i
+
8
<=
n
;
i
+=
8
)
{
__m256
a_vec
=
_mm256_loadu_ps
(
a
+
i
);
__m256
b_vec
=
_mm256_loadu_ps
(
b
+
i
);
__m256
d_vec
=
_mm256_sub_ps
(
a_vec
,
b_vec
);
d2_vec
=
_mm256_fmadd_ps
(
d_vec
,
d_vec
,
d2_vec
);
}
d2_vec
=
_mm256_add_ps
(
_mm256_permute2f128_ps
(
d2_vec
,
d2_vec
,
1
),
d2_vec
);
d2_vec
=
_mm256_hadd_ps
(
d2_vec
,
d2_vec
);
d2_vec
=
_mm256_hadd_ps
(
d2_vec
,
d2_vec
);
simsimd_f32_t
result
[
1
];
_mm_store_ss
(
result
,
_mm256_castps256_ps128
(
d2_vec
));
// Accumulate the tail:
for
(;
i
<
n
;
++
i
)
result
[
0
]
+=
(
a
[
i
]
-
b
[
i
])
*
(
a
[
i
]
-
b
[
i
]);
return
result
[
0
];
}
To avoid doing the tail, you can use the
_mm256_maskload_ps
for masking, but it’s only available for 32 and 64-bit entries. Now, here’s where AVX-512 makes things better. It can handle uneven data sizes more gracefully, so we can get rid of the “tail” for
f32
,
f16
,
i8
, and other data types.
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
__attribute__
((
target
(
"avx512f,avx512vl"
)))
simsimd_f32_t
simsimd_avx512_f32_l2sq
(
simsimd_f32_t
const
*
a
,
simsimd_f32_t
const
*
b
,
simsimd_size_t
n
)
{
__m512
d2_vec
=
_mm512_set1_ps
(
0
);
for
(
simsimd_size_t
i
=
0
;
i
<
n
;
i
+=
16
)
{
__mmask16
mask
=
n
-
i
>=
16
?
0xFFFF
:
((
1u
<<
(
n
-
i
))
-
1u
);
__m512
a_vec
=
_mm512_maskz_loadu_ps
(
mask
,
a
+
i
);
__m512
b_vec
=
_mm512_maskz_loadu_ps
(
mask
,
b
+
i
);
__m512
d_vec
=
_mm512_sub_ps
(
a_vec
,
b_vec
);
d2_vec
=
_mm512_fmadd_ps
(
d_vec
,
d_vec
,
d2_vec
);
}
return
_mm512_reduce_add_ps
(
d2_vec
);
}
For 1535-dimensional OpenAI Ada embeddings on Intel Xeon Platinum 8480+ the
performance get’s 84% better
:
AVX2: 3.3 Million ops/s, same as auto-vectorized code.
AVX-512: 6.1 Million ops/s.
Another neat idea is to swap out some
_mm512_maskz_loadu_ps
instructions in the code for better-aligned ones, like
_mm512_maskz_load_ps
. But this doesn’t always work, especially with tools like SVE, which handle things differently. You will often see intrinsics like
svwhilelt
and
svcnt
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
__attribute__
((
target
(
"+sve"
)))
simsimd_f32_t
simsimd_sve_f32_l2sq
(
simsimd_f32_t
const
*
a
,
simsimd_f32_t
const
*
b
,
simsimd_size_t
n
)
{
simsimd_size_t
i
=
0
;
svfloat32_t
d2_vec
=
svdupq_n_f32
(
0.f
,
0.f
,
0.f
,
0.f
);
do
{
svbool_t
pg_vec
=
svwhilelt_b32
((
unsigned
int
)
i
,
(
unsigned
int
)
n
);
svfloat32_t
a_vec
=
svld1_f32
(
pg_vec
,
a
+
i
);
svfloat32_t
b_vec
=
svld1_f32
(
pg_vec
,
b
+
i
);
svfloat32_t
d_vec
=
svsub_f32_x
(
pg_vec
,
a_vec
,
b_vec
);
d2_vec
=
svmla_f32_x
(
pg_vec
,
d2_vec
,
d_vec
,
d_vec
);
i
+=
svcntw
();
}
while
(
i
<
d
);
simsimd_f32_t
d2
=
svaddv_f32
(
svptrue_b32
(),
d2_vec
);
return
d2
;
}
For 1535-dimensional OpenAI Ada embeddings on AWS Graviton 3 the
performance get’s 43% better
:
NEON: 3.5 Million ops/s.
SVE: 5 Million ops/s.
To wrap it up, this might be a glimpse into the future of computing, where the lines between different types of computer brains—like CPUs and GPUs—start to blur. It’s more evident here than with other technologies we’ve seen in the past, like Intel Knights Landing lineup.
The Challenge of
f16
#
Half-precision math, represented as
_Float16
, has been part of the C standard since 2011. But even today, it’s tricky to get optimal performance. While compilers like GCC and Clang can work with
_Float16
or its variant
__fp16
, they often don’t vectorize it effectively. As a result, when you compile with options like
-O3
and
-ffast-math
, half-precision code tends to run about 10 times slower than its single-precision counterpart. Here’s a breakdown of some benchmarks:
1
2
3
4
5
6
7
8
9
------------------------------------------------------------------------------------------------------------
Benchmark
Time
CPU
Iterations
UserCounters
...
------------------------------------------------------------------------------------------------------------
avx2_f32_l2sq_1536d
/
min_time
:
10.000
/
threads
:
224
1.37
ns
306
ns
46795392
pairs
=
3.2643
M
/
s
avx2_f16_l2sq_1536d
/
min_time
:
10.000
/
threads
:
224
1.48
ns
329
ns
44446528
pairs
=
3.03545
M
/
s
avx512_f32_l2sq_1536d
/
min_time
:
10.000
/
threads
:
224
0.741
ns
166
ns
85654240
pairs
=
6.03806
M
/
s
avx512_f16_l2sq_1536d
/
min_time
:
10.000
/
threads
:
224
0.495
ns
111
ns
122070592
pairs
=
9.01289
M
/
s
auto_f32_l2sq_1536d
/
min_time
:
10.000
/
threads
:
224
1.45
ns
325
ns
50284192
pairs
=
3.08087
M
/
s
auto_f16_l2sq_1536d
/
min_time
:
10.000
/
threads
:
224
30.2
ns
6752
ns
1931328
pairs
=
148.094
k
/
s
In a table format for clarity:
auto-vectorization
AVX2 + F16C + FMA
AVX-512 FP16
f32
3.0 M
3.3 M
6.0 M
f16
148.0 K
3.0 M
9.0 M
Given AI’s increasing reliance on half-precision floats for most workloads, the lag in performance is concerning. Some vendors initially prioritized
bf16
support, offering a different balance between exponent and mantissa than the IEEE 754 16-bit
float
. However, 4th generation Intel Xeon now supports
bf16
and introduces mixed-precision fused-multiply-add instructions, streamlining most of the vectorized dot-product tasks.
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
__attribute__
((
target
(
"avx512fp16,avx512vl,avx512f"
)))
simsimd_f32_t
simsimd_avx512_f16_l2sq
(
simsimd_f16_t
const
*
a
,
simsimd_f16_t
const
*
b
,
simsimd_size_t
d
)
{
__m512h
d2_vec
=
_mm512_set1_ph
(
0
);
for
(
simsimd_size_t
i
=
0
;
i
<
d
;
i
+=
32
)
{
__mmask32
mask
=
d
-
i
>=
32
?
0xFFFFFFFF
:
((
1u
<<
(
d
-
i
))
-
1u
);
__m512i
a_vec
=
_mm512_maskz_loadu_epi16
(
mask
,
a
+
i
);
__m512i
b_vec
=
_mm512_maskz_loadu_epi16
(
mask
,
b
+
i
);
__m512h
d_vec
=
_mm512_sub_ph
(
_mm512_castsi512_ph
(
a_vec
),
_mm512_castsi512_ph
(
b_vec
));
d2_vec
=
_mm512_fmadd_ph
(
d_vec
,
d_vec
,
d2_vec
);
}
return
_mm512_reduce_add_ph
(
d2_vec
);
}
To maintain clarity in the demonstration, I’ve used a sequential
_mm512_reduce_add_ph
at the conclusion; yet, this choice doesn’t impede performance. These compelling results are set to be integrated into the forthcoming
USearch v3 release
, bolstering its reputation as the fastest Vector Search engine in the domain.
Bonus Section: Bypassing
sqrt
and LibC Dependencies!
#
One of the joys of library development is achieving independence from external dependencies. This means
total independence
, including from staples like LibC and the Standard Template Library of C++. In SimSIMD, I previously depended on just one header from LibC,
<math.h>
. Not anymore.
Originally, it was used for the angular distance computation given by
1 - ab / sqrtf(a2 * b2)
. A simple optimization for this is substituting with the renowned
rsqrt
bithack from Quake 3:
1
2
3
4
5
6
7
simsimd_f32_t
simsimd_approximate_inverse_square_root
(
simsimd_f32_t
number
)
{
simsimd_f32i32_t
conv
;
conv
.
f
=
number
;
conv
.
i
=
0x5F1FFFF9
-
(
conv
.
i
>>
1
);
conv
.
f
*=
0.703952253f
*
(
2.38924456f
-
number
*
conv
.
f
*
conv
.
f
);
return
conv
.
f
;
}
This hack is already a remarkable trick. However, not everyone is aware of alternative approaches, some of which offer improved computational steps or employ different magic numbers to enhance numerical stability. I opted for methods recommended by Jan Kadlec. To bolster numerical stability, consider:
1
2
3
1
-
ab
/
sqrt
(
a2
*
b2
);
1
-
ab
*
rsqrt
(
a2
*
b2
);
1
-
ab
*
rsqrt
(
a2
)
*
rsqrt
(
b2
);
Going further, modern CPUs furnish specialized instructions, and I’ve integrated several of these into SimSIMD. Some prominent examples are:
_mm_rsqrt_ss
for SSE.
_mm_mask_rsqrt14_pd
for AVX-512.
vrsqrte_f32
for NEON.
For those keen on eliminating the
<math.h>
dependency, these instructions are certainly worth exploring!
Benchmark Results
#
Methodology:
#
For Cosine, squared Euclidean, Hamming, and Jaccard distances, I employed specialized functions from the
scipy.spatial.distance
module of SciPy.
Inner Product distance calculations were performed directly using NumPy as
1 - np.inner(A, B)
.
cdist
Inner Product distance was computed with
1 - np.dot(A, B.T)
, translating directly into a BLAS
sgemm
call.
For batch processes where direct support from SciPy is absent, each row was looped using SciPy and NumPy.
For Cosine, squared Euclidean, and Inner Product 3 datatypes were benchmarked:
f32
,
f16
,
i8
.
For binary metrics the only datatype that makes sense is an 8-bit unsigned integer -
u8
.
Notably, there are two specific scenarios where SimSIMD doesn’t outshine:
Inner Product distance between pairwise rows in two matrices (expressed as
1 - np.dot(A, B.T)
)
: When matrices increase in size, effective caching is required to retain parts of the matrix on the CPU, circumventing frequent RAM fetches. While BLAS optimizes this, SimSIMD doesn’t and has no plans to.
Minimal operations on contemporary Intel CPUs involving only two vectors
: Despite bypassing heavy abstractions like
PyArg_ParseTuple
in the CPython binding, the performance is impacted due to a combination of substantial
type-checking and ancillary tasks between the API and its execution
. Potential optimization could arise from backend pre-selection upon module loading, saving it in a global variable, rather than the current approach of
verifying the
cpuid
for every interaction
.
In upcoming endeavors, I’ll delve into Intel’s Advanced Matrix eXtensions (AMX) and Arm’s Scalable Matrix Extensions (SME). These have already enhanced our
Unum’s UForm Transformer models
, trimming inference time to a mere 1.3 milliseconds on a Sapphire Rapids CPU. While these extensions are yet to be integrated into SimSIMD, I openly invite contributions. Excited to see your inputs! 🤗
Appendix 1: Performance on Apple M2 Pro
#
Between 2 Vectors, Batch Size: 1
#
Datatype
Method
Ops/s
SimSIMD Ops/s
SimSIMD Improvement
f32
scipy.cosine
67,352
1,559,963
23.16 x
f16
scipy.cosine
26,723
1,553,700
58.14 x
i8
scipy.cosine
78,937
3,259,101
41.29 x
f32
scipy.sqeuclidean
383,307
1,587,302
4.14 x
f16
scipy.sqeuclidean
89,709
1,567,298
17.47 x
i8
scipy.sqeuclidean
213,618
1,794,259
8.40 x
f32
numpy.inner
1,346,952
1,611,604
1.20 x
f16
numpy.inner
266,904
1,545,994
5.79 x
i8
numpy.inner
862,502
3,302,596
3.83 x
u8
scipy.hamming
1,632,432
27,874,556
17.08 x
u8
scipy.jaccard
1,180,928
24,515,213
20.76 x
Between 2 Vectors, Batch Size: 1,000
#
Datatype
Method
Ops/s
SimSIMD Ops/s
SimSIMD Improvement
f32
scipy.cosine
68,414
2,471,680
36.13 x
f16
scipy.cosine
27,964
2,470,154
88.33 x
i8
scipy.cosine
81,064
15,364,768
189.54 x
f32
scipy.sqeuclidean
415,326
2,462,800
5.93 x
f16
scipy.sqeuclidean
90,795
2,439,524
26.87 x
i8
scipy.sqeuclidean
203,094
4,144,373
20.41 x
f32
numpy.inner
1,590,667
2,535,124
1.59 x
f16
numpy.inner
268,583
2,505,481
9.33 x
i8
numpy.inner
914,879
16,985,118
18.57 x
u8
scipy.hamming
1,645,641
134,064,810
81.47 x
u8
scipy.jaccard
1,237,944
103,444,581
83.56 x
Between All Pairs of Vectors (
cdist
), Batch Size: 1,000
#
Datatype
Method
Ops/s
SimSIMD Ops/s
SimSIMD Improvement
f32
scipy.cosine
777,894
2,533,840
3.26 x
f16
scipy.cosine
776,171
2,480,454
3.20 x
i8
scipy.cosine
778,570
17,927,198
23.03 x
f32
scipy.sqeuclidean
2,349,645
2,569,746
1.09 x
f16
scipy.sqeuclidean
2,158,488
2,377,701
1.10 x
i8
scipy.sqeuclidean
2,091,610
4,118,384
1.97 x
f32
numpy.inner
21,854,341
2,092,590
0.10 x
f16
numpy.inner
304,646
2,423,802
7.96 x
i8
numpy.inner
1,819,572
17,014,688
9.35 x
u8
scipy.hamming
46,265,239
1,502,534,579
32.48 x
u8
scipy.jaccard
129,574,247
971,895,663
7.50 x
Appendix 2: Performance on 4th Gen Intel Xeon Platinum (8480+)
#
Between 2 Vectors, Batch Size: 1
#
Datatype
Method
Ops/s
SimSIMD Ops/s
SimSIMD Improvement
f32
scipy.cosine
57,346
224,148
3.91 x
f16
scipy.cosine
17,068
226,829
13.29 x
i8
scipy.cosine
71,983
234,372
3.26 x
f32
scipy.sqeuclidean
341,301
218,177
0.64 x
f16
scipy.sqeuclidean
37,076
229,565
6.19 x
i8
scipy.sqeuclidean
236,241
237,825
1.01 x
f32
numpy.inner
912,270
225,867
0.25 x
f16
numpy.inner
92,400
230,110
2.49 x
i8
numpy.inner
700,822
231,987
0.33 x
u8
scipy.hamming
1,586,149
1,875,391
1.18 x
u8
scipy.jaccard
1,083,886
1,871,898
1.73 x
Between 2 Vectors, Batch Size: 1,000
#
Datatype
Method
Ops/s
SimSIMD Ops/s
SimSIMD Improvement
f32
scipy.cosine
56,848
2,835,761
49.88 x
f16
scipy.cosine
17,125
4,144,457
242.01 x
i8
scipy.cosine
71,990
7,627,362
105.95 x
f32
scipy.sqeuclidean
370,555
2,817,710
7.60 x
f16
scipy.sqeuclidean
37,116
4,451,408
119.93 x
i8
scipy.sqeuclidean
224,866
10,432,198
46.39 x
f32
numpy.inner
910,884
2,814,501
3.09 x
f16
numpy.inner
91,347
4,728,760
51.77 x
i8
numpy.inner
700,576
7,347,589
10.49 x
u8
scipy.hamming
1,611,206
79,796,509
49.53 x
u8
scipy.jaccard
1,096,522
87,557,689
79.85 x
Between All Pairs of Vectors (
cdist
), Batch Size: 1,000
#
Datatype
Method
Ops/s
SimSIMD Ops/s
SimSIMD Improvement
f32
scipy.cosine
2,430,617
3,106,912
1.28 x
f16
scipy.cosine
2,272,228
4,304,768
1.89 x
i8
scipy.cosine
2,370,290
8,384,383
3.54 x
f32
scipy.sqeuclidean
2,226,342
5,505,910
2.47 x
f16
scipy.sqeuclidean
2,237,966
4,732,212
2.11 x
i8
scipy.sqeuclidean
2,234,063
13,029,101
5.83 x
f32
numpy.inner
175,492,443
4,984,406
0.03 x
f16
numpy.inner
106,677
5,048,223
47.32 x
i8
numpy.inner
1,807,566
8,257,849
4.57 x
u8
scipy.hamming
159,574,713
2,325,251,446
14.57 x
u8
scipy.jaccard
19,478,797
1,705,905,017
87.58 x
Appendix 3: Performance on AWS Graviton 3
#
Between 2 Vectors, Batch Size: 1
#
Datatype
Method
Ops/s
SimSIMD Ops/s
SimSIMD Improvement
f32
scipy.cosine
30,830
1,007,218
32.67 x
f16
scipy.cosine
14,683
1,055,420
71.88 x
i8
scipy.cosine
38,843
1,441,367
37.11 x
f32
scipy.sqeuclidean
173,800
1,076,601
6.19 x
f16
scipy.sqeuclidean
48,080
1,136,170
23.63 x
i8
scipy.sqeuclidean
120,281
1,371,827
11.41 x
f32
numpy.inner
642,658
1,103,082
1.72 x
f16
numpy.inner
171,904
1,078,110
6.27 x
i8
numpy.inner
459,605
1,438,284
3.13 x
u8
scipy.hamming
796,739
10,041,370
12.60 x
u8
scipy.jaccard
534,529
9,181,640
17.18 x
Between 2 Vectors, Batch Size: 1,000
#
Datatype
Method
Ops/s
SimSIMD Ops/s
SimSIMD Improvement
f32
scipy.cosine
31,162
2,692,131
86.39 x
f16
scipy.cosine
14,721
3,034,736
206.15 x
i8
scipy.cosine
38,837
10,442,992
268.89 x
f32
scipy.sqeuclidean
177,025
2,705,020
15.28 x
f16
scipy.sqeuclidean
50,164
3,151,582
62.83 x
i8
scipy.sqeuclidean
121,269
6,081,171
50.15 x
f32
numpy.inner
657,257
3,078,979
4.68 x
f16
numpy.inner
171,875
3,153,530
18.35 x
i8
numpy.inner
459,975
9,719,212
21.13 x
u8
scipy.hamming
845,629
46,755,187
55.29 x
u8
scipy.jaccard
546,286
30,730,463
56.25 x
Between All Pairs of Vectors (
cdist
), Batch Size: 1,000
#
Datatype
Method
Ops/s
SimSIMD Ops/s
SimSIMD Improvement
f32
scipy.cosine
1,570,730
3,066,406
1.95 x
f16
scipy.cosine
1,605,807
3,057,974
1.90 x
i8
scipy.cosine
1,590,897
14,750,039
9.27 x
f32
scipy.sqeuclidean
1,622,545
3,272,164
2.02 x
f16
scipy.sqeuclidean
1,578,548
3,178,287
2.01 x
i8
scipy.sqeuclidean
1,592,369
6,436,115
4.04 x
f32
numpy.inner
58,199,003
3,445,812
0.06 x
f16
numpy.inner
218,842
3,274,774
14.96 x
i8
numpy.inner
1,356,633
14,812,931
10.92 x
u8
scipy.hamming
78,713,290
579,018,344
7.36 x
u8
scipy.jaccard
34,455,520
318,356,871
9.24 x
