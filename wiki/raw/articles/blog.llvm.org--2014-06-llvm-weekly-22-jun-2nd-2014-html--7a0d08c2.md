---
title: "LLVM Weekly - #22, Jun 2nd 2014"
url: "https://blog.llvm.org/2014/06/llvm-weekly-22-jun-2nd-2014.html"
fetched_at: 2026-05-05T07:01:42.172238+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #22, Jun 2nd 2014

Source: https://blog.llvm.org/2014/06/llvm-weekly-22-jun-2nd-2014.html

LLVM Weekly - #22, Jun 2nd 2014
Welcome to the twenty-second issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects.LLVM Weekly is brought to you by
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
Last week I expressed worry about GMANE not updating. I'm happy to report that it's back to normal now. Some of my readers might be interested in my
account of the neat Raspberry Pi-based projects I saw at Maker Faire Bay Area
.
The canonical home for this issue
can be found here at llvmweekly.org
.
News and articles from around the web
David Given has
shared
his partially complete backend for the VideoCore IV VPU as used in the BCM2835 in the Raspberry Pi. It would also be interesting to see a QPU LLVM backend now it has been
publicly documented
.
Documentation on how TableGen's DAGISel backend works
has been updated
.
The
LLVM Compiler Infrastructure in HPC Workshop
has been announced. This is a workshop to be held in conjunction with SC14. The deadline for the call for papers is September 1st.
Tartan
is a Clang analysis plugin for GLib and GNOME. To quote its homepage "The plugin works by loading gobject-introspection metadata for all functions it encounters (both functions exported by the code being compiled, if it is a library; and functions called by it). This metadata is then used to add compiler attributes to the code, such as non-NULL attributes, which the compiler can then use for static analysis and emitting extra compiler warnings."
On the mailing lists
LLVM commits
A LoadCombine pass was added, though is disabled by default for now.
r209791
.
AAPCS-VFP has been taught to deal with Cortex-M4 (which only has single precision floating point).
r209650
.
InstructionCombining gained support for combining GEPs across PHI nodes.
r209843
.
Vectorization of intrinsics such as powi, cttz and ctlz is now allowed.
r209873
.
MIPS64 long branch has been optimised to be 3 instructions smaller.
r209678
.
Clang commits
OpenMP implementation continues. Parsing and Sema have been implemented for OMPAlignedClause.
r209816
.
The
-Rpass-missed
and
-Rpass-analysis
flags have been added. pass-missed is used by optimizers to inform the user when they tried to apply an optimisation but couldn't, while pass-analysis is used to report analysis results back to the user. A followup commit documents the family of flags.
r209839
,
r209841
.
The clang optimize pragma has now been documented.
r209738
.
There has been some API refactoring. The release and take methods were removed from ActionResult and Owned removed from Sema.
r209800
,
r209812
.
Other project commits
ThreadSanitizer has seen a refactoring of storage of meta information for heap blocks and sync objects.
r209810
.
