---
title: "Clever memory tricks"
url: "http://xania.org/202512/22-memory-cunningness?utm_source=feed&utm_medium=rss"
fetched_at: 2026-05-01T07:01:06.719503+00:00
source: "xania.org"
tags: [blog, raw]
---

# Clever memory tricks

Source: http://xania.org/202512/22-memory-cunningness?utm_source=feed&utm_medium=rss

Clever memory tricks
Written by me, proof-read by an LLM.
Details at end.
After exploring SIMD vectorisation over the last
couple
of
days
, let’s shift gears to look at another class of compiler cleverness: memory access patterns. String comparisons seem straightforward enough - check the length, compare the bytes, done. But watch what Clang does when comparing against compile-time constants, and you’ll see some rather clever tricks involving overlapping memory reads and bitwise operations. What looks like it should be a call to
memcmp
becomes a handful of inline instructions that exploit the fact that the comparison value is known at compile time
.
I’ve set up nine functions that each compare a
std::string_view
against a constant string of increasing length, from one to nine characters. This gives us a chance to see how the compiler’s approach changes based on the length of the comparison.
As we learned when looking at
calling conventions
, a
std::string_view
is a pointer and a length, passed in two registers on x86 Linux. Each of these functions receives a
std::size_t
length in
rdi
and a
const char *
pointer in
rsi
. One might reasonably expect a call to
memcmp
, but the compiler has both
inlined
and specialised the comparison for each constant string. Let’s take a look at some of these comparison functions, starting with
t1
:
t1:
cmp
rdi
,
1
; is length 1?
jne
.LBB0_1
; if not 1, goto "return false"
cmp
byte
ptr
[
rsi
],
65
; is the byte 65 ('A')?
sete
al
; set result to 0 or 1 accordingly
ret
; return
.LBB0_1:
xor
eax
,
eax
; set result to false
ret
; return
We see the length is checked first, and if it’s not 1, then we return. Otherwise, we check the one character to see if it’s
A
or not, and then set the return value accordingly. The compiler has used a conditional set
sete
instruction to avoid a second branch.
The pattern holds for power-of-two sizes: Looking at
t2
,
t4
and
t8
we see that the compiler does the same length check, and then cleverly realises it can compare a 2, 4 or 8-byte value directly with a constant of either
AB
,
ABCD
or
ABCDEFGH
(mouse over the constants in the view to see Compiler Explorer interpret them as ASCII).
Things get more interesting with the 7 character case,
t7
:
t7:
cmp
rdi
,
7
; is length 7?
jne
.LBB6_1
; if not, goto "return false"
mov
eax
,
1145258561
; set eax to "ABCD"
xor
eax
,
dword
ptr
[
rsi
]
; eax ^= first four chars of sv
mov
ecx
,
1195787588
; set ecx to "DEFG"
xor
ecx
,
dword
ptr
[
rsi
+
3
]
; ecx ^= chars 3,4,5,6 of sv
or
ecx
,
eax
; ecx |= eax
sete
al
; result = 1 if "zero flag" else 0
ret
; return
The check for the length is the same as the other cases, but once we know we’re going to be comparing 7 bytes, some cunning tricks come into play. First, the compiler isn’t directly comparing, as you might expect: It uses the fact that XORing identical values will result in a zero. Secondly, it has used two
overlapping
reads - reading bytes 0,1,2,3 and then 3,4,5,6. The redundant read of byte 3 doesn’t matter, but doing two 32-bit reads is cheaper than having to read individual bytes.
Once the two XORs have happened, we have “zero only if first four bytes match ABCD” in
eax
and “zero only if bytes 3,4,5,6 match DEFG” in
ecx
. Simply logical-ORing the two together gives us zero if and only if both were zero - only if all bytes matched. Then a simple
sete
turns the “zero flag” into either 0 or 1 for the
true
/
false
return value needed. Cute!
This optimisation works well on x86 as reading unaligned 32-bit values is free. You can play around with the compiler choice and see what neat tricks are conjured up by different compilers and architecture choices.
And that’s what makes modern compilers remarkable - all this cleverness is conjured up from a simple
sv == "ABCDEFG"sv
. The overlapping reads, the XOR operations, the branchless conditionals - they’re all applied automatically. Your job is to write clear code; the compiler’s job is to make it fast. Leave it to do its thing, and try not to get in its way!
See
the video
that accompanies this post.
This post is day 22 of
Advent of Compiler Optimisations 2025
,
a 25-day series exploring how compilers transform our code.
←
When SIMD Fails: Floating Point Associativity
|
Switching it up a bit
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
