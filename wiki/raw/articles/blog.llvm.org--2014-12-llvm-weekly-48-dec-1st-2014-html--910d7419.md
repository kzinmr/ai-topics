---
title: "LLVM Weekly - #48, Dec 1st 2014"
url: "https://blog.llvm.org/2014/12/llvm-weekly-48-dec-1st-2014.html"
fetched_at: 2026-05-05T07:01:41.225375+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #48, Dec 1st 2014

Source: https://blog.llvm.org/2014/12/llvm-weekly-48-dec-1st-2014.html

LLVM Weekly - #48, Dec 1st 2014
Welcome to the forty-eighth issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
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
John Regehr has posted an
update on the Souper superoptimizer
which he and his collaborators have been working on. They have implemented a reducer for Souper optimizations that tries to reduce the optimization to something more minimal. There current results given ~4000 distinct optimisations of which ~1500 LLVM doesn't know how to do. Of course many of these may in fact be covered by a single rule or pass. One of the next steps for Souper is to extend Souper to support the synthesis of instruction sequences. See also the
discussion on the llvm mailing list
.
The LLVM Blog features a summary of
recent advances in loop vectorization for LLVM
. This includes diagnostics remarks to get feedback on why loops which aren't vectorized are skipped, the loop pragma directive in Clang, and performance warnings when the directive can't be followed.
The LLVM Haskell Compiler (LHC) has been
newly reborn
along with
its blog
. The next steps in development are to provide better support for Haskell2010, give reusable libraries for name resolution and type checking, and to produce human-readable compiler output.
The next LLVM Social in Paris
will take place on December 9th
.
Intel have published a blog post
detailing new X86-specific optimisations in GCC 5.0
. You may also be interested in the
discussion of this post on Hacker News
.
On the mailing lists
LLVM commits
Support for
-debug-ir
(emitting the LLVM IR in debug data) was removed. There's no real justification or explanation in the commit message, but it's likely it was unfinished/unused/non-functional.
r222945
.
InstCombine will now canonicalize toward the value type being stored rather than the pointer type. The rationale (explained in more detail in the commit message) is that memory does not have a type, but operations and the values they produce do.
r222748
.
The documentation for
!invariant.load
metadata has been clarified.
r222700
.
In tablegen, neverHasSideEffects=1 is now hasSideEffects=0.
r222801
.
Clang commits
Four new ASTMatchers have been added: typedefDecl, isInMainFile, isInSystemFile, and isInFileMatchinName.
r222646
.
The documentation on MSVC compatibility has been updated to represent the current state of affairs. Clang has also gained support for rethrowing MS C++ exceptions.
r222731
,
r222733
.
Other project commits
Initial tests have been added for lldb-mi (the LLDB machine interface).
r222750
.
libcxxabi can now be built and tested without threads using CMake.
r222702
.
The compact-unwind-dumper tool now has complete support for x86-64 and i386 binaries.
r222951
.
