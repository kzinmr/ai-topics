---
title: "LLVM Weekly - #58, Feb 9th 2015"
url: "https://blog.llvm.org/2015/02/llvm-weekly-58-feb-9th-2015.html"
fetched_at: 2026-05-05T07:01:40.975747+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #58, Feb 9th 2015

Source: https://blog.llvm.org/2015/02/llvm-weekly-58-feb-9th-2015.html

LLVM Weekly - #58, Feb 9th 2015
Welcome to the fifty-eighth issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
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
The Red Hat developer blog has a post about the plan to
change the G++ ABI along with GCC 5
. This is required for full C++11 compatibility. Unlike the last ABI change where the libstdc++ soname was changed, it will stay the same and instead different mangled names will be used for symbols.
Quarks lab have a tutorial on how to
add a simple obfuscation pass to LLVM
.
On the mailing lists
LLVM commits
A straight-line strength reduction pass has been introduced. This is intended to simplify statements that are generated after loop unrolling. It is enabled only for NVPTX for the time being.
r228016
.
A MachineInstruction pass that converts stack-relative moves of function arguments to use the X86 push instruction. This is only enabled when optimising for code size.
r227752
.
The BasicAA will now try to disambiguate GetElementPtr through arrays of structs into different fields.
r228498
.
Work on improving support in LLVM for GC continues, with the addition of a pass for inserting safepoints into arbitrary IR.
r228090
.
(Very) minimal support for the newly announced ARM Cortex-A72 landed. For now, the A72 is modeled as an A57.
r228140
.
A new heuristic has been added for complete loop unrolling, which looks at what loads might be made constant if the loop is completely unrolled.
r228265
.
A pass to exploit PowerPC's pre-increment load/store support has been added.
r228328
.
A platform-independent interface to a PDB reader has landed.
r228428
.
LLVM learnt to recognise masked gather and scatter intrinsics.
r228521
.
Clang commits
Clang learnt the 'novtable' attribute (for MS ABI support).
r227796
,
r227838
.
New functionality has been added for thread safety analysis, before/after annotations can now be used on mutexes.
r227997
.
Other project commits
A whole bunch of work on LLDB with multithreaded applications on Linux has landed.
r227909
,
r227912
,
r227913
, and more.
The default Polly build is now completely free of GPL dependencies. The isl and imath dependencies have been imported into the codebase to make it easier to build with a known-good revision.
r228193
.
