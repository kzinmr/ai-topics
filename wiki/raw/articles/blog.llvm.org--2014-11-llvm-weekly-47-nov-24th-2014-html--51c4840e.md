---
title: "LLVM Weekly - #47, Nov 24th 2014"
url: "https://blog.llvm.org/2014/11/llvm-weekly-47-nov-24th-2014.html"
fetched_at: 2026-05-05T07:01:41.379905+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #47, Nov 24th 2014

Source: https://blog.llvm.org/2014/11/llvm-weekly-47-nov-24th-2014.html

LLVM Weekly - #47, Nov 24th 2014
Welcome to the forty-seventh issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
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
Version 3.0 of the Capstone disassembly framework
has been released
. Python bindings have been updated to support Python 3, and this release also adds support for Sparc, SystemZ and XCore. It also has performance improvements.
Herb Sutter has penned a
trip report
of the recent ISO C++ meeting.
Emscripten has
updated to use LLVM 3.4 from the PNaCl team
. There's more work to be done to rebase on top of 3.5.
Woboq has written a blog post
detailing C++14 features of interest to Qt programmers
, though I suspect the article has a wider potential audience than that. Recent Clang of course has
good support
for the new C++14 features.
There is going to be an LLVM Devroom at FOSDEM 2015, and the
submission deadline for presentations/talks/tutorials is on Dec 1st
.
Apple's LLVM Source Tools and Program Analysis teams are
looking for interns for Summer 2015
.
On the mailing lists
If you're wondering how the process of adding OpenMP support to Clang is going, the
answer
is that it's still ongoing and there's hope it will be done by the 3.6 release, depending on the speed of code reviews.
Siva Chandra kicked off a discussion on the mailing list about
how to better manage breakages caused by LLVM or Clang API changes
. Siva suggests LLDB should be developed against a known-good version of LLVM/Clang that gets periodically bumped. Vince Harron says that he is
looking to add a continuous build on curated versions of Clang/LLVM
in addition to a continuous build on top of tree for everything. This should help improve the signal to noise ratio and make it easier for LLDB developers to tell when a breaking change is due to their addition or a change elsewhere. Reid Kleckner
suggests lldb should be treated part of the same project as Clang/LLDB
and more pressure should be put on developers to fix breakages, presumably in the same way that API changes in LLVM almost always come with an associated patch to fix Clang.
Peter Collingbourne has proposed
adding the llgo frontend to the LLVM project
. Chris Lattner is
in favour of this
, but would like to see the GPLv3+runtime exception dependencies rewritten before being checked in. Some people in the thread expressed concern that the existing base of LLVM/Clang reviewers know C++ and may not be able to review patches in Go, though it looks like a non-zero of existing LLVM reviewers are appropriately multilingual.
Brett Simmers is working on HHVM and
is interested if there are ways to control where a BasicBlock ends up in memory
, with the motivation to make best of the instruction cache by keeping frequently executed pieces of code closer together. There's general agreement this would be a great feature to have, but it doesn't sound like this is easily supported in LLVM right now.
LLVM commits
A small doc fix has the honour of being
commit 222222
.
A nice little optimisation has been committed which replaces a switch table with a mul and add if there is a linear mapping between index and output.
r222121
.
The SeparateConstOffsetFromGEP, EarlyCSE, and LICM passes have been enabled on AArch64. This has
measurable gains for some SPEC benchmarks
.
r222331
.
The description of the noalias attribute has been clarified.
r222497
.
MDNode is being split into two classes, GenericMDNode and MDNodeFwdDecl.
r222205
.
The LLVM CMake-based build system learned to support
LLVM_USE_SANITIZER=Thread
.
r222258
.
The R600 backend gained the SIFoldOperands pass which attempts to fold source operands of mov and copy instructions into their uses.
r222581
.
Clang commits
Other project commits
LLDB can now perform basic debugging operations on Windows.
r222474
.
LLDB's line editing support was been completely rewritten.
r222163
.
MemorySanitizer gained support for MIPS64.
r222388
.
A sample tool was added to lldb to extract and dump unwind information from Darwin's compact unwind section.
r222127
.
