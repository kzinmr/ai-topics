---
title: "LLVM Weekly - #97, Nov 9th 2015"
url: "https://blog.llvm.org/2015/11/llvm-weekly-97-nov-9th-2015.html"
fetched_at: 2026-05-05T07:01:39.894773+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #97, Nov 9th 2015

Source: https://blog.llvm.org/2015/11/llvm-weekly-97-nov-9th-2015.html

LLVM Weekly - #97, Nov 9th 2015
Welcome to the ninety-seventh issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
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
A number of slide decks have started appearing from last week's LLVM Dev Meeting. The first set of videos made a brief appearance
here
but apparently they weren't ready for distribution and have been taken down again. In the mean time, you might be interested in the slides for:
Living downstream without drowning
,
Automated performance tracking of LLVM-generated code
,
opaque pointer types
, and
debug info on a diet
.
Pyston 0.4 has
been released
. It now features a baseline JIT in addition to the LLVM JIT.
The LLVM-based ELLCC cross-compilation tool chain has had a
new release, version 0.1.18
. This release has been tested for building the Linux kernel.
There is going to be an LLVM devroom at FOSDEM 2016. Check
here for the call for papers and participation
. The deadline for receiving submissions is December 1st.
On the mailing lists
As loyal LLVM Weekly readers will know, for a long time now there's been a movement to replace autoconf in the LLVM build system with CMake. It's now at the point where Chris Bieneman suggests we should consider
deprecating autoconf
. His proposal suggests it is marked deprecated for the 3.8 release and removed after 3.8 branches from the main development tree. This proposal is getting a lot of positive feedback.
After a discussion about the spotty use of the
DEBUG_TYPE
in passes to prefix debug messages, Daniel Berlin makes the suggestion
that a new
DEBUG_MSG
macro be introduced
which will always include the
DEBUG_TYPE
. Although there are a number of responses indicating how useful they find it when debug messages are prefixed with their source, there doesn't seem to yet be a consensus on whether it's worth replacing all
DEBUG(dbgs() << ..)
with something like this.
George Burgess is
seeking feedback for his proposal on performing nullability analysis in Clang
.
Richard Diamond has written a
proposal on introducing an llvm.blackbox intrinsic
with the purpose of explicitly preventing certain optimisations. So far, there's some confusion about exactly what this intrinsic would do, and whether there's an alternative way to achieve the same aims.
James Molloy
proposes adding a new norecurse attribute
. With no major exceptions, this has actually already been committed. See the commit summary below for more information.
David Blaikie is planning to implement an llvm-dwp tool to support building a DWARF package file out of a number of .dwo split debug files. He is
seeking feedback
on his plan.
Chris Bieneman has been improving support with the CMake build system for bootstrapping a cross-compiler toolchain and has
run in to issues involving compiler-rt and bootstrapping builtins
. There seems to be some support for the third of the proposed options, splitting the builtins and runtime libraries.
LLVM commits
A new optimisation was added to SimplifyCFG to merge conditional stores. The commit message notes it has little impact on the standard LLVM test suite, but it apparently causes many changes in a third party suite.
r252051
.
Implicit conversions between ilist iterators and pointers are now disabled. All in-tree code has been updated to use explicit conversions, but out-of-tree developers may need to either revert this patch for now or update their code.
r252380
.
The LoopLoadElimination pass was introduced, which can discover store-to-load forwarding opportunities.
r251972
,
r252017
.
Work on operand bundles continues with the addition of a
data_operand
abstraction.
r252077
.
LLVM gained portable helper macros for packed struct definitions.
r252099
.
DebugInfo has been modified so that a reference to a subprogram is stored in function-level metadata rather than subprograms containing a metadata reference to the function they describe. A script to update out-of-tree textual IR is
attached here
.
r252219
,
r252268
.
The
norecurse
attribute has been introduced. This indicates the function will never recurse into itself, either directly or indirectly, and can be used to demote global variables to locals.
r252282
.
The
notail
marker for call instructions was added, which prevents tail or musttail markers being added by the optimizer.
r252368
.
Clang commits
The idea of 'module file extensions' has been introduced. These add additional information to a module file that can be queried when it's read, allowing tools built on Clang to stash their own data in module files. See
the original mailing list RFC
for more details.
r251955
.
Clang now supports the
__make_integer_seq
template.
__make_integer_seq<std::integer_sequence, int, 90000>
takes 0.25 seconds while
std::make_integer_sequence<int, 90000>
takes so long the patch author didn't wait for it to finish.
r252036
.
The newly-introduced VforkChecker will look for unsafe code in a vforked process.
r252285
.
Other project commits
