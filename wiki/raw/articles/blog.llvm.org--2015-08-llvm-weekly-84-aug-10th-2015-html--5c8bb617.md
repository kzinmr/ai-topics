---
title: "LLVM Weekly - #84, Aug 10th 2015"
url: "https://blog.llvm.org/2015/08/llvm-weekly-84-aug-10th-2015.html"
fetched_at: 2026-05-05T07:01:40.203152+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #84, Aug 10th 2015

Source: https://blog.llvm.org/2015/08/llvm-weekly-84-aug-10th-2015.html

LLVM Weekly - #84, Aug 10th 2015
Welcome to the eighty-fourth issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
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
Adrian Sampson has written a fantastic
introduction to LLVM
. It's titled LLVM for Grad Students, but it should be useful for anybody looking to use LLVM or just wanting to understand it better.
Brandon Holt has written up a short and helpful post giving
hints and tips on debugging LLVM
.
The move of the mailing lists from UIUC on to lists.llvm.org is now complete. All public LLVM-related mailing lists
are shown here
. List addresses have now changed to listname@lists.llvm.org.
There's been some exciting activity in the world of GCC. Support for the draft C++ Concepts TS
has been committed
. A draft of the technical specification is
available here
. Additionally, Nick Clifton has posted a useful summary of
GNU toolchain developments for July/August
.
On the mailing lists
LLVM commits
A handy new LLVM Support header was introduced. The TrailingObjects template class abstracts away
reinterpret_cast
, pointer arithmetic, and size calculation needed for the case where a class has some other objects appended to the end of it.
r244164
.
Initial documentation for the Machine IR serialization format has been written.
r244292
.
Uniquable DICompilerUnits have been disallowed. Old bitcode will be automatically upgraded and the sed script in the commit message should be useful for updating out-of-tree testcases.
r243885
.
All of the TargetTransformInfo cost APIs now use int rather than unsigned.
r244080
.
Clang commits
A new checker for code-level localizability issues on OSX/iOS was born. It will warn about the use of non-localized NSStrings passed to UI methods and about failing to include a comment in NSLocalizedString macros.
r244389
.
New AST matchers have been introduced for constructors that are default, copy, or move.
r244036
.
Other project commits
The old COFF linker in LLD has been removed in favour of the new, faster, and simpler implementation.
r244226
.
ThreadSanitizer is now enabled for AArch64.
r244055
.
