---
title: "A Survey of Results on the Blum-Blum-Shub Pseudorandom Number Generator"
url: "https://iczelia.net/posts/bbs-survey/"
fetched_at: 2026-05-05T07:01:19.517220+00:00
source: "Kamila Szewczyk (iczelia)"
tags: [blog, raw]
---

# A Survey of Results on the Blum-Blum-Shub Pseudorandom Number Generator

Source: https://iczelia.net/posts/bbs-survey/

Introduction.
⌗
Blum-Blum-Shub (henceforth referred to as BBS) is a pseudorandom number generator uniquely based on the difficulty of factoring large composite numbers. It was introduced by Lenore Blum, Manuel Blum, and Michael Shub in 1986. It is notable for its so-called
provable security under certain assumptions
, luring many cryptographers to study it.
Let
M
=
p
q
M = pq
M
=
pq
where
p
p
p
and
q
q
q
are two distinct large primes. The internal state step function is given by:
x
n
+
1
=
x
n
2
m
o
d
M
x_{n+1} = x_n^2 \mod M
x
n
+
1
​
=
x
n
2
​
mod
M
With
x
0
x_0
x
0
​
being a random seed coprime to
M
M
M
and greater than one. The following requirements are placed on
p
p
p
and
q
q
q
:
They should be Sophie Germain primes, i.e. both
2
p
+
1
2p + 1
2
p
+
1
and
2
q
+
1
2q + 1
2
q
+
1
are also prime.
They should be congruent to 3 modulo 4, i.e.
p
≡
3
m
o
d
4
p \equiv 3 \mod 4
p
≡
3
mod
4
and
q
≡
3
m
o
d
4
q \equiv 3 \mod 4
q
≡
3
mod
4
.
gcd
⁡
(
(
p
−
3
)
/
2
,
(
q
−
3
)
/
2
)
\gcd((p-3)/2, (q-3)/2)
g
cd
((
p
−
3
)
/2
,
(
q
−
3
)
/2
)
should be as small as possible, ideally 1.
The random bits are extracted from the internal state at each step. The amount of bits extracted provides a trade-off between speed and security. The most common extraction method is to take the least significant bit of the internal state, but more bits can be extracted at once.
Quadratic residues.
⌗
We will start with some preliminary definitions and theorems concerning number-theoretic basis of BBS.
Definition 1.
An integer
x
∈
Z
n
∗
x \in \mathbb{Z}_n^*
x
∈
Z
n
∗
​
is called a
quadratic residue modulo
n
n
n
if
there exists some
y
y
y
such that
y
2
m
o
d
n
=
x
y^2 \bmod n = x
y
2
mod
n
=
x
.
Definition 2.
The Jacobi symbol
(
a
n
)
\left( \frac{a}{n} \right)
(
n
a
​
)
is defined as follows:
(
a
n
)
=
{
1
if
a
is a quadratic residue modulo
n
and
a
≢
0
m
o
d
n
,
−
1
if
a
is not a quadratic residue modulo
n
,
0
if
a
≡
0
m
o
d
n
.
\left( \frac{a}{n} \right) = \begin{cases}
1 & \text{if } a \text{ is a quadratic residue modulo } n \text{ and } a \not\equiv 0 \mod n, \\
-1 & \text{if } a \text{ is not a quadratic residue modulo } n, \\
0 & \text{if } a \equiv 0 \mod n.
\end{cases}
(
n
a
​
)
=
⎩
⎨
⎧
​
1
−
1
0
​
if
a
is a quadratic residue modulo
n
and
a

≡
0
mod
n
,
if
a
is not a quadratic residue modulo
n
,
if
a
≡
0
mod
n
.
​
Definition 3.
Consider
n
=
p
q
n = pq
n
=
pq
like in the BBS generator.
Z
n
∗
\mathbb{Z}_n^*
Z
n
∗
​
is then partitioned into two sets of equal cardinality -
Z
n
∗
,
−
1
\mathbb{Z}_n^{*,-1}
Z
n
∗
,
−
1
​
and
Z
n
∗
,
1
\mathbb{Z}_n^{*,1}
Z
n
∗
,
1
​
where
Z
n
∗
,
y
=
{
a
∈
Z
n
∗
∣
(
a
n
)
=
y
}
\mathbb{Z}_n^{*,y} = \{a \in \mathbb{Z}_n^* \mid \left( \frac{a}{n} \right) = y\}
Z
n
∗
,
y
​
=
{
a
∈
Z
n
∗
​
∣
(
n
a
​
)
=
y
}
. Logically, none of the elements in
Z
n
∗
,
1
\mathbb{Z}_n^{*,1}
Z
n
∗
,
1
​
are quadratic residues modulo
n
n
n
and exactly half of the elements in
Z
n
∗
,
−
1
\mathbb{Z}_n^{*,-1}
Z
n
∗
,
−
1
​
are quadratic residues modulo
n
n
n
.
Definition 4.
A solution to the quadratic residuosity problem (QRP) decides whether some
x
∈
Z
n
∗
,
1
x \in \mathbb{Z}_n^{*,1}
x
∈
Z
n
∗
,
1
​
is a quadratic residue modulo
n
n
n
.
Theorem 5.
An unproven but considered by researchers highly likely assumption is that any PPT (probabilistic polynomial-time) algorithm that solves the QRP has the probability of success at most
1
/
2
+
ε
1/2 + \varepsilon
1/2
+
ε
, where
ε
\varepsilon
ε
is small and in
O
(
log
⁡
n
)
O(\log n)
O
(
lo
g
n
)
.
Many known partial solutions to the QRP orbit around prime factorisation of
n
n
n
. In particular, quadratic residuosity is efficient to check for prime
n
n
n
, and a number is a quadratic residue modulo
n
n
n
if it’s a quadratic residue modulo every prime factor of
n
n
n
. The practical implication of this is that the factorisation of
n
n
n
can not be known by an adversary. More generally, finding hard to factor semiprimes is a well-known problem in RSA.
This leads many researchers to believe that QRP and prime factorisation are mostly interchangeable in that efficient factorisation of
n
n
n
implies efficient solution to the QRP. Indeed, the most efficient known algorithm for solving the QRP is based on factorisation, but formally speaking an efficient solution to the QRP does not need to imply efficient factorisation of
n
n
n
.
Digging deeper, there is also no proof of the statement that factorization is hard - albeit millenia of research have not yet come up with an efficient factorization method, so it must not be trivial. Accordingly, the security status of BBS is similar to that of RSA.
Circling back.
⌗
Let’s discuss how this connects to BBS.
In the specific case of BBS, we have concrete evidence that the assumption of hardness of QRP can be equivalently replaced by the assumption of hardness of factorisation. This was proven by W. B. Alexi, B. Chor, O. Goldreich, and C. P. Schnorr.
RSA/Rabin functions: certain parts are as hard as the whole.
in SIAM J. Computing, 17(2):194-209, April 1988.
The reduction in Blum, Blum, Shub (1986) proceeds by demonstrating that, if there is a PPT algorithm that operates backwards on the BBS generator (i.e. after observing some consecutive outputs of the generator, it can predict the output preceding them) with a specific probability, then there is also a PPT algorithm that solves the QRP with the same probability.
The original construction assumes that we extract the lowest order bit of the internal state at each step, but it can be generalized to extract more bits at once. Specifically, U.V. Vazirani and V.V. Vazirani,
Efficient And Secure Pseudo-Random Number Generation
in 25th Annual Symposium on Foundations of Computer Science, 1984, showed that we can securely extract
O
(
log
⁡
log
⁡
M
)
\mathcal O(\log \log M)
O
(
lo
g
lo
g
M
)
bits at each step.
The generator can be seeked around to any position using Carmichael’s function of M, which degenerates to
(
p
−
1
)
(
q
−
1
)
/
g
c
d
(
p
−
1
,
q
−
1
)
(p - 1)(q - 1) / gcd(p - 1, q - 1)
(
p
−
1
)
(
q
−
1
)
/
g
c
d
(
p
−
1
,
q
−
1
)
via Euler’s theorem, stating that
f
(
i
)
=
f
(
0
)
(
2
i
m
o
d
Carmichael
(
M
)
)
m
o
d
M
f(i) = f(0)^{\left(2^i \bmod \text{Carmichael}(M)\right)} \bmod M
f
(
i
)
=
f
(
0
)
(
2
i
mod
Carmichael
(
M
)
)
mod
M
A concrete (non-asymptotic) proof of correctness is given by A. Sidorenko and B. Schoenmakers,
Concrete Security of the Blum-Blum-Shub Pseudorandom Generator
. Cryptography and Coding. They claim:
Theorem.
Suppose the BBS pseudorandom generator extracting
j
j
j
bits at a time is not
(
T
A
,
ε
)
(T_A, \varepsilon)
(
T
A
​
,
ε
)
-secure. Then there exists an algorithm
F
F
F
that factors the modulus
N
N
N
in expected time
T
F
≤
36
n
(
log
⁡
2
n
)
δ
−
2
(
T
A
+
2
2
j
+
9
n
δ
−
4
)
T_F \leq 36n (\log_2 n) \delta^{-2} (T_A + 2^{2j + 9} n \delta^{-4})
T
F
​
≤
36
n
(
lo
g
2
​
n
)
δ
−
2
(
T
A
​
+
2
2
j
+
9
n
δ
−
4
)
where
δ
=
(
2
j
−
1
)
−
1
M
−
1
ε
\delta = (2^j - 1)^{-1} M^{-1} \varepsilon
δ
=
(
2
j
−
1
)
−
1
M
−
1
ε
.
Moving on to factoring, the most efficient known algorithm is the General Number Field Sieve (GNFS), which has a sub-exponential complexity proportional to:
R
∼
γ
exp
⁡
(
(
1.9229
+
o
(
1
)
)
(
ln
⁡
N
)
1
/
3
(
ln
⁡
ln
⁡
N
)
2
/
3
)
R \sim \gamma \exp\left((1.9229 + o(1))(\ln N)^{1/3}(\ln \ln N)^{2/3}\right)
R
∼
γ
exp
(
(
1.9229
+
o
(
1
))
(
ln
N
)
1/3
(
ln
ln
N
)
2/3
)
The authors thus approximate the number of clock cycles required to factor an
n
n
n
-bit integer as:
L
(
n
)
≈
2.8
⋅
1
0
−
3
⋅
exp
⁡
(
1.9229
(
n
ln
⁡
2
)
1
/
3
(
ln
⁡
(
n
ln
⁡
2
)
)
2
/
3
)
L(n) \approx 2.8 \cdot 10^{-3} \cdot \exp\left(1.9229(n \ln 2)^{1/3}(\ln(n \ln 2))^{2/3}\right)
L
(
n
)
≈
2.8
⋅
1
0
−
3
⋅
exp
(
1.9229
(
n
ln
2
)
1/3
(
ln
(
n
ln
2
)
)
2/3
)
Under the assumption that no algorithm can factor an
n
n
n
-bit Blum prime in less than
L
(
n
)
L(n)
L
(
n
)
clock cycles, the BBS generator is
(
T
A
,
ε
)
(T_A, \varepsilon)
(
T
A
​
,
ε
)
-secure if:
T
A
≤
L
(
n
)
36
n
(
log
⁡
2
n
)
δ
−
2
−
2
2
j
+
9
n
δ
−
4
T_A \leq \frac{L(n)}{36n (\log_2 n) \delta^{-2}} - 2^{2j + 9} n \delta^{-4}
T
A
​
≤
36
n
(
lo
g
2
​
n
)
δ
−
2
L
(
n
)
​
−
2
2
j
+
9
n
δ
−
4
where
δ
=
(
2
j
−
1
)
−
1
M
−
1
ε
\delta = (2^j - 1)^{-1} M^{-1} \varepsilon
δ
=
(
2
j
−
1
)
−
1
M
−
1
ε
.
The paper demonstrates a practical application of this result: If we take
M
=
2
20
M = 2^{20}
M
=
2
20
outputs, bound
T
A
T_A
T
A
​
to
2
100
2^{100}
2
100
clock cycles and
ε
=
1
/
2
\varepsilon = 1/2
ε
=
1/2
. Then, the recommended amount of bits of security is
n
=
6800
n = 6800
n
=
6800
, while the amount of bits extracted at each step is
j
=
5
j = 5
j
=
5
.
Another result is given by S. Chatterjee, A. Menezes, and P. Sarkar
Another Look at Tightness
, where they demonstrate that some common exceedingly-liberal choices of
n
n
n
and
j
j
j
(in that case
n
=
768
n=768
n
=
768
and
j
=
9
j=9
j
=
9
) lead to lack of tangible security and dismantle the proof. This is however due to the fact that
j
j
j
is way too large, and the double-log bound for
n
=
768
n=768
n
=
768
is at most
j
=
2
j=2
j
=
2
or
j
=
3
j=3
j
=
3
.
Security implications.
⌗
It is generally assumed that
p
p
p
and
q
q
q
(and thus
M
M
M
) remain secret. Further, it is assumed that
x
0
x_0
x
0
​
is secret and similar in magnitude to
M
M
M
.
If
p
p
p
and
q
q
q
become public, we can create a seekable generator per the formula from the introductory section, as the Carmichael function of
M
M
M
can now be feasibly computed. Further, we can approximate the period of the generator and produce a suitable distinguisher.
On the other hand, retaining
p
p
p
and
q
q
q
offers a performance improvement on the side of a legitimate generator. In this case, we observe that finding roots modulo
M
M
M
, in general, is difficult. However, if
p
p
p
and
q
q
q
are known, we can compute the roots modulo
p
p
p
and
q
q
q
separately, and then combine them using the Chinese Remainder Theorem, resulting in three
n
n
n
-bit multiplications rather than a
2
n
2n
2
n
-bit multiplication.
For a concrete exposition of how to do this, consider:
x
p
=
x
n
m
o
d
p
,
x
q
=
x
n
m
o
d
q
,
x_p = x_n \mod p,\quad x_q = x_n \mod q,
x
p
​
=
x
n
​
mod
p
,
x
q
​
=
x
n
​
mod
q
,
x
p
’
=
x
p
2
m
o
d
p
,
x
q
’
=
x
q
2
m
o
d
q
.
x_p’ = x_p^2 \mod p,\quad x_q’ = x_q^2 \mod q.
x
p
​
’
=
x
p
2
​
mod
p
,
x
q
​
’
=
x
q
2
​
mod
q
.
These squarings are faster because
p
p
p
and
q
q
q
are each roughly half the bit-length of
M
M
M
.
We reconstruct
x
n
+
1
m
o
d
M
x_{n+1} \mod M
x
n
+
1
​
mod
M
using:
M
=
p
q
,
M
p
=
q
,
M
q
=
p
,
M = pq,\quad M_p = q,\quad M_q = p,
M
=
pq
,
M
p
​
=
q
,
M
q
​
=
p
,
y
p
=
q
−
1
m
o
d
p
,
y
q
=
p
−
1
m
o
d
q
.
y_p = q^{-1} \mod p,\quad y_q = p^{-1} \mod q.
y
p
​
=
q
−
1
mod
p
,
y
q
​
=
p
−
1
mod
q
.
Then, the CRT gives:
x
n
+
1
=
(
x
p
’
⋅
q
⋅
y
p
+
x
q
’
⋅
p
⋅
y
q
)
m
o
d
M
.
x_{n+1} = (x_p’ \cdot q \cdot y_p + x_q’ \cdot p \cdot y_q) \mod M.
x
n
+
1
​
=
(
x
p
​
’
⋅
q
⋅
y
p
​
+
x
q
​
’
⋅
p
⋅
y
q
​
)
mod
M
.
Specifically,
y
p
y_p
y
p
​
and
y
q
y_q
y
q
​
can be cached as they are constant for a given
M
M
M
. The computation usually proceeds via the EEA.
Toy experiments.
⌗
We can begin by taking the two primes for granted and subsequently computing
n
=
p
q
n=pq
n
=
pq
.
Then, we can precompute the CRT constants, which is particularly easy in Python:
C implementation.
⌗
A fully-featured C implementation of the BBS generator is more involved. In this article we will primarily cover the
cbbs-rng
implementation produced by the author of this article.
The generator supports OpenMP parallelisation for faster generation of the starting state. Some preliminary feature detection code follows:
Most importantly, we use the new C23 feature -
_BitInt
- to define bit integers of arbitrary size. This allows us to work with large numbers without worrying about overflow or performance penalty as accurred with
gmp
. The values of
p
p
p
,
q
q
q
and
x
0
x_0
x
0
​
must come from a cryptographically secure source, such as
/dev/urandom
on Linux or
CryptGenRandom
on Windows:
For primality testing we use generally use the Miller-Rabin test. However, for the sake of performance, we will perform some rudimentary trial division first to weed out the obvious non-primes. This is however not as simple as it may seem: trial divisions of large numbers are excruciatingly slow.
In the cbbs-rng implementation, we use a common trick in cryptography and data compression called the Barrett Reduction. Long story short, we can replace a division by a multiplication with a shift. For pre-generating the table of small primes, we use the Sieve of Atkin.
The Miller-Rabin test is then implemented as follows with a variable amount of iterations:
Nominally, the inner loop computing
x
:
=
x
2
m
o
d
n
x := x^2 \mod n
x
:=
x
2
mod
n
could also use Barrett reductions for improved performance, but the author observed that it is not particularly beneficial in practice.
All these components build up to the main part of our BBS generator which computes the parameters
p
p
p
and
q
q
q
under the condition that they are Sophie Germain primes and Blum integers.
The
gcd
⁡
\gcd
g
cd
function will be necessary to compute the period of the generator. An efficient algorithm for that is given by Stein and implemented below:
Finally, the state of the BBS generator itself is represented, initialised and seeked as follows:
Simply advancing the generator is performed by the following procedures:
A parallel version of the generator can be implemented to slightly alleviate its slowness:
Via the CLI stub we can both do some rudimentary checks and generate some pseudo-random numbers. Alternatively, we can also test the output so that it can be fed into a statistical test suite such as the NIST SP 800-22 or Diehard tests:
Miscellaneous results.
⌗
The period of the BBS generator is strictly tied to the Carmichael function. BBS is ultimately periodic with period
λ
(
λ
(
n
)
)
\lambda(\lambda(n))
λ
(
λ
(
n
))
. Hence minimising
gcd
⁡
(
(
p
−
3
)
/
2
,
(
q
−
3
)
/
2
)
\gcd((p-3)/2, (q-3)/2)
g
cd
((
p
−
3
)
/2
,
(
q
−
3
)
/2
)
is crucial for security, as it maximises
λ
(
n
)
\lambda(n)
λ
(
n
)
, which in turn tends to maximise
λ
(
λ
(
n
)
)
\lambda(\lambda(n))
λ
(
λ
(
n
))
.
The existence of one-way functions is equivalent to the existence of pseudorandom generators that pass all polynomial-time statistical tests. The proof of this is given by J. Hastad, R. Impagliazzo, L. Levin, and M. Luby.
A Pseudorandom Generator from any One-way Function
in SIAM J. Computing, 28(4):1364-1396, April 1999.
The so-called proof of security is rather misleading - its practical consequences are not as significant as it may seem. Most importantly, dated literature about BBS tends to underestimate the magnitude of the parameters to the generator. The magnitude of 6800 bits in the modulus results in extremely slow generation of pseudo-random numbers.
The generator is very slow. For
n
=
512
n=512
n
=
512
in parallel mode, we generate only about 2.65MB/s of random data.
n
=
1024
n=1024
n
=
1024
yields a more depressing figure of 721.6kB/s. Predictably, the functions
__divmodbitint4
and
__mulbitint3
constitute the majority of the runtime (>95%) with an equal proportion between them. Future improvements could involve the use of the Chinese Remainder Theorem for faster computation. Operation in the Montgomery domain could also be evaluated. The author hopes that future releases of GCC ship a
__mulbitint3
function that is not quadratic but perhaps uses Karatsuba or such.
An simple implementation using GMP (and thus is not constant-time, and is more vulnerable to side-channel attacks) put together by the author at hand can accomplish the rate of about 3.1MB/s for
n
=
1024
n=1024
n
=
1024
. The author is interested in investigating this as a future project and specialising the parts of the GMP responsible for the speedup for the BBS generator.
