---
title: "LLVM Weekly - #110, Feb 8th 2016"
url: "https://blog.llvm.org/2016/02/llvm-weekly-110-feb-8th-2016.html"
fetched_at: 2026-05-05T07:01:39.326830+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #110, Feb 8th 2016

Source: https://blog.llvm.org/2016/02/llvm-weekly-110-feb-8th-2016.html

LLVM Weekly - #110, Feb 8th 2016
Welcome to the one hundred and tenth issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
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
Slides from the LLVM devroom at FOSDEM last weekend are
now available online
. Unfortunately there was an issue with the recording of the talks so videos will not be available.
JavaScriptCore's
FTL JIT
is moving away from using LLVM as its backend, towards
B3 (Bare Bones Backend)
. This includes its own
SSA IR
, optimisations, and instruction selection backend.
Source tarballs and binaries are
now available
for LLVM and Clang 3.8-RC2.
The Zurich LLVM Social
is coming up this Thursday
, February 11th at 7pm.
Jeremy Bennett has written up a
comparison of the Clang and GCC command-line flags
. The headline summary is that 397 work in both GCC and LLVM, 433 are LLVM-only and 598 are GCC-only.
vim-llvmcov
has been released. It is a vim plugin to show code coverage using the llvm-cov tool.
On the mailing lists
Mehdi Amini has posted an
RFC on floating point environment and rounding mode handling in LLVM
. The work started all the way back in 2014 and has a whole bunch of patches up for review. Chandler Carruth has responded with a
detail description of his concerns about the current design
, and his proposed alternative seems to be getting a lot of positive feedback.
Morten Brodersen has recently upgraded a number of applications from the old JIT to the new MCJIT under LLVM 3.7.1 but has
found significant performance regressions
. Some other respondents have seen similar issues, either in compilation time or in reduced code quality in the generated code. Some of the thread participants will be providing specific examples so they can be investigated. It's possible the issue is something as simple as a different default somewhere. Benoit Belley noted
they saw regressions due to their frontend's use of allocas in 3.7
.
Lang Hames kicked off a long discussion about
error handling in LLVM libraries
. Lang has implemented a new scheme and is seeking feedback on it. There's a lot of discussion that unfortunately I haven't had time to summarise properly. If error handling design interests you, do get stuck in.
Adrian McCarthy has written up details on the
recent addition of minidump support to LLDB
. Minidumps are the Windows equivalent of a core file.
Juan Wajnerman is looking at adding support for multithreading to the Crystal language, and has a
question about thread local variables
. LLVM won't re-load the thread local address, which causes issues when a thread local variable is read in a coroutine running on one thread which is then suspended and continued on a different thread. This is apparently a known issue, covered by
PR19177
.
Steven Wu has posted an
RFC on embedding bitcode in object files
. The intent is to upstream support that already exists in Apple's fork. Understandably some of the respondents asked how this relates to the .llvmbc section that the Thin-LTO work is introducing. Steven indicates it's pretty much the same, but for Mach-O rather than ELF and that he hopes to unify them during the upstreaming.
LLVM commits
LLVM now has a memory SSA form. This isn't yet used by anything in-tree, but should form a very useful basis for a variety of analyses and transformations. This patch has been baking for a long time, first being submitted for initial feedback in April last year.
r259595
.
A new loop versioning loop-invariant code motion (LICM) pass was introduced. This enables more opportunities for LICM by creating a new version of the loop guarded by runtime checks to test for potential aliases that can't be determined not to exist at compile-time.
r259986
.
LazyValueInfo gained an intersect operation on lattice values, which can be used to exploit multiple sources of facts at once. The intent is to make greater use of it, but already it is able to remove a half range-check when performing jump-threading.
r259461
.
The SmallSet and SmallPtrSet templates will now error out if created with a size greater than 32.
r259419
.
The ability to emit errors from the backend for unsupported features has been refactored, so BPF, WebAssembly, and AMDGPU backends can all share the same implementation.
r259498
.
A simple pass using LoopVersioning has been added, primarily for testing. The new pass will fully disambiguate all may-aliasing memory accesses no matter how many runtime checks are required.
r259610
.
The way bitsets are used to encode type information has now been documented.
r259619
.
You can now use the flag
-DLLVM_ENABLE_LTO
with CMake to build LLVM with link-time optimisation.
r259766
.
TableGen's AsmOperandClass gained the
IsOptional
field. Setting this to 1 means the operand is optional and the AsmParser will not emit an error if the operand isn't present.
r259913
.
There is now a scheduling model for the Exynos-M1.
r259958
.
Clang commits
Other project commits
AddressSanitizer now supports iOS.
r259451
.
The current policy for using the new ELF LLD as a library has been documented.
r259606
.
Polly's new Sphinx documentation gained a guide on using Polly with Clang.
r259767
.
