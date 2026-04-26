---
title: "Loop-Invariant Code Motion"
url: "http://xania.org/202512/13-licking-licm?utm_source=feed&utm_medium=rss"
fetched_at: 2026-04-25T12:09:17.133241+00:00
source: "xania.org"
tags: [blog, raw]
---

# Loop-Invariant Code Motion

Source: http://xania.org/202512/13-licking-licm?utm_source=feed&utm_medium=rss

Loop-Invariant Code Motion
Written by me, proof-read by an LLM.
Details at end.
Look back at
our simple loop example
- there’s an optimisation I completely glossed over. Let me show you what I mean:
On every loop iteration we are calling
vec.size()
to compare the index value, and to check if the index has reached the end of the vector. However, looking in the assembly, the compiler has pulled the size calculation
out of the loop entirely - the
sar
that divides the “end - start” value by the size of an int is only performed
before
the loop! The compiler quietly rewrote our code to be:
Such a transformation is called Loop-Invariant Code Motion, or LICM. It’s not just expressions in the
for
clauses themselves, any code inside the loop that the compiler can prove doesn’t depend on which iteration it’s in is fair game.
Let’s give our loop something more to do: We’ll take a
std::string_view
and count how many characters fall within a given range (being “capital letters” or “numerics”)
. We’ll write it naively, using a
get_range()
function that returns the min and max character “in range” as a pair:
You can see that clang
here has realised the range from
get_range
cannot change during the loop and so has moved it outside:
count_in_range:
; ...preamble removed for brevity...
call
get_range
(
RangeType
)
@
PLT
; call get_range (OUTSIDE OF LOOP)
movsx
ecx
,
al
; ecx = range.first
shr
eax
,
8
movsx
edx
,
al
; edx = range.second
xor
esi
,
esi
; esi = loop counter = 0
xor
eax
,
eax
; eax = num = 0
.LBB0_4:
movsx
edi
,
byte
ptr
[
rbx
+
rsi
]
; read next c
cmp
ecx
,
edi
; compare with first
setle
r8b
; r8b = c >= first
cmp
edx
,
edi
; compare with second
setge
dil
; dil = c <= second
and
dil
,
r8b
; dil = dil & r8b
; ie 1 if c in range, else 0
movzx
edi
,
dil
; edi = (zero extended) dil
add
rax
,
rdi
; num += (1 if in range, else 0)
inc
rsi
; increment loop counter
cmp
r14
,
rsi
; are we done?
jne
.LBB0_4
; loop if not
; ...postamble/return removed for brevity...
Clang has also played some other neat tricks
here to avoid a branch inside the loop using
setle
and
setge
to get a 0 or 1 based on a condition code.
Usually I end with a “trust the compiler” type sentiment. However, in this case I was surprised that gcc wasn’t able to perform code motion here
. I guess that’s what
Compiler Explorer
is for: Trust the compiler, but know how to verify its output too.
See
the video
that accompanies this post.
This post is day 13 of
Advent of Compiler Optimisations 2025
,
a 25-day series exploring how compilers transform our code.
←
Unswitching loops for fun and profit
|
When LICM fails us
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
