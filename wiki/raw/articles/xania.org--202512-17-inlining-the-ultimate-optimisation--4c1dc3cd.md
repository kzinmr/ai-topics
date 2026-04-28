---
title: "Inlining - the ultimate optimisation"
url: "http://xania.org/202512/17-inlining-the-ultimate-optimisation?utm_source=feed&utm_medium=rss"
fetched_at: 2026-04-28T07:01:44.353257+00:00
source: "xania.org"
tags: [blog, raw]
---

# Inlining - the ultimate optimisation

Source: http://xania.org/202512/17-inlining-the-ultimate-optimisation?utm_source=feed&utm_medium=rss

Inlining - the ultimate optimisation
Written by me, proof-read by an LLM.
Details at end.
Sixteen days in, and I’ve been dancing around what many consider the fundamental compiler optimisation: inlining. Not because it’s complicated - quite the opposite! - but because inlining is less interesting for what it does (copy-paste code), and more interesting for what it enables.
Initially inlining was all about avoiding the expense of the call
itself, but nowadays inlining enables many other optimisations to shine.
We’ve already encountered inlining (though I tried to limit it until now): On
day 8
to get the size of a vector, we called its
.size()
method. I completely glossed over the fact that while
size()
is a method on
std::vector
, we don’t see a call in the assembly code, just the subtraction and shift.
So, how does inlining enable other optimisations? Using ARMv7
, let’s convert a string to uppercase. We might have a utility
change_case
function
that either turns a single character from upper to lower, or lower to upper, so, we’ll use it in our code:
The compiler decides
to inline
change_case
into
make_upper
, and then seeing that
upper
is
always
true
, it can simplify the whole code to:
.LBB0_1:
ldrb
r2
,
[
r0
]
; read next `c`; c = *string;
sub
r3
,
r2
,
#97
; tmp = c - 'a'
uxtb
r3
,
r3
; tmp = tmp & 0xff
cmp
r3
,
#26
; check tmp against 26
sublo
r2
,
r2
,
#32
; if lower than 26 then c = c - 32
; c = ((c - 'a') & 0xff) < 26 ? c - 32 : c;
strb
r2
,
[
r0
],
#1
; store 'c' back; *string++ = c
subs
r1
,
r1
,
#1
; reduce counter
bne
.LBB0_1
; loop if not zero
There’s no trace left of the
!upper
case and the compiler, having inlined the code, has a fresh copy of the code to then further modify to take advantage of things it knows are true. It does a neat trick of avoiding a branch to check whether the character is uppercase: If
(c - 'a') & 0xff
is less than 26, it must be a lowercase character. It then conditionally subtracts 32, which has the effect of making
a
into
A
.
Inlining gives the compiler the ability to make local changes: The implementation can be special cased at the inline site as by definition there’s no other callers to the code. The special casing can include propagating values known to be constants (like the
upper
bool above), and looking for code paths that are unused
.
Inlining has some drawbacks though: if it’s overused, the code size of your program can grow quite substantially
. The compiler has to make its best guess as to whether inlining a function (and the functions that
it
calls…and so on), based on heuristics about the code size increase, and whether the perceived benefit is worth it. Ultimately it’s a guess though.
In rare cases accepting the cost of calling a common routine
can
be a benefit: if there is an unavoidable branch in the routine that’s globally predictable, sometimes having one shared branch site can be better for the branch predictor. In many cases, though, the reverse is true: if there’s a branch in code that’s inlined many times across the codebase then sometimes the (more local) branch history for the many copies of that branch can yield more predictability. It’s…complex
.
An important consideration for inlining is the visibility of the
definition
of the function you’re calling (that is, the body of the function). If the compiler has only seen the
declaration
of a function (e.g. in the case above just
char change_case(char c, bool upper);
), then it can’t inline it: there’s nothing to inline! In modern C++ with templates and a lot of code in headers, this usually isn’t a problem, but if you’re trying to minimise build times and interdependency this can be an issue
.
Frustratingly, inlining is also one of the most heuristic-driven optimisations; with different compilers making reasonable but different guesses about which functions should be inlined. This can be frustrating when adding a single line to a function somewhere has ripple effects throughout a codebase affecting inlining decisions
.
All that said: Inlining is the ultimate enabling optimisation. On its own, copying function bodies into call sites might save a few cycles here and there. But give the compiler a fresh copy of code at the call site, and suddenly it can propagate constants, eliminate dead branches, and apply transformations that would be impossible with a shared function body. Who said copy paste was always bad?
See
the video
that accompanies this post.
This post is day 17 of
Advent of Compiler Optimisations 2025
,
a 25-day series exploring how compilers transform our code.
←
Calling all arguments
|
Partial inlining
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
