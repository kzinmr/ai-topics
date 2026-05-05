---
title: "LLVM Weekly - #57, Feb 2nd 2015"
url: "https://blog.llvm.org/2015/02/llvm-weekly-57-feb-2nd-2015.html"
fetched_at: 2026-05-05T07:01:41.003790+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #57, Feb 2nd 2015

Source: https://blog.llvm.org/2015/02/llvm-weekly-57-feb-2nd-2015.html

LLVM Weekly - #57, Feb 2nd 2015
Welcome to the fifty-seventh issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
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
I've been at FOSDEM this weekend in Brussels (which is why this week's issue is perhaps a little shorter than usual!). Most talks were recorded and I'll be linking to the videos from the LLVM devroom once they're up. For those interested, you can
see the slides from my lowRISC talk here
. If you want to chat about the project, you may want to join #lowRISC on irc.oftc.net.
The canonical home for this issue
can be found here at llvmweekly.org
.
News and articles from around the web
Eli Bendersky has written a useful
introduction to using the llvmlite Python to LLVM binding
, which was borne out of the Numba project.
LLVM/Clang 3.6-rc2
has been tagged
and is ready for testing.
The next LLVM bay-area social is taking place
on Feb 5th at 7pm
.
The EuroLLVM
call for papers
closes on Feb 16th.
On the mailing lists
LLVM commits
A simple in-process fuzzer was added to LLVM.
r227252
.
The programmer's manual gained a section about type hierarchies, polymorphism, and virtual dispatch.
r227292
.
The upstreaming of Sony's patches for their PS4 compiler started with the addition of the PS4 target triple.
r227060
.
DataLayout now lives again in the TargetMachine rather than the TargetSubtagertInfo.
r227113
.
RuntimeDyld learned to support weak symbols.
r227228
.
LLVM gained a new tool, llvm-pdbdump to dump the contents of Microsoft PDB ('Program DataBase') files, including debug tables.
r227241
,
r227257
.
The loop vectorizer now supports an arbitrary constant step for its induction variables, rather than just -1 or +1.
r227557
.
Clang commits
The clang-format-fuzzer tool was added, which builds on the LLVM fuzzer lib.
r227354
.
MS ABI work continues with proper support for setjmp.
r227426
.
Clang started to learn about the PS4 target triple.
r227194
.
Other project commits
The PowerPC ELF target was dropped from lld.
r227320
.
