---
title: "New RSA number factored"
url: "https://www.johndcook.com/blog/2026/09/03/new-rsa-number-factored/"
fetched_at: 2026-09-04T10:00:43.497693+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# New RSA number factored

Source: https://www.johndcook.com/blog/2026/09/03/new-rsa-number-factored/

Eric Lu
announced
on X today that he has factored RSA-260, a number
N
with 260 digits (862 bits) that is the product of two large primes [1].
RSA numbers are challenge problems posed to gauge the security of RSA encryption, which rests on the difficulty of factoring large numbers [2]. The naming scheme is confusing because RSA-
n
might have
n
digits or
n
bits. For example, RSA-768 is smaller than RSA-260 because the former has 768 bits and the latter has 260 digits.
RSA-260 is the largest RSA number factored so far. What does the news of its factorization say about the security of RSA?
Based on equations
here
, an RSA key with 862 bits would have a security level of 74 bits, i.e. the same security level as symmetric encryption with a 74-bit key. The minimum recommended RSA key size now is 2048 bits, which has a security level of 107 bits.
Security levels are on a logarithmic scale: each additional bit of security doubles the effort required to break the encryption by brute force. So breaking a 2048-bit RSA key would take 2
34
, roughly 10
10
, times more effort than factoring RSA-260. All this depends on numerous assumptions, such as the state of factorization algorithms and the non-existence of CRQC [3].
Related posts
[1]
N
=
pq
= 22112825529529666435281085255026230927612089502470015394413748319128822941402001986512729726569746599085900330031400051170742204560859276357953757185954298838958709229238491006703034124620545784566413664540684214361293017694020846391065875914794251435144458199
p
= 4397328654844826923795068102505872571721883526553349659561256924505973939597593482272505698004801207988043088656411102133523080581
q
= 5028695206842569864686141618253083416610081090075366674776775706538324961364412200138116378509733307971876652984898985905923678379
[2] The ability to efficiently factor large primes would break RSA. It’s possible that there’s a way to break RSA without being able to factor large numbers. More on that
here
.
[3] Cryptographically-relevant quantum computer. Quantum computers exist, but so far they’re cryptographically irrelevant. So far quantum computers cannot factor 21 without
cheating
.
