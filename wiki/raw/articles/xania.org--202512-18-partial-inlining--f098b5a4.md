---
title: "Partial inlining"
url: "http://xania.org/202512/18-partial-inlining?utm_source=feed&utm_medium=rss"
fetched_at: 2026-04-29T07:01:05.502160+00:00
source: "xania.org"
tags: [blog, raw]
---

# Partial inlining

Source: http://xania.org/202512/18-partial-inlining?utm_source=feed&utm_medium=rss

Partial inlining
Written by me, proof-read by an LLM.
Details at end.
We’ve learned how important inlining is to optimisation, but also that it might sometimes cause code bloat. Inlining doesn’t have to be all-or-nothing!
Let’s look at a simple function that has a fast path and slow path; and then see how the compiler handles it
.
In this example we have some
process
function that has a really trivial fast case for numbers in the range 0-100. For other numbers it does something more expensive. Then
compute
calls
process
twice (making it less appealing to inline all of
process
).
Looking at the assembly output, we see what’s happened: The compiler has split
process
into two functions, a
process (part.0)
that does the expensive part only. It then rewrites
process
into the quick check for 100, returning double the value if less than 100. If not, it jumps to the
(part.0)
function:
process
(
unsigned
int
):
cmp
edi
,
99
; less than or equal to 99?
jbe
.L7
; skip to fast path if so
jmp
process
(
unsigned
int
)
(.
part.0
)
; else jump to the expensive path
.L7:
lea
eax
,
[
rdi
+
rdi
]
; return `value * 2`
ret
This first step - extracting the cold path into a separate function - is called
function outlining
. The original
process
becomes a thin wrapper handling the hot path, delegating to the outlined
process (.part.0)
when needed. This split sets up the real trick:
partial inlining
. When the compiler later inlines
process
into
compute
, it inlines just the wrapper whilst keeping calls to the outlined cold path. External callers can still call
process
and have it work correctly for all values.
Let’s see this optimisation in action in the
compute
function:
compute
(
unsigned
int
,
unsigned
int
):
cmp
edi
,
99
; is a <= 99?
jbe
.L13
; if so, go to the inlined fast path for a
call
process
(
unsigned
int
)
(.
part.0
)
; else, call expensive case
mov
r8d
,
eax
; save the result of process(a)
cmp
esi
,
99
; is b <= 99?
jbe
.L14
; if so go to the inlined fast path for b
.L11:
mov
edi
,
esi
; otherwise, call expensive case for b
call
process
(
unsigned
int
)
(.
part.0
)
add
eax
,
r8d
; add the two slow cases together
ret
; return
.L13:
; case where a is fast case
lea
r8d
,
[
rdi
+
rdi
]
; process(a) is just a + a
cmp
esi
,
99
; is b > 99?
ja
.L11
; jump to b slow case if so
; (falls through to...)
.L14:
; b fast case
lea
eax
,
[
rsi
+
rsi
]
; double b
add
eax
,
r8d
; return 2*a + 2*b
ret
Looking at
compute
, we can see the benefits of this approach clearly: The simple range check and arithmetic (
cmp
,
lea
) are inlined directly, avoiding the function call overhead for the fast path. When a value is 100 or greater, it calls the outlined
process (.part.0)
function for the more expensive computation.
This is the best of both worlds: we get the performance benefit of inlining the lightweight check and simple arithmetic, whilst avoiding code bloat from duplicating the expensive computation
. The original
process
function remains intact and callable, so external callers still work correctly.
Partial inlining lets the compiler make nuanced trade-offs about what to inline and what to keep shared. The compiler can outline portions of a function based on its heuristics about code size and performance
, giving you benefits of inlining without necessarily paying the full code size cost. In this example, the simple check is duplicated whilst the complex computation stays shared.
As with many optimisations, the compiler’s heuristics
usually make reasonable choices about when to apply partial inlining, but it’s worth checking your hot code paths to see if the compiler has made the decisions you expect. Taking a quick peek in
Compiler Explorer
is a good way to develop your intuition.
See
the video
that accompanies this post.
This post is day 18 of
Advent of Compiler Optimisations 2025
,
a 25-day series exploring how compilers transform our code.
←
Inlining - the ultimate optimisation
|
Chasing your tail
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
