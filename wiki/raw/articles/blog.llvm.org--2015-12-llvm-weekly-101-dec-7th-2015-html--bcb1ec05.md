---
title: "LLVM Weekly - #101, Dec 7th 2015"
url: "https://blog.llvm.org/2015/12/llvm-weekly-101-dec-7th-2015.html"
fetched_at: 2026-05-05T07:01:39.693906+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #101, Dec 7th 2015

Source: https://blog.llvm.org/2015/12/llvm-weekly-101-dec-7th-2015.html

LLVM Weekly - #101, Dec 7th 2015
Welcome to the one hundred and first issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
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
The implementation of the Swift programming language is
now open source
. Rather than being a simple code dump, development will now occur out in the open with
external contributions encouraged
. If you haven't already, now might be a good time to watch Joseph Groff and Chris Lattner's
talk on the Swift Intermediate Language
.
Rui Ueyama
wrote about the new LLD ELF linker
on the official LLVM blog.
The Visual C++ team have released
Clang with Microsoft CodeGen
. This uses the Clang parser along with the code generator and optimizer from Visual C++. The majority of the Clang and LLVM changes will be contributed back upstream.
Alex Denisov wrote about
using the LLVM API with Swift
.
If you haven't already submitted your talk proposal for the LLVM devroom at FOSDEM, you've now got a little more time.
Get your submission in by this Friday
.
On the mailing lists
LLVM commits
llc and opt gained an option to run all passes twice. This is intended to help show up bugs that occur when using the same pass manager to compile multiple modules.
r254774
.
An initial prototype for llvm-dwp has been committed. This will eventually be a tool for building a DWARF package file out of a number of .dwo split debug files.
r254355
.
All weight-based interfaces in MachineBasicBlock have now been replaced with probability-based interfaces.
r254377
.
LLVM's STLExtras gained a range-based version of
std::any_of
and
std::find
.
r254391
,
r254390
.
llvm.get.dynamic.area.offset.{i32,264}
intrinsics have been added. These can be used to get the address of the most recent dynamic alloca.
r254404
.
The X86 backend gained a new pass to reduce code size by removing redundant address recalculations for LEA.
r254712
.
The WebAssembly backend now has initial support for varargs.
r254799
.
Clang commits
Design docs have been added for forward-edge CFI for indirect calls.
r254464
.
The
pass_object_size
attribute was added to Clang. This intended to be used to work around cases where
__builtin_object_size
doesn't function.
r254554
.
Documentation was added for UndefinedBehaviorSanitizer.
r254733
.
Other project commits
