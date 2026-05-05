---
title: "Introduction to load elimination in the GVN pass"
url: "https://blog.llvm.org/2009/12/introduction-to-load-elimination-in-gvn.html"
fetched_at: 2026-05-05T07:01:44.423464+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# Introduction to load elimination in the GVN pass

Source: https://blog.llvm.org/2009/12/introduction-to-load-elimination-in-gvn.html

Introduction to load elimination in the GVN pass
One very important optimization that the GVN pass (opt -gvn) does is load elimination. Load elimination involves several subsystems (including alias analysis, memory dependence analysis, SSA construction, PHI translation) and has many facets (full vs partial redundancy elimination, value coercion, handling memset/memcpy, etc).  In this post, I introduce and motivate the topic, which will let us expand on it in future posts.
Basic Redundant Load Elimination
GVN (which stands for "Global Value Numbering", though this detail has nothing to do with load elimination) is responsible for the form of load elimination known as
redundant
load elimination.  This is the elimination of loads whose values are already available (other forms of load elimination includes deletion of
dead
loads).  A simple example of a redundant load is:
%x = load i32* %P
%y = load i32* %P  ; <- Redundant
Clearly in this example, we can delete the second load and "replace all uses" of %y with %x, because the value at address %p is already available as the value "i32 %x". Another simple form of redundant elimination comes about from stores, as in:
store i32 4, i32* %P
%a = load i32* %P
In this example, we can replace %a with 4.  This sort of transformation generalizes to support other operations: the GVN pass can forward memsets to loads, memcpy from constant globals to loads, etc.  Note that GVN is not allowed to optimize away volatile loads.
The implementation of this is pretty straight-forward: GVN (through the memdep class) scans backwards from the load that we are trying to eliminate up through the block until it gets an instruction that provides the value (as in these examples) or until it finds an instruction that might affect the memory in an unknown way like a call.  If we find an instruction that potentially clobbers the memory location, we can't eliminate the load.
However, straight-line code is pretty boring, lets look at more complex examples.
SSA Construction in GVN
GVN can also eliminate non-local loads, which can require PHI node insertion.  Here's a simple example:
BB1:
store i32 5, i32* %P
br label %Merge
BB2:
%X = load i32* %P
... use %X ...
br label %Merge
Merge:
%Y = load i32 *%P
...
... use %Y ...
In this case, GVN scans for available values of %P within the block (starting at the %Y load), and runs into the top of the %Merge block.  Since it got to the top of the block, it starts scanning the predecessor blocks (%BB1 and %BB2) and it finds out that the value of the load is 5 in BB1 and %X in BB2.  GVN then renames these values with the SSAUpdater class, producing:
BB1:
store i32 5, i32* %P
br label %Merge
BB2:
%X = load i32* %P
... use %X ...
br label %Merge
Merge:
%Y = phi i32 [5, %BB1], [%X, %BB2]
...
... use %Y ...
Replacing a load with a PHI node may not seem like a win, however the cost model we use in the LLVM optimizer assumes that PHI nodes will be coalesced away by the code generator, and are thus free.  The logic that does PHI insertion is contained and maintained by the SSAUpdater class, which may be the subject of a future Blog post.
Pros and Cons of Redundant Load Elimination
We always consider it profitable to eliminate a load in the optimizer when possible. Loads can be quite expensive (e.g. if they miss in the cache), and load/store traffic can hide other redundant or further simplifyable logic from the scalar optimizer.  One idiom used to test alias analyses usually looks like this:
%A =
load i32* %P
store i32 1, i32* %Q
%B =
load i32* %P
%C = sub i32 %A, %B
ret i32 %C
If GVN + instcombine are able to turn this into "
ret i32 0
" then we know that alias analysis was able to prove that P and Q did not alias.  While somewhat unlikely in the real world, this is one example that shows a scalar optimization (X-X == 0) that can not be done unless the redundant loads are eliminated.
The cost of eliminating redundant loads is that it creates longer live ranges that the code generator may not be able to cope with.  This is a real issue that we don't currently have a good solution for.  The ultimate answer is that improved rematerialization will be able to rematerialize the load further down in the code to reduce register pressure, we don't have great support for this yet though.
