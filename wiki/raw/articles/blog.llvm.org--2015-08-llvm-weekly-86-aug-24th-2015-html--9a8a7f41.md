---
title: "LLVM Weekly - #86, Aug 24th 2015"
url: "https://blog.llvm.org/2015/08/llvm-weekly-86-aug-24th-2015.html"
fetched_at: 2026-05-05T07:01:40.179670+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #86, Aug 24th 2015

Source: https://blog.llvm.org/2015/08/llvm-weekly-86-aug-24th-2015.html

LLVM Weekly - #86, Aug 24th 2015
Welcome to the eighty-sixth issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
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
The LLVM Foundation
has been granted 501(c)(3) non-profit status
. This means contributions are tax-deductible for US tax payers.
LLVM 3.7-rc3
has been tagged
. This is the final release candidate and 3.7.0 final is expected very shortly.
The paper
Fast and Precise Symbolic Analysis of Concurrency Bugs in Device Drivers
makes use of Clang and LLVM as part of its verification flow.
Good news everyone! The deadline for submissions for the 2015 LLVM Developers' meeting has been
extended
to August the 25th.
On the mailing lists
LLVM commits
TransformUtils gained the module splitter, which splits a module into linkable partitions and is intended to be used for parallel LTO code generation.
r245662
.
MergeFunctions is now closer to being deterministic.
r245762
.
ScalarEvolution has been ported to the new pass manager.
r245193
.
The 'kaleidoscope' tutorials on creating a language backend using LLVM are now partially updated to use C++11 features and idioms.
r245322
.
The peephole optimiser learned to look through PHIs to find additional register sources.
r245479
.
Clang commits
Other project commits
