---
title: "LLVM Weekly - #90, Sep 21st 2015"
url: "https://blog.llvm.org/2015/09/llvm-weekly-90-sep-21st-2015.html"
fetched_at: 2026-05-05T07:01:40.000624+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #90, Sep 21st 2015

Source: https://blog.llvm.org/2015/09/llvm-weekly-90-sep-21st-2015.html

LLVM Weekly - #90, Sep 21st 2015
Welcome to the ninetieth issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
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
The ISO C++ committee have started putting together a set of
C++ Core Guidelines
. The document describes itself as a set of guidelines for using C++ well, with the intention that adherence to the rules could be checked by an analysis tool. Bjarne Stroustrup and Herb Sutter are acting as editors for this project.
A reddit user has posted a
detailed description of how they use libclang to generate reflection data for C++
.
Andrew Chambers has written a blog post about his use of
fuzzing to look for ABI bugs
.
This
short and sweet blog post
introduces the
clazy static checker
, a simple checker for some common suboptimal uses of Qt types. There are plenty of ideas in the comments for further analyses that might be useful.
On the mailing lists
LLVM commits
Assert builds will now produce human-readable numbers to identify dumped SelectionDAG nodes. "0x7fcbd9700160: ch = EntryToken" becomes "t0: ch = EntryToken".
r248010
.
Basic support for reading GCC AutoFDO profiles has landed.
r247874
.
The llvm-mc-fuzzer tool has been documented.
r247979
.
The llvm.invariant.group.barrier intrinsic was born.
r247711
.
The LLVM default target triple can now be set to the empty string at configure time.
r247775
.
Clang commits
AST matcher functions have been renamed to match the AST node names directly. This is a breaking change.
r247885
,
r247887
.
The static analyzer gained a new Objective-C checker. DynamicTypeChecker will check for cases where the dynamic and static type of an object are unrelated.
r248002
.
Other project commits
The LLD COFF linker has gained some extra parallelisation. Self-link time has now improved from 1022ms to 654ms.
r248038
,
r248078
.
Support code was added to LLDB for recognising and printing Go types.
r247629
.
MemorySanitizer has been enabled for AArch64.
r247809
.
