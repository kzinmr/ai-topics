---
title: "Implementing the Faddeev-LeVerrier algorithm in APL"
url: "https://iczelia.net/posts/linalg-apl/"
fetched_at: 2026-05-05T07:01:22.075523+00:00
source: "Kamila Szewczyk (iczelia)"
tags: [blog, raw]
---

# Implementing the Faddeev-LeVerrier algorithm in APL

Source: https://iczelia.net/posts/linalg-apl/

The Faddeev-LeVerrier algorithm is one of my favourite algorithms related to linear algebra for a variety of reasons:
It’s incredibly elegant
It computes many things at once - the trace of a matrix, its determinant, inverse and the characteristic polynomial (and thus, its eigenvalues).
The task of computing the characteristic polynomial usually requires the use of symbolic computation - one needs to compute
det
⁡
(
A
−
λ
I
)
\det(A - \lambda I)
det
(
A
−
λ
I
)
to get a function of
λ
\lambda
λ
, while the Faddeev-LeVerrier algorithm can do it numerically.
Initial considerations
⌗
The objective of the Faddeev-LeVerrier algorithm is to compute coefficients of the characteristic polynomial of a square matrix.
p
A
(
λ
)
≡
det
⁡
(
λ
I
n
−
A
)
=
∑
k
=
0
n
c
k
λ
k
p_{A}(\lambda )\equiv \det(\lambda I_{n}-A)=\sum_{k=0}^{n}c_{k}\lambda ^{k}
p
A
​
(
λ
)
≡
det
(
λ
I
n
​
−
A
)
=
k
=
0
∑
n
​
c
k
​
λ
k
The first observation to be made is that
c
n
=
1
c_n = 1
c
n
​
=
1
and
c
0
=
(
−
1
)
n
det
⁡
A
c_0 = (-1)^n \det A
c
0
​
=
(
−
1
)
n
det
A
. The algorithm states:
M
0
≡
0
M
k
≡
A
M
k
−
1
+
c
n
−
k
+
1
I
c
n
−
k
=
−
1
k
t
r
(
A
M
k
)
M_{0} \equiv 0 \\
M_{k} \equiv AM_{k-1}+c_{n-k+1}I \\
c_{n-k} =-{\frac {1}{k}}\mathrm {tr} (AM_{k}) \\
M
0
​
≡
0
M
k
​
≡
A
M
k
−
1
​
+
c
n
−
k
+
1
​
I
c
n
−
k
​
=
−
k
1
​
tr
(
A
M
k
​
)
A few observations assuming a
n
n
n
by
n
n
n
matrix
A
A
A
:
M
n
+
1
=
0
M_{n+1} = 0
M
n
+
1
​
=
0
.
The trace of
A
A
A
is equal to
−
c
2
-c_2
−
c
2
​
.
det
⁡
A
\det A
det
A
is equal to
(
−
1
)
n
c
0
(-1)^n c_0
(
−
1
)
n
c
0
​
(a consequence of the previous observations about
c
c
c
).
A
−
1
A^{-1}
A
−
1
is equal to
−
1
c
0
M
k
-\frac{1}{c_0}M_k
−
c
0
​
1
​
M
k
​
.
An implementation
⌗
I start my implementation by asserting a few things about the environment and the input:
I’m interested only in matrices (arrays of rank 2 -
2=≢⍴⍵
) and I specifically want them square -
=/⍴⍵
. If the conditions aren’t met, the algorithm returns an empty coefficient vector.
Next up, I define
n
as the number of rows/columns of the input matrix,
M0
as the starting matrix for the algorithm, and
I
as an identity matrix of order
n
. The actual recursive implementation of the algorithm will return a vector of the characteristic polynomial coefficients and the matrix corresponding to the current iteration. Since the matrix corresponding to the last iteration is simply
n n⍴0
(per observation 1), I will discard it:
I have also added a guard for the final iteration, which simply returns the identity matrix and
1
as the coefficient.
I recursively call the function asking for the pair of
M
n
−
1
M_{n-1}
M
n
−
1
​
and the corresponding
c
value. I also multiply matrices
M0
(the input matrix) and
MP
(the previous matrix), as it’ll prove itself useful in upcoming computations, first one of them being the computation of
c
for the current iteration. For this purpose, I take the trace of
X
and divide it by the negated iteration index. The
dyadic transposition
(axis rearrangement)
0 0⍉X
yields the leading diagonal of
X
, while
+/
sums it.
I am one step away from the final version of the algorithm, the only thing left is returning the result tuple:
The computation of the current
M
matrix is derived verbatim from the second equation of the algorithm.
Applications
⌗
I will combine today’s post with the
yesterday’s one
about polynomial roots. Namely, the yesterday’s post already contains an example use of my
faddeev_leverrier
function. Let’s do something different today.
With a few not so beautiful hacks on top of my existing function, I can compute all the properties of my test matrix:
The function will return a vector of:
inverse matrix
trace
characteristic polynomial
determinant
The results appear to match my pencil and paper calculations (not presented in this blog post - as an exercise, feel free to compute these properties of my test matrix yourself). Of course, there is a way to compute the remaining properties besides the characteristic polynomial using more idiomatic APL:
The results appear to be the same:
To my surprise, though, it appears that the Faddeev-LeVerrier algorithm is faster for this particular test case! The benchmark data:
Replacing the generalised alternant with a (hopefully) more performant determinant function yields oddly similar results:
Eigenvectors
⌗
The final part of my blog post will shed some more light on eigenvectors. Let’s compute the eigenvalues first:
For simplicity, I will present the pencil and paper calculations for
λ
=
10
\lambda = 10
λ
=
10
alongside the APL code. I start with computing
A
−
λ
I
A - \lambda I
A
−
λ
I
:
A
−
λ
I
=
∣
−
7
1
5
3
−
7
1
4
6
−
6
∣
A - \lambda I =
\begin{vmatrix}
-7 & 1 & 5\\
3 & -7 & 1\\
4 & 6 & -6
\end{vmatrix}
A
−
λ
I
=
​
−
7
3
4
​
1
−
7
6
​
5
1
−
6
​
​
(
A
−
λ
I
)
⋅
v
=
0
(A - \lambda I) \cdot v = 0
(
A
−
λ
I
)
⋅
v
=
0
yields a homogenous equation system which needs to be solved. A very sad property of this system is that it’s underspecified, so
x
k
−
1
x_{k-1}
x
k
−
1
​
up to
n
n
n
are all functions of
x
n
x_n
x
n
​
. Surprisingly, that’s not a problem, though! If we ignore the presence of
x
n
x_n
x
n
​
, turns out one row of the matrix is redundant. If we assume that
x
n
=
1
x_n = 1
x
n
​
=
1
, in our example, we solve a non-homogenous system of equations with two variables.
x
1
=
18
23
x
2
=
11
23
x
3
=
1
x_1 = \frac{18}{23} \\
x_2 = \frac{11}{23} \\
x_3 = 1
x
1
​
=
23
18
​
x
2
​
=
23
11
​
x
3
​
=
1
Of course, one could scale
x
3
x_3
x
3
​
as they please, and modify
x
1
x_1
x
1
​
and
x
2
x_2
x
2
​
accordingly. I also use the same real/imaginary truncation technique as outlined in the previous post to strip (likely) unnecessary real/imaginary parts. Finally, I test my code:
The results seem to match. Great!
Summary
⌗
I believe that today’s post was much more involved than the previous ones. The full source code follows:
