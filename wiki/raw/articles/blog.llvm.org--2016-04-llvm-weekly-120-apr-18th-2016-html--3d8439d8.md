---
title: "LLVM Weekly - #120, Apr 18th 2016"
url: "https://blog.llvm.org/2016/04/llvm-weekly-120-apr-18th-2016.html"
fetched_at: 2026-05-05T07:01:38.973318+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #120, Apr 18th 2016

Source: https://blog.llvm.org/2016/04/llvm-weekly-120-apr-18th-2016.html

LLVM Weekly - #120, Apr 18th 2016
Welcome to the one hundred and twentieth issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
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
This week has seen not one, but two articles about LLVM and profile-guided optimisation. Dig in John Engelen's article about
optimising D's virtual function calls with PGO
, then read Geoffroy Couprie's article about
PGO with Rust
.
The next Cambridge (UK) social
will be at 7.30pm on April 20th
, at the Cambridge Blue.
Alex Denisov has written a blog post
around the idea of building a mutation testing system using LLVM
.
On the mailing lists
LLVM commits
AtomicExpandPass learned to lower various atomic operations to
__atomic_*
library calls. The eventual aim is to move all atomic lowering from Clang to LLVM.
r266115
.
Targets can now define an inlining threshold multiplier, to e.g. increase the likelihood of inlining on platforms where calls are very expensive.
r266405
.
The ownership between DICompileUnit and DISubprogram has been reversed. This may break tests for your out-of-tree backend, but the commit has a link to a Python script to update your testcases.
r266446
.
llvm-readobj learned to print a histogram of an input ELF file's .gnu.hash .
r265967
.
More target-specific support for the Swift calling convention (on ARM, AARch64, and X86) has landed. Also, a callee save register is used for the swiftself parameter.
r265997
,
r266251
.
A new
allocsize
attribute has been introduced. This indicates the given function is an allocation function.
r266032
.
analyzeSiblingValues has been replaced with a new lower-complexity implementation in order to reduce compile times.
r266162
.
The AMDGPU backend gained a skeleton GlobalISel implementation.
r266356
.
Every use of getGlobalContext other than the C API has been removed.
r266379
.
Clang commits
Clang gained support for the GCC ifunc attribute.
r265917
.
The
__unaligned
type qualifier was implemented for MSVC compatibility.
r266415
.
Support for C++ core guideline Type.6: always initialize a member variable was completed in clang-tidy.
r266191
.
A new clang-tidy checker for suspicious sizeof expressions was added.
r266451
.
Other project commits
The way relocations are applied in the new ELF linker has been reworked.
r266158
.
ELF LLD now supports parallel codegen for LTO using splitCodeGen.
r266484
.
Support for Linux on SystemZ in LLDB landed.
r266308
.
