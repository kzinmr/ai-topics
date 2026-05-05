---
title: "LLVM Weekly - #56, Jan 26th 2015"
url: "https://blog.llvm.org/2015/01/llvm-weekly-56-jan-26th-2015.html"
fetched_at: 2026-05-05T07:01:41.001173+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #56, Jan 26th 2015

Source: https://blog.llvm.org/2015/01/llvm-weekly-56-jan-26th-2015.html

LLVM Weekly - #56, Jan 26th 2015
Welcome to the fifty-sixth issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
Alex Bradbury
. Subscribe to future issues at
http://llvmweekly.org
and pass it on to anyone else you think may be interested. Please send any tips or feedback to
asb@asbradbury.org
, or or
@llvmweekly
or
@asbradbury
on Twitter.
I'll be talking the
lowRISC
project to produce a fully open-source SoC at FOSDEM this coming weekend. Do come and see my
main track talk
and read my
speaker interview
for more background. There is of course an
LLVM toolchain devroom
on the Sunday.
The canonical home for this issue
can be found here at llvmweekly.org
.
News and articles from around the web
Stephen Diehl has written an absolutely fantastic tutorial on
writing an LLVM specializer for Python
, guiding you through the process of creating something like
Numba
.
A new tool,
Dwgrep
(DWARF Grep) may be of interest to many LLVM Weekly readers. This
blog post
gives an intro to using it.
Paul Smith has a blog post on
getting started with the LLVM C API
.
A post on the official LLVM Blog announces that
LLDB is coming to Windows
, announcing to a wider audience that it is now possible to debug simple programs with LLDB on Windows and giving a rationale for investing effort into porting LLDB to Windows and adding support for the MS debug format. The post also features a todo list indicating what's next for Windows support.
A draft version 0.1 of the IA-32 psABI (processor specific application binary interface) is
available
. This aims to supplement the existing System V ABI with conventions relevant to newer features such as SSE1-4 and AVX. Comments
are welcome
.
LLVM/Clang 3.6-rc1 is now
available
. Get testing and filing bugs.
ELLCC 0.1.8
has been released
. ELLCC is an LLVM/Clang-based cross compilation toolchain.
LLDB now
has it's own IRC channel
. You'll want to join #lldb on irc.oftc.net.
On the mailing lists
LLVM commits
A backend targeting the extended BPF (Berkeley Packet Filter) interpreter/JIT in the Linux kernel has been added. See
this LWN article
for more background.
r227008
.
The initial version of the new ORC JIT API has landed.
r226940
.
There's been a flurry of work on the new pass manager this week. One commit I will choose to pick out is the port of InstCombine to the new pass manager, which seems like a milestone or sorts.
r226987
.
LLVM learnt how to use the GHC calling convention on AArch64.
r226473
.
InstCombine will now canonicalize loads which are only ever stored to always use a legal integer type if one is available.
r226781
.
The
llvm_any_ty
type for intrinsics has been born.
r226857
.
llvm-objdump now understands
-indirect-symbols
to dump the Mach-O indirect symbol table.
r226848
.
Clang commits
Clang now supports SPIR calling conventions.
r226548
.
It's now possible to set the stack probe size on the command line.
r226601
.
Clang gained initial support for Win64 SEH IR emission.
r226760
.
Other project commits
Sun Solaris users, now is the time to celebrate. libc++ will now build on your platform of choice.
r226947
.
A minimal implementation of ARM static linking landed in lld.
r226643
.
Basic support for PPC was added to openmp.
r226479
.
