---
title: "LLVM Weekly - #122, May 2nd 2016"
url: "https://blog.llvm.org/2016/05/llvm-weekly-122-may-2nd-2016.html"
fetched_at: 2026-05-05T07:01:38.978641+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #122, May 2nd 2016

Source: https://blog.llvm.org/2016/05/llvm-weekly-122-may-2nd-2016.html

LLVM Weekly - #122, May 2nd 2016
Welcome to the one hundred and twenty-second issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
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
GCC 6.1
has been released
. Perhaps the most apparent user-visible change is that the C++ frontend now defaults to C++14.
The Rust compiler has
introduced a new intermediate representation
, MIR, used for optimisations prior to lowering to LLVM IR.
Tanya Lattner has
written about the LLVM Foundation's plans for 2016
. The LLVM Foundation has established 3 main programs: Educational Outreach, Grants and Scholarships, and Women in Compilers and Tools.
On the mailing lists
LLVM commits
LLVM now supports indirect call promotion based on value-profile information. This will promote indirect calls to a direct call guarded by a precondition.
r267815
.
The LLVM documentation has been extended with a CMake primer covering the basics of the CMake scripting language.
r268096
.
The PDB dumper has been refactored into a library.
r267431
.
The MinLatency attributed has been removed from SchedMachineModel.
r267502
.
CodeGenPrepare will now use branch weight metadata to decide if a select should be turned into a branch.
r267572
.
Support for
llvm.loop.distribute.enable
metadata was added. This indicates a loop should be split in to multiple loops.
r267672
.
The SystemZ backend now supports the Swift calling convention.
r267823
.
libFuzzer's documentation has been expanded and improved.
r267892
.
Clang commits
clang-tidy gained a new checker for redundant expressions on both sides of a binary operator.
r267574
.
A new clang-tidy check will warn for use of functions like
atoi
and
atol
that don't report conversion errors.
r268100
.
The
nodebug
attribute on a global or static variable will now suppress all debug info for that variable.
r267746
.
A number of OpenMP features gained codegen support, such as the map clause and target data directive.
r267808
,
r267811
.
Other project commits
LLD now supports an
-O0
option to produce output as quickly as possible. Currently this disables section merging at the cost of a potentially much larger output.
r268056
.
The symbol table in LLD's ELF linker has been redesigned with the intent of improving memory locality. The new design produces measurable speedups for the binaries tested in the commit message.
r268178
.
LLD's linkerscript support expanded to encompass comparison operators.
r267832
.
LLD performance on large executables has been improved by skipping scanRelocs on sections that are never mapped to memory at runtime (e.g. debug sections).
r267917
.
