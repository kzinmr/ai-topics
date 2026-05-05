---
title: "LLVM Weekly - #127, June 6th 2016"
url: "https://blog.llvm.org/2016/06/llvm-weekly-127-june-6th-2016.html"
fetched_at: 2026-05-05T07:01:38.754686+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #127, June 6th 2016

Source: https://blog.llvm.org/2016/06/llvm-weekly-127-june-6th-2016.html

LLVM Weekly - #127, June 6th 2016
Welcome to the one hundred and twenty-seventh issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
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
The canonical home for this issue
can be found here at llvmweekly.org
.
News and articles from around the web
Graham Markall at Embecosm has been comparing the code size of
RISC-V binaries produced by the GCC and LLVM ports
, as well as compared to ARM. GCC is currently ahead, though it is worth noting the LLVM port has seen much less attention.
Matthias Reisinger is a Google Summer of Code student working on enabling polyhedral optimisations for the Julia programming language. He's written a blog post detailing his
initial steps and immediate future plans
. Hopefully we'll see more posts over the summer.
Loïc Hamot has been working on a
C++ to D converter
, implemented using Clang.
The MSVC team have blogged about the
latest release of Clang with Microsoft CodeGen
, based on Clang 3.8.
There is going to be a
clang-tidy code dojo
in Warsaw on Tuesday the 7th of June.
On the mailing lists
LLVM commits
LLVM gained support for 'SJLJ' (setjmp/longjmp) exception handling on x86 targets.
r271244
.
LLVM now requires CMake 3.4.3 to build
r271325
.
Support was added for attaching metadata to global variables.
r271348
.
The AArch64 backend switched to use SubtargetFeatures rather than testing for specific CPUs.
r271555
.
Clang commits
The release notes have been updated to explain the current level of OpenMP support (full support of non-offloading features of OpenMP 4.5).
r271263
.
Clang's source-based code coverage has been documented.
r271454
.
Other project commits
An
-fno-exceptions
libc++abi library variant was defined, to match the
-fno-exceptions
libc++ build.
r271267
.
LLDB's compact unwind printing tool gained support for ARMv7's compact unwind format.
r271744
.
