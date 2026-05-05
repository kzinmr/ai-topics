---
title: "What Every C Programmer Should Know About Undefined Behavior #1/3"
url: "https://blog.llvm.org/2011/05/what-every-c-programmer-should-know.html"
fetched_at: 2026-05-05T07:01:43.871313+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# What Every C Programmer Should Know About Undefined Behavior #1/3

Source: https://blog.llvm.org/2011/05/what-every-c-programmer-should-know.html

What Every C Programmer Should Know About Undefined Behavior #1/3
People occasionally ask why LLVM-compiled code sometimes generates SIGTRAP signals when the optimizer is turned on.
After digging in, they find that Clang generated a "ud2" instruction (assuming X86 code) - the same as is generated
by __builtin_trap(). There are several issues at work here, all centering around undefined behavior in C code and
how LLVM handles it.
This blog post (the first in a series of three) tries to explain some of these
issues so that you can better understand the tradeoffs and complexities involved, and perhaps learn a few more
of the dark sides of C. It turns out that C is
not
a "high level assembler" like many experienced C
programmers (particularly folks with a low-level focus) like to think, and that C++ and Objective-C have directly
inherited plenty of issues from it.
Introduction to Undefined Behavior
Translation available in:
Japanese
and
Spanish
Both LLVM IR and the C programming language have the concept of "undefined behavior". Undefined behavior is a
broad topic with a lot of nuances. The best introduction I've found to it is a post on
John Regehr's Blog
. The short version of this excellent article
is that many seemingly reasonable things in C actually have undefined behavior, and this is a common source of bugs
in programs. Beyond that, any undefined behavior in C gives license to the implementation (the compiler and runtime) to produce code that formats your hard drive, does completely unexpected things,
or worse
. Again, I would highly recommend reading
John's article
.
Undefined behavior exists in C-based languages because the designers of C wanted it to be an extremely efficient low-level programming language. In contrast, languages like Java (and many other 'safe' languages) have eschewed undefined behavior because they want safe and reproducible behavior across implementations, and willing to sacrifice performance to get it. While neither is "the right goal to aim for," if you're a C programmer you really should understand what undefined behavior is.
Before getting into the details, it is worth briefly mentioning what it takes for a compiler to get good performance out a broad range of C apps, because
there is no magic bullet
. At a very high level, compilers produce high performance apps by a) doing a good job at bread and butter algorithms like register allocation, scheduling, etc. b) knowing lots and lots of "tricks" (e.g. peephole optimizations, loop transformations, etc), and applying them whenever profitable. c) being good at eliminating unnecessary abstractions (e.g. redundancy due to macros in C, inlining functions, eliminating temporary objects in C++, etc) and d) not screwing anything up. While any of the optimizations below may sound trivial, it turns out that saving just one cycle out of a critical loop can make some codec run 10% faster or take 10% less power.
Advantages of Undefined Behavior in C, with Examples
Before getting into the dark side of undefined behavior and LLVM's policy and behavior when used as a C compiler, I thought it would be helpful to consider a few specific cases of undefined behavior, and talk about how each enables better performance than a safe language like Java. You can look at this either as "optimizations enabled" by the class of undefined behavior or as the "overhead avoided" that would be required to make each case defined. While the compiler optimizer could eliminate some of these overheads some of the time, to do so in general (for every case) would require solving the halting problem and many other "interesting challenges".
It is also worth pointing out that both Clang and GCC nail down a few behaviors that the C standard leaves undefined. The things I'll describe are both undefined according to the standard and treated as undefined behavior by both of these compilers in their default modes.
Use of an uninitialized variable:
This is commonly known as source of problems in C programs and there are many tools to catch these: from compiler warnings to static and dynamic analyzers. This improves performance by not requiring that all variables be zero initialized when they come into scope (as Java does). For most scalar variables, this would cause little overhead, but stack arrays and malloc'd memory would incur a memset of the storage, which could be quite costly, particularly since the storage is usually completely overwritten.
Signed integer overflow:
If arithmetic on an 'int' type (for example) overflows, the result is undefined. One example is that "INT_MAX+1" is not guaranteed to be INT_MIN. This behavior enables certain classes of optimizations that are important for some code. For example, knowing that INT_MAX+1 is undefined allows optimizing "X+1 > X" to "true". Knowing the multiplication "cannot" overflow (because doing so would be undefined) allows optimizing "X*2/2" to "X". While these may seem trivial, these sorts of things are commonly exposed by inlining and macro expansion. A more important optimization that this allows is for "<=" loops like this:
for (i = 0; i <= N; ++i) { ... }
In this loop, the compiler can assume that the loop will iterate exactly N+1 times if "i" is undefined on overflow, which allows a broad range of loop optimizations to kick in. On the other hand, if the variable is defined to wrap around on overflow, then the compiler must assume that the loop is possibly infinite (which happens if N is INT_MAX) - which then disables these important loop optimizations. This particularly affects 64-bit platforms since so much code uses "int" as induction variables.
It is worth noting that unsigned overflow is guaranteed to be defined as 2's complement (wrapping) overflow, so you can always use them. The cost to making signed integer overflow defined is that these sorts of optimizations are simply lost (for example, a common symptom is a ton of sign extensions inside of loops on 64-bit targets). Both Clang and GCC accept the "-fwrapv" flag which forces the compiler to treat signed integer overflow as defined (other than divide of INT_MIN by -1).
Oversized Shift Amounts:
Shifting a uint32_t by 32 or more bits is undefined. My guess is that this originated because the underlying shift operations on various CPUs do different things with this: for example, X86 truncates 32-bit shift amount to 5 bits (so a shift by 32-bits is the same as a shift by 0-bits), but PowerPC truncates 32-bit shift amounts to 6 bits (so a shift by 32 produces zero). Because of these hardware differences, the behavior is completely undefined by C (thus shifting by 32-bits on PowerPC could format your hard drive, it is
*not*
guaranteed to produce zero). The cost of eliminating this undefined behavior is that the compiler would have to emit an extra operation (like an 'and') for variable shifts, which would make them twice as expensive on common CPUs.
Dereferences of Wild Pointers and Out of Bounds Array Accesses:
Dereferencing random pointers (like NULL, pointers to free'd memory, etc) and the special case of accessing an array out of bounds is a common bug in C applications which hopefully needs no explanation. To eliminate this source of undefined behavior, array accesses would have to each be range checked, and the ABI would have to be changed to make sure that range information follows around any pointers that could be subject to pointer arithmetic. This would have an extremely high cost for many numerical and other applications, as well as breaking binary compatibility with every existing C library.
Dereferencing a NULL Pointer:
contrary to popular belief, dereferencing a null pointer in C is undefined. It is
not defined to trap
, and if you mmap a page at 0, it is
not defined to access that page
. This falls out of the rules that forbid dereferencing wild pointers and the use of NULL as a sentinel. NULL pointer dereferences being undefined enables a broad range of optimizations: in contrast, Java makes it invalid for the compiler to move a side-effecting operation across any object pointer dereference that cannot be proven by the optimizer to be non-null. This significantly punishes scheduling and other optimizations. In C-based languages, NULL being undefined enables a large number of simple scalar optimizations that are exposed as a result of macro expansion and inlining.
If you're using an LLVM-based compiler, you can dereference a "volatile" null pointer to get a crash if that's what you're looking for, since volatile loads and stores are generally not touched by the optimizer. There is currently no flag that enables random NULL pointer loads to be treated as valid accesses or to make random loads know that their pointer is "allowed to be null".
Violating Type Rules:
It is undefined behavior to cast an int* to a float* and dereference it (accessing the "int" as if it were a "float"). C requires that these sorts of type conversions happen through memcpy: using pointer casts is not correct and undefined behavior results. The rules for this are quite nuanced and I don't want to go into the details here (there is an exception for char*, vectors have special properties, unions change things, etc). This behavior enables an analysis known as "Type-Based Alias Analysis" (TBAA) which is used by a broad range of memory access optimizations in the compiler, and can significantly improve performance of the generated code. For example, this rule allows clang to optimize this function:
float *P;
void zero_array() {
int i;
for (i = 0; i < 10000; ++i)
P[i] = 0.0f;
}
into "
memset(P, 0, 40000)
". This optimization also allows many loads to be hoisted out of loops, common subexpressions to be eliminated, etc. This class of undefined behavior can be disabled by passing the -fno-strict-aliasing flag, which disallows this analysis. When this flag is passed, Clang is required to compile this loop into 10000 4-byte stores (which is several times slower), because it has to assume that it is possible for any of the stores to change the value of P, as in something like this:
int main() {
P = (float*)&P;  // cast causes TBAA violation in zero_array.
zero_array();
}
This sort of type abuse is pretty uncommon, which is why the standard committee decided that the significant performance wins were worth the unexpected result for "reasonable" type casts. It is worth pointing out that Java gets the benefits of type-based optimizations without these drawbacks because it doesn't have unsafe pointer casting in the language at all.
Anyway, I hope that this gives you an idea of some of the classes of optimizations enabled by undefined behavior in C. There are many other kinds of course, including sequence point violations like "foo(i, ++i)", race conditions in multithreaded programs, violating 'restrict', divide by zero, etc.
In our
next post
, we'll discuss why undefined behavior in C is a pretty scary thing if performance is not your only goal. In our final post in the series, we'll talk about how LLVM and Clang handle it.
-
Chris Lattner
