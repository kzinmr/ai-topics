---
title: "LLVM Weekly - #80, Jul 13th 2015"
url: "https://blog.llvm.org/2015/07/llvm-weekly-80-jul-13th-2015.html"
fetched_at: 2026-05-05T07:01:40.359439+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #80, Jul 13th 2015

Source: https://blog.llvm.org/2015/07/llvm-weekly-80-jul-13th-2015.html

LLVM Weekly - #80, Jul 13th 2015
Welcome to the eightieth issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
Alex Bradbury
. Subscribe to future issues at
http://llvmweekly.org
and pass it on to anyone else you think may be interested. Please send any tips or feedback to
asb@asbradbury.org
, or
The canonical home for this issue
can be found here at llvmweekly.org
.
News and articles from around the web
The 2015 LLVM Developers' Meeting
has been announced
. It will take place on October the 29th and 30th in San Jose, California. Registration information and a call for papers will be sent out later in the month.
LLVM/Clang 3.6.2
has been tagged
. All being well, we can expect 3.6.2 to be released soon.
On the mailing lists
LLVM commits
The Hexagon backend gained a BitTracker class. This is intended to be target independent. As described at the top of BitTracker.cpp, this is intended to be used with a target-specific machine instruction evaluator. There have been some other large additions to the Hexagon backend this week too. I hope the authors will consider given another talk on their work at some point.
r241595
.
llc learnt the
run-pass
option, which will run one specific code generation pass only.
r241476
.
LLVM now has documentation on its inline assembly!
r241698
.
The llvm.frameescape and llvm.framerecover intrinsics have been renamed to localescape and localrecover.
r241463
.
Various refactoring commits have been made with the aim of having a single DataLayout used during compilation, owned by the module.
r241775
.
A new llvm.canonicalize intrinsics has been introduced, intended to be used to canonicalize floating point values.
r241977
.
The new argmemonly attribute can be used to mark functions that can only access memory through its argument pointers.
r241979
.
Clang commits
A few patches landed in Clang improving Objective-C support. This includes parsing, semantic analysis, and AST support for Objective-C type parameters, support for Objective-C type arguments, the
__kindof
type qualifier. Douglas Gregor has more to say about these changes
on the mailing list
.
r241541
,
r241542
,
r241548
, and more.
Clang will attached the readonly or readnone attributes when appropriate to inline assembly instructions, meaning the inline asm will not be treated as conservatively. e.g. in some cases an inline asm block could be hoisted out of a loop.
r241930
.
PCH (pre-compiled headers) are now wrapped in an object file.
r241690
,
r241620
.
Clang now recognises the GCC-compatible
-fprofile-generate
and
-fprofile-use
flags.
r241825
.
Other project commits
libcxx add
try_emplace
and
insert_or_assign
to
map
and
unordered_map
, as specified in
N4279
.
r241539
.
The new LLD COFF linker now has basic support for x86 (it was previously x86-64 only).
r241857
.
