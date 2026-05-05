---
title: "LLVM Weekly - #94, Oct 19th 2015"
url: "https://blog.llvm.org/2015/10/llvm-weekly-94-oct-19th-2015.html"
fetched_at: 2026-05-05T07:01:39.976427+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #94, Oct 19th 2015

Source: https://blog.llvm.org/2015/10/llvm-weekly-94-oct-19th-2015.html

LLVM Weekly - #94, Oct 19th 2015
Welcome to the ninety-fourth issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
Alex Bradbury
. Subscribe to future issues at
http://llvmweekly.org
and pass it on to anyone else you think may be interested. Please send any tips or feedback to
asb@asbradbury.org
, or @llvmweekly or @asbradbury on Twitter.
A good time was had by all at
ORConf
last week at CERN. We had over 100 open source hardware enthusiasts join us in Geneva. You can find my
slides updating on lowRISC here
. Videos should appear on youtube in the next week or so.
The canonical home for this issue
can be found here at llvmweekly.org
.
News and articles from around the web
A
six month retrospective of LLILC
, the project to produce an open source LLVM-based compiler for .NET, has been posted. It describes work still to be done for garbage collection and exception handling, code size and code quality, and JIT throughput.
The
schedule for the 2015 LLVM Developers' Meeting
is now available.
The new ELF linker in LLD is
looking pretty fast
. Right now it can link Clang in about half the time of binutils gold. However, the resulting binary is larger. It will be interesting to see how the performance compares when both are at feature parity, but this is looking promising.
On the mailing lists
LLVM commits
Hexagon gained a new pass to merge adjacent stores.
r250542
.
Hexagon gained skeleton support for the 'HVX' extension instructions.
r250600
.
The loop vectorizer will now shrink integer operations into the smallest type possible.
r250032
.
Documentation has been added for binary sample profile encoding.
r250309
.
RewriteStatpointsForGC is starting to make use of operand bundles.
r250489
.
Clang commits
Clang gained support for the
-fdebug-prefix-map=
option as in GCC.
r250094
.
The PS4 toolchain definition has been added to Clang.
r250262
.
Clang now understands
-flto=thin
.
r250398
.
Other project commits
The libc++ testing guide has been updated.
r250323
.
LLD got even faster at linking clang.
r250315
.
LLDB gained preliminary NetBSD support.
r250146
.
