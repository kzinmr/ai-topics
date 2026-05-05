---
title: "LLVM Weekly - #76, Jun 15th 2015"
url: "https://blog.llvm.org/2015/06/llvm-weekly-76-jun-15th-2015.html"
fetched_at: 2026-05-05T07:01:40.402531+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #76, Jun 15th 2015

Source: https://blog.llvm.org/2015/06/llvm-weekly-76-jun-15th-2015.html

LLVM Weekly - #76, Jun 15th 2015
Welcome to the seventy-sixth issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
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
The big news this week is that Apple have announced Swift 2.0 and, perhaps more importantly, that
Swift will be open source later this year
. The intention is that iOS, OS X and Linux will be supported at release.
On the mailing lists
LLVM commits
The loop vectorizer gained an optimisation for interleaved memory access. It is disabled by default but can be turned on using
-enable-interleaved-mem-accesses=true
. An AArch64InterleavedAccess pass was also added.
r239291
,
r239514
.
A prototype for 32-bit SEH (Structured Exception Handling) has been added.
r239433
.
LLVM has grown LibDriver and llvm-lib, intended to provide a lib.exe compatible utility.
r239434
.
x86 gained a new reassociation MachineCombiner optimisation to increase ILP.
r239486
.
The R600 backend has now been renamed to AMDGPU.
r239657
.
Clang commits
Support for C99 partial re-initialization behaviour has been implemented.
r239446
.
Clang gained support for the BPF backend.
r239496
.
The loop vectorize pragma now recognises
assume_safety
. This will tell loop access analysis to skip memory dependency checking.
r239572
.
The target attribute is now supported. Much like GCC's target attribute, it allows adding subtarget features and changing the CPU for a particular function.
r239579
.
Other project commits
The COFF linker in LLD continues to get faster.
r239332
,
r239292
.
LLD grew a TypeSystem interface to support adding non-clang languages (though it seems it's reverted for now).
r239360
.
