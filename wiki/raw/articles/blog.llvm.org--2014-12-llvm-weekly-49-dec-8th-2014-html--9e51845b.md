---
title: "LLVM Weekly - #49, Dec 8th 2014"
url: "https://blog.llvm.org/2014/12/llvm-weekly-49-dec-8th-2014.html"
fetched_at: 2026-05-05T07:01:41.232242+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #49, Dec 8th 2014

Source: https://blog.llvm.org/2014/12/llvm-weekly-49-dec-8th-2014.html

LLVM Weekly - #49, Dec 8th 2014
Welcome to the forty-ninth issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
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
Most of the 2014 LLVM Developers' Meeting videos and slides are
now online
. Sadly, there are no videos from the talks by Apple employees yet. Hopefully they'll be appearing later.
QuarksLab has a rather nice write-up of
deobfuscating an OLLVM-protected program
.
The LLVM-based ELLCC has been making progress on
ELK, a bare-metal POSIX-like environment
.
Support for statepoints landed in LLVM this week, and Philip Reames has a blog post detailing
some notes and caveats
. See also the mailing list discussion linked to below about future plans for GC in LLVM.
On the mailing lists
LLVM commits
The statepoint infrastructure for garbage collection has landed. See the final patch in the series for documentation.
r223078
,
r223085
,
r223137
,
r223143
.
The LLVM assembler gained support for ARM's funky modified-immediate assembly syntax.
r223113
.
The OCaml bindings now has a CMake buildsystem.
r223071
.
The PowerPC backend gained support for readcyclecounter on PPC32.
r223161
.
Support for 'prologue' metadata on functions has been added. This can be used for inserting arbitrary code at a function entrypoint. This was previously known as prefix data, and that term has been recycled to be used for inserting data just before the function entrypoint.
r223189
.
PowerPC gained a Power8 instruction schedule definition
r223257
.
Clang commits
LLVM IR for vtable addresses now uses the type of the field being pointed to, to enable more optimisations.
r223267
.
New attributes have been added to specify AMDGPU register limits. This is a performance hint that can be used to attempt to limit the number of used registers.
r223384
.
Clang gained the
__has_declspec_attribute
preprocessor macro.
r223467
.
__has_attribute
now only looks for GNU-style attributes. You should be able to use
__has_cpp_atribute
or
__has_declspec_attribute
instead.
r223468
.
Other project commits
DataFlowSanitizer is now supported for MIPS64.
r223517
.
libcxx now supported
std::random_device
on (P)NaCl.
r223068
.
An effort has started in lld to reduce abstraction around InputGraph, which has been found to get in the way of new features due to excessive information hiding.
r223330
. The commit has been temporarily reverted due to breakage on Darwin and ELF.
A large chunk of necessary code for Clang module support has been added to LLDB.
r223433
.
LLDB now has
documented coding conventions
.
r223543
.
