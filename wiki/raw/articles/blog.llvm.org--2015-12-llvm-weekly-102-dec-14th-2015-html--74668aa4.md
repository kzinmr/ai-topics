---
title: "LLVM Weekly - #102, Dec 14th 2015"
url: "https://blog.llvm.org/2015/12/llvm-weekly-102-dec-14th-2015.html"
fetched_at: 2026-05-05T07:01:39.630543+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #102, Dec 14th 2015

Source: https://blog.llvm.org/2015/12/llvm-weekly-102-dec-14th-2015.html

LLVM Weekly - #102, Dec 14th 2015
Welcome to the one hundred and second issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
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
Version 1.5 of the Rust programming language
has been released
. Rust of course uses LLVM as its backend.
George Balatsouras has written a blog post on
compiling a project using autotools to LLVM bitcode
.
On the mailing lists
LLVM commits
A new minimum spanning tree based method of instrumenting code for profile-guided optimisation was added. This guarantees the minimum number of CFG edges are instrumented.
r255132
.
MatchBSwap in InstCombine will now also detect bit reversals.
r255334
.
Sample-based profile-guided optimisation memory usage has been reduced by 10x by changing from using a DenseMap for sample records to a std::map.
r255389
.
An
Instruction::getFunction
method was added. It's perhaps surprising this didn't exist before.
r254975
.
FP16 vector instructions defined in ARMv8.2-A are now supported.
r255010
.
The EarlyCSE (common subexpression elimination) pass learned to perform value forwarding for unordered atomics.
r255054
.
Debug info in LLVM IR can now refer to macros.
r255245
.
LLVM's developer policy has been updated to detail the currently accepted C API stability policy and other guidelines.
r255300
.
A massive rework of funclet-oriented exception handling (needed for Windows exceptions) has landed.
r255422
.
Clang commits
Clang gained an option to use the new ThinLTO pipeline.
r254927
.
Hexagon will use the integrated assembler by default.
r255127
.
dllexport and dllimport attributes are now exposed through the libclang API.
r255273
.
Other project commits
