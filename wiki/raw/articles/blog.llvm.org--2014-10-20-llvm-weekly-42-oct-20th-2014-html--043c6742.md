---
title: "LLVM Weekly - #42, Oct 20th 2014"
url: "https://blog.llvm.org/2014-10-20-llvm-weekly-42-oct-20th-2014.html"
fetched_at: 2026-05-05T07:01:41.429079+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #42, Oct 20th 2014

Source: https://blog.llvm.org/2014-10-20-llvm-weekly-42-oct-20th-2014.html

LLVM Weekly - #42, Oct 20th 2014
Welcome to the forty-second issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
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
If you're local to London, you may be interested to know that I'll be talking about
lowRISC
at the
Open Source Hardware User Group on Thursday
.
The canonical home for this issue
can be found here at llvmweekly.org
.
News and articles from around the web
ELLCC, the LLVM-based cross-compilation toolchain
now has pre-built binaries for all LLVM tools
.
Eli Bendersky's repository of examples for using LLVM and Clang as libraries and for building new passes aren't new, but they are incredibly useful for newcomers to LLVM/Clang and I haven't featured them before. If you want to build something using LLVM or Clang, the
llvm-clang-samples repos
is one of the best places to start.
On the mailing lists
LLVM commits
Go LLVM bindings have been committed.
r219976
.
Invoking patchpoint intrinsics is now supported.
r220055
.
LLVM gained a workaround for a Cortex-A53 erratum.
r219603
.
Basic support for ARM Cortex-A17 was added.
r219606
.
The C API has been extended with the LLVMWriteBitcodeToMemoryBuffer function.
r219643
.
NumOperands has been moved from User to Value. On 64-bit host architectures this reduces
sizeof(User)
and subclasses by 8.
r219845
.
The LLVMParseCommandLineOptions was added to the C API.
r219975
.
Clang commits
Constant expressions can now be used in pragma loop hints.
r219589
.
The libclang API gained a function to retrieve the storage class of a declaration.
r219809
.
With the
-fsanitize-address-field-padding
flag, Clang can insert poisoned paddings between fields in C++ classes to allow AddressSanitizer to find intra-object overflow bugs.
r219961
.
Other project commits
lldb now supports a gdb-style batch mode.
r219654
.
