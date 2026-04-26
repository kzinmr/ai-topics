---
title: "Induction variables and loops"
url: "http://xania.org/202512/09-induction-variables?utm_source=feed&utm_medium=rss"
fetched_at: 2026-04-25T12:09:19.055085+00:00
source: "xania.org"
tags: [blog, raw]
---

# Induction variables and loops

Source: http://xania.org/202512/09-induction-variables?utm_source=feed&utm_medium=rss

Induction variables and loops
Written by me, proof-read by an LLM.
Details at end.
Loop optimisations often surprise us. What looks expensive might be fast, and what looks clever might be slow.
Yesterday
we saw how the compiler canonicalises loops so it (usually) doesn’t matter how you write them, they’ll come out the same. What happens if we do something a little more expensive inside the loop?
Let’s take a look at something that looks like it would need an “expensive” multiply each loop iteration
:
Despite our “times table” seemingly requiring a multiply for each step, the compiler realises it can rephrase the loop to keep an accumulator, and add
table
each iteration instead:
.L3:
add
rdx
,
4
; advance the output pointer
mov
DWORD
PTR
[
rdx-4
],
eax
; write "accumulator"
add
eax
,
edi
; add "table" to the accumulator
cmp
rdx
,
rcx
; have we reached the end?
jne
.L3
; loop if not
That “accumulator” is called an induction variable, and if you know a thing about maths
, you know we can rewrite lots of things as a series of sums. For example, if we wanted to output squares (x²) instead, we might expect the compiler to smartly turn this into a series of additions
, something like
:
But in fact, if we try it, the compiler goes back to squaring with
imul
:
What’s going on here?! Yet again, the compiler is probably smarter than us: multiplies are pretty quick (around 3 cycles), and by keeping each loop iteration independent of the previous iteration, the processor can actually run many multiplications simultaneously.
In our manual induction variable code, each loop iteration requires the results of the previous loop iteration - a
loop carried dependency
- which could prevent this overlapping of calculations.
To test this theory, we can use
llvm-mca
- the
LLVM Machine Code Analyser
. This tool runs a CPU simulation and can show this overlapping
of computation. I’ve used it to generate a timeline of what happens on the CPU, cycle by cycle. In this view, instructions run from top to bottom, and time left to right. Each instruction’s journey through the pipeline is shown:
D
is decode,
e
is execution,
E
is execution complete,
R
is retired (fully complete).
=
shows a stall. Each row shows one instruction - for example,
[0,2]
means iteration 0, instruction 2.
Watch how the instructions from different iterations overlap - that’s the key to performance here. This trace is for the induction variable version:
[0,0]     DeER .    .    .  .   add     rsi, 4
[0,1]     D=eER.    .    .  .   mov     dword ptr [rsi - 4], eax
[0,2]     DeE-R.    .    .  .   add     eax, edx
[0,3]     DeE-R.    .    .  .   add     edx, 2
[0,4]     .DeER.    .    .  .   cmp     rcx, rsi
[0,5]     .D=eER    .    .  .   jne     .L3
[1,0]     .DeE-R    .    .  .   add     rsi, 4
[1,1]     .D=eER    .    .  .   mov     dword ptr [rsi - 4], eax
[1,2]     . DeER    .    .  .   add     eax, edx
[1,3]     . DeER    .    .  .   add     edx, 2
[1,4]     . DeER    .    .  .   cmp     rcx, rsi
[1,5]     . D=eER   .    .  .   jne     .L3
Nearly the whole first loop iteration is decoded each cycle, and by the third cycle all of the first loop iteration is executing. The first iteration is complete on the 6th cycle, and the second by the seventh cycle, which means once things settle down, an iteration completes every 1½ cycles
. You can see the full trace
at this Compiler Explorer link
.
If we simulate the square-with-multiply version:
[0,0]     DeER .    .    .    .   mov   edx, eax
[0,1]     D=eeeER   .    .    .   imul  edx, eax
[0,2]     D====eER  .    .    .   mov   dword ptr [rsi + 4*rax], edx
[0,3]     DeE----R  .    .    .   inc   rax
[0,4]     .DeE---R  .    .    .   cmp   rax, rdi
[0,5]     .D=eE--R  .    .    .   jne   .L3
[1,0]     .DeE---R  .    .    .   mov   edx, eax
[1,1]     .D=eeeER  .    .    .   imul  edx, eax
[1,2]     . D===eER .    .    .   mov   dword ptr [rsi + 4*rax], edx
[1,3]     . DeE---R .    .    .   inc   rax
[1,4]     . D=eE--R .    .    .   cmp   rax, rdi
[1,5]     . D==eE-R .    .    .   jne   .L3
On this simulated Haswell processor, the average loop still takes 1.5 cycles! Check the
full link here
. Despite using a more expensive multiply, and despite a loop iteration now taking 8 cycles, because each loop iteration is independent of the last, we still get the throughput of one iteration every 1½ cycles.
Compilers
are
smart - trust them. But know how to use tools like
Compiler Explorer
and
llvm-mca
to verify, and always benchmark.
See
the video
that accompanies this post.
This post is day 9 of
Advent of Compiler Optimisations 2025
,
a 25-day series exploring how compilers transform our code.
←
Going loopy
|
Unrolling loops
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
