---
title: "LLVM Weekly - #119, Apr 11th 2016"
url: "https://blog.llvm.org/2016/04/llvm-weekly-119-apr-11th-2016.html"
fetched_at: 2026-05-05T07:01:39.113973+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #119, Apr 11th 2016

Source: https://blog.llvm.org/2016/04/llvm-weekly-119-apr-11th-2016.html

LLVM Weekly - #119, Apr 11th 2016
Welcome to the one hundred and nineteenth issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
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
Last week the slides from the
recent EuroLLVM 2016 Developers' Meeting
made it online. This week this has been followed by
videos of the talks from the conference
.
John Regehr has written about
efficient integer overflow checking in LLVM
, looking at cases where LLVM can and cannot remove unnecessary overflow checks, and how this might be improved.
Version 0.13 of Pocl, the portable OpenCL implementation
has been released
. This release works with LLVM/Clang 3.8 and 3.7, and adds initial OpenCL 2.0 support and improved HSA support.
Serge Guelton at QuarksLab has written up a really useful guide to
implementing a custom directive handler in Clang
.
Microsoft's Visual C++ team are
looking for feedback on Clang/C2
(Clang with Microsoft CodeGen).
On the mailing lists
James Molloy has posted an RFC on adding support for
constant folding calls to math.h functions on long doubles
. Currently these functions aren't constant-folded as the internal APFloat class doesn't implement them and long double operations aren't portable. Solutions include adding support to APFloat, linking against libMPFR to provide compile-time evaluation, or recognising when the long double format of the host and target are the same, so the host math library can be called. From the responses so far, there seems to be some push-back on adding the libMPFR dependency.
Sanjoy Das has an RFC on
adding a patchable-prologue attribute
. This would be used to indicate that the function's prologue is compiled so as to provide support for easy hot-patching.
Ulrich Weigand has shared a patch for
supporting LLDB on Linux on SystemZ
. The patchset contains many big-endian fixes, and may be of interest to others looking at porting LLDB.
LLVM commits
The Swift calling convention as well as support for the 'swifterror' argument has been added.
r265433
,
r265480
.
Work on GlobalISel continues with many commits related to the assignment of virtual registers to register banks.
r265445
,
r265440
.
LLVM will no longer perform inter-procedural optimisation over functions that can be "de-refined".
r265762
.
The substitutions supported by lit are now documented.
r265314
.
Unrolled loops now execute the remainder in an epilogue rather than the prologue. This should produce slightly improved code.
r265388
.
Clang commits
Clang gained necessary support for the Swift calling convention.
r265324
.
New flags
-fno-jump-tables
and
-fjump-tables
can be used to disable/enable support for jump tables when lowering switch statements.
r265425
.
TargetOptions is now passed through all the TargetInfo constructors. This will allow target information to be modified based on the ABI selected.
r265640
.
A large number of intrinsics from emmintrin.h now have Doxygen docs.
r265844
.
Other project commits
clang-tidy gained a new check to flag initializers of globals that access extern objects, leading to potential order-of-initialization issues.
r265774
.
LLD's ELF linker gained new options
--start-lib
,
--end-lib
,
--no-gnu-unique
,
--strip-debug
.
r265710
,
r265717
,
r265722
.
