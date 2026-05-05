---
title: "LLVM 3.3 Vectorization Improvements"
url: "https://blog.llvm.org/2013/05/llvm-33-vectorization-improvements.html"
fetched_at: 2026-05-05T07:01:43.232979+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM 3.3 Vectorization Improvements

Source: https://blog.llvm.org/2013/05/llvm-33-vectorization-improvements.html

LLVM 3.3 Vectorization Improvements
I would like to give a brief update regarding vectorization in LLVM. When LLVM 3.2 was released, it featured a new experimental
loop vectorizer
that was disabled by default. Since LLVM 3.2 was released, we have continued to work hard on improving vectorization, and we have some news to share. First, the loop vectorizer has new features and is now enabled by default on -O3. Second, we have a new SLP vectorizer. And finally, we have new clang command line flags to control the vectorizers.
Loop Vectorizer
The LLVM Loop Vectorizer has a number of new features that allow it to vectorize even more complex loops with better performance. One area that we focused on is the vectorization "cost model". When LLVM estimates if a loop may benefit from vectorization it uses a detailed description of the processor that can estimate the cost of various instructions. We improved both the X86 and ARM cost models. Improving the cost models helped the compiler to detect benefitting loops and improve the performance of many programs. During the analysis of vectorized programs, we also found and optimized many vector code sequences.
Another important improvement to the loop vectorizer is the ability to unroll during vectorization. When the compiler unrolls loops it generates more independent instructions that modern out-of-order processors can execute in parallel. The loop below adds all of the numbers in the array. When compiling this loop, LLVM creates two independent chains of calculations that can be executed in parallel.
int
sum_elements
(
int
*
A
,
int
n
)
{
int
sum
=
0
;
for
(
int
i
=
0
;
i
<
n
;
+
+
i
)
sum
+
=
A
[
i
]
;
return
sum
;
}
The innermost loop of the program above is compiled into the X86 assembly sequence below, which processes 8 elements at once, in two parallel chains of computations. The vector registers XMM0 and XMM1 are used to store the partial sum of different parts of the array. This allows the processor to load two values and add two values simultaneously.
LBB0
_
4
:
movdqu
16
(
%
rdi
,
%
rax
,4
)
,
%
xmm2
paddd
%
xmm2
,
%
xmm1
movdqu
(
%
rdi
,
%
rax
,4
)
,
%
xmm2
paddd
%
xmm2
,
%
xmm0
addq      $
8
,
%
rax
cmpq
%
rax
,
%
rcx
jne       LBB0
_
4
Another important improvement is the support for loops that contain IFs, and the detection of the popular min/max patterns. LLVM is now able to vectorize the code below:
int
fins_max
(
int
*
A
,
int
n
)
{
int
mx
=
A
[
0
]
;
for
(
int
i
=
0
;
i
<
n
;
+
+
i
)
if
(
mx
>
A
[
i
]
)
mx
=
A
[
i
]
;
return
mx
;
}
In the last release, the loop vectorizer was able to vectorize many, but not all, loops that contained floating point arithmetic. Floating point operations are not associative due to the unique rounding rules. This means that the expression (a + b) + c is not always equal to a + (b + c). The compiler flag -ffast-math tells the compiler not to worry about rounding errors and to optimize for speed. One of the new features of the loop vectorizer is the vectorization of floating point calculations when -ffast-math mode is used. Users who decide to use the -ffast-math flag will notice that many more loops get vectorized with the upcoming 3.3 release of LLVM.
SLP Vectorizer
The SLP vectorizer (short for superword-level parallelism) is a new vectorization pass. Unlike the loop vectorizer, which vectorizes consecutive loop iterations, the SLP vectorizer combines similar independent instructions in a straight-line code.
The SLP Vectorizer is now available and will be useful for many people.
The SLP Vectorizer can boost the performance of many programs in the LLVM test suite. In one benchmark, "Olden/Power", the SLP Vectorizer boosts the performance of the program by 16%. Here is one small example of a function that the SLP Vectorizer can vectorize.
void
foo
(
int
*
restrict A
,
int
*
restrict B
)
{
A
[
0
]
=
7
+
(
B
[
0
]
*
11
)
;
A
[
1
]
=
6
+
(
B
[
1
]
*
12
)
;
A
[
2
]
=
5
+
(
B
[
2
]
*
13
)
;
A
[
3
]
=
4
+
(
B
[
3
]
*
14
)
;
}
The code above is compiled into the ARMv7s assembly sequence below. Notice that the 4 additions and 4 multiplication operations became a single Multiply-Accumulate instruction "vmla".
_
foo
:
adr       r2
,
LCPI0
_
0
adr       r3
,
LCPI0
_
1
vld1
.32
{
d18
,
d19
}
,
[
r1
]
vld1
.64
{
d16
,
d17
}
,
[
r3
:
128
]
vld1
.64
{
d20
,
d21
}
,
[
r2
:
128
]
vmla
.
i32  q10
,
q9
,
q8
vst1
.32
{
d20
,
d21
}
,
[
r0
]
bx        lr
Command Line Flags
We've also added new command line flags to clang to control the vectorizers. The loop vectorizer is enabled by default for -O3, and it can be enabled or disabled for other optimization levels using the command line flags:
$ clang
.
.
.
-
fvectorize
/
-
fno
-
vectorize   file
.
c
The SLP vectorizer is disabled by default, and it can be enabled using the command line flags:
$ clang
.
.
.
-
fslp
-
vectorize file
.
c
LLVM has a second basic block vectorization phase which is more compile-time intensive (BB vectorizer). This optimization can be enabled through clang using the command line flag:
$ clang
.
.
.
-
fslp
-
vectorize
-
aggressive file
.
c
We've made huge progress in improving vectorization during the development of LLVM 3.3. Special thanks to all of the people who contributed to this effort.
