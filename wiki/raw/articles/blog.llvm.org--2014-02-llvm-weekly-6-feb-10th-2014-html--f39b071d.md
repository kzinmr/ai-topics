---
title: "LLVM Weekly - #6, Feb 10th 2014"
url: "https://blog.llvm.org/2014/02/llvm-weekly-6-feb-10th-2014.html"
fetched_at: 2026-05-05T07:01:42.610454+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #6, Feb 10th 2014

Source: https://blog.llvm.org/2014/02/llvm-weekly-6-feb-10th-2014.html

LLVM Weekly - #6, Feb 10th 2014
Welcome to the sixth issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
Alex Bradbury
. Subscribe to future issues at
http://llvmweekly.org
and pass it on to anyone else you think may be interested. Please send any tips or feedback to
asb@asbradbury.org
, or
@llvmweekly
or
@asbradbury
on Twitter. I've been keeping the
@llvmweekly Twitter account
updated throughout the week, so follow that if you want more frequent news updates.
The canonical home for this issue
can be found here at llvmweekly.org
.
News and articles from around the web
Alexi Starovoitov has
published an LLVM backend
targeting an extended version of the Linux Kernel's BPF. An example of the sort of program that might be compiled and run via BPF can be found
here
.
There is now under a week to go to submit proposals for presentations, tutorials, posters, etc for the upcoming
EuroLLVM 2014
. Get writing!
LWN's coverage of the recent discussion about LLVM and its licensing on the GCC mailing list is
now available
to non-subscribers.
Renato Golin
posted to the GCC mailing list
suggesting there be more collaboration where possible on issues such as standardisation of command line interfaces, language extensions, or just general technical discussion.I know a mailing list GCC developers who want to keep abreast of LLVM/Clang developments should subscribe to...
Phoronix has
published a benchmark
comparing GCC 4.8.2, a GCC 4.9 snapshot and Clang 3.4 on an Intel Core i5-4670 system.
On the mailing lists
LLVM commits
The x86 backend was slightly simplified by moving some matching for x86 bit manipulation instructions from X86ISelLowering.cpp to X86InstrInfo.td. I mention this commit mainly as it's a useful reference for those of you working on LLVM backend code.
r200824
.
The register allocator gained a new 'last chance recoloring mechanism'. Sadly the commit message doesn't include any data of how this improves register allocation for a given codebase.
r200883
.
The old SmallPtrSetImpl was renamed to SmallPtrSetImplBase, and a new SmallPtrSetImpl was introduced. This new SmallPtrSetImpl doesn't require a specific set size to be specified in its templated parameter.
r200688
.
A whole bunch of code was added to CodeGenPrepare which attempts to move sign extensions away from loads in order to increase the chance that the address computation can be folded in to the load on architectures like x86 with complex addressing modes.
r200947
.
strchr(p, 0)
is now simplified to
p + strlen(p)
.
r200736
.
Information on handling minor ('dot') releases was added to the HowToReleaseLLVM documentation.
r200772
.
The MIPS assembler learned to understand
%hi(sym1 - sym2)
and
%hi(sym1 - sym2)
expressions.
r200783
.
Mips gained a NaCl target.
r200855
.
LLVM now assumes the assembler supports the
.loc
directive for specifying debug line numbers.
r200862
.
The inliner was modified to consider the cold attribute on a function when deciding whether to inline.
r200886
. A later commit set the inlinecold-threshold to the same as the inline-threshold so that current inlining behaviour is maintained for now.
r200898
.
Initial implementation for a lazy call graph analysis pass (for use with the upcoming new pass manager) was committed.
r200903
.
The allowsUnalignedMemoryAccess function in TargetLowering now takes an address space argument. This was added for architectures like the R600 where different address spaces have different alignment requirements.
r200887
.
Clang commits
More support was MS ABI-compatible mangling was added.
r200857
.
The behaviour suggested by the C++ Defect Report
329
was implemented.
r200673
.
The ARM target gained support for crypto intrinsics defined in
arm_neon.h
.
r200708
.
The forRangeStmt AST matcher gained a handy hasLoopVariable sub-matcher.
r200850
.
The -verify-pch CC1 option is now supported.
r200884
.
The -fhiding-week-vtables CC1 option has been removed.
r201011
.
LLVM's new diagnostic system is now wired into clang's diagnostic system.
r200931
.
Other project commits
The address sanitizer gained two functions that would allow implementation of C++ garbage collection to work with its fake stack.
r200908
.
In lldb, the the Mac OS X SystemRuntime plugin now uses the libBacktraceRecording library.
r200822
.
