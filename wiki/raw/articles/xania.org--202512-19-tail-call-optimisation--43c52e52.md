---
title: "Chasing your tail"
url: "http://xania.org/202512/19-tail-call-optimisation?utm_source=feed&utm_medium=rss"
fetched_at: 2026-05-01T07:01:07.040205+00:00
source: "xania.org"
tags: [blog, raw]
---

# Chasing your tail

Source: http://xania.org/202512/19-tail-call-optimisation?utm_source=feed&utm_medium=rss

Chasing your tail
Written by me, proof-read by an LLM.
Details at end.
Inlining is fantastic, as we’ve
seen
recently
. There’s a place it surely can’t help though: recursion! If we call our own function, then surely we can’t inline…
Let’s see what the compiler does with the classic recursive “greatest common divisor” routine - surely it can’t avoid calling itself?
And yet: The compiler is able to avoid the recursion! When a function ends by calling another function (including itself), the compiler is often able to replace the call with a jump to that function. This is called “tail call optimisation”. If that function is itself, the “jump to the start” is effectively the same as a loop. Our compiler turns our recursive function into a loop:
gcd
(
unsigned
int
,
unsigned
int
):
mov
eax
,
edi
; eax (return val) = a
test
esi
,
esi
; is b == 0?
je
.LBB0_4
; if b is zero, jump to the end
mov
edx
,
esi
; edx = b
.LBB0_2:
mov
ecx
,
edx
; ecx = b
xor
edx
,
edx
; edx = 0 (set up for divide)
div
ecx
; eax = edx:eax (0:a) / ecx (b)
; edx = edx:eax (0:a) % ecx (b)
mov
eax
,
ecx
; eax = b
test
edx
,
edx
; was a % b == 0?
jne
.LBB0_2
; if not, keep looping
mov
eax
,
ecx
; eax (return val) = b
.LBB0_4:
ret
Pretty neat, eh? In this particular case the fact that we are recursing also unlocked further optimisations
, but in general, tail recursion is useful to save a few instructions and some stack space
.
Sometimes we need to guarantee that tail calls happen
. Clang has a way to force tail call optimisation or error if it’s not possible: the
[[clang::musttail]]
annotation. In our gcd example, without tail-call optimisations we need a lot more stack space. To guarantee that tail calls happen (even in debug mode) we can specify this annotation.
Tail call optimisation saves stack space, enables loop optimisations, and can even make your branch predictor happier. All this from a compiler noticing your function ends with a call and thinking “why bother coming back?” Sometimes the best optimisation is to just keep forging ahead!
One last point worth mentioning, tying back to
calling conventions
: if you arrange for your tail-called function’s arguments to be in the same order (or partial order) as the calling function’s parameters, the compiler can be super efficient. Compare these two functions:
Our same order function simply jumps on to
wrapped_func
even though we take
z
too - the compiler can ignore it without issue. For the switched args version, the compiler has to emit instructions to switch parameters around, which obviously is more work. Sometimes that’s unavoidable, of course, but it’s worth keeping in mind when designing your function interfaces.
Bonus: TCOs in emulators
Note
: This section explores a more advanced application of TCO. If you’re feeling overwhelmed, feel free to skip it - the core TCO concepts are all covered above.
One surprising application of tail call optimisation is in CPU emulators
. Most emulators use a
switch
statement inside a loop - fetch an opcode byte, switch on it to handle the instruction, repeat. That’s simple and works well.
But there’s an alternative approach using tail calls
:
Each instruction handler calls
next_opcode()
, which looks up and calls the next handler. This looks like unbounded recursion! But the compiler inlines
next_opcode()
and uses TCO, turning it into a jump. Each handler ends with an indirect
jmp
through the opcode table - no stack growth at all.
Why bother with this complexity? Branch prediction! Modern CPUs predict branches based on history and branch path, indexed by each branch location. With a
switch
statement, there’s
one
branch trying to predict which of 256 instructions comes next - an impossible task. In my emulators, that single branch accounts for a double-digit percentage of
all
mispredictions.
With the TCO approach, each of the 256 instruction handlers has its own branch, each with its own predictor state. The branch at the end of the 6502
CMP
can learn “often followed by
BNE
”, while the branch at the end of
LDA
learns different patterns. This gives the CPU’s branch predictor much better information to work with.
It’s a niche optimisation, but a neat example of how TCO enables techniques that would otherwise be impractical!
See
the video
that accompanies this post.
This post is day 19 of
Advent of Compiler Optimisations 2025
,
a 25-day series exploring how compilers transform our code.
←
Partial inlining
|
SIMD City: Auto-vectorisation
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
