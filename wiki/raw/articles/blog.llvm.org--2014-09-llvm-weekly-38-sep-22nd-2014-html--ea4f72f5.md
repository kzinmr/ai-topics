---
title: "LLVM Weekly - #38, Sep 22nd 2014"
url: "https://blog.llvm.org/2014/09/llvm-weekly-38-sep-22nd-2014.html"
fetched_at: 2026-05-05T07:01:41.953770+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #38, Sep 22nd 2014

Source: https://blog.llvm.org/2014/09/llvm-weekly-38-sep-22nd-2014.html

LLVM Weekly - #38, Sep 22nd 2014
Welcome to the thirty-eighth issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
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
I've been at PyConUK this past weekend so I'm afraid it's another slightly shorter than normal issue. I've been talking about
Pyland
, a programming game that aims to teach children programming in Python (and of course, runs on Raspberry Pi).
The canonical home for this issue
can be found here at llvmweekly.org
.
News and articles from around the web
A paper has recently been published about
Harmony
. In the words of the authors "Harmony is an open source tool (built as an LLVM pass) that creates a new kind of application profile called Parallel Block Vectors, or PBVs. PBVs track dynamic program parallelism at basic block granularity to expose opportunities for improving hardware design and software performance." Their most recent
paper on ParaShares
describes how they find the most 'important' basic blocks in multithreaded programs.
Richard Pennington has written up
some more thoughts on cross compilation configuration for Clang
.
Clike
is a low-level programming language with an extensible syntax based on C. It of course targets LLVM.
If you want your Emacs editor to automatically disassemble LLVM bitcode inside Emacs buffers, then
autodisass-llvm-bitcode
is for you.
On the mailing lists
LLVM commits
The LLVM MC layer can now write BigObj-style COFF object files.
r217812
.
X86AtomicExpandPass has been removed in favour of using the generic AtomicExpandHooks (which now has the necessary hooks).
r217928
.
llvm-cov's internal API has been reworked.
r217975
.
Clang commits
Clang can now use 'response files' when calling other tools when the length of the command line exceeds system limits.
r217792
.
The
-Wbind-to-temporary-copy
warning is no longer on by default.
r218008
.
Clang's thread safety analysis gained
-Wthread-safety-reference
which warns when a guarded variable is passed by reference as a function argument.
r218087
.
Other project commits
libcxx gained some support for using newlib as its C library.
r218144
.
