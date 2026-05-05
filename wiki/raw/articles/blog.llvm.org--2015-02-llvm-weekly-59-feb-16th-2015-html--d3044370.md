---
title: "LLVM Weekly - #59, Feb 16th 2015"
url: "https://blog.llvm.org/2015/02/llvm-weekly-59-feb-16th-2015.html"
fetched_at: 2026-05-05T07:01:40.963939+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #59, Feb 16th 2015

Source: https://blog.llvm.org/2015/02/llvm-weekly-59-feb-16th-2015.html

LLVM Weekly - #59, Feb 16th 2015
Welcome to the fifty-ninth issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
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
Reminder, the EuroLLVM 2015 call for papers submission deadline is
TODAY
. See
here
for details.
LLVM and Clang 3.6-rc3
has been tagged
, any help with testing is greatly appreciated.
On the mailing lists
LLVM commits
The biggest chunk of internal refactoring of debug metadata has landed, with the addition of specialized debug info metadata nodes.
r228640
.
New intrinsics llvm.eh.begincatch and llvm.eh.endcatch intrinsics have been added to support Windows exception handling.
r228733
.
A DebugInfoPDB implementation using the MS Debug Interface Access SDK has landed.
r228747
.
SimplifyCFG will now use TargetTransformInfo for cost analysis.
r228826
.
A profitability heuristic has been added for the x86 mov-to-push optimisation.
r228915
.
PassManager.h is now LegacyPassManager.h. As described in the commit message, if you are an out of tree LLVM user you may need to update your includes.
r229094
.
Clang commits
Other project commits
C++14's sized deallocation functions have been implemented in libcxx.
r229281
.
lld learnt to handle the
--wrap
option.
r228906
.
lldb gained the concept of "runtime support values".
r228791
.
The remote-android platform has been added to lldb.
r228943
.
