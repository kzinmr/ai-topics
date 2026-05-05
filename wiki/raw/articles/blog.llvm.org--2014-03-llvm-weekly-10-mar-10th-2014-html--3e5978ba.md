---
title: "LLVM Weekly - #10, Mar 10th 2014"
url: "https://blog.llvm.org/2014/03/llvm-weekly-10-mar-10th-2014.html"
fetched_at: 2026-05-05T07:01:42.563293+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #10, Mar 10th 2014

Source: https://blog.llvm.org/2014/03/llvm-weekly-10-mar-10th-2014.html

LLVM Weekly - #10, Mar 10th 2014
Welcome to the tenth issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
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
This week the book I authored in collaboration with
Ben Everard
,
Learning Python with Raspberry Pi
(
Amazon US
) is officially released.
The canonical home for this issue
can be found here at llvmweekly.org
.
News and articles from around the web
John Regehr has written a blog post detailing
some ideas for implementing a superoptimizer for LLVM
. There's some good stuff in the comments too.
Version 2.1 of the Capstone disassembly framework has
been released
. Library size is about 40% smaller, memory usage is down 40% and there are performance improvements as well.
Facebook have released
Chisel
, a collection of LLDB commands to assist debugging iOS apps.
A
fork of vim-lldb
, the LLDB plugin for Vim included in the lldb repo has appeared. Changes so far have been relatively minor.
On the mailing lists
Probably one of the most interesting discussions on the mailing list this week came from Mark Seaborn's
questions about upstreaming PNaCl's IR simplification passes
. Both PNaCl and the new Emscripten fastcomp backend make use of a series of out-of-tree IR-to-IR passes that simplify the IR by lowering complex to simpler features. The suggestion is to upstream these so that everyone can benefit. Chandler Carruth
raises concerns
that these passes might bitrot without any in-tree users, suggesting that the PNaCl and Emscripten communities could do more to contribute to upstream LLVM and that such a track record would help ease that concern. There are a number of people chiming in to say they would find the functionality useful.
Diego Novillo asks
whether people would be interested in an optimization report facility
. This would give useful information about the decisions taken by various optimisers, which might be useful when investigating why code doesn't perform as expected and in finding missed optimisations. Unsurprisingly, everyone thinks this would be a good feature. Diego promises to write some more detailed, concrete proposals in the coming days now it's clear people like the general idea.
Kev Kitchens
asks about cross-compiling compiler-rt
. Vadim Chugunov helpfully points to
his work on Rust's fork of compiler-rt
to support this. It's also pointed out in the thread that support for unwinding actually lives in libc++abi rather than in a separate libunwind where you might expect to find it.
There's a pretty
long discussion on naming for reverse iterators and other issues
which should make entertaining reading for anyone who enjoys bikeshedding (not that there's anything wrong with it, there's some good discussion of API naming principles there).
Tim Northover has shared an RFC (with initial patch) on
adding a second ordering operand to cmpxchg
which which indicates the failure ordering.
LLVM commits
A new implementation of PBQP (partitioned boolean quadratic programming)-based register allocator landed.
r202735
. The original commit (
r202551
) message details the changes, including massively reduced memory consumption. Average memory reduction is claimed to be 400x. The tagline is "PBQP: No longer feasting upon every last byte of your RAM".
AArch64 gained a machine description for Cortex-A53, which involved giving all non-NEON instructions scheduling annotations.
r203125
. REVERTED
The SPARC backend gained support for the VIS SIMD instruction set extensions.
r202660
A whole bunch of classes moved around, with the intention that LLVM's support library will work when building with C++ modules.
r202814
and many others. InstIterator, GetElementPtrTypeIterator, CallSite, PatternMatch, ValueHandle, ValueMap, CFG, ConstantFolder, NoFolder, PredIteratorCache, ConstantRange, PassNameParser, and LeakDetector moved from Support to IR.
The
PROLOG_LABEL
TargetOpcode was replaced with
CFI_INSTRUCTION
which is intended to have simpler semantics and be less convoluted to use. See the commit message for more details.
r203204
.
Uses of
OwningPtr<T>
were replaced with
std::unique_ptr<T>
.
r203083
.
The
inalloca
grammar was cleaned up.
r203376
.
Clang commits
The PGO (profile-guided optimisation) code got some minor refactoring in preparation for handling non-C/C++ code, and initial suport for Objective-C blocks.
r203073
,
r203157
.
Module dependences are now included in the dependency files created by
-MD/-MMD
etc.
r203208
.
The
-Wunreachable-code
option no longer warns about dead code guarded by a configuration value.
r202912
.
The MSVC mangling scheme is not used for statics or types which aren't visible.
r202951
.
Other project commits
LLDB now supported JIT debugging on Linux using the GDB JIT interface.
r202956
.
Polly started emitting llvm.loop metadata for parallel loops.
r202854
.
In compiler-rt, assembler implementations of
__sync_fetch_and_*
for ARM were committed.
r202812
.
The level of windows support in LLD has been documented.
r203017
.
