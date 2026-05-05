---
title: "LLVM Weekly - #115, Mar 14th 2016"
url: "https://blog.llvm.org/2016/03/llvm-weekly-115-mar-14th-2016.html"
fetched_at: 2026-05-05T07:01:39.502504+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #115, Mar 14th 2016

Source: https://blog.llvm.org/2016/03/llvm-weekly-115-mar-14th-2016.html

LLVM Weekly - #115, Mar 14th 2016
Welcome to the one hundred and fifteenth issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
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
We have an LLVM-related research position currently being
advertised here at the University of Cambridge Computer Lab
. If you'd like an informal chat about what it's like working in this group or on this project please don't hesitate to get in touch with me.
News and articles from around the web
LLVM and Clang 3.8 have now been released. Check out the
LLVM
and
Clang
release notes for a run-down of the new features.
It's GDC this week and if you're attending you may be interested that there's an
LLVM meetup scheduled for Thursday
.
Felix Angell has a detailed blog post introducing
generating LLVM IR from Go
.
On the mailing lists
LLVM commits
Loop invariant code motion learnt the ability the exploit the fact a memory location is known to be thread-local.
r263072
.
A new
llvm.experimental.deoptimize
intrinsic has been added.
r26328
.
A ThinLTOCodeGenerator was added in order to provide a proof-of-concept implementation.
r262977
.
The Sparc backend gained support for co-processor condition branching and conditional traps.
r263044
.
Clang commits
Clang gained support for the
[[nodiscard]]
attribute.
r262872
.
New AST matchers were added for addrLabelExpr, atomicExpr, binaryCondtionalOperator, designatedINitExpr, designatedInitExpr, designatorCountIs, hasSyntacticForm, implicitValueINitExpr, labelDecl, opaqueValueExpr, parenListExpr, predefinedExpr, requiresZeroInitialization, and stmtExpr.
r263027
.
Other project commits
