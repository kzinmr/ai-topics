---
title: "Switching it up a bit"
url: "http://xania.org/202512/23-switching-it-up?utm_source=feed&utm_medium=rss"
fetched_at: 2026-04-30T07:00:57.332739+00:00
source: "xania.org"
tags: [blog, raw]
---

# Switching it up a bit

Source: http://xania.org/202512/23-switching-it-up?utm_source=feed&utm_medium=rss

Switching it up a bit
Written by me, proof-read by an LLM.
Details at end.
The standard wisdom is that switch statements compile to jump tables. And they do - when the compiler can’t find something cleverer to do instead.
Let’s start with a really simple example:
Here the compiler has spotted the relationship between
x
and the return value, and rewritten the code as:
if (x < 5) return (x+1) * 100; else return 0;
- pretty neat. No jump table, just maths!
If we mix up the code a bit so there’s no obvious relationship between the input and the return value:
Still no jump table: Now the compiler has built a bespoke lookup table (
CSWTCH.1
) and then uses
x
to index into it (after checking it’s in bounds).
For “dense” case statements, like the ones above, the compiler can be smart. But even with relatively sparse inputs, the compiler can work its magic. Consider this “is it whitespace?” routine
:
That
still
avoids any kind of jump table; and in fact even avoids a branch:
is_whitespace
(
char
):
sub
edi
,
9
; edi = x - 9 (`\t`)
mov
eax
,
8388631
; eax = 0b100000000000000000010111
bt
rax
,
rdi
; test bit edi in the eax bitmask
setc
al
; al = (bit was set) ? 1 : 0
xor
edx
,
edx
; edx = 0
cmp
dil
,
24
; compare edi with 24
cmovnb
eax
,
edx
; replace al with edx (0) if not below
ret
; return
The compiler has built a bitmask where each bit says “should we consider this character to be whitespace”. To fit the range of bits needed to cover all the whitespace characters, the compiler indexes into the bitmask with
(x - 9)
. The bit test instruction (
bt
) will test any bit position, but our 32-bit bitmask only has meaningful data in positions 0-31. The compiler checks that
(x - 9) <= 24
to ensure we’re within the valid range
of the bitmask (covering tab at position 0 through space at position 23), and replaces the result with 0 for anything outside this range.
Just to see what else the compiler can generate, let’s take a look at both a dense and sparse example that the compiler can’t replace with a table (you’ll need to scroll around in the Compiler Explorer panes to see more):
For the dense case, the compiler does make a jump table, and indexes by
x
to jump to the right
func
routine
. For the sparse case, the compiler has to fall back to essentially a set of
if()
statements, comparing and branching. However, it’s clever enough to compare a “mid-range” value first (
2511
), and if the
x
value is greater, jumps to code that only looks at the
5284
and
4865
. So it’s essentially a binary serarch tree of comparisons.
Different compilers employ quite different tricks, so take some time to see what clang does for all the above examples.
Write clear switch statements; let the compiler decide whether that means multiplication, bitmasks, or jump tables. It’s pretty darned good at it!
See
the video
that accompanies this post.
This post is day 23 of
Advent of Compiler Optimisations 2025
,
a 25-day series exploring how compilers transform our code.
←
Clever memory tricks
|
When compilers surprise you
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
