---
title: "The linear algebra of bit twiddling"
url: "https://www.johndcook.com/blog/2026/05/10/the-linear-algebra-of-bit-twiddling/"
fetched_at: 2026-05-11T07:01:21.522980+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# The linear algebra of bit twiddling

Source: https://www.johndcook.com/blog/2026/05/10/the-linear-algebra-of-bit-twiddling/

The
previous post
looked at the tempering step of the Mersenne Twister, formulating a sequence of bit operations as multiplication by a matrix mod 2. This post will look at the components more closely.
The theorems of linear algebra generally hold independent of the field of scalars. Typically the field is ℝ or ℂ, but most of basic linear algebra works the same over every field [1]. In particular, we can do linear algebra over a finite field, and we’re interested in the most finite of finite fields GF(2), the field with just two elements, 0 and 1.
In GF(2), addition corresponds to XOR. We will denote this by ⊕ to remind us that although it’s addition, it’s not the usual addition, i.e. 1 ⊕ 1 = 0. Similarly, multiplication corresponds to AND. We’ll work with 8-bit numbers to make the visuals easier to see.
Shifting a number left one bit corresponds to multiplication by a matrix with 1’s below the diagonal main. Shifting left by
k
bits is the same as shifting left by 1 bit
k
times, so the the matrix representation for
x
<<
k
is the
k
th power of the matrix representation of shifting left once. This matrix has 1s on the
k
th diagonal below the main diagonal. Below is the matrix for shifting left two bits,
x
<<
k
.
Right shifts are the mirror image of left shifts. Here’s the matrix for shifting right two bits,
x
>>
k
.
Shifts are not fully invertible because bits either fall off the left or the right end. The steps in the Mersenne Twister are invertible because shifts are always XOR’d with the original argument. For example, although the function that takes
x
to
x
>> 2 is not invertible, the function that takes
x
to
x
⊕ (
x
>> 2) is invertible. This operation corresponds to the matrix below.
This is an upper triangular matrix, so its determinant is the product of the diagonal elements. These are all 1s, so the determinant is 1, and the matrix is invertible.
Bitwise AND multiplies each bit of the input by the corresponding bit in another number known as the mask. The bits aligned with a 1 are kept and the bits aligned with a 0 are cleared. This corresponds to multiplying by a diagonal matrix whose diagonal elements correspond to the bits in the mask. For example, here is the matrix that corresponds to taking the bitwise AND with 10100100.
Each of the steps in the Mersenne Twister tempering process are invertible because they all correspond to triangular matrices with all 1’s on the diagonal. For example, the line
y ^= (y <<  7) & 0x9d2c5680
says to shift the bits of
y
left 7 places, then zero out the elements corresponding to 0s in the mask, then XOR the result with
y
. In matrix terms, we multiply by a lower triangular matrix with zeros on the main diagonal, then multiply by a diagonal matrix that zeros out some of the terms, then add the identity matrix. So the matrix corresponding to the line of code above is lower triangular, with all 1s on the diagonal, so it is invertible.
[1] Until you get to eigenvalues. Then it matters whether the field is algebraically complete, which no finite field is.
