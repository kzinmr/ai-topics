---
title: "LLVM Weekly - #60, Feb 23rd 2015"
url: "https://blog.llvm.org/2015/02/llvm-weekly-60-feb-23rd-2015.html"
fetched_at: 2026-05-05T07:01:40.956194+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #60, Feb 23rd 2015

Source: https://blog.llvm.org/2015/02/llvm-weekly-60-feb-23rd-2015.html

LLVM Weekly - #60, Feb 23rd 2015
Welcome to the sixtieth issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
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
LLVM/Clang 3.6.0-rc4 is
now available for testing
.
A new LLVM-based tainted flow analysis tool
has been created
. It's a tool designed to help detect timing attack vulnerabilities. An
online demo
is available.
The March bay-area LLVM social
will take place on Thursday 5th March
, along with the Game Developer's Conference.
The Cambridge LLVM social will take place
on Wednesday 25th Feb
.
HHVM, the optimised PHP virtual machine from Facebook
plan to integrate an LLVM-based optimisation phase
.
On the mailing lists
LLVM commits
The coding standards document has been updated now that MSVC 2012 support has been dropped.
r229369
.
The Orc API continues to evolve. The JITCompileCallbackManager has been added to create and manage JIT callbacks.
r229461
.
A new pass, the bit-tracking dead code elimination pass has been added. It tracks dead bits of integer-valued instructions and removes them when all bits are set.
r229462
.
The SystemZ backend now supports all TLS access models.
r229652
,
r229654
.
A new pass for constructing gc.statepoint sequences with explicit relocations was added. The pass will be further developed and bugfixed in-tree.
r229945
.
The old x86 vector shuffle lowering code has been removed (the new shuffle lowering code has been the default for ages and known regressions have been fixed).
r229964
.
A new bitset metadata format and lowering pass has been added. In the future, this will be used to allow a C++ program to efficiently verify that a vtable pointer is in the set of valid vtable pointers for the class or its derived classes.
r230054
.
Clang commits
clang-format gained support for JS type annotations and classes.
r229700
,
r229701
.
Most of the InstrProf coverage mapping generation code has been rewritten.
r229748
.
Clang learnt how to analyze FreeBSD kernel printf extensions.
r229921
.
Support has been added to Clang for a form of Control Flow Integrity for virtual function calls. It verifies the vptr of the correct dynamic type is being used.
r230055
.
Other project commits
ThreadSanitizer gained support for MIPS64.
r229972
.
lldb now supports process language on Android from lldb-gdbserver.
r229371
.
OpenMP gained a new user-guided lock API.
r230030
.
