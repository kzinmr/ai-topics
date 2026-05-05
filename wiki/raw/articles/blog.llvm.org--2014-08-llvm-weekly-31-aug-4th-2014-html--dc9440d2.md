---
title: "LLVM Weekly - #31, Aug 4th 2014"
url: "https://blog.llvm.org/2014/08/llvm-weekly-31-aug-4th-2014.html"
fetched_at: 2026-05-05T07:01:41.951731+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #31, Aug 4th 2014

Source: https://blog.llvm.org/2014/08/llvm-weekly-31-aug-4th-2014.html

LLVM Weekly - #31, Aug 4th 2014
Welcome to the thirty-first issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
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
Renato Golin has posted a
summary of feedback from his talk on LLVM and GCC collaboration at the GNU Tools Cauldron
. This both summarises the main areas he's looking for collaboration, and the feedback that people gave at the event or afterwards.
This blog post describes
how to use Obfuscator-LLVM to to obfuscate Android NDK binaries
.
On the mailing lists
LLVM commits
FastISel for AArch64 saw a number of improvements, including support for shift-immediate, arithmetic with overflow intrinsics.
r214345
,
r214348
, and more.
The SLPVectorizer has seen a largeish commit that implements an "improved scheduling algorithm". Sadly the commit message offers no further details.
r214494
.
TargetInstrInfo gained
isAsCheapAsMove
which takes a MachineInstruction and returns true if that instruction is as cheap as a move instruction.
r214158
.
LLVM libraries can now be exported as importable CMake targets, making it easier for those building LLVM-based projects. This is now documented.
r214077
.
Release notes for PowerPC changes during 3.5 development have been committed.
r214403
.
Initial work towards supporting debug locations for fragmented variables (e.g. by-value struct arguments passed in registers) has been committed.
r214576
.
Clang commits
Work on support for the MSVC ABI continues. Clang will now consider required alignment constraints on fields.
r214274
.
AddressSanitizer now passes source-level information from Clang to ASan using metadata rather than by creating global variables.
r214604
.
The PowerPC backend now support selection of the ELFv1/ELFv2 ABI via the
-mabi=
option.
r214074
.
Other project commits
