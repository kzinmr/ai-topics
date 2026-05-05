---
title: "LLVM Weekly - #14, Apr 7th 2014"
url: "https://blog.llvm.org/2014/04/llvm-weekly-14-apr-7th-2014.html"
fetched_at: 2026-05-05T07:01:42.378868+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #14, Apr 7th 2014

Source: https://blog.llvm.org/2014/04/llvm-weekly-14-apr-7th-2014.html

LLVM Weekly - #14, Apr 7th 2014
Welcome to the fourteenth issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
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
There seems to have been a flood of LLVM-related news this week, hopefully I've managed to collect it all. If you're in London next week, you might be interested in attending
my introductory LLVM talk
on Wednesday. Abstract is
here
.
EuroLLVM is of course taking place on Monday and Tuesday of this week. Sadly I won't be in attendance. If anyone is blogging the event, please do send me links.
The canonical home for this issue
can be found here at llvmweekly.org
.
News and articles from around the web
The LLVM-related news that has made the biggest splash this week is surely the
announcement of Pyston, a JIT for Python targeting LLVM
. More technical details are
available on the Github repo
. For many this immediately conjures up memories of the
Unladen Swallow project
, started by Google engineers with the same aim of JITting Python with LLVM. That project was eventually unsuccessful, but it's unfair to the authors of Pyston to assume it will have the same fate. It's unclear how much developer time Dropbox are contributing to Pyston. They clearly have a lot of work to do, though it's no secret that
Apple are also looking to target LLVM from JavaScript
which means they're not the only developers working in this area. Kevin Modzelewski
shared some more info
on the LLVM mailing list which details some of the LLVM work they've implemented so far (including some initial escape analysis for GCed memory).
An independent, non-profit LLVM Foundation
is to be formed
. As a vendor neutral organisation it will represent the community interest and aims to be set up by the end of the year.The initial board of directors will be Vikram Adve, Chandler Carruth, Doug Gregor, David Kipping, Anton Korobeynikov, Chris Lattner, Tanya Lattner, and Alex Rosenberg.
Rust 0.10
has been released
. See also the discussion on
Hacker News
and
Reddit
. Rust is a systems programming language from Mozilla which uses LLVM as its code generator backend.
The
Dagger
LLVM-based decompilation framework has
released its source
as well as publishing a series of five articles documenting its implementation approach and documenting the next steps or 'TODOs'.
An
LLVM backend for the Accelerate Array Language
has been released. It compiles Accelerate code to LLVM IR and can target multicore CPUs as well as NVIDIA GPUs.
The
PDF slides
for a recent talk about the LLVM-based
MalDiv
diversifying compiler have been published. Such a tool effectively defeats signature-based matching of malware.
On the mailing lists
LLVM commits
MipsAsmParser and MipsOperand was rewritten. The improvements are documented in the commit message.
r205292
.
The ARM backend gained support for segmented stacks.
r205430
.
Windows on ARM support is now possible with the MachineCode layer.
r205459
.
TargetLowering gained a hook to control when
BUILD_VECTOR
might be expanded using shuffles.
r205230
. Targets might choose to use ExpandBVWithShuffles which was added in a later commit.
r205243
.
X86TargetTransformInfo gained getUnrollingPreferences, which is used by the generic loop unroller. This helps to optimise use of the micro-op caches on X86. This produced 7.5%-15% speedups in the TSVC benchmark suite.
r205348
.
ARM gained a nice little optimisation pass that removes duplicated DMB instructions.
r205409
.
Atomic ldrex/strex loops are now expanded in IR rather than at MachineInstr emission time. This cleans up code, but should also make future optimisations easier.
r205525
.
Clang commits
The clang static analyzer gained double-unlock detection in PthreadLockChecker, as well as a check for using locks after they are destroyed.
r205274
,
r205275
.
The OpenMP 'copyin' clause was implemented.
r205164
.
The 'optnone' attribute was added, which suppresses most optimisations on a function.
r205255
.
The heuristics for choosing methods to suggest as corrections were improved, to ignore methods that obviously won't work.
r205653
.
The 'BitwiseConstraintManager' idea was added to the open projects page.
r205666
.
Other project commits
AddressSanitizer can now be used as a shared library on Linux.
r205308
.
compiler-rt gained support for IEEE754 quad precision comparison functions.
r205312
.
lld now supports
.gnu.linkonce
sections.
r205280
.
