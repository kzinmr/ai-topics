---
title: "LLVM Weekly - #33, Aug 18th 2014"
url: "https://blog.llvm.org/2014/08/llvm-weekly-33-aug-18th-2014.html"
fetched_at: 2026-05-05T07:01:41.672381+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #33, Aug 18th 2014

Source: https://blog.llvm.org/2014/08/llvm-weekly-33-aug-18th-2014.html

LLVM Weekly - #33, Aug 18th 2014
Welcome to the thirty-third issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects.LLVM Weekly is brought to you by
Alex Bradbury
.Subscribe to future issues at
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
Binaries for LLVM/Clang 3.5RC2 are now
available for testing
. Try it on your codebases, and be sure to report any regressions.
LDC 0.14.0
has been released
. LDC is an LLVM-based compiler for the D programming language. There's a mixture of new features and bug fixes, see the release notes for full details of what's changed.
Viva64, who sell the PVS-Studio static analyzer has written up their experiences of
using the Clang static analyzer on the PVS-Studio codebase
. It managed to find 12 issues which the blog author considers genuine bugs.
On the mailing lists
LLVM commits
FastISel for AArch64 will now make use of the zero register when possible and supports more addressing modes.
r215591
,
r215597
.
MIPS gained support for the .end, .end, .frame, .mask, and .fmask assembler directives.
r215359
.
ARM gained the MRS/MSR system instructions.
r215700
.
Clang commits
Documentation has been added describing how the Language options in .clang-format files works.
r215443
.
Prefetch intrinsics were added for ARM and AArch64.
r215568
,
r215569
.
The logic for the
-include
command line parameter is now properly implemented.
r215433
.
Other project commits
LLD now has initial support for ELF/AArch64.
r215544
.
UndefinedBehaviourSanitizer gained a returns-nonnull sanitizer. This verifies that functions annotated with
returns_nonnull
do return nonnull pointers.
r215485
.
A number of lldb tests now compile on Windows.
r215562
.
