---
title: "LLVM Weekly - #52, Dec 29th 2014"
url: "https://blog.llvm.org/2014/12/llvm-weekly-52-dec-29th-2014.html"
fetched_at: 2026-05-05T07:01:41.168211+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #52, Dec 29th 2014

Source: https://blog.llvm.org/2014/12/llvm-weekly-52-dec-29th-2014.html

LLVM Weekly - #52, Dec 29th 2014
Welcome to the fifty-second issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
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
This issue marks the end of one full year of LLVM Weekly. It's a little shorter than usual as the frenetic pace of LLVM/Clang development has slowed over the holiday period. Surprising even to me is that we managed to make it full all 52 weeks with an issue every Monday as promised. This requires a non-trivial amount of time each week (2-3+ hours), but I am intending to keep it going into 2015. I'd like to give a big thank you to everyone who's said hi at a conference, sent in corrections or tips on content, or just sent a random thank you. It's been very helpful in motivation. I don't currently intend to change anything about the structure or content of each issue for next year, but if you have any ideas then please let me know.
I can't make it to 31C3 due to the awkward timing of the event, but do let me know if there are any LLVM/Clang related talks worth sharing. There was a
talk about Code Pointer Integrity
which has previously been covered in LLVM Weekly and is working towards upstreaming. The video is
here
. If you're interested in
lowRISC
and at 31C3, Bunnie is leading a
discussion about it
at 2pm on Monday (today).
The canonical home for this issue
can be found here at llvmweekly.org
.
News and articles from around the web
There doesn't seem to have been any LLVM or Clang related news over the past week. Everyone seems to be busy with non-LLVM related activities over the christmas break. If you're looking for a job though, Codeplay tell me they have two vancancies: one for a
debugger engineer
and another for a
compiler engineer
.
On the mailing lists
David Li has shared some
early info on Google's plans for LTO
. He describes the concept of 'peak optimization performance' and some of the objectives of the new design. This includes the ability to handle programs 10x or 100x the size of Firefox. We can expect more information in 2015, maybe as early as January.
The discussion on possible approaches to reducing the size of libLLVM has continued. Chris Bieneman has
shared some more size stats
. These gains come from removing unused intrinsics. Chandler Carruth has followed up with a pleasingly thought-provoking argument on a different approach:
target-specific intrinsics shouldn't exist in the LLVM front or middle-end
. He describes the obvious issues with this, with the most fiddly probably being instruction selection converting appropriate IR to the right target-specific functionality.
LLVM commits
The SROA (scalar replacement of aggregates) pass has seen some refactoring to, in the future, allow for more intelligent rewriting.
r224742
,
r224798
.
The masked load and store intrinsics have been documented.
r224832
.
CodeGenPrepare learned to speculate calls to llvm.cttz/ctlz (count trailing/leading zeroes) if
isCheapToSpeculateCtlz/isCheapToSpeculatCttz
in TargetLowering return true.
r224899
.
Clang commits
The Clang internals manual has been extended with stub sections on Parse, Sema, and CodeGen.
r224894
.
Other project commits
The libcxx LIT test-suite has seen a number of new configuration options. Even better, these are
now documented
.
r224728
.
