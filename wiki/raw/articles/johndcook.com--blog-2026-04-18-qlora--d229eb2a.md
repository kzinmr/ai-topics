---
title: "Gaussian distributed weights for LLMs"
url: "https://www.johndcook.com/blog/2026/04/18/qlora/"
fetched_at: 2026-04-29T07:02:07.089383+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Gaussian distributed weights for LLMs

Source: https://www.johndcook.com/blog/2026/04/18/qlora/

The
previous post
looked at the
FP4
4-bit floating point format. This post will look at another 4-bit floating point format,
NF4
, and higher precision analogs. NF4 and FP4 are common bitsandbytes 4-bit data types. If you download LLM weights from Hugging Face quantized to four bits, the weights might be in NF4 or FP4 format. Or maybe some other format: there’s a surprising amount of variety in how 4-bit numbers are implemented.
Why NF4
LLM parameters have a roughly Gaussian distribution, and so evenly spaced numeric values are not ideal for parameters. Instead, you’d like numbers that are closer together near 0.
The FP4 floating point numbers, described in the previous post, are spaced 0.5 apart for small values, and the larger values are spaced 1 or 2 apart. That’s hardly a Gaussian distribution, but it’s closer to Gaussian than a uniform distribution would be. NF4 deliberately follows more of a Gaussian distribution.
QLoRA
The QLoRA formats [1], unlike FP4, are not analogs of IEEE numbers. The bits are not interpreted as sign, exponent, and mantissa, but rather as integers to be used as indexes. An NF
n
number is an index into a list of 2
n
real numbers with Gaussian spacing. To put it another way, the numbers represented by NF
n
have uniformly distributed
z
-scores.
That makes sense at a high level, but the paper [1] is hard to follow in detail. It says
More formally, we estimate the 2
k
values
q
i
of the data type as follows:
where
Q
X
(·) is the quantile function of the standard normal distribution
N
(0, 1).
The paper doesn’t give the range of
i
but it says there are 2
k
values, implying that
i
runs from 0 to 2
k
−1 or from 1 to 2
k
. Either way runs into infinite values since
Q
(0) = −∞ and
Q
(1) = ∞. We could avoid infinities by letting
i
run from 1 to 2
n
− 1.
The next sentence is puzzling.
A problem for a symmetric k-bit quantization is that this approach does not have an exact representation of zero, which is an important property to quantize padding and other zero-valued elements with no error.
I understand the desire to represent 0 exactly, but the equation above has an exact representation of 0 when
i
= 2
n
− 1
. Perhaps the authors had in mind that
i
takes on the values ½, 1 + ½, 2 + ½, …, 2
n
− ½. This would be reasonable, but a highly unusual use of notation. It seems that the real problem is not the lack of a representation of 0 but an unused index, with
i
running from 1 to 2
n
− 1.
To be fair, the first sentence quoted above says “we
estimate
the 2
k
values …” and so the equation above may not be intended as a definition but as motivation for the actual definition.
Reproducing NF4
The authors give a procedure for using 2
n
values of
i
and obtaining an exact representation of 0, and they give a list of NF4 values in Appendix E. I was not able to get the two to match. I implemented a few possible interpretations of the procedure described in the paper, and each approximates the list of values in the appendix, but not closely.
The following code, written with the help of ChatGPT, reverse engineers the NF4 values to 8 decimal places, i.e. to the precision of a 32-bit floating point number.
from scipy.stats import norm

Q = norm.ppf

α  = 0.9677083
Z  = Q(α)
δ1 = (α - 0.5)/7
δ2 = (α - 0.5)/8

q = [0]*16
for i in range(7):
    q[i] = -Q(α - i*δ1)/Z
for i in range(8):
    q[i+8] = Q(0.5 + (i+1)*δ2)/Z
    
# Values given in Appendix E
NF4 = [
    -1.0,
    -0.6961928009986877,
    -0.5250730514526367,
    -0.39491748809814453,
    -0.28444138169288635,
    -0.18477343022823334,
    -0.09105003625154495,
    0.0,
    0.07958029955625534,
    0.16093020141124725,
    0.24611230194568634,
    0.33791524171829224,
    0.44070982933044434,
    0.5626170039176941,
    0.7229568362236023,
    1.0
]

# Compare 
for i in range(16):
    print(i, NF4[i] - q[i])
The magic number α = 0.9677083 is a mystery. I asked ChatGPT to look into this further, and it said that bitsandbytes uses α = 929/960 = 0.9677083333333333. When I use this value for α the precision is about the same, which is fine. However, the values in the paper were given to 16 decimal places, so I thought it might be able to match the values to more precision.
Quibbles over the exact values of NF4 aside, the NF4 format works well in practice. Models. quantized to 4 bits using NF4 perform better than models quantized to other 4-bit formats on some benchmarks.
Related posts
[1] QLoRA: Efficient Finetuning of Quantized LLMs by Tim Dettmers, Artidoro Pagnoni, Ari Holtzman, and Luke Zettlemoyer.
https://arxiv.org/abs/2305.14314
.
