---
title: "LLVM Weekly - #43, Oct 27th 2014"
url: "https://blog.llvm.org/2014/10/llvm-weekly-43-oct-27th-2014.html"
fetched_at: 2026-05-05T07:01:41.410381+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #43, Oct 27th 2014

Source: https://blog.llvm.org/2014/10/llvm-weekly-43-oct-27th-2014.html

LLVM Weekly - #43, Oct 27th 2014
Welcome to the forty-third issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
Alex Bradbury
. Subscribe to future issues at
http://llvmweekly.org
and pass it on to anyone else you think may be interested. Please send any tips or feedback to
asb@asbradbury.org
, or
@llvmweekly
or
@asbradbury
on Twitter.
This week it's the LLVM Developers' Meeting in San Jose. Check out the
schedule
. Unfortunately I won't be there, so I'm looking forward to the slides and videos going online.
The canonical home for this issue
can be found here at llvmweekly.org
.
News and articles from around the web
Philip Reames has written up a detailed
discussion of statepoints vs gcroot
for representing call safepoints. The aim is to clearly explain how the safepoint functionality provided by the
patches currently up for review
differ to the current gc.root support.
The Haskell community have put together a
proposal for an improved LLVM backend to GHC
. They intend to ship GHC with its own local LLVM build.
CoderGears have published a blog post about
using Clang to get better warnings in Visual C++ projects
.
There is going to be a dedicated LLVM devroom at FOSDEM 2015. Here is the
call for speakers and participation
.
On the mailing lists
LLVM commits
The
nonnull
metadata has been introduced for Load instructions.
r220240
.
minnum and maxnum intrinsics have been added.
r220341
,
r220342
.
The Hexagon backend gained a basic disassembler.
r220393
.
PassConfig gained usingDefaultRegAlloc to tell if the default register allocator is being used.
r220321
.
An llvm-go tool has been added. It is intended to be used to build components such as the Go frontend in-tree.
r220462
.
Clang commits
C compilation defaults to C11 by default, matching the behaviour of GCC 5.0.
r220244
.
Clang should now be better at finding Visual Studio in non-standard setups.
r220226
.
The Windows toolchain is now known as MSVCToolChain, to allow the addition a CrossWindowsToolChain which will use clang/libc++/lld.
r220362
,
r220546
.
Other project commits
The libcxxabi gained support for running libc++abi tests with sanitizers.
r220464
.
