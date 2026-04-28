---
title: "Toffoli gates are all you need"
url: "https://www.johndcook.com/blog/2026/04/06/tofolli-gates/"
fetched_at: 2026-04-28T07:02:47.439082+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Toffoli gates are all you need

Source: https://www.johndcook.com/blog/2026/04/06/tofolli-gates/

Landauer’s principle gives a lower bound on the amount of energy it takes to erase one bit of information:
E
≥ log(2)
k
B
T
where
k
B
is the Boltzmann constant and
T
is the ambient temperature in Kelvin. The lower bound applies no matter how the bit is physically stored. There is no theoretical lower limit on the energy required to carry out a reversible calculation.
In practice the energy required to erase a bit is around a billion times greater than Landauer’s lower bound. You might reasonably conclude that reversible computing isn’t practical since we’re nowhere near the Landauer limit. And yet in practice reversible circuits have been demonstrated to use less energy than conventional circuits. We’re far from the ultimate physical limit, but reversibility still provides practical efficiency gains today.
A Toffoli gate is a building block of reversible circuits. A Toffoli gate takes three bits as input and returns three bits as output:
T
(
a
,
b
,
c
) = (
a
,
b
,
c
XOR (
a
AND
b
)).
In words, a Toffoli gate flips its third bit if and only if the first two bits are ones.
A Toffoli gate is its own inverse, and so it is reversible. This is easy to prove. If
a
=
b
= 1, then the third bit is flipped. Apply the Toffoli gate again flips the bit back to what it was. If
ab
= 0, i.e. at least one of the first two bits is zero, then the Toffoli gate doesn’t change anything.
There is a theorem that any Boolean function can be computed by a circuit made of only NAND gates. We’ll show that you can construct a NAND gate out of Toffoli gates, which shows any Boolean function can be computed by a circuit made of Toffoli gates, which shows any Boolean function can be computed reversibly.
To compute NAND, i.e. ¬ (
a
∧
b
), send (
a
,
b
, 1) to the Toffoli gate. The third bit of the output will contain the NAND of
a
and
b
.
T
(a, b
, 1) = (
a
,
b
, ¬ (
a
∧
b
))
A drawback of reversible computing is that you may have to send in more input than you’d like and get back more output than you’d like, as we can already see from the example above. NAND takes two input bits and returns one output bit. But the Toffoli gate simulating NAND takes three input bits and returns three output bits.
Related posts
