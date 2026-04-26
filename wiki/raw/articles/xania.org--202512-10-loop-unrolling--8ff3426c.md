---
title: "Unrolling loops - Matt Godbolt’s blog"
url: "http://xania.org/202512/10-loop-unrolling?utm_source=feed&utm_medium=rss"
fetched_at: 2026-04-25T12:09:18.591798+00:00
source: "xania.org"
tags: [blog, raw]
---

# Unrolling loops - Matt Godbolt’s blog

Source: http://xania.org/202512/10-loop-unrolling?utm_source=feed&utm_medium=rss

Unrolling loops
Written by me, proof-read by an LLM.
Details at end.
A common theme for helping the compiler optimise is to give it as much information as possible. Using the
right signedness of types
, targeting the right CPU model, keeping
loop iterations independent
, and for today’s topic: telling it how many loop iterations there are going to be ahead of time.
Taking the range-based sum example
from our earlier post on loops
, but using a
std::span
, we can explore this ability. Let’s take a look at what happens if we use a dynamically-sized span - we’d expect it to look very similar to the
std::vector
version:
The compiler doesn’t know how many ints there will be ahead of time, and it generates pretty straightforward code
:
.LBB0_2
ldr
r3
,
[
r2
],
#4
; value = *ints++
subs
r1
,
r1
,
#4
; count down remaining bytes
add
r0
,
r3
,
r0
; sum = value + sum
bne
.LBB0_2
; loop if no more bytes
A simple modification to the code to pass a
std::span<int, 8>
, so the compiler now knows it will always loop eight times:
The compiler takes advantage of this knowledge by unrolling the loop - it compiles the code as if all eight iterations of the loop had been written out one after another, avoiding the loop counter, and the conditional branch. That saves two instructions per loop iteration (the
subs
and the
bne
), and also allows the compiler to spot more patterns: We see that it loads the first two values at once using the “load multiple”
ldmib
instruction
.
Try changing the
8
in the example above to other values and you’ll see the variety of different ways the compiler chooses to implement the loop. At 32 iterations it gets quite register-happy, even spilling onto the stack briefly to get more registers to load. At 50 iterations the optimiser gives up and falls back to regular looping
.
Compilers will sometimes partially unroll loops (chunking up unrolled sections in a larger loop), or even speculatively unroll when the count isn’t known ahead of time. There’s a ton of heuristics at play, and honestly, the compiler’s guess is usually pretty good. But it’s worth checking your hot loops
to see what it’s doing - and if you can give it the loop count at compile time, you’re setting it up for success.
See
the video
that accompanies this post.
This post is day 10 of
Advent of Compiler Optimisations 2025
,
a 25-day series exploring how compilers transform our code.
←
Induction variables and loops
|
Pop goes the…population count?
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
