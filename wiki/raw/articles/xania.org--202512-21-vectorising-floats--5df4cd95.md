---
title: "When SIMD Fails: Floating Point Associativity"
url: "http://xania.org/202512/21-vectorising-floats?utm_source=feed&utm_medium=rss"
fetched_at: 2026-04-30T07:00:57.573065+00:00
source: "xania.org"
tags: [blog, raw]
---

# When SIMD Fails: Floating Point Associativity

Source: http://xania.org/202512/21-vectorising-floats?utm_source=feed&utm_medium=rss

When SIMD Fails: Floating Point Associativity
Written by me, proof-read by an LLM.
Details at end.
Yesterday
we saw SIMD work beautifully with integers. But floating point has a surprise in store. Let’s try summing an array
:
Looking at the core loop, the compiler has pulled off a clever trick:
.L2:
; pick up 8 integers and add them element-wise to ymm0
vpaddd
ymm0
,
ymm0
,
YMMWORD
PTR
[
rdi
]
add
rdi
,
32
; move to the next batch of integers
cmp
rax
,
rdi
; at the end?
jne
.L2
; loop if not
The compiler is using a vectorised add instruction which treats the
ymm0
as 8 separate integers, adding them up individually to the corresponding elements read from
[rdi]
. That’s incredibly efficient, processing 8 integers per loop iteration, but at the end of that loop we’ll have 8 separate subtotals. The compiler adds a bit of “fix up” code after the loop to sum all these 8 subtotals:
vextracti128
xmm1
,
ymm0
,
0x1
; xmm1 = ymm0 >> 128
vpaddd
xmm0
,
xmm1
,
xmm0
; xmm0 += xmm1
vpsrldq
xmm1
,
xmm0
,
8
; xmm1 = xmm0 >> 64
vpaddd
xmm0
,
xmm0
,
xmm1
; xmm0 += xmm1
vpsrldq
xmm1
,
xmm0
,
4
; xmm1 = xmm0 >> 32
vpaddd
xmm0
,
xmm0
,
xmm1
; xmm0 += xmm1
vmovd
eax
,
xmm0
; return xmm0
This sequence repeatedly adds the “top half” of the result to the bottom half until there’s only one left. This fix up code is a little bit extra work, but the efficiency of the loop makes up for it
.
Let’s switch to
float
s
and see what happens:
We’re still processing 32 bytes’ worth of
float
s per loop iteration
, but something unfortunate is going on:
.L2:
vaddss
xmm0
,
xmm0
,
DWORD
PTR
[
rdi
]
; xmm0 += first elem
add
rdi
,
32
; move to next 8 floats
vaddss
xmm0
,
xmm0
,
DWORD
PTR
[
rdi-28
]
; xmm0 += second
vaddss
xmm0
,
xmm0
,
DWORD
PTR
[
rdi-24
]
; etc
vaddss
xmm0
,
xmm0
,
DWORD
PTR
[
rdi-20
]
; ...
vaddss
xmm0
,
xmm0
,
DWORD
PTR
[
rdi-16
]
vaddss
xmm0
,
xmm0
,
DWORD
PTR
[
rdi-12
]
vaddss
xmm0
,
xmm0
,
DWORD
PTR
[
rdi-8
]
vaddss
xmm0
,
xmm0
,
DWORD
PTR
[
rdi-4
]
; xmm0 += eighth
cmp
rax
,
rdi
; at the end?
jne
.L2
; loop if not
The compiler has chosen to do 8 floats per loop iteration…but then proceeded to do each add individually. What has happened here?
To understand we need to recall that maths on
float
s is special: Operations are not associative. When adding integers, you can regroup the operations however you like—
(x + y) + z
gives the same result as
x + (y + z)
. Not so with
float
s: after each operation, rounding occurs. Depending on the relative magnitudes of
x
,
y
and
z
, regrouping the additions will change the result.
When our compiler rewrote our integer sum loop into eight subtotals to take advantage of SIMD, and then summed the subtotals, it was regrouping the additions. We wrote a loop that summed from the first element to the last, and the compiler changed it to “accumulate every 8th element in 8 separate groups, then add those together”. That works for integers but not floating point numbers.
So - are we stuck? Perhaps we know we don’t care about associativity? Some of you may be itching to use the
-Ofast
or
-funsafe-math-optimizations
flag here.  Both flags give the compiler leeway to globally ignore the rules about floating-point maths and both will work
. However, there’s a better, more targeted way:
In this example, we tell GCC to “assume maths is associative” for just the function
sum
by using an annotation. That means the effects are limited to just that one function, and will be applied consistently regardless of how this function is compiled or used. Yes; it does rely on a GCC extension, which is unfortunate. In theory we can use
std::reduce
with an unsequenced execution policy, but in my testing that didn’t work here.
Floating point maths has some unusual and perhaps surprising gotchas. Knowing about them can help you work with the compiler to get super fast vectorised code.
See
the video
that accompanies this post.
This post is day 21 of
Advent of Compiler Optimisations 2025
,
a 25-day series exploring how compilers transform our code.
←
SIMD City: Auto-vectorisation
|
Clever memory tricks
→
This post was written by a human (
Matt Godbolt
) and reviewed and proof-read by LLMs and humans.
Support Compiler Explorer on
Patreon
or
GitHub
,
or by buying CE products in the
Compiler Explorer Shop
.
