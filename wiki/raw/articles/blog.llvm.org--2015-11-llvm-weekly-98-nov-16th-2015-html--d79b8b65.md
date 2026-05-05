---
title: "LLVM Weekly - #98, Nov 16th 2015"
url: "https://blog.llvm.org/2015/11/llvm-weekly-98-nov-16th-2015.html"
fetched_at: 2026-05-05T07:01:39.797532+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #98, Nov 16th 2015

Source: https://blog.llvm.org/2015/11/llvm-weekly-98-nov-16th-2015.html

LLVM Weekly - #98, Nov 16th 2015
Welcome to the ninety-eighth issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
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
This week's issue comes to you from Vienna where I'm just about to head home from a short break (so apologies if it's a little later than usual and perhaps a little less detailed). I'll admit that nobody has actually written in to beg that LLVM Weekly share travel tips, but I will say that Vienna is a beautiful city that's provided lots to do over the past few days. If you're visiting, I can strongly recommend
Salm Bräu
for good beer and food.
The canonical home for this issue
can be found here at llvmweekly.org
.
News and articles from around the web
All of the
LLVM Dev Meeting Videos
are now up, and will stay up. This includes
Chris Lattner and Joseph Groff's talk on Swift's IR
. You can also find most of the slides
here
. The folks at Quarkslab have also
posted a trip report
.
The big news this week is that code derived from NVIDIA's PGI Fortran compiler
is to be open-sourced and a production-grade Fortran front-end to LLVM produced
. This project is a collaboration between the US NNSA (National Nuclear Security Administration), NVIDIA, and the Lawrence Livermore, Sandia, and Los Alamos national laboratories. Hal Finkel has
shared a little more on the LLVM mailing list
. With a source code release not due for about another year, where does this leave the existing
Flang
efforts? The hope is that
parts of Flang will be merged with the PGI release
. Douglas Miles from the PGI team has also
shared a mini-FAQ
. Fortran announcement
Bjarne Stroustrup has shared a
detailed trip report
from the last C++ Standards Meeting.
This post over at the Include Security Blog
delves in to some details of support for the SafeStack buffer overflow protection in LLVM
.
At the official LLVM blog, a new post gives a very useful guide on
how to reduce your testcases using bugpoint and custom scripts
. As the post notes, bugpoint is a very powerful tool but can be difficult to use.
On the mailing lists
LLVM commits
LLVM's autoconf-based build system is now officially deprecated, with the CMake build system being preferred.
r252520
.
Do you want to compile CUDA code with Clang and LLVM? There's now some
handy documentation describing how to do so
. See also
Jingyue's talk
from the recent LLVM Dev Meeting.
r252660
.
A simple MachineInstruction SSA pass for PowerPC has been added. The implementation is short and straight-forward, so worth a read if you want to do some MI-level peephole optimisations for your target.
r252651
.
Basic support for AArch64's address tagging has been added. In AArch64, the top 8 bits of an address can be used to store extra metadata with these bits being masked out before going through address translation.
r252573
.
The Hexagon backend now supports assembly parsing.
r252443
.
The CMake build system gained a new LLVMExternalProjectUtils module. As an example, this is used with the LLVM test suite which can be set up to be rebuilt whenever the in-tree clang or lld change. This could also be used with compiler-rt or libcxx.
r252747
.
An 'empty token' is now defined (written as
token empty
) for when using tokens in LLVM IR.
r252811
.
LibFuzzer gained a new experimental search heuristic, drill. As the comment in FuzzerLoop.cpp explains, this will 1) read+shuffle+execute+minimize the corpus, 2) choose a random unit, 3) reset the coverage, 4) start fuzzing as if the chosen unit was the only element of the corpus, 5) reset the coverage again when done, 6) merge the newly created corpus into the original one.
r252838
.
A BITREVERSE SelectionDAG node and a set of
llvm.bitreverse.*
intrinsics have been introduced. The intention is that backends should no longer have to reimplement similar code to match instruction patterns to their own ISA's bitreverse instruction. See also the patch to the ARM backend that replaces ARMISD::RBIT with ISD::BITREVERSE.
r252878
,
r253047
.
Clang commits
Support for
__attribute__(internal_linkage)
was added. This is much like C's static keyword, but applies to C++ class methods.
r252648
.
Clang now supports GCC's
__auto_type
extension, with a few minor enhancements.
r252690
.
Other project commits
