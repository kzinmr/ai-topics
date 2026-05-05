---
title: "The LLVM Project Blog"
url: "https://blog.llvm.org/2019/03/llvm-numerics-blog.html"
fetched_at: 2026-05-05T07:01:37.844768+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# The LLVM Project Blog

Source: https://blog.llvm.org/2019/03/llvm-numerics-blog.html

LLVM Numerics Blog
By Michael Berg
Mar 15, 2019
#numerics
8 minute read
Keywords: Numerics, Clang, LLVM-IR, : 2019 LLVM Developers' Meeting, LLVMDevMtg.
The goal of this blog post is to start a discussion about numerics in LLVM – where we are, recent work and things that remain to be done.  There will be an informal discussion on numerics at the 2019 EuroLLVM conference next month. One purpose of this blog post is to refresh everyone's memory on where we are on the topic of numerics to restart the discussion.
In the last year or two there has been a push to allow fine-grained decisions on which optimizations are legitimate for any given piece of IR.  In earlier days there were two main modes of operation: fast-math and precise-math.  When operating under the rules of precise-math, defined by IEEE-754, a significant number of potential optimizations on sequences of arithmetic instructions are not allowed because they could lead to violations of the standard.
For example:
The Reassociation optimization pass is generally not allowed under precise code generation as it can change the order of operations altering the creation of NaN and Inf values propagated at the expression level as well as altering precision.
Precise code generation is often overly restrictive, so an alternative fast-math mode is commonly used where all possible optimizations are allowed, acknowledging that this impacts the precision of results and possibly IEEE compliant behavior as well.  In LLVM, this can be enabled by setting the unsafe-math flag at the module level, or passing the -funsafe-math-optimizations to clang which then sets flags on the IR it generates.  Within this context the compiler often generates shorter sequences of instructions to compute results, and depending on the context this may be acceptable.  Fast-math is often used in computations where loss of precision is acceptable.  For example when computing the color of a pixel, even relatively low precision is likely to far exceed the perception abilities of the eye, making shorter instruction sequences an attractive trade-off.  In long-running simulations of physical events however loss of precision can mean that the simulation drifts from reality making the trade-off unacceptable.
Several years ago LLVM IR instructions gained the ability of being annotated with flags that can drive optimizations with more granularity than an all-or-nothing decision at the module level.
The IR flags in question are:
nnan, ninf, nsz, arcp, contract, afn, reassoc, nsw, nuw, exact
.
Their exact meaning is described in the
LLVM Language Reference Manual
.   When all the flags are are
enabled
, we get the current fast-math behavior.  When these flags are
disabled
, we get precise math behavior.  There are also several options available between these two models that may be attractive to some applications.  In the past year several members of the LLVM community worked on making IR optimizations passes aware of these flags.  When the unsafe-math module flag is not set these optimization passes will work by examining individual flags, allowing fine-grained selection of the optimizations that can be enabled on specific instruction sequences.  This allows vendors/implementors to mix fast and precise computations in the same module, aggressively optimizing some instruction sequences but not others.
We now have good coverage of IR passes in the LLVM codebase, in particular in the following areas:
* Intrinsic and libcall management
* Instruction Combining and Simplification
* Instruction definition
* SDNode definition
* GlobalIsel Combining and code generation
* Selection DAG code generation
* DAG Combining
* Machine Instruction definition
* IR Builders (SDNode, Instruction, MachineInstr)
* CSE tracking
* Reassociation
* Bitcode
There are still some areas that need to be reworked for modularity, including vendor specific back-end passes.
The following are some of the contributions mentioned above from the last 2 years of open source development:
Commit: e0ab896a84be9e7beb59874b30f3ac51ba14d025 : [InstCombine] allow more fmul folds with ‘reassoc'
Commit: 3e5c120fbac7bdd4b0ff0a3252344ce66d5633f9 : [InstCombine] distribute fmul over fadd/fsub
While multiple people have been working on finer-grained control over fast-math optimizations and other relaxed numerics modes, there has also been some initial progress on adding support for
more
constrained numerics models. There has been considerable progress towards adding and enabling constrained floating-point intrinsics to capture FENV_ACCESS ON and similar semantic models.
These experimental constrained intrinsics prohibit certain transforms that are not safe if the default floating-point environment is not in effect. Historically, LLVM has in practice basically “split the difference” with regard to such transforms; they haven’t been explicitly disallowed, as LLVM doesn’t model the floating-point environment, but they have been disabled when they caused trouble for tests or software projects. The absence of a formal model for licensing these transforms constrains our ability to enable them. Bringing language and backend support for constrained intrinsics across the finish line will allow us to include transforms that we disable as a matter of practicality today, and allow us to give developers an easy escape valve (in the form of FENV_ACCESS ON and similar language controls) when they need more precise control, rather than an ad-hoc set of flags to pass to the driver.
We should discuss these new intrinsics to make sure that they can capture the right models for all the languages that LLVM supports.
Here are some possible discussion items:
Should specialization be applied at the call level for edges in a call graph where the caller has special context to extend into the callee wrt to flags?
Should the inliner apply something similar to calls that meet inlining criteria?
What other part(s) of the compiler could make use of IR flags that are currently not covered?
What work needs to be done regarding code debt wrt current areas of implementation.
