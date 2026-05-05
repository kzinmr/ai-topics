---
title: "LLVM Weekly - #50, Dec 15th 2014"
url: "https://blog.llvm.org/2014/12/llvm-weekly-50-dec-15th-2014.html"
fetched_at: 2026-05-05T07:01:41.207913+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #50, Dec 15th 2014

Source: https://blog.llvm.org/2014/12/llvm-weekly-50-dec-15th-2014.html

LLVM Weekly - #50, Dec 15th 2014
Welcome to the fiftieth issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
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
I'll be at
MICRO-47
this week. If you're there do say hi, especially if you want to chat about LLVM or lowRISC/RISC-V.
The canonical home for this issue
can be found here at llvmweekly.org
.
News and articles from around the web
The videos and slides from the 2014 LLVM dev meeting went online last week. I already linked to them then, but there's enough interesting stuff there I think I can justify
linking again
.
LLVM/Clang 3.5.1-rc1
has been tagged
. Volunteer testers are very welcome.
Clang UPC 3.4.1
has been released
. This is a Unified Parallel C compiler that can target SMP systems or
Portals4
.
On the mailing lists
LLVM commits
The LLVM Kaleidoscope tutorial has been extended with an 8th chapter, describing how to add debug information using DWARF And DIBuilder.
r223671
. A rendered version can be found
here
.
Extensive documentation has been added for the MergeFunctions pass.
r223931
.
A monster commit to split Metadata from the Value class hierarchy has landed.
r223802
.
InstrProf has been born. This involves the
llvm.instrprof_increment
instrinsic and the
-instrprof
pass. This moves logic from Clang's CodeGenPGO into LLVM.
r223672
.
With the addition of support for SELECT nodes, the MIPS backend now supports codegen of MIPS-II targets on the LLVM test-suite. Code generation has also been enabled for MIPS-III.
r224124
,
r224128
.
Work has started on an LLVM-based dsymutil tool, with the aim to replace Darwin's dsymutil (a DWARF linker).
r223793
.
LiveInterval has gained support to track the liveness of subregisters.
r223877
.
Work has started on converting moves to pushes on X86 when appropriate.
r223757
.
Print and verify passes are now added after each MachineFunctionPass by default, rather than on some arbitrarily chosen subset.
r224042
.
LLVM now requires Python 2.7. Previously 2.5 was required.
r224129
.
Clang commits
The
__builtin_call_with_static_chain
GNU extension has been implemented.
r224167
.
Clang's CodeGenPGO has moved to using the new LLVM
-instrprof
pass.
r223683
.
Clang now accepts Intel microarchitecture names as the
-march
argument.
r223776
.
Other project commits
libcxx gained relational operators in std::experimental::optional.
r223775
.
libcxx can now be built as a 32-bit library.
r224096
.
The lldb unwinder has learned to use unwind information from the compact-unwind section for x86-64 and i386 on Darwin.
r223625
.
