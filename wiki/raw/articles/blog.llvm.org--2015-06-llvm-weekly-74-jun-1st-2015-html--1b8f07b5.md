---
title: "LLVM Weekly - #74, Jun 1st 2015"
url: "https://blog.llvm.org/2015/06/llvm-weekly-74-jun-1st-2015.html"
fetched_at: 2026-05-05T07:01:40.517079+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #74, Jun 1st 2015

Source: https://blog.llvm.org/2015/06/llvm-weekly-74-jun-1st-2015.html

LLVM Weekly - #74, Jun 1st 2015
Welcome to the seventy-fourth issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
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
You may be interested in the
second RISC-V workshop
, which will be held in Berkeley June 29-30. Early bird registration ends today, but academics can register for free. My colleague Wei and I will be there representing
lowRISC
.
The canonical home for this issue
can be found here at llvmweekly.org
.
News and articles from around the web
MPI-Checker
, a static analysis tool for MPI code has been released. It is of course implemented using Clang's
Static Analyzer framework
.
The LLVM-HPC2 workshop will be held on November 15th, co-located with SC15. The
call for papers
has been published. Submissions are due by September 1st.
On the mailing lists
LLVM commits
Codegen for memcpy on Thumb2 has been improved to make use of load/store multiple (more details of how this works in the commit message, worth a read for those interested).
r238473
.
Popcount on x86 will now be implemented using a
lookup table in register technique
.
r238636
,
r238652
.
Work continues on reducing peak memory usage through optimisations to debug info.
r238364
.
Initial support for the
convergent
attribute has landed.
r238264
.
The documentation about the current state of LLVM's Phabricator has been updated along with a call for volunteers to help develop necessary improvements and modifications to Phabricator's PHP codebase.
r238295
.
MCJIT gained support for MIPS64r2 and MIPS64r6.
r238424
.
Clang commits
Other project commits
A new PE/COFF section-based linker has been added to lld. This follows on from discussions about the direction of lld and whether it makes sense to build on top of the atom model. The linker is able to self-link on Windows and is significantly faster than the current implementations (1.2 seconds vs 5 seconds, even without multi-threading). It also takes only 250MB of RAM to self-link vs 2GB.
r238458
.
LLDB on Windows can now demangle Linux or Android symbols.
r238460
.
