---
title: "LLVM Weekly - #61, Mar 2nd 2015"
url: "https://blog.llvm.org/2015/03/llvm-weekly-61-mar-2nd-2015.html"
fetched_at: 2026-05-05T07:01:40.833642+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #61, Mar 2nd 2015

Source: https://blog.llvm.org/2015/03/llvm-weekly-61-mar-2nd-2015.html

LLVM Weekly - #61, Mar 2nd 2015
Welcome to the sixty-first issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
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
The biggest headline this week is undoubtedly the release of LLVM/Clang 3.6. See the
LLVM 3.6 release notes
and the
Clang 3.6 release notes
for a full run-down of the major changes.
The
LLVMSharp
C# and .NET bindings to LLVM have been released.
Pyston, the LLVM-based Python JIT developed by Dropbox has had its
0.3 release
. It is now minimally self-hosting. You can also see
performance results
online.
Readers may enjoy this
walkthrough of creating a basic compiler with LLVM
.
On the mailing lists
LLVM commits
Work has started on the move towards opaque pointer types. See the commit messages for more details and help on migrating existing textual IR.
r230786
,
r230794
.
The PlaceSafepoints and RewriteGCForStatepoints passes have been documented.
r230420
.
The GC statepoints documentation has been cleaned up and extended with example IR, assembly, and stackmaps.
r230601
.
The loop-invariant code motion pass has been refactored to expose its core functionality as utility functions that other transformations could use.
r230178
.
Implementation of support for alloca on MIPS fast-isel has started.
r230300
.
The PowerPC backend gained support for the QPX vector instruction set.
r230413
.
InductiveRangeCheckElimination can now handle loops with decreasing induction variables.
r230618
.
Among other improvements, llvm-pdbdump gained colorized output.
r230476
.
The Forward Control Flow Integrity Pass has been removed as it is being rethought and is currently unused.
r230780
.
The Performance Tips for Frontend Authors document was born.
r230807
.
Clang commits
The control flow integrity design docs has been updated to document optimisations.
r230458
,
r230588
.
Other project commits
Remote testing support was added to the libc++ and libc++abi test suites.
r230592
,
r230643
.
LLD learned to understand .gnu.linkonce input sections.
r230194
.
