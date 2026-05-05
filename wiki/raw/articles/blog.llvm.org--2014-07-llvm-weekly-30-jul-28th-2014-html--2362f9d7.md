---
title: "LLVM Weekly - #30, Jul 28th 2014"
url: "https://blog.llvm.org/2014/07/llvm-weekly-30-jul-28th-2014.html"
fetched_at: 2026-05-05T07:01:41.802701+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #30, Jul 28th 2014

Source: https://blog.llvm.org/2014/07/llvm-weekly-30-jul-28th-2014.html

LLVM Weekly - #30, Jul 28th 2014
Welcome to the thirtieth issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
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
Nuno Lopes, David Menendez, Santosh Nagarakatte, and John Regehr have
written about ALIVe
. This is a very promising tool that aims to aid the specification and proof of peephole optimisations (such as those currently found in LLVM's InstCombine). It uses an SMT solver in order to prove optimisations correct (and if incorrect, provides a counter-example).
Source and binaries for the first LLVM/Clang 3.5 Release Candidate
are now available
. If you like your LLVM releases to be on-time and regression-free, do your part and test them on your codebases.
Thomas Ströder and colleagues have recently published a paper "Proving Termination and Memory Safety for Programs with Pointer Arithmetic" which creates symbolic execution graphs from LLVM IR in order to perform its analysis. The preprint is
available here
.
The next Cambridge (UK) LLVM Social will be on the
30th July, at 7.30 pm
.
On the mailing lists
LLVM commits
Support for scoped noalias metadata has been added. The motivation for this is to preserve noalias function attribute information when inlining and to model block-scope C99 restrict pointers.
r213864
,
r213948
,
r213949
.
The llvm-vtabledump tool is born. This will dump vtables inside object files. Right now it only supports MS ABI, but will in the future support Itanium ABI vtables as well.
r213903
.
The llvm.assume intrinsic has been added. This can be used to provide the optimizer with a condition it may assume to be true.
r213973
.
The loop vectorizer has been extended to make use of the alias analysis infrastructure.
r213486
.
Various additions have been made to support the PowerPC ELFv2 ABI.
r213489
,
r213490
, and more.
The R600 backend gained an instruction shrinking pass, which will convert 64-bit instructions to 32-bit when possible.
r213561
.
The llvm.loop.vectorize.unroll metadata has been renamed to llvm.loop.interleave.count.
r213588
.
LLVM 3.5 release notes for MIPS have been committed, if you're interested in seeing a summary of work in the last development cycle.
r213749
.
The IR backward compatibility policy is now documented.
r213813
.
Clang commits
Support for
#pragma unroll
was added.
r213574
.
Clang learned a range of AVX-512 intrinsics.
r213641
.
Work on MS ABI support continues.
r214004
.
Other project commits
A dynamic loader for the Hexagon DSP was committed to lldb as well as an ABI description.
r213565
,
r213566
.
A new fast-path implementation of C++ demangling has been added to lldb. It promises significantly better performance.
r213671
.
