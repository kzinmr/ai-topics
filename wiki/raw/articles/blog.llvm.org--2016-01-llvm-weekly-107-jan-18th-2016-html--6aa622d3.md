---
title: "LLVM Weekly - #107, Jan 18th 2016"
url: "https://blog.llvm.org/2016/01/llvm-weekly-107-jan-18th-2016.html"
fetched_at: 2026-05-05T07:01:39.426289+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #107, Jan 18th 2016

Source: https://blog.llvm.org/2016/01/llvm-weekly-107-jan-18th-2016.html

LLVM Weekly - #107, Jan 18th 2016
Welcome to the one hundred and seventh issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
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
I have a very exciting piece of non-LLVM news to share this week. On Saturday I proposed to my partner Carrie Anne, and I'm delighted to report that
she said yes
. You may well question if this piece of personal news has any relevance to you, and in response I'd like to highlight just how important Carrie Anne is to this weekly newsletter. For over two years now, I've given up 2-3+ hours of my time every week without fail on evenings and weekends, time we could really be spending together as a couple. Without Carrie Anne's understanding and support LLVM Weekly couldn't exist. 2016 is going to be a very exciting year.
News and articles from around the web
Registration is
now open
for EuroLLVM 2016. The conference will be held in Barcelona on March 17th-18th. The call for papers closes on January 25th.
Registration is
open
for the Clang/LLVM development sprint to be held on the weekend of Feb 6th/7th at Bloomberg's London and New York offices.
The next Cambridge LLVM social will be held
on Wednesday 20th January at 7.30pm
, and will be colocated with the FreeBSD social.
On the mailing lists
LLVM commits
The ORC JIT API now supports remote JITing over an RPC interface to a separate process. The LLI tool has been updated to use this interface.
r257305
,
r257343
.
The Hexagon backend gained a target-independent SSA-based data flow framework for representing data flow between physical registers and passes using this to implement register liveness analysis, dead code elimination, and copy propagation.
r257447
,
r257480
,
r257485
,
r257490
.
The documentation on committing code reviewed on Phabricator to trunk has been improved.
r257764
.
WebAssembly gained a prototype instruction encoder and disassembler based on a temporary binary format.
r257440
.
LLVM's MathExtras gained a SaturatingMultiplyAdd helper.
r257352
.
llvm-readobj has much-expanded support for dumping CodeView debug info.
r257658
.
The code that finds code sequences implementing bswap or bitreverse and emits the appropriate intrinsic has been rewritten.
r257875
.
The AMDGPU backend gained a new machine scheduler for the Southern Islands architecture.
r257609
.
Clang commits
A Python implementation of scan-build has been added.
r257533
.
The 'interrupt' attribute is now supported on x86.
r257867
.
Clang learned to respond to the
-fsanitize-stats
flag. It can currently only be used with control-flow integrity and allows statistics to be dumped.
r257971
.
Other project commits
The compiler-rt CMake buildsystem gained experimental support for tvOS and watchOS.
r257544
.
Initial support was added for PPC and the new ELF linker.
r257374
.
The CMake and Lit runners in the LLVM test-suite can now support the integer C and C++ tests from SPEC CPU2006.
r257370
.
