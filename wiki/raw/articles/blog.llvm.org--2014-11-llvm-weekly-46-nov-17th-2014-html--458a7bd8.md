---
title: "LLVM Weekly - #46, Nov 17th 2014"
url: "https://blog.llvm.org/2014/11/llvm-weekly-46-nov-17th-2014.html"
fetched_at: 2026-05-05T07:01:41.361832+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #46, Nov 17th 2014

Source: https://blog.llvm.org/2014/11/llvm-weekly-46-nov-17th-2014.html

LLVM Weekly - #46, Nov 17th 2014
Welcome to the forty-sixth issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
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
Chrome on Linux
now uses Clang for production builds
. Clang has of course been used on OS X Chrome for quite some time. The switch saw reduction in binary size of ~8%, but this was vs GCC 4.6 rather than something more up-to-date.
The LLVM in HPC workshop at SC14 is taking place on Monday and the full agenda with abstracts
is available online
On the mailing lists
LLVM commits
Work on call lowering for MIPS FastISel has started.
r221948
.
Work has started on an assembler for the R600 backend.
r221994
.
A pass implementing forward control-flow integrity as been added.
r221708
.
A whole slew of patches that made MDNode a Value have been reverted due to a change in plan. The aim is now to separate metadata from the Value hierarchy.
r221711
.
There are two ways to inform the optimizer the result of a load is never null. Either with metadata or via assume. The latter is now canonicalized into the former.
r221737
.
vec_vsx_ld
and
vec_vsx_st
intrinsics have been added for PowerPC.
r221767
.
PowerPC gained support for small-model PIC.
r221791
.
The llvm.arm.space intrinsic was added to make it easier to write tests for ARM ConstantIslands.
r221903
.
Clang commits
Other project commits
