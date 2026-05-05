---
title: "LLVM Weekly - #130, Jun 27th 2016"
url: "https://blog.llvm.org/2016/06/llvm-weekly-130-jun-27th-2016.html"
fetched_at: 2026-05-05T07:01:38.571634+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #130, Jun 27th 2016

Source: https://blog.llvm.org/2016/06/llvm-weekly-130-jun-27th-2016.html

LLVM Weekly - #130, Jun 27th 2016
Welcome to the one hundred and thirtieth issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
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
If you're reading this on blog.llvm.org then do note this is LAST TIME it will be cross-posted there directly. There is a great effort underway to increase the content on the LLVM blog, and unfortunately LLVM Weekly has the effect of drowning out this content. As ever, you can head to
http://llvmweekly.org
, subscribe to get it by email, or subscribe to the
RSS feed
.
The canonical home for this issue
can be found here at llvmweekly.org
.
News and articles from around the web
After recently being taken down due to excessive resource usage, the
LLVM apt repositories are now back
.
A detailed
introduction to ThinLTO
has been published on the LLVM blog. This covers the background, design, current status, and usage information for ThinLTO.
A post on Reddit gives a summary of
notable language features voted into the C++17 working draft at the Oulu meeting
.
On the mailing lists
LLVM commits
The new representation for control-flow integrity and virtual call metadata has landed. The commit message further details the problems this change addresses.
r273729
.
The
llvm.type.checked.load
intrinsic was added. It loads a function pointer from a virtual table pointer using type metadata.
r273576
.
As part of the work on CFL-AA, interprocedural function summaries were added. These avoid recomputation for many properties of a function.
r273219
,
r273596
.
MemorySSA gained new APIs for PHI creation and MemoryAccess creation.
r273295
.
Metadata attachments are now allowed for declarations.
r273336
.
A new runtimes directory was added to the LLVM tree.
r273620
.
LLVM's dynamic loader gained basic support for COFF ARM.
r273682
.
Clang commits
constexpr if
support has been added to Clang.
r273602
.
clang-tidy has a new
modernize-use-emplace
check that will replace calls of
push_back
to
emplace_back
.
r273275
.
The CMake build system for Clang gained a
ENABLE_X86_RELAX_RELOCATIONS
option.
r273224
.
Other project commits
Basic support for versioned symbols was added to LLD.
r273143
.
LLD now handles both single and double dashes for all options.
r273256
.
