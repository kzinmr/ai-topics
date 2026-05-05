---
title: "LLVM Weekly - #39, Sep 29th 2014"
url: "https://blog.llvm.org/2014/09/llvm-weekly-39-sep-29th-2014.html"
fetched_at: 2026-05-05T07:01:41.575342+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #39, Sep 29th 2014

Source: https://blog.llvm.org/2014/09/llvm-weekly-39-sep-29th-2014.html

LLVM Weekly - #39, Sep 29th 2014
Welcome to the thirty-ninth issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
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
An implementation of Common Lisp with an LLVM backend, Clasp,
has been announced
. There's a lot of work to be done on performance, but development is
very active on Github
.
A backend for the educational 'y86' instruction set architecture has
been started
. The source is
on Github
.
A new binary snopshot of the ELLCC cross compilation toolchain is
now available
. Pre-compiled binaries are available for ARM, MIPS, PPC, and x86. All tarballs contain header files and runtime libraries for all targets to allow you to build for any supported target.
On the mailing lists
LLVM commits
Segmented stacks support for the x32 ABI has been fixed.
r218247
.
Robin Morisset's work on optimisation of atomics continues. AtomicExpandPass now inserts fences itself rather than SelectionDAGBuilder.
r218329
.
LLVM's libSupport gained a type-safe alternative to
llvm::format()
.
r218463
.
llvm-vtabledump learned how to dump RTTI structures for the MS ABI.
r218498
.
Clang commits
The
assume_aligned
function attribute is now supported.
r218500
.
The thread safety analysis documentation has seen a hefty update.
r218420
.
MS compatibility is further improved with support for the
__super
scope specifier.
r218484
.
Other project commits
