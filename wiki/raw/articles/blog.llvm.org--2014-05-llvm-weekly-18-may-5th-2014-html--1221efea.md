---
title: "LLVM Weekly - #18, May 5th 2014"
url: "https://blog.llvm.org/2014/05/llvm-weekly-18-may-5th-2014.html"
fetched_at: 2026-05-05T07:01:42.308553+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #18, May 5th 2014

Source: https://blog.llvm.org/2014/05/llvm-weekly-18-may-5th-2014.html

LLVM Weekly - #18, May 5th 2014
Welcome to the eighteenth issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
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
I'm going to be in the San Francisco area May 13th-20th with some other Raspberry Pi people. We'll be at Maker Faire Bay Area on the 17th and 18th. Let me know if there's anything else I should check out while over there.
The canonical home for this issue
can be found here at llvmweekly.org
.
News and articles from around the web
Andrew Ruef has written a blog post about
using static analysis and Clang to find the SSL heartbleed bug
. The code for the checker described in the blog post is
available on Github
.
The FTL ('Fourth tier LLVM') Javascript JIT is
now enabled in WebKit for Mac
. The WebKit Wiki has
more information
. I haven't seen any public benchmark figures. Please do share if you have any.
Eli Bendersky has written an article about
how to use libTooling to implement source to source transformations
.
The next
Paris LLVM Social
will take place on May 5th (i.e. this evening).
The LLVM Bay Area social
will take place on May 8th
. Please RSVP if you are interested.
On the mailing lists
LLVM commits
The patch to
perform common subexpression elimination for a group of getelementptrs
that was discussed a couple of weeks ago has been merged. It is currently only enabled for the NVPTX backend.
r207783
.
X86 code generation has been implemented for the musttail function attribute.
r207598
.
Pass run listeners were added to the pass manager. This adds C/C++ APIs to enable fine-grain progress report and safe suspension points. See the commit message for more info
r207430
.
The optimisation remark system has started to be used, with calls to emitOptimizationRemark added to the loop unroller and vectorizer.
r207528
,
r207574
.
The SLPVectorizer gained the ability to recognize and vectorize intrinsic math functions.
r207901
.
Clang commits
NRVO (named return value optimisation) determination was rewritten. According to the commit message, "a variable now has NRVO applied if and only if every return statement in that scope returns that variable." Also, NRVO is performed roughly 7% more often in a bootstrap clang build.
r207890
.
libclang's documentation comment API has been split in to a separate header.
r207392
.
The SLPVectorizer (superword-level parallelism) is now disabled at O0, O1 and Oz.
r207433
. It was later re-enabled at Oz.
r207858
.
The libclang API now supports attributes 'pure', 'const', and 'noduplicate'.
r207767
.
The comment parser no longer attempts to validate HTML attributes (the previous solution was insufficient).
r207712
.
Other project commits
