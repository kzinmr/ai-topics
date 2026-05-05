---
title: "LLVM Weekly - #95, Oct 26th 2015"
url: "https://blog.llvm.org/2015/10/llvm-weekly-95-oct-26th-2015.html"
fetched_at: 2026-05-05T07:01:39.962255+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #95, Oct 26th 2015

Source: https://blog.llvm.org/2015/10/llvm-weekly-95-oct-26th-2015.html

LLVM Weekly - #95, Oct 26th 2015
Welcome to the ninety-fifth issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
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
The C++ Standardization Committee just finished up their most recent meeting, and STL (Stephan T. Lavavej) has
provided a useful summary
. Herb Sutter has also
posted a trip report
.
The HHVM team have posted an
update on the status of LLVM code generation in HHVM
. They managed to get LLVM to equal the performance of their custom backend, but are not going to deploy the LLVM backend to production for now. They're no longer actively working on the LLVM backend, but hope to ensure it doesn't regress.
Hal Finkel is
proposing an LLVM social in Austin on the evening of November 15th
. There should be a high density of LLVM users due to the
LLVM in HPC workshop
.
On the mailing lists
LLVM commits
The
TargetLowerBase::LibCall
LegalizeAction has been introduced. This allows backends to control whether they prefer expansion or conversion to a libcall.
r250826
.
The Hexagon backend continues to accumulate sophisticated target-specific optimisations. HexagonBitSimplify continues a number of transformations to perform simplifications, redundant code elimination etc.
r250868
.
The new AliasAnalysis infrastructure gained an optional 'external' AA wrapper pass, to allow users to merge in external AA results. The unit test included in the patch gives a good example of how to use this.
r250894
.
CodeGenPrepare can now transform select instructions into branches and sink expensive operands.
r250743
.
Loop rotation can now use profile data in making decisions during MachineBlockPlacement.
r250754
.
ValueTracking now has a
isKnownNonEqual
predicate.
r251012
.
Clang commits
Basic (currently parsing and basic semantic analysis) support for the anticipated C++1z coroutine feature was added.
r250980
,
r250985
,
r250993
.
-fvisibility=internal
is now aliased to
-fvisibility=hidden
, as LLVM doesn't currently support internal visibility.
r250954
.
Clang's static analyzer learnt to associate hashes with found issues. This hash aims to be resilient to code changes, so should be useful for suppressing false positives.
r251011
.
Other project commits
lld gained support for lazy relocations on x86-64.
r250808
.
The new LLD ELF linker now supports the
--gc-sections
parameter. This increases the time to link Clang by 8% bus reduces the size of the output binary by 4%.
r251043
.
LLDB gained a REPL.
r250753
,
r250773
.
DWARF parsing in LLDB can now be multi-threaded, which can drastically incrase the speed of loading debug info.
r251106
.
