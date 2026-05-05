---
title: "Loop Vectorization: Diagnostics and Control"
url: "https://blog.llvm.org/2014/11/loop-vectorization-diagnostics-and.html"
fetched_at: 2026-05-05T07:01:41.315308+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# Loop Vectorization: Diagnostics and Control

Source: https://blog.llvm.org/2014/11/loop-vectorization-diagnostics-and.html

Loop Vectorization: Diagnostics and Control
Loop vectorization
was first introduced in LLVM 3.2 and turned on by default in LLVM 3.3. It has been discussed previously on this blog in
2012
and
2013
, as well as at
FOSDEM 2014
, and at
Apple's WWDC 2013
. The LLVM loop vectorizer combines multiple iterations of a loop to improve performance. Modern processors can exploit the independence of the interleaved instructions using advanced hardware features, such as multiple execution units and out-of-order execution, to improve performance.
Unfortunately, when loop vectorization is not possible or profitable the loop is silently skipped. This is a problem for many applications that rely on the performance vectorization provides. Recent updates to LLVM provide command line arguments to help diagnose vectorization issues and new a pragma syntax for tuning loop vectorization, interleaving, and unrolling.
New Feature: Diagnostics Remarks
Diagnostic remarks
provide the user with an insight into the behavior of the behavior of LLVM’s optimization passes including unrolling, interleaving, and vectorization. They are enabled using the
Rpass command line arguments
. Interleaving and vectorization diagnostic remarks are produced by specifying the ‘loop-vectorize’ pass. For example, specifying ‘-Rpass=loop-vectorize’ tells us the following loop was vectorized by 4 and interleaved by 2.
void test1(int *List, int Length) {
int i = 0;
while(i < Length) {
List[i] = i*2;
i++;
}
}
clang -O3
-Rpass=loop-vectorize
-S test1.c -o /dev/null
test1.c:4:5:
remark:
vectorized loop (vectorization factor: 4, unrolling interleave factor: 2)
while(i < Length) {
^
Many loops cannot be vectorized including loops with complicated control flow, unvectorizable types, and unvectorizable calls. For example, to prove it is safe to vectorize the following loop we must prove that array ‘A’ is not an alias of array ‘B’. However, the bounds of array ‘A’ cannot be identified.
void test2(int *A, int *B, int Length) {
for (int i = 0; i < Length; i++)
A[B[i]]++;
}
clang -O3
-Rpass-analysis=loop-vectorize
-S test2.c -o /dev/null
test2.c:3:5:
remark:
loop not vectorized: cannot identify array bounds
for (int i = 0; i < Length; i++)
^
Control flow and other unvectorizable statements are reported by the '-Rpass-analysis' command line argument. For example, many uses of ‘break’ and ‘switch’ are not vectorizable.
C/C++ Code
-Rpass-analysis=loop-vectorize
for (int i = 0; i < Length; i++) {
if (A[i] > 10.0)
break;
A[i] = 0;
}
control_flow.cpp:5:9:
remark:
loop not vectorized: loop control flow is not understood by vectorizer
for (int i = 0; i < Length; i++) {
switch(A[i]) {
case 0: B[i] = 1; break;
case 1: B[i] = 2; break;
default: B[i] = 3;
}
}
no_switch.cpp:4:5:
remark:
loop not vectorized: loop contains a switch statement
New Feature: Loop Pragma Directive
Explicitly control over the behavior of vectorization, interleaving and unrolling is necessary to fine tune the performance. For example, when compiling for size (-Os) it's a good idea to vectorize the hot loops of the application to improve performance. Vectorization, interleaving, and unrolling can be explicitly specified using the
#pragma clang loop
directive
prior to any for, while, do-while, or c++11 range-based for loop. For example, the vectorization width and interleaving count is explicitly specified for the following loop using the loop pragma directive.
void test3(float *Vx, float *Vy, float *Ux, float *Uy, float *P, int Length) {
#pragma clang loop vectorize_width(4) interleave_count(4)
#pragma clang loop unroll(disable)
for (int i = 0; i < Length; i++) {
float A = Vx[i] * Ux[i];
float B = A + Vy[i] * Uy[i];
P[i] = B;
}
}
clang -O3
-Rpass=loop-vectorize
-S test3.c -o /dev/null
test3.c:5:5:
remark:
vectorized loop (vectorization factor: 4, unrolling interleave factor: 4)
for (int i = 0; i < Length; i++) {
^
Integer Constant Expressions
The options vectorize_width, interleave_count, and unroll_count take an integer constant expression. So it can be computed as in the example below.
template <int ArchWidth, int ExecutionUnits>
void test4(float *Vx, float *Vy, float *Ux, float *Uy, float *P, int Length) {
#pragma clang loop vectorize_width(ArchWidth)
#pragma clang loop interleave_count(ExecutionUnits * 4)
for (int i = 0; i < Length; i++) {
float A = Vx[i] * Ux[i];
float B = A + Vy[i] * Uy[i];
P[i] = B;
}
}
void compute_test4(float *Vx, float *Vy, float *Ux, float *Uy, float *P, int Length) {
const int arch_width = 4;
const int exec_units = 2;
test4<arch_width, exec_units>(Vx, Vy, Ux, Uy, P, Length);
}
clang -O3
-Rpass=loop-vectorize
-S test4.cpp -o /dev/null
test4.cpp:6:5:
remark:
vectorized loop (vectorization factor: 4, unrolling interleave factor: 8)
for (int i = 0; i < Length; i++) {
^
Performance Warnings
Sometimes the loop transformation is not safe to perform. For example, vectorization fails due to the use of complex control flow. If vectorization is explicitly specified a warning message is produced to alert the programmer that the directive cannot be followed. For example, the following function which returns the last positive value in the loop, cannot be vectorized because the ‘last_positive_value’ variable is used outside the loop.
int test5(int *List, int Length) {
int last_positive_index = 0;
#pragma clang loop vectorize(enable)
for (int i = 1; i < Length; i++) {
if (List[i] > 0) {
last_positive_index = i;
continue;
}
List[i] = 0;
}
return last_positive_index;
}
clang -O3 -g -S test5.c -o /dev/null
test5.c:5:9:
warning:
loop not vectorized: failed explicitly specified loop vectorization
for (int i = 1; i < Length; i++) {
^
The debug option ‘-g’ allows the source line to be provided with the warning.
Conclusion
Diagnostic remarks and the loop pragma directive are two new features that are useful for feedback-directed-performance tuning. Special thanks to all of the people who contributed to the development of these features. Future work includes adding diagnostic remarks to the SLP vectorizer and an additional option for the loop pragma directive to declare the memory operations as safe to vectorize. Additional ideas for improvements are welcome.
