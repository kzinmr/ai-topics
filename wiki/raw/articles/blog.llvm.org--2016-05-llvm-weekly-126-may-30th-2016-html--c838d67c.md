---
title: "LLVM Weekly - #126, May 30th 2016"
url: "https://blog.llvm.org/2016/05/llvm-weekly-126-may-30th-2016.html"
fetched_at: 2026-05-05T07:01:38.749443+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #126, May 30th 2016

Source: https://blog.llvm.org/2016/05/llvm-weekly-126-may-30th-2016.html

LLVM Weekly - #126, May 30th 2016
Welcome to the one hundred and twenty-sixth issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
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
I've been moving house this weekend, so do accept my apologies if you find this issue to be a little less thorough than usual.
News and articles from around the web
Pyston, the LLVM-based Python compiler has
released version 0.5
. The main changes are a switch to reference counting and NumPy compatibility.
I don't want to become "C++ weekly", but I think this audience appreciates a fun use of C++ features.
Verdigris
is a header-only library that allows you to use Qt5 without the moc preprocessor.
The call for papers for the
3rd workshop on the LLVM compiler infrastructure in HPC
has been published. The deadline for paper submission is September 1st. The workshop will take place on November 14th in Salt Lake City, and is held in conjunction with SC16.
On the mailing lists
Vivek Pandya, a GSoC student working on interprocedural register allocation has shared
a weekly status report
.
Rafael Espíndola has proposed
creating a bitcode symbol table
.
There's been
some
updates
on the progress of open-sourcing PGI's Fortran frontend.
Elena Lepilkina has proposed some
enhancement to FileCheck
. Some questions were raised about how useful the proposed extensions will be. Sergey Yakoushkin provided more background on
how these features are used
in a commercial codebase. As Elena notes, these features don't need to all be upstreamed at once (or at all), and are mostly independent.
Lang Hames has posted a heads-up about
upcoming breaking API changes for ORC and MCJIT
.
Sean Silva has kicked off a discussion on
the state of IRPGO
. You might ask what is IRPGO? This is profile-guided optimisation performed through instrumentation at the LLVM IR level, as opposed to FEPGO where instrumentation is added by the frontend (e.g. Clang), prior to lowering to IR. Sean would like to make IRPGO the default on all platforms other than Apple at the moment (who may require a longer deprecation period). A number of followup comments discuss possibilities for ensuring all platforms can move forward together, and ensuring a sensible flag exists to choose between frontend or middle-end PGO.
What exactly is a register pressure set? Both
Quentin Colombet
and
Andrew Trick
have answers for us.
LLVM commits
New optimisations covering checked arithmetic were added.
r271152
,
r271153
.
Advanced unrolling analysis is now enabled by default.
r270478
.
The initial version of a new chapter to the 'Kaleidoscope' tutorial has been committed. This describes how to build a JIT using ORC.
r270487
,
r271054
.
LLVM's stack colouring analysis data flow analysis has been rewritten in order to increase the number of stack variables that can be overlapped.
r270559
.
Parts of EfficiencySanitizer are starting to land, notably instrumentation for its working set tool.
r270640
.
SelectionDAG learned how to expand multiplication for larger integer types where there isn't a standard runtime call to handle it.
r270720
.
LLVM will now report more accurate loop locations in optimisation remarks by reading the starting location from llvm.loop metadata.
r270771
.
Symbolic expressions are now supported in assembly directives, matching the behaviour of the GNU assembler.
r271102
.
Symbols used by plugins can now be auto-exported on Windows, which improves support for plugins in Windows. See the commit message for a full description.
r270839
.
Clang commits
Software floating point for Sparc has been exposed in Clang through
-msoft-float
.
r270538
.
Clang now supports the
-finline-functions
argument to enable inlining separately from the standard
-O
flags.
r270609
.
Other project commits
SectionPiece in LLD is now 8-bytes smaller on 64-bit platforms. This improves the time to link Clang with debug info by 2%.
r270717
.
LLD has replaced a use of binary search with a hash table lookup, resulting in a 4% speedup when linking Clang with debug info.
r270999
.
LLDB now supports AArch64 compact unwind tables, as used on iOS, tvos and watchos.
r270658
.
