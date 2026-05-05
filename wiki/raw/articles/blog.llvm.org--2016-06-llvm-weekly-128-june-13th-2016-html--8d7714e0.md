---
title: "LLVM Weekly - #128, June 13th 2016"
url: "https://blog.llvm.org/2016/06/llvm-weekly-128-june-13th-2016.html"
fetched_at: 2026-05-05T07:01:38.823444+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #128, June 13th 2016

Source: https://blog.llvm.org/2016/06/llvm-weekly-128-june-13th-2016.html

LLVM Weekly - #128, June 13th 2016
Welcome to the one hundred and twenty-eighth issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
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
LDC, a compiler for the D programming language with an LLVM backends has a
major release with 1.0.0
. The big news with this release is that the frontend is now completely written in D. Congratulations to everyone involved in this release. See
the D website
for more information about the D programming language.
The minor release LLVM 3.8.1-rc1
has been tagged
.
On the mailing lists
LLVM commits
Some of the work from the GSoC project on interprocedural register allocation has started to land. A RegUsageInfoCollector analysis was added that collects the list of clobbered registers for a MachineFunction. A new transformation pass was committed which scans the body of a function to find calls and updates the register mask with the one saved by RegUsageInfoCollector.
r272403
,
r272414
.
Chapter 2 of the tutorial on building a JIT with ORC has been fleshed out with a rough draft of the text.
r271885
.
The host CPU detection code for x86 has seen a large refactoring.
r271921
.
More documentation has been added about LLVM's CodeView support.
r272057
.
llvm-symbolizer will now be searched for in the same directory as the LLVM or Clang tool being executed. This increases the chance of being able to print pretty backtraces for systems where LLVM tools aren't installed in the $PATH.
r272232
.
Clang commits
Clang analyzer gained a checker for correct usage of the MPI API in C and C++.
r271907
.
Documentation was added on avoiding static initializers when using profiling.
r272067
,
r272214
.
Other project commits
A hardened allocator, 'scudo' was added to compiler-rt. It attempts to mitigate some common heap-based vulnerabilities.
r271968
.
Initial support for ARM has landed in LLD. This is just enough to link a hello world on ARM Linux.
r271993
.
Initial support for AddressSanitizer on Win64 was added.
r271915
.
