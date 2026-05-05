---
title: "LLVM Weekly - #109, Feb 1st 2016"
url: "https://blog.llvm.org/2016/02/llvm-weekly-109-feb-1st-2016.html"
fetched_at: 2026-05-05T07:01:39.739461+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #109, Feb 1st 2016

Source: https://blog.llvm.org/2016/02/llvm-weekly-109-feb-1st-2016.html

LLVM Weekly - #109, Feb 1st 2016
Welcome to the one hundred and ninth issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
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
The GNU Tools Cauldron 2016 has been
announced
for the 9th-11th of September 2016, in Hebden Bridge, UK.
The Sulong project has been
announced
. It is an LLVM IR interpreter using the Truffle framework and Graal on the JVM to support JIT compilation.
Ehsan Akhgari has posted an
updated on building Firefox with clang-cl
. It is now possible to build a complete Firefox with Clang without using the MSVC fallback once.
I've mentioned it down below in the list of notable commits, but it's worth calling out here too: the old autoconf build-system has now been
removed
from LLVM. 3.8 will be the last release to include it. Time to switch to CMake if you haven't already.
John Regehr gave a talk about undefined behaviour in LLVM at the Paris LLVM meetup, and you can find the slides
here
.
On the mailing lists
LLVM commits
The autoconf build system for LLVM has been removed.
r258861
.
The WebAssembly backend gained support for unaligned loads and stores.
r258779
.
LLVM's MCAsmSreamer will now always use .p2align rather than .align, because .align's behaviour can differ between targets.
r258750
.
Intrinsic IDs are now looked up by binary search rather than the previous more complex mechanism. This improves the compile time of Function.cpp.
r258774
.
TargetSelectionDAGInfo has been renamed to SelectionDAGTargetInfo and now lives in CodeGen rather than Target.
r258939
.
A LoopSimplifyCFG pass was added to canonicalise loops before running through passes such as LoopRotate and LoopUnroll.
r259256
.
Clang commits
The clang-cl driver will now warn for unknown arguments rather than erroring, to match the behaviour of MSVC.
r258720
.
The old autoconf build system was removed from Clang.
r258862
.
The 'sancov' (SanitizerCoverage) tool gained some documentation.
r259000
.
Other project commits
libcxx gained an implementation of
ostream_joiner
.
r259014
,
r259015
.
lld gained a new error function which won't cause process exit. The hope is this can be used to provide a gradual path towards lld-as-a-library.
r259069
.
The lit runner for the LLVM test suite can now be passed
--param=profile=perf
which will cause each test to be run under
perf record
.
r259051
.
