---
title: "LLVM Weekly - #53, Jan 5th 2015"
url: "https://blog.llvm.org/2015/01/llvm-weekly-53-jan-5th-2015.html"
fetched_at: 2026-05-05T07:01:41.156633+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #53, Jan 5th 2015

Source: https://blog.llvm.org/2015/01/llvm-weekly-53-jan-5th-2015.html

LLVM Weekly - #53, Jan 5th 2015
Welcome to the fifty-third issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
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
I'm going to be in California next week for the
RISC-V workshop
. I'm arriving at SFO on Monday 12th and leaving on Sunday the 18th. Do let me know if you want to meet and talk
lowRISC
/RISC-V or LLVM, and we'll see what we can do.
The canonical home for this issue
can be found here at llvmweekly.org
.
News and articles from around the web
I was getting ready to break out gitstats for some analysis of the LLVM repo and I find to my delight that Phoronix has saved me the trouble and has
shared some stats on activity in the LLVM repo over the past year
.
Tom Stellard has made a blog post
announcing some recent RadeonSI performance improvements
on his LLVM development branch. This includes 60% improvement in one OpenCL benchmark and 10-25% in a range of other OpenCL tests.
Gaëtan Lehmann has written a blog post about
getting started with libclang using the Python bindings
.
The C++ Filesystem Technical Specification, based on the Boost.Filesystem library
has been approved
.
On the mailing lists
LLVM commits
Instruction selection for bit-permuting operations on PowerPC has been improved.
r225056
.
The scalar replacement of aggregates (SROA) pass has started to learn how to more intelligently handle split loads and stores. As explained in detail in the commit message, the old approach lead to complex IR that can be difficult for the optimizer to work with. SROA is now also more aggressive in its splitting of loads.
r225061
,
r225074
.
InstCombine will now try to transform
A-B < 0
in to
A < B
.
r225034
.
The Hexagon (a Qualcomm DSP) backend has seen quite a lot of work recently. Interested parties are best of flicking through the commit log of lib/Target/Hexagon.
r225005
,
r225006
, etc.
Clang commits
Other project commits
