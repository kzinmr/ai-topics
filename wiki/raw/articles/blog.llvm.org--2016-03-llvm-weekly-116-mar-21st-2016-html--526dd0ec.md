---
title: "LLVM Weekly - #116, Mar 21st 2016"
url: "https://blog.llvm.org/2016/03/llvm-weekly-116-mar-21st-2016.html"
fetched_at: 2026-05-05T07:01:39.168501+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #116, Mar 21st 2016

Source: https://blog.llvm.org/2016/03/llvm-weekly-116-mar-21st-2016.html

LLVM Weekly - #116, Mar 21st 2016
Welcome to the one hundred and sixteenth issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
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
If you're a student and would like to get paid to work on an LLVM-related project over the summer then do consider
applying for Google Summer of Code with LLVM
. More details about Summer of Code are available
here
. The deadline for applications is this Friday, March 25th at 1900 GMT. I'd also encourage you to look at
lowRISC's project ideas
if you have an interest in open source hardware.
Stephen Kelly has written about his
new Clang-based tool for porting a C++ codebase to use almost-always-auto
. As was pointed out on Twitter, Ryan Stortz from Trail of Bits has a tools that removes auto and does
roughly the opposite
.
Honza Hubička has written up his experiments of
building LibreOffice with GCC6 and LTO
. This includes a comparison to a build using LLVM and Clang.
Nick Clifton has shared an update for February and March
on the GNU toolchain
that may be of interest.
The developer of the Capstone disassembly framework and the Unicorn multi-architecture simulator is running a funding campaign for the
Keystone multi-architecture assembler framework
. Like Capstone, this will build on LLVM but also
aims to go beyond it
.
On the mailing lists
LLVM commits
A new Error support class has been added to support structured error handling. See the associated updates to the LLVM programmer's manual for more info.
r263609
.
New documentation was committed for advanced CMake build configurations.
r263834
.
Support was added for MIPS32R6 compact branches.
r263444
.
The MemCpyOptimizer will now attempt to reorder instructions in order to create an optimisable sequence.
r263503
.
llvm-readobj learnt to print sections and relocations in the GNU style.
r263561
.
Clang commits
Attributes have been added for the
preserve_mostcc
and
preserve_allcc
calling conventions.
r263647
.
clang-format will handle some cases of automatic semicolon insertion in JavaScript.
r263470
.
Clang learned to convert some Objective-C message sends to runtime calls.
r263607
.
Other project commits
AddressSanitizer is now supported on mips/mips64 Android.
r263261
.
The documentation on the LLD linker has added a few numbers to give an idea of the sort of inputs it needs to handle. e.g. Chrome with debug info contains roughly 13M relocations, 6.3M symbols, 1.8M sections and 17k files.
r263466
.
