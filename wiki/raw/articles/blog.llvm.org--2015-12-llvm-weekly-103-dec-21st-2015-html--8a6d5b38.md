---
title: "LLVM Weekly - #103, Dec 21st 2015"
url: "https://blog.llvm.org/2015/12/llvm-weekly-103-dec-21st-2015.html"
fetched_at: 2026-05-05T07:01:39.589286+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #103, Dec 21st 2015

Source: https://blog.llvm.org/2015/12/llvm-weekly-103-dec-21st-2015.html

LLVM Weekly - #103, Dec 21st 2015
Welcome to the one hundred and third issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
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
Regular readers will know about lowRISC, a not-for-profit project a group of us founded aiming to produce a complete open-source System-on-Chip in volume. We've just hit a new milestone with the
untethering of the base SoC
. If you're interested in contributing, the blog post contains a number of potential starting points.
News and articles from around the web
The 6th EuroLLVM conference will be held on March 17th-18th in Barcelona, Spain. The
call for papers
is now open and will remain open until January 25th 2016. EuroLLVM CFP
Chandler Carruth's keynote, "Understanding compiler optimizations" from the Meeting C++ 2015 conference is
now online
.
Richard Pennington has blogged about
bootstrapping LLVM and Clang using pre-compiled ELLCC binaries
.
Bloomberg is going to be holding a
weekend Clang and LLVM hackathon
in NYC and in London on February 6th and 7th. The event will be open to everyone in the community and Bloomberg will provide space, power, food, beverages, and internet access.They're looking for experienced Clang and LLVM developers to help as mentors.
On the mailing lists
LLVM commits
LLVM IR now supports floating point atomic loads and stores.
r255737
.
New attributes have been introduced:
InaccessibleMemOnly
(a function may only access memory that is not accessible by the module being compiled) and
InaccessibleMemOrArgMemOnly
(a function may only access memory that is either not accessible by the module being compiled or is pointed to by its pointer arguments).
r255778
.
The PowerPC backend gained support for soft float operations on ppc32.
r255516
.
The
terminatepad
instruction has been removed from LLVM IR.
r255522
.
IR call instructions can now take a fast-math flags marker which indicates fast-math flags may allow otherwise unsafe optimisations.
r255555
.
LLVM gained a C++11 ThreadPool in its internal library. It is intended to be used for ThinLTO.
r255593
.
The default set of passes has been adjusted. mem2reg will not be run immediately after globalopt and more scalar optimization passes have been added to the LTO pipeline.
r255634
.
The llvm-profdata tool now supports specifying a weight when merging profile data. This can be used to give more relative importance to one of multiple profile runs.
r255659
.
For CMake builds, a
compile_commands.json
file will now be generated which tells tools like YouCompleteMe and
clang_complete
how to build each source file.
r255789
.
The Hexagon VLIW packetizer saw a large update (though unfortunately the changes aren't summarised in the commit message).
r255807
.
A number of LLVM's C APIs have been depreciated: LLVMParseBitcode, LLVMParseBitcodeInContext, LLVMGetBitcodeModuleInContext and LLVMGetBitcodeModule. These have been replaced with new versions of the functions which don't record a diagnostic.
r256065
.
The AVR backend (which is being imported incrementally) gained AVR.td and AVRRegisterInfo.td.
r256120
.
Clang commits
A new checker has been introduced to detect excess padding in classes and structs.
r255545
.
A new control-flow integrity mode was introduced, cross-DSO CFI allows control flow to be protected across shared objects. It is currently marked experimental.
r255694
.
Clang's CMake build system now supports generating profile data for Clang.
r255740
,
r256069
.
Other project commits
It is now possible to suppress reports from UndefinedBehaviourSanitizer for certain files, functions, or modules at runtime.
r256018
.
The llvm test-suite's CMake+Lit runner gained support for SPEC2000 and SPEC CPU95.
r255876
,
r255878
.
