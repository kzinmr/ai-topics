---
title: "LLVM Weekly - #121, Apr 25th 2016"
url: "https://blog.llvm.org/2016/04/llvm-weekly-121-apr-25th-2016.html"
fetched_at: 2026-05-05T07:01:38.986083+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #121, Apr 25th 2016

Source: https://blog.llvm.org/2016/04/llvm-weekly-121-apr-25th-2016.html

LLVM Weekly - #121, Apr 25th 2016
Welcome to the one hundred and twenty-first issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
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
Congratulations to the eight students who have
been selected for LLVM projects on Google Summer of Code this year
. There's about a month before they start coding. The time between now and then is the 'community bonding period', so please do make them feel welcome.
The preliminary release schedule for LLVM/Clang 3.8.1 has
been published
. This would have a deadline of May 25th for requesting changes to be merged and would see the final release on June 15th.
On the mailing lists
LLVM commits
An implementation of optimisation bisection support has landed. This helps to track down bugs by allowing optimisations to be selectively disabled at compile-time to identify the one introducing a miscompile.
r267022
.
The AArch64 and ARM thread pointer intrinsics have been merged to make a target-independent
llvm.thread.pointer
intrinsic.
r266818
.
The llvm.load.relative intrinsic has been added.
r267233
.
There have been more changes to DebugInfo which will require a bitcode upgrade. A script to perform this upgrade is linked in the commit message.
r27296
.
The ORC JIT API improved its support for RPC, including support for calling functions with return values.
r266581
.
The patchable-function function attribution has been introduced, indicating that the function should be easily patchable at runtime.
r266715
.
The IntrReadArgMem intrinsic property has been split in to IntrReadMem and IntrArgMemOnly.
r267021
.
The MachineCombiner gained the ability to combine AArch64 fmul and fadd in to an fmadd.
r267328
.
Scheduling itineraries were added for Sparc, specifically for the LEON processors.
r267121
.
Clang commits
A prototype of an include fixing tool was created. The indexer remains to be written.
r266870
.
A new warning has been added, which will trigger if the compiler tries to make an implicit instantiation of a template but cannot find the template definition.
r266719
.
Initial driver flags for EfficiencySanitizer were added.
r267059
.
Other project commits
The initial EfficiencySanitizer base runtime library was added to compiler-rt. It doesn't do much of anything yet.
r267060
.
LLD learned to support the linkerscript ALIGN command.
r267145
.
LLDB can now parse EABI attributes for an ELF input.
r267291
.
