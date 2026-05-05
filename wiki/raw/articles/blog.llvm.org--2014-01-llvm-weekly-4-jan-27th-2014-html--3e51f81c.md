---
title: "LLVM Weekly - #4, Jan 27th 2014"
url: "https://blog.llvm.org/2014/01/llvm-weekly-4-jan-27th-2014.html"
fetched_at: 2026-05-05T07:01:42.749930+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #4, Jan 27th 2014

Source: https://blog.llvm.org/2014/01/llvm-weekly-4-jan-27th-2014.html

LLVM Weekly - #4, Jan 27th 2014
Welcome to the fourth issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. This marks the end of the first month of operation, here's to many more! LLVM Weekly is brought to you by
Alex Bradbury
. Subscribe to future issues at
http://llvmweekly.org
and pass it on to anyone else you think may be interested. Please send any tips or feedback to
asb@asbradbury.org
, or
@llvmweekly
or
@asbradbury
on Twitter. I've been keeping the
@llvmweekly Twitter account
updated throughout the week, so follow that if you want more frequent news updates.
The canonical home for this issue
can be found here at llvmweekly.org
.
News and articles from around the web
The biggest compiler-related news this week has been the discussions on the GCC mailing list. Things kicked off with
Eric S. Raymond's post
suggesting that technical progress in GCC is being held back by concerns about reusing parts of GCC in a way that bypasses the copyleft license. Ian Lance Taylor
responded
to point out that GCC now has a plugin system, albeit with an unstable interface, which mostly put a stop to that line of discussion. However a
later post to the mailing list from Richard Stallman
has proved very controversial by claiming that "The existence of LLVM is a terrible setback for our community precisely because it is not copylefted and can be used as the basis for nonfree compilers". There's plenty of discussion of these comments around the web
at LWN
, Hacker News, Reddit, Slashdot etc. Although many of us may have a preference for non-copyleft ('permissive') free software licenses, RMS has consistently and over a long period of time argued that copyleft licenses ultimately do a better job of spreading free software and preserving its freedom. As such, it's not clear to me why this mailing list post has come as a surprise to many. I'm personally surprised he didn't bring up the fact that the BSD-style license used by LLVM contains no explicit patent grant (though LLVM does have a
patent policy
to help protect its users).
Rapidly moving away from controversial topics, an exciting milestone for the LLVM project was hit this week. The
200000th commit
has been applied. Takumi Nakamura was lucky enough to be the one to author that commit.
The Khronos group has
released the SPIR 1.2 specification
. SPIR is a standardised intermediate representation meant for use with OpenCL, and is based on LLVM 3.2 IR. With the release, the Khronos Group have open sourced a modified Clang 3.2 which can generate SPIR from OpenCL C programs as well as a module verifier.
Joaquín M López Muñoz has published a benchmark
comparing hash table performance on Clang
. He compares GCC's libstdc++-v3 to the LLVM project's libc++.
The Cambridge (UK) LLVM socials
are starting up again
, with the next one on the 29th Jan at 7.30pm. Sadly I can't make it, hopefully the next one!
On the mailing lists
LLVM commits
LoopSimplify is no longer a LoopPass, instead it is both a utility function and a FunctionPass. The motivation was to be able to compute function analysis passes after running LoopSimplify, but the change has a bunch of other advantages described in detail in the commit message.
r199884
. Additionally, the LCSSA (loop-closed SSA) pass was made a utility with a function pass and the LoopVectorizer became a FunctionPass.
r200067
,
r200074
.
The Constant Hoisting Pass was born.
r200022
.
InstCombine learned how to deal with vectors for most fmul/fvid/add/sub/mul/div combines.
r199598
,
r199602
.
Type-based alias analysis has, for the time being, been disabled when using alias analysis in CodeGen due to two shortcomings described in the commit message.
r200093
.
LTO gained new methods which allows the user to parse metadata nodes, extract linker options, and extract dependent libraries from a bitcode module.
r199759
.
The Sparc backend now supports the inline assembly constraint 'I'.
r199781
.
The x86 backend allows segment and address-size overrides for movs/lods/outs, fixing
bug 9385
.
r199803
and more.
llvm-ar no longer opens or fstats file twice.
r199815
.
When compiling a function with the minsize attribute, the ARM backend will now use literal pools even for normal i32 immediates.
r199891
.
There was a fair bit of activity on the R600 backend. I haven't had the time to properly summarise that activity or pick out the most important commits, so I recommend those interested take a look through the commit logs.
JIT is now supported for Sparc64.
r199977
.
llvm-readobj gained support for the PE32+ format (used for Windows 64-bit executables).
r200117
.
Clang commits
Registry::getCompletions was implemented. This returns a list of valid completions for a given context.
r199950
.
Clang gained basic support for the attribute
returns_nonnull
.
r199626
,
r199790
.
getResultType on function and method declarations was renamed to getReturnType which is a semantically more accurate name.
r200082
. Similarly, getResultLoc was renamed to getReturnLoc.
r200105
.
All applicable accessors in FunctionProtoType have been renamed from
*argument*
to
*parameter*
.
r199686
.
Clang was taught to look in its installation libdir for libraries such as libc++ when the installation is within the system root.
r199769
.
A module.map file is now required to load a module.
r199852
.
Other project commits
lldb learned the 'step-avoid-libraries' setting, which allows a user to list libraries to avoid.
r199943
.
In compiler-rt, support was added for intercepting and sanitizing arguments passed to printf functions in AddressSanitizer and ThreadSanitizer.
r199729
.
A fix was committed to ThreadSanitizer to prevent deadlocking after a fork.
r199993
.
Dragonegg can now be built with CMake.
r199994
.
Compiler-rt gained support in its udiv/umod implementations for ARMv4 which lacks bx and clz. Code changes also resulting in a 30%+ performance improvement on the Raspberry Pi (armv7, ARM1176) and 5-10% on a Cortex A9.
r200001
.
In AddressSanitizer on Android, all AddressSanitizer output is duplicated to the system log.
r199887
.
lld gained support for emitting a PE32+ file header.
r200128
.
lldb now supports Haswell on x86-64.
r199854
.
