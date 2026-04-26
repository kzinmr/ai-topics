---
title: "When LICM fails us"
url: "http://xania.org/202512/14-licm-when-it-doesnt?utm_source=feed&utm_medium=rss"
fetched_at: 2026-04-25T12:09:16.590392+00:00
source: "xania.org"
tags: [blog, raw]
---

# When LICM fails us

Source: http://xania.org/202512/14-licm-when-it-doesnt?utm_source=feed&utm_medium=rss

When LICM fails us
Written by me, proof-read by an LLM.
Details at end.
Yesterday’s LICM post
ended with the compiler pulling invariants like
size()
and
get_range
out of our loop - clean assembly, great performance. Job done, right?
Not quite. Let’s see how that optimisation can disappear.
Let’s say you had a
const char *
, and wanted to write a function to return if there was an exclamation mark or not:
Here we’re relying on loop-invariant code motion (LICM) to move the
strlen
out of the loop, called once before we loop, and then the loop is:
.L4:
add
rdi
,
1
; ++index
cmp
BYTE
PTR
[
rdi-1
],
33
; is string[index-1] a '!' ?
je
.L5
; if so, jump to "return true"
.L2:
cmp
rdi
,
rax
; else...are we at the end?
jne
.L4
; loop if not
All pretty good. We’ll learn in later posts
that we can improve on this simple loop, but for now this seems ok.
Now let’s assume we were curious how many characters in total we were comparing across our entire program, and add some basic instrumentation
:
We might reasonably expect a single increment to be added to our loop. But if we take a closer look:
.L4:
add
QWORD
PTR
num_compares
[
rip
],
1
; ++num_compares;
cmp
BYTE
PTR
[
rbp
+
0
+
rbx
],
33
; is char a '!' ?
je
.L5
; if so, jump to "return true"
add
rbx
,
1
; ++index
.L2:
mov
rdi
,
rbp
; er...
call
strlen
; what the heck? strlen?
cmp
rbx
,
rax
; oh no! what happened?
jb
.L4
; loop if index != strlen(...)
Suddenly we’ve lost our lovely LICM! By simply incrementing a global variable
, we lost the ability to call
strlen
and keep the result. Why is this?
It comes down to aliasing: the compiler can’t prove that the string we’re getting the length of doesn’t share memory with the
num_compares
variable! Every time we modify
num_compares
the compiler has to assume that
maybe
the string changed as a result!
This seems pretty odd: why on earth would a string overlap with a
std::size_t
? Don’t we have rules about this? Aren’t we disallowed from doing such things - type punning is barred - at least in C++?
Unfortunately,
char*
has a
special
status in the standard
: it’s allowed to alias with
anything
. That’s why the compiler can’t assume our string and
num_compares
occupy different memory! If we had any other type than
char *
then the compiler
could
use LICM.
At least, that’s what I hoped. In practice neither GCC
, clang
nor MSVC were able to LICM the code I tried. I could easily be missing something here, so do let me know if you have any ideas.
Today’s post seems a bit of a downer: the compiler wasn’t able to do an optimisation I had otherwise hoped it might. Tomorrow we’ll look at some other examples where the compiler struggles with aliasing, and we’ll see how to help it out.
See
the video
that accompanies this post.
This post is day 14 of
Advent of Compiler Optimisations 2025
,
a 25-day series exploring how compilers transform our code.
←
Loop-Invariant Code Motion
|
Aliasing
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
