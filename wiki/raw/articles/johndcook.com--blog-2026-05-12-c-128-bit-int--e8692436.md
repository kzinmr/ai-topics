---
title: "C 128-bit unsigned int literals and printing"
url: "https://www.johndcook.com/blog/2026/05/12/c-128-bit-int/"
fetched_at: 2026-05-13T07:01:24.862515+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# C 128-bit unsigned int literals and printing

Source: https://www.johndcook.com/blog/2026/05/12/c-128-bit-int/

If you look very closely at my previous post, you’ll notice that I initialize a 128-bit integer with a 64-bit value. The 128-bit unsigned integer represents the internal state of a random number generator. Why not initialize it to a 128-bit value? I was trying to keep the code simple.
A surprising feature of C compilers, at least of GCC and Clang, is that you cannot initialize a 128-bit integer to a 128-bit integer
literal
. You can’t directly print a 128-bit integer either, which is why the previous post introduces a function
print_u128
.
The code
__uint128_t x = 0x00112233445566778899aabbccddeeff;
Produces the following error message.
error: integer literal is too large to be represented in any integer type
The problem isn’t initializing a 128-bit number to a 128-bit value; the problem is that the compiler cannot parse the literal expression
0x00112233445566778899aabbccddeeff
One solution to the problem is to introduce the macro
#define U128(hi, lo) (((__uint128_t)(hi) << 64) | (lo))
and use it to initialize the variable.
__uint128_t x = U128(0x0011223344556677, 0x8899aabbccddeeff);
You can verify that
x
has the intended state by calling
print_u128
from the previous post.
void print_u128(__uint128_t n)
{
    printf("0x%016lx%016lx\n",
           (uint64_t)(n >> 64),      // upper 64 bits
           (uint64_t)n);             // lower 64 bits
}
Then
print_u128(x);
prints
0x00112233445566778899aabbccddeeff
Update
. The code for
print_u128
above compiles cleanly with
gcc
but
clang
gives the following warning.
warning: format specifies type 'unsigned long' but the argument has type 'uint64_t' (aka 'unsigned long long') [-Wformat]
You can suppress the warning by including the
inttypes
header and modifying the
print_u128
function.
Here’s the final code. It compiles cleanly under
gcc
and
clang
.
#include <stdio.h>
#include <stdint.h>
#include <inttypes.h>
#define U128(hi, lo) (((__uint128_t)(hi) << 64) | (lo))

void print_u128(__uint128_t n)
{
    printf("0x%016" PRIx64 "%016" PRIx64 "\n",
           (uint64_t)(n >> 64),
           (uint64_t)n);
}

int main(void)
{
    __uint128_t x = U128(0x0011223344556677, 0x8899aabbccddeeff);
    print_u128(x);
    return 0;
}
