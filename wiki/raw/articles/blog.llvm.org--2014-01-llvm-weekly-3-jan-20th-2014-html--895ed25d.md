---
title: "LLVM Weekly - #3, Jan 20th 2014"
url: "https://blog.llvm.org/2014/01/llvm-weekly-3-jan-20th-2014.html"
fetched_at: 2026-05-05T07:01:43.011476+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #3, Jan 20th 2014

Source: https://blog.llvm.org/2014/01/llvm-weekly-3-jan-20th-2014.html

LLVM Weekly - #3, Jan 20th 2014
Welcome to the third issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
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
Eli Bendersky has penned
some thoughts on LLVM vs. libjit
. Eli describes libjit as being more limited, yet easier to understand and to get going with due to its focus. He also makes interesting claims such as "to be honest, I don't think it's possible to create a really fast JIT within the framework of LLVM, because of its modularity. The faster the JIT, the more you’ll have to deviate from the framework of LLVM". As well as the comments directly on the blog post, there is some good discussion over
at Reddit
.
Version 2.0-RC1 Capstone disassembly framework has been released
. Capstone is built using code from LLVM. The new release features reduced memory usage, faster Python bindings, and support for PowerPC among other changes.
Planet Clang
has been
announced
. It is a news feed following blog posts from Clang and LLVM committers and contributors. The blog roll is fairly short right now, but you're welcome to submit your RSS feed via the email address in the announcement post.
The PDF of an upcoming paper to be presented at CGO next month has been released.
WatchdogLite: Hardware-Accelerated Compiler-Based Pointer Checking
proposes instruction set extensions to accelerate pointer checking functions and achieves a performance overhead of 29% in return for memory safety. The compiler extends (and is compared to)
SoftBound + CETS
.
On the mailing lists
David Woodhouse has posted a
detailed update on the status of 16-bit x86 in LLVM
. David has successfully built the 16-bit startup code of the Linux kernel and invites people to start testing it on real code.
Tom Stellard opens a discussion on
stable LLVM 3.4.x releases
. A number of people volunteer their assistance and there seems to be general agreement that any 3.4.1 release would include bug-fixes only with no ABI changes.
Diego Novillo is looking to boost the performance of the SPEC benchmark libquantum
using profile info and loop unrolling
. Sean Silva did us all a great service by asking for clarification on what a "runtime unroller" means in this context. The answer is that the trip count (the number of times the loop is executed) is not known at compile time. The thread is worth a read if you're interested in loop unrolling or vectorization.
Aaron Ballman has stepped up as
code owner for the attribute subsystem
with unanimous approval.
Skye Wanderman-Milne was looking for help on
loop unrolling a single function using the C++ API
. Simply adding the LoopUnrollPass to a FunctionPassManager had no effect, but after some advice from the mailing list Skye did respond to confirm that the set of ScalarReplAggregates, LoopRotate, and LoopUnroll passes did have the desired effect.
Tobias Grosser asks why LLVM's LNT (used for performance tracking) defaults to
aggregating results by taking the minimum rather than an average
. Replies quickly hone on in the real problem at hand, which is that results are 'noisy' potentially due to other processes on the machine but also quantised to certain values due to the timer being relatively coarse-grained in comparison to the execution time for the benchmarks.
This week's unsolved question is from Keith Walker, who's noticed that on ARM, the function prologue generated in GCC and LLVM ends up with
the frame register pointing to a different address
. The LLVM prologue results in the frame pointer pointing to just after the pushed r11 register (the saved frame pointer) while on GCC the frame pointer points to just after the pushed link register. The difference makes it difficult to produce a generic stack walker.
LLVM commits
The MCJIT remote execution protocol was heavily refactored and it was hoped fixed on ARM where it was previously non-functional. There are still some random failures on ARM though, see
bug 18507
.
r199261
The cutoff on when to attempt to convert a switch to a lookup table was changed from 4 to 3. Experimentally, Hans Wennborg found that there was no speedup for two cases but three produced a speedup. When building Clang, this results in 480 new switches to be transformed and an 8KB smaller binary size.
r199294
Support for the
preserve_mostcc
and
preserve_allcc
calling conventions was introduced and implemented for x86-64. These are intend to be used by a future version of the ObjectiveC runtime in order to reduce overhead of runtime calls.
r199508
The configure script now checks for a sufficiently modern host compiler (Clang 3.1 or GCC 4.7)
r199182
More work on the new PassManager driver. Bitcode can now be written using the new PM and more preparation/cleanup work has been performed.
r199078
,
r199095
,
r199104
Dominators.h and Verifier.h moved from the Analysis directory to the IR directory.
r199082
The DAGCombiner learned to reassociate (i.e. change the order of) vector operations
r199135
dllexport and dllimport are no longer represented as linkage types
r199218
Parsing of the .symver directive in ARM assembly was fixed
r199339
Clang commits
The MS ABI is now used for Win32 targets by default
r199131
The MicrosoftMode language option was renamed to MSVCCompat and its role clarified (see the commit message for a description of MicrosoftExt vs MSVCCompat).
r199209
The
-cxx-abi
command-line flag was killed and is instead inferred depending on the target.
r199250
The analyzer learned that shifting a constant value by its bit width is undefined.
r199405
The
nonnull
attribute can now be applied to parameters directly.
r199467
Support for AArch64 on NetBSD was added to the compiler driver.
r199124
Other project commits
AddressSanitizer in compiler-rt gained the ability to start in 'deactivated' mode. It can later be activated when
__asan_init
is called in an instrumented library.
r199377
A number of patches were committed to lld for better MIPS support.
r199231
and many more.
lldb recognises Linux distribution in the vendor portion of the host triple. e.g.
x86_64-ubuntu-linux-gnu
.
r199510
