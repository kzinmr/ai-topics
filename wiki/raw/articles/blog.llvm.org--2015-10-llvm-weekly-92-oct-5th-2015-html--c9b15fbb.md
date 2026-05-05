---
title: "LLVM Weekly - #92, Oct 5th 2015"
url: "https://blog.llvm.org/2015/10/llvm-weekly-92-oct-5th-2015.html"
fetched_at: 2026-05-05T07:01:39.974072+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #92, Oct 5th 2015

Source: https://blog.llvm.org/2015/10/llvm-weekly-92-oct-5th-2015.html

LLVM Weekly - #92, Oct 5th 2015
Welcome to the ninety-second issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
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
Most of the presentation materials from CppCon2015 are
now online
. Talks that may be of particular interest include
Kostya Serebryany on fuzzing with libFuzzer
,
Piotr Padlewski on C++ devirtualization in Clang
, and
JF Bastien talking about C++ on the web
.
Rafael Espíndola wrote in to share an impressive milestone for the new LLD ELF linker. It can now link itself and all of LLVM and Clang (though not all tests pass, and you must use
LLVM_ENABLE_THREADS=OFF
). Things will of course get really interesting once LLD matures if it can compete with Gold in terms of speed.
The next Paris LLVM social will
take place on October 15th
. Calixte Denizet will be talking about Scilab's usage of LLVM.
On the mailing lists
LLVM commits
A scheduler for the MIPS P5600 processor landed.
r248725
.
Align metadata for the load instruction was introduced.
r248721
.
Support for windows exception handling continues with support in AsmPrinter for 'funclets'.
r248824
.
Support landed for the HHVM JIT calling convention.
r248832
.
Clang commits
clang-format's
#include
sorting functionality has been extended.
r248782
.
Other project commits
The new ELF linker gained initial support for MIPS.
r248779
.
Some basic linker script support was added to the new ELF linker, enough to parse Linux's libc.so.
r248918
.
.ARM.exidx and .ARM.extab unwind information is now supported by lldb.
r248903
.
