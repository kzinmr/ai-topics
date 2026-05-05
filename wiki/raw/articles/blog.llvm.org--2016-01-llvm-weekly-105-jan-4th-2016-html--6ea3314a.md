---
title: "LLVM Weekly - #105, Jan 4th 2016"
url: "https://blog.llvm.org/2016/01/llvm-weekly-105-jan-4th-2016.html"
fetched_at: 2026-05-05T07:01:39.525693+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #105, Jan 4th 2016

Source: https://blog.llvm.org/2016/01/llvm-weekly-105-jan-4th-2016.html

LLVM Weekly - #105, Jan 4th 2016
Welcome to the one hundred and fifth issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
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
Happy new year! This issue marks the second anniversary of LLVM Weekly. It's rather short as the past week has been very quiet, with most LLVM developers seemingly taking a break over the holidays. My colleague Wei Song and myself will be presenting about
lowRISC
at the
3rd RISC-V workshop
on Wednesday this week. Do say hi if you're going to be there.
The canonical home for this issue
can be found here at llvmweekly.org
.
News and articles from around the web
Sanjoy Das has written a blog post about
issues with LLVM's undef value
. Interestingly, he provides an example where undef can actually inhibit optimisations.
On the mailing lists
LLVM commits
The
-align-all-loops
and
-align-all-functions
arguments have been introduced to force function or loop alignments for testing purposes.
r256571
.
The x86 backend has added intrinsics for reading and writing to the flags register.
r256685
.
Clang commits
Various Clang classes have been converted to use the TrailingObjects helper.
r256658
,
r256659
, and more.
__readeflags
and
__writeeflags
intrinsics are exposed in Clang.
r256686
.
Other project commits
