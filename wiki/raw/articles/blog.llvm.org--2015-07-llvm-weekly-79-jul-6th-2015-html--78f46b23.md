---
title: "LLVM Weekly - #79, Jul 6th 2015"
url: "https://blog.llvm.org/2015/07/llvm-weekly-79-jul-6th-2015.html"
fetched_at: 2026-05-05T07:01:40.388014+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #79, Jul 6th 2015

Source: https://blog.llvm.org/2015/07/llvm-weekly-79-jul-6th-2015.html

LLVM Weekly - #79, Jul 6th 2015
Welcome to the seventy-ninth issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
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
Last week I was in Berkeley for the second RISC-V conference. If you weren't able to make it, worry not because I liveblogged both
day one
and
day two
.
The canonical home for this issue
can be found here at llvmweekly.org
.
News and articles from around the web
Stephen Cross has
released llvm-abi
, a library for generating LLVM IR that complies with platform ABIs.
This is a
rather cute implementation of Tetris in C++ header files
, compatible with Clang.
On the mailing lists
LLVM commits
The initial skeleton of the WebAssembly backend has been committed. It is not yet functional.
r241022
.
DIModule metadata nodes have been introduced. A DIModule is meant to be used to record modules importaed by the current compile unit.
r241017
.
New exception handling intrinsics have been added for recovering and restoring parent frames.
r241125
.
Clang commits
Other project commits
libcxx gained
shared_mutux
.
r241067
.
LLD has gained some generally applicable optimisations. e.g. devirtualizing SymbolBody and compacting its in-memory representation.
r241001
.
LLD's COFF linker can now link a working 64-bit debug build of Chrome. chrome.dll takes 24 seconds (vs 48 seconds for linking it with MSVC).
r241318
.
LLDB grew an example of scripted steps in Python.
r241216
.
