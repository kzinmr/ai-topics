---
title: "Backdoors, Incompetence, and Elliptic Curves"
url: "https://www.johndcook.com/blog/2026/10/21/emudhra/"
fetched_at: 2026-10-22T10:01:03.064244+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Backdoors, Incompetence, and Elliptic Curves

Source: https://www.johndcook.com/blog/2026/10/21/emudhra/

The NIST elliptic curves have been in the news twice lately. A few days ago Anthropic posted a paper on the NIST curve seeds that I wrote about
here
. Now the curves are in the news again, this time over broken certificates.
My post a few days ago was about the possibility that the NSA had added a backdoor to the NIST curves. Anthropic researchers showed that this wasn’t the case. The NSA had not been able to defend how the curve seeds were chosen because they forgot, but researchers from Anthropic were able to reverse engineer the source of the seeds.
So apparently the NIST curves do not have a backdoor, but as with all encryption, the Achilles heel is human error. eMudrha was using the NIST curve
P-384
with extremely small keys: 4, 56, 115, 155, 156, 230, and 237. To understand why this is a problem, I’ll briefly describe how elliptic curve cryptography works.
P-384 is an elliptic curve designed by NIST, with input from the NSA, for use in cryptography. The curve has on the order of 2
384
points because the base field is the integers mod
p
= 2
384
− 2
128
− 2
96
+ 2
32
− 1,
a 384-bit prime number. Given a basepoint
b
on the curve and an exponent
e
, it is practically impossible to recover
e
from
b
e
. That’s the discrete logarithm problem [1], the basis for the security of elliptic curve cryptography. If and when cryptographically relevant quantum computers arrive, the discrete logarithm problem will be solvable and elliptic curve cryptography will be broken.
Until the advent of quantum computing, elliptic curve cryptography is presumably safe, unless someone does something negligent, such as using a tiny value of
e
like 4.
If
e
is chosen at random from a group with on the order of 2
384
elements, you cannot recover
e
from
b
e
without brute force. But apparently someone said
Let’s see. Is
e
= 1? Is it 2? Is it 3? Is it 4? Why yes:
e
= 4.
Ordinarily this would be hopeless. You can’t just try 2
384
exponents. But someone thought to test whether the keys were horrifically bad, and they were right.
[1] The exponentiation here is not over the integers, or over the integers mod
p
. It’s over the group structure of the elliptic curve, and that is what makes it hard to compute the discrete logarithm.
