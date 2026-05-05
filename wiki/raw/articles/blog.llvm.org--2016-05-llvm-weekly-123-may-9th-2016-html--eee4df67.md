---
title: "LLVM Weekly - #123, May 9th 2016"
url: "https://blog.llvm.org/2016/05/llvm-weekly-123-may-9th-2016.html"
fetched_at: 2026-05-05T07:01:38.981963+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #123, May 9th 2016

Source: https://blog.llvm.org/2016/05/llvm-weekly-123-may-9th-2016.html

LLVM Weekly - #123, May 9th 2016
Welcome to the one hundred and twenty-third issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
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
If you're in London tomorrow you may be interested in the
NMI Open Source Conference
. You can register until midday today. I'll be giving a brief talk on
lowRISC
. While on the subject of conferences, if you are interested in diversity and inclusion in computing education, you may want to check out the
CAS #include diversity conference
in Manchester on the 11th June.
The canonical home for this issue
can be found here at llvmweekly.org
.
News and articles from around the web
Fabien Giesen has written a brief article explaining
why compilers exploit undefined signed overflow
.
The Google Open Source blog has a
short piece
on the XRay function call tracing system that was proposed for upstreaming last week on the LLVM mailing list.
On the mailing lists
LLVM commits
LLVM's CppBackend has been removed. As the commit message says, this backend has bit-rotted to the extent that it's not useful for its original purpose and doesn't generate code that compiles.
r268631
.
The AVR backend has seen a large amount of code merged in to LLVM.
r268722
.
The MIPS backend has seen some large changes to how relocations are handled. These are now represented using MipsMCExpr instead of MCSymbolRefExpr. As someone who has done quite a lot of (out-of-tree) LLVM backend work, I've always found it odd how some architectures have globally visible enum members in include/llvm/MC/MCExpr.h.
r268379
.
LLVM builds should hopefully now be deterministic by default, as
LLVM_ENABLE_TIMESTAMPS
is now opt-in rather than opt-out. In fact, a follow-up patch removed the option altogether.
r268441
,
r268670
.
The AARch64 backend learned to combine adjustments to the stack pointer for callee-save stack memory and local stack memory.
r268746
.
Clang commits
Clang now supports
-malign-double
for x86. This matches the default behaviour on x86-64, where i64 and f64 types are aligned to 8-bytes instead of 4.
r268473
.
Loop unrolling is no longer completely disabled for
-Os
.
r268509
.
Clang's release notes (reflecting the state of current trunk) have been updated to say more about the state of C++1z support.
r268663
.
Other project commits
libcxx will now build a libc++experimental.a static library to hold symbols from the experimental C++ Technical Specifications (e.g. filesystem). This library provides no ABI compatibility.
r268443
,
r268456
.
All usage of pthreads in libcxx has been refactored in to the
__threading_support
header, with the intention of making it easier to retarget libcxx to platform that don't support pthreads.
r268374
.
libcxx gained support for the
polymorphic memory resources
C++ TS.
r268829
.
