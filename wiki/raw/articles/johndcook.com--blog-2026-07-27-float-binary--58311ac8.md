---
title: "Printing floating point numbers in binary"
url: "https://www.johndcook.com/blog/2026/07/27/float-binary/"
fetched_at: 2026-07-28T10:08:50.504008+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Printing floating point numbers in binary

Source: https://www.johndcook.com/blog/2026/07/27/float-binary/

It’s well known that you can convert the base 16 (hex) representation of an integer to the base 2 (binary) representation by simply converting each digit from hex to binary. For example,
CAFE
hex
= 1100 1010 1111 1110
two
I imagine it’s less well known that you can do the same thing with floating point numbers.
I wanted to find the binary representation of a floating point number using Python, and discovered that it has no function to do this. However, there is a method on floats to show a hex representation. For example, here’s the hex representation of π.
>>> import math
>>> (math.pi).hex()
'0x1.921fb54442d18p+1'
Curiously, the p+
k
part at the end is an exponent of 2, not an exponent of 16. So after we convert 1.921fb54442d18 to binary, we’ll need to multiply by 2, i.e. move the fractional point one space to the right.
So first we convert 1.921fb54442d18
hex
to binary by converting 1, 9, 2, etc. each to binary.
1.1001 0010 0001 1111 1011 0101 0100 0100 0100 0010 1101 0001 1000
two
Then after shifting the fraction point to account for the
p+1
part we have
π = 11.001001000011111101101010100010001000010110100011000
two
You could use Python’s bin() function to convert the fractional part, interpreted as an integer, to hex, though you may need to pad with 0 bits. For example,
>>> (1.03).hex()
'0x1.07ae147ae147bp+0

>>> bin(0x7ae147ae147)
'0b1111010111000010100011110101110000101000111'
The binary representation of 1.03
ten
is
1.000001111010111000010100011110101110000101000111
two
We added a total of five zero bits, four for the 0 after the fractional point and one for converting 7 to 0111
two
.
