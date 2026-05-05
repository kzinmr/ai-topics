---
title: "LLVM Weekly - #72, May 18th 2015"
url: "https://blog.llvm.org/2015/05/llvm-weekly-72-may-18th-2015.html"
fetched_at: 2026-05-05T07:01:40.583816+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #72, May 18th 2015

Source: https://blog.llvm.org/2015/05/llvm-weekly-72-may-18th-2015.html

LLVM Weekly - #72, May 18th 2015
Welcome to the seventy-second issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
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
Some of you may be interested that over at the lowRISC project, we've announced the
full set of summer student projects
we're supporting.
The canonical home for this issue
can be found here at llvmweekly.org
.
News and articles from around the web
The Rust programming language, which of course uses LLVM as its compiler backend, has just
released version 1.0
.
The next Cambridge LLVM Social will
take place on Wednesday 20th May
at the Cambridge Beer Festival.
On the mailing lists
LLVM commits
The ARM backend has been updated to use AEABI aligned function variants.
r237127
.
The heuristic for estimating the effect of complete loop unrolling has been reimplemented.
r237156
.
Statepoints are now 'patchable'.
r237214
.
Support for function entry count metadata has been added.
r237260
.
A new loop distribution pass has been born. It is off by default.
r237358
.
New SelectionDAG nodes have been added for signed/unsigned min/max.
r237423
.
A simple speculative execution pass, targeted mainly at GPUs has been added.
r237459
.
Clang commits
The little endian SPARC target has been added to clang.
r237001
.
clang-format's formatter has undergone some refactoring, which also led to a few bug fixes.
r237104
.
Documentation on adding new attributes has seen a significant update.
r237268
.
Other project commits
libcxx learnt
std::experimental::sample
r237264
.
lldb has enabled multithreaded debugging on Windows.
r237392
.
lldb can now set and clear hardware watchpoints and breakpoints on AArch64.
r237419
.
lldb gained an assembly profiler for mips32.
r237420
.
