---
title: "What's wrong with this code?"
url: "https://blog.llvm.org/2010/04/whats-wrong-with-this-code.html"
fetched_at: 2026-05-05T07:01:44.201994+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# What's wrong with this code?

Source: https://blog.llvm.org/2010/04/whats-wrong-with-this-code.html

What's wrong with this code?
By Daniel Dunbar
Apr 7, 2010
#KLEE
2 minute read
A user on IRC sent me this interesting KLEE example today, which I thought was cute enough I should post it.
If you aren't familiar with it,
KLEE
is a tool for symbolic execution of LLVM code. It is way too complicated to explain here, but for the purposes of this example all you need to know is that it tries to explore all possible paths through a program.
In this case, the user was actually talking to me because he thought there was a bug in KLEE, because it was only finding one path through the code. Here is the example:
$ cat t.c
#include "klee/klee.h"
int f0(int x) {
if (x * x == 1000)
return 1;
else
return 0;
}
int main() {
return f0(klee_int("x"));
}
The idea here is that
klee_int("x")
creates a new symbolic variable, which can be
anything
(well, any possible
int
).
The user was expecting that there would be two possible paths through this program, one returning 1 and one returning 0. But KLEE only finds one:
$ clang -I ~/public/klee/include -flto -c t.c
$ ~/public/klee.obj.64/Debug/bin/klee t.o
KLEE: output directory = "klee-out-5"
KLEE: done: total instructions = 24
KLEE: done: completed paths = 1
KLEE: done: generated tests = 1
Upon showing the example to me, I was also confused for a moment. However, since I happen to trust KLEE, I knew to look for a problem in the test case! And of course, the square root of 1000 isn't an integer, so there is no way this code can return 1. If we change the 1000 to 100, KLEE finds two paths as we would expect:
$ cat t.c
#include "klee/klee.h"
int f0(int x) {
if (x * x == 100)
return 1;
else
return 0;
}
int main() {
return f0(klee_int("x"));
}
$ clang -I ~/public/klee/include -flto -c t.c
$ ~/public/klee.obj.64/Debug/bin/klee t.o
KLEE: output directory = "klee-out-6"
KLEE: done: total instructions = 31
KLEE: done: completed paths = 2
KLEE: done: generated tests = 2
This example shows exactly what KLEE was designed for -- reasoning about code (or math) is hard, and it is great to let a machine do it for you!
