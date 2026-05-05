---
title: "What Every C Programmer Should Know About Undefined Behavior #2/3"
url: "https://blog.llvm.org/2011/05/what-every-c-programmer-should-know_14.html"
fetched_at: 2026-05-05T07:01:43.856998+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# What Every C Programmer Should Know About Undefined Behavior #2/3

Source: https://blog.llvm.org/2011/05/what-every-c-programmer-should-know_14.html

What Every C Programmer Should Know About Undefined Behavior #2/3
In
Part 1
of our series, we discussed what undefined behavior is, and how it allows C and C++ compilers
to produce higher performance applications than "safe" languages. This post talks about how
"unsafe" C really is, explaining some of the highly surprising effects that undefined behavior
can cause. In
Part
#3
, we talk about what friendly compilers can do to mitigate some of the surprise, even
if they aren't required to.
I like to call this "
Why undefined behavior is often a scary and terrible thing for C
programmers
". :-)
Translation available in:
Japanese
,
and
Spanish
a>.
Interacting Compiler Optimizations Lead to Surprising Results
A modern compiler optimizer contains many optimizations that are run in specific orders, sometimes iterated, and change as the compiler evolves over time (e.g. new releases come out). Also, different compilers often have substantially different optimizers. Because optimizations run at different stages, emergent effects can occur due to previous optimizations changing the code.
Lets take a look at a silly example (simplified from an exploitable bug that was found in the Linux Kernel) to make this more concrete:
void contains_null_check(int *P) {
int dead = *P;
if (P == 0)
return;
*P = 4;
}
In this example, the code "clearly" checks for the null pointer. If the compiler happens to run "Dead Code Elimination" before a "Redundant Null Check Elimination" pass, then we'd see the code evolve in these two steps:
void contains_null_check_after_DCE(int *P) {
//int dead = *P;
// deleted by the optimizer.
if (P == 0)
return;
*P = 4;
}
and then:
void contains_null_check_after_DCE_and_RNCE(int *P) {
if (P == 0)   // Null check not redundant, and is kept.
return;
*P = 4;
}
However, if the optimizer happens to be structured differently, it could run RNCE before DCE. This would give us these two steps:
void contains_null_check_after_RNCE(int *P) {
int dead = *P;
if (
false
)  // P was dereferenced by this point, so it can't be null
return;
*P = 4;
}
and then dead code elimination runs:
void contains_null_check_after_RNCE_and_DCE(int *P) {
//int dead = *P;
//if (false)
//  return;
*P = 4;
}
To many (reasonable!) programmers, deleting the null check from this function would be very surprising (and they'd probably file a bug against the compiler :). However, both "contains_null_check_after_DCE_and_RNCE" and "contains_null_check_after_RNCE_and_DCE" are perfectly valid optimized forms of "contains_null_check" according to the standard, and both of the optimizations involved are important for the performance of various applications.
While this is intentionally a simple and contrived example, this sort of thing happens all the time with inlining: inlining a function often exposes a number of secondary optimization opportunities. This means that if the optimizer decides to inline a function, a variety of local optimizations can kick in, which change the behavior of the code. This is both perfectly valid according to the standard, and important for performance in practice.
Undefined Behavior and Security Don't Mix Well
The C family of programming languages is used to write a wide range of security critical code, such as kernels, setuid daemons, web browsers, and much more. This code is exposed to hostile input and bugs can lead to all sorts of exploitable security problems. One of the widely cited advantages of C is that it is relatively easy to understand what is going on when you read the code.
However, undefined behavior takes this property away. After all, most programmers would think that "contains_null_check" would do a null check above. While this case isn't too scary (the code will probably crash in the store if passed a null check, which is relatively easy to debug) there are a wide range of
very reasonable
looking C fragments that are completely invalid. This problem has bit many projects (including the Linux Kernel, OpenSSL, glibc, etc) and even led to CERT issuing a
vulnerability note
against GCC (though my personal belief is that all widely-used optimizing C compilers are vulnerable to this, not just GCC).
Lets look at an example. Consider this carefully written C code:
void process_something(int size) {
// Catch integer overflow.
if (size > size+1)
abort();
...
// Error checking from this code elided.
char *string = malloc(size+1);
read(fd, string, size);
string[size] = 0;
do_something(string);
free(string);
}
This code is checking to make sure that the malloc is big enough to hold the data read from the file (because a nul terminator byte needs to be added), bailing out if an integer overflow error occurs. However, this is
exactly the example we gave before
in which the compiler is allowed to (validly) optimize out the check. This means that it is perfectly possible for the compiler to turn this into:
void process_something(int *data, int size) {
char *string = malloc(size+1);
read(fd, string, size);
string[size] = 0;
do_something(string);
free(string);
}
When being built on a 64-bit platform, it is quite likely that this is an exploitable bug when "size" is INT_MAX (perhaps the size of a file on disk). Lets consider how terrible this is: a code auditor reading the code would very reasonably think that a proper overflow check is happening. Someone testing the code would find no problem unless they specifically tested that error path. The secure code seems to work, until someone goes ahead and exploits the vulnerability. All in all, this is a surprising and quite scary class of bugs. Fortunately, the fix is simple in this case: just use "size == INT_MAX" or similar.
As it turns out, integer overflow is a security problem for many reasons. Even if you are using fully defined integer arithmetic (either by using
-fwrapv
or by using unsigned integers), there is a
wholly different class
of integer overflow bug possible. Fortunately, this class is visible in the code and knowledgable security auditors are usually aware of the problem.
Debugging Optimized Code May Not Make Any Sense
Some people (for example, low level embedded programmers who like to look at generated machine code) do all of their development with optimizations turned on. Because code
frequently
has bugs when it is being developed, these folks end up seeing a disproportionate number of surprising optimizations that can lead to difficult-to-debug behaviors at runtime. For example, accidentally leaving out the "i = 0" in the "zero_array" example from the first article allows the compiler to completely discard the loop (compiling zero_array into "return;") because it is a use of an uninitialized variable.
Another interesting case that bit someone recently happened when they had a (global) function pointer. A simplified example looks like this:
static void (*FP)() = 0;
static void impl() {
printf("hello\n");
}
void set() {
FP = impl;
}
void call() {
FP();
}
which clang optimizes into:
void set() {}
void call() {
printf("hello\n");
}
It is allowed to do this because calling a null pointer is undefined, which permits it to assume that set() must be called before call(). In this case, the developer forgot to call "set", did not crash with a null pointer dereference, and their code broke when someone else did a debug build.
The upshot is that it is a fixable issue: if you suspect something weird is going on like this, try building at -O0, where the compiler is much less likely to be doing any optimizations at all.
"Working" code that uses undefined behavior can "break" as the compiler evolves or changes
We've seen many cases where applications that "appear to be work" suddenly break when a newer LLVM is used to build it, or when the application was moved from GCC to LLVM. While LLVM does occasionally have a bug or two itself :-), this is most often because of latent bugs in the application that are now being exposed by the compiler. This can happen all sorts different ways, two examples are:
1. an uninitialized variable which was zero initialized by luck "before", and now it shares some other register that isn't zero. This is commonly exposed by register allocation changes.
2. an array overflow on the stack which starts clobbering a variable that actually matters, instead of something that was dead. This is exposed when the compiler rearranges how it packs things on the stack, or gets more aggressive about sharing stack space for values with non-overlapping lifetimes.
The important and scary thing to realize is that just about *any* optimization based on undefined behavior can start being triggered on buggy code at any time in the future. Inlining, loop unrolling, memory promotion and other optimizations will keep getting better, and a significant part of their reason for existing is to expose secondary optimizations like the ones above.
To me, this is deeply dissatisfying, partially because the compiler inevitably ends up getting blamed, but also because it means that huge bodies of C code are land mines just waiting to explode. This is even worse because...
There is No Reliable Way to Determine if a Large Codebase Contains Undefined Behavior
Making the landmine a much much worse place to be is the fact that there is
no good way
to determine whether a large scale application is free of undefined behavior, and thus not susceptible to breaking in the future. There are many useful tools that can help find
some
of the bugs, but nothing that gives full confidence that your code won't break in the future. Lets look at some of these options, along with their strengths and weaknesses:
1. The
Valgrind
memcheck tool
is a fantastic way to find all sorts of uninitialized variables and other memory bugs. Valgrind is limited because it is quite slow, it can only find bugs that still exist in the generated machine code (so it
can't find things the optimizer removes
), and doesn't know that the source language is C (so it can't find shift-out-of-range or signed integer overflow bugs).
2. Clang has an experimental
-fcatch-undefined-behavior
mode that inserts runtime checks to find violations like shift amounts out of range, some simple array out of range errors, etc. This is limited because it slows down the application's runtime and it can't help you with random pointer dereferences (like Valgrind can), but it can find other important bugs. Clang also fully supports the
-ftrapv
flag (not to be confused with
-fwrapv
) which causes signed integer overflow bugs to trap at runtime (GCC also has this flag, but it is completely unreliable/buggy in my experience). Here is a quick demo of
-fcatch-undefined-behavior
:
$ cat t.c
int foo(int i) {
int x[2];
x[i] = 12;
return x[i];
}
int main() {
return foo(2);
}
$ clang t.c
$ ./a.out
$ clang t.c -fcatch-undefined-behavior
$ ./a.out
Illegal instruction
3. Compiler warning messages are good for finding some classes of these bugs, like uninitialized variables and simple integer overflow bugs. It has two primary limitations: 1) it has no dynamic information about your code as it executes, and 2) it must run very quickly because any analysis it does slows down compile time.
4.
The Clang Static Analyzer
performs a much deeper analysis to try to find bugs (including use of undefined behavior, like null pointer dereferences). You can think of it as generating souped up compiler warning messages, because it is not bound by the compile time constraints of normal warnings. The primary disadvantages of the static analyzer is that it 1) doesn't have dynamic information about your program as it runs, and 2) is not integrated into normal workflows for many developers (though its integration into
Xcode 3.2 and later
is fantastic).
5. The
LLVM "Klee" Subproject
uses symbolic analysis to "try every possible path" through a piece of code to find bugs in the code and it
produces a testcase
. It is a great little project that is mostly limited by not being practical to run on large-scale applications.
6. While I have never tried it, the
C-Semantics tool
by Chucky Ellison and Grigore Rosu is a very interesting tool that can apparently find some classes of bugs (such as sequence point violations). It is still a research prototype, but may be useful for finding bugs in (small and self-contained) programs. I recommend reading
John Regehr's post about it
for more information.
The end result of this is that we have lots of tools in the toolbox to find some bugs, but no good way to prove that an application is free of undefined behavior. Given that there are lots of bugs in real world applications and that C is used for a broad range of critical applications, this is pretty scary. In our
final article
, I look at various options that C compilers have when dealing with undefined behavior, with a specific focus on
Clang
.
-
Chris Lattner
