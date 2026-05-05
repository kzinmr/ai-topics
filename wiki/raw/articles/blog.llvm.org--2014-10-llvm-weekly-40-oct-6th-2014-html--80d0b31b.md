---
title: "LLVM Weekly - #40, Oct 6th 2014"
url: "https://blog.llvm.org/2014/10/llvm-weekly-40-oct-6th-2014.html"
fetched_at: 2026-05-05T07:01:41.518781+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #40, Oct 6th 2014

Source: https://blog.llvm.org/2014/10/llvm-weekly-40-oct-6th-2014.html

LLVM Weekly - #40, Oct 6th 2014
Welcome to the fortieth issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
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
I'll be in Munich next weekend for the
OpenRISC conference
where I'll be presenting on the
lowRISC
project to produce an open-source SoC. I'll be giving a similar talk in London at the Open Source Hardware User Group
on 23rd October
.
The canonical home for this issue
can be found here at llvmweekly.org
.
News and articles from around the web
Capstone 3.0 RC1
has been released
Capstone is an open source disassembly engine, based initially on code from LLVM. This release features support for Sparc, SystemZ and XCore as well as the previously supported architectures. Among other changes, the Python bindings are now compatible with Python 3.
An interesting paper from last year came up on the mailing list. From EPFL, it proposes
adding -OVERIFY to optimise programs for fast verification
. The performance of symbolic execution tools is improved by reducing the number of paths to explore and the complexity of branch conditions. They managed a maximum 95x reduction in total compilation and analysis time.
The next Cambridge (UK) social
will take place on Wed 8th Oct at 7.30 pm
.
On the mailing lists
LLVM commits
The expansion of atomic loads/stores for PowerPC has been improved.
r218922
. The documentation on atomics has also been updated.
r218937
.
For the past few weeks, Chandler Carruth has been working on a new vector shuffle lowering implementation. There have been too many commits to summarise, but the time has come and the new codepath is now enabled by default. It claims 5-40% improvements in the right conditions (when the loop vectorizer fires in the hot path for SSE2/SSE3).
r219046
.
The Cortex-A57 scheduling model has been refined.
r218627
.
SimplifyCFG now has a configurable threshold for folding branches with common destination. Changing this threshold can be worthwhile for GPU programs where branches are expensive.
r218711
.
Basic support for the newly-announced Cortex-M7 has been added.
r218747
.
As discussed on the mailing list last week, the sqrt intrinsic will now return undef when given a negative input.
r218803
.
llvm-readobj learnt
-coff-imports
which will print out the COFF import table.
r218891
,
r218915
.
Clang commits
Support for the
align_value
attribute has been added, matching the behaviour of the attribute in the Intel compiler. The commit message explains why this attribute is useful in addition to
aligned
.
r218910
.
A rather useful diagnostic has been added.
-Winconsistent-missing-override
will warn if override is missing on an overridden method if that class has at least one override specified on its methods.
r218925
.
Support for MS ABI continues.
thread_local
is now supported for global variables.
r219074
.
Matcher and DynTypedMatcher saw some nice performance tweaking, resulting in a 14% improvement on a clang-tidy benchmark and compilation of Dynamic/Registry.cpp sped up by 17%.
r218616
.
lifetime.start and lifetime.end markers are now emitted for unnamed temporary objects.
r218865
.
The
__sync_fetch_and_nand
intrinsic was re-added. See the commit message for a history of its removal.
r218905
.
Clang gained its own implementation of C11
stdatomic.h
. The system header will be used in preference if present.
r218957
.
Clang now understands
-mthread-model
to specify the thread model to use, e.g. posix, single (for bare-metal and single-threaded targets).
r219027
.
Other project commits
libcxxabi should now work with the ARM Cortex-M0.
r218869
.
lldb gained initial support for scripting stepping. This is the ability to add new stepping modes implemented by python classes. The example in the follow-on commit has a large comment at the head of the file to explain its operation.
r218642
,
r218650
.
