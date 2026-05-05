---
title: "LLVM Weekly - #25, Jun 23rd 2014"
url: "https://blog.llvm.org/2014/06/llvm-weekly-25-jun-23rd-2014.html"
fetched_at: 2026-05-05T07:01:42.104164+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #25, Jun 23rd 2014

Source: https://blog.llvm.org/2014/06/llvm-weekly-25-jun-23rd-2014.html

LLVM Weekly - #25, Jun 23rd 2014
Welcome to the twenty-fifth issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
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
Facebook have released a number of clang plugins they have been using internally. This includes plugins to the clang analyzer primarily for iOS development as well as a plugin to export the Clang AST to JSON. The code is
available on Github
and they have started a
discussion on the mailing list
about moving some of this code upstream.
This week saw the
release
of LLVM and Clang 3.4.2. This is a bug-fix release which maintains ABI and API compatibility with 3.4.1.
Clang's C++ status page
now lists C++1z feature status
.
On the mailing lists
Rafael Espíndola has started a thread to discuss
clarification on the backward compatibility promises of LLVM
. He summarises what seems to be the current policy (old .bc is upgraded upon read, there is no strong guarantee on .ll compatibility). Much of the subsequent discussion is about issues such as compatibility with metadata format changes.
Duncan P.N. Exon Smith has posted a
review of the new pass manager
in its current form. He starts with a high-level overview of what Chandler Carruth's new PassManager infrastructure offers and has a list of queries and concerns. There are no responses yet, but it's worth keeping your eyes on this thread if you're interested in LLVM internals development.
This week has brought two separate proposals for LLVM code coverage support (neither of which have any replies at the time of writing). Christian Holler has
proposed inclusion of LLCov code
. This is a module pass that instruments basic blocks with calls to functions that will track coverage. The current LLCov code is
available on Github
. Alex L has also posted a
detailed proposal on improving code coverage support for Clang and LLVM
. He is looking for feedback on the approach before starting to submit patches.
LLVM commits
The LLVM global lock is dead, and the LLVM Programmer's Manual has been updated to reflect this.
llvm_start_multithreaded
and
llvm_stop_multithreaded
have been removed.
r211277
,
r211287
.
The patchset to improve MergeFunctions performance from O(NxN) to O(N x log(N)) has finally been completely merged.
r211437
,
r211445
and more.
Range metadata can now be attached to call and invoke (previously it could only be attached to load).
r211281
.
ConvertUTF in the Support library was modified to find the maximal subpart of an ill-formed UTF-8 sequence.
r211015
.
LoopUnrollPass will now respect loop unrolling hints in metadata.
r211076
.
The R600 backend has been updated to make use of LDS (Local Data Share) and vectors for private memory.
r211110
.
X86FastISel continues to improve with optimisation for predicates, cmp folding, and support for 64-bit absolute relocations.
r211126
,
r211130
.
The SLPVectorizer (superword-level parallelism) will now recognize and vectorize non-SIMD instruction patterns like sequences of fadd,fsub or add,sub. These will be vectorized as vector shuffles if they are profitable.
r211339
.
LLVM can now generate native unwind info on Win64.
r211399
.
Clang commits
Clang's OpenMP implementation now contains initial support of the 'reduction' clause,
#pragma omp for
, the 'schedule' clause, the 'ordered' clause, and the 'nowait' clause.
r211007
,
r211140
,
r211342
,
r211347
,
r211352
.
MS ABI support continues with the merging of support for x86-64 RTTI.
r211041
.
The
-std=c+++1z
flag was added to enable support for C++17 features.
r211030
.
The clang User's Manual has been expanded with documentation for profile-guided optimisation with instrumentation.
r211085
.
Emission of ARM NEON intrinsics has been totally rewritten to be easier to read and maintain as well as to provide better protection against coding errors.
r211101
.
Other project commits
compiler-rt now offers add, sub, and mul for IEEE quad precision floating point.
r211312
,
r211313
.
