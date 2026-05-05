---
title: "LLVM Weekly - #11, Mar 17th 2014"
url: "https://blog.llvm.org/2014/03/llvm-weekly-11-mar-17th-2014.html"
fetched_at: 2026-05-05T07:01:42.547212+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #11, Mar 17th 2014

Source: https://blog.llvm.org/2014/03/llvm-weekly-11-mar-17th-2014.html

LLVM Weekly - #11, Mar 17th 2014
Welcome to the eleventh issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
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
It seems an extra comma slipped in to my bio in
Learning Python with Raspberry Pi
(
US
) meaning rather than being described as a "compiler hacker, ...", I am a "compiler, hacker, Linux geek, and Free Software enthusiast". It's therefore official, I am a compiler. Presumably this makes me uniquely suited to writing LLVM Weekly.
Previously I've only linked to internship opportunities rather than job ads. I'd be interested in how readers feel about linking to job ads looking for someone with LLVM experience? Do let me know via email or Twitter.
The canonical home for this issue
can be found here at llvmweekly.org
.
News and articles from around the web
On the mailing lists
LLVM commits
I don't believe I made mention of this last week, but it's been decided that virtual methods that override their base class should be marked with the
override
keyword (and that the
virtual
keyword would then be considered redundant).
r203433
,
r203442
, and others.
Support for NaCl support on MIPS developed, with the addition of sandboxing for loads, stores, stack pointer changes, and function calls.
r203484
,
r203606
.
As discussed in an
RFC last week
, cmpxchg now has a second ordering operand which describes the required semantics in case no exchange takes place.
r203559
.
An optimisation was added so that switch-to-lookup-table conversion can be done by adding a bitmask check. An example is given in the commit message.
r203694
.
The sample LLVM project has been removed. It has bitrotted over time and doesn't include CMake support at a time that LLVM is moving away from autoconf/automake.
r203729
.
The PowerPC backend learned basic support for the VSX instruction set extensions.
r203768
.
The merging of a patchset to improve MergeFunctions time complexity from
O(N*N)
to
O(N*log(N))
.
r203788
.
MachineRegisterInfo has been undergoing some major refactoring in order to allow the use of C++11 range-based for loops.
r203865
.
The
linker_private
and
linker_private_weak
linkage types were removed.
r203866
.
Clang commits
Clang will now produce a warning when an invalid ordering is passed to one of the atomic builtins.
r203561
,
r203564
..
In the world of profile guided optimisation (PGO), PGO counters are now scaled down to 32 bits when necessary instead of just truncated.
r203592
.
The static analyzer gained support for detecting when passing pointers to const but uninitialized memory.
r203822
.
The
-Wunreachable-code
diagnostic has been broken up into different diagnostic groups to provide access to unreachable code checks for cases where the default heuristics of
-Wunreachable-code
aren't enough.
r203994
.
Other project commits
lld now has a todo list containing a listing of missing GNU ld command line options.
r203491
.
lldb saw some reworking on how the ShouldStopHere mechanism works. This allows a mode where stepping out of a frame into a frame with no debug information will continue stepping until it arrives at a frame that does have deug information.
r203747
.
The Polly build system has been updated so the Makefile builds a single monolithic LLVMPolly.so.
r203952
.
