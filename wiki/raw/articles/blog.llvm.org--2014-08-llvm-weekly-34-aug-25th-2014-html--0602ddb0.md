---
title: "LLVM Weekly - #34, Aug 25th 2014"
url: "https://blog.llvm.org/2014/08/llvm-weekly-34-aug-25th-2014.html"
fetched_at: 2026-05-05T07:01:41.629733+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #34, Aug 25th 2014

Source: https://blog.llvm.org/2014/08/llvm-weekly-34-aug-25th-2014.html

LLVM Weekly - #34, Aug 25th 2014
Welcome to the thirty-fourth issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects.LLVM Weekly is brought to you by
Alex Bradbury
.Subscribe to future issues at
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
The third release candidate for LLVM/Clang 3.5 is
now available
. As ever, test it on your codebases and report any regressions.
Adrian Sampson has written a
blog post about Quala
, a tool for implementing pluggable type systems for C/C++ using Clang. The example type systems are a system allowing nullable and non-nullable pointers as well as an information flow tracking system. In the future, Adrian wants to connect type annotations to LLVM IR.
C++14 is
now done
. A quick look at the
Clang C++14 implementation status
confirms that Clang support is in pretty good shape.
Santiago Fernandez has been an intern on the .NET team at Microsoft this summer. In this MSDN Channel9 posting, Beth Massi
interviews him about his work on using LLVM in the .NET native code generator
.
The next Cambridge (UK) LLVM social
will be held on Weds 27th August, 7.30pm
.
On the mailing lists
There is a
proposal
to move the minimum supported Visual Studio version for compiling LLVM/Clang up to 2013 from 2012. LLVM/Clang 3.6 would be the first stable release with this requirement assuming there are no objections. With the introduction of C++11 features into the LLVM/Clang codebases, MSVC2012 support is troublesome due to a number of unsupported constructs. If this change would effect you negatively, now is the time to pipe up.
Richard Carback
reports
that two of his interns at Draper Laboratories have been working on resurrecting the LLVM C Backend, with
source on Github
. If this is to make it back into the mainstream repository, somebody will have to volunteer to maintain it which
Richard has kindly done
.
Diego Novillo has posted an
update on his plans for supporting profile data from Perf in LLVM
. He is now planning on keeping conversion to Perf's format out-of-tree. The current LLVM representation can be used as an exchange format, but Diego will be submitting a more compact representation for internal use.
Chris Bieneman has posted an RFC on
removing static initializers for command line options
. This would make it easier for LLVM clients like WebKit and Mesa. There is a lot of discussion about this proposal that I'm afraid I don't have time to summarise.
LLVM commits
X86 Haswell gained a detailed scheduling model.
r215094
,
r215905
, and more.
LLVM's code coverage mapping format gained extensive documentation.
r215990
.
FastISel for AArch64 saw yet more changes, this time optimisations for ADDS/SUBS emission and support for variable shifts.
r216033
,
r216242
.
The MIPS assembler gained support for
.set arch=x
.
r215978
.
The PeepholeOptimizer has been improved to take advantage of the recently added isRegSequence, isExtractSubreg, and isInsertSubreg properties.
r216088
,
r216136
,
r216144
.
A thread-model option has been added along with the 'single' option for lowering atomics on baremetal and single-threaded systems.
r216182
.
The gold plugin has been rewritten in order to fix
bug 19901
.
r216215
.
Clang commits
Other project commits
