---
title: "LLVM Weekly - #106, Jan 11th 2016"
url: "https://blog.llvm.org/2016/01/llvm-weekly-106-jan-11th-2016.html"
fetched_at: 2026-05-05T07:01:39.757769+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #106, Jan 11th 2016

Source: https://blog.llvm.org/2016/01/llvm-weekly-106-jan-11th-2016.html

LLVM Weekly - #106, Jan 11th 2016
Welcome to the one hundred and sixth issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
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
Many readers may be interested that last week was the 3rd RISC-V Workshop. You can find slides from the two
lowRISC
talks
here
and
here
. You may also want to read my
liveblog of the event
.
News and articles from around the web
The BSD Now podcast recently
interviewed Alex Rosenberg
about his work on LLVM/Clang and FreeBSD.
The folks at QuarksLab have shared a
Clang hardening cheat sheet
.
LLDB 3.8 will
feature initial Go debugging support
.
The next Paris LLVM Social will be held
on January 27th
and includes a talk from John Regehr.
The next Zurich LLVM Social
will be taking place on January 14th
.
On the mailing lists
LLVM commits
LLVM gained the
-print-funcs
option which can be used to filter IR printing to only certain functions.
r256952
.
The LLVM ADT library gained a new sum type abstraction for pointer-like types and an abstraction for embedding an integer within a pointer-like type.
r257282
,
r257284
.
LLVM now recognises the Samsung Exynos M1 core.
r256828
.
InstCombine learned to expose more constants when comparing getelementptrs (GEPs) by detecting when both GEPs could be expressed as GEPs with the same base pointer.
r257064
.
SelectionDAGBuilder will set NoUnsignedWrap for an inbounds getelementptr and for load/store offsets.
r256890
.
AArch64 MachineCombine will now allow fadd and fmul instructions to be reassociated.
r257024
.
Macro emission in DWARFv4 is now supported.
r257060
.
llvm-symbolizer gained the
-print-source-context-lines
option to print source code around the line.
r257326
.
Clang commits
Clang's CMake build system can now perform a multi-stage bootstrap build with profile-guided optimisation.
r256873
.
Clang's command line frontend learned to handle a whole bunch of
-fno-builtin-*
arguments.
r256937
.
The new ELF LLD linker will now be used for th AMDGPU target.
r257175
.
Other project commits
The performance of string table construction in the LLD ELF linker has been improved. This improves link time of lld by 12% from 3.50 seconds to 3.08 seconds.
r257017
.
The LLD ELF linker gained support for the AMDGPU target.
r257023
.
