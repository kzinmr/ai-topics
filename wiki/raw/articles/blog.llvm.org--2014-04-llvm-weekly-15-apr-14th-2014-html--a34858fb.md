---
title: "LLVM Weekly - #15, Apr 14th 2014"
url: "https://blog.llvm.org/2014/04/llvm-weekly-15-apr-14th-2014.html"
fetched_at: 2026-05-05T07:01:42.401050+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #15, Apr 14th 2014

Source: https://blog.llvm.org/2014/04/llvm-weekly-15-apr-14th-2014.html

LLVM Weekly - #15, Apr 14th 2014
Welcome to the 15th issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
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
Videos are not yet ready, but
most slides from last week's EuroLLVM meeting are now up
.
ARM have
announced
the release of version 6 of the ARM compiler, which is now built on LLVM and Clang.
Philip Reames has
written an update on his work on late safepoint placement
, which is useful for implementing efficient precise garbage collection on LLVM. The bad news is their initial plan did not survive contact with the enemy, though they're hard at work on fixing it and a new update can be expected in good time.
As
reported by Phoronix
, a number of patches towards the goal of compiling the Linux kernel with clang have been
merged
by Linus.
The first release candidate of GCC 4.9 has been
released
. New features in the 4.9 branch are
documented here
.
Polly had a meeting via phone call, and
notes of that meeting are available
. The part of most general interest is probably discussion around the potential of merging Polly into the LLVM mainline.
On the mailing lists
LLVM commits
The NVPTX backend gained preliminary intrinsics and codegen support for textures and surfaces.
r205907
.
Support for optimisation report diagnostics was added. This starts to implement the idea
documented and discussed previously
. In the future it will be possible to get a report of the major optimization decisions taken by compiler transformations.
r205774
,
r205775
.
The merge of AArch64 and ARM4 continues. Named immediate operand mapping logic and enums have been copied from AArch64 to ARM64.
r205866
. The ARM64 backend has seen a large series of smaller commits as well.
Constant hoisting is now enabled for the ARM64 backend.
r205791
.
Previously, optimisation logic in CodeGenPrepare that tried to merge address computation in to the memory operation itself (when supported by the platform's addressing modes) would do so by adding integer operations and using ptrtoint and inttoptr. This caused issues when trying to use alias analysis during CodeGen. There is now opt-in support for doing this using GetElementPtr.
r206092
.
The debug info compression support introduced two weeks ago was reverted, and replaced with a new implementation that compresses the whole section rather than a fragment.
r205989
,
r205990
.
The segmented stack switch has been moved to a function attribute and the old
-segmented-stacks
command line flag removed.
r205997
.
Clang commits
A major refactoring of the thread safety analysis has been started.
r205728
,
r205745
, and more.
libclang gained a
clang_CXXMethod_isConst
method.
r205714
.
As part of the ongoing project to support the MSVC++ ABI, support for
#pragma section
and related programs was added.
r205810
.
New command line options were added to support big or little endian for ARM and AArch64.
r205966
,
r205967
.
Other project commits
The openmp project gained the offload directory, which contains code needed to support OpenMP 4.0 target directives.
r205909
.
