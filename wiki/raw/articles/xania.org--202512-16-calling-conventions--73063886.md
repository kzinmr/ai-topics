---
title: "Calling all arguments"
url: "http://xania.org/202512/16-calling-conventions?utm_source=feed&utm_medium=rss"
fetched_at: 2026-04-29T07:01:05.546204+00:00
source: "xania.org"
tags: [blog, raw]
---

# Calling all arguments

Source: http://xania.org/202512/16-calling-conventions?utm_source=feed&utm_medium=rss

Calling all arguments
Written by me, proof-read by an LLM.
Details at end.
Today we’re looking at calling conventions
- which aren’t purely optimisation related but are important to understand. The calling convention is part of the ABI (Application Binary Interface), and varies from architecture to architecture and even OS to OS. Today I’ll concentrate on the System V ABI for x86 on Linux, as (to me) it’s the most sane ABI.
Before we go on: I’d be remiss if I didn’t point out that I can
never
remember which register has what in it, and for years I had a Post It note on my monitor with a hand-written crib sheet of the ABI. While on holiday I had an idea: Why not put the ABI on a mug! I created these ABI mugs and you can get your own one - and support Compiler Explorer - at the
Compiler Explorer shop
.
The Compiler Explorer ABI mug: Get yours at the
CE Shop!
We’ve already touched on calling conventions as I’ve commented the assembly in previous days, but concretely, for x86 Linux, the first couple of parameters go in
rdi
and
rsi
. This makes sense for discrete integer types, and even pointers. What about structures? Let’s compare two functions:
With
ArgType
set to
long
it might surprise you that the body of those two functions are identical! Both are just
lea rax, [rdi+rsi]
: We expect the separate arguments to be in
rdi
and
rsi
, but passing that larger structure by value
also
got placed in
rdi
and
rsi
. Neat!
If you explore by changing the
ArgType
you’ll see that the compiler has to do more work if we don’t (conveniently) use
long
s here. For example, changing to
int
changes the separate argument version to
lea eax...
to reflect the 32-bit return value, but the body of the structure version becomes:
; structure is _packed_ into rdi as "y<<32 | x"
mov
rax
,
rdi
; rax = args.y<<32 | args.x
shr
rax
,
32
; rax >>= 32; rax is now 'y'
add
eax
,
edi
; y += x;
ret
It’s a little tricky to follow as the compiler is cunningly switching between the 64-bit
r
prefixed register names and the 32-bit
e
versions, but you can see that, for the cost of a couple more instructions we still passed the structure pretty efficiently, and in a single register.
It gets more interesting when we pass
lots
of arguments
. Even on System V ABI, only the first 6 parameters are passed in registers. After that, it spills to the stack. Let’s update our example to pass many arguments to show this:
In this case we can see the separate args version adding all the registers, and then having to get some off the stack:
add rax, QWORD PTR [rsp+8]
and so on. On the structure side, the whole structure
is copied to the stack, which seems bad
.
However! Changing
ArgType
to
char
and you’ll see an interesting difference. The separate args version is similar, though it can’t use
lea
any more, and has to sign-extend all the values its getting from its registers. The struct args version has no stack spillage: our entire
StructArgs
structure fits into one register! The compiler has a bit of a time shifting it around to extract each
char
, but it’s not having to spill to the stack at least. In my testing, different compilers used different tricks, so play around with the
ArgType
and compiler (e.g. clang) and get a sense of what it can do
.
So, all this is pretty abstract: why is this important? Sometimes knowing the ABI, and how the compiler can optimise around it can inform your design. There was some debate about the design of
std::string_view
and
std::optional
and their usefulness
: these are types that are convenient to pass
by value
, and so their footprint in registers is important
.
Overall, knowing the calling convention helps you make smart decisions about layout and parameter passing that give the compiler the best shot at generating efficient code.
See
the video
that accompanies this post.
This post is day 16 of
Advent of Compiler Optimisations 2025
,
a 25-day series exploring how compilers transform our code.
←
Aliasing
|
Inlining - the ultimate optimisation
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
