---
title: "LLVM Weekly - #75, Jun 8th 2015"
url: "https://blog.llvm.org/2015/06/llvm-weekly-75-jun-8th-2015.html"
fetched_at: 2026-05-05T07:01:40.430043+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #75, Jun 8th 2015

Source: https://blog.llvm.org/2015/06/llvm-weekly-75-jun-8th-2015.html

LLVM Weekly - #75, Jun 8th 2015
Welcome to the seventy-fifth issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
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
Botond Ballo has posted a
wonderfully thorough summary of the recent Lenexa C++ standards meeting
, even including a table to summarise the status of various major proposals.
I have somehow neglected to mention the
Crystal language
previously. It is a statically typed language with syntax inspired by Ruby which (of course) compiles using LLVM. It was
discussed last week on Hacker News
.
icGrep has
been released
. It makes use of the 'Parabix' text representation and LLVM for high performance regex matching. More details are available
at the icGrep homepage
.
The winners of the 7th Underhanded C Contest
have now been announced online
. Congratulations to the winner, Karen Pease, for creating such a monstrous piece of code.
On the mailing lists
Chandler Carruth has posted a
summary of a recent in-person discussion about LLD's future and design
. It looks like this was a very positive meeting with agreement in important areas. The recently contributed experimental COFF linker is going to be evaluated to see if its linking model would be appropriate for Darwin. If so, the hope is work can focus on adopting that as the standard model. If not, more work will need to be done on refactoring LLD and making sure that code which makes sense to be shared is.
Christos Margiolas has been working as an intern at the Qualcomm Innovation Center on support for heterogeneous compute, including transparent offloading of loops or functions to accelerators. He is
asking for feedback
and looking to see if there is interest in getting this upstream. He has
shared a slide deck
which gives more details.
Woodrow Barlow is interested in
implementing a new PIC backend for LLVM
. Renato Golin gave a very thorough and helpful response about
how you might proceed
.
Frank Winter is looking for a way to
replace a sequence of repetitive code with a loop
. It was pointed out that the LLVM loop reroll pass should be helpful for this, but it does need to run on an existing loop. This would mean it requires modification or the IR should be modified to introduce a trivial loop before running the reroll pass.
Philip Reames has posted an RFC on adding a
liveoncall parameter attribute
. This would be used to leave an argument marked as live even if it isn't actually used (so it might be later inspected at runtime). Chris Lattner queried whether
adding an intrinsic might be a better approach
.
LLVM commits
LLVM gained support for the new AArch64 v8.1a atomic instructions.
r238818
.
The MPX (Intel Memory Protection eXtensions) feature bit and bound registers are now supported on the X86 backend.
r238916
.
MIPS FastISel gained more instruction and intrinsic implementations.
r238756
,
r238757
,
r238759
.
With the introduction of MCSymbolELF, the base MCSymbol size is now reduced to 48 bytes on x86-64.
r238801
.
Work has started on porting AliasAnalysis to the new pass manager.
r239003
.
The BPF backend now supports big and host endian, in addition to the previously supported little endian.
r239071
.
The naming and structure of the recently added unroll heuristics has been modified.
r239164
.
Clang commits
-mcpu
for ARM will now ignore the case of its arguments for ARM.
r239059
.
A mass of predefined vector functions for PowerPC has been added.
r239066
.
The concept and requires keywords (as used in the C++ Concepts TS) are now lexed. Let's hope this starting point is followed up with work towards full concepts support in the coming months.
r239128
.
Other project commits
The lld COFF linker gained an initial implementation of link-time optimisation.
r238777
.
LLDB gained support for software emulation of the MIPS64 branch instructions.
r238820
.
libiomp5 is now libomp.
r238712
.
