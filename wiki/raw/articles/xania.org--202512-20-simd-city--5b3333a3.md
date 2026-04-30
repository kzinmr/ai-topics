---
title: "SIMD City: Auto-vectorisation"
url: "http://xania.org/202512/20-simd-city?utm_source=feed&utm_medium=rss"
fetched_at: 2026-04-30T07:00:57.449051+00:00
source: "xania.org"
tags: [blog, raw]
---

# SIMD City: Auto-vectorisation

Source: http://xania.org/202512/20-simd-city?utm_source=feed&utm_medium=rss

SIMD City: Auto-vectorisation
Written by me, proof-read by an LLM.
Details at end.
It’s time to look at one of the most sophisticated optimisations compilers can do: autovectorisation. Most “big data” style problems boil down to “do this maths to huge arrays”, and the limiting factor isn’t the maths itself, but the feeding of instructions to the CPU, along with the data it needs.
To help with this problem, CPU designers came up with SIMD: “Single Instruction, Multiple Data”. One instruction tells the CPU what to do with a whole chunk of data. These chunks could be 2, 4, 8, 16 or similar units of integers or floating point values, all treated individually. Initially
the only way to use this capability was to write assembly language directly, but luckily for us, compilers are now able to help.
To take advantage of SIMD we need to ensure our data is laid out in a nice long line, like an array, or vector
. It’s also much better to store different “fields” of the data in separate arrays
. We’re going to start with some integer maths - let’s update an array
x
to be element-wise the max of
x
and
y
:
In this
-O2
-compiled code
, we don’t see any vectorisation, just the nice tight loop code we’ve come to expect:
.L3:
mov
edx
,
DWORD
PTR
[
rsi
+
rax
*
4
]
; read y[i]
cmp
edx
,
DWORD
PTR
[
rdi
+
rax
*
4
]
; compare with x[i]
jle
.L2
; if less, skip next instr
mov
DWORD
PTR
[
rdi
+
rax
*
4
],
edx
; x[i] = y[i]
.L2:
add
rax
,
1
; ++i
cmp
rax
,
65536
; are we at 65536?
jne
.L3
; keep looping if not
To ramp up to the next level, we’ll need to add two flags: first we need to turn up the optimiser to
-O3
, and then we need to tell the compiler to target a CPU that has the appropriate SIMD instruction
with something like
-march=skylake
.
Our inner loop has gotten a little more complex, but spot the cool part:
.L4:
; Reads 8 integers into ymm1, y[i..i+7]
vmovdqu
ymm1
,
YMMWORD
PTR
[
rsi
+
rax
]
; Compares that with 8 integers x[i..i+7]
vpcmpgtd
ymm0
,
ymm1
,
YMMWORD
PTR
[
rdi
+
rax
]
; Were all 8 values less or equal?
vptest
ymm0
,
ymm0
; if so, skip the write
je
.L3
; mask move x[i..i+7] with the y values that were greater
vpmaskmovd
YMMWORD
PTR
[
rdi
+
rax
],
ymm0
,
ymm1
.L3:
add
rax
,
32
; move forward 32 bytes
cmp
rax
,
262144
; are we at the end? (4*65536)
jne
.L4
; keep looping if not
With a very similar number of instructions we’re now processing 8 integers at a time! This is the power of SIMD - we’d likely be limited by the bandwidth to memory rather than the housekeeping of working out what to do with them.
There are a couple of things to talk about though. Firstly, what’s all this “mask move” stuff? Well, with SIMD we can act on “multiple data” but only with a “single instruction”. Our original code has a conditional update: not every array element is necessarily processed in the same way. The compiler has cleverly used a “mask move” to let it
conditionally
write back only the elements that are “greater than”, which is pretty clever of it. We can help it if we don’t mind unconditionally writing to memory:
By unconditionally writing to
x[i]
we can reduce the loop to:
.L3:
; Read 8 integers from x[i..i+7]
vmovdqu
ymm0
,
YMMWORD
PTR
[
rdi
+
rax
]
; "max" the integers with y[i..i+7]
vpmaxsd
ymm0
,
ymm0
,
YMMWORD
PTR
[
rsi
+
rax
]
; Store them back
vmovdqu
YMMWORD
PTR
[
rdi
+
rax
],
ymm0
add
rax
,
32
; move forward 32 bytes
cmp
rax
,
262144
; are we at the end?
jne
.L3
; keep looping if not
The compiler has spotted our ternary operator is actually exactly the same as the built-in vector “max” instruction! No explicit comparisons or branches now - fantastic.
There’s one last thing to cover - the eagle-eyed amongst you might have spotted the fact there are actually
two
loops, one using vector instructions, and one doing regular one-at-a-time operations. The regular loop is jumped to conditionally after this check:
lea
rax
,
[
rdi-4
]
; rax = x - 4
sub
rax
,
rsi
; rax = x - 4 - y
cmp
rax
,
24
; compare rax with 24
mov
eax
,
0
; (set up loop counter for below)
jbe
.L2
; if rax <= 24; jump to the slow case
; falls through to the vectorised loop here
So what’s going on here? We’re checking
x
and
y
- not the
values
of the two arrays, but the addresses. That somewhat awkward sequence is essentially saying “do the two arrays overlap with each other in a way that would prevent us being able to vectorise”. If they overlap by 28 or more bytes, then we can’t read and write in 8
int
(32-byte) chunks: working in batches like this would give different results as the overlap means writing to
x[i]
might affect
y[i+2]
(or similar). So, the compiler has to add this check
and
generate a fall-back case that does one at a time.
With some non-standard trickery we tell the compiler to ignore vector dependencies for the loop
:
That’s it for today: with the right flags and a little care about data layout, the compiler can turn your one-at-a-time loops into batch-processing powerhouses! Tomorrow we’ll look at floating point vectorisation and its own peculiar quirks.
See
the video
that accompanies this post.
This post is day 20 of
Advent of Compiler Optimisations 2025
,
a 25-day series exploring how compilers transform our code.
←
Chasing your tail
|
When SIMD Fails: Floating Point Associativity
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
