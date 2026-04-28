---
title: "4-bit floating point FP4"
url: "https://www.johndcook.com/blog/2026/04/17/fp4/"
fetched_at: 2026-04-28T07:02:46.543130+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# 4-bit floating point FP4

Source: https://www.johndcook.com/blog/2026/04/17/fp4/

In ancient times, floating point numbers were stored in 32 bits. Then somewhere along the way 64 bits became standard. The C programming language retains the ancient lore, using
float
to refer to a 32-bit floating point number and
double
to refer to a floating point number with double the number of bits. Python simply uses
float
to refer to the most common floating point format, which C calls
double
.
Programmers were grateful for the move from 32-bit floats to 64-bit floats. It doesn’t hurt to have more precision, and some numerical problems go away when you go from 32-bits to 64-bits. (Though not all. Something I’ve written about numerous times.)
Neural networks brought about something extraordinary: demand for floating point numbers with
less
precision. These networks have an enormous number of parameters, and its more important to fit more parameters into memory than it is to have higher precision parameters. Instead of double precision (64 bits) developers wanted
half
precision (16 bits), or even less, such as FP8 (8 bits) or FP4 (4 bits). This post will look at 4-bit floating point numbers.
Why even bother with floating point numbers when you don’t need much precision? Why not use integers? For example, with four bits you could represent the integers 0, 1, 2, …, 15. You could introduce a bias, subtracting say 7 from each value, so your four bits represent −7 through 8. Turns out it’s useful to have a more dynamic range.
FP4
Signed 4-bit floating point numbers in FP4 format use the first bit to represent the sign. The question is what to do with the remaining three bits. The notation E
x
M
y
denotes a format with
x
exponent bits and
y
mantissa bits. In the context of signed 4-bit numbers,
x
+
y
= 3
but in other contexts the sum could be larger. For example, for an 8-bit signed float,
x
+
y
= 7.
For 4-bit signed floats we have four possibilities: E3M0, E2M1, E1M2, and E0M3. All are used somewhere, but E2M1 is the most common and is supported in Nvidia hardware.
A number with sign bit
s
, exponent
e
, and mantissa
m
has the value
(−1)
s
2
e
−
b
(1 +
m
/2)
where
b
is the bias. The purpose of the bias is to allow positive and negative exponents without using signed numbers for
e
. So, for example, if
b
= 1 and
e
= 1, 2, or 3 then the exponent part 2
e
−
b
can represent 1, 2, or 4.
The bias impacts the range of possible numbers but not their relative spacing. For any value of bias
b
, the E3M0 format is all exponent, no mantissa, and so its possible values are uniformly distributed on a log scale. The E0M3 format is all mantissa, so its values are uniformly distributed on a linear scale. The E1M2 and E2M1 formats are unevenly spaced on both log and linear scales.
There is an exception to the expression above for converting (
s
,
e
,
m
) into a real number when
e
= 0. In that case,
m
= 0 represents 0 and
m
= 1 represents ½.
Table of values
Since there are only 16 possible FP4 numbers, it’s possible to list them all. Here is a table for the E2M1 format.
Bits s exp m  Value
-------------------
0000 0  00 0     +0
0001 0  00 1   +0.5
0010 0  01 0     +1
0011 0  01 1   +1.5
0100 0  10 0     +2
0101 0  10 1     +3
0110 0  11 0     +4
0111 0  11 1     +6
1000 1  00 0     -0
1001 1  00 1   -0.5
1010 1  01 0     -1
1011 1  01 1   -1.5
1100 1  10 0     -2
1101 1  10 1     -3
1110 1  11 0     -4
1111 1  11 1     -6
Note that even in this tiny floating point format, there are two zeros, +0 and −0, just like full precision floats. More on that
here
.
Pychop library
The Python library
Pychop
emulates a wide variety of reduced-precision floating point formats. Here is the code that used Pychop to create the table above.
import pychop

# Pull the format metadata from Pychop.
spec = pychop.MX_FORMATS["mxfp4_e2m1"]
assert (spec.exp_bits, spec.sig_bits) == (2, 1)

def e2m1_value(s: int, e: int, m: int) -> float:
    sign = -1.0 if s else 1.0

    # Subnormal / zero
    if e == 0:
        return sign * (m / 2.0)

    # Normal
    return sign * (2.0 ** (e - 1)) * (1.0 + m / 2.0)

def display_value(bits: int, x: float) -> str:
    if bits == 0b0000:
        return "+0"
    if bits == 0b1000:
        return "-0"
    return f"{x:+g}"

rows = []
for bits in range(16):
    s = (bits >> 3) & 0b1
    e = (bits >> 1) & 0b11
    m = bits & 0b1
    x = e2m1_value(s, e, m)

    rows.append(
        {
            "Bits": f"{bits:04b}",
            "s": s,
            "exp_bits": f"{e:02b}",
            "m": m,
            "Value": display_value(bits, x),
        }
    )

# Pretty-print the table.
header = f"{'Bits':<4} {'s':>1} {'exp':>3} {'m':>1} {'Value':>6}"
print(header)
print("-" * len(header))
for row in rows:
    print(
        f"{row['Bits']:<4} " f"{row['s']:>1} "
        f"{row['exp_bits']:>3} "
        f"{row['m']:>1} "
        f"{row['Value']:>6}"
    )
Other formats
FP4 isn’t the only 4-bit floating point format. There’s a surprisingly large number of formats in use. I intend to address another format my next post.
Update
: See the
next post
for a discussion of NF4, a format whose representable numbers more closely matches the distribution of LLM weights.
