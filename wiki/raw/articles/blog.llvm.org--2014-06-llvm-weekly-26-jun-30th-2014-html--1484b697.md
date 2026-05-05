---
title: "LLVM Weekly - #26, Jun 30th 2014"
url: "https://blog.llvm.org/2014/06/llvm-weekly-26-jun-30th-2014.html"
fetched_at: 2026-05-05T07:01:42.097981+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #26, Jun 30th 2014

Source: https://blog.llvm.org/2014/06/llvm-weekly-26-jun-30th-2014.html

LLVM Weekly - #26, Jun 30th 2014
Welcome to the twenty-sixth issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
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
Vladmir Makarov has done his
yearly comparison of GCC and LLVM
, posting performance comparisons using SPECInt2000 on ARM and x86-64.
Version 0.13.0 of LDC, the LLVM-based D compiler has
been released
. This brings a whole host of improvements, listed in detail within the release announcement.
Some Mozilla engineers have been looking at using clang-cl (the MSVC-compatible Clang driver) to build Firefox. With the help of the fallback flag (which falls back o compiling with MSVC if Clang fails) they've
managed to get a completed build
. Ehsan tells us that
602 of the 7168 files, about 8% require the MSVC fallback
at the moment.
Trail of Bits have posted a
preview of McSema
, a framework for translating x86 binaries to LLVM bitcode. The accompanying talk took place on the 28th June, so hopefully we'll hear more about this soon. The blog post tells us that McSema will be open source and made available soon.
Bruce Mitchener has written up his
experience of integrating with LLDB for Dylan
.
Codeplay (based in Edinburgh) are advertising for a
full time compiler engineer
.
On the mailing lists
LLVM commits
A significant overhaul of how vector lowering is done in the x86 backend has been started. While it's under development it's off by default, though it's hoped that in times there will be measurable performance improvements on benchmarks conducive to vectorization.
r211888
and more.
X86 FastISel will use EFLAGS directly when lowering select instructions if the condition comes from a compare. It also now supports floating-point selects among other improvements.
r211543
,
r211544
, and more.
ScaledNumber has been split out from BlockFrequencyInfo into the Support library.
r211562
.
The loop vectorizer now features
-Rpass-missed
and
-Rpass-analysis
reports.
r211721
.
The developer documentation has been updated to clarify that although you can use Phabricator to submit code for review, you should also ensure the relevant -commits mailing list is added as a subscriber on the review and be prepared to respond to comments there.
r211731
.
COMDATs have been added to the IR. What's a COMDAT?
StackOverflow has you covered
.
r211920
.
The NVPTX backend saw a whole series of commits.
r211930
,
r211932
,
r211935
, and more.
LLVM gained an abstraction for a random number generator (RNG).
r211705
.
Clang commits
A nice little diagnostic improvement has been added for when the user accidentally puts braces before the identifer, e.g.
int [4] foo;
.
r211641
.
OpenMP learned the 'section' directive (and some more, see the full commit logs).
r211685
,
r211767
.
Other project commits
