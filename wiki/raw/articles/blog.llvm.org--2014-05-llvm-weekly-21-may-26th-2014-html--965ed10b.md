---
title: "LLVM Weekly - #21, May 26th 2014"
url: "https://blog.llvm.org/2014/05/llvm-weekly-21-may-26th-2014.html"
fetched_at: 2026-05-05T07:01:42.169310+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #21, May 26th 2014

Source: https://blog.llvm.org/2014/05/llvm-weekly-21-may-26th-2014.html

LLVM Weekly - #21, May 26th 2014
Welcome to the 21st issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
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
I'm back in the UK and mostly recovered from the ensuing jetlag. I am however disturbed that all mailing lists on
GMANE
don't seem to have been updated for the past week and have been unable to find any explanation of what is going on online. GMANE is an important and massively useful aggregrator and archiver of free software development lists and I really hope these are only temporary problems. For this issue, I have instead linked directly to the mailman archives at UIUC.
The canonical home for this issue
can be found here at llvmweekly.org
.
News and articles from around the web
Jonathan Mah has written a
Clang plugin for checking key path strings in Objective C code
. The implementation is
available on Github
.
LWN has published an
article about ThreadSanitizer v2
.
This week, the merge of the AArch64 and the Apple-contributed ARM64 backends was completed. The old AArch64 was deleted and the result of merging code from AArch64 in to ARM64 was renamed to AArch64.
A paper '
Static energy consumption analysis of LLVM IR programs
' has been posted to arXiv.org.
On the mailing lists
LLVM commits
A new attribute, 'nonnull' has been added. When applied to a parameter or return pointer this indicates it is not null, which may allow additional optimisations (at least, avoiding comparisons between that value and null).
r209185
,
r209193
.
The llvm.arm.undefined intrinsic has been added. This is used to generate the 0xde opcode on ARM. It takes an integer parameter, which might be used by the OS to implement custom behaviour on the trap.
r209390
.
The MIPS disassembler has seen some work. Some support has been added for MIPS64r6 and various issues fixed.
r209415
.
LLVM learned the
-pass-remarks-missed
and
-pass-remarks-analysis
command line options.
-pass-remarks-missed
shows diagnostics when a pass tried to apply a transformation but couldn't.
-pass-remarks-analysis
shows information about analysis results.
r209442
.
The documentation for the
llvm.mem.parallel_loop_access
metadata has been updated.
r209507
.
Old AArch64 has been removed and ARM64 renamed to AArch64.
r209576
,
r209577
.
Clang commits
clang-format has seen more JS support. It can now reformat ES6 arrow functions and ES6 destructuring assignments.
r209112
,
r209113
.
Experimental checkers for the clang static analyzer are
now documented
.
r209131
.
Support was added to clang for global named registers, using the LLVM intrinsics which were recently added.
r209149
.
Clang learned the
no_split_stack
attribute to turn off split stacks on a per-function bases.
r209167
.
Clang learned the
flatten
attribute. This causes calls within the function to be inlined where possible.
r209217
.
An initial version of codegen for pragma omp simd has been committed. This also adds CGLoopInfo which is a helper for marking memory instructions with
llvm.mem.parallel_loop_access
metadata.
r209411
.
The pragma
clang optimize {on,off}
has been implemented. This allows you to selectively disable optimisations on certain functions.
r209510
.
An implementation of Microsoft ABI-compatible RTTI (run-time type information) has landed.
r209523
.
Other project commits
'Chained origins' as used by MemorySanitizer has been redesigned.
r209284
.
