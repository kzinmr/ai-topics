---
title: "LLVM Weekly - #104, Dec 28th 2015"
url: "https://blog.llvm.org/2015/12/llvm-weekly-104-dec-28th-2015.html"
fetched_at: 2026-05-05T07:01:39.528403+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #104, Dec 28th 2015

Source: https://blog.llvm.org/2015/12/llvm-weekly-104-dec-28th-2015.html

LLVM Weekly - #104, Dec 28th 2015
Welcome to the one hundred and fourth issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
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
schedule for the LLVM devroom at FOSDEM
has been published. This will be on January 30th 2016 in Brussels at
FOSDEM
.
Andy Finnell spent some time over the Christmas vacation porting the LLVM Kaleidoscope tutorial to Erlang and has kindly
shared the fruits of his labours
.
Richard Pennington has written another blog post about ELLCC, this time about
using it to cross-compile the Linux kernel for the Raspberry Pi
.
Tim Jones (lecturer at the University of Cambridge Computer Laboratory) has written about the
alias analysis used in the HELIX compiler
. There's nothing LLVM-specific here, indeed it was implemented using ILDJIT but should be of general interest to compiler developers.
On the mailing lists
LLVM commits
An initial implementation of an LLVMCodeView library has landed. This implements support for emitting debug info in the CodeView format.
r256385
.
lit has gained support for a per-test timeout which can be set using
--timeout=
.
r256471
.
All uses of edge wights in BranchProbabilityInfo have been replaced with probabilities.
r256263
.
The LLVM project documentation on patch reviews via Phabricator now has advice on choosing reviewers.
r256265
.
The gc.statepoint intrinsic's return type is now a token type rather than i32.
r256443
.
Clang commits
ASTtemplateKWAndArgsInfo and ASTTemplateArgumentListInfo have been converted to use the TrailingObjects header. This abstracts away
reinterpret_cast
, pointer arithmetic, and size calculations needed for the case where a class has some other objects appended to the end of it.
r256359
.
Other project commits
Development of LLD's new ELF linker is continuing, with support for new relocations on x86, x86-64, and MIPS.
r256143
,
r256144
,
r256172
,
r256416
.
