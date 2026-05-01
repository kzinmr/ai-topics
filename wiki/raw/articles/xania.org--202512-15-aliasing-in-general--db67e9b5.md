---
title: "Aliasing - Matt Godbolt’s blog"
url: "http://xania.org/202512/15-aliasing-in-general?utm_source=feed&utm_medium=rss"
fetched_at: 2026-05-01T07:01:07.174830+00:00
source: "xania.org"
tags: [blog, raw]
---

# Aliasing - Matt Godbolt’s blog

Source: http://xania.org/202512/15-aliasing-in-general?utm_source=feed&utm_medium=rss

Aliasing
Written by me, proof-read by an LLM.
Details at end.
Yesterday
we ended on a bit of a downer: aliasing stopped optimisations dead in their tracks. I know this is supposed to be the
Advent of Compiler Optimisations
, not the
Advent of Compiler Giving Up
! Knowing why your compiler can’t optimise is just as important as knowing all the clever tricks it can pull off.
Let’s take a simple example of a counter class
. It accumulates integers into a member variable
total
. I’ve used C++ templates to show two versions of the code: one that accumulates in an
int
and one that accumulates in an
long
.
At first glance, the two loop bodies look almost identical, as you might expect. In one case we’ll accumulate in
eax
, and the other in
rax
, right? The truth is more subtle. Let’s first look at the
int
case:
mov
eax
,
DWORD
PTR
[
rdi
]
; eax = total
.L3:
add
eax
,
DWORD
PTR
[
rsi
]
; add element to total
add
rsi
,
4
; move to next element
mov
DWORD
PTR
[
rdi
],
eax
; total = eax
cmp
rsi
,
rdx
; are we finished?
jne
.L3
; loop if not
ret
Looks pretty reasonable, right? Now let’s look at the
long
version:
mov
rax
,
QWORD
PTR
[
rdi
]
; rax = total
.L9:
movsx
rdx
,
DWORD
PTR
[
rsi
]
; read & sign extend next element
add
rsi
,
4
; move to next element
add
rax
,
rdx
; rax += element
cmp
rcx
,
rsi
; are we finished?
jne
.L9
; loop if not
mov
QWORD
PTR
[
rdi
],
rax
; total = rax
ret
; return
The first change from the 32-bit case you’ll notice is the
movsx
to turn the 32-bit signed integer into a 64-bit signed integer. That’s all but free on modern CPUs, and so while it looks like the loop is doing more work than the 32-bit version, it’s not as bad as it seems.
The important difference here is the update of
total
: In the first version, each loop iteration updates the member variable
total
. In the second version everything remains in registers until the end of the loop, and then
total
is only updated at the end. CPU caches are super fast, but it’s still best to avoid redundant stores in hot loops!
So, why this difference? Of course it’s aliasing: In the
int
version the compiler can’t be sure that the
span
passed in to
count
doesn’t cover the
Counter
’s member variable
total
. They are the same type, and so that would be perfectly OK by the type-based aliasing rules of C++.
In the
long
version, the types differ (
int
vs
long
), and under C++’s strict aliasing rules, it would be undefined behaviour for them to overlap in memory. Since the compiler can assume the program doesn’t invoke undefined behaviour, it knows they don’t alias and can safely optimise. That lets it cache the
total
in a register and only update the member variable at the end. As we’ll see later in the series, being aliasing-free helps other optimisations too, like vectorisation.
To fix this issue, we have a couple of choices. The easy way would be to rewrite to accumulate in a local variable, and then update the total at the end: Using
total += std::accumulate(span.begin(), span.end(), 0)
would fix this
and
be more intention-revealing.
The other, non-standard way to work around this issue is to use
__restrict
. This GNU extension (borrowed from C) lets us decorate pointers and essentially promises that this pointer uniquely refers to the object it points at. In our case, the thing we need to prove is unique is the
Counter
’s “this pointer” itself. Adding
__restrict
after the parameter list (where you would add
const
for a const member function) works. But again - this is very non-standard, so use at your peril
.
Aliasing is one of C++’s sneakier gotchas, especially when you’re working with base types like
int
and
float
- you can’t avoid using them, and they’re prime candidates for aliasing with each other
. It’s perfectly legal to have overlapping same-type pointers, so the compiler assumes the worst and peppers your hot loops with memory accesses. The fix may be as simple as only using local variables within your loop - but first you have to spot it. Fire up
Compiler Explorer
, look for those unexpected writes to memory when you’d expect everything to stay in registers, and you’ll know when aliasing is holding you back!
See
the video
that accompanies this post.
This post is day 15 of
Advent of Compiler Optimisations 2025
,
a 25-day series exploring how compilers transform our code.
←
When LICM fails us
|
Calling all arguments
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
