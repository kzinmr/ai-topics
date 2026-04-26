---
title: "Going loopy - Matt Godbolt’s blog"
url: "http://xania.org/202512/08-going-loopy?utm_source=feed&utm_medium=rss"
fetched_at: 2026-04-25T12:09:19.539068+00:00
source: "xania.org"
tags: [blog, raw]
---

# Going loopy - Matt Godbolt’s blog

Source: http://xania.org/202512/08-going-loopy?utm_source=feed&utm_medium=rss

Going loopy
Written by me, proof-read by an LLM.
Details at end.
Which loop style is “best”? This very question led to the creation of Compiler Explorer! In 2011 I was arguing with my team about whether we could switch all our loops from ordinal or iterator-style to the “new” range-for
. I wrote a small
shell script
to iteratively show the compiler output as I edited code in
vim
, and the seed of
Compiler Explorer
was born.
C and C++ have many ways to phrase loops:
for()
,
while()
,
do..while()
, range-for (
for (x : container)
), STL algorithms like
std::for_each
, and now range transformations! Let’s see if loop style actually matters for performance.
Let’s look at similar functions that calculate the sum of a
std::vector<int>
, using different looping strategies. First, let’s use the ordinal-based approach:
To explain the generated assembly code, we need to take a look at the innards of a
std::vector
. Internally, the vector holds three pointers: one to the beginning of the allocated data (“start”), one to the just past the end of the used data (“finish”), and a last one to the end of the storage (the space which we can grow into without reallocating). It does not explicitly store the size. Let’s look at the first few instructions:
mov
rsi
,
QWORD
PTR
[
rdi
]
; rsi = vec->start
mov
rcx
,
QWORD
PTR
[
rdi
+
8
]
; rcx = vec->finish
sub
rcx
,
rsi
; rcx = finish - start
je
.L4
; if zero; early return
sar
rcx
,
2
; rcx >>= 2 (divide by sizeof(int))
; rcx = vec.size()
xor
eax
,
eax
; eax = 0 (this will be "index")
xor
edx
,
edx
; edx = 0 (this will be "sum")
The first thing we do is get the start and finish pointers of the vector, and then subtract them to work out the size (returning early if it’s zero). So far so good! (The .L4 label just returns 0, so I’ll ignore it in this description).
Next we see the loop itself:
.L3:
add
edx
,
DWORD
PTR
[
rsi
+
rax
*
4
]
; edx += *(int*)(start + index*4)
add
rax
,
1
; ++index
cmp
rax
,
rcx
; if index == size?
jb
.L3
; if not, loop
mov
eax
,
edx
; return "sum"
ret
Here we see the slightly bonkers x86 addressing mode we touched on in the
earlier lea post
which lets us read a value from memory calculated from the start plus the index (times four, as each
int
is four bytes),
and
add it in a single instruction. CISC, am I right?
Anyway, everything seems ok in this loop, right? Except, it bothers me that we calculate the size at all. I mean, we don’t
really
care what size it is, we just want to iterate over every element, right?
How about we rephrase this to use the pointers directly? We can fish out the start pointer with
.data()
, and calculate the end pointer by adding the size (and hope the optimiser spots it doesn’t need to
actually
use the size, it can just use the
end
directly). What does that look like?
That’s
much
better! The optimiser
has
avoided all the shifts and size calculation in the setup code, and the inner loop is simply reading and walking a pointer forward.
Any time you see C++ code with naked pointers in it, you should ask yourself if there’s a better way, though. So, let’s see what would happen if we used the fancy range-for:
Exactly
the same code as our
while
-based, pointer approach! The compiler canonicalised the range-for into identical assembly. Less error-prone pointer manipulation, more intention-revealing C++ code,
and
the best code generation!
Even with a standard algorithm, the pattern continues:
Identical again! Canonicalisation rewrites all these different loop forms into the same basic setup, generating optimal code every time
. Whether you write explicit loops or use standard algorithms, the compiler sees through to the underlying iteration pattern. Write clear, intention-revealing code - the optimiser has your back.
See
the video
that accompanies this post.
This post is day 8 of
Advent of Compiler Optimisations 2025
,
a 25-day series exploring how compilers transform our code.
←
Multiplying our way out of division
|
Induction variables and loops
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
