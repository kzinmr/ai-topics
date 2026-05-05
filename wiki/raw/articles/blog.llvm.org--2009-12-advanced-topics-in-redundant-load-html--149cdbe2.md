---
title: "Advanced Topics in Redundant Load Elimination with a Focus on PHI Translation"
url: "https://blog.llvm.org/2009/12/advanced-topics-in-redundant-load.html"
fetched_at: 2026-05-05T07:01:44.357737+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# Advanced Topics in Redundant Load Elimination with a Focus on PHI Translation

Source: https://blog.llvm.org/2009/12/advanced-topics-in-redundant-load.html

Advanced Topics in Redundant Load Elimination with a Focus on PHI Translation
In our
previous post on GVN
we introduced some basics of load elimination.  This post describes some advanced topics and focuses on PHI translation: what it is, why it is important, shows some nice things it can do, and describes the implementation in LLVM.
What is PHI Translation All About?
When performing redundancy elimination on SSA form, PHI translation is required when we are walking through the CFG and the value being analyzed has an operand defined in the block we're walking through.  In the case of load elimination, the operand of the value being analyzed is the pointer we're loading from. This means that PHI translation happens when the pointer we're loading is defined in a block. For example, consider this C code:
if (...) {
*A = 5;
P = A;
} else {
*B = 9;
P = B;
}
use(*P);
This compiles into LLVM IR that looks like this:
BB1:
store i32 5, i32* %A
br label %Merge
BB2:
store i32 9, i32* %B
br label %Merge
Merge:
%P = phi i32* [%A, %BB1], [%B, %BB2]
%Y = load i32 *%P
...
... use %Y ...
In this example, GVN starts looking at the %Y load to see if it can eliminate it.  It scans backwards up the block, looking for other things that provide the value of the memory address at %P.  Unlike in the example in the previous post, here we actually find a definition of %P: what do we do?
In LLVM 2.6 and before, memory dependence analysis would just give up and act as though the memory had been clobbered, preventing the load from being analyzed further (and eventually being eliminated in this case).  New in LLVM 2.7, GVN is able to translate %P into each predecessor.  In this case, it sees that %P has the value of %A in %BB1 (and then sees that %A is available there) and that %P has the value of %B in %BB2 (where it is also available). This allows GVN to optimize this example into:
BB1:
store i32 5, i32* %A
br label %Merge
BB2:
store i32 9, i32* %B
br label %Merge
Merge:
%Y = phi i32 [5, %BB1], [9, %BB2]
%P = phi i32* [%A, %BB1], [%B, %BB2]
...
... use %Y ...
which eliminates the load. This post talks about how this is done, the nuances involved in getting this right, and what this allows us to optimize.
Why is PHI Translation Required for Correctness?
One thing that wasn't obvious to me when I dove into this is that PHI translation is actually required for correctness.  This is the reason why memory dependence analysis must stop scanning if it finds the definition of the pointer.  The cases where this happen are somewhat subtle and usually involve partial redundancy elimination.  For example, consider this loop:
Loop:
%P = phi i32* [%A, %Entry], [%B, %Loop]
%X = load i32* %P
...
store i32 5, i32* %B
store i32 4, i32* %P
br i1 %cond, label %Loop, label %Out
Consider what would happen if PHI translation kept scanning for %P in predecessors as it went up the CFG: it would scan from the %X load up to the top of the Loop block. If not doing PHI translation correctly, it would continue scanning for %P in the Entry block (which we ignore in this example), then scan for %P in the Loop block (which is a predecessor of itself).
Scanning for %P in the loop block finds the store of 4 to %P, so we'd consider 4 to be a live-in value on the edge from loop. However, this is
incorrect
and will lead to a miscompilation: the actual value live on that backedge is 5, which is provided by the previous store.
This simple example is intended to show that PHI translation is not an optimization: it is required for correctness, and that the most simple form of PHI translation is to give up when you see a definition of the address. However, LLVM recently got smart enough to do much better than this or the simple pointer case above.
A More Interesting Case
Consider this test case:
struct S { int X, Y; };
int foo(struct S *P1, struct S *P2, int C) {
struct S *P;
if (C) {
P1->X = 4;
P1->Y = 2;
P = P1;
} else {
P2->X = 24;
P2->Y = 2;
P = P2;
}
return P->X + P->Y;
}
This code compiles down to IR that looks like this (using "
clang t.c -S -o - -emit-llvm | opt -mem2reg -S
":
if.then:
%tmp2 = getelementptr inbounds %struct.S* %P1, i32 0, i32 0
store i32 4, i32* %tmp2
%tmp4 = getelementptr inbounds %struct.S* %P1, i32 0, i32 1
store i32 2, i32* %tmp4
br label %if.end
if.else:
%tmp7 = getelementptr inbounds %struct.S* %P2, i32 0, i32 0
store i32 24, i32* %tmp7
%tmp9 = getelementptr inbounds %struct.S* %P2, i32 0, i32 1
store i32 2, i32* %tmp9
br label %if.end
if.end:
%P = phi %struct.S* [ %P1, %if.then ], [ %P2, %if.else ]
%tmp12 = getelementptr inbounds %struct.S* %P, i32 0, i32 0
%tmp13 = load i32* %tmp12
%tmp15 = getelementptr inbounds %struct.S* %P, i32 0, i32 1
%tmp16 = load i32* %tmp15
%add = add nsw i32 %tmp13, %tmp16
ret i32 %add
}
In this case, GVN looks to eliminate the %tmp13 and %tmp14 loads.  Consider the %tmp13 load: it scans backwards from the load, looking for available values of %tmp12.  As it goes, it immediately finds the definition of the pointer (%tmp12), so it needs to PHI translate the pointer or give up.  Without getting into the details yet of how this is done, here is the intuition of what happens:
In this case, the pointer is not a PHI node, but it
uses
a PHI node as an operand.  Because of this, GVN needs to phi translate the entire symbolic expression "gep P, 0, 0" into the predecessors.  It does this, forming the symbolic expression "gep P1, 0, 0" and it finds that the phi translated address is available as %tmp2 in the %if.then block.  It then PHI translates the "gep P, 0, 0" expression into the %if.else forming the "gep P2, 0, 0" symbolic expression and finds that it is available as %tmp7.  It scans those blocks for the pointers and finds that the values are, in fact, available.  Because they are both available, it can use insert construct SSA form to eliminate the load.
This allows it to see the both loads are in fact available in the predecessors.  Here is the code after GVN (using "
clang t.c -S -o - -emit-llvm | opt -mem2reg -S -gvn -die
):
if.then:
%tmp2 = getelementptr inbounds %struct.S* %P1, i32 0, i32 0
store i32 4, i32* %tmp2
%tmp4 = getelementptr inbounds %struct.S* %P1, i32 0, i32 1
store i32 2, i32* %tmp4
br label %if.end
if.else:
%tmp7 = getelementptr inbounds %struct.S* %P2, i32 0, i32 0
store i32 24, i32* %tmp7
%tmp9 = getelementptr inbounds %struct.S* %P2, i32 0, i32 1
store i32 2, i32* %tmp9
br label %if.end
if.end:
%tmp13 = phi i32 [ 1, %if.then ], [ 2, %if.else ]
%tmp16 = phi i32 [ 3, %if.then ], [ 4, %if.else ]
%add = add nsw i32 %tmp13, %tmp16
ret i32 %add
}
Here you can see that GVN found the available values, inserted PHI nodes, and eliminated the loads.
More Complex Address Expressions
While the example above hopefully makes intuitive sense, it turns out that PHI translating expressions like this is actually a bit more difficult than it looks. It was so much so that it got split out into its own class,
PHITransAddr
(in
llvm/Analysis/PHITransAddr.h
). Doing this was actually motivated by a few cute little examples like this:
void test(int N, double* G) {
for (long j = 1; j < 1000; j++)
G[j] = G[j] + G[j-1];
}
This example (which was reduced from a larger example) has a loop carried redundancy where every iteration reads the previous iteration's value. In fact, the code could be rewritten like this, which only has one load in the loop:
void test(int N, double* G) {
double Prev = G[0];
for (long j = 1; j < 1000; j++) {
Prev = G[j] + Prev;
G[j] = Prev;
}
}
Some compilers have specific optimization passes that identify and eliminate these recurrences through dependence analysis. While this is a nice thing to do, sufficiently smart partial redundancy elimination of loads should also be able to eliminate this, and LLVM now does.
The unoptimized code looks like this in LLVM IR:
define void @test(i32 %N, double* %G) {
bb.nph:
br label %for.body
for.body:
%indvar = phi i64 [ 0, %bb.nph ], [ %tmp, %for.body ] ;
indvar = [0 ... 999]
%arrayidx6 = getelementptr double* %G, i64 %indvar
%tmp = add i64 %indvar, 1
%arrayidx = getelementptr double* %G, i64 %tmp
%tmp3 = load double* %arrayidx                  ;
load G[indvar+1]
%tmp7 = load double* %arrayidx6                 ;
load G[indvar]
%add = fadd double %tmp3, %tmp7
store double %add, double* %arrayidx            ;
store G[indvar+1]
%exitcond = icmp eq i64 %tmp, 999
br i1 %exitcond, label %for.end, label %for.body
for.end:
ret void
}
One interesting thing to be aware of here is that the -indvars
pass rewrote the induction variable to count from 0 to 999 instead of from 1 to 1000.  This is just a canonicalization, but it is why we see a store to indvar+1 instead of directly through indvar.
In order to eliminate the redundant "
load G[indvar]
", GVN starts by looking for the dependencies of the %tmp7 load.  It scans up the block, over several instructions that obviously don't modify the memory value, until it gets to the %arrayidx6 instruction, which defines the value.  At this point it has to either stop phi translation (correct, but not very aggressive) or incorporate it into the scan and start looking for "gep %G, %indvar".  It does this, until the next instruction, which defines %indvar.  Since it found a definition of one of the inputs, it either has to phi translate (again, correct, not not very aggressive) or try to incorporate the value.
In this case, PHITransAddr attempts to translate the "gep %G, %indvar" symbolic expression across the PHI for each predecessor.  In the %for.body predecessor, it looks to see if there is an instruction that produces the value "gep %G, %tmp" (because %tmp is the value of the PHI in the %for.body predecessor), and finds that this expression exists as %arrayidx.  Since PHI translation succeeded, it scans from the bottom of the block to see if there is a definition of the value at the address %arrayidx, and finds that the %tmp3 load produces the desired value.
In the other predecessor (%bb.nph), PHITransAddr translates the symbolic "gep %G, %indvar" expression into "gep %G, 0" (which it uses InstSimplify to simplify down to "%G") and then checks to see if it is available as an address.  "%G" is in fact a value address, so it scans from the bottom of the %bb.nph block to see if the value at address %G is available.  In this case it isn't, so it records that the value is not available in the entry block, and that the phi translated address in that block is %G.
At this point, the recursive walk of the CFG has completed, and GVN knows that the %tmp7 load is in fact available as the %tmp3 value in one predecessor, but it is not available in the other predecessor.  This is a classic case of a partial redundancy.  Since the value is redundant on one edge but not the other, GVN makes the value fully redundant by inserting the computation (a load of %G) into the %bb.nph block, constructs SSA and eliminates the original load.
The final LLVM IR we get is:
define void @test(i32 %N, double* %G) {
bb.nph:
%tmp7.pre = load double* %G                     ;
Inserted by PRE
br label %for.body
for.body:
%tmp7 = phi double [ %tmp7.pre, %bb.nph ],
[ %add, %for.body ]          ;
SSA Construction
%indvar = phi i64 [ 0, %bb.nph ], [ %tmp, %for.body ]
%arrayidx6 = getelementptr double* %G, i64 %indvar
%tmp = add i64 %indvar, 1
%arrayidx = getelementptr double* %G, i64 %tmp
%tmp3 = load double* %arrayidx
%add = fadd double %tmp3, %tmp7      ;
Now uses the PHI instead of a load
store double %add, double* %arrayidx
%exitcond = icmp eq i64 %tmp, 999
br i1 %exitcond, label %for.end, label %for.body
for.end:
ret void
}
Through this, GVN and PHI translation have worked together to eliminate a load in the loop.  If you're more comfortable reading X86 machine code, here is the before and after code for the loop:
Before:
LBB1_1:
movsd 8(%rsi,%rax,8), %xmm0   # Load
addsd (%rsi,%rax,8), %xmm0    # Load
movsd %xmm0, 8(%rsi,%rax,8)   # Store
incq %rax
cmpq $999, %rax
jne LBB1_1
After:
LBB1_1:
addsd 8(%rsi,%rcx,8), %xmm0   # Load
movsd %xmm0, 8(%rsi,%rcx,8)   # Store
incq %rax
incq %rcx
cmpq $999, %rcx
jne LBB1_1
If you're interested in other examples of PHI translation, take a look at test/Transforms/GVN/rle-phi-translate.ll and test/Transforms/GVN/rle.ll in the LLVM distribution.
Division of Labor
Getting this to work requires a number of different LLVM subsystems to work together.  Here are the major players:
PHI Translation
The
PHITransAddr
class is the one that is responsible for building and translating symbolic expression like "gep %P, 1, (add %i, 1))" through PHI nodes.  When the "instruction scan" finds a definition of an input to the current PHITransAddr expression, it either has to incorporate it into a (potentially larger and more complex) expression or give up.  If it gives up, then PHI translation fails, otherwise it can keep scanning.
Memory Dependence Analysis
"MemDep" is the pass that does the CFG and instruction scanning.  It builds a lazy and cached representation that is morally similar to "Virtual SSA Form" used by some other compilers, but is significantly more efficient than the virtual SSA forms that I'm aware of.
It exposes two major interfaces:
1) "give me all the local dependences of this load".  This query scans the block the load lives in for dependent instructions. If it does not find a dependent instruction it returns "nonlocal" to indicate that the loaded memory value is potentially live-in to the block.
2) "give me all the non-local dependences for a load that is live in to a block". This query does the recursive upwards CFG scan that does PHI translation to find other definitions of the value.
In the interesting cases for PHI translation, we end up doing a non-local query and get back a set of blocks where the value is available along with a set of blocks where the value isn't available.
Alias Analysis:
Alias analysis
(in this case, the -basicaa pass) is the underlying analysis that tells us whether two pointers can point to the same memory location or whether an instruction can modify or read from a memory location.  This is required to allow MemDep to scan beyond stores and calls that do not clobber the address we're interested in.
SSA Update:
The
SSAUpdater
class is used to insert PHI nodes based on the set of loads that we find are available.
GVN
:
The GVN pass is the transformation sitting on top of all of these subsystems.  Because it is based on these other facilities, its logic is relatively simple: First, do a non-local memdep query.  If it returns a set of definitions with no clobbers, then the load is fully redundant and can be eliminated.  Otherwise, if there are some definitions live in, we have a partially redundant case.  GVN handles inserting the new computation to make the value fully redundant.
Limitations
While there is a lot of power here, there are still some significant limitations to this system.  As of this writing, here are some of the most significant ones:
First, an symbolic expression address must exist as an SSA value for PHI translation to succeed.  In the last example, if we tried to phi translate "gep %G, %indvar" into a predecessor value which formed the symbolic expression of "gep %G, %xxx" and that symbolic expression did not actually exist in the code, PHI translation would fail.  This happens because because after PHI translation occurs, we need MemDep to scan the block to find dependent instructions.  Since MemDep queries are based on pointer values expressed as LLVM 'Value*'s, we have to have one to do the query.
Second, critical edges currently block PRE of loads because we do not want to introduce the load on a control flow path where it would not exist before.  In principle, we could do this by lazily splitting the edge, but this would require updating the other in-flight data structures that the GVN pass is maintaining and we don't do this yet.
Finally, our PRE of loads can certainly be improved.  Currently we only do PRE in cases where it would not grow the code and not introduce a computation on a path where it wouldn't exist before.  Since we are deleting a load, this means that we only want to insert at most one load.  The heuristic we use to determine whether this is the case is currently very local and can be improved.
In any case, I hope this gives an useful overview of how this subsystem in LLVM works, and how it got better in what will be LLVM 2.7.
-Chris
