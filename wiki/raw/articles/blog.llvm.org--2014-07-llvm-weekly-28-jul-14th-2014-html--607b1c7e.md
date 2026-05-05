---
title: "LLVM Weekly - #28, Jul 14th 2014"
url: "https://blog.llvm.org/2014/07/llvm-weekly-28-jul-14th-2014.html"
fetched_at: 2026-05-05T07:01:41.902344+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #28, Jul 14th 2014

Source: https://blog.llvm.org/2014/07/llvm-weekly-28-jul-14th-2014.html

LLVM Weekly - #28, Jul 14th 2014
Welcome to the twenty-eighth issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
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
I'll be at the
GNU Tools Cauldron 2014
next weekend, being held at the University of Cambridge Computer Laboratory (which handily is also where I work). If you're there, do say hi.
The canonical home for this issue
can be found here at llvmweekly.org
.
News and articles from around the web
An update on Clang/LLVM on Windows has been
posted on the LLVM blog
. Impressive progress has been made, and as I mentioned last week the
MSVC compatibility page
has been updated.
There is (somewhat amazingly) now a
Pascal-86 frontend for LLVM
. The compiler frontend is written entirely in Python. More information is available in the author's
Master's thesis
(via
Phoronix
).
On the mailing lists
LLVM commits
FastISel gained some infrastructure to support a target-independent call lowering hook as well as target-independent lowering for the patchpoint intrinsic.
r212848
,
r212849
.
DominanceFrontier has been templatified, so in theory it can now be used for MachineBasicBlocks (where previously it was only usable with BasicBlocks).
r212885
.
The quality of results for CallSite vs CallSite BasicAA queries has been improved by making use of knowledge about certain intrinsics such as memcpy and memset.
r212572
.
Work on overhauling x86 vector lowering continues. Chandler now reports that with the new codepath enabled, LLVM is now at performance pairty with GCC for the core C loops of the x264 code when compiling for SSE2/SSE3.
r212610
.
ASM instrumentation for AddressSanitizer is now generated entirely in MachineCode, without relying on runtime helper functions.
r212455
.
Generation of the new mips.abiflags section was added to the MIPS backend.
r212519
.
isDereferenceablePointer will now look through some bitcasts.
r212686
.
Clang commits
A new checker was added, to flag code that tests a variable for 0 after using it as a denominator (implying a potential division by zero).
r212731
.
Clang gained initial support for omp parallel for, the omp parallel sections directive, and omp task.
r212453
,
r212516
,
r212804
.
On the ARM target, LLVM's atomicrmw instructions will be used when ldrex/strex are available.
r212598
.
Support was adding for mips-img-linux-gnu toolchains.
r212719
.
Other project commits
ThreadSanitizer's deadlock detector is enabled by default after being battle-tested on the Chromium codebase for some time.
r212533
.
Support for Android's bionic C library has been added to libcxx.
r212724
.
LLDB's Python scripting interface should now work on Windows.
r212785
.
