---
title: "When compilers surprise you"
url: "http://xania.org/202512/24-cunning-clang?utm_source=feed&utm_medium=rss"
fetched_at: 2026-04-28T07:01:43.936116+00:00
source: "xania.org"
tags: [blog, raw]
---

# When compilers surprise you

Source: http://xania.org/202512/24-cunning-clang?utm_source=feed&utm_medium=rss

When compilers surprise you
Written by me, proof-read by an LLM.
Details at end.
Every now and then a compiler will surprise me with a really smart trick. When I first saw this optimisation I could hardly believe it. I was looking at loop optimisation, and wrote something like this simple function that sums all the numbers up to a given value:
So far so decent: GCC has done some preliminary checks, then fallen into a loop that efficiently sums numbers using
lea
(we’ve
seen this before
). But taking a closer look at the loop we see something unusual:
.L3:
lea
edx
,
[
rdx
+
1
+
rax
*
2
]
; result = result + 1 + x*2
add
eax
,
2
; x += 2
cmp
edi
,
eax
; x != value
jne
.L3
; keep looping
The compiler has cleverly realised it can do two numbers
at a time using the fact it can see we’re going to add
x
and
x + 1
, which is the same as adding
x*2 + 1
. Very cunning, I think you’ll agree!
If you turn the optimiser up to
-O3
you’ll see the compiler works even harder to vectorise the loop using parallel adds. All very clever.
This is all for GCC. Let’s see what clang does with our code:
This is where I nearly fell off my chair:
there is no loop
! Clang checks for positive
value
, and if so it does:
lea
eax
,
[
rdi
-
1
]
; eax = value - 1
lea
ecx
,
[
rdi
-
2
]
; ecx = value - 2
imul
rcx
,
rax
; rcx = (value - 1) * (value - 2)
shr
rcx
; rcx >>= 1
lea
eax
,
[
rdi
+
rcx
]
; eax = value + rcx
dec
eax
; --eax
ret
It was not at all obvious to me what on earth was going on here. By backing out the maths a little, this is equivalent to:
v + ((v - 1)(v - 2) / 2) - 1;
Expanding the parentheses:
v + (v² - 2v - v + 2) / 2 - 1
Rearranging a bit:
(v² - 3v + 2) / 2 + (v - 1)
Multiplying the
(v - 1)
by 2 / 2:
(v² - 3v + 2) / 2 + (2v - 2)/2
Combining those and cancelling:
Simplifying and factoring gives us
v(v - 1) / 2
which is the closed-form solution to the “sum of integers”! Truly amazing
- we’ve gone from an O(n) algorithm as written, to an O(1) one!
I love that despite working with compilers for more than twenty years, they can still surprise and delight me. The years of experience and work that have been poured into making compilers great is truly humbling, and inspiring.
We’re nearly at the end of this series - there’s so much more to say but that will have to wait for another time. Tomorrow will be a little different: see you then!
See
the video
that accompanies this post.
This post is day 24 of
Advent of Compiler Optimisations 2025
,
a 25-day series exploring how compilers transform our code.
←
Switching it up a bit
|
Thank you
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
