---
title: "Multiplying our way out of division"
url: "http://xania.org/202512/07-division-again?utm_source=feed&utm_medium=rss"
fetched_at: 2026-04-28T07:01:44.963628+00:00
source: "xania.org"
tags: [blog, raw]
---

# Multiplying our way out of division

Source: http://xania.org/202512/07-division-again?utm_source=feed&utm_medium=rss

Multiplying our way out of division
Written by me, proof-read by an LLM.
Details at end.
I occasionally give presentations to undergraduates, and one of my favourites is taking the students on a journey of optimising a “binary to decimal” routine
. There are a number of tricks, which I won’t go in to here, but the opening question I have is “how do you even turn a number into its ASCII representation?”
If you’ve never stopped to think about it, take a moment now to do so, it can be a fun problem.
The simple
approach is to use
number % 10
to get the rightmost digit (adding 48 to turn it into the ASCII number), then divide by ten, and keep going until the number is zero. This produces the digits backwards
, but you can reverse them afterwards, which I won’t show here. This routine is one of the few legitimate uses of
do while
in C, as we always want to emit at least one digit even if the number
is
zero to start with. The code looks something like:
Here the compiler does a fantastic job.
Yesterday
we saw how division by powers of two can be optimised to shifts; today we’ll see the compiler manages to avoid expensive division even when we
aren’t
dividing by a power of two. It also gets the remainder cheaply, which we usually get for free from the divide instruction.
The transformation is quite clever - let’s walk through the annotated assembly:
to_decimal_backwards
(
unsigned
int
,
char
*):
mov
rax
,
rsi
; rax = buf
mov
esi
,
3435973837
; esi = 0xcccccccd
.L2:
mov
edx
,
edi
; edx = number
mov
ecx
,
edi
; ecx = number
add
rax
,
1
; ++buf
imul
rdx
,
rsi
; rdx *= 0xcccccccd
shr
rdx
,
35
; rdx = rdx >> 35
; rdx = number / 10 [see below]
lea
r8d
,
[
rdx
+
rdx
*
4
]
; r8 = rdx * 5
add
r8d
,
r8d
; r8 = rdx * 5 * 2 = rdx * 10
; r8 = (number / 10) * 10 [rounded down]
sub
ecx
,
r8d
; ecx = number - (number / 10) * 10
; ecx = number % 10
add
ecx
,
48
; ecx = '0' + (number % 10)
cmp
edi
,
9
; number > 9?
mov
edi
,
edx
; number = number / 10
mov
BYTE
PTR
[
rax-1
],
cl
; *(buf-1) = '0' + (number % 10)
ja
.L2
; loop if number (prior to divide) >= 10
ret
There’s a lot to unpack here, several different optimisations, but the main one is how the compiler has turned division by a constant ten into a multiply and a shift. There’s a magic constant
0xcccccccd
and a shift right of 35! Shifting right by 35 is the same as dividing by 2
35
- what’s going on?
Let’s see what happens each step of the algorithm:
>>>
1234
*
0xcccccccd
4239991714858
>>>
4239991714858
//
(
2
**
35
)
123
>>>
123
*
10
1230
>>>
1234
-
1230
4
What’s happening is that
0xcccccccd / 2**35
is very close to ⅒ (around 0.10000000000582077). By multiplying our input value by this constant first, then shifting right, we’re doing fixed-point multiplication by ⅒ - which is division by ten. The compiler knows that for all possible unsigned integer values, this trick will always give the right answer. For other values and signednesses, sometimes it needs to account for rounding, for example, dividing a signed value by three:
Here we see that it has to account for rounding. If you edit the code above and try dividing by fifteen, you’ll see that causes even more code to be emitted. However, it’s all still faster than a real divide instruction.
Back to our ASCII conversion example, to get the remainder (the modulus); the compiler takes the (truncated)
number / 10
, multiplies it back up by 10 using
lea
tricks (we’ve covered this
before
), and then the difference between the original number and this computed value is the remainder.
The rest of the optimisations are the compiler trying to do work eagerly (like incrementing
buf
), and checking one loop iteration ahead: there’s no point looping if the current number is less than or equal to 9.
Overall, some very clever optimisations that avoid division entirely!
See
the video
that accompanies this post.
This post is day 7 of
Advent of Compiler Optimisations 2025
,
a 25-day series exploring how compilers transform our code.
←
Division
|
Going loopy
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
