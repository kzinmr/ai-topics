---
title: "LLVM Weekly - #83, Aug 3rd 2015"
url: "https://blog.llvm.org/2015/08/llvm-weekly-83-aug-3rd-2015.html"
fetched_at: 2026-05-05T07:01:40.237160+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #83, Aug 3rd 2015

Source: https://blog.llvm.org/2015/08/llvm-weekly-83-aug-3rd-2015.html

LLVM Weekly - #83, Aug 3rd 2015
Welcome to the eighty-third issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
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
The CodeChecker static analysis infrastructure built on Clang Static Analyzer
has been released
. The
slides
from the talk at EuroLLVM earlier this year give a good overview.
LLVM/Clang 3.7 RC2
has been tagged
. Time to get testing.
The implementation of the
Picon
Control Flow Integrity protection mechanism has been released. See also the associated paper
Picon: Control Flow Integrity on LLVM IR
.
On the mailing lists
LLVM commits
A new exception handling representation has been introduced for MSVC compatibility. The commit includes the appropriate updates to the LLVM language reference.
r243766
.
A test to check bitcode compatibility has been added. This will help ensure the bitcode format produced by an X.Y release is readable by the following X.Z releases.
r243779
.
The lli documentation has been updated and now better explains its purpose.
r243401
.
LLVM gained a target-independent thread local storage (TLS) implementation.
r243438
.
A
reverse(ContainerTy)
range adapter was added.
r243581
.
Clang commits
The method for emitting metadata for loop hint pragmas has been modified, using CGLoopInfo.
r243315
.
Clang learned to pass
-Wa,-mfpu
,
-Wa,-mhwdiv
, and
-Wa,-mcpu
to the integrated assembler.
r243353
.
Initial support for Open MP 4.1's extended ordered clause was added.
r243635
.
Other project commits
