---
title: "Unswitching loops for fun and profit"
url: "http://xania.org/202512/12-loop-unswitching?utm_source=feed&utm_medium=rss"
fetched_at: 2026-04-30T07:00:58.087760+00:00
source: "xania.org"
tags: [blog, raw]
---

# Unswitching loops for fun and profit

Source: http://xania.org/202512/12-loop-unswitching?utm_source=feed&utm_medium=rss

Unswitching loops for fun and profit
Written by me, proof-read by an LLM.
Details at end.
Sometimes the compiler decides the best way to optimise your loop is to… write it twice. Sounds counterintuitive? Let’s change our
sum
example from before
to optionally return a sum-of-squares
:
At
-O2
the compiler turns the ternary into:
sum += value * (squared ? value : 1);
- using a multiply and add (
mla
) instruction to do the multiply and add, and conditionally picking either
value
or the constant
1
to avoid a branch inside the loop.
However, if we turn the optimisation level up, the compiler uses a new approach:
Here the compiler realises the
bool squared
value doesn’t change throughout the loop, and decides to duplicate the loop: one copy that squares each time unconditionally, and one where it never multiplies at all. This is called “loop unswitching”.
The check of
squared
is moved out of the loop, and the appropriate loop is then selected, either
.LBB0_4
(non-squaring) or continuing to
.LBB0_2
(the squaring version).
Each loop is perfectly optimised for its duties, and it’s as if you had written:
By duplicating the loop this way, the compiler makes sure that the multiplication doesn’t happen unless you specifically asked for it. In the
-O2
code, the compiler bet on doing the multiply-and-add each time
even when it wasn’t needed. In the loop unswitching case, we do pay a code size penalty (
some
code is duplicated, after all), and that’s why loop unswitching didn’t occur on the lower optimisation setting.
As always, it’s good to trust your compiler’s decisions, but know the kinds of trade-offs it’s making at various optimisation levels. You can always verify what it’s doing with
Compiler Explorer
, after all!
See
the video
that accompanies this post.
This post is day 12 of
Advent of Compiler Optimisations 2025
,
a 25-day series exploring how compilers transform our code.
←
Pop goes the…population count?
|
Loop-Invariant Code Motion
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
