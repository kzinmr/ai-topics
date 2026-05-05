---
title: "How a Bug(?) in the Linux CRC-32 Checksum Turned out not to be a Bug"
url: "https://danlark.org/2021/03/08/how-a-bug-in-the-linux-crc-32-checksum-turned-out-not-to-be-a-bug/"
fetched_at: 2026-05-05T07:01:53.317558+00:00
source: "Daniel Kutenin (danlark)"
tags: [blog, raw]
---

# How a Bug(?) in the Linux CRC-32 Checksum Turned out not to be a Bug

Source: https://danlark.org/2021/03/08/how-a-bug-in-the-linux-crc-32-checksum-turned-out-not-to-be-a-bug/

A friend of mine nerd sniped me with a good story to investigate which kinda made me giggle and want to tell to the public some cool things happened to me during my experience with hashing and other stuff.
The story is simple and complex at the same time, I’d try to stick to a simple version with the links for those who do understand the underlying computations better.
A Cyclic Redundancy Check (CRC) is the remainder of binary division of a potentially long message, by a CRC polynomial. This technique is employed in network and storage applications due to its effectiveness at detecting errors. It has some good properties as linearity.
Speaking in mathematical language CRC is calculated in the following way:
where the polynomial
defines the CRC algorithm and the symbol
denotes
carry-less multiplication
. Most of the times the polynomial
is irreducible, it just leads to fewer errors in some applications. CRC-32 is basically a CRC with
of degree 32 over Galois Field GF(2). Nevermind, it still does not matter much, mostly for the context.
x86 processors for quite some time have instructions
CLMUL
which are responsible for multiplication in GF(2) and can be enabled with
-mplcmul
in your C/C++ compilers. They are useful, for example, in
erasure coding
to speed up the recovery from the parity parts. As CRC uses something similar to this, there are algorithms that speed up the CRC computation with such instructions.
The main and almost the only one source of knowledge how to do it properly with other SIMD magic is
Fast CRC Computation for Generic Polynomials Using PCLMULQDQ Instruction
from Intel which likely hasn’t been changed since 2009, it has lots of pictures and it is nice to read when you understand the maths. But even if you don’t, it has a well defined algorithm which you can implement and check with other naive approaches that it is correct.
When it tries to define the final result, it uses so called scary
Barrett reduction
which is basically the subtraction of the inverse times the value. Just some maths.
Still not so relevant though. But here comes the most interesting part. In the guide there are some constants for that reduction for
gzip
CRC. They are looking this way
Look at k6′ and u’
If we look closely, we would notice that k6′ and u’ are ending in
640 and 641
respectively. So far, so good, yet, in the Linux kernel the constants are slightly different, let me show you
https://github.com/torvalds/linux/blob/v5.11/arch/x86/crypto/crc32-pclmul_asm.S#L72
It is stated to be written from the guide in the header, so they should be same. The constant is
0x1DB710641
vs
0x1DB710640
stated in the guide, the off by 1 but with the same 3 digits in the end as u’.
Two is that there’s also this line a little earlier on the same page:
= 0x1DB710641 This
number differs from
only in the final bit: 0x41 vs 0x40. This isn’t coincidental. Calculating
(in the Galois Field GF(2) space) means dividing (i.e. bitwise XOR-ing) a 33-bit polynomial (
, with only one ‘on’ bit) by the 33-bit polynomial
.
I thought for a while this is a legitimate bug. But wait a second, how can this be even possible given that CRC is used worldwide.
0x1DB710640 camp:
Rust
Intel with a guide and
code
Other “clean” implementations
0x1DB710641 camp:
I decided that this is too good to be true to be a bug, even though the number is changed, I also tried 0x42 and the tests fail. After that I started looking at the code and managed to prove that this constant +-1 does not matter
Let’s look the snippet where this constant is used from
zlib
:
static const uint64_t zalign(16) poly[] = { 0x01db710641, 0x01f7011641 };
//                                          ^^^^^^^^^^^^
// No use of poly
// …
// x0, x1, x2, x3 are 128 bit registers
x3 = _mm_setr_epi32(~0, 0, ~0, 0); // Set reverse, i.e. bits from 0 to 31 are 1s, from 32 to 63 are zeros, etc
// No reassignment of x3
// …
/*
* Barret reduce to 32-bits.
*/
x0 = _mm_load_si128((__m128i*)poly); // Load 16 bytes
x2 = _mm_and_si128(x1, x3);              // Do logical AND with x3
x2 = _mm_clmulepi64_si128(x2, x0, 0x10); // Do CLMUL with the high 8 bytes of poly
x2 = _mm_and_si128(x2, x3);              // Do logical AND with x3
x2 = _mm_clmulepi64_si128(x2, x0, 0x00); // Do CLMUL with the low 8 bytes of poly
x1 = _mm_xor_si128(x1, x2);              // XOR x1 and x2
/*
* Return the crc32.
*/
return _mm_extract_epi32(x1, 1); // Return bytes from 4 to 8 of x1, i.e. extract the second 32 bit integer
Speaking about CLMUL instruction, it has the following signature
__m128i _mm_clmulepi64_si128 (__m128i a, __m128i b, const int imm8)
, i.e. takes two 16 byte registers and mask and returns 16 byte register. The algorithm is the following
While executing the 15th line in gist
x2 = _mm_clmulepi64_si128(x2, x0, 0x10);
the mask imm8 takes the high 8 bytes in TEMP2 and thus the result isn’t changed, no need to worry here.
The most interesting part is the second _mm_clmulepi64_si128 with the third argument 0x00 which takes first 8 bytes from the operation in TEMP2. Actually the resulting values would be different but all we need to prove is that the bytes from 4 to 8 are the same because return happens with _mm_extract_epi32 which returns exactly uint32_t of that bytes (to be clear, the xor from x1 and x2 but if we prove bytes from 4 to 8 are the same for x2, it would be sufficient).
The bytes from 4 to 8 are only used in one loop in the operation:
TEMP2 is now our “magic” k6 value and TEMP1 is just some input. Note that when changing from 0x1DB710640 to 0x1DB710641 we only swap bit TEMP2[0]. Given it makes AND with all bits when
i
equals to
j
, the result would not change if and only if TEMP1[
j
] is zero for all j from 32 to 63.
And this turns out to be true because before the second CLMUL happens the following:
x2 = _mm_and_si128(x2, x3);
. And as you can see, x3 has bits zero from 32 to 63. And the returning result isn’t changed. What a coincidence! Given the conditions, if the last byte is changed to 0x42, only the highest bit can differ at the very most as it changes TEMP2[1].
For now I don’t know for 100% if it was made on purpose, to me looks like a human issue where the value was copy pasted and accidentally it worked. I wish during the interviews I also may miss any +-1 because of such bit magic 🙂
Bonus: speaking about CRC
This is not for the first time I face some weird bit magic issues with CRC, for example, look at the following code:
// For a fully compiled version look at
https://gist.github.com/danlark1/69c9d5e1d356eaa32dbdfccb2e19f401
#include <stdint.h>
#include <stddef.h>
#include <stdio.h>
#define FNV32INIT 2166136261U
#define FNV32PRIME 16777619U
#define FNV64INIT 14695981039346656037ULL
#define FNV64PRIME 1099511628211ULL
// Any table
extern unsigned long crc64table[256];
unsigned long fnv64(const void *p, size_t len) {
unsigned long init = FNV64INIT;
const unsigned char *_p = (const unsigned char *)p;
for (size_t i = 0; i < len; ++i) {
init = (init * FNV64PRIME) ^ _p[i];
}
return init;
}
unsigned long crc64(unsigned long crc, const void *p, size_t len) {
size_t i, t;
const unsigned char *_p = (const unsigned char *)p;
for (i = 0; i < len; i++) {
t = ((crc >> 56) ^ (*_p++)) & 0xFF;
crc = crc64table[t] ^ (crc << 8);
}
return crc;
}
int main() {
const char* data1 = "l.im/8ca";
const char* data2 = "l.im/8cf";
size_t size = 8;
unsigned long crc = crc64(fnv64(data1, size), data1, size);
printf("%lu\n", crc); // 6193082687915471267
crc = crc64(fnv64(data2, size), data2, size);
printf("%lu\n", crc); // 6193082687915471267
}
It seeds CRC64 hash with
FNV
hash and the results are the same. Though the last byte of the 8 word strings are different. I faced it once in URL hashing and it was failing for urls with very short domain and path.
The proof is left as an exercise to the reader
, try it out, really, it is some good bit twiddling. More hashing is sometimes bad hashing, be careful 🙂
Thanks to
Nigel Tao
who first suspected an issue with the Linux kernel and described it in the
wuffs
repository. I think no one should do anything as it perfectly works or at the very most fix the constants to better match the guideline.
