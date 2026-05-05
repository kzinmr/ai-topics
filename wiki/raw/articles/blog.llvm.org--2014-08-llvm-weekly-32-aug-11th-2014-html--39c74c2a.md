---
title: "LLVM Weekly - #32, Aug 11th 2014"
url: "https://blog.llvm.org/2014/08/llvm-weekly-32-aug-11th-2014.html"
fetched_at: 2026-05-05T07:01:41.710087+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #32, Aug 11th 2014

Source: https://blog.llvm.org/2014/08/llvm-weekly-32-aug-11th-2014.html

LLVM Weekly - #32, Aug 11th 2014
Welcome to the thirty-second issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
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
Some readers may be interested to know that
lowRISC
, a project to produce a fully open-source SoC started by a number of us at the University of Cambridge Computer Lab has been announced.
We are hiring
.
The canonical home for this issue
can be found here at llvmweekly.org
.
News and articles from around the web
Codeplay contributed the LLDB MI (Machine Interface) frontend a while ago, and have now committed some additional features. To coincide with that, they've published a
series of blog posts
covering the MI driver's implementation, how to set it up from within Eclipse, and how to add support for new MI commands.
McSema, a framework for transforming x86 programs to LLVM bitcode has
now been open-sourced
. The talk about McSema from the ReCON conference is also now online.
Registration for the LLVM Developer's Meeting 2014 is
now open
. The event will take place in San Jose on October 28th-29th. You have until September 1st to
submit your talk/BoF/poster/tutorial proposal
.
On the mailing lists
LLVM commits
Initial work on the MachineCombiner pass landed. This estimates critical path length of the original instruction sequence vs a transformed (combined) instruction sequence and chooses the faster code. An example given in the commit message is choosing between add+mul vs madd on AArch64, and a followup commit implements MachineCombiner for this target.
r214666
,
r214669
.
A few useful helper functions were added to the LLVM C API:
LLVM{IsConstantString, GetAsString, GetElementAsConstant}
.
r214976
.
A whole load of AVX512 instructions were added.
r214719
.
FastISel for AArch64 now support basic argument lowering.
r214846
.
A flag has been added to experiment with running the loop vectorizer before the SLP vectorizer. According to the commit message, eventually this should be the default.
r214963
.
The old JIT is almost dead, it has been removed (for those not paying close attention, 3.5 has already been branched so still contains the old JIT). However, the patch was then reverted, so it's in zombie status.
r215111
.
AArch64 gained a load balancing pass for the Cortex-A57, which tries to make maximum use of available resources by balancing use of even and odd FP registers.
r215199
.
Clang commits
Thread safety analysis gained support for negative requirements to be specified.
r214725
.
Coverage mapping generation has been committed. The
-fcoverage-mapping
command line option can be used to generate coverage mapping information, which can then be combined with execution counts from instrumentation-based profiling to perform code coverage analysis.
r214752
.
A command line option to limit the alignment that the compiler can assume for an arbitrary pointer.
r214911
.
Other project commits
LLDB's FileSpec class learned to understand Windows paths.
r215123
.
LLDB learned a whole bunch of new commands and features for its Machine Interface.
r215223
.
OpenMP gained PowerPC64 support.
r215093
.
