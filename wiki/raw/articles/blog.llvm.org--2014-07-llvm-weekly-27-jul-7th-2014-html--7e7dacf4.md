---
title: "LLVM Weekly - #27, Jul 7th 2014"
url: "https://blog.llvm.org/2014/07/llvm-weekly-27-jul-7th-2014.html"
fetched_at: 2026-05-05T07:01:42.052280+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #27, Jul 7th 2014

Source: https://blog.llvm.org/2014/07/llvm-weekly-27-jul-7th-2014.html

LLVM Weekly - #27, Jul 7th 2014
Welcome to the twenty-seventh issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects.LLVM Weekly is brought to you by
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
An LLVM code generator has been
merged
into the MLton whole-program optimizing compiler for Standard ML. This was written by Brian Leibig as part of his
Master's thesis
, which contains more information on its performance and design.
Eli Bendersky has
written a tool
which converts the output of Clang's
-ast-dump
to HTML. See
here
for an example. The code is
available on Github
.
Clang's Microsoft Visual C++
compatibility page
has been updated to reflect the status of the current SVN trunk. As can be seen from the
relevant diff
, record layout has been marked complete along with RTTI. Lambdas are now marked mostly complete.
On the mailing lists
LLVM commits
The X86 backend now expands atomics in IR instead of as MachineInstrs. Doing the expansions at the IR level results in shorter code and potentially there may be benefit from other IR passes being able to run on the expanded atomics.
r212119
.
The ARM backend learned the ISB memory barrier intrinsic.
r212276
.
The X86 backend gained support for
__builtin_ia32_rdpmc
which is used to read performance monitoring counters.
r212049
.
The peephole optimizer gained new code (currently disabled) to rewrite copies to avoid copies across register banks.
r212100
.
Control flow graph building code has been moved from MC to a new MCAnalysis library.
r212209
.
TableGen gained support for MSBuiltin, which allows for adding intrinsics for Microsoft compatibility.
r212350
.
Clang commits
MSVC RTTI (run-time type information) implementation has been completed.
r212125
.
The
__builin_arm_ldaex
and
__builtin_arm_stlex
intrinsics were added.
r212175
.
Nested blocks are now supported in Microsoft inline assembly.
r212389
.
Other project commits
lldb-gdbserver support has been merged for Linux x86-64.
r212069
.
AddressSanitizer gained support for i686-linux-android.
r212273
.
libcxxabi gained a CMake build system.
r212286
.
lld now supports parsing of x86 and ARM/Thumb relocations for MachO.
r212239
,
r212306
.
