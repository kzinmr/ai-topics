---
title: "Rice and Rice-Shapiro theorems."
url: "https://iczelia.net/posts/rice-shapiro/"
fetched_at: 2026-05-05T07:01:20.221420+00:00
source: "Kamila Szewczyk (iczelia)"
tags: [blog, raw]
---

# Rice and Rice-Shapiro theorems.

Source: https://iczelia.net/posts/rice-shapiro/

Programs have semantic and syntactic properties. For example, a syntactic property of a certain program could be that it contains a loop, while a semantic property could be that it halts. A trivial property is satisfied by all programs or none. For example, the property “halts” is non-trivial, as it is satisfied by some programs and not by others. The property “domain has zero or more elements” is trivial, as it is satisfied by all programs. According to Rice’s theorem, non-trivial semantic properties of a program are undecidable. The theorem is named after Henry Gordon Rice, who proved it in his doctoral dissertation of 1951 at Syracuse University.
Suppose that we have a set
A
A
A
of all programs with a particular non-trivial semantic property. We know that there exists a program
t
∈
A
t \in A
t
∈
A
and a program
f
∉
A
f \notin A
f
∈
/
A
. Hence, if
A
A
A
were decidable, there would be a function
h
(
x
)
h(x)
h
(
x
)
which yields
f
f
f
if
x
∈
A
x \in A
x
∈
A
and
t
t
t
if
x
∉
A
x \notin A
x
∈
/
A
. Per Kleene’s recursion theorem, given a function
F
F
F
, a fixed point of
F
F
F
is an index
e
e
e
(in an admissable numbering
φ
\varphi
φ
) such that
φ
e
=
φ
F
(
e
)
\varphi_e = \varphi_{F(e)}
φ
e
​
=
φ
F
(
e
)
​
. Roger’s fixed point theorem states that if
F
F
F
is a total computable function, then it has a fixed point. Now consider the program
e
e
e
. If
e
∈
A
e \in A
e
∈
A
, then
h
(
e
)
=
f
h(e) = f
h
(
e
)
=
f
, and per the fixed point theorem
φ
e
=
φ
F
(
e
)
=
φ
f
\varphi_e = \varphi_{F(e)} = \varphi_f
φ
e
​
=
φ
F
(
e
)
​
=
φ
f
​
. However,
e
∈
A
e \in A
e
∈
A
, but
f
∉
A
f \notin A
f
∈
/
A
- a contradiction. On the contrary, if
e
∉
A
e \notin A
e
∈
/
A
, then
h
(
e
)
=
t
h(e) = t
h
(
e
)
=
t
, and per the fixed point theorem
φ
e
=
φ
F
(
e
)
=
φ
t
\varphi_e = \varphi_{F(e)} = \varphi_t
φ
e
​
=
φ
F
(
e
)
​
=
φ
t
​
. However,
e
∉
A
e \notin A
e
∈
/
A
, but
t
∈
A
t \in A
t
∈
A
- a contradiction again. Therefore,
A
A
A
is undecidable.
A more general version of this claim is the Rice-Shapiro theorem. While Rice’s theorem proves that all non-trivial semantic property is undecidable (i.e. there is no algorithm that can decide whether a program has a certain non-trivial semantic property and halt), the Rice-Shapiro demonstrates that
finitary properties
are recursively enumerable (i.e. there is an algorithm which decides if a program has a property which depends on a finite number of inputs by either accepting or diverging). Formally speaking, the The Rice-Shapiro theorem states that given a recursively enumerable set
A
A
A
which contains the indices of programs with a certain property, then for any program
φ
n
\varphi_n
φ
n
​
,
φ
n
∈
A
\varphi_n \in A
φ
n
​
∈
A
if and only if there exists a finite function
f
⊆
φ
n
f \subseteq \varphi_n
f
⊆
φ
n
​
such that
f
∈
A
f \in A
f
∈
A
.
A more elementary variant of this theorem states that if the set
A
A
A
is recursively enumerable, then for every
g
∈
A
g \in A
g
∈
A
, there is an
j
∈
I
j \in I
j
∈
I
with
dom
(
j
)
⊆
dom
(
g
)
\text{dom}(j) \subseteq \text{dom}(g)
dom
(
j
)
⊆
dom
(
g
)
and
dom
(
j
)
\text{dom}(j)
dom
(
j
)
is finite. The proof of this theorem is more elementary: Suppose there is a function
k
(
x
)
k(x)
k
(
x
)
such that
k
(
x
)
=
1
k(x)=1
k
(
x
)
=
1
if
x
∈
A
x \in A
x
∈
A
and diverges otherwise. Then, by applying the recursion theorem, there is a program
φ
j
(
n
)
=
f
(
j
,
n
)
\varphi_j(n)=f(j,n)
φ
j
​
(
n
)
=
f
(
j
,
n
)
such that
f
f
f
computes
g
(
n
)
g(n)
g
(
n
)
if
k
(
j
)
k(j)
k
(
j
)
takes more than
n
n
n
steps to halt. Then, if
φ
j
∉
A
\varphi_j \notin A
φ
j
​
∈
/
A
, then then
k
(
j
)
k(j)
k
(
j
)
diverges and
f
(
j
,
n
)
=
g
(
n
)
f(j,n)=g(n)
f
(
j
,
n
)
=
g
(
n
)
for all
n
n
n
, but
g
∈
A
g \in A
g
∈
A
- contradiction. On the other hand, if
φ
j
∈
A
\varphi_j \in A
φ
j
​
∈
A
, then
k
(
j
)
=
1
k(j)=1
k
(
j
)
=
1
and
f
(
j
,
n
)
f(j,n)
f
(
j
,
n
)
is defined for finitely many
n
n
n
, hence
dom
(
j
)
\text{dom}(j)
dom
(
j
)
is finite. If
φ
j
(
n
)
\varphi_j(n)
φ
j
​
(
n
)
is defined, then
φ
j
(
n
)
=
g
(
n
)
\varphi_j(n) = g(n)
φ
j
​
(
n
)
=
g
(
n
)
, and
dom
(
φ
j
)
\text{dom}(\varphi_j)
dom
(
φ
j
​
)
is a finite subset of
dom
(
g
)
\text{dom}(g)
dom
(
g
)
.
A corollary of this result is that if
Ω
\Omega
Ω
is an always-diverging program, then
Ω
∈
A
\Omega \in A
Ω
∈
A
implies that
H
ˉ
≤
A
\bar H \le A
H
ˉ
≤
A
, and further if
Ω
∉
A
\Omega \notin A
Ω
∈
/
A
, then
H
≤
A
H \le A
H
≤
A
, where
H
H
H
is the set of tuples of programs and inputs on which they halt.
