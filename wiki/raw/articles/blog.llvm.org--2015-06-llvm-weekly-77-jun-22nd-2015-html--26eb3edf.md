---
title: "LLVM Weekly - #77, Jun 22nd 2015"
url: "https://blog.llvm.org/2015/06/llvm-weekly-77-jun-22nd-2015.html"
fetched_at: 2026-05-05T07:01:40.398595+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #77, Jun 22nd 2015

Source: https://blog.llvm.org/2015/06/llvm-weekly-77-jun-22nd-2015.html

LLVM Weekly - #77, Jun 22nd 2015
Welcome to the seventy-seventh issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
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
I'll be in California next week for the
second RISC-V workshop
. Me and my colleague Wei will both be giving talks about recent
lowRISC
progress. Say hi if you're going to be there. I might have some spare time towards the end of the week too if anyone wants to meet up.
The canonical home for this issue
can be found here at llvmweekly.org
.
News and articles from around the web
WebAssembly
has been announced. It is a new collaboration between browser vendors to define a new binary executable format that can be used as a compilation target. A good summary is available
here on the emscripten mailing list
.
Tilmann Scheller has written up a
pair
of
blog posts about improving build times of Clang. He steps through a wide range of generic approaches (using Ninja, ccache, the gold linker, LTO+PGO in the host compiler etc etc) and some specific to Clang/LLVM.
The
Cambridge LLVM Social
will be taking place on Wed 24th June, 7.30pm at the Blue.
On the mailing lists
LLVM commits
Some initial support for 'fault maps' and a
FAULTING_LOAD_OP
, intended for use in a managed language runtime, has been added. The new ImplicitNullChecks pass will fold null checks into nearby memory operations.
r239740
,
r239743
.
The
SafeStack
pass to protect against stack-based memory corruption errors has been added.
r239761
.
All temporary symbols are now unnamed. This saves a small amount of memory.
r240130
.
There's been some enhancement to the heuristics for switch lowering.
r240224
.
Clang commits
The
-fsanitize-trap=
flag has been introduced, which will be used to control if the given sanitizer traps upon detecting an error.
r240105
.
Appropriate bitsets for use by LLVM's control flow integrity implementation can now be emitted for the Microsoft ABI.
r240117
.
Kernel AddressSanitizer now has basic support.
r240131
.
Clang learned to recognise type nullability specifiers.
r240146
.
Other project commits
