---
title: "LLVM Weekly - #36, Sep 8th 2014"
url: "https://blog.llvm.org/2014/09/llvm-weekly-36-sep-8th-2014.html"
fetched_at: 2026-05-05T07:01:41.607147+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #36, Sep 8th 2014

Source: https://blog.llvm.org/2014/09/llvm-weekly-36-sep-8th-2014.html

LLVM Weekly - #36, Sep 8th 2014
Welcome to the thirty-sixth issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
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
The biggest news this week is of course undoubtedly the long-awaited
release of LLVM/Clang 3.5
. See the
release notes
for a full breakdown of what's changed.
Rhine
, a Clojure-inspired Lisp with an LLVM JIT backend has been released (or at least, I wasn't aware of it before). There's plenty of discussion about it
over at HN
.
Intel have
released a new version
of their
CilkPlus LLVM-basd compiler
. This releases implements support for version 1.2 of Intel's Cilk Plus Language Extension Specification.
On the mailing lists
LLVM commits
LLVM gained a new alias analysis implementation, the CFL (Context-free language) alias analysis algorithm. When bootstrapping LLVM, this pass gives 7-8% NoAlias responses to queries that TBAA and BasicAA couldn't answer.
r216970
.
The old JIT has finally been removed.
r216982
.
FastISel gained the option to skip target-independent instruction selection. This is now used by AARch64, which uses target-dependent instruction selection only.
r216947
,
r216955
.
MCAnalysis has been removed. The code was judged to be buggy and poorly tested.
r216983
.
AArch64 gained a pass to try to remove redundant comparison operations.
r217220
.
FastISel has seen some spring cleaning.
r217060
.
Clang commits
VariantMatcher::MatcherOps
was modified to reduce the amount of generated code. This reduces object size and compilation time.
r217152
.
Support for the 'w' and 'h' length modifiers in MS format strings was added.
r217195
,
r217196
.
A new warning is born.
-Wunused-local-typedef
will warn about unused local typedefs.
r217298
.
Other project commits
LLDB has gained initial support for 'type validators'. To quote the commit message, "Type Validators have the purpose of looking at a ValueObject, and making sure that there is nothing semantically wrong about the object's contents For instance, if you have a class that represents a speed, the validator might trigger if the speed value is greater than the speed of light".
r217277
.
It is now possible to build libc++ on systems without POSIX threads.
r217271
.
A
target.process.memory-cache-line-size
option has been added to LLDB which changes the size of lldb's internal memory cache chunks read from the remote system.
r217083
.
