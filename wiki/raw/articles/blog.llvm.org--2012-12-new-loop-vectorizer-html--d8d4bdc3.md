---
title: "The LLVM Project Blog"
url: "https://blog.llvm.org/2012/12/new-loop-vectorizer.html"
fetched_at: 2026-05-05T07:01:43.472889+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# The LLVM Project Blog

Source: https://blog.llvm.org/2012/12/new-loop-vectorizer.html

New Loop Vectorizer
I would like to give a brief update regarding the development of the Loop Vectorizer. LLVM now has two vectorizers: The Loop Vectorizer, which operates on Loops, and the
Basic Block Vectorizer
, which optimizes straight-line code. These vectorizers focus on different optimization opportunities and use different techniques. The BB vectorizer merges multiple scalars that are found in the code into vectors while the Loop Vectorizer widens instructions in the original loop to operate on multiple consecutive loop iterations.
LLVM’s Loop Vectorizer is now available and will be useful for many people. It is not enabled by default, but can be enabled through clang using the command line flag
"-mllvm -vectorize-loops"
. We plan to enable the Loop Vectorizer by default as part of the LLVM 3.3 release.
The Loop Vectorizer can boost the performance of many loops, including some loops that are not vectorizable by GCC. In one benchmark, Linpack-pc, the Loop Vectorizer boosts the performance of gaussian elimination of single precision matrices from 984 MFlops to 2539 MFlops - a 2.6X boost in performance. The vectorizer also boosts the “GCC vectorization examples”
benchmark
by a geomean of 2.15X.
The LLVM Loop Vectorizer has a number of features that allow it to vectorize complex loops. Most of the features described in this post are available as part of the LLVM 3.2 release, but some features were added after the cutoff date. Here is one small example of a loop that the LLVM Loop Vectorizer can vectorize.
int
foo
(
int
*
A
,
int
*
B
,
int
n
)
{
unsigned
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
if
(
A
[
i
]
>
B
[
i
]
)
sum
+
=
A
[
i
]
+
5
;
return
sum
;
}
In this example, the Loop Vectorizer uses a number of non-trivial features to vectorize the loop. The ‘sum’ variable is used by consecutive iterations of the loop. Normally, this would prevent vectorization, but the vectorizer can detect that ‘sum’ is a reduction variable. The variable ‘sum’ becomes a vector of integers, and at the end of the loop the elements of the array are added together to create the correct result. We support a number of different reduction operations, such as multiplication.
Another challenge that the Loop Vectorizer needs to overcome is the presence of control flow in the loop. The Loop Vectorizer is able to "flatten" the IF statement in the code and generate a single stream of instructions. Another important feature is the vectorization of loops with an unknown trip count. In this example, ‘n’ may not be a multiple of the vector width, and the vectorizer has to execute the last few iterations as scalar code. Keeping a scalar copy of the loop increases the code size.
The loop above is compiled into the ARMv7s assembly sequence below. Notice that the IF structure is replaced by the "vcgt" and "vbsl" instructions.
LBB0_3:
vld1.32
{
d26
,
d27
}
,
[
r3
]
vadd.i32     q12
,
q8
,
q9
subs         r2
,
#
4
add.w        r3
,
r3
,
#
16
vcgt.s32     q0
,
q13
,
q10
vmla.i32     q12
,
q13
,
q11
vbsl         q0
,
q12
,
q8
vorr         q8
,
q0
,
q0
bne
LBB0_3
In the second example below, the Loop Vectorizer must use two more features in order to vectorize the loop. In the loop below, the iteration start and finish points are unknown, and the Loop Vectorizer has a mechanism to vectorize loops that do not start at zero. This feature is important for loops that are converted from Fortran, because Fortran loops start at 1.
Another major challenge in this loop is memory safety. In our example, if the pointers A and B point to consecutive addresses, then it is illegal to vectorize the code because some elements of A will be written before they are read from array B.
Some programmers use the 'restrict' keyword to notify the compiler that the pointers are disjointed, but in our example, the Loop Vectorizer has no way of knowing that the pointers A and B are unique. The Loop Vectorizer handles this loop by placing code that checks, at runtime, if the arrays A and B point to disjointed memory locations. If arrays A and B overlap, then the scalar version of the loop is executed.
void
bar
(
float
*
A
,
float
*
B
,
float
K
,
int
start
,
int
end
)
{
for
(
int
i
=
start
;
i
<
end
;
+
+
i
)
A
[
i
]
*
=
B
[
i
]
+
K
;
}
The loop above is compiled into this X86 assembly sequence. Notice the use of the 8-wide YMM registers on systems that support AVX.
LBB1_4:
vmovups
(
%
rdx
)
,
%
ymm2
vaddps
%
ymm1
,
%
ymm2
,
%
ymm2
vmovups
(
%
rax
)
,
%
ymm3
vmulps
%
ymm2
,
%
ymm3
,
%
ymm2
vmovups
%
ymm2
,
(
%
rax
)
addq
$32
,
%
rax
addq
$32
,
%
rdx
addq    $
-8
,
%
r1
1
jne
LBB1_4
In the last example, we don’t see a loop because it is hidden inside the "accumulate" function of the standard c++ library. This loop uses c++ iterators, which are pointers, and not integer indices, like we saw in the previous examples. The Loop Vectorizer detects pointer induction variables and can vectorize this loop. This feature is important because many C++ programs use iterators.
int
baz
(
int
*
A
,
int
n
)
{
return
std
::
accumulate
(
A
,
A
+
n
,
0
)
;
}
The loop above is compiled into this x86 assembly sequence.
LBB2_8:
vmovdqu
(
%
rcx
,
%
rdx
,
4
)
,
%
xmm1
vpaddd
%
xmm0
,
%
xmm1
,
%
xmm0
addq
$4
,
%
rdx
cmpq
%
rdx
,
%
rsi
jne
LBB2_8
The Loop Vectorizer is a target independent IR-level optimization that depends on target-specific information from the different backends. It needs to select the optimal vector width and to decide if vectorization is worthwhile. Users can force a certain vector width using the command line flag
"-mllvm -force-vector-width=X"
, where X is the number of vector elements. At the moment, only the X86 backend provides detailed cost information, while other targets use a less accurate method.
The work on the Loop Vectorizer is not complete and the vectorizer has a long way to go. We plan to add additional vectorization features such as automatic alignment of buffers, vectorization of function calls and support for user pragmas. We also plan to improve the quality of the generated code.
