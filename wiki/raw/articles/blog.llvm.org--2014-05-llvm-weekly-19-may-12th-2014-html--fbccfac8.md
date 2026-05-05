---
title: "LLVM Weekly - #19, May 12th 2014"
url: "https://blog.llvm.org/2014/05/llvm-weekly-19-may-12th-2014.html"
fetched_at: 2026-05-05T07:01:42.248168+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #19, May 12th 2014

Source: https://blog.llvm.org/2014/05/llvm-weekly-19-may-12th-2014.html

LLVM Weekly - #19, May 12th 2014
Welcome to the ninteenth issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
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
I'm flying out to San Francisco tomorrow and will be there for the Bay Area Maker Faire at the weekend with some other Raspberry Pi Foundation people. If you're around, be sure to say hi.
The canonical home for this issue
can be found here at llvmweekly.org
.
News and articles from around the web
LLVM 3.4.1
has been released
. This is a bug-fix release so offers API and ABI compatibility with LLVM 3.4. Thanks to everyone who contributed to the release by suggesting or backporting patches, and for testing.
John Regehr has
shared some early results and discussion
on using
Souper
(a new superoptimizer for LLVM IR) in combination with Csmith and C-reduce in order to find missed optimisations and then produce minimal test cases. This has already resulted in a
new performance bug being filed
with I'm sure many more to come.
Crange
, a tool to index and cross-reference C/C++ source code built on top of Clang has
been released
. It aims to offer a more complete database than e.g. ctags, though the running time on a large codebase like the Linux kernel is currently very high.
llgo
, the LLVM-based compiler for Go is
now self-hosting
.
Last week I asked for benchmarks of the new
JavascriptCore Fourth Tier LLVM JIT
. Arewefastyet from Mozilla now includes such results. FTLJIT
does particularly well on asm.js examples
.
On the mailing lists
LLVM commits
A new algorithm has been implemented for tail call marking. A build of clang now ends up with 470k calls in the IR marked as tail vs 375k before. The total tail call to loop conversions remains the same though.
r208017
.
llvm::function_ref
has been introduced and described in the LLVM programmers manual. It is a type-erased reference to a callable object.
r208025
,
r208067
.
Initial support for named register intrinsics (as previously discussed
on the mailing list
has landed. Right now, only the stack pointer is supported. Other non-allocatable registers could be supported with not too much difficulty, allocatable registers are much harder.
r208104
.
The
-disable-cfi
option has been removed. LLVM now requires assemblers to support cfi (control-flow integrity) directives in order to generate stack unwinding information.
r207979
.
The superword-level parallelism (SLP) pass is now enabled by default for link time optimisation.
r208013
.
The llvm-cov documentation has been expanded
r208098
.
The second and third patch of a series to improve MergeFunctions performance to
O(n*log(n))
has been merged.
r208173
,
r208189
.
The standard 'x86-64' CPU used as the default architecture now uses the Sandy Bridge scheduling model in the hope this provides a reasonable default over a wide range of modern x86-64 CPUs.
r208230
.
Custom lowering for the
llvm.{u|s}add.with.otherflow.i32
intrinsics as been added for ARM.
r208435
.
Clang commits
MSVC ABI compatibility has again been improved. Clang now understands that the 'sret' (a structure return pointer) is passed after 'this' for MSVC.
r208458
.
Initial codegen from OpenMP's
#pragma omp parallel
has landed.
r208077
.
Field references to struct names and C++11 aliases are now supported from inline asm.
r208053
.
Parsing and semantic analysis has been implemented for the OpenMP
proc_bind
clause.
r208060
.
clang-format gained initial support for JavaScript regex literals (yes, clang-format can reformat your JavaScript!).
r208281
.
Other project commits
libcxxabi gained support for ARM zero-cost exception handling.
r208466
.
In libcxx, std::vector gained Address Sanitizer support.
r208319
.
The test suite from
OpenUH
has been added to the openmp repository.
208472
.
