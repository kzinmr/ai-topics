---
title: "LLVM Weekly - #44, Nov 3rd 2014"
url: "https://blog.llvm.org/2014/11/llvm-weekly-44-nov-3rd-2014.html"
fetched_at: 2026-05-05T07:01:41.396222+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #44, Nov 3rd 2014

Source: https://blog.llvm.org/2014/11/llvm-weekly-44-nov-3rd-2014.html

LLVM Weekly - #44, Nov 3rd 2014
Welcome to the forty-fourth issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
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
The
2014 LLVM Dev meeting
was held last week. I couldn't make it, but it seems like there was a great selection of talks. Sadly the keynote about Swift's high-level IR
was cancelled
. No word yet on when we can expect slides and videos online. However, slides by Philip Reames and Sanjoy Das from their talk on on implementing fully relocating garbage collection in LLVM
are online
.
Peter Zotov
has been doing lots of work on the LLVM OCaml bindings recently, and is looking for additional help. Recently, he's closed almost all open bugs for the bindings, migrated them to ocamlfind, fixed
Lllvm_executionengine
, and ensured pretty much the whole LLM-C API is exposed. Tasks on the todo list include writing tests in OUnit2 format, migrating the Kaleidoscope tutorial off camlp4, and splitting up and adding OCaml bindings to
this patch
. More ambitiously, it would be interesting to writing LLVM passes in OCaml and to represent LLVM IR as pure AST. If any of this interests you, do get in touch with Peter. He's able to review any patches, but could do with help on working through this list of new features.
The LLVM Bay Area monthly social is
going to be held on 6th November
.
On the mailing lists
Reid Kleckner has
proposed dropping support for running LLVM on Windows XP
. This would allow the use of system APIs only available in Vista and above. Thus far all responses have been positive, with one even suggesting raising the minimum to Windows 7.
Tom Stellard suggests
deprecating the autoconf build system
. Right now there is both an autotools based system and a CMake system, though CMake seems most used by developers for LLVM at least. Bob Wilson
points out
that the effort required to keep the existing makefiles working is much less than what might be needed to update the CMake build to support all uses cases. Though other replies make it seems that the CMake build supports pretty much all configurations people use now. If there are people who actually enjoy fiddling with build systems (far-fetched, I know), it seems like a little effort could go a long way and allow the makefile system to be jettisoned.
Betul Buyukkurt has posted an
RFC on indirect call target profiling
. The goal is to use the collected data for optimisation. Kostya Serebryany
described how it can be used to provide feedback to fuzzers
and detailed properties that would be useful for this usecase.
Chris Matthews
announces
that a new Jenkins-based OSX build cluster is up and running. This includes multiple build profiles and an O3 LTO performance tracker. The Jenkins config should be committed to zorg soon.
LLVM commits
Support for writing sampling profiles has been committed. In the future, support to read (and maybe write) profiles in GCC's gcov format will be added, and llvm-profdata will get support to manipulate sampling profiles.
r220915
.
A comment has been added to X86AsmInstrumentation to describe how asm instrumentation works.
r220670
.
The Microsoft vectorcall calling convention has been implemented for x86 and x86-64.
r220745
.
The C (and OCaml) APIs gained functions to query and modify branches, and to obtain the values for floating point constants. There have been a whole bunch of additional commits related to the OCaml bindings, too many to pick out anything representative.
r220814
,
r220815
,
r220817
,
r220818
.
The loop and SLP (superword level parallelism) vectorizers are now enabled in the Gold plugin.
r220886
,
r220887
.
Clang commits
A refactoring of libTooling to reduce required dependencies means that clang-format's binary is now roughly half the size.
r220867
.
Other project commits
