---
title: "LLVM Weekly - #85, Aug 17th 2015"
url: "https://blog.llvm.org/2015/08/llvm-weekly-85-aug-17th-2015.html"
fetched_at: 2026-05-05T07:01:40.188614+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #85, Aug 17th 2015

Source: https://blog.llvm.org/2015/08/llvm-weekly-85-aug-17th-2015.html

LLVM Weekly - #85, Aug 17th 2015
Welcome to the eighty-fifth issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
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
If you're interested in open source hardware, lowRISC, RISC-V, OpenRISC, and more then consider
joining us at ORConf 2015 in October
. I'm also looking for talk submissions.
The canonical home for this issue
can be found here at llvmweekly.org
.
News and articles from around the web
Videos from April's EuroLLVM
are now online
.
The deadline for the 2015 LLVM Developer's Meeting
call for papers
is rapidly approaching. Get your proposal in by August 20th, 11:59PM PDT.
A new paper covering the AST generation techniques used in Polly in great detail has been published in the July issue of TOPLAS. You can read the preprint
here
.
The
Customizable Naming Convention Checker (CNCC)
is a new Clang-based tool that can be used to validate class, field, variable, and namespace naming conventions against a chosen regular expression.
EvilML
is a deliciously terrifying compiler that compiles ML to C++ template language.
On the mailing lists
LLVM commits
MergeFunctions has been sped up substantially by hashing functions and comparing that hash before performing a full comparison. This results in a speedup of 46% for MergeFunctions in libxul and 117% for Chromium.
r245140
.
i64 loads and stores are now supported for 32-bit SPARC. This is a little fiddly to support as the LDD/STD instructions need a consecutive even/odd pair of 32-bit registers.
r244484
.
Machine basic blocks are now serialized using custom syntax rather than YAML. A later commit documented this syntax.
r244982
,
r245138
.
A new TargetTransformInfo hook has been added for specifying per-target defaults for interleaved accesses.
r244449
.
The llvm.loop.unroll.enable metadata was introduced. This will cause a loop to be unrolled fully if the trip count is known at compiler time and partially if it isn't (unlike llvm.loop.unroll.full which won't unroll a loop if the trip count isn't known).
r244466
.
Rudimentary support for the new Windows exception handling instructions has been introduced.
r244558
.
Token types have been added to LLVM IR.
r245029
.
The BPF backend gained documentation and an instruction set description.
r245105
.
Clang commits
Other project commits
