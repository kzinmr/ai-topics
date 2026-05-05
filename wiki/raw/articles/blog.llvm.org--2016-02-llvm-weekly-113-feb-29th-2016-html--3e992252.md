---
title: "LLVM Weekly - #113, Feb 29th 2016"
url: "https://blog.llvm.org/2016/02/llvm-weekly-113-feb-29th-2016.html"
fetched_at: 2026-05-05T07:01:39.190712+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #113, Feb 29th 2016

Source: https://blog.llvm.org/2016/02/llvm-weekly-113-feb-29th-2016.html

LLVM Weekly - #113, Feb 29th 2016
Welcome to the one hundred and thirteenth issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
Alex Bradbury
. Subscribe to future issues at
http://llvmweekly.org
and pass it on to anyone else you think may be interested. Please send any tips or feedback to
asb@asbradbury.org
, or @llvmweekly or @asbradbury on Twitter.
News and articles from around the web
LLVM and Clang 3.8RC3
has been tagged
.
EuroLLVM 2016 is
less than a month away
. If you want to attend, be sure to
register
.
The Red Hat blog has a
summary of new features in the upcoming GCC 6 release
.
The Meeting C++ blog has a
helpful summary of a subset of the proposals for the next C++ committee meeting
.
On the mailing lists
LLVM commits
The Sparc backend now contains definitions for all registers and instructions defined in the Sparc v8 manual.
r262133
.
LLVM gained a basic LoopPassManager, though it currently only contains dummy passes.
r261831
.
A number of TargetInstrInfo predicates now take a reference to a MachineInstr rather than a pointer.
r261605
.
The WebAssembly backend gained redzone support for the userspace stack.
r261662
.
Clang commits
Whole-program vtable optimisation is now available in Clang using the
-fwhole-program-vtables
flag.
r261767
.
Clang gained
__builtin_canonicalize
which returns the platform-specific canonical encoding of a floating point number.
r262122
.
A hasAnyName matcher was added.
r261574
.
The pointer arithmetic checker has been improved to report fewer false positives.
r261632
.
Other project commits
The new ELF linker gained support for identical code folding (ICF). This reduces the size of an LLD binary by 3.6% and of a Clang binary by 2.7%. As described in the commit message, this is not a "safe" version of ICF as implemented in GNU gold, so will cause issues if the input relies on two distinct functions always having distinct addresses.
r261912
.
Polly's tree now contains an
update_check.py
script that may be useful to other LLVM devs. It updates a FileCheck-based lit test by updating the
CHECK:
lines with the actual output of the
RUN:
command.
r261899
.
LLDB gained a new set of plugins to help debug Java programs, specifically Java code JIT-ed by the Android runtime.
r262015
.
The new OpenMP 4.5 affinity API is now supported in LLVM's openmp implementation.
r261915
.
The new ELF linker gained support for the
-r
command-line option, which produces relocatable output (partial linking).
r261838
.
The CMake/lit runner for SPEC in the LLVM test-suite can now run the C CPU2006 floating point benchmarks (but not the Fortran ones).
r261816
.
The old ELF linker has been deleted from LLD.
r262158
.
