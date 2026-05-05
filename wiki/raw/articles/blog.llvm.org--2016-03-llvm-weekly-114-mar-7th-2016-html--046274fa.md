---
title: "LLVM Weekly - #114, Mar 7th 2016"
url: "https://blog.llvm.org/2016/03/llvm-weekly-114-mar-7th-2016.html"
fetched_at: 2026-05-05T07:01:39.180811+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #114, Mar 7th 2016

Source: https://blog.llvm.org/2016/03/llvm-weekly-114-mar-7th-2016.html

LLVM Weekly - #114, Mar 7th 2016
Welcome to the one hundred and fourteenth issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
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
LLVM has been
accepted
as a mentoring organisation in Google Summer of Code 2016. See
here
for more about what that means. If you're a student who would like to get paid to work on LLVM over the summer, you should definitely consider applying. Also take a look at the full list of
organisations in GSoC 2016
. If you have an interest in open source hardware, in my (biased) opinion you should definitely look at
lowRISC's listed project ideas
.
LLVM and Clang 3.8 'final'
has been tagged
. A release should be imminent.
There was a big C++ committee meeting last week. You can find summaries
here
and
here
. If you were hoping for modules, concepts, UFCS, ranges, or coroutines in C++17 I'm afraid you're in for disappointment. Many new features will be available in C++ Technical Specifications though.
llvmlite 0.9.0 has been
released
. llvmlite is a light-weight Python binding for LLVM. If you're wondering how to get started with llvmlite, then check out this recent blog post from Ian Bertolacci on
writing fibonacci in LLVM with llvmlite
.
Andi McClure has written a really interesting blog post about
writing software without a compiler
. In this case, generating LLVM IR from LuaJIT.
On the mailing lists
LLVM commits
MemorySSA has gained an initial update API.
r262362
.
TableGen can now check at compile time that a scheduling model is complete.
r262384
.
New comments in PassBuilder give a description of what trade-offs are expected for each optimisation level.
r262196
.
LoopLoadElimination is now enabled by default.
r262250
.
A new patch adding infrastructure for profile-guided optimisation enhancements in the inline has landed.
r262636
.
Experimental ValueTracking code which tried to infer more precise known bits using implied dominating conditions has been removed. Experiments didn't find it to be profitable enough, but it may still be useful to people wanting to experiment out of tree.
r262646
.
Clang commits
Clang's C API gained an option to demote fatal errors to non-fatal errors. This is likely to be useful for clients like IDEs.
r262318
.
clang-cl gained initial support for precompiled headers.
r262420
.
An
-fembed-bitcode
driver option has been introduced.
r262282
.
Semantic analysis for the swiftcall calling convention has landed.
r262587
.
Clang's TargetInfo will now store an actual DataLayout instance rather than a string.
r262737
.
Other project commits
LLDB can now read line tables from Microsoft's PDB debug info files.
r262528
.
The LLVM test-suite gained the ability to hash generated binaries and to skip tests if the hash didn't change since a previous run.
r262307
.
LLVM's OpenMP runtime now supports the new OpenMP 4.5 doacross loop nest and taskloop features.
r262532
,
r262535
.
