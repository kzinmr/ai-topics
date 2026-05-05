---
title: "LLVM Weekly - #108, Jan 25th 2016"
url: "https://blog.llvm.org/2016/01/llvm-weekly-108-jan-25th-2016.html"
fetched_at: 2026-05-05T07:01:39.381388+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #108, Jan 25th 2016

Source: https://blog.llvm.org/2016/01/llvm-weekly-108-jan-25th-2016.html

LLVM Weekly - #108, Jan 25th 2016
Welcome to the one hundred and eighth issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
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
LLVM 3.8 RC1
has been released
. Now is the time to test it out with your favourite projects and report any issues.
The deadline for the
EuroLLVM call for papers
is today.
Version 1.6 of the Rust programming language
was released
las week. Rust uses LLVM for its code generation.
The LLVM Social in Paris
will be held this week
on Wednesday.
On the mailing lists
LLVM commits
llvm::SplitModule
gained a new flag which can be used to cause it to attempt to split the module without globalizing local objects.
r258083
.
The WebAssembly backend will now rematerialize constants with multiple uses rather than holding them live in registers, as there is no code size saving in using registers in for constants in most cases in the WebAssembly encoding.
r258142
.
Some small patches from the global instruction selection effort have started to land, such as the introduction of a generic machine opcode for ADD (
G_ADD
) and the all-important CMake support for building it.
r258333
,
r258344
.
getCacheLineSize
was added to TargetTransformInfo. It's currently only used by PPCLoopDataPrefetch.
r258419
.
LoopIdiomRecognize improved in its ability to recognise memsets.
r258620
.
Clang commits
A number of new AST matchers were added.
r258042
,
r258072
, and more.
The LeakSanitizer documentation has been updated with a usage example.
r258476
.
Other project commits
The new ELF linker gained initial support for MIPS local GOT (global offset table) entries.
r2583888
.
The LLVM test suite now contains a ClangAnalyzer subdirectory containing tests for the static analyzer.
r258336
.
