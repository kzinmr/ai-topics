---
title: "LLVM Weekly - #125, May 23rd 2016"
url: "https://blog.llvm.org/2016/05/llvm-weekly-125-may-23rd-2016.html"
fetched_at: 2026-05-05T07:01:38.791732+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #125, May 23rd 2016

Source: https://blog.llvm.org/2016/05/llvm-weekly-125-may-23rd-2016.html

LLVM Weekly - #125, May 23rd 2016
Welcome to the one hundred and twenty-fifth issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
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
Stephen Kelly has written a blog post about
using Clang through the cindex API to automatically generate Python bindings
. He also makes use of
SIP
.
Krister Walfridsson has written a wonderfully clear post on
C's type-based aliasing rules
.
This week I discovered the
Swift Weekly Brief newsletter
. Its author, Jesse Squires does a wonderful job of summarising mailing list traffic, recent commits, and discussions on swift-evolution proposals. If you have an interest in Swift development or language design in general I highly recommend it.
Are you interested in
writing for the LLVM blog
? Or volunteering to help recruit content authors? If so, get in touch with Tanya.
The next Cambridge LLVM Social will be held
at 7.30pm on May 25th at the Cambridge Blue
.
On the mailing lists
LLVM commits
llc will now report all errors in the input file rather than just exiting after the first.
r269655
.
The SPARC backend gained support for soft floating point.
r269892
.
Reloc::Default
no longer exists. Instead,
Optional<Reloc>
is used.
r269988
.
An initial implementation of a "guard widening" pass has been committed. This will combine multiple guards to reduce the number of checks at runtime.
r269997
.
Clang commits
clang-include-fixer gained a basic Vim integration.
r269927
.
The intrinsics headers now have feature guards enabled in Microsoft mode to combat the compile-time regression discussed last week due to their increased size.
r269675
.
avxintrin.h gained many new Doxygen comments.
r269718
.
Other project commits
lld now lets you specify a subset of passes to run in LTO.
r269605
.
LLDB has replaced uses of its own Mutex class with
std::mutex
.
r269877
,
r270024
.
