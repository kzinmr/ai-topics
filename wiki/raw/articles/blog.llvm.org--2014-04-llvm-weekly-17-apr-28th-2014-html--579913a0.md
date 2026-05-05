---
title: "LLVM Weekly - #17, Apr 28th 2014"
url: "https://blog.llvm.org/2014/04/llvm-weekly-17-apr-28th-2014.html"
fetched_at: 2026-05-05T07:01:42.355601+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #17, Apr 28th 2014

Source: https://blog.llvm.org/2014/04/llvm-weekly-17-apr-28th-2014.html

LLVM Weekly - #17, Apr 28th 2014
Welcome to the 17th issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
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
Last week I wondered why the GCC logo is a
GNU leaping out of an egg
. Thank you to everyone who wrote in to let me know it is a reference to EGCS. GCC was of course famously forked as EGCS which was later merged back in. Apparently this was pronounced by some as "eggs". Mystery solved.
The canonical home for this issue
can be found here at llvmweekly.org
.
News and articles from around the web
GCC 4.9.0 was
released last Tuesday
. See
here
for more detailed notes on changes in this release.
Honza Hubička wrote a blog post on the
history of linktime optimisation in GCC
, which was followed by a post containing a
benchmark comparison of LTO in GCC vs LLVM
.
On Twitter, @lambdamix drew my attention to
Notes on Graph Algorithms Used in Optimizing Compilers
(PDF). I imagine it will be of interest to many LLVM Weekly readers.
On the mailing lists
LLVM commits
The 'musttail' marker which was
proposed several weeks ago
has been added. Unlike the 'tail' marker, musttail guarantees that tail call optimization will occur. Check the documentation added in the commit for a more detailed explanation.
r207143
.
The rewrite of BlockFrequencyInfo finally landed. A description of the advantages of the new algorithm is in the original commit message,
r206548
. After a series of bounces, it landed in
r206766
.
LLVM can now generate PE/COFF object files targeting 'Windows on ARM'.
r207345
.
A CallGraph strongly connected components pass manager has been added making use of the new LazyCallGraph analysis framework. This is part of the new pass manager work Chandler Carruth has been working on and is of course a work in progress.
r206745
.
The scheduler model for the Intel Silvermont microarchitecture has been replaced. The commit message claims substantial improvements on integer tests. I'm assuming RAL in this context refers to RegAllocLocal?
r206957
.
ARM64 has of course seen a large number of changes. Among those, support for feature predicates for NEON/FP/CYPTO instructions. This allows the compiler to generate code without using those instructions.
r206949
. Additionally, there is now a big endian version of the ARM64 target machine.
r206965
.
getFileOffset has been dropped from LLVM's C API. Justification is in the commit message.
r206750
.
The LoopVectorize pass now keeps statistics on the number of analyzed loops and the number of vectorized loops.
r206956
.
The x86 backend gained new intrinsics for Read Time Stamp Counter.
r207127
.
Initial work on mutation support for the lazy call graph has landed. As with most of Chandler's commits, there's much more information in the commit message.
r206968
.
MCTargetOptions has been introduced, which for now only contains a single flag. SanitizeAddress enabled AddressSanitizer instrumentation of inline assembly.
r206971
.
llvm-cov now supports gcov's
--long-file-names
option.
r207035
.
Clang commits
Documentation for sample profiling was added.
r206994
.
Support for parsing the linear clause for the 'omp simd' directive was added.
r206891
.
Clang gained support for the
-fmodules-search-all
option, which searches for symbols in non-imported modules (i.e. those referenced in module maps but not imported).
r206977
.
Other project commits
