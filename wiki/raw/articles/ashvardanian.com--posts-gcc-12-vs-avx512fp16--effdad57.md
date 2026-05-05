---
title: "GCC Compiler vs Human - 119x Faster Assembly 💻🆚🧑‍💻"
url: "https://ashvardanian.com/posts/gcc-12-vs-avx512fp16/"
fetched_at: 2026-05-05T07:01:51.017178+00:00
source: "Ash Vardanyan"
tags: [blog, raw]
---

# GCC Compiler vs Human - 119x Faster Assembly 💻🆚🧑‍💻

Source: https://ashvardanian.com/posts/gcc-12-vs-avx512fp16/

When our Python code is too slow, like most others we switch to C and often get 100x speed boosts, just like when we
replaced SciPy distance computations with SimSIMD
. But imagine going 100x faster than C code!
It sounds crazy, especially for number-crunching tasks that are “data-parallel” and easy for compilers to optimize.
In such spots the compiler will typically “unroll” the loop, vectorize the code, and use SIMD instructions to process multiple data elements in parallel.
But I’ve found a simple case, where the
GNU C Compiler
(GCC 12) failed to do so, and lost to hand-written SIMD code by a factor of
119
.
Enough to make the friendly bull compiler cry.
For the curious, the code is already part of my
SimSIMD library on GitHub
, and to be fair, today, it’s unimaginable that a compiler can properly optimize high-level code choosing from thousands of complex Assembly instructions, same way as a human can. So let’s see how we’ve got to a two-orders-of-magnitude speedup.
Background
#
Continuing with my work on
USearch
and the core
SimSIMD
library, I’ve turned my attention to speeding up the
Jensen Shannon divergence
, a symmetric variant of the
Kullback-Leibler divergence
, popular in stats, bioinformatics and cheminformatics.
$$
JS(P, Q) = \frac{1}{2} D(P || M) + \frac{1}{2} D(Q || M)
$$
$$
M = \frac{1}{2}(P + Q), D(P || Q) = \sum P(i) \cdot \log \left( \frac{P(i)}{Q(i)} \right)
$$
It’s tougher to compute than the usual
Cosine Similarity
, mainly because it needs to crunch logarithms, which are pretty slow with
LibC’s
logf
and most other math libraries. So, I reworked the logarithm part and the rest of the code using
AVX-512 and AVX-512FP16 SIMD
goodies for Intel’s Sapphire Rapids 2022 CPUs.
Optimizations
#
Logarithm Computation
. Instead of using multiple bitwise operations, I now use
_mm512_getexp_ph
and
_mm512_getmant_ph
to pull out the exponent and the mantissa of the floating-point number, which makes things simpler. I’ve also brought in
Horner’s method
for the polynomial approximation.
Division Avoidance
. To skip over the slow division operations, I’ve used reciprocal approximations -
_mm512_rcp_ph
for half-precision and
_mm512_rcp14_ps
for single-precision. Found out
_mm512_rcp28_ps
wasn’t needed for this work.
Handling Zeros
. I’m using
_mm512_cmp_ph_mask
to create a mask for near-zero values, which avoids having to add a small “epsilon” to every component, making it cleaner and more accurate.
Parallel Accumulation
. I now accumulate $KL(P||Q)$ and $KL(Q||P)$ in different registers, and use
_mm512_maskz_fmadd_ph
to replace separate addition and multiplication operations, which makes the calculation more efficient.
Implementation
#
The basic Jensen Shannon divergence implementation in C 99 appears as follows:
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
inline
static
simsimd_f32_t
simsimd_serial_f32_js
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
simsimd_f32_t
sum_a
=
0
;
simsimd_f32_t
sum_b
=
0
;
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
++
)
{
simsimd_f32_t
m
=
(
a
[
i
]
+
b
[
i
])
*
0.5f
;
if
(
m
>
1e-6
f
)
{
sum_a
+=
a
[
i
]
*
logf
(
a
[
i
]
/
m
);
sum_b
+=
b
[
i
]
*
logf
(
b
[
i
]
/
m
);
}
}
return
0.5f
*
(
sum_a
+
sum_b
);
}
This is a straightforward implementation utilizing the
log2f
function from LibC. To enhance its speed, one approach is to eliminate the
if (m > 1e-6f)
branch which is there to prevent division by zero. Instead, we could add a small epsilon to every component:
1
2
3
simsimd_f32_t
m
=
(
a
[
i
]
+
b
[
i
])
*
0.5f
;
sum_a
+=
a
[
i
]
*
logf
((
a
[
i
]
+
1e-6
f
)
/
(
m
+
1e-6
f
));
sum_b
+=
b
[
i
]
*
logf
((
b
[
i
]
+
1e-6
f
)
/
(
m
+
1e-6
f
));
However, the AVX-512FP16 implementation that I ended up with is quite different:
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
__attribute__
((
target
(
"avx512f,avx512vl,avx512fp16"
)))
inline
static
simsimd_f32_t
simsimd_avx512_f16_js
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
n
)
{
__m512h
sum_a_vec
=
_mm512_set1_ph
((
_Float16
)
0
);
__m512h
sum_b_vec
=
_mm512_set1_ph
((
_Float16
)
0
);
__m512h
epsilon_vec
=
_mm512_set1_ph
((
_Float16
)
1e-6
f
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
32
)
{
// Masked loads prevent reading beyond array limits
__mmask32
mask
=
n
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
n
-
i
))
-
1u
);
__m512h
a_vec
=
_mm512_castsi512_ph
(
_mm512_maskz_loadu_epi16
(
mask
,
a
+
i
));
__m512h
b_vec
=
_mm512_castsi512_ph
(
_mm512_maskz_loadu_epi16
(
mask
,
b
+
i
));
__m512h
m_vec
=
_mm512_mul_ph
(
_mm512_add_ph
(
a_vec
,
b_vec
),
_mm512_set1_ph
((
_Float16
)
0.5f
));
// Masking helps sidestep division by zero issues later
__mmask32
nonzero_mask_a
=
_mm512_cmp_ph_mask
(
a_vec
,
epsilon_vec
,
_CMP_GE_OQ
);
__mmask32
nonzero_mask_b
=
_mm512_cmp_ph_mask
(
b_vec
,
epsilon_vec
,
_CMP_GE_OQ
);
__mmask32
nonzero_mask
=
nonzero_mask_a
&
nonzero_mask_b
&
mask
;
// Approximate the reciprocal of `m` to avoid two division operations
__m512h
m_recip_approx
=
_mm512_rcp_ph
(
m_vec
);
__m512h
ratio_a_vec
=
_mm512_mul_ph
(
a_vec
,
m_recip_approx
);
__m512h
ratio_b_vec
=
_mm512_mul_ph
(
b_vec
,
m_recip_approx
);
// Compute log2, adjusting with `loge(2)` to get the natural logarithm
__m512h
log_ratio_a_vec
=
simsimd_avx512_f16_log2
(
ratio_a_vec
);
__m512h
log_ratio_b_vec
=
simsimd_avx512_f16_log2
(
ratio_b_vec
);
// FMA boosts efficiency by replacing separate mul and add operations
sum_a_vec
=
_mm512_maskz_fmadd_ph
(
nonzero_mask
,
a_vec
,
log_ratio_a_vec
,
sum_a_vec
);
sum_b_vec
=
_mm512_maskz_fmadd_ph
(
nonzero_mask
,
b_vec
,
log_ratio_b_vec
,
sum_b_vec
);
}
simsimd_f32_t
log2_normalizer
=
0.693147181f
;
return
_mm512_reduce_add_ph
(
_mm512_add_ph
(
sum_a_vec
,
sum_b_vec
))
*
0.5f
*
log2_normalizer
;
}
This version leverages GCC attributes to ensure the compiler processes the AVX512-FP16 instructions, even on older CPUs. It calls the
simsimd_avx512_f16_log2
function, inlined below:
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
__attribute__
((
target
(
"avx512f,avx512vl,avx512fp16"
)))
inline
__m512h
simsimd_avx512_f16_log2
(
__m512h
x
)
{
// Extract the exponent and mantissa
__m512h
one
=
_mm512_set1_ph
((
_Float16
)
1
);
__m512h
e
=
_mm512_getexp_ph
(
x
);
__m512h
m
=
_mm512_getmant_ph
(
x
,
_MM_MANT_NORM_1_2
,
_MM_MANT_SIGN_src
);
// Compute the polynomial using Horner's method
__m512h
p
=
_mm512_set1_ph
((
_Float16
)
-
3.4436006e-2
f
);
p
=
_mm512_fmadd_ph
(
m
,
p
,
_mm512_set1_ph
((
_Float16
)
3.1821337e-1
f
));
p
=
_mm512_fmadd_ph
(
m
,
p
,
_mm512_set1_ph
((
_Float16
)
-
1.2315303f
));
p
=
_mm512_fmadd_ph
(
m
,
p
,
_mm512_set1_ph
((
_Float16
)
2.5988452f
));
p
=
_mm512_fmadd_ph
(
m
,
p
,
_mm512_set1_ph
((
_Float16
)
-
3.3241990f
));
p
=
_mm512_fmadd_ph
(
m
,
p
,
_mm512_set1_ph
((
_Float16
)
3.1157899f
));
return
_mm512_add_ph
(
_mm512_mul_ph
(
p
,
_mm512_sub_ph
(
m
,
one
)),
e
);
}
It computes the polynomial approximation of the logarithm, using Horner’s method, accumulating five components, and then adds the exponent back to the result.
Benchmarks
#
I carried out benchmarks at both Python and C++ layers, comparing auto-vectorization on GCC against our new implementation on an Intel Sapphire Rapids CPU on AWS.
The newest LTS Ubuntu version is 22.04, which comes with GCC 11 and doesn’t support AVX512-FP16 intrinsics. So I’ve further upgraded the compiler on the machine to GCC 12 and compiled it with
-O3
,
-march=native
, and
-ffast-math
flags.
Looking at the
logs from the Google Benchmark suite
, we see that the benchmark was executed on all cores of the 4-core instance, which might have tilted the scales in favor of the old non-vectorized solution, but the gap is still outrageous.
Single-Precision Math
:
Implementation
Pairs/s
Gigabytes/s
Speedup
Absolute Error
Relative Error
serial_f32_js_1536d
0.243 M/s
2.98 G/s
0
0
avx512_f32_js_1536d
1.127 M/s
13.84 G/s
4.64x
0.001
345u
Half-Precision Math
:
Implementation
Pairs/s
Gigabytes/s
Speedup
Absolute Error
Relative Error
serial_f16_js_1536d
0.018 M/s
0.11 G/s
0.123
0.035
avx2_f16_js_1536d
0.547 M/s
3.36 G/s
30.39x
0.011
0.003
avx512_f16_js_1536d
2.139 M/s
13.14 G/s
118.84x
0.070
0.020
Undoubtedly, the outcomes may fluctuate based on the vector size. Typically, I employ 1536 dimensions, which align with the size of OpenAI Ada embeddings, a standard in NLP tasks.
But the most interesting applications of JS divergence would be far from NLP - closer to natural sciences.
The application I am most excited about -
clustering of Billions of different protein sequences
without any Multiple Sequence Alignment procedures. Sounds interesting? Check out the clustering capabilities of
USearch
🤗
