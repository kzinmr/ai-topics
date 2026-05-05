---
title: "A no-bullshit introduction to groups: Part 1."
url: "https://iczelia.net/posts/groups/"
fetched_at: 2026-05-05T07:01:18.984656+00:00
source: "Kamila Szewczyk (iczelia)"
tags: [blog, raw]
---

# A no-bullshit introduction to groups: Part 1.

Source: https://iczelia.net/posts/groups/

Many years ago, back when I was in my early teens, I picked up an interest in math. Arguably much more superficial than it is now. My gateway drug to discovering abstract algebra was a YouTube video about the unsolvability of the quintic.
Of course, I didn’t understand shit after watching it. I think that I got lost somewhere midway the video, where the author decided that the best idea is to keep on with the “graphical” and “friendly” explanation of groups by rotating cubes or balls, and explained the rest of the concepts in this insurmountably confusing and pointless way. It must’ve sucked to be me, because every exposition of basic group theory was either that, or needless complexity galore that required much more mathematical maturity than a 13 year old could’ve spared.
When I was procrastinating working, now - give or take - 8 years later, I saw another pointless rehashing of the same topic in the same pointless logical framework. So I thought that maybe I can do a better job.
What is a group?
⌗
Suppose that you have a set. Of anything, really - potatoes, dodgeballs, whatever. Actually, who am I lying to? Just take non-negative integers smaller than 4. Call it
G
G
G
.
Now suppose that you have an action (for potatoes it could be mashing, for dodgeballs -
this
, for integers - addition modulo 4) that you can perform on any two elements of that set, and that action (call it
⋅
\cdot
⋅
- like the product operator) has the following properties:
(
a
⋅
b
)
⋅
c
=
a
⋅
(
b
⋅
c
)
(a \cdot b) \cdot c = a \cdot (b \cdot c)
(
a
⋅
b
)
⋅
c
=
a
⋅
(
b
⋅
c
)
for any
a
,
b
,
c
∈
G
a, b, c \in G
a
,
b
,
c
∈
G
(associativity).
There exists an element
ε
∈
G
\varepsilon \in G
ε
∈
G
such that for any
a
∈
G
a \in G
a
∈
G
,
ε
⋅
a
=
a
⋅
ε
=
a
\varepsilon \cdot a = a \cdot \varepsilon = a
ε
⋅
a
=
a
⋅
ε
=
a
(identity element).
For any
a
∈
G
a \in G
a
∈
G
, there exists an element
b
∈
G
b \in G
b
∈
G
such that
a
⋅
b
=
b
⋅
a
=
ε
a \cdot b = b \cdot a = \varepsilon
a
⋅
b
=
b
⋅
a
=
ε
(inverse element).
From here it should also be clear that
(
⋅
)
:
G
×
G
→
G
(\cdot) : G \times G \to G
(
⋅
)
:
G
×
G
→
G
(closure; i.e.
(
⋅
)
(\cdot)
(
⋅
)
maps two elements of
G
G
G
to another element of
G
G
G
). Then the pair
(
G
,
⋅
)
(G, \cdot)
(
G
,
⋅
)
is called a
group
.
So in our example,
G
=
0
,
1
,
2
,
3
G = {0, 1, 2, 3}
G
=
0
,
1
,
2
,
3
and
(
⋅
)
(\cdot)
(
⋅
)
is addition modulo 4. The identity element is 0, because adding 0 to any number doesn’t change it. The inverse of 1 is 3, because
1
+
3
≡
0
m
o
d
4
1 + 3 \equiv 0 \bmod 4
1
+
3
≡
0
mod
4
; the inverse of 2 is 2, because
2
+
2
≡
0
m
o
d
4
2 + 2 \equiv 0 \bmod 4
2
+
2
≡
0
mod
4
; and the inverse of 3 is 1.
So here we discover one of the most straightforward families of groups: integers modulo
n
n
n
form a group. Formally speaking,
Z
n
=
(
0
,
1
,
…
,
n
−
1
,
+
m
o
d
n
)
\mathbb{Z}_n = ({0, 1, \ldots, n-1}, +_{\bmod n})
Z
n
​
=
(
0
,
1
,
…
,
n
−
1
,
+
mod
n
​
)
is a group for any integer
n
≥
1
n \geq 1
n
≥
1
.
What is this useful for? You could model a hand of a clock with it, for example. What happens when an analog clock shows 10:35 a.m. and you add 50 minutes to it? It shows 11:25 a.m. In other words,
35
+
50
≡
25
m
o
d
60
35 + 50 \equiv 25 \bmod 60
35
+
50
≡
25
mod
60
.
Simplest example of a group is when we set
G
=
ε
G = { \varepsilon }
G
=
ε
, a set with a single element, and define
(
⋅
)
(\cdot)
(
⋅
)
such that
ε
⋅
ε
=
ε
\varepsilon \cdot \varepsilon = \varepsilon
ε
⋅
ε
=
ε
. This group is called the
trivial group
.
Exercise: It easily follows that
(
Z
,
+
)
(\mathbb{Z}, +)
(
Z
,
+
)
is a group. Is
(
Z
,
−
)
(\mathbb{Z}, -)
(
Z
,
−
)
a group? Don’t skim over this. Try to informally prove or disprove it. Would this construction violate any of the group properties?
Bijections and the group of bijections.
⌗
A bijection is essentially a function that maps elements from one set to another in a one-to-one manner. In other words, no two elements from the first set map to the same element in the second set, and every element in the second set has a corresponding element in the first set.
For example, we can define a bijection between
N
\mathbb{N}
N
and
Z
\mathbb{Z}
Z
as follows:
f
(
n
)
=
{
n
2
,
if
n
is even
−
n
+
1
2
,
if
n
is odd
f(n) = \begin{cases}
\frac{n}{2}, & \text{if } n \text{ is even} \
-\frac{n+1}{2}, & \text{if } n \text{ is odd}
\end{cases}
f
(
n
)
=
{
2
n
​
,
​
if
n
is even
−
2
n
+
1
​
,
​
if
n
is odd
​
We see that
f
:
N
→
Z
f : \mathbb{N} \to \mathbb{Z}
f
:
N
→
Z
is a bijection, because every natural number maps to a unique integer, and every integer has a corresponding natural number. We can also invert this mapping to get
f
−
1
:
Z
→
N
f^{-1} : \mathbb{Z} \to \mathbb{N}
f
−
1
:
Z
→
N
.
As another example, we can define a bijection that maps natural numbers to even natural numbers as
f
(
n
)
=
2
n
f(n) = 2n
f
(
n
)
=
2
n
. Detour: It may seem a bit illogical: after all, aren’t there more natural numbers than even natural numbers? Infinite sets are a bit tricky to reason about. In mathematics we would say that both sets have the same
cardinality
(because there is a bijection between them), but they have a different
density
(because even natural numbers are less frequent in the set of natural numbers).
Now, let’s take our newfound group powers. The group
Bij
(
X
)
\text{Bij}(X)
Bij
(
X
)
is the group of all bijections from a set to itself, with the group operation being function composition. So
f
∈
Bij
(
X
)
:
X
→
X
f \in \text{Bij}(X) : X \to X
f
∈
Bij
(
X
)
:
X
→
X
for some set
X
X
X
, and the group operation
∘
\circ
∘
is defined as
(
f
∘
g
)
(
x
)
=
f
(
g
(
x
)
)
(f \circ g)(x) = f(g(x))
(
f
∘
g
)
(
x
)
=
f
(
g
(
x
))
for any
f
,
g
∈
Bij
(
X
)
f, g \in \text{Bij}(X)
f
,
g
∈
Bij
(
X
)
and
x
∈
X
x \in X
x
∈
X
.
Is this actually a group? Well, go and check: the function composition is associative, the identity function
i
d
(
x
)
=
x
\mathrm{id}(x) = x
id
(
x
)
=
x
serves as the identity element, and every bijection has an inverse function that is also a bijection. Furthermore, if
f
,
g
f, g
f
,
g
are bijections then so is
f
∘
g
f \circ g
f
∘
g
, so the closure property holds as well.
How to demonstrate this formally, axiom by axiom:
Axiom 1: Notice that for any functions
f
,
g
,
h
:
X
→
X
f,g,h:X\to X
f
,
g
,
h
:
X
→
X
and any
x
∈
X
x\in X
x
∈
X
, we have:
(
(
f
∘
g
)
∘
h
)
(
x
)
=
(
f
∘
g
)
(
h
(
x
)
)
=
f
(
g
(
h
(
x
)
)
)
=
f
(
(
g
∘
h
)
(
x
)
)
=
(
f
∘
(
g
∘
h
)
)
(
x
)
.
((f\circ g)\circ h)(x)=(f\circ g)(h(x))=f(g(h(x)))=f((g\circ h)(x))=(f\circ (g\circ h))(x).
((
f
∘
g
)
∘
h
)
(
x
)
=
(
f
∘
g
)
(
h
(
x
))
=
f
(
g
(
h
(
x
)))
=
f
((
g
∘
h
)
(
x
))
=
(
f
∘
(
g
∘
h
))
(
x
)
.
.
Since the two compositions agree on every
x
∈
X
x\in X
x
∈
X
,
(
f
∘
g
)
∘
h
=
f
∘
(
g
∘
h
)
(f\circ g)\circ h=f\circ (g\circ h)
(
f
∘
g
)
∘
h
=
f
∘
(
g
∘
h
)
. So (more generally) composition is associative on the set of all functions from
X
X
X
to
X
X
X
.
Axiom 2: Define
i
d
X
:
X
→
X
\mathrm{id}_X:X\to X
id
X
​
:
X
→
X
by
i
d
X
(
x
)
=
x
\mathrm{id}_X(x)=x
id
X
​
(
x
)
=
x
. This map is bijective. For any bijective
f
f
f
and any
x
∈
X
x\in X
x
∈
X
, we have
(
i
d
X
∘
f
)
(
x
)
=
i
d
X
(
f
(
x
)
)
=
f
(
x
)
,
(
f
∘
i
d
X
)
(
x
)
=
f
(
i
d
X
(
x
)
)
=
f
(
x
)
.
(\mathrm{id}_X\circ f)(x)=\mathrm{id}_X(f(x))=f(x),\quad (f\circ \mathrm{id}_X)(x)=f(\mathrm{id}_X(x))=f(x).
(
id
X
​
∘
f
)
(
x
)
=
id
X
​
(
f
(
x
))
=
f
(
x
)
,
(
f
∘
id
X
​
)
(
x
)
=
f
(
id
X
​
(
x
))
=
f
(
x
)
.
Hence
(
i
d
X
)
(\mathrm{id}_X)
(
id
X
​
)
is an identity element.
Axiom 3: Let
f
f
f
be a bijection. For each
y
∈
X
y \in X
y
∈
X
there exists a
unique
x
∈
X
x \in X
x
∈
X
with
f
(
x
)
=
y
f(x) = y
f
(
x
)
=
y
. Define
f
−
1
:
X
→
X
f^{-1}: X \to X
f
−
1
:
X
→
X
by “
f
−
1
(
y
)
=
f^{-1}(y) =
f
−
1
(
y
)
=
the unique
x
x
x
such that
f
(
x
)
=
y
f(x) = y
f
(
x
)
=
y
”. This is a well-defined function. Then for any
x
∈
X
x \in X
x
∈
X
,
f
−
1
(
f
(
x
)
)
=
x
f^{-1}(f(x)) = x
f
−
1
(
f
(
x
))
=
x
, so
(
f
−
1
∘
f
)
(
x
)
=
x
(f^{-1} \circ f)(x) = x
(
f
−
1
∘
f
)
(
x
)
=
x
, i.e.
f
−
1
∘
f
=
i
d
X
f^{-1} \circ f = \mathrm{id}_X
f
−
1
∘
f
=
id
X
​
. For any
y
∈
X
y \in X
y
∈
X
,
f
(
f
−
1
(
y
)
)
=
y
f(f^{-1}(y)) = y
f
(
f
−
1
(
y
))
=
y
, so
(
f
∘
f
−
1
)
(
y
)
=
y
(f \circ f^{-1})(y) = y
(
f
∘
f
−
1
)
(
y
)
=
y
, i.e.
f
∘
f
−
1
=
i
d
X
f \circ f^{-1} = \mathrm{id}_X
f
∘
f
−
1
=
id
X
​
. So
f
−
1
f^{-1}
f
−
1
is bijective (its inverse is
f
f
f
).
Closure: This is proven by first working forwards (prove that the composition of two bijections is injective) and then backwards (prove that the composition of two bijections is surjective). You can find a trillion proofs of this online.
Homomorphisms
⌗
A homomorphism is a “structure-preserving map” between two groups. What a useless definition. Take two groups,
(
G
,
⋅
)
(G, \cdot)
(
G
,
⋅
)
and
(
H
,
∗
)
(H, *)
(
H
,
∗
)
. A homomorphism from
G
G
G
to
H
H
H
is a function
f
:
G
→
H
f : G \to H
f
:
G
→
H
such that for any
a
,
b
∈
G
a, b \in G
a
,
b
∈
G
,
f
(
a
⋅
b
)
=
f
(
a
)
∗
f
(
b
)
f(a \cdot b) = f(a) * f(b)
f
(
a
⋅
b
)
=
f
(
a
)
∗
f
(
b
)
.
Example:
ln
⁡
(
x
y
)
=
ln
⁡
(
x
)
+
ln
⁡
(
y
)
\ln(xy) = \ln(x) + \ln(y)
ln
(
x
y
)
=
ln
(
x
)
+
ln
(
y
)
shows that the natural logarithm is a homomorphism from the multiplicative group of positive real numbers
(
R
+
,
⋅
)
(\mathbb{R}^+, \cdot)
(
R
+
,
⋅
)
to the additive group of real numbers
(
R
,
+
)
(\mathbb{R}, +)
(
R
,
+
)
.
Important: an
isomorphism
is a bijective homomorphism. In other words, it’s a structure-preserving map between two groups that is also one-to-one and onto. If two structures are isomorphic, we write
G
≅
H
G \cong H
G
≅
H
.
Example: The groups
(
R
+
,
⋅
)
(\mathbb{R}^+, \cdot)
(
R
+
,
⋅
)
and
(
R
,
+
)
(\mathbb{R}, +)
(
R
,
+
)
are isomorphic via the natural logarithm function
ln
⁡
:
R
+
→
R
\ln : \mathbb{R}^+ \to \mathbb{R}
ln
:
R
+
→
R
, which is a bijective homomorphism (inverse function is the exponential function
exp
⁡
:
R
→
R
+
\exp : \mathbb{R} \to \mathbb{R}^+
exp
:
R
→
R
+
).
That’s it.
Subgroups
⌗
A subgroup is a subset of a group that is itself a group under the same operation. Formally, if
(
G
,
⋅
)
(G, \cdot)
(
G
,
⋅
)
is a group and
H
⊆
G
H \subseteq G
H
⊆
G
, then
(
H
,
⋅
)
(H, \cdot)
(
H
,
⋅
)
is a subgroup of
(
G
,
⋅
)
(G, \cdot)
(
G
,
⋅
)
if:
For any
a
,
b
∈
H
a, b \in H
a
,
b
∈
H
,
a
⋅
b
∈
H
a \cdot b \in H
a
⋅
b
∈
H
(closure).
There exists an element
ε
∈
H
\varepsilon \in H
ε
∈
H
such that for any
a
∈
H
a \in H
a
∈
H
,
ε
⋅
a
=
a
⋅
ε
=
a
\varepsilon \cdot a = a \cdot \varepsilon = a
ε
⋅
a
=
a
⋅
ε
=
a
(identity element).
For any
a
∈
H
a \in H
a
∈
H
, there exists an element
b
∈
H
b \in H
b
∈
H
such that
a
⋅
b
=
b
⋅
a
=
ε
a \cdot b = b \cdot a = \varepsilon
a
⋅
b
=
b
⋅
a
=
ε
(inverse element).
For any
a
,
b
,
c
∈
H
a, b, c \in H
a
,
b
,
c
∈
H
,
(
a
⋅
b
)
⋅
c
=
a
⋅
(
b
⋅
c
)
(a \cdot b) \cdot c = a \cdot (b \cdot c)
(
a
⋅
b
)
⋅
c
=
a
⋅
(
b
⋅
c
)
(associativity).
This is tricky, because we have to maintain closure, identity, inverses, and associativity.
Example: Consider the group
(
Z
,
+
)
(\mathbb{Z}, +)
(
Z
,
+
)
. The set of even integers
2
Z
=
…
,
−
4
,
−
2
,
0
,
2
,
4
,
…
2\mathbb{Z} = {\ldots, -4, -2, 0, 2, 4, \ldots}
2
Z
=
…
,
−
4
,
−
2
,
0
,
2
,
4
,
…
is a subgroup of
(
Z
,
+
)
(\mathbb{Z}, +)
(
Z
,
+
)
because:
The sum of any two even integers is an even integer (closure).
The identity element 0 is an even integer (identity element).
The inverse of any even integer is also an even integer (inverse element).
Addition is associative for all integers, including even integers (associativity).
Cayley’s theorem.
⌗
Every group
(
G
,
⋅
)
(G,\cdot)
(
G
,
⋅
)
is isomorphic to a subgroup of
B
i
j
(
G
)
\mathrm{Bij}(G)
Bij
(
G
)
, the group of bijections of
G
G
G
under composition.
We constructively demonstrate this below. For each
a
∈
G
a \in G
a
∈
G
, define
left multiplication by
a
a
a
as the map
L
a
:
G
→
G
,
L
a
(
x
)
=
a
⋅
x
.
L_a : G \to G,\quad L_a(x)=a\cdot x .
L
a
​
:
G
→
G
,
L
a
​
(
x
)
=
a
⋅
x
.
Now:
Each
L
a
L_a
L
a
​
is a bijection: its inverse is
L
a
−
1
L_{a^{-1}}
L
a
−
1
​
.
Composition matches multiplication:
L
a
∘
L
b
=
L
a
⋅
b
.
L_a\circ L_b = L_{a\cdot b}.
L
a
​
∘
L
b
​
=
L
a
⋅
b
​
.
The map
Φ
:
G
→
B
i
j
(
G
)
\Phi:G\to\mathrm{Bij}(G)
Φ
:
G
→
Bij
(
G
)
given by
Φ
(
a
)
=
L
a
\Phi(a)=L_a
Φ
(
a
)
=
L
a
​
is a homomorphism.
Φ
\Phi
Φ
is injective, since
L
a
(
ε
)
=
a
L_a(\varepsilon)=a
L
a
​
(
ε
)
=
a
.
Hence:
Φ
(
G
)
\Phi(G)
Φ
(
G
)
is a subgroup of
B
i
j
(
G
)
\mathrm{Bij}(G)
Bij
(
G
)
, and
G
≅
Φ
(
G
)
G\cong \Phi(G)
G
≅
Φ
(
G
)
. Thus every group can be realized as a group of bijections.
Just as a simple example: Cayley’s theorem says that
Z
n
≅
Φ
(
Z
n
)
\mathbb{Z}_n \cong \Phi(\mathbb{Z}_n)
Z
n
​
≅
Φ
(
Z
n
​
)
for
Φ
(
a
)
=
L
a
\Phi(a) = L_a
Φ
(
a
)
=
L
a
​
where
L
a
(
x
)
=
a
+
m
o
d
n
x
L_a(x) = a +_{\bmod n} x
L
a
​
(
x
)
=
a
+
mod
n
​
x
. Notice that
Φ
\Phi
Φ
here is not our invention: The theorem demands we take each group element and turn it into a bijection of the set
Z
n
\mathbb{Z}_n
Z
n
​
onto itself by “left multiplication” (here, addition modulo
n
n
n
). So each element k of the group becomes the function “add k”. Every group element is doing
something
to a set, and group multiplication is just doing those things one after another.
The image is the set of functions
Ψ
(
Z
n
)
=
,
x
↦
x
+
k
(
m
o
d
n
)
∣
k
∈
Z
n
,
.
\Psi(\mathbb Z_n) = {,x\mapsto x+k \pmod n \mid k\in\mathbb Z_n,}.
Ψ
(
Z
n
​
)
=
,
x
↦
x
+
k
(
mod
n
)
∣
k
∈
Z
n
​
,
.
This is a
subset of
B
i
j
(
Z
n
)
\mathrm{Bij}(\mathbb Z_n)
Bij
(
Z
n
​
)
, and it is closed under composition:
(
x
↦
x
+
a
)
∘
(
x
↦
x
+
b
)
=
(
x
↦
x
+
a
+
b
)
.
(x\mapsto x+a)\circ(x\mapsto x+b) = (x\mapsto x+a+b).
(
x
↦
x
+
a
)
∘
(
x
↦
x
+
b
)
=
(
x
↦
x
+
a
+
b
)
.
This is about the right time to explain symmetric groups: the symmetric group on a set
X
X
X
, denoted
Sym
(
n
)
\textrm{Sym}(n)
Sym
(
n
)
typically taking
X
=
1
,
2
,
…
,
n
X = {1, 2, \ldots, n}
X
=
1
,
2
,
…
,
n
, is the group of all bijections from
X
X
X
to itself under composition. The order (number of contained elements) of the symmetric group
Sym
(
n
)
\textrm{Sym}(n)
Sym
(
n
)
is
n
!
n!
n
!
, which counts the number of ways to arrange
n
n
n
distinct elements.
See the link already? An alternative concrete rephrasing of Cayley’s theorem is that every (finite) group of order
n
n
n
is isomorphic to a subgroup of the symmetric group
Sym
(
n
)
\textrm{Sym}(n)
Sym
(
n
)
.
Cosets
⌗
Suppose that
(
G
,
⋅
)
(G, \cdot)
(
G
,
⋅
)
is a group and
(
H
,
⋅
)
(H, \cdot)
(
H
,
⋅
)
is a subgroup of
(
G
,
⋅
)
(G, \cdot)
(
G
,
⋅
)
(stated tersely as
H
≤
G
H \le G
H
≤
G
). For any element
g
∈
G
g \in G
g
∈
G
, the
left coset
of
H
H
H
in
G
G
G
with respect to
g
g
g
is the set
g
H
=
g
⋅
h
:
h
∈
H
gH = { g \cdot h : h \in H }
g
H
=
g
⋅
h
:
h
∈
H
. Similarly, the
right coset
of
H
H
H
in
G
G
G
with respect to
g
g
g
is the set
H
g
=
h
⋅
g
:
h
∈
H
Hg = { h \cdot g : h \in H }
H
g
=
h
⋅
g
:
h
∈
H
.
Basic facts:
Every element of
G
G
G
belongs to some left-coset.
Two left-cosets are either disjoint or identical.
All left-cosets of
H
H
H
in
G
G
G
have the same number of elements as
H
H
H
.
Cosets, vaguely speaking, are useful for partitioning groups. Given a group
G
G
G
and a subgroup
H
≤
G
H \le G
H
≤
G
, we let:
G
/
H
=
g
H
:
g
∈
G
G / H = { gH : g \in G }
G
/
H
=
g
H
:
g
∈
G
be the set of all left-cosets of
H
H
H
in
G
G
G
. Now suppose that we wanted to turn this set into a group. For this purpose, we want to define:
(
g
H
)
⋅
(
k
H
)
=
(
g
⋅
k
)
H
(gH) \cdot (kH) = (g \cdot k)H
(
g
H
)
⋅
(
k
H
)
=
(
g
⋅
k
)
H
However, this definition is only valid if it doesn’t depend on the choice of representatives
g
g
g
and
k
k
k
. In other words, if
g
H
=
g
’
H
gH = g’H
g
H
=
g
’
H
and
k
H
=
k
’
H
kH = k’H
k
H
=
k
’
H
, we need to ensure that
(
g
⋅
k
)
H
=
(
g
’
⋅
k
’
)
H
(g \cdot k)H = (g’ \cdot k’)H
(
g
⋅
k
)
H
=
(
g
’
⋅
k
’
)
H
. From
g
1
H
=
g
2
H
g_1H = g_2H
g
1
​
H
=
g
2
​
H
we get
g
2
−
1
g
1
∈
H
g_2^{-1}g_1 \in H
g
2
−
1
​
g
1
​
∈
H
, and from
k
1
H
=
k
2
H
k_1H = k_2H
k
1
​
H
=
k
2
​
H
we get
k
2
−
1
k
1
∈
H
k_2^{-1}k_1 \in H
k
2
−
1
​
k
1
​
∈
H
. Thus, for the operation to be well-defined, we need:
(
g
2
g
2
’
)
−
1
(
g
1
g
1
’
)
=
(
g
2
’
)
−
1
(
g
2
−
1
g
1
)
g
1
’
∈
H
(g_2 g_2’)^{-1} (g_1 g_1’) = (g_2’)^{-1} (g_2^{-1} g_1) g_1’ \in H
(
g
2
​
g
2
​
’
)
−
1
(
g
1
​
g
1
​
’
)
=
(
g
2
​
’
)
−
1
(
g
2
−
1
​
g
1
​
)
g
1
​
’
∈
H
And thus we see
g
2
−
1
g
1
∈
H
g_2^{-1} g_1 \in H
g
2
−
1
​
g
1
​
∈
H
, but it is conjugated by
g
1
’
g_1’
g
1
​
’
:
(
g
2
’
)
−
1
H
g
1
′
(g_2’)^{-1} H g_1'
(
g
2
​
’
)
−
1
H
g
1
′
​
For this product to be in
H
H
H
, we need
H
H
H
to be invariant under conjugation by any element of
G
G
G
, i.e.
g
H
g
−
1
=
H
gHg^{-1} = H
g
H
g
−
1
=
H
for all
g
∈
G
g \in G
g
∈
G
. Such subgroups are called
normal subgroups
(denoted
H
◃
G
H \triangleleft G
H
◃
G
).
So now if we augment
G
/
N
=
g
N
:
g
∈
G
G/N = { gN : g \in G }
G
/
N
=
g
N
:
g
∈
G
with the operation
(
g
N
)
(
k
N
)
=
(
g
k
)
N
(gN)(kN) = (gk)N
(
g
N
)
(
k
N
)
=
(
g
k
)
N
, we get a group called the
quotient group
.
This is a well-defined, pretty regular, group:
Identity:
N
N
N
Inverse:
(
g
N
)
−
1
=
g
−
1
N
(gN)^{-1} = g^{-1}N
(
g
N
)
−
1
=
g
−
1
N
Associativity inherited from
G
G
G
This construction has a very special purpose: it is the only way groups can be simplified without losing structure.
First Isomorphism Theorem
⌗
Suppose that
f
:
G
→
H
f : G \to H
f
:
G
→
H
is a homomorphism between two groups
(
G
,
⋅
)
(G, \cdot)
(
G
,
⋅
)
and
(
H
,
∗
)
(H, *)
(
H
,
∗
)
. The
kernel
of
f
f
f
is the set
ker
⁡
(
f
)
=
g
∈
G
:
f
(
g
)
=
ε
H
\ker(f) = { g \in G : f(g) = \varepsilon_H }
ker
(
f
)
=
g
∈
G
:
f
(
g
)
=
ε
H
​
, where
ε
H
\varepsilon_H
ε
H
​
is the identity element of
H
H
H
. The
image
of
f
f
f
is the set
i
m
(
f
)
=
h
∈
H
:
h
=
f
(
g
)
for some
g
∈
G
\mathrm{im}(f) = { h \in H : h = f(g) \text{ for some } g \in G }
im
(
f
)
=
h
∈
H
:
h
=
f
(
g
)
for some
g
∈
G
.
As a simple example of a kernel, consider the homomorphism
f
:
(
Z
,
+
)
→
(
Z
n
,
+
m
o
d
n
)
f : (\mathbb{Z}, +) \to (\mathbb{Z}_n, +_{\bmod n})
f
:
(
Z
,
+
)
→
(
Z
n
​
,
+
mod
n
​
)
defined by
f
(
k
)
=
k
m
o
d
n
f(k) = k \bmod n
f
(
k
)
=
k
mod
n
. The kernel of this homomorphism is the set of all integers that are multiples of
n
n
n
, i.e.
ker
⁡
(
f
)
=
n
Z
=
…
,
−
2
n
,
−
n
,
0
,
n
,
2
n
,
…
\ker(f) = n\mathbb{Z} = {\ldots, -2n, -n, 0, n, 2n, \ldots}
ker
(
f
)
=
n
Z
=
…
,
−
2
n
,
−
n
,
0
,
n
,
2
n
,
…
- because (informally) these are the integers that map to 0 in
Z
n
\mathbb{Z}_n
Z
n
​
.
We know for a fact that the kernel of a homomorphism is always a normal subgroup of the domain group. In our example,
n
Z
n\mathbb{Z}
n
Z
is indeed a normal subgroup of
(
Z
,
+
)
(\mathbb{Z}, +)
(
Z
,
+
)
. Furthermore,
f
f
f
is injective if and only if
ker
⁡
(
f
)
=
ε
G
\ker(f) = {\varepsilon_G}
ker
(
f
)
=
ε
G
​
, where
ε
G
\varepsilon_G
ε
G
​
is the identity element of
G
G
G
.
As an example of an image, consider the same homomorphism
f
:
(
Z
,
+
)
→
(
Z
n
,
+
m
o
d
n
)
f : (\mathbb{Z}, +) \to (\mathbb{Z}_n, +_{\bmod n})
f
:
(
Z
,
+
)
→
(
Z
n
​
,
+
mod
n
​
)
. The image of this homomorphism is the entire group
Z
n
\mathbb{Z}_n
Z
n
​
, i.e.
i
m
(
f
)
=
Z
n
\mathrm{im}(f) = \mathbb{Z}_n
im
(
f
)
=
Z
n
​
- because every element in
Z
n
\mathbb{Z}_n
Z
n
​
can be obtained by taking some integer modulo
n
n
n
.
The
structural theorem
(or the First Isomorphism Theorem) states that if
f
:
G
→
H
f : G \to H
f
:
G
→
H
is a homomorphism, then the quotient group
G
/
ker
⁡
(
f
)
G / \ker(f)
G
/
ker
(
f
)
is isomorphic to the image of
f
f
f
, i.e.
G
/
ker
⁡
(
f
)
≅
i
m
(
f
)
G / \ker(f) \cong \mathrm{im}(f)
G
/
ker
(
f
)
≅
im
(
f
)
.
Constuctively we can define a map
φ
:
G
/
ker
⁡
(
f
)
→
i
m
(
f
)
\varphi : G / \ker(f) \to \mathrm{im}(f)
φ
:
G
/
ker
(
f
)
→
im
(
f
)
by
φ
(
g
ker
⁡
(
f
)
)
=
f
(
g
)
\varphi(g \ker(f)) = f(g)
φ
(
g
ker
(
f
))
=
f
(
g
)
. This map is well-defined, because if
g
ker
⁡
(
f
)
=
g
’
ker
⁡
(
f
)
g \ker(f) = g’ \ker(f)
g
ker
(
f
)
=
g
’
ker
(
f
)
, then
g
’
−
1
g
∈
ker
⁡
(
f
)
g’^{-1} g \in \ker(f)
g
’
−
1
g
∈
ker
(
f
)
, which implies that
f
(
g
’
−
1
g
)
=
ε
H
f(g’^{-1} g) = \varepsilon_H
f
(
g
’
−
1
g
)
=
ε
H
​
, and thus
f
(
g
)
=
f
(
g
’
)
f(g) = f(g’)
f
(
g
)
=
f
(
g
’
)
. The map
φ
\varphi
φ
is a homomorphism, because:
φ
(
(
g
ker
⁡
(
f
)
)
(
k
ker
⁡
(
f
)
)
)
=
φ
(
(
g
k
)
ker
⁡
(
f
)
)
=
f
(
g
k
)
=
f
(
g
)
∗
f
(
k
)
=
φ
(
g
ker
⁡
(
f
)
)
∗
φ
(
k
ker
⁡
(
f
)
)
.
\varphi((g \ker(f))(k \ker(f))) = \varphi((gk) \ker(f)) = f(gk) = f(g) * f(k) = \varphi(g \ker(f)) * \varphi(k \ker(f)).
φ
((
g
ker
(
f
))
(
k
ker
(
f
)))
=
φ
((
g
k
)
ker
(
f
))
=
f
(
g
k
)
=
f
(
g
)
∗
f
(
k
)
=
φ
(
g
ker
(
f
))
∗
φ
(
k
ker
(
f
))
.
The map
φ
\varphi
φ
is surjective by definition of the image, and it is injective because if
φ
(
g
ker
⁡
(
f
)
)
=
ε
H
\varphi(g \ker(f)) = \varepsilon_H
φ
(
g
ker
(
f
))
=
ε
H
​
, then
f
(
g
)
=
ε
H
f(g) = \varepsilon_H
f
(
g
)
=
ε
H
​
, which implies that
g
∈
ker
⁡
(
f
)
g \in \ker(f)
g
∈
ker
(
f
)
, and thus
g
ker
⁡
(
f
)
=
ker
⁡
(
f
)
g \ker(f) = \ker(f)
g
ker
(
f
)
=
ker
(
f
)
.
Intuitively: A homomorphism collapses elements of G that differ by elements of the kernel. Once you factor out exactly this redundancy, what remains is structurally identical to the image.
Going back to our example with
f
:
(
Z
,
+
)
→
(
Z
n
,
+
m
o
d
n
)
f : (\mathbb{Z}, +) \to (\mathbb{Z}_n, +_{\bmod n})
f
:
(
Z
,
+
)
→
(
Z
n
​
,
+
mod
n
​
)
, we have
ker
⁡
(
f
)
=
n
Z
\ker(f) = n\mathbb{Z}
ker
(
f
)
=
n
Z
and
i
m
(
f
)
=
Z
n
\mathrm{im}(f) = \mathbb{Z}_n
im
(
f
)
=
Z
n
​
. According to the First Isomorphism Theorem, we have:
Z
/
n
Z
≅
Z
n
.
\mathbb{Z} / n\mathbb{Z} \cong \mathbb{Z}_n.
Z
/
n
Z
≅
Z
n
​
.
This means that the quotient group
Z
/
n
Z
\mathbb{Z} / n\mathbb{Z}
Z
/
n
Z
is structurally identical to the group
Z
n
\mathbb{Z}_n
Z
n
​
, and we can give an explicit isomorphism between them:
φ
:
Z
/
n
Z
→
Z
n
,
φ
(
k
+
n
Z
)
=
k
m
o
d
n
.
\varphi : \mathbb{Z} / n\mathbb{Z} \to \mathbb{Z}_n, \quad \varphi(k + n\mathbb{Z}) = k \bmod n.
φ
:
Z
/
n
Z
→
Z
n
​
,
φ
(
k
+
n
Z
)
=
k
mod
n
.
It’s useful to visualize the algebraic structures at hand a little bit:
n
Z
n\mathbb{Z}
n
Z
is the subgroup of
Z
\mathbb{Z}
Z
consisting of all multiples of
n
n
n
, i.e.
n
Z
=
…
,
−
2
n
,
−
n
,
0
,
n
,
2
n
,
…
=
n
k
∣
k
∈
Z
n\mathbb{Z} = {\ldots, -2n, -n, 0, n, 2n, \ldots} = { nk\mid k \in \mathbb{Z} }
n
Z
=
…
,
−
2
n
,
−
n
,
0
,
n
,
2
n
,
…
=
nk
∣
k
∈
Z
.
The quotient group
Z
/
n
Z
\mathbb{Z} / n\mathbb{Z}
Z
/
n
Z
consists of the cosets of
n
Z
n\mathbb{Z}
n
Z
in
Z
\mathbb{Z}
Z
, i.e.
Z
/
n
Z
=
k
+
n
Z
:
k
∈
Z
\mathbb{Z} / n\mathbb{Z} = { k + n\mathbb{Z} : k \in \mathbb{Z} }
Z
/
n
Z
=
k
+
n
Z
:
k
∈
Z
. There are exactly
n
n
n
distinct cosets, which can be represented by the integers
0
,
1
,
…
,
n
−
1
0, 1, \ldots, n-1
0
,
1
,
…
,
n
−
1
.
In
Z
/
n
Z
\mathbb{Z} / n\mathbb{Z}
Z
/
n
Z
, an element is not a single integer, but rather a set of integers that differ by multiples of
n
n
n
. For example, the coset
2
+
n
Z
2 + n\mathbb{Z}
2
+
n
Z
includes all integers of the form
2
+
k
n
2 + kn
2
+
kn
for any integer
k
k
k
. Addition is defined as:
(
a
+
n
Z
)
+
(
b
+
n
Z
)
=
(
a
+
b
)
+
n
Z
.
(a + n\mathbb{Z}) + (b + n\mathbb{Z}) = (a + b) + n\mathbb{Z}.
(
a
+
n
Z
)
+
(
b
+
n
Z
)
=
(
a
+
b
)
+
n
Z
.
Making it a group (check the propeties!).
Tying the knot.
⌗
A group
G
G
G
is simple if it has no normal subgroups other than the trivial group
ε
{\varepsilon}
ε
and itself
G
G
G
. Simple groups are like the prime numbers of group theory - they cannot be broken down into smaller, non-trivial normal subgroups.
The factorisation lets us analyse complex groups by breaking them down into simpler components. This is the essence of the Jordan-Hölder theorem. A composition series of a finite group
G
G
G
is a sequence of subgroups:
ε
=
G
0
◃
G
1
◃
G
2
◃
…
◃
G
n
=
G
{ \varepsilon } = G_0 \triangleleft G_1 \triangleleft G_2 \triangleleft \ldots \triangleleft G_n = G
ε
=
G
0
​
◃
G
1
​
◃
G
2
​
◃
…
◃
G
n
​
=
G
where each
G
i
G_{i}
G
i
​
is a normal subgroup of
G
i
+
1
G_{i+1}
G
i
+
1
​
, and the quotient groups
G
i
+
1
/
G
i
G_{i+1} / G_i
G
i
+
1
​
/
G
i
​
are simple groups. The Jordan-Hölder theorem states that any two composition series of a finite group have the same length and the same simple quotient groups, up to isomorphism and order.
Detour: Applications of the First Isomorphism Theorem
⌗
An integer
q
q
q
is called a quadratic residue modulo
n
∈
N
n \in \mathbb{N}
n
∈
N
if it is congruent to a perfect square modulo
n
n
n
; in other words, if there exists
x
∈
Z
x \in \mathbb{Z}
x
∈
Z
such that
x
2
≡
q
m
o
d
n
x^2 \equiv q \bmod n
x
2
≡
q
mod
n
.
When the number
p
>
2
p > 2
p
>
2
is prime, it has
(
p
−
1
)
/
2
(p-1)/2
(
p
−
1
)
/2
quadratic residues. This is a pretty elementary result in number theory, but we can also prove it elegantly using the First Isomorphism Theorem:
Let
Z
p
\mathbb{Z}_p
Z
p
​
be the group of integers modulo
p
p
p
under addition, and let
Z
p
∗
\mathbb{Z}_{p}^*
Z
p
∗
​
be the group of invertible elements of
Z
p
\mathbb{Z}_p
Z
p
​
under integer multiplication (i.e.
Z
p
∗
=
1
,
2
,
…
,
p
−
1
\mathbb{Z}_p^* = {1, 2, \ldots, p-1}
Z
p
∗
​
=
1
,
2
,
…
,
p
−
1
). Define the group homomorphism
f
:
Z
p
∗
→
Z
p
∗
f : \mathbb{Z}_p^* \to \mathbb{Z}_p^*
f
:
Z
p
∗
​
→
Z
p
∗
​
by
f
(
x
)
=
x
2
m
o
d
p
f(x) = x^2 \bmod p
f
(
x
)
=
x
2
mod
p
. The kernel of
f
f
f
is the set of all
x
∈
Z
p
∗
x \in \mathbb{Z}_p^*
x
∈
Z
p
∗
​
such that
x
2
≡
1
m
o
d
p
x^2 \equiv 1 \bmod p
x
2
≡
1
mod
p
, which is
1
,
−
1
{1, -1}
1
,
−
1
(or
1
,
p
−
1
{1, p-1}
1
,
p
−
1
; both follow from the fact that
p
p
p
is prime).
By the First Isomorphism Theorem, we have:
Z
p
∗
/
ker
⁡
(
f
)
≅
i
m
(
f
)
.
\mathbb{Z}_p^* / \ker(f) \cong \mathrm{im}(f).
Z
p
∗
​
/
ker
(
f
)
≅
im
(
f
)
.
Hence:
∣
i
m
(
f
)
∣
=
∣
Z
p
∗
∣
/
∣
ker
⁡
(
f
)
∣
=
(
p
−
1
)
/
2.
|\mathrm{im}(f)| = |\mathbb{Z}_p^*| / |\ker(f)| = (p-1) / 2.
∣
im
(
f
)
∣
=
∣
Z
p
∗
​
∣/∣
ker
(
f
)
∣
=
(
p
−
1
)
/2.
Which concludes the proof.
It’s quite magical, so anticipate to sit with this for a while. This theorem lets us prove that if
n
n
n
is prime and
λ
<
1
/
2
\lambda < 1/2
λ
<
1/2
, then quadratic probing will always find a vacant bucket, and furthermore, no buckets will be checked twice.
Classification of finite groups, algebraically.
⌗
A finite simple group
S
S
S
is isomorphic to exactly one of the following:
A cyclic group of prime order, i.e.
S
≅
Z
p
S \cong \mathbb{Z}_p
S
≅
Z
p
​
for some prime
p
p
p
.
An alternating group
A
n
A_n
A
n
​
for some
n
≥
5
n \geq 5
n
≥
5
.
A group of Lie type (finite groups of
F
q
\mathbb{F}_q
F
q
​
-rational points of simple algebraic groups over finite fields
F
q
\mathbb{F}_q
F
q
​
, modulo center plus twisted forms):
Classical groups:
P
S
L
n
(
q
)
\mathrm{PSL}_n(q)
PSL
n
​
(
q
)
,
P
S
p
2
n
(
q
)
\mathrm{PSp}_{2n}(q)
PSp
2
n
​
(
q
)
,
P
S
U
n
(
q
)
\mathrm{PSU}_n(q)
PSU
n
​
(
q
)
,
P
Ω
n
±
(
q
)
\mathrm{P\Omega}_n^{\pm}(q)
PΩ
n
±
​
(
q
)
.
Exceptional and twisted groups:
G
2
(
q
)
G_2(q)
G
2
​
(
q
)
,
F
4
(
q
)
F_4(q)
F
4
​
(
q
)
,
E
6
(
q
)
E_6(q)
E
6
​
(
q
)
,
E
7
(
q
)
E_7(q)
E
7
​
(
q
)
,
E
8
(
q
)
E_8(q)
E
8
​
(
q
)
,
2
E
6
(
q
)
{}^2E_6(q)
2
E
6
​
(
q
)
,
3
D
4
(
q
)
{}^3D_4(q)
3
D
4
​
(
q
)
,
2
B
2
(
q
)
{}^2B_2(q)
2
B
2
​
(
q
)
,
2
G
2
(
q
)
{}^2G_2(q)
2
G
2
​
(
q
)
,
2
F
4
(
q
)
{}^2F_4(q)
2
F
4
​
(
q
)
.
One of the 26 sporadic groups.
Every group is some gluing and extension of these (this is actually a pretty impressive result!).
Alternating groups.
⌗
Not really super related to our topic, but alternating groups kind of interesting. Recall that
S
y
m
(
n
)
\mathrm{Sym}(n)
Sym
(
n
)
is the group of all bijections of the set
1
,
2
,
…
,
n
{1,2,\dots,n}
1
,
2
,
…
,
n
, with group operation given by composition.
There exists a surjective group homomorphism
Ψ
:
S
y
m
(
n
)
⟶
Z
2
\Psi : \mathrm{Sym}(n) \longrightarrow \mathbb{Z}_2
Ψ
:
Sym
(
n
)
⟶
Z
2
​
whose kernel has index 2 (the kernel is half the size of
S
y
m
(
n
)
\mathrm{Sym}(n)
Sym
(
n
)
). We do not need to construct
Ψ
\Psi
Ψ
explicitly; its existence is a theorem.
We define the alternating group
A
n
A_n
A
n
​
to be exactly this kernel:
A
n
:
=
ker
⁡
(
Ψ
)
A_n := \ker(\Psi)
A
n
​
:=
ker
(
Ψ
)
By general group theory we notice that:
A
n
◃
S
y
m
(
n
)
A_n \triangleleft \mathrm{Sym}(n)
A
n
​
◃
Sym
(
n
)
(normal subgroup).
[
S
y
m
(
n
)
:
A
n
]
=
2
[\mathrm{Sym}(n) : A_n] = 2
[
Sym
(
n
)
:
A
n
​
]
=
2
(index 2).
∣
A
n
∣
=
n
!
/
2
|A_n| = n! / 2
∣
A
n
​
∣
=
n
!
/2
(order).
Finally, per the First Isomorphism Theorem, we have
S
y
m
(
n
)
/
A
n
≅
Z
2
\mathrm{Sym}(n) / A_n \cong \mathbb{Z}_2
Sym
(
n
)
/
A
n
​
≅
Z
2
​
- important!
The unremarkable cases are as follows:
A
1
A_1
A
1
​
is the trivial group; we see that definitionally
S
y
m
(
1
)
=
ε
\mathrm{Sym}(1) = {\varepsilon}
Sym
(
1
)
=
ε
, so
A
1
=
ε
A_1 = {\varepsilon}
A
1
​
=
ε
.
A
2
A_2
A
2
​
is also the trivial group;
S
y
m
(
2
)
≅
Z
2
\mathrm{Sym}(2) \cong \mathbb{Z}_2
Sym
(
2
)
≅
Z
2
​
, so
A
2
=
ker
⁡
(
Ψ
)
=
ε
A_2 = \ker(\Psi) = {\varepsilon}
A
2
​
=
ker
(
Ψ
)
=
ε
.
A
3
A_3
A
3
​
is isomorphic to
Z
3
\mathbb{Z}_3
Z
3
​
;
S
y
m
(
3
)
\mathrm{Sym}(3)
Sym
(
3
)
has 6 elements, so
A
3
A_3
A
3
​
has 3 elements. It can be verified that
A
3
≅
Z
3
A_3 \cong \mathbb{Z}_3
A
3
​
≅
Z
3
​
.
To explain
A
4
A_4
A
4
​
, we must first expose Lagrange’s theorem and Cauchy’s theorem. Lagrange’s theorem states that for any finite group
G
G
G
and any subgroup
H
≤
G
H \le G
H
≤
G
, the order of
H
H
H
divides the order of
G
G
G
. In other words,
∣
G
∣
=
[
G
:
H
]
⋅
∣
H
∣
|G| = [G : H] \cdot |H|
∣
G
∣
=
[
G
:
H
]
⋅
∣
H
∣
, where
[
G
:
H
]
[G : H]
[
G
:
H
]
is the index of
H
H
H
in
G
G
G
(the number of distinct left cosets of
H
H
H
in
G
G
G
).
The proof of Lagrange’s theorem is straightforward: the left cosets of
H
H
H
in
G
G
G
partition the group
G
G
G
into disjoint subsets, each of size
∣
H
∣
|H|
∣
H
∣
. Therefore, the total number of elements in
G
G
G
is equal to the number of left cosets multiplied by the size of each coset, which gives us
∣
G
∣
=
[
G
:
H
]
⋅
∣
H
∣
|G| = [G : H] \cdot |H|
∣
G
∣
=
[
G
:
H
]
⋅
∣
H
∣
. From this equation, it follows that
∣
H
∣
|H|
∣
H
∣
divides
∣
G
∣
|G|
∣
G
∣
.
Cauchy’s theorem states that if
G
G
G
is a finite group and
p
p
p
is a prime number that divides the order of
G
G
G
, then
G
G
G
contains an element of order
p
p
p
. Consequently,
G
G
G
also contains a subgroup of order
p
p
p
. We will adjourn the proof of this for later, because it’s a little involved.
Now,
A
4
A_4
A
4
​
has 12 elements. By Lagrange’s theorem, the possible orders of subgroups of
A
4
A_4
A
4
​
are 1, 2, 3, 4, 6, and 12.
To decide which of these orders actually occur, we will use Cauchy’s theorem:
2
∣
12
2 \mid 12
2
∣
12
, so there exists
x
∈
A
4
x \in A_4
x
∈
A
4
​
such that
x
2
=
ε
x^2 = \varepsilon
x
2
=
ε
. Pick
x
x
x
as such element. Then,
ε
,
x
≤
A
4
{\varepsilon, x} \le A_4
ε
,
x
≤
A
4
​
is such a subgroup of order 2.
If the group had one element of order 2, then the subgroup would be normal and the quotient would have order 6, which is impossible because
A
4
≤
S
y
m
(
4
)
A_4 \le \mathrm{Sym}(4)
A
4
​
≤
Sym
(
4
)
. If there were more than three such elements, then their pairwise disjointness would imply that
A
4
A_4
A
4
​
has more than 12 elements. Therefore, there are exactly three elements of order 2 in
A
4
A_4
A
4
​
, which we can denote as
x
x
x
,
y
y
y
, and
z
z
z
.
Now we can form the subgroup:
H
=
ε
,
x
,
y
,
z
≤
A
4
H = {\varepsilon, x, y, z} \le A_4
H
=
ε
,
x
,
y
,
z
≤
A
4
​
where
x
,
y
,
z
x, y, z
x
,
y
,
z
are the three elements of order 2. Inverses are automatic, closure holds because the product of any two elements of order 2 is the third element of order 2 (e.g.,
x
y
=
z
xy = z
x
y
=
z
), and the identity element is included; further the associativity is inherited from
A
4
A_4
A
4
​
.
As a direct result, we see that the quotient group
A
4
/
H
A_4 / H
A
4
​
/
H
has order 3. We can prove that
S
y
m
(
A
4
/
H
)
≅
S
y
m
(
3
)
\mathrm Sym(A_4 / H) \cong \mathrm Sym(3)
S
y
m
(
A
4
​
/
H
)
≅
S
y
m
(
3
)
(exercise for the reader). Taking the kernel of the action
K
=
ker
⁡
(
Φ
:
A
4
→
S
y
m
(
A
4
/
H
)
)
K = \ker(\Phi : A_4 \to \mathrm{Sym}(A_4 / H))
K
=
ker
(
Φ
:
A
4
​
→
Sym
(
A
4
​
/
H
))
, we see that
K
◃
A
4
K \triangleleft A_4
K
◃
A
4
​
and
[
A
4
:
K
]
∣
6
[A_4 : K] \mid 6
[
A
4
​
:
K
]
∣
6
(Lagrange’s theorem). Since
[
A
4
:
H
]
=
3
[A_4 : H] = 3
[
A
4
​
:
H
]
=
3
, then
∣
A
4
∣
=
3
∣
H
∣
|A_4| = 3|H|
∣
A
4
​
∣
=
3∣
H
∣
. Since
K
⊆
H
K \subseteq H
K
⊆
H
,
[
A
4
:
K
]
=
[
A
4
:
H
]
[
H
:
K
]
=
3
[
H
:
K
]
[A_4 : K] = [A_4 : H][H : K] = 3[H : K]
[
A
4
​
:
K
]
=
[
A
4
​
:
H
]
[
H
:
K
]
=
3
[
H
:
K
]
, so
[
A
4
:
K
]
[A_4 : K]
[
A
4
​
:
K
]
is either 3 or 6. If it were 6, then this would give a subgroup of order 2 in
S
y
m
(
3
)
\mathrm{Sym}(3)
Sym
(
3
)
arising as a quotient of
H
H
H
, which is impossible because the image of
H
H
H
under the action must fix a coset. Hence
[
A
4
:
K
]
=
3
[A_4 : K] = 3
[
A
4
​
:
K
]
=
3
, so
[
H
:
K
]
=
1
[H : K] = 1
[
H
:
K
]
=
1
and therefore
K
=
H
K = H
K
=
H
. Since
k
e
r
(
Φ
)
\mathrm{ker}(\Phi)
ker
(
Φ
)
is normal in
A
4
A_4
A
4
​
, we have shown that
H
◃
A
4
H \triangleleft A_4
H
◃
A
4
​
.
This is enough to conclude via the first isomorphism theorem that
A
4
/
H
≅
Z
3
A_4 / H \cong \mathbb{Z}_3
A
4
​
/
H
≅
Z
3
​
, giving us a non-trivial normal subgroup
H
H
H
of
A
4
A_4
A
4
​
that proves that
A
4
A_4
A
4
​
is not simple.
As a side note,
H
H
H
here is the Klein four-group, often denoted
V
4
V_4
V
4
​
or just
V
V
V
. It is isomorphic to the direct product
Z
2
×
Z
2
\mathbb{Z}_2 \times \mathbb{Z}_2
Z
2
​
×
Z
2
​
.
Starting with
A
5
A_5
A
5
​
, the alternating groups become simple. One stanard presentation is as follows:
A
5
≅
⟨
x
,
y
∣
x
2
=
y
3
=
(
x
y
)
5
=
ε
⟩
A_5 \cong \langle x, y \mid x^2 = y^3 = (xy)^5 = \varepsilon \rangle
A
5
​
≅
⟨
x
,
y
∣
x
2
=
y
3
=
(
x
y
)
5
=
ε
⟩
This means that
A
5
A_5
A
5
​
is generated by two elements
x
x
x
and
y
y
y
with the relations
x
2
=
ε
x^2 = \varepsilon
x
2
=
ε
,
y
3
=
ε
y^3 = \varepsilon
y
3
=
ε
, and
(
x
y
)
5
=
ε
(xy)^5 = \varepsilon
(
x
y
)
5
=
ε
.
Via Cayley’s theorem we let
G
=
A
5
G = A_5
G
=
A
5
​
act on itself by left-multiplication. This gives a homomorphism
Φ
:
A
5
→
S
y
m
(
A
5
)
\Phi : A_5 \to \mathrm{Sym}(A_5)
Φ
:
A
5
​
→
Sym
(
A
5
​
)
defined by
Φ
(
g
)
(
h
)
=
g
h
\Phi(g)(h) = gh
Φ
(
g
)
(
h
)
=
g
h
for all
g
,
h
∈
A
5
g, h \in A_5
g
,
h
∈
A
5
​
. Since
A
5
A_5
A
5
​
has 60 elements,
S
y
m
(
A
5
)
\mathrm{Sym}(A_5)
Sym
(
A
5
​
)
is isomorphic to
S
y
m
(
60
)
\mathrm{Sym}(60)
Sym
(
60
)
.
The characterisaton of these groups for
n
≥
5
n \geq 5
n
≥
5
is hard as heck, and I don’t know how to do this myself. So we will just leave it at that: for
n
≥
5
n \geq 5
n
≥
5
, the alternating group
A
n
A_n
A
n
​
is simple.
Detour: Burnside’s lemma
⌗
The amount of binary sequences of length
n
≥
1
n \geq 1
n
≥
1
distinct under cyclic shift is given by:
a
(
n
)
=
1
n
∑
k
=
1
n
−
1
2
gcd
⁡
(
n
,
k
)
a(n) = \frac{1}{n} \sum_{k=1}^{n-1} 2^{\gcd(n,k)}
a
(
n
)
=
n
1
​
k
=
1
∑
n
−
1
​
2
g
c
d
(
n
,
k
)
This is super useful when analysing cyclic redundancy codes, like CRC-32 (who knew?).
A cyclic shift is a permutation of the vector
x
=
(
x
0
,
x
1
,
…
,
x
n
−
1
)
x = (x_0, x_1, \ldots, x_{n-1})
x
=
(
x
0
​
,
x
1
​
,
…
,
x
n
−
1
​
)
to the vector
(
x
n
−
1
,
x
0
,
x
1
,
…
,
x
n
−
2
)
(x_{n-1}, x_0, x_1, \ldots, x_{n-2})
(
x
n
−
1
​
,
x
0
​
,
x
1
​
,
…
,
x
n
−
2
​
)
. Cyclic codes (parent family of CRC-32 and others) are defined in such a way that the code is invariant under cyclic shifts, i.e. if
x
x
x
is a codeword, then so is any cyclic shift of
x
x
x
. We will avoid talking too much about that because it requires leaping to a different river of a topic (polynomial rings over finite fields).
Anyway, how come this formula works? A group
G
G
G
is cyclic if there exists an element
g
∈
G
g \in G
g
∈
G
such that
G
=
⟨
g
⟩
=
g
k
:
k
∈
Z
.
G = \langle g \rangle = { g^k : k \in \mathbb{Z} }.
G
=
⟨
g
⟩
=
g
k
:
k
∈
Z
.
The cyclic group of order
n
n
n
is
C
n
=
⟨
r
⟩
=
ε
,
r
,
r
2
,
…
,
r
n
−
1
,
r
n
=
ε
.
C_n = \langle r \rangle = { \varepsilon, r, r^2, \dots, r^{n-1} }, \qquad r^n = \varepsilon.
C
n
​
=
⟨
r
⟩
=
ε
,
r
,
r
2
,
…
,
r
n
−
1
,
r
n
=
ε
.
Further, let the group
G
G
G
act on a set
X
X
X
. For any element
x
x
x
, the
orbit
of
x
x
x
is the subset:
O
r
b
(
x
)
=
g
⋅
x
:
g
∈
G
⊆
X
.
\mathrm{Orb}(x) = { g \cdot x : g \in G } \subseteq X.
Orb
(
x
)
=
g
⋅
x
:
g
∈
G
⊆
X
.
In other words: the orbit of
x
x
x
is the set of all elements of
X
X
X
that can be reached by applying elements of
G
G
G
to
x
x
x
.
Let
X
=
0
,
1
n
X = {0,1}^n
X
=
0
,
1
n
be the set of binary strings of length
n
n
n
. Define an action of
C
n
C_n
C
n
​
on
X
X
X
by letting the generator
r
r
r
act as a one-step cyclic rotation:
r
⋅
(
x
0
x
1
…
x
n
−
1
)
=
(
x
n
−
1
x
0
x
1
…
x
n
−
2
)
.
r \cdot (x_0 x_1 \dots x_{n-1}) = (x_{n-1} x_0 x_1 \dots x_{n-2}).
r
⋅
(
x
0
​
x
1
​
…
x
n
−
1
​
)
=
(
x
n
−
1
​
x
0
​
x
1
​
…
x
n
−
2
​
)
.
Then
r
k
r^k
r
k
acts as rotation by
k
k
k
positions, and
r
n
=
ε
r^n = \varepsilon
r
n
=
ε
acts trivially.
Two strings are equivalent under cyclic shift if and only if they lie in the same orbit of this action. Hence the number of distinct binary sequences under cyclic shift is
a
(
n
)
=
∣
X
/
C
n
∣
a(n) = |X / C_n|
a
(
n
)
=
∣
X
/
C
n
​
∣
the number of orbits (binary necklaces).
Burnside’s lemma says that for a finite group action
G
→
X
G \to X
G
→
X
,
∣
X
/
G
∣
=
1
∣
G
∣
∑
g
∈
G
∣
F
i
x
(
g
)
∣
,
|X/G| = \frac{1}{|G|} \sum_{g \in G} |\mathrm{Fix}(g)|,
∣
X
/
G
∣
=
∣
G
∣
1
​
g
∈
G
∑
​
∣
Fix
(
g
)
∣
,
where
F
i
x
(
g
)
=
x
∈
X
:
g
⋅
x
=
x
.
\mathrm{Fix}(g) = { x \in X : g \cdot x = x }.
Fix
(
g
)
=
x
∈
X
:
g
⋅
x
=
x
.
Applying this to
C
n
C_n
C
n
​
over
X
X
X
, we obtain
a
(
n
)
=
1
n
∑
k
=
0
n
−
1
∣
F
i
x
(
r
k
)
∣
.
a(n) = \frac{1}{n} \sum_{k=0}^{n-1} |\mathrm{Fix}(r^k)|.
a
(
n
)
=
n
1
​
k
=
0
∑
n
−
1
​
∣
Fix
(
r
k
)
∣.
Thus it remains to compute
∣
F
i
x
(
r
k
)
∣
|\mathrm{Fix}(r^k)|
∣
Fix
(
r
k
)
∣
.
Fix
k
∈
0
,
1
,
…
,
n
−
1
k \in {0,1,\dots,n-1}
k
∈
0
,
1
,
…
,
n
−
1
. A string
x
=
(
x
0
,
x
1
,
…
,
x
n
−
1
)
x = (x_0, x_1, \dots, x_{n-1})
x
=
(
x
0
​
,
x
1
​
,
…
,
x
n
−
1
​
)
is
fixed
by
r
k
r^k
r
k
if and only if
x
i
=
x
i
+
k
m
o
d
n
for all
i
.
x_i = x_{i+k \bmod n} \quad \text{for all } i.
x
i
​
=
x
i
+
k
mod
n
​
for all
i
.
Thus the indices
0
,
1
,
…
,
n
−
1
{0,1,\dots,n-1}
0
,
1
,
…
,
n
−
1
are partitioned into cycles under the permutation
i
⟼
i
+
k
(
m
o
d
n
)
,
i \longmapsto i + k \pmod n,
i
⟼
i
+
k
(
mod
n
)
,
and the string must be constant on each cycle.
Let
d
=
gcd
⁡
(
n
,
k
)
d = \gcd(n,k)
d
=
g
cd
(
n
,
k
)
. Consider the cycle containing
0
0
0
:
0
,
,
k
,
,
2
k
,
,
3
k
,
,
…
(
m
o
d
n
)
.
0,, k,, 2k,, 3k,, \dots \pmod n.
0
,,
k
,,
2
k
,,
3
k
,,
…
(
mod
n
)
.
Its length is the smallest
t
>
0
t>0
t
>
0
such that
t
k
≡
0
(
m
o
d
n
)
.
tk \equiv 0 \pmod n.
t
k
≡
0
(
mod
n
)
.
Write
n
=
d
n
’
n = dn’
n
=
d
n
’
,
k
=
d
k
’
k = dk’
k
=
d
k
’
with
gcd
⁡
(
n
’
,
k
’
)
=
1
\gcd(n’,k’) = 1
g
cd
(
n
’
,
k
’
)
=
1
. Then
t
k
≡
0
(
m
o
d
n
)
⟺
t
d
k
’
≡
0
(
m
o
d
d
n
’
)
⟺
t
k
’
≡
0
(
m
o
d
n
’
)
.
tk \equiv 0 \pmod n
\iff tdk’ \equiv 0 \pmod{dn’}
\iff tk’ \equiv 0 \pmod{n’}.
t
k
≡
0
(
mod
n
)
⟺
t
d
k
’
≡
0
(
mod
d
n
’
)
⟺
t
k
’
≡
0
(
mod
n
’
)
.
Since
gcd
⁡
(
k
’
,
n
’
)
=
1
\gcd(k’,n’) = 1
g
cd
(
k
’
,
n
’
)
=
1
, this holds if and only if
n
’
∣
t
n’ \mid t
n
’
∣
t
. Hence the minimal such
t
t
t
is
t
=
n
’
=
n
d
.
t = n’ = \frac{n}{d}.
t
=
n
’
=
d
n
​
.
Therefore:
each cycle has length
n
/
d
n/d
n
/
d
,
the total number of cycles is
n
n
/
d
=
d
=
gcd
⁡
(
n
,
k
)
.
\frac{n}{n/d} = d = \gcd(n,k).
n
/
d
n
​
=
d
=
g
cd
(
n
,
k
)
.
On each cycle, all bits must agree, but different cycles may be chosen independently. Hence
∣
F
i
x
(
r
k
)
∣
=
2
gcd
⁡
(
n
,
k
)
.
|\mathrm{Fix}(r^k)| = 2^{\gcd(n,k)}.
∣
Fix
(
r
k
)
∣
=
2
g
c
d
(
n
,
k
)
.
Finally we substitute into Burnside’s lemma:
a
(
n
)
=
1
n
∑
k
=
0
n
−
1
2
gcd
⁡
(
n
,
k
)
.
a(n) = \frac{1}{n} \sum_{k=0}^{n-1} 2^{\gcd(n,k)}.
a
(
n
)
=
n
1
​
k
=
0
∑
n
−
1
​
2
g
c
d
(
n
,
k
)
.
This completes the proof.
Burnside’s lemma (also seldom called Cauchy-Frobenius lemma) follows by noticing the following (as givne by Ben Lynn in Polya Theory):
Let the orbits
X
1
,
X
2
,
…
,
X
k
X_1, X_2, \ldots, X_k
X
1
​
,
X
2
​
,
…
,
X
k
​
be the partition of
X
X
X
under the action of
G
G
G
. Observe that the resulting sets
F
i
x
X
k
(
g
)
\mathrm{Fix}_{X_k}(g)
Fix
X
k
​
​
(
g
)
for
k
≤
n
k \le n
k
≤
n
also partition
F
i
x
(
g
)
\mathrm{Fix}(g)
Fix
(
g
)
. As such, we have:
∑
g
∈
G
∣
F
i
x
(
g
)
∣
=
∑
g
∈
G
∑
i
=
1
k
∣
F
i
x
X
i
(
g
)
∣
=
∣
(
g
,
x
)
∣
g
∈
G
,
x
∈
F
i
x
X
i
(
g
)
∣
=
∑
i
=
1
k
∑
g
∈
G
∣
G
x
∣
\begin{aligned}
\sum_{g \in G} |\mathrm{Fix}(g)| &= \sum_{g \in G} \sum_{i=1}^k |\mathrm{Fix}_{X_i}(g)| \
&= |{(g,x)\mid g \in G, x \in \mathrm{Fix}_{X_i}(g)}| \
&= \sum_{i=1}^k \sum_{g \in G} |G_x|
\end{aligned}
g
∈
G
∑
​
∣
Fix
(
g
)
∣
​
=
g
∈
G
∑
​
i
=
1
∑
k
​
∣
Fix
X
i
​
​
(
g
)
∣
​
=
∣
(
g
,
x
)
∣
g
∈
G
,
x
∈
Fix
X
i
​
​
(
g
)
∣
​
=
i
=
1
∑
k
​
g
∈
G
∑
​
∣
G
x
​
∣
​
By the orbit-stabiliser theorem and Lagrange’s theorem, we have
∣
G
∣
=
∣
G
x
∣
⋅
∣
O
r
b
(
x
)
∣
|G| = |G_x| \cdot |\mathrm{Orb}(x)|
∣
G
∣
=
∣
G
x
​
∣
⋅
∣
Orb
(
x
)
∣
, and hence the result follows.
Extra reading:
Cauchy’s theorem (partial converse to Lagrange’s theorem)
Sylow theorems (existence of subgroups of order
p
k
p^k
p
k
)
Orbit-stabilizer theorem; isotropy groups (here
G
x
G_x
G
x
​
).
Solvable groups
⌗
It’s a little late to introduce this, but an Abelian group is a special type of a group where the group operation is commutative, i.e. for any
a
,
b
∈
G
a, b \in G
a
,
b
∈
G
,
a
⋅
b
=
b
⋅
a
a \cdot b = b \cdot a
a
⋅
b
=
b
⋅
a
. That’s just an additional axiom on top of the group axioms.
We call a finite group
G
G
G
solvable
if there exists a finite sequence of subgroups:
ε
=
G
0
◃
G
1
◃
G
2
◃
…
◃
G
n
=
G
{ \varepsilon } = G_0 \triangleleft G_1 \triangleleft G_2 \triangleleft \ldots \triangleleft G_n = G
ε
=
G
0
​
◃
G
1
​
◃
G
2
​
◃
…
◃
G
n
​
=
G
such that each
G
i
G_{i}
G
i
​
is a normal subgroup of
G
i
+
1
G_{i+1}
G
i
+
1
​
, and the quotient groups
G
i
+
1
/
G
i
G_{i+1} / G_i
G
i
+
1
​
/
G
i
​
are Abelian groups. Equivalently, all (simple) composition factors of
G
G
G
are cyclic groups of prime order.
There’s two immediate facts that we will state without proof:
If
G
G
G
is solvable, then every subgroup and every quotient group of
G
G
G
is also solvable.
If
N
◃
G
N \triangleleft G
N
◃
G
is a normal subgroup such that both
N
N
N
and
G
/
N
G/N
G
/
N
are solvable, then
G
G
G
is also solvable.
Part 2
⌗
Fields, automorphisms, Galois groups, extensions, fundamental theorem of Galois theory, solvability by radicals. One day.
