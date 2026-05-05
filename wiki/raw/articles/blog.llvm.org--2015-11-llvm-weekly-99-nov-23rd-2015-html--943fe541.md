---
title: "LLVM Weekly - #99, Nov 23rd 2015"
url: "https://blog.llvm.org/2015/11/llvm-weekly-99-nov-23rd-2015.html"
fetched_at: 2026-05-05T07:01:39.760562+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #99, Nov 23rd 2015

Source: https://blog.llvm.org/2015/11/llvm-weekly-99-nov-23rd-2015.html

LLVM Weekly - #99, Nov 23rd 2015
Welcome to the ninety-ninth issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
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
LLVM/Clang 3.7.1-rc2
has been tagged
. As always, help testing is appreciated.
Clasp 0.4
has been released
. Clasp is a new Common Lisp implementation that uses LLVM as a compiler backend and aims to offer seamless C++ interoperation.
On the mailing lists
LLVM commits
Initial support for value profiling landed.
r253484
.
It is now possible to use the
-force-attribute
command-line option for specifying a function attribute for a particular function (e.g. norecurse, noinline etc). This should be very useful for testing.
r253550
.
The WebAssembly backend gained initial prototype passes for register coloring (on its virtual registers) and register stackifying.
r253217
,
r253465
.
The built-in assembler now treats fatal errors as non-fatal in order to report all errors in a file rather than just the first one encountered.
r253328
.
As
discussed on the mailing list last week
, lane masks are now always precise.
r253279
.
Support for prelinking has been dropped. See the commit message for a full rationale.
r253280
.
llvm-lto can now be used to emit assembly rather than object code.
r253622
,
r253624
.
Clang commits
Clang should now be usable for CUDA compilation out of the box.
r253389
.
When giving the
-mcpu/-march
options to Clang targeting ARM, you can now specify
+feature
.
r253471
.
Other project commits
Compiler-rt gained support for value profiling.
r253483
.
The 'new ELF linker' is now the default ELF linker in lld.
r253318
.
The LLVM test suite gained support for running SPEC2000int and SPEC2006int+fp with PGO and reference inputs.
r253362
.
