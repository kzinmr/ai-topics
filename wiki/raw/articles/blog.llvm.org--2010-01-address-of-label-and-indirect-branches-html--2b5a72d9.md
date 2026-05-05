---
title: "Address of Label and Indirect Branches in LLVM IR"
url: "https://blog.llvm.org/2010/01/address-of-label-and-indirect-branches.html"
fetched_at: 2026-05-05T07:01:44.344048+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# Address of Label and Indirect Branches in LLVM IR

Source: https://blog.llvm.org/2010/01/address-of-label-and-indirect-branches.html

Address of Label and Indirect Branches in LLVM IR
The GCC Compiler supports a useful "
Label as Values
" extension, which allows code to take the address of a label and then later do an unconditional branch to an address specified as a void*. This extension is particularly useful for building efficient interpreters.
LLVM has long supported this extension by lowering it to a "correct" but extremely inefficient form. New in LLVM 2.7 is IR support for taking the address of a label and jumping to it later, which allows implementing this extension much more efficiently. This post describes this new LLVM IR feature and how it works.
In this discussion, I limit the scope to only considering "local" jumps. We don't talk about non-local jumps in the GCC extension sense: jumps from a nested function to an outer one.
The Address of Label Extension
Before I dive into the new feature, I'll describe the GCC C extension along with how LLVM 2.6 and earlier used to compile it. Consider this code (from
PR3120
):
static int fn(Opcodes opcodes) {
static const void *codetable[] =
{ &&RETURN, &&INCREMENT, &&DECREMENT, &&DOUBLE, &&SWAPWORD };
int result = 0;
goto *codetable[*(opcodes++)];
RETURN:
return result;
INCREMENT:
result++;
goto *codetable[*(opcodes++)];
DECREMENT:
result--;
goto *codetable[*(opcodes++)];
DOUBLE:
result <<= 1;
goto *codetable[*(opcodes++)];
SWAPWORD:
result = (result << 16) | (result >> 16);
goto *codetable[*(opcodes++)];
}
As you can see, the code initializes the 'codetable' array with the addresses of 5 labels, and later jumps through a computed pointer.
An interesting aspect about this extension is that the only thing you are allowed to do with an address taken label is to jump to it. While it is widely misused for other things (e.g. the BUG macro in the linux kernel, which prints the address of a label on error), you are
really really
only allowed jump to it. You are not allowed to use it in an inline asm, inspect the value, or do anything else.
LLVM 2.6 and Earlier
In LLVM 2.6 and earlier, LLVM took full advantage of the fact that you're not allowed to do anything with the value other than jump to the address of a label. Because this extension is only used rarely, we did not want to add direct support for this extension, because it would increase the complexity of LLVM IR. Instead, we took a very simple implementation approach, which faithfully implemented the extension, but did not require any new IR features. The approach was simple:
When the address of a label was taken, that label was assigned a unique integer ID (within its function) starting at 1. Taking the address of the label provided this integer ID, and not the actual address of the label.
When an indirect goto is seen, we lowered this construct as a standard LLVM
switch instruction
. For each uniquely assigned integer ID, the switch would jump to the corresponding label.
The combination of these two elements meant that we could support this extension with no special support in LLVM IR. To give a more concrete example, this is how the example above was lowered. The "codetable" array was lowered as if it were written as:
static const void *codetable[] =
{ (void*)1, (void*)2, (void*)3, (void*)4, (void*)5 };
This clearly doesn't provide the addresses of the specified labels, but it does provide unique ID numbers for each. With this, an indirect goto was lowered as if it were written as:
switch (..) {
default: __builtin_unreachable();
case 1: goto RETURN;
case 2: goto INCREMENT;
case 3: goto DECREMENT:
case 4: goto DOUBLE;
case 5: goto SWAPWORD;
}
Since code is only allowed to jump to the address of a label taken in the current function (again, not considering non-local gotos), we know all possible destinations, and we can codegen the indirect jump as a switch. To reiterate, the primary advantage of this approach was that it did not require any LLVM extension: switch statements required the LLVM IR switch instruction, so reusing it here was no problem.
It is also worthwhile to point out that while this implementation fulfills the letter of the extension, it is fairly far from the intent of it. Beyond that, the major problem with the LLVM 2.6 implementation is that the generated code is quite slow.
LLVM 2.7 and Later: blockaddress and indirectbr
While it is true that this extension is relatively rare, the cases where it is used are quite important. This extension is used in critical interpreter loops, where it can provide a fairly substantial win (around 15% is typical). Because of this, LLVM grew the ability to represent and codegen this in the intended form. This extension uses two new LLVM IR features:
First, taking the address of a label produces a new
blockaddress
node (represented by the LLVM BlockAddress class).
Second, jumping through an address results in a new
indirectbr
terminator instruction (the IndirectBrInst class).
The two new features have a couple of interesting ramifications, but before we get into them, I'll show you how the example above compiles. First, the "codetable" array compiles into this pseudo IR:
static const void *codetable[] =
{ blockaddress(@fn, %RETURN),
blockaddress(@fn, %INCREMENT),
blockaddress(@fn, %DECREMENT),
blockaddress(@fn, %DOUBLE),
blockaddress(@fn, %SWAPWORD)
};
At codegen time, the new blockaddress constant actually lowered into a reference to the label for the LLVM BasicBlock that it correspond to. Next, instead of a switch, indirect gotos codegen into the new 'indirectbr' LLVM IR instruction like this:
indirectbr i8* %address, [ label %RETURN, label %DOUBLE, label %INCREMENT, label %DECREMENT, label %SWAPWORD ]
While the blockaddress constant is relatively straightforward, you might be surprised to see all of the labels duplicated here. The 'indirectbr' is typically lowered to very simple machine code: a machine level jump through a register. Despite this underlying simplicity, the invariant on the "indirectbr" instruction is that it must include (possibly a superset of) all possible label targets in the list of labels in the instruction. Jumping to a label that is not included is undefined behavior. The order of labels in the instruction doesn't matter, but the presence or absence of a label is important.
Ramifications of this design
When this feature was being added to LLVM, we considered many different approaches, which all had a variety of different tradeoffs. Instead of describing all possible implementation approaches, lets just talk about some of the ramifications of this approach by considering a set of questions you might have:
Why does indirectbr include a list of possible target blocks?
One of the foremost concerns we had when implementing this new feature was that we wanted it to fit into the rest of the compiler with as little special case code as possible. One particularly important structure is the Control Flow Graph (CFG), which is the basis for all dataflow analysis in LLVM.
In LLVM, the CFG is walked with the
pred_iterator and succ_iterator
iterators.
succ_iterator
is very simple, it just walks the BasicBlock operands of the
terminator instruction
at the end of a block.
pred_iterator
is trickier: it walks the use-def chains of a BasicBlock, and reports any uses coming from terminators as predecessors.
Clearly, for this extension to work with this scheme, we wanted to follow as closely as possible with the way the existing system works. This means that indirectbr having a list of possible targets makes the successor iterator very simple (it can just walk the list to get the possible destinations). A second major benefit is that this also fixes the predecessor iterator: since each operand is considered a 'use', walking the use list of a block that has its address taken will work correctly, because the indirectbr uses will be seen.
How does this extension interact with PHI nodes?
PHI nodes are defined based on properties of the CFG, so they work normally as you'd expect based on the CFG behavior described above. Taking the address of a block itself doesn't cause it to have any PHI nodes. An address-taken block gets PHI node entries when an indirectbr jumps to it.
Why is blockaddress a constant?
This is an easy one: the BlockAddress IR object inherits from Constant because it needs to be able to be used to initialize global variables. Global variable initializers must be Constant's.
Why does blockaddress take both a function and a basic block name?
There are a couple answers to this. The most obvious one is that LLVM IR is not nested like C code is. When the address of a label is used to initialize a static variable, that static variable becomes an LLVM global variable like any other. If there were a reference to "foo" from a global variable, we need to know
which
"foo" label is being referenced (since each function has its own local namespace).
A second and less obvious answer is that LLVM IR is more general than the GCC C extension: you are allowed to take the address of a block in a different function. This support falls out of the support we need to initialize global variables, and isn't obviously useful, but it is there nonetheless.
How does this extension interact with inlining?
Simply put, LLVM currently refuses to inline a function containing an indirectbr (as does GCC). It is conceivably possible to relax this restriction in the future in some cases, but it would require a lot of analysis. The basic problem is that inlining an indirectbr is actually a pretty tricky thing to do: in addition to cloning the callee into the caller, we have to clone all blockaddress objects referring to block in the caller, and clone everything that refers to them. Here's a silly example in pseudo IR:
static void *G = blockaddress(@foo, %bb);
void foo() {
goto *G;
bb:
return;
}
void bar() {
foo();
}
Simply cloning foo into bar like this would not be correct:
static void *G = blockaddress(@foo, %bb);
void foo() {
goto *G;
bb:  return;
}
void bar() {
goto *G;
bb:
return;
}
The problem is that 'bar' would jump through G to a label defined in 'foo'. It is not legal to jump from one function to another. To do this inlining, we'd actually have to clone G itself. Doing this is possible, but not worth it, particularly because most functions that use this extension are large interpreter loops.
How does this extension interact with critical edge splitting?
Poorly.
A critical edge in the CFG is an edge which comes from a block with multiple successors (e.g. a block that ends with a conditional branch) and goes to a block with multiple predecessors (like the merge point of an if/then/else). Critical edges are problematic for various code motion transformations. Prior to this extension, any critical edge in the CFG could be split by introducing a new intermediate block between the source and destination blocks.
My biggest disappointment with this extension (and the reason I resisted implementing it for so long) centers around the fact that it inherently makes some edges un-splittable. Consider a simple little CFG like this:
BB1:
indirectbr i8* %P1, [ label %A, label %B ]
BB2:
br label %A
A:
...
The edge "BB1->A" is critical because A has multiple predecessors (from both BB1 and BB2) and BB1 has multiple successors (to A and B). We could easily split the edge in this example by introducing a new intermediary block:
BB1:
indirectbr i8* %P1, [ label %A1, label %B ]
BB2:
br label %A
A1:
br label %A
A:
...
This is the normal critical-edge splitting transformation. Here we can see that the edge from BB1->A1 is not critical (because A1 has one predecessor) and the edge from A1->A is not critical either (because A1 has one predecessor). The problem with this is that we just broke an important invariant: since we didn't adjust places that took the address of A, we now have a situation where the CFG looks like BB1 jumps to A1 - but in reality, the pointer that the indirectbr gets will contain the address of A. This will cause us to do invalid dataflow analysis and lead to all sorts of problems.
As with inlining, it is possible to teach the optimizer to be able to split some critical edges. However, this isn't enough. If there is a single critical edge that the optimizer may not be able to split it means that various LLVM optimizations have to assume that critical edge splitting can fail. This had some significant effects on the loop optimizer, for example, which assumed that it could split critical edges to form canonical loops.
Can we get an N^2 explosion of CFG edges?
Absolutely. The issue here is that you can have N indirect branch instructions (in the example at the top, N = 5) and M labels with their addresses taken (in the example, M = 5). Since each indirectbr needs an edge to each label with its address taken, you get N*M edges, which is N^2. This can quickly become a big compile time problem, because it is fairly common for big interpreters to have hundreds of these things in their loops.
Fortunately, the fix for this is pretty simple: while the optimizer can safely duplicate an indirectbr instruction, it decides that it isn't profitable to do so. By trying to maintain at most one indirectbr instruction per function, we effectively get a factoring of the edges. The llvm-gcc and clang frontends both generate IR which has at most one indirectbr instruction per function: all other indirect gotos are lowered as a branch to the communal indirectbr in a function.
In order to produce efficient code, the code generator performs tail duplication to introduce the N^2 CFG. It does this early enough to get good code but late enough to not impact compile time too much.
What about labels whose address is taken but not branched to?
Circling back to the Linux BUG macro and other abuses of this extension, it is natural to wonder whether we support these uses better than LLVM 2.6. The answer is "sort of". In cases where code takes the address of a block and has an indirectbr in a function, that address will persist and other uses will have the expected behavior: They will see the address of a block and not some magic block ID number.
However, this typically isn't good enough. The issue is that taking the address of a block is not enough to prevent other optimizations (like block merging) from affecting it, it needs to have predecessors in the CFG. If we ever decide to better support abuses like this, we will need to extend our model to support them somehow.
In any case, I hope this discussion about indirectbr is helpful and illuminating. Interpreter loops will be much more performant with LLVM 2.7 than with LLVM 2.6 and earlier!
-Chris
