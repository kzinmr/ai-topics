---
title: "LLVM Weekly - #118, Apr 4th 2016"
url: "https://blog.llvm.org/2016/04/llvm-weekly-118-apr-4th-2016.html"
fetched_at: 2026-05-05T07:01:39.119464+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #118, Apr 4th 2016

Source: https://blog.llvm.org/2016/04/llvm-weekly-118-apr-4th-2016.html

LLVM Weekly - #118, Apr 4th 2016
Welcome to the one hundred and eighteenth issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
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
Almost all slides from the recent EuroLLVM conference are
now available online
for your enjoyment.
Some readers my be interested in a new paper about the 'LifeJacket' tool for
verifying precise floating-point optimisations in LLVM
.
Christian Neumüller has written a
new tool for syntax highlighting and cross-referencing C and C++ source
using libclang.
On the mailing lists
LLVM commits
The Lanai backend has landed.
r264578
.
A new
llvm.experimental.guard
intrinsic has been added. As described in the accompanying documentation, along with deoptimization operand bundles this allows frontends to express guards or checks on optimistic assumptions made during compilation.
r264976
.
Support for a number of new Altivec instructions has been added. Amazingly, this includes BCD (Binary Coded Decimal) instructions.
r264568
.
The concept of MachineFunctionProperties has been introduced, with the first property being AllVRegsAllocated. This allows passes to declare that they require a particular property, in this case requiring that they be run after regalloc.
r264593
.
On X86, push will now be used in preference to mov at all optimisation levels (before it was only enabled for
-Os
).
r264966
.
LLVM's support library can now compute SHA1 hashes. This is used to implement a 'build-id'.
r265094
,
r265095
.
When metadata is only referenced in a single function, it will now be emitted just in that function block. The aim of this is to improve the potential of lazy-loading.
r265226
.
Clang commits
Other project commits
Parts of LLD are starting to use the new Error handling.
r264910
,
r264921
,
r264924
, and more.
Infrastructure was added to LLD for generating thunks (as required on platforms like MIPS when calling PIC code from non-PIC).
r265059
.
