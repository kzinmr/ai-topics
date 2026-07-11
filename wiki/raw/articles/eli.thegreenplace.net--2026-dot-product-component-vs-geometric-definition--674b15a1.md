---
title: "Dot product: Component vs. Geometric definition"
url: "https://eli.thegreenplace.net/2026/dot-product-component-vs-geometric-definition/"
fetched_at: 2026-07-11T07:00:47.935268+00:00
source: "eli.thegreenplace.net"
tags: [blog, raw]
---

# Dot product: Component vs. Geometric definition

Source: https://eli.thegreenplace.net/2026/dot-product-component-vs-geometric-definition/

July 10, 2026 at 18:42
Tags
Math
The goal of this post is to answer a simple question: why are the
following two definitions of the vector dot product in Euclidean
space  equivalent for vectors
\vec{a}
and
\vec{b}
:
Component definition:
\vec{a}\cdot\vec{b}=\sum_{i=1}^{n}a_i b_i
Geometric definition:
\vec{a}\cdot\vec{b}=|\vec{a}||\vec{b}|cos(\theta)
, where
|\vec{a}|
is the magnitude of
\vec{a}
and
is the angle between the vectors’ directions
Here’s a graphical depiction of our vectors (focusing on
for clarity, though this applies to any-dimensional
vectors). It shows both the components of the vectors and the angle
between them. The
length
of the arrow for
\vec{a}
is
|\vec{a}|
.
We’ll show two proofs of the equivalence here, the
geometric proof
and
the
projection proof
. The Appendix describes some properties of dot
products that facilitate these proofs.
Geometric proof
We’ll be using this diagram of our vectors
\vec{a}
and
\vec{b}
, as well as the vector
\vec{c}=\vec{a}-\vec{b}
:
Using the law of cosines  on the triangle formed by the three
vectors:
\[|\vec{c}|^2=|\vec{a}|^2+|\vec{b}|^2-2|\vec{a}||\vec{b}|cos(\theta)\]
Since for any vector
\vec{a}
, we have
\vec{a}\cdot\vec{a}=|\vec{a}|^2
(see Appendix), let’s rewrite
this equation as:
\[\vec{c}\cdot\vec{c}=\vec{a}\cdot\vec{a}+\vec{b}\cdot\vec{b}-2|\vec{a}||\vec{b}|cos(\theta)\]
But
\vec{c}=\vec{a}-\vec{b}
and the dot product obeys the
distributive property (see Appendix). Therefore:
\[\begin{aligned}
(\vec{a}-\vec{b})\cdot(\vec{a}-\vec{b})&=\vec{a}\cdot\vec{a}+\vec{b}\cdot\vec{b}-2|\vec{a}||\vec{b}|cos(\theta)\\
\vec{a}\cdot\vec{a}-2\vec{a}\cdot\vec{b}+\vec{b}\cdot\vec{b}&=\vec{a}\cdot\vec{a}+\vec{b}\cdot\vec{b}-2|\vec{a}||\vec{b}|cos(\theta)\\
-2\vec{a}\cdot\vec{b}&=-2|\vec{a}||\vec{b}|cos(\theta)\\
\vec{a}\cdot\vec{b}&=|\vec{a}||\vec{b}|cos(\theta)
\end{aligned}\]
Projection proof
For this proof, we’ll assume the geometric definition is correct and
will see how it leads to the component definition. We’ll begin by
denoting vectors
\vec{e}_1,\vec{e}_2\dots\vec{e}_n
as the
standard orthonormal basis for
. For example, in 2D
space, these basis vectors are
\vec{e}_1=[1\ 0]
and
\vec{e}_2=[0\ 1]
, shown in
this diagram:
If we take an arbitrary
\vec{a}\in\mathbb{R}^n
and calculate its
dot product with a basis vector, we can use the geometric definition:
\[\vec{a}\cdot\vec{e}_i=|\vec{a}||\vec{e}_i|cos(\theta_i)=|\vec{a}|cos(\theta_i)=a_i\]
where
a_i
is the component of
\vec{a}
in the direction
of
\vec{e}_i
. The diagram makes it easy to see why this is true
from basic trigonometry, but in the more general case this is just a
vector
projection
.
Now let’s represent vectors
\vec{a}
and
\vec{b}
as
linear combinations of the basis vectors:
\[\begin{aligned}
    \vec{a}&=\sum_{i=1}^{n}a_i\vec{e}_i\\
    \vec{b}&=\sum_{i=1}^{n}b_i\vec{e}_i\\
\end{aligned}\]
And calculate the dot product
\vec{a}\cdot\vec{b}
, beginning by
rewriting
\vec{b}
with its linear combination of basis vectors
representation:
\[\vec{a}\cdot\vec{b}=\vec{a}\cdot\sum_{i=1}^{n}b_i\vec{e}_i\]
Using the fact that the dot product distributes over linear
combinations:
\[\vec{a}\cdot\vec{b}=\sum_{i=1}^{n}b_i(\vec{a}\cdot\vec{e}_i)\]
But earlier we’ve shown that
\vec{a}\cdot\vec{e}_i=a_i
.
Therefore:
\[\vec{a}\cdot\vec{b}=\sum_{i=1}^{n}b_i a_i=\sum_{i=1}^{n}a_i b_i\]
Which is the component definition
\blacksquare
.
Appendix A: Inner product space
A generalization of dot products in
is the
inner
product
, which is an operation meeting some specific requirements,
defined on a vector space.
The inner product is denoted as
\langle x,y\rangle:\mathbb{R}^n\times\mathbb{R}^n\to\mathbb{R}
,
and must satisfy the following requirements for all vectors
x,y,z\in\mathbb{R}^n
and scalars
a,b\in\mathbb{R}
:
Symmetry:
\langle x,y\rangle=\langle y,x\rangle
Linearity in the first argument:
\langle ax+by,z\rangle=a\langle x,z\rangle+b\langle y,z\rangle
Positive-definiteness: if
x\ne 0
then
\langle x,x\rangle>0
For
, we define the inner product operation in its
component formulation as:
\[\langle x,y\rangle=\sum_{i=1}^{n}x_i\cdot y_i\]
Let’s prove the requirements listed above for this operation; this is
fairly straightforward, given the well-known properties of scalar
multiplication and addition on
:
Symmetry:
\[\langle x,y\rangle=\sum_{i=1}^{n}x_i\cdot y_i=\sum_{i=1}^{n}y_i\cdot x_i=\langle y,x\rangle\]
Linearity in the first argument:
\[\begin{aligned}
\langle ax+by,z\rangle&=\sum_{i=1}^{n}(ax+by)_i\cdot z_i\\
&=\sum_{i=1}^{n}a x_i\cdot z_i+b y_i\cdot z_i\\
&=a\sum_{i=1}^{n}x_i\cdot z_i+b\sum_{i=1}^{n}y_i\cdot z_i=a\langle x,z\rangle+b\langle y,z\rangle
\end{aligned}\]
Positive-definiteness:
Consider the components
of vector
x
. Clearly,
\forall i\quad x_i\cdot x_i=x_i^2\ge 0
. Since the vector
x
is not the zero vector, at least one of its components
is nonzero, and for that component
x_i\cdot x_i>0
.
Therefore:
\[\langle x,x\rangle=\sum_{i=1}^{n}x_i\cdot x_i>0\]
Now that we’ve proved all the inner product requirements on our
operation
\langle x,y\rangle
, we can say that
is an
inner product space
with this operation.
By meeting these requirements, it can be readily shown that our inner
product operation has additional useful properties:
\langle x,0\rangle=\langle 0,x\rangle=0
\langle x,x\rangle=0
if and only if
x=0
\langle x,ay+bz\rangle=a\langle x,y\rangle+b\langle x,z\rangle
\langle x+y,x+y\rangle=\langle x,x\rangle+2\langle x,y\rangle+\langle y,y\rangle
The third property is particularly helpful, because it means the inner
product is
bilinear
, and thus is distributive over addition.
Note that these are shown for the component definition of dot product.
It’s not too hard to prove distributivity for the geometric definition
using the notion of projections and how they add up.
Norm
The
norm
of a vector
x
in an inner product space is defined as
|x|=\sqrt{\langle x,x\rangle}
. Therefore, the square of the norm
is
|x|^2=\langle x,x\rangle
.
The norm is used to express the notion of
magnitude
, or
length
of a
vector. If you think of a vector
x\in\mathbb{R}^n
in Cartesian
coordinates, the definition of the norm is a generalization of the
Pythagorean theorem.
