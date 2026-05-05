---
title: "LLVM Weekly - #41, Oct 13th 2014"
url: "https://blog.llvm.org/2014/10/llvm-weekly-41-oct-13th-2014.html"
fetched_at: 2026-05-05T07:01:41.467063+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #41, Oct 13th 2014

Source: https://blog.llvm.org/2014/10/llvm-weekly-41-oct-13th-2014.html

LLVM Weekly - #41, Oct 13th 2014
Welcome to the forty-first issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
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
I've been in Munich for ORCONF this weekend. Slides from my talk about
lowRISC
are available
here
.
The canonical home for this issue
can be found here at llvmweekly.org
.
News and articles from around the web
ELLCC, the LLVM/Clang-based cross development toolkit
now has Windows binaries available
.
IBM have
posted a bounty
on fixing the AddressSanitizer tests that fail on PowerPC.
GCC needs you! A large number of
potential starting points for new contributors
has been posted to the GCC mailing list.
On the mailing lists
LLVM commits
Switches with only two cases and a default are now optimised to a couple of selects.
r219223
.
llvm-symbolizer will now be used to symbolize LLVM/Clang crash dumps.
r219534
.
The calculation of loop trip counts for loops with multiple exits has been de-pessimized.
r219517
.
MIPS fast-isel learnt integer and floating point compare and conditional branches.
r219518
,
r219530
,
r219556
.
R600 gained a load/store machine optimizer pass.
r219533
.
Clang commits
The integrated assembler has been turned on by default for ppc64 and ppc64le.
r219129
.
clang-format's interpretation of special comments to disable formatting within a delimited range has been documented.
r219204
.
The integrated assembler has been turned on by default for SystemZ.
r219426
.
Other project commits
lld gained support for 'fat' mach-o archives.
r219268
.
The lldbtk example has seen some further development.
r219219
.
lldb-gdbserver can now be used for local-process Linux debugging.
r219457
.
The disassembly format for lldb can now be customized.
r219544
.
