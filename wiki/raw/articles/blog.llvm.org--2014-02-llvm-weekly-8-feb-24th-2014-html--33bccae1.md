---
title: "LLVM Weekly - #8, Feb 24th 2014"
url: "https://blog.llvm.org/2014/02/llvm-weekly-8-feb-24th-2014.html"
fetched_at: 2026-05-05T07:01:42.598053+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #8, Feb 24th 2014

Source: https://blog.llvm.org/2014/02/llvm-weekly-8-feb-24th-2014.html

Welcome to the eighth issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
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
As a followup to the proposal that Philip Reames posted last week, where he described plans for contributing precise garbage collection support to LLVM, he has
written a blog post about why the llvm.gcroot intrinsic is insufficient for this purpose
. A followup post is promised describing the approach they've decided to take. The article is is written so as to be accessible to those who may not be familiar with GC implementation. He also raises some interesting issues with gcroot, even when using it for a non-relocating collector.
Some may remember the
Dagger project
for decompilation of programs to LLVM IR from EuroLLVM 2013 (
slides
). The promised source code release didn't happen, but the developers have
posted an update
detailing what they've been up to. There have been a lot of design changes, and some of the work has been submitted upstream as patches to LLVM MC. "At this point we don't really have a schedule; whenever we feel a patch is ready to go, we submit it to the community. The goal being, once we're done, our work becomes a full part of LLVM, where we and all contributors can continue to advance it!"
Tamás Szelei has written up a
useful guide to implementing a code generator with libclang and Python
.
The Emscripten project is
getting ready to use its 'fastcomp' LLVM backend by default
. Previously they had a series of passes written in Javascript to convert from LLVM IR to Javascript, but this is now implemented as a C++ LLVM backend. See
their wiki
for more info.
Agner has
updated his popular optimisation manuals
to include test results for AMD Steamroller processors, as well as adding some more AVX-512 information.
The
DWARF Debugging Information Format Committee
are welcoming comments, suggestions or proposals for changes to DWARF
until March 31st
. Although DWARF Version 5 is 'nearing completion', it seems that no drafts have been published so you'll have to base your comments on DWARF 4. Do drop me a note if you know otherwise.
There have been
several updates
to
http://llvm.org/apt/
. The upcoming Ubuntu 14.04 is now a supported distribution, and additionally both the stable and development versions of LLVM/Clang are built and can be installed side-by-side.
Renato Golin
reminds us
that although work is underway to update all buildbots to support C++11, the switch to use
-std=c++11
has not yet been flipped, so you'll have to hold off on using C++11 features in LLVM/Clang patches for just a little longer.
Saleem Abulrasool
points to an issue running recent Clang on the Linux kernel
related to the integrated assembler. As regular readers will know, the behaviour was recently changed so that for backends which have an integrated assembler, any inline assembly will be validated by it during compilation, even when compiling with
-S
(i.e. outputting assembly). The problem is that the Linux kernel is purposely including invalid assembly in some cases when outputting assembler files. Early responses are in favour of keeping current behaviour, people who are doing weird and wacky things can just use the
-no-integrated-as
switch.
In response to the earlier discussion about unwind behaviour in LLVM/Clang, Logan Chien has
posted a detailed description of the problems he sees
.
Kevin Qin writes
asking about adding register allocation constraints
. Often the mailing list threads which get highlighted in LLVM Weekly are about particularly hairy problems that don't currently have a good solution. I'm happy to see this problem has a simple solution though, as Tim Northover and Quentin Colombet point out the
@earlyclobber
constraint can be used to ensure the output register allocated is different to the input registers.
While working on changes to CodeGenPrepare, Quentin Combet noted his patch would introduce a dependency from libLLVMScalarOpts (where CodeGenPrepare currently lives) to libLLVMCodeGen. He
writes to the list
asking for views on how to solve this problem. The forming consensus seems to be that it should just be moved to CodeGen. Potentially, any IR pass that depends directly on TargetLowering should be moved also. The move to CodeGenPrepare to lib/CodeGen has now
been committed
.
Per Viberg is
soliciting comments
on his design draft for improving the detection of uninitialized arguments.
The llvm-profdata tool was introduced. This tool will merge profile data generated by PGO instrumentation in Clang, though may later pick up more functionality.
r201535
.
In a long overdue cleanup, various member variables were renamed from TD to DL to match the renaming of TargetData to DataLayout.
r201581
,
r201827
,
r201833
. Additionally, DebugLoc variables which were named DL have now been renamed to DbgLoc so as not to be confused with DataLayout.
r201606
.
MCAsmParser now supports required parameters in macros, increasing GNU assembler compatibility.
r201630
.
A new TargetLowering hook,
isVectorShiftByScalarCheap
was added to indicate whether it's significantly cheaper to shift a vector by a scalar rather than by another vector with different values for different lanes. This is used by the new
OptimizeShuffleVectorInst
in CodeGenPrepare which tries to sink shufflevector instructions down to the basic block they're used so CodeGen can determine if the right hand of a shift is really a scalar.
r201655
.
Private linkage is now properly supported for MachO.
r201700
.
getNameWithPrefix and getSymbol were moved from TargetLowering to TargetMachine, which removes the dependency from Target to CodeGen.
r201711
.
The PGO instrumentation will now compute counts in a separate AST traversal. The reasons for and advantages of this change are documented in detail in the commit message.
r201528
.
Some initial work was committed on documenting available attributes in Clang. Attribute authors are encouraged to submit missing documentation (the method of documentation is described in the addition to the InternalManual.rst).
r201515
.
The IdenticalExprChecker has been extended to check the two branches of an if as well as logical and bitwise expressions. For those not familiar, this checker tries to warn about the unintended use of identical expressions.
r201701
,
r201702
.
CGRecordLayoutBuilder has been completely rewritten to remove cruft, simplify the implementation, and to work in one pass.
r201907
.
The CastSizeChecker was taught how to correctly deal with flexible array members.
r201583
.
A number of thread-safety attributes have been renamed (with their old name silently deprecated). e.g.
lockable
is now
capability
,
exclusive_locks_required
is now
requires_capability
.
r201585
. Additionally, the documentation was updated and greatly expanded.
r201598
.
Initial virtual file system support
discussed previously on the mailing list
has landed.
r201618
,
r201635
.
The vcvtX intrinsics were added for v8 ARM as opposed to only being recognised when targeting AArch64.
r201661
.
The hard-float ARM EABI (often known as gnueabihf) is now supported for FreeBSD.
r201662
.
Clang will now provide
max_align_t
in C11 and C++11 modes. Note the complaint in the commit message though that
max_align_t
as defined is not 'good' or 'useful'.
r201729
.
Again, there were a number of commits related to increasing compatibility with the MS ABI. None of them immediately leaped out at me as worth highlighting individually, so I recommend you have a flick through last weeks commits if you're particularly interested.
