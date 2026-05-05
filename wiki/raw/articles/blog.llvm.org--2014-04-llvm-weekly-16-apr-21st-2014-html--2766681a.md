---
title: "LLVM Weekly - #16, Apr 21st 2014"
url: "https://blog.llvm.org/2014/04/llvm-weekly-16-apr-21st-2014.html"
fetched_at: 2026-05-05T07:01:42.398958+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #16, Apr 21st 2014

Source: https://blog.llvm.org/2014/04/llvm-weekly-16-apr-21st-2014.html

LLVM Weekly - #16, Apr 21st 2014
Welcome to the 16th issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
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
Apologies that last week's LLVM Weekly went out twice via email. Mailgun have the useful ability to schedule an email for the future, but when this is done incorrectly have no ability to cancel it via the API. Possibly there is no way for them to cancel it either, I have no way to know as my support ticket on the issue was never answered.
Seeing as it's Easter, does anybody know why GCC has a
GNU breaking out of an egg as a logo
?
The canonical home for this issue
can be found here at llvmweekly.org
.
News and articles from around the web
The new backend to
Emscripten
which is implemented as an LLVM backend has
now been merged to Emscripten's master branch
. This should result in a noticeable speedup in compile times.
Phoronix have published a
small set of benchmarks comparing GCC 4.9RC1 and Clang 3.5 HEAD
.
Diego Novillo has
announced AutoFDO
, a tool which will convert profile data generated with
Linux Perf
to a format compatible with LLVM's sample-based profiler.
The Polly project have
minutes from another phone call
, this time focusing on delinearization.
On the mailing lists
LLVM commits
LLVM's internal BumpPtrAllocator has been switched to using a vector of pointers to slabs rather than a single linked list and the underlying allocator is now a template parameter.
r206147
,
r206149
. The allocator can now also pass the size to the deallocation function, which improves performance with some libraries (e.g. tcmalloc).
r206265
.
Support for building persistent strongly connected components has been added to the LazyCallGraph. There are detailed comments on the reasoning of this approach and some details on implementation in the commit message.
r206581
.
Constant hoisting has been enabled on PowerPC.
r206141
.
PseudoSourceValue is no longer a subclass of Value.
r206255
.
A DebugInfoVerifier has been implemented.
r206300
.
MIPS gained initial support for the IEEE 754-2008 NaN encoding.
r206396
.
OnDiskHashTable has been moved from Clang to LLVM.
r206438
.
ARM's IR-based atomics pass has been moved from Target to CodeGen, which allows it to be used by ARM64.
r206485
,
r206490
.
Module verification is now off by default in release builds for the JIT, but this can be overridden.
r206561
.
The Cortex-A53 machine model description has been ported from AArch64 to ARM64.
r206652
.
Clang commits
There is now a new hash algorithm for calculating the function hash for instruction profiling, rewritten to help ensure the hash changes when control flow does.
r206397
.
The thread safety analysis SSA pass has been rewritten.
r206338
.
Support for big endian ARM64 was added to Targets.cpp.
r206390
. It is also now possible to disable NEON and crypto support for ARM64.
r206394
.
Other project commits
LLD now supports
--defsym=<symbol>=<symbol>
, as supported by GNU LD.
r206417
.
