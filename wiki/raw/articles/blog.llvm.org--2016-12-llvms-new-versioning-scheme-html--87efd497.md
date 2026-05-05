---
title: "LLVM's New Versioning Scheme"
url: "https://blog.llvm.org/2016/12/llvms-new-versioning-scheme.html"
fetched_at: 2026-05-05T07:01:38.472468+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM's New Versioning Scheme

Source: https://blog.llvm.org/2016/12/llvms-new-versioning-scheme.html

LLVM's New Versioning Scheme
By Hans Wennborg
Dec 14, 2016
#release
3 minute read
Historically, LLVM's major releases always added "0.1" to the version number, producing major versions like 3.8, 3.9, and 4.0 (expected by March 2017). With our next release though, we're changing this.  The LLVM version number will now increase by "1.0" with every major release, which means that the first major release after LLVM 4.0 will be LLVM 5.0 (expected September 2017).
We believe that this approach will provide a simpler and more standard approach to versioning.
LLVM’s version number (also shared by many of its sub-projects, such as Clang, LLD, etc.) consists of three parts:
major
.
minor
.
patch
. The community produces a new release every six months, with "patch" releases (also known as "dot" or "stable" releases) containing bug fixes in between.
Until now, the six-monthly releases would cause the
minor
component of the version to be incremented. Every five years, after
minor
reached 9, a more major release would occur, including some breaking changes:
2.0
introduced the bitcode format,
3.0
a
type system rewrite
.
During
the discussions
about what to call the release after 3.9, it was pointed out that since our releases are time-based rather than feature-based, the distinction between major and minor releases seems arbitrary. Further, every release is also API breaking, so by the principles of
semantic versioning
, we should be incrementing the major version number.
We decided that going forward,
every release on the six-month cycle will be a major release
. Patch releases will increment the
patch
component as before (producing versions like 5.0.1), and the
minor
component will stay at zero since no minor releases will be made.
Bitcode Compatibility
Before LLVM 4.0.0, the
Developer Policy
specified that bitcode produced by LLVM would be readable by the next versions up to and including the next major release. The new version of the Developer Policy instead specifies that LLVM will currently load any bitcode produced by version 3.0 or later. When developers decide to drop support for some old bitcode feature, the policy will be updated.
API Compatibility
Nothing has changed. As before, patch releases are API and ABI compatible with the main releases, and the C API is "
best effort
" for stability, but besides that, LLVM’s API changes between releases.
What About the Minor Version?
Since the
minor
version is expected to always be zero, why not drop it and just use
major
.
patch
as the version number?
Dropping the minor component from the middle of the version string would introduce ambiguity: whether to interpret
x
.
y
as
major
.
minor
or
major
.
patch
would then depend on the value of
x
.
The version numbers are also exposed through various APIs, such as LLVM's
llvm-config.h
and Clang's
__clang_minor__
preprocessor macro. Removing the
minor
component from these APIs would break a lot of existing code.
Going forward, since the
minor
number will be zero and patch releases are compatible, I expect we will generally refer to versions simply by their
major
number and treat the rest of the version string as details (just as Chromium 55 might really be 55.0.2883.76). Future versions of LLVM and Clang can generally be referred to simply as "LLVM 4" or "Clang 5".
