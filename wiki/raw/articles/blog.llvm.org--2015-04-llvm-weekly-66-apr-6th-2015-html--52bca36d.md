---
title: "LLVM Weekly - #66, Apr 6th 2015"
url: "https://blog.llvm.org/2015/04/llvm-weekly-66-apr-6th-2015.html"
fetched_at: 2026-05-05T07:01:40.767561+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #66, Apr 6th 2015

Source: https://blog.llvm.org/2015/04/llvm-weekly-66-apr-6th-2015.html

LLVM Weekly - #66, Apr 6th 2015
Welcome to the sixty-sixth issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
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
color_coded
, a vim plugin for syntax highlighting using libclang is
now available
.
Ravi, a dialect of Lua with JIT compilation via LLVM has
has its first alpha release
. The status of JIT compilation can be seen
here
.
On the mailing lists
LLVM commits
API migration has started for GEP constant factories. For now, nullptr can be passed for the pointee type, but you'll need to pass the type explicitly to be future-proof.
r233938
.
A proof of concept fuzzer based on DataFlowSanitizer has been added, as well as support for token-based fuzzing.
r233613
,
r233745
.
DebugLoc's API has been rewritten.
r233573
.
The SystemZ backend now supports transactional execution on the zEC12.
r233803
.
Clang commits
Clang gained a toolchain driver for targeting NaCl.
r233594
.
The size of various Stmt subclasses has been optimised on 64-bit targets.
r233921
.
Codegen was added for the OpenMP atomic update construct.
r233513
.
Other project commits
LLDB system initialization has been reworked.
r233758
.
