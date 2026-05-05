---
title: "Faster practical modular inversion"
url: "https://purplesyringa.moe/blog/./faster-practical-modular-inversion/"
fetched_at: 2026-05-05T07:02:09.304969+00:00
source: "Alisa Sireneva (PurpleSyringa)"
tags: [blog, raw]
---

# Faster practical modular inversion

Source: https://purplesyringa.moe/blog/./faster-practical-modular-inversion/

Faster practical modular inversion
December 20, 2025
Hacker News
Last year,
Lemire wrote
about an optimized variation of
the Euclidean algorithm
for computing
the greatest common divisor
of two numbers, called
binary Euclidean algorithm
or
Stein’s algorithm
. It’s a best-of-class implementation, though it’s currently only used by libc++.
If you’re looking to contribute to OSS, that’s your cue.
The post also briefly mentions
the extended Euclidean algorithm
, a related algorithm most often used to compute the
modular multiplicative inverse
(given a remainder
a
and a modulus
m
, find
x
such that
a
⋅
x
mod
m
=
1
):
There is also a binary version of the extended Euclidean algorithm[,] although it is quite a bit more involved and it is not clear that it […] can be implemented at high speed, leveraging fast instructions, when working on integers that fit in general-purpose registers. […]
My implementation of the binary extended Euclidean algorithm is quite a bit slower and not recommended. I expect that it should be possible to optimize it further.
– Lemire
That’s a big shame, because the extended Euclidean algorithm can be optimized in a very similar manner, and the underlying ideas were described
in a 2020 paper
. It’s probably not well-known because the paper focuses on constant-time evaluation and long arithmetic, so people might have assumed it’s irrelevant.
I’m hoping to bring justice to the extended Stein’s algorithm with this post. I’ll cover how the algorithm works, its limitations, some optimizations compared to Pornin’s paper, and potential further improvements.
My implementation is
available on GitHub
as part of a Rust modular arithmetic library.
Disclaimer
The textbook algorithm can be used not only to compute inverses, but also to solve
linear Diophantine equations
. I will focus on the former in this post, since that’s where the optimizations shine at. I’ll briefly cover the general case at the end of the post.
I won’t make claims on exact performance, because something strange is going on with the Lemire’s benchmarking results and I don’t want to add to the mess. I’ve measured that my implementation of the algorithm is
1.3
–
2
times faster than the textbook implementation on average, even on M4, but you may see a completely different picture if your compiler produces slightly different codegen.
Lemire’s benchmark seems to be skewed by the choice of the compiler (GCC vs Clang), its version (Clang 18 vs Clang 21), optimization flags (
-O2
vs
-O3
), the microarchitecture (Haswell vs Ice Lake vs Zen 2), and minutiae of the benchmarking code. Results don’t make much sense mathematically and look disproportionately affected by microarchitectural conditions.
If you want to get the fastest implementation, I suggest you inspect the assembly more closely than me, because I have no idea what’s going on.
Nevertheless, here is some raw data for transparency. The benchmark measures the time per inversion (in ns), the cell format is “Stein’s algorithm / Euclidean algorithm”.
8 bits
16 bits
32 bits
64 bits
Haswell
11.38
/
19.21
(-41%)
17.48
/
33.96
(-49%)
29.76
/
61.69
(-52%)
67.18
/
152.19
(-56%)
Alder Lake
8.20
/
10.19
(-20%)
13.77
/
16.87
(-18%)
21.47
/
31.00
(-31%)
50.38
/
69.57
(-28%)
Zen 5
7.77
/
10.56
(-26%)
9.43
/
14.80
(-36%)
13.96
/
23.98
(-42%)
34.58
/
49.24
(-30%)
M1
14.58
/
13.05
(+12%)
11.48
/
18.63
(-38%)
19.74
/
35.47
(-44%)
43.14
/
71.14
(-39%)
M2
8.93
/
10.26
(-13%)
11.00
/
17.90
(-39%)
19.38
/
33.78
(-43%)
41.33
/
68.03
(-39%)
M4
5.28
/
8.60
(-39%)
8.07
/
14.77
(-45%)
13.63
/
28.05
(-51%)
28.68
/
56.22
(-49%)
Cortex-A72
29.80
/
33.48
(-11%)
38.30
/
49.36
(-22%)
61.28
/
83.63
(-27%)
162.55
/
151.77
(+7%)
Snapdragon 8 Gen 3
9.72
/
12.13
(-20%)
14.97
/
21.91
(-32%)
28.51
/
39.89
(-29%)
70.11
/
75.46
(-7%)
Kryo 485
15.08
/
19.36
(-22%)
21.54
/
30.41
(-29%)
33.63
/
50.96
(-34%)
90.32
/
94.76
(-5%)
GCD
Let’s start with the algorithm for computing the GCD of
a
and
b
. Suppose for now that
b
is odd. Here’s the core idea:
If
a
is divisible by
2
k
, this factor can be removed:
gcd
(
2
k
a
,
b
)
=
gcd
(
a
,
b
)
. This decreases the bit length of
a
by at least
1
, guaranteeing
𝒪
(
log
⁡
a
)
time complexity if we can apply this reduction consistently.
If both
a
and
b
are odd, rewriting
gcd
(
a
,
b
)
=
gcd
(
a
−
b
,
b
)
guarantees
a
′
=
a
−
b
will be even and reducible on the next iteration. To avoid negative integers, swap
a
and
b
if
a
<
b
beforehand; new
b
remains odd because
a
was odd.
The implementation is very short:
while
a !=
0
{
    a >>= a.
trailing_zeros
();
if
a < b {
        (a, b) = (b, a);
    }
    a -= b;
}
return
b;
If the initial
b
is not guaranteed to be odd, some adjustments are necessary:
let
shift
= (a | b).
trailing_zeros
(); 
b >>= b.
trailing_zeros
();
return
b << shift;
But for modular inversion, the modulus is usually odd, so I won’t dwell on this.
Optimizations
This covers the general structure of the algorithm, but some optimizations are crucial for getting good performance.
The conditional swap should be compiled to branchless code to avoid branch misprediction. Compiler hints like
__builtin_unpredictable
or
core::hint::select_unpredictable
may be useful.
The loop has a high latency because
trailing_zeros
,
>>=
,
if
, and
-=
are computed sequentially. But since
(-a).trailing_zeros() == a.trailing_zeros()
,
a.trailing_zeros()
can in principle be computed before the swap on the previous iteration:
let
mut
q
= a.
trailing_zeros
();
while
a !=
0
{
    a >>= q;
    q = (a - b).
trailing_zeros
();
if
a < b {
        (a, b) = (b - a, a);
    }
else
{
        (a, b) = (a - b, b);
    }
}
This brings the latency down to 3 operations:
>>=
;
a - b
and
b - a
computed in parallel;
trailing_zeros
and
if
computed in parallel. It also slightly increases the number of operations (computing
b - a
and
a - b
and only using one), but the tradeoff pays off.
Pay close attention to
trailing_zeros
if you’re implementing this in C. The algorithm can invoke it with a zero input on the last iteration. This is well-defined in Rust, which maps
0
to the bit width of the data type, but in C
__builtin_clz(0)
is UB. Use
__builtin_clzg
to avoid issues. In C++,
std::countr_zero(0)
is well-defined.
GCC
documents
__builtin_clz(0)
as having an “undefined result”, so I initially assumed it means an indeterminate value. In reality,
GCC maintainers consider it UB
and
LLVM documents it as UB
… but the optimizers seem to model it exactly like an indeterminate value? (e.g. LLVM considers
@llvm.cttz(0)
to produce
poison
) This is frankly ridiculous, someone do something about it.
Extending
You might be wondering how this algorithm is related to modular inversion.
The trick is to express the values of
a
and
b
at each point as weighted sums of the original
a
and
b
(denoted
a
0
,
b
0
) with some coefficients
k
i
,
l
i
:
If
a
0
is invertible modulo
b
0
, their GCD is
1
, and so at the end of the algorithm
b
=
1
. This gives us:
k
1
a
0
+
l
1
b
0
=
1
⟹
k
1
a
0
=
1
(
mod
b
0
)
That is,
k
1
is the inverse of
a
0
modulo
b
0
. So all we need to do is track the coefficients across iterations. We start with:
{
a
=
a
0
=
1
a
0
+
0
b
0
b
=
b
0
=
0
a
0
+
1
b
0
When
a
is divided by
2
q
, the coefficients are divided by the same value:
a
=
k
0
a
0
+
l
0
b
0
⟹
a
2
q
=
k
0
2
q
a
0
+
l
0
2
q
b
0
When
a
and
b
are swapped, the pairs
(
k
0
,
l
0
)
and
(
k
1
,
l
1
)
are swapped.
When
b
is subtracted from
a
, the coefficients are subtracted:
In other words, whatever we do to
a
and
b
, we also do to the coefficient pairs
(
k
0
,
l
0
)
.
Here’s a linear algebraic restatement if you want a different perspective.
Weighted sums are actually
linear combinations
, and the coefficients can be tracked because subtraction and division by a constant are both
linear operators
.
The algorithm tracks a matrix
A
of a specific form, mapping
(
a
0
b
0
)
T
to
(
a
b
)
T
.
Treating values as opaque,
a
and
b
are elements of a
vector space
with
basis
⟨
a
0
,
b
0
⟩
,
A
is a
change-of-basis matrix
, and the integers
a
and
b
in code are values of some
evaluation functional
at
a
and
b
.
Simplifying
⟨
a
0
,
b
0
⟩
to
⟨
0
,
gcd
(
a
0
,
b
0
)
⟩
is essentially
lattice reduction
, which can be seen as a generalization of GCD to higher-dimensional spaces.
Limitations
Implementation attempts quickly reveal a problem: coefficients are not necessarily divisible by
2
q
, so it’s not clear how to represent them. Surely not with floats.
This is actually a core difference between Stein’s algorithm and the textbook Euclidean algorithm, which is implemented as
gcd
(
a
,
b
)
=
gcd
(
b
,
a
mod
b
)
.
The Euclidean algorithm uses division (
q = a / b
), but only to compute constant factors. The values are updated with subtraction and multiplication alone (
a -= b * q
). Stein’s algorithm divides values (
a /= 2^q
), causing non-integer coefficients.
This is likely why the extended Stein’s algorithm is unpopular. We’ll use tricks tailored to modular inverse, but the general-purpose case covered at the end of the post essentially boils down to “compute modular inverse and post-process”. I believe it can still be faster than the textbook implementation, but I haven’t tested it.
Fractions
We can track coefficients as fractions to stay in integers. The most efficient approach uses the same denominator
2
p
for all variables:
{
a
=
2
−
p
(
k
0
a
0
+
l
0
b
0
)
b
=
2
−
p
(
k
1
a
0
+
l
1
b
0
)
We start with
p
=
0
. Instead of dividing
k
0
,
l
0
by
2
q
, we increase
p
by
q
and multiply
k
1
,
l
1
by
2
q
. Subtraction can ignore
p
because all coefficients use the same precision.
This seems pointless at first, since we need to know
2
−
p
mod
b
0
, but if the modulus is fixed, we can precompute it. Each iteration reduces the total bit length of
a
and
b
by at least
q
, and after the last right-shift
a
,
b
≠
0
, so if the input numbers fit in
k
bits, the sum of
q
(and thus
p
) is limited by
2
k
−
2
. This means that we can increase precision to
2
k
−
2
at the end and use a single precomputed value
2
−
(
2
k
−
2
)
mod
b
0
.
The multitude of variables is getting confusing, so let’s simplify it. We’re looking for
k
1
mod
b
0
and don’t care about
l
i
, so tracking just
k
0
and
k
1
suffices. Let’s rename these variables to
u
and
v
respectively to get rid of indices. This gives us:
let
mut
u
=
1
;
let
mut
v
=
0
;
let
mut
p
=
0
;
let
mut
q
= a.
trailing_zeros
();
while
a !=
0
{
    a >>= q;
    v <<= q;
    p += q;

    q = (a - b).
trailing_zeros
();
if
a < b {
        (a, b) = (b - a, a);
        (u, v) = (v, u);
    }
else
{
        (a, b) = (a - b, b);
    }
    u -= v;
}
assert!
(b ==
1
,
"not invertible"
);
v <<=
62
- p;
return
(v * inverse_of_2p62) % b0;
We don’t apply the latency-reducing trick to
u
and
v
because the latency is dominated by other calculations. Computing both
u - v
and
v - u
would most likely reduce performance, since we’re already pushing the CPU limit of parallel operations.
Types
It’s easy to prove by induction that at the beginning of each iteration,
Note that
u
is one bit longer than
v
at this point because
u
is increased at the end of the previous iteration, while
v
is increased at the beginning of the next iteration.
This means that
u
and
v
fit in signed
p
+
2
-bit integers. Since
p
≤
2
k
−
2
, that amounts to
2
k
-bit types, i.e. twice as wide as the input. And that’s a problem: while it works just fine for
32
-bit inputs,
64
-bit inputs require
i128
arithmetic, which slows down the algorithm considerably. We’ll discuss what to do about it in a bit.
Montgomery
Before we do this, though, let’s finish the
32
-bit case. There’s just one thing left to improve: computing
v
⋅
2
−
62
mod
b
0
.
On the face of it, this is one multiplication and one reduction, but
Montgomery multiplication
demonstrates that these operations can be performed faster together.
Assume for a moment that
v
is non-negative. The idea is to subtract a multiple of
b
0
from
v
such that the bottom
62
bits become zero, so that the remainder remains the same, but division by
2
62
can be performed with a shift. We’re looking for
t
such that
This is equivalent to
t
=
v
⋅
b
0
−
1
(
mod
2
62
)
, and by precomputing
j
=
b
0
−
1
mod
2
62
, we obtain
v
−
(
v
j
mod
2
62
)
b
0
as the easily divisible value. Since
v
and
(
v
j
mod
2
62
)
b
0
have equal bottom
62
bits,
v
−
(
v
j
mod
2
62
)
b
0
2
62
=
⌊
v
2
62
⌋
−
⌊
(
v
j
mod
2
62
)
b
0
2
62
⌋
We’ve just found that
v
≤
2
p
≤
2
62
, so unless
v
=
2
62
exactly, this is just
−
⌊
(
v
j
mod
2
62
)
b
0
2
62
⌋
=
−
⌊
(
v
(
4
j
)
mod
2
64
)
b
0
2
64
⌋
This number is in range
[
−
b
0
+
1
;
0
]
. We know that
0
can never be an inverse, so it’s actually
[
−
b
0
+
1
;
−
1
]
, and by adding
b
0
, we obtain the exact remainder. This can be computed with only two multiplications and some glue:
fn
redc62
(v:
i64
)
->
u32
{
if
v == (
1
<<
62
) {
1
}
else
{
let
x
= v.
unsigned_abs
().
wrapping_mul
(j <<
2
).
widening_mul
(b0
as
u64
).
1
as
u32
;
if
v >
0
{ b0 - x }
else
{ x }
    }
}
That’s it for
32
-bit and smaller inputs. Yay! Buy yourself a cupcake.
64-bit inputs
For
64
-bit inputs, coefficients only fit in
i128
. This makes each operation twice as slow. We can reduce
u
and
v
modulo
b
0
on each iteration so that coefficients fit in
64
bits, since we only need
v
mod
b
0
, but this tanks performance too.
Hmm. Notice that at the beginning of the algorithm,
u
and
v
fit in
1
bit and then grow slowly. Only once their length exceeds
64
bits do we need long integers. What if we could somehow reset the length every few iterations, so that
64
-bit integers suffice?
Just like
a
and
b
can be represented as weighted sums of
a
0
,
b
0
,
u
and
v
can be represented as weighted sums of their earlier versions
u
0
,
v
0
:
The trick is to save
u
0
,
v
0
and update short coefficients
f
i
,
g
i
instead of long values
u
,
v
in the loop. We start with
u
0
=
1
,
v
0
=
0
and trivial coefficients:
{
u
=
u
0
=
1
u
0
+
0
v
0
v
=
v
0
=
0
u
0
+
1
v
0
When the coefficients
f
i
,
g
i
grow past
64
bits, we pause, compute
u
,
v
based on these formulas, replace
u
0
,
v
0
with
u
,
v
, and reset the coefficients
f
i
,
g
i
back to trivial, bringing the length back to
1
.
let
mut
u0
=
1
;
let
mut
v0
=
0
;
let
mut
q
= a.
trailing_zeros
();
while
a !=
0
{
let
mut
(f0, g0) = (
1
,
0
);
let
mut
(f1, g1) = (
0
,
1
);
let
mut
p
=
0
;
while
a !=
0
&& p + q <=
62
{
        a >>= q;
        f1 <<= q;
        g1 <<= q;
        p += q;

        q = (a - b).
trailing_zeros
();
if
a < b {
            (a, b) = (b - a, a);
            (f0, f1) = (f1, f0);
            (g0, g1) = (g1, g0);
        }
else
{
            (a, b) = (a - b, b);
        }
        f0 -= f1;
        g0 -= g1;
    }

    
    
    
    
    
    a >>=
62
- p;
    f1 <<=
62
- p;
    g1 <<=
62
- p;
    q -=
62
- p;
let
f0
=
redc62
(f0);
let
g0
=
redc62
(g0);
let
f1
=
redc62
(f1);
let
g1
=
redc62
(g1);
    (u0, v0) = ((f0 * u0 + g0 * v0) % b0, (f1 * u0 + g1 * v0) % b0);
}
assert!
(b ==
1
,
"not invertible"
);
return
v0;
Expand
Vectorization
The astute among you might realize this doesn’t improve much, since we went from updating two
128
-bit numbers in a loop to updating four
64
-bit numbers in a loop. But since we apply the exact same operations to
f
i
and
g
i
, we can vectorize them.
We can’t use SIMD because x86 doesn’t have
cmov
for vector registers, but we can decrease the coefficient length to
32
bits and pack two coefficients into one integer:
This technique is called
SWAR
. It was invented before hardware SIMD support existed, but it’s useful to this day. I wrote about another application of SWAR
here
.
This simplifies the inner loop to:
while
a !=
0
&& p + q <=
30
{
    a >>= q;
    c1 <<= q;
    p += q;

    q = (a - b).
trailing_zeros
();
if
a < b {
        (a, b) = (b - a, a);
        (c0, c1) = (c1, c0);
    }
else
{
        (a, b) = (a - b, b);
    }
    c0 -= c1;
}
Just like
u
and
v
,
c
0
and
c
1
take
p
+
2
bits, so we limit
p
by
32
−
2
=
30
. But with care, we can squeeze out one more bit. Recall the inequalities:
Only
u
takes
p
+
2
bits.
v
fits in
p
+
1
, if barely: signed integer types represent the range
[
−
2
p
;
2
p
−
1
]
, while this is
[
−
2
p
+
1
;
2
p
]
, but the number of distinct values is the same. So even if we run out of the
30
-bit limit, we can shift
v
once more. This affects the code after the inner loop:
a >>=
31
- p;
c1 <<=
31
- p;
q -=
31
- p;
let
(f0, g0) =
parse_coefficients
(c0);
let
(f1, g1) =
parse_coefficients
(c1);
let
f0
=
redc31
(f0);
let
g0
=
redc31
(g0);
let
f1
=
redc31
(f1);
let
g1
=
redc31
(g1);
(u0, v0) = ((f0 * u0 + g0 * v0) % b0, (f1 * u0 + g1 * v0) % b0);
Note that the inner loop is still limited by
30
, since it not only shifts
v
, but also subtracts from
u
, which could cause an overflow with a limit of
31
.
Parsing coefficients from
c
i
is slightly tricky due to the unusual signed integer format, but not impossibly so:
int
(
x
)
=
{
x
if
x
≤
2
31
x
−
2
32
if
x
>
2
31
{
f
i
=
int
(
c
i
mod
2
32
)
g
i
=
int
(
⌊
c
i
+
2
31
−
1
2
32
⌋
)
This assumes that
c
i
is stored in an unsigned type.
Pornin uses a simpler way to pack
f
i
,
g
i
into
c
i
: by adding
2
31
−
1
to
f
i
and
g
i
, we can ensure the two parts don’t interfere with each other’s bits. But this makes arithmetic slower due to conversions between the biased and non-biased forms.
Symmetry
With packed coefficients, the inner loop is similar to the unoptimized version, differing only in
c
0
,
c
1
vs
u
,
v
. This allows us to cheaply combine two approaches: track the true values
u
,
v
for the first
62
iterations and then switch to coefficients. It’s faster than relying on coefficients alone because it recalculates
u
0
,
v
0
less often.
The final implementation looks something like this:
let
mut
u0
=
1
;
let
mut
v0
=
0
;
let
mut
q
= a.
trailing_zeros
();
let
mut
is_first_iteration
=
true
;
while
a !=
0
{
let
mut
c0
=
1
;
let
mut
c1
=
if
is_first_iteration {
0
}
else
{
1
<<
32
};
let
mut
p_left
=
if
is_first_iteration {
63
}
else
{
31
};
while
a !=
0
&& q < p_left { 
        a >>= q;
        c1 <<= q;
        p_left -= q;

        q = (a - b).
trailing_zeros
();
if
a < b {
            (a, b) = (b - a, a);
            (c0, c1) = (c1, c0);
        }
else
{
            (a, b) = (a - b, b);
        }
        c0 -= c1;
    }

    a >>= p_left;
    c1 <<= p_left;
    q -= p_left;
if
is_first_iteration {
        u0 =
redc63
(c0);
        v0 =
redc63
(c1);
    }
else
{
let
(f0, g0) =
parse_coefficient
(c0);
let
(f1, g1) =
parse_coefficient
(c1);
let
f0
=
redc31
(f0);
let
g0
=
redc31
(g0);
let
f1
=
redc31
(f1);
let
g1
=
redc31
(g1);
        (u0, v0) = ((f0 * u0 + g0 * v0) % m, (f1 * u0 + g1 * v0) % m);
    }

    is_first_iteration =
false
;
}
assert!
(b ==
1
,
"not invertible"
);
return
v0;
Expand
We store
p_left
instead of
p
so that
p_left -= q
and
q < p_left
can be computed with a single instruction.
The
32
-bit and
64
-bit cases can use the same implementation, as replacing
q < p_left
with
true
makes it identical to the
32
-bit algorithm, and compilers recognize this.
redc31(x)
can be implemented as
redc63(x << 32)
.
And that’s it! You now know a cool way to compute
64
-bit modular inverses.
General case
To support variable
b
0
, we can compute
j
=
b
0
−
1
mod
2
64
in runtime. This can be done very quickly with
an algorithm by Jeffrey Hurchalla
.
j
only exists if
b
0
is odd. If it’s even, swap
a
0
and
b
0
. If both are even, divide them by their common power of two and choose whichever becomes odd as
b
0
.
To replace the extended Euclidean algorithm, we need to find
integers
x
,
y
such that:
Luckily, our
v
is no longer a fraction, but rather a remainder modulo
b
0
, so we can substitute
x
=
v
mod
b
0
.
y
can then be computed from the equation:
y
=
gcd
(
a
0
,
b
0
)
−
a
0
x
b
0
=
b
−
a
0
x
b
0
Since this division is exact, it can be calculated with multiplication by
j
:
Despite this complexity, I believe this method can be faster than the extended Euclidean algorithm, since the auxiliary logic takes constant time, except for computing
j
in
𝒪
(
log
⁡
k
)
=
𝒪
(
log
⁡
log
⁡
a
)
, which is still pretty good.
Outro
As a reminder, you can find my code
on GitHub
. The source of latency-optimized GCD is
this post
. Using coefficients to reset bit lengths of
u
,
v
comes from
this paper
, which also covers the case when values don’t fit in general-purpose registers.
Thanks to many friends of mine for contributing to the benchmarking results, to Ian Qvist for the motivation to complete this post and editorial comments, and to Yuki for saving me from going insane over unexplainable performance phenomena.
