---
title: "LLVM Weekly - #88, Sep 7th 2015"
url: "https://blog.llvm.org/2015/09/llvm-weekly-88-sep-7th-2015.html"
fetched_at: 2026-05-05T07:01:40.097557+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #88, Sep 7th 2015

Source: https://blog.llvm.org/2015/09/llvm-weekly-88-sep-7th-2015.html

LLVM Weekly - #88, Sep 7th 2015
Welcome to the eighty-eighth issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
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
The biggest news from the past week is of course the
release of LLVM and Clang 3.7
. See the
LLVM release notes
and the
Clang release notes
for more details.
Slides from the 2015 GNU Tools Cauldron are
now available online
.
Version 1.12 of TCE, the TTA-based co-design environment
has been released
.
On the mailing lists
LLVM commits
The LLVM plugin for the gold linker now supports parallel LTO code generation.
r246584
.
The 'unpredictable' metadata annotation is now supported. This can be used to signal that a branch or switch is unpredictable.
r246888
.
A tool built on libFuzzer to fuzz llvm-as has been added.
r246458
.
The FunctionAttrs pass learned to infer nonnull attributes on returns.
r246476
.
Work on Windows exception handling continues with the addition of the cleanupendpad instruction and the llvm.eh.exceptionpointer intrinsic.
r246751
,
r246752
.
Clang commits
Basic support for the WebAssembly target landed in Clang. Basic codegen is supported, but not yet assembling or linking.
r246814
.
Clang will now warn when you reference object members from a handler of a constructor/destructor function-try-block.
r246548
.
Clang learnt the
__builtin_unpredictable
builtin, which will generate the newly added unpredictable metadata.
r246699
.
Other project commits
