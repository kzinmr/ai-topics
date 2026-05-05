---
title: "Optimizing 128-bit Division"
url: "https://danlark.org/2020/06/14/128-bit-division/"
fetched_at: 2026-05-05T07:01:55.475698+00:00
source: "Daniel Kutenin (danlark)"
tags: [blog, raw]
---

# Optimizing 128-bit Division

Source: https://danlark.org/2020/06/14/128-bit-division/

When it comes to hashing, sometimes 64 bit is not enough, for example, because of
birthday paradox
— the hacker can iterate through random
entities and it can be proven that with some constant probability they will find a collision, i.e. two different objects will have the same hash.
is around 4 billion objects and with the current power capacity in each computer it is certainly achievable. That’s why we need sometimes to advance the bitness of hashing to at least 128 bits. Unfortunately, it comes with a cost because platforms and CPUs do not support 128 bit operations natively.
Division historically is the most complex operation on CPUs and all guidelines suggest avoiding the division at all costs.
At my job I faced an interesting problem of optimizing 128 bit division from
abseil library
in order to split some data across buckets with the help of 128 bit hashing (the number of buckets is not fixed for some uninteresting historical reasons). I found out that the division takes a really long time. The
benchmarks
from abseil on Intel(R) Xeon(R) W-2135 CPU @ 3.70GHz show some horrible results
Benchmark                       Time(ns)  CPU(ns)
BM_DivideClass128UniformDivisor     13.8     13.8  // 128 bit by 128 bit
BM_DivideClass128SmallDivisor        168      168  // 128 bit by 64 bit
150 nanoseconds for dividing the random 128 bit number by a random 64 bit number? Sounds crazy. For example,
div
instruction on x86-64 Skylake takes 76 cycles (also, for AMD processors it is much less), the division takes around 20-22ns.
https://godbolt.org/z/o2vTZr
In reality everything is slightly better because of pipeline execution and division has its own ALU, so if you divide something and do something else in the next instructions, you will get lower average latency. Still, 128 bit division cannot be 8x slower than 64 bit division. All latencies you can find in Agner Fog
instruction table
for most of the modern x86 CPUs. The truth is more complex and division latency can even depend on the values given.
Agner Fog instruction table for Skylake CPUs, the second but last column is the latency.
Even compilers when dividing by some constants, try to use the reciprocal (or, the same as inverse in a ring) value and multiply the reciprocal and the value with some shifts afterwards
https://gcc.godbolt.org/z/PRibsx
Overall, given the fact that only some
sin
,
cos
instructions cost more than division, division is one of the most complex instructions in CPUs and optimizations in that place matter a lot. My exact case was more or less general, maybe I was dividing 128 bit by 64 bit a bit more frequent. We are going to optimize the general case in LLVM.
We need to understand how 128 bit division is working through the compiler stack.
https://gcc.godbolt.org/z/fB3aq2
It calls
__udivti3
function. Let’s first understand how to read these functions. In runtime libraries the modes of the functions are:
QI: An integer that is as wide as the smallest addressable unit, usually 8 bits.
HI: An integer, twice as wide as a QI mode integer, usually 16 bits.
SI: An integer, four times as wide as a QI mode integer, usually 32 bits.
DI: An integer, eight times as wide as a QI mode integer, usually 64 bits.
SF: A floating point value, as wide as a SI mode integer, usually 32 bits.
DF: A floating point value, as wide as a DI mode integer, usually 64 bits.
TI: An integer, 16 times as wide as a QI mode integer, usually 128 bits.
So,
udivti3
is an
u
nsigned division of TI (128 bits) integers, last ‘
3′
means that it has 3 arguments including the return value. Also, there is a function
__udivmodti4
which computes the divisor and the remainder (division and modulo operation) and it has 4 arguments including the returning value. These functions are a part of runtime libraries which compilers provide by default. For example, in GCC it is
libgcc
, in LLVM it is
compiler-rt
, they are linked almost in every program if you have the corresponding toolchain. In LLVM,
__udivti3
is a simple alias to
__udivmodti4
.
#include "int_lib.h"
/*
typedef      int si_int;
typedef unsigned su_int;
typedef          long long di_int;
typedef unsigned long long du_int;
typedef int ti_int __attribute__((mode(TI))); // 128 signed
typedef unsigned tu_int __attribute__((mode(TI))); // 128 bit unsigned
*/
#ifdef CRT_HAS_128BIT
COMPILER_RT_ABI tu_int __umodti3(tu_int a, tu_int b) {
tu_int r;
__udivmodti4(a, b, &r);
return r;
}
// Returns: a % b
COMPILER_RT_ABI ti_int __modti3(ti_int a, ti_int b) {
const int bits_in_tword_m1 = (int)(sizeof(ti_int) * CHAR_BIT) – 1;
ti_int s = b >> bits_in_tword_m1; // s = b < 0 ? -1 : 0
b = (b ^ s) – s;                  // negate if s == -1
s = a >> bits_in_tword_m1;        // s = a < 0 ? -1 : 0
a = (a ^ s) – s;                  // negate if s == -1
tu_int r;
__udivmodti4(a, b, &r);
return ((ti_int)r ^ s) – s; // negate if s == -1
}
#endif // CRT_HAS_128BIT
#include "int_lib.h"
/*
typedef      int si_int;
typedef unsigned su_int;
typedef          long long di_int;
typedef unsigned long long du_int;
typedef int ti_int __attribute__((mode(TI))); // 128 signed
typedef unsigned tu_int __attribute__((mode(TI))); // 128 bit unsigned
*/
#ifdef CRT_HAS_128BIT
// Returns: a / b
COMPILER_RT_ABI tu_int __udivti3(tu_int a, tu_int b) {
return __udivmodti4(a, b, 0);
}
COMPILER_RT_ABI ti_int __divti3(ti_int a, ti_int b) {
const int bits_in_tword_m1 = (int)(sizeof(ti_int) * CHAR_BIT) – 1;
ti_int s_a = a >> bits_in_tword_m1;                   // s_a = a < 0 ? -1 : 0
ti_int s_b = b >> bits_in_tword_m1;                   // s_b = b < 0 ? -1 : 0
a = (a ^ s_a) – s_a;                                  // negate if s_a == -1
b = (b ^ s_b) – s_b;                                  // negate if s_b == -1
s_a ^= s_b;                                           // sign of quotient
return (__udivmodti4(a, b, (tu_int *)0) ^ s_a) – s_a; // negate if s_a == -1
}
#endif // CRT_HAS_128BIT
__udivmodti4
function was written with the help of
Translated from Figure 3-40 of The PowerPC Compiler Writer's Guide.
After looking at it
here
, it looks like this was written long time ago and things have changed since then
First of all, let’s come up with something easy, like shift-subtract algorithm that we have been learning since childhood. First, if
divisor > dividend
, then the quotient is zero and remainder is the
dividend
, not an interesting case.
// dividend / divisor, remainder is stored in rem.
uint128 __udivmodti4(uint128 dividend, uint128 divisor, uint128* rem) {
if (divisor > dividend) {
if (rem)
*rem = dividend;
return 0;
}
// Calculate the distance between most significant bits, 128 > shift >= 0.
int shift = Distance(dividend, divisor);
divisor <<= shift;
quotient = 0;
for (; shift >= 0; –shift) {
quotient <<= 1;
if (dividend >= divisor) {
dividend -= divisor;
quotient |= 1;
}
divisor >>= 1;
}
if (rem)
*rem = dividend;
return quotient;
}
The algorithm is easy, we align the numbers by their most significant bits, if dividend is more than divisor, subtract and add 1 to the output, then shift by 1 and repeat.  Some sort of animation can be seen like that:
For 128 bit division it will take at most 128 iterations in the for loop. Actually, the implementation in
LLVM
for loop is a fallback and we saw it takes 150+ns to complete it because it requires to shift many registers because 128 bit numbers are represented as two registers.
Now, let’s dive into the architecture features. I noticed that while the compiler generates the
divq
instructions, it frees
rdx
register
In the manual they say the following
divq
instruction provides 128 bit division from [%rdx]:[%rax] by
S
. The quotient is stored in
%rax
and the remainder in
%rdx
. After some experimenting with inline asm in C/C++, I figured out that if the result does not fit in 64 bits, SIGFPE is raised. See:
#include <cinttypes>
uint64_t div(uint64_t u1, uint64_t u0, uint64_t v) {
uint64_t result;
uint64_t remainder;
__asm__("divq %[v]" : "=a"(result), "=d"(remainder) : [v] "r"(v), "a"(u0), "d"(u1));
return result;
}
int main() {
div(1, 0, 1); // 2**64 / 1
}
/*
g++ -std=c++17 -O0 main.cpp -o main
./main
“./main” terminated by signal SIGFPE (Floating point exception)
*/
Compilers don’t use this instruction in 128 bit division because they cannot know for sure if the result is going to fit in 64 bits. Yet, if the high 64 bits of the 128 bit number is smaller than the divisor, the result fits into 64 bits and we can use this instruction. As compilers don’t generate
div
q instruction for their own reasons, we would use inline asm for x86-64.
#if defined(__x86_64__)
inline uint64_t Divide128Div64To64(uint64_t high, uint64_t low,
uint64_t divisor, uint64_t* remainder) {
uint64_t result;
__asm__("divq %[v]"
: "=a"(result), "=d"(*remainder) // Output parametrs, =a for rax, =d for rdx, [v] is an
// alias for divisor, input paramters "a" and "d" for low and high.
: [v] "r"(divisor), "a"(low), "d"(high));
return result;
}
#endif
tu_int __udivmodti4(tu_int dividend, tu_int divisor, tu_int* remainder) {
…
#if defined(__x86_64__)
if (divisor.high == 0 && dividend.high < divisor) {
remainder->high = 0;
uint64_t quotient =
Divide128Div64To64(dividend.high, dividend.low,
divisor.low, &remainder->low);
return quotient;
}
#endif
…
}
What to do if the high is not less than the divisor? The right answer is to use 2 divisions because
So, first we can divide
hi
by
divisor
and then
{hi_r, lo}
by
divisor
guaranteeing that
hi_r
is smaller than
divisor
and thus the result is smaller than
. We will get something like
#if defined(__x86_64__)
inline uint64_t Divide128Div64To64(uint64_t high, uint64_t low,
uint64_t divisor, uint64_t* remainder) {
uint64_t result;
__asm__("divq %[v]"
: "=a"(result), "=d"(*remainder) // Ouput parametrs, =a for rax, =d for rdx, [v] is an
// alias for divisor, input paramters "a" and "d" for low and high.
: [v] "r"(divisor), "a"(low), "d"(high));
return result;
}
#endif
tu_int __udivmodti4(tu_int dividend, tu_int divisor, tu_int* remainder) {
…
#if defined(__x86_64__)
if (divisor.high == 0) {
remainder->high = 0;
if (dividend.high < divisor) {
uint64_t quotient =
Divide128Div64To64(dividend.high, dividend.low,
divisor.low, &remainder->low);
return quotient;
} else {
tu_int quotient;
quotient.high = Divide128Div64To64(0, dividend.high, divisor.low,
&dividend.high);
quotient.low = Divide128Div64To64(dividend.high, dividend.low,
divisor.low, &remainder->low);
return quotient;
}
}
#endif
…
}
After that the benchmarks improved significantly
Benchmark                       Time(ns)  CPU(ns)
BM_DivideClass128UniformDivisor 11.9      11.9
BM_DivideClass128SmallDivisor   26.6      26.6
Only 26.6ns for small divisors, that’s a clear 6x win.
Then there are multiple choices to do next but we know that both dividend and divisor have at least one bit in their high registers and the shift-subtract algorithm will have at most 64 iterations. Also the quotient is guaranteed to fit in 64 bits, thus we can use only the low register of the resulting quotient and save more shifts in the shift-subtract algorithm. That’s why the uniform divisor slightly improved.
One more optimization to do in shift-subtract algorithm is to remove the branch inside the for loop (read carefully, it should be understandable).
// dividend / divisor, remainder is stored in rem.
uint128 __udivmodti4(uint128 dividend, uint128 divisor, uint128* rem) {
if (divisor > dividend) {
if (rem)
*rem = dividend;
return 0;
}
// 64 bit divisor implementation
…
// end
// Calculate the distance between most significant bits, 128 > shift >= 0.
int shift = Distance(dividend, divisor);
divisor <<= shift;
quotient.low = 0;
quotient.high = 0;
for (; shift >= 0; –shift) {
quotient.low <<= 1;
const int128 s = (int128)(divisor.all – dividend.all – 1) >> 127;
quotient.low |= s & 1;
dividend.all -= divisor.all & s;
divisor >>= 1;
}
if (rem)
*rem = dividend;
return quotient;
}
In the end, it gives 0.4ns more for uniform 128 bit divisor.
And finally I believe that’s one of the best algorithm to divide 128 bit by 128 bit numbers. From statistics, the case when the divisor is 64 bit is worth optimizing and we showed that additional checks on the high register of divisor has its own advantages and expansion of the invariants. Now let’s see what other libraries perform in that case.
LibDivide
Libdivide
is a small library targeting fast division, for example, if you divide by some fixed number a lot of times, there are techniques that can precalculate reciprocal and then multiply by it. Libdivide provides a very good interface for such optimizations. Even though, it has some optimizations regarding 128 bit division. For example, function
libdivide_128_div_128_to_64
computes the division 128 bit number by 128 bit number if the result fits in 64 bits. In the case where both numbers are more or equal to
it does the following algorithm that they took from
Hackers Delight
book:
With the instruction that produces the 64 bit result when the divisor is 128 bit result we can compute
Then we compute
.
It cannot overflow because
because the maximum value of
is
and minimum value of
is
. Now let’s show that
.
Now we want to show that
.
is the largest when the remainder in the numerator is as large as possible, it can be up to
. Because of the definition of
,
. The smallest value of
in the denominator is
. That’s why
. As n iterates from 0 to 63, we can conclude that
. So we got either the correct value, either the correct plus one. Everything else in the algorithms is just a correction of which result to choose.
Unfortunately, these corrections increase the latency of the benchmark pretty significant
Benchmark                                          Time(ns)  CPU(ns)
BM_DivideClass128UniformDivisor<LibDivideDivision>    26.3    26.3  
BM_RemainderClass128UniformDivisor<LibDivideDivision> 26.2    26.2
BM_DivideClass128SmallDivisor<LibDivideDivision>      25.8    25.8
BM_RemainderClass128SmallDivisor<LibDivideDivision>   26.3    26.3
So I decided to drop this idea after I’ve tried this.
GMP
GMP
library is a standard GNU library for long arithmetic. They also have something for 128 bit by 64 bit division and in my benchmark the following code worked
struct
GmpDiv
{
uint64_t
operator
()(
uint64_t
u1
,
uint64_t
u0
,
uint64_t
v
,
du_int
*
r
)
const
{
mp_limb_t
q
[
2
]
=
{
u0
,
u1
};
mp_limb_t
result
[
2
]
=
{
0
,
0
};
*
r
=
mpn_divrem_1
(
result
,
0
,
q
,
2
,
v
);
return
result
[
0
];
}
};
It divides the two limbs by a
uint64_t
and provides the result. Unfortunately, the latency is much higher than expected, also does not work
Benchmark                                          Time(ns)  CPU(ns)
BM_DivideClass128UniformDivisor<GmpDivision>          11.5    11.5
BM_RemainderClass128UniformDivisor<GmpDivision>       10.7    10.7
BM_DivideClass128SmallDivisor<GmpDivision>            47.5    47.5
BM_RemainderClass128SmallDivisor<GmpDivision>         47.8    47.8
Conclusion
In the end I’ve tried several method of 128 bit division and came up with something that is the fastest among popular alternatives.
Here
is the full code for benchmarks, though it is quite hard to install, maybe later I will provide an easy version of installation. The final benchmarks are
Benchmark                                           Time(ns)  CPU(ns)
---------------------------------------------------------------------
BM_DivideClass128UniformDivisor<absl::uint128>        13.7      13.7
BM_RemainderClass128UniformDivisor<absl::uint128>     14.0      14.0  
BM_DivideClass128SmallDivisor<absl::uint128>          169       169    
BM_RemainderClass128SmallDivisor<absl::uint128>       153       153    
BM_DivideClass128UniformDivisor<LLVMDivision>         12.6      12.6  
BM_RemainderClass128UniformDivisor<LLVMDivision>      12.3      12.3  
BM_DivideClass128SmallDivisor<LLVMDivision>           145        145    
BM_RemainderClass128SmallDivisor<LLVMDivision>        140        140    
**BM_DivideClass128UniformDivisor<MyDivision1>          11.6      11.6**
**BM_RemainderClass128UniformDivisor<MyDivision1>       10.7      10.7**
**BM_DivideClass128SmallDivisor<MyDivision1>            25.5      25.5**
**BM_RemainderClass128SmallDivisor<MyDivision1>         26.2      26.2**
BM_DivideClass128UniformDivisor<MyDivision2>          12.7      12.7  
BM_RemainderClass128UniformDivisor<MyDivision2>       12.8      12.8  
BM_DivideClass128SmallDivisor<MyDivision2>            36.9      36.9  
BM_RemainderClass128SmallDivisor<MyDivision2>         37.0      37.1  
BM_DivideClass128UniformDivisor<GmpDivision>          11.5      11.5  
BM_RemainderClass128UniformDivisor<GmpDivision>       10.7      10.7  
BM_DivideClass128SmallDivisor<GmpDivision>            47.5      47.5  
BM_RemainderClass128SmallDivisor<GmpDivision>         47.8      47.8  
BM_DivideClass128UniformDivisor<LibDivideDivision>    26.3      26.3  
BM_RemainderClass128UniformDivisor<LibDivideDivision> 26.2      26.2  
BM_DivideClass128SmallDivisor<LibDivideDivision>      25.8      25.8  
BM_RemainderClass128SmallDivisor<LibDivideDivision>   26.3      26.3
MyDivision1 is going to be
upstreamed
in LLVM, MyDivision2 will be the default version for all non x86-64 platforms which also has a solid latency, much better than the previous one.
Future Work
However, benchmarks are biased in the uniform divisor case because the distance between most significant bits in the dividend and divisor falls exponentially and starting from 10-15, the benchmark becomes worse rather than libdivide approach.
I also prepared some recent research
paper
patch in
https://reviews.llvm.org/D83547
where the reciprocal is computed beforehand and then only some multiplication happens. Yet, with the cold cache of the 512 byte lookup table it is worse than the already submitted approach. I also tried just division by
in the screenshot below and it showed some inconsistent results which I don’t understand for now.
Also, subscribe to my Twitter
https://twitter.com/Danlark1
🙂
