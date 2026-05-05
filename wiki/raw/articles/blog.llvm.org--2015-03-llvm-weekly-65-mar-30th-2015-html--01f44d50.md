---
title: "LLVM Weekly - #65, Mar 30th 2015"
url: "https://blog.llvm.org/2015/03/llvm-weekly-65-mar-30th-2015.html"
fetched_at: 2026-05-05T07:01:40.781373+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #65, Mar 30th 2015

Source: https://blog.llvm.org/2015/03/llvm-weekly-65-mar-30th-2015.html

LLVM Weekly - #65, Mar 30th 2015
Welcome to the sixty-fifth issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
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
The Z3 theorem prover from Microsoft Research is
now on Github
, and more importantly now
released under the MIT license
. This is a true open source license allowing commercial use, unlike the previous non-commercial use only license. It's been used with LLVM in the
ALIVe project
.
The
schedule
for EuroLLVM has been published. There are still a number of
early registration tickets left
. If you can be in London on 13th and 14th of April then I'd highly recommend registering.
On the mailing lists
LLVM commits
The GlobalMerge pass will no longer run at O1 on AArch64+ARM, and instead will only be enabled at O3.
r233024
.
A float2int pass was added which, as the name suggests, attempts to demote from float to int where possible.
r233062
.
A simple Orc-based lazy JIT has been added to lli.
r233182
.
LLVM gained support for PowerPC hardware transactional memory.
r233204
.
The ARMv8.1a architecture has been added along with some of its new instructions.
r233290
,
r233301
Clang commits
The on-disk hash table for modules should now have a stable representation.
r233156
,
r233249
.
Intrinsics have been added for PowerPC hardware transaction memory support.
r233205
.
An initial version of a clang-fuzzer has been added, making use of the LLVMFuzzer library.
r233455
.
Other project commits
libclc gained more builtin implementations.
r232977
,
r232965
,
r232964
.
lld learnt how to understand the MIPS N64 relocation record format (which is described in the commit message).
r233057
.
lld's ARM support has improved with with the addition of indirect function handling and GOT relocations.
r233383
,
r233277
.
