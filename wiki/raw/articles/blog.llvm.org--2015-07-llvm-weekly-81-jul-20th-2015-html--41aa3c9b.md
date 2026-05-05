---
title: "LLVM Weekly - #81, Jul 20th 2015"
url: "https://blog.llvm.org/2015/07/llvm-weekly-81-jul-20th-2015.html"
fetched_at: 2026-05-05T07:01:40.375948+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #81, Jul 20th 2015

Source: https://blog.llvm.org/2015/07/llvm-weekly-81-jul-20th-2015.html

LLVM Weekly - #81, Jul 20th 2015
Welcome to the eighty-first issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
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
I'm "on holiday" (at EuroPython) this week in Bilbao, mostly helping out the Raspberry Pi team with the education track. Do say hello, particularly if you want to chat lowRISC, LLVM, or Raspberry Pi.
The canonical home for this issue
can be found here at llvmweekly.org
.
News and articles from around the web
LLVM 3.6.2
has been released
.
LLVM and Clang 3.7
has been branched
.
The team behind Pyston, the LLVM-based Python JIT have written a blog post about
their new object code caching feature
.
On the mailing lists
LLVM commits
The API to determine callee-save registers has been rewritten.
r242165
.
The 'debugger tuning' concept has been introduced, allowing the specification of the debugger the debug info should be optimised for. This defaults to lldb on OS X and FreeBSD and GDB for everything else (other than PS4, which defaults to the SCE debugger).
r242388
.
Intrinsics for absolute difference operations have been introduced.
r242409
.
The PostRAScheduler has been disabled for the Apple Swift CPU and MachineScheduler is used in place. The commit message argues PostRAScheduler is not a good fit for out-of-order architectures and suggests the same switch might be worth while for other ARM OoO CPUs.
r242500
.
Clang commits
Support for armv7-windows-gnu targets has been added to the Clang front-end.
r242292
.
The clang module container format is now selectable from the command line (raw or obj).
r242499
.
A minimal AMDGPU toolchain configuration has been added.
r242601
.
Other project commits
LLD now supports MIPS big-endian targets.
r242014
.
LLDB's gdbserver is moving towards being a single-threaded application.
r242018
.
The OpenMP CMake build system has been massively refactored.
r242298
.
