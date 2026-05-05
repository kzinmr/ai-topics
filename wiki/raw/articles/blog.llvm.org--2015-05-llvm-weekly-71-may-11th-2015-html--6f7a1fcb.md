---
title: "LLVM Weekly - #71, May 11th 2015"
url: "https://blog.llvm.org/2015/05/llvm-weekly-71-may-11th-2015.html"
fetched_at: 2026-05-05T07:01:40.586436+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #71, May 11th 2015

Source: https://blog.llvm.org/2015/05/llvm-weekly-71-may-11th-2015.html

LLVM Weekly - #71, May 11th 2015
Welcome to the seventy-first issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
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
The implementation of OpenMP 3.1 in Clang/LLVM is
now complete
. Well done to everyone involved.
Most slides from the presentations at
EuroLLVM 2015
are now online. Video is
coming soon
.
Version 3.5.1 of Clang UPC, the Unified Parallel C compiler has
been released
. The main change seems to be the move to Clang/LLVM 3.5.
The Pony Language, which features an LLVM backend has recently
been released
. It received quite a lot of
discussion on Hacker News
.
Many readers might be interested in this
update from the last C++ standardization committee meeting
.
IBM have posted some bounties for
TSAN support
and
MSAN support
for PPC64.
On the mailing lists
LLVM commits
A new 'shrink-wrap' pass has been added. It attempts to insert the prologue and epilogue of a function somewhere other than the entry/exit blocks. See the commit message for a motivating example.
r236507
.
Support for the z13 processor and its vector capabilities have been added to the SystemZ backend.
r236520
,
r236521
.
Documentation has been written for the new masked gather and scatter intrinsics.
r236721
.
The statepoint intrinsic has been extended to allow statepoints to be marked as tranditions from GC-aware code to nonGC-aware code.
r236888
.
Clang commits
Clang support for the z13 processor was added.
r236531
.
Thread-safe initialization using the MSVC 2015 ABI has been implemented.
r236697
.
User-friendly
-fsanitize-coverage=
flags are now available.
r236790
.
Other project commits
libiomp's CMake has been integrated into the LLVM CMake build system, so you can now checkout libiomp and have it built alongside llvm, clang and so on.
r236534
.
