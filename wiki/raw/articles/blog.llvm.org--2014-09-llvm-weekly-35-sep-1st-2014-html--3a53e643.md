---
title: "LLVM Weekly - #35, Sep 1st 2014"
url: "https://blog.llvm.org/2014/09/llvm-weekly-35-sep-1st-2014.html"
fetched_at: 2026-05-05T07:01:41.950750+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #35, Sep 1st 2014

Source: https://blog.llvm.org/2014/09/llvm-weekly-35-sep-1st-2014.html

LLVM Weekly - #35, Sep 1st 2014
Welcome to the thirty-fifth issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects.LLVM Weekly is brought to you by
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
As I mentioned in a previous issue, I am involved in the
lowRISC
projects to produce a fully open-source SoC. Just a quick reminder that
we are hiring
, and you have just over a week to get your application in.
The canonical home for this issue
can be found here at llvmweekly.org
.
News and articles from around the web
LLVM/Clang 3.5 is inching ever closer to release. The fourth and hopefully final release candidate is
available for testing
.
Quarks Lab have published a
preview of SCAF
, a Source Code Analysis Framework built on Clang. It promises a release soon.
The
VMKit project website
has this week been
updated
to mark the project as retired. VMKit was a project to implement virtual machines such as a JVM on top of LLVM. People interested in restarting the project are encouraged to get in touch with Gaël Thomas.
AMD and Microsoft have
released a C++ AMP compiler targeting version 1.2 of the specification
. The C++ AMP (Accelerated Massive Parallelism) compiler is of course based on LLVM and Clang, and can be
found here
.
On the mailing lists
Manuel Klimek has provided a
quick run-down of the state of his work on Clang C++ refactoring tools
. He reports there are a number of standalone, single-use refacotring tools but more work needs to be done on generalising and integrating them. The plan is to push more of these tools to tools-extra (where clang-rename lives), make them integratable as a library, integrate them into libclang and then integrate them into projects like
ycmd
.
Robin Morisset has been working on optimisations for lowering of atomics and has
asked for input on a fence elimination algorithm
he's been thinking about. He has outlined two possible implementation routes he would like feedback on.
A discussion about
improving llvm-objdump
, kicked offed by Steve King, makes an interesting read. I'm looking forward to a future with a more featureful llvm-objdump that prints symbols of branch targets by default.
David Blaikie has started a discussion about
supporting -gmlt in LLVM/Clang
. Vital to having any chance of understanding this thread is to know that gmlt refers to debug info containing 'minimal line tables', a feature that
was added to GCC a while back
.
I linked last week to the mailing list thread on removing static initializers for command line options and regrettably was unable to summarise the extensive discussion. The bad news is discussion has continued at a rapid pace, but thankfully Chandler Carruth has rather helpfully
sumarised the main outcomes of the discussion
. It's also worth reading
this thread
for an idea of what the new infrastructure might look like.
LLVM commits
The AArch64 backend learned about v4f16 and v8f16 operations,
r216555
.
The LLVM CMake build system now includes support for building with UndefinedBehaviourSanitizer.
r216701
.
Clang commits
The
-fdevirtualize
and
-fdevirtualize-speculatively
flags are now recognised (and ignored) for compatibility with GCC.
r216477
.
Some Google Summer of Code work has started to land. In particular, the Clang static analyzer gained initial infrastructure to support for synthesizing function implementations from external model files. See the commit message for full details on the intent of this feature.
r216550
.
Support was added for capturing variable length arrays in C++11 lambda expressions.
r216649
.
Other project commits
