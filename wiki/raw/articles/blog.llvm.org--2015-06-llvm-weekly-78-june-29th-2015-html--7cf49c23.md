---
title: "LLVM Weekly - #78, June 29th 2015"
url: "https://blog.llvm.org/2015/06/llvm-weekly-78-june-29th-2015.html"
fetched_at: 2026-05-05T07:01:40.383250+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #78, June 29th 2015

Source: https://blog.llvm.org/2015/06/llvm-weekly-78-june-29th-2015.html

LLVM Weekly - #78, June 29th 2015
Welcome to the seventy-eighth issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
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
I'm in the Bay Area this week for the
second RISC-V workshop
where my colleague and I will of course be talking about
lowRISC
. If you're not able to make it, keep an eye on the lowRISC blog which I intend to keep updating semi-live with notes from the talks and presentations.
The canonical home for this issue
can be found here at llvmweekly.org
.
News and articles from around the web
Hans Wennborg has shared the
release plan for LLVM/Clang 3.7
. This would see the release branch created on 14th July, with a final release targeted for 21st August.
A
detailed analysis
of the results of the "What is C in practice" survey has now been posted. The survey gained around 300 responses, and aims to help guide the definition of a formal model for the de facto standard of C (i.e. C as it is used rather than purely as specified in the ISO standard).
The 3.6.2-rc1 LLVM/Clang release
has been tagged
. As always, testing is encouraged.
On the mailing lists
Unfortunately at the time of writing GMANE seems to be having some problems, so for this week I'll be using links to the pipermail archives of the relevant mailing list posts.
LLVM commits
The InterleavedAccess pass has been introduced to identify interleaved memory accesses so they can be transformed into target-specific intrinsics.
r240751
.
Initial serialisation of machine instructions has been added, representing MachineInstructions in YAML.
r240295
,
r240425
, and more.
The CaptureTracking pass has been optimised to improve performance on very large basic blocks.
r240560
.
A parser for LLVM stackmap sections has been added and made available through llvm-readobj.
r240860
.
Clang commits
Other project commits
The README for the COFF linker in LLD has been updated with new performance numbers. It's now 3.5 seconds to self-host (was previously 5 seconds), and this compared 7 seconds with the MSVC linker and 30 seconds with the old LLD.
r240759
.
The safestack TODO list in compiler-rt has been updated.
r240473
.
LLD gained support for thread-local storage in MachO objects.
r240454
.
Polly has had a meaningful improvement in compile time through enabling the small integer optimisation of the ISL (Integer Set Library). Polybench benchmarks on average take 20% less time to compile.
r240689
.
