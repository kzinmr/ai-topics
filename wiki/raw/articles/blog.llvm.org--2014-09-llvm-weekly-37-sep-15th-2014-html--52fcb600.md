---
title: "LLVM Weekly - #37, Sep 15th 2014"
url: "https://blog.llvm.org/2014/09/llvm-weekly-37-sep-15th-2014.html"
fetched_at: 2026-05-05T07:01:41.942556+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #37, Sep 15th 2014

Source: https://blog.llvm.org/2014/09/llvm-weekly-37-sep-15th-2014.html

LLVM Weekly - #37, Sep 15th 2014
Welcome to the thirty-seventh issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
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
This week's issue comes to you from sunny Tenerife. Yes, my dedication to weekly LLVM updates is so great that I'm writing it on holiday. Enjoy! I'll also note that I'm at PyCon UK next week where I'll be
presenting
on the results of a project we had some interns working on over the summer creating a programming game for the Raspberry Pi.
The canonical home for this issue
can be found here at llvmweekly.org
.
News and articles from around the web
Not only does Pyston have a shiny new blog, they've also
released version 0.2
. Pyston is an implementation of Python using LLVM, led by Dropbox. This release supports a range of language features that weren't supported in 0.1, including support for the native C API. The plan is to focus on performance during the development cycle for 0.3.
Sylvestre Ledru has posted a
report of progress in building Debian with Clang
following the completion of this year's Google Summer of Code projects. Now with Clang 3.5.0 1261 packages fail to build with Clang. Sylvestre describes how they're attacking the problem from both sides, by submitting patches to upstream projects as well as to Clang where appropriate (e.g. to ignore some unsupported optimisation flags rather than erroring out).
On the mailing lists
Philip Reames has started a discussion on
adding optimisation hints for 'constant' loads
. A common case is where a field is initialised exactly once and then is never modified. If this invariant could be expressed, it could improve alias analysis as the AA pass would never consider that field to MayAlias with something else (Philip reports that the obvious approach of using type-based alias analysis isn't quite enough).
Hal Finkel has posted an
RFC on attaching attributes to values
. Currently, attributes such as noalias and nonnull can be attached to function parameters, but in cases such as C++11 lambdas these can be packed up into a structure and the attributes are lost. Some followup discussion focused on whether these could be represented as metadata. The problem there of course is that metadata is intended to be droppable (i.e. is semantically unimportant). I very much like the
suggestion
from Philip Reames that the test suite should run with a pass that forcibly drops metadata to verify it truly is safe to drop.
Robin Morisset has posted a
proposal on implementing a fence elimination algorithm
. The proposed algorithm is based on partial redundancy elimination. He's looking for feedback on the suggested implementation approach.
There's been a little bit of discussion on the topic of
rekindling work on VMKit
.
LLVM commits
The start of the llvm.assume infrastructure has been committed, as well as an AlignmentFromAssumptions pass. See
the original RFC
for a refresher on the llvm.assume intrinsic.
r217342
,
r217344
.
LLVM's sample profile reader has been refactored into lib/ProfileData.
r217437
.
The AMD 16H Jaguar microarchitecture now has a scheduling model.
r217457
.
The 'bigobj' COFF variant can now be read.
r217496
.
Clang commits
Other project commits
LLD gained support for AArch64 Mach-O.
r217469
.
