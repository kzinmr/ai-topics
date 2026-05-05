---
title: "LLVM Weekly - #24, Jun 16th 2014"
url: "https://blog.llvm.org/2014/06/llvm-weekly-24-jun-16th-2014.html"
fetched_at: 2026-05-05T07:01:42.148128+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #24, Jun 16th 2014

Source: https://blog.llvm.org/2014/06/llvm-weekly-24-jun-16th-2014.html

Welcome to the twenty-fourth issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
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
A weak variant of cmpxchg has been added to the LLVM IR, as has been
argued for
on the mailing list. Weak cmpxchg allows failure and the operation returns
{iN, i1}
(in fact, for uniformity all cmpxchg instructions do this now). According to the commit message, this change will mean legacy assembly IR files will be invalid but legacy bitcode files will be upgraded during read.
r210903
.
X86 FastISel gained support for handling a bunch more intrinsics.
r210709
,
r210720
and more. FastISel also saw some target-independent improvements
r210742
.
This week there were many updates to the MIPS backend for mips32r6/mips64r6. e.g.
r210899
,
r210784
and many more.
NoSignedWrap, NoUnsignedWrap and Exact flags are now exposed to the SelectionDAG.
r210467
.
Support has been added for variable length arrays on the Windows on ARM Itanium ABI.
r201489
.
Some simple reordering of fields in Value and User saves 8 bytes of padding on 64-bit.
r210501
.
FastISel will now collect statistics on when it fails with intrinsics.
r210556
.
The MIPS backend gained support for jr.hb and jalr.hb (jump register with hazard barrier, jump and link register with hazard barrier).
r210654
.
AArch64 gained a basic schedule model for the Cortex-A57.
r210705
.
LLVM has transitioned to using
std::error_code
instead of
llvm::error_code
.
r210687
.
