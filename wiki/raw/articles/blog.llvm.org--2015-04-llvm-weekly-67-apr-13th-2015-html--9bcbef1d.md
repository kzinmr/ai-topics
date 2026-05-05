---
title: "LLVM Weekly - #67, Apr 13th 2015"
url: "https://blog.llvm.org/2015/04/llvm-weekly-67-apr-13th-2015.html"
fetched_at: 2026-05-05T07:01:40.716977+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #67, Apr 13th 2015

Source: https://blog.llvm.org/2015/04/llvm-weekly-67-apr-13th-2015.html

LLVM Weekly - #67, Apr 13th 2015
Welcome to the sixty-seventh issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
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
EuroLLVM
is going on today and tomorrow in London. I hope to see a number of you there. Provided there's a reasonable internet connection, I hope to be live-blogging the event on the
llvmweekly.org version of this issue
.
The canonical home for this issue
can be found here at llvmweekly.org
.
News and articles from around the web
A new post on the LLVM Blog deatils
how to use LLVM's libFuzzer for guided fuzzing of libraries
.
The Red Hat developer blog has an
article about libgccjit
, a new feature in GCC5, which may be of interest.
On the mailing lists
LLVM commits
The R600 backend gained an experimental integrated assembler.
r234381
.
The libFuzzer documentation has been extended to demonstrate how the Heartbleed vulnerability could have been found using it.
r234391
.
The preserve-use-list-order flags are now on by default.
r234510
.
LLVM gained a pass to estimate when branches in a GPU program can diverge.
r234567
.
The ARM backend learnt to recognise the Cortex-R4 processor.
r234486
.
Clang commits
Lifetime markers for named temporaries are now always inserted.
r234581
.
The quality of error messages for assignments to read-only variables has been enhanced.
r234677
.
clang-format's nested block formatting got a little better.
r234304
.
Other project commits
Support for the 'native' file format was removed from lld.
r234641
.
Remote debugging, the remote test suite, and the process to cross-compile lldb has been documented.
r234317
,
r234395
,
r234489
.
LLDB gained initial runtime support for RenderScript.
r234503
.
