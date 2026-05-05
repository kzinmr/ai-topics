---
title: "Implementing Taylor Series in APL"
url: "https://iczelia.net/posts/taylor-apl/"
fetched_at: 2026-05-05T07:01:22.405532+00:00
source: "Kamila Szewczyk (iczelia)"
tags: [blog, raw]
---

# Implementing Taylor Series in APL

Source: https://iczelia.net/posts/taylor-apl/

What problem are we trying to solve?
⌗
Have you ever wondered how does your favourite programming language’s standard library compute the values of
sin
⁡
(
θ
)
\sin(\theta)
sin
(
θ
)
,
cos
⁡
(
θ
)
\cos(\theta)
cos
(
θ
)
and other trigonometric functions?
There are many ideas that might come to your mind. First, we might use the reflective property for negative arguments (e.g.
sin
⁡
(
−
θ
)
=
−
sin
⁡
(
θ
)
\sin(-\theta)=-\sin(\theta)
sin
(
−
θ
)
=
−
sin
(
θ
)
holds), to bring the argument into range
<
0
,
∞
>
<0, \infty>
<
0
,
∞
>
. Then, the full period shift could be used to further reduce the range to
<
0
,
2
π
>
<0, 2\pi>
<
0
,
2
π
>
, yielding the
sin
⁡
(
θ
+
2
k
π
)
=
sin
⁡
(
θ
)
\sin(\theta + 2k\pi) = \sin(\theta)
sin
(
θ
+
2
kπ
)
=
sin
(
θ
)
for
k
∈
Z
k \in Z
k
∈
Z
formula. While there are more interesting tricks to further reduce the domain for easier computations, we can’t repeat these steps forever.
Using just mathematical insight, we’ve established that computing
sin
⁡
(
θ
)
\sin(\theta)
sin
(
θ
)
for
θ
∈
<
−
π
,
π
>
\theta \in <-\pi, \pi>
θ
∈<
−
π
,
π
>
is enough to tell the values of
sin
⁡
(
θ
)
\sin(\theta)
sin
(
θ
)
for all
θ
∈
R
\theta \in R
θ
∈
R
. There are many possibilities to follow from there, for example, using the ridiculous (but valued by engineers) approximation
sin
⁡
(
θ
)
=
θ
\sin(\theta) = \theta
sin
(
θ
)
=
θ
combined with some more properties:
Although, such an approximation is generally too inaccurate for many use cases, so a different method has to be used. Currently, the values of
sin
⁡
(
θ
)
\sin(\theta)
sin
(
θ
)
are nuemrically approximated using two mathematical devices - the Chebyshev polynomials and the Taylor series.
Since it’s
not the first time
Chebyshev polynomials are a little star of my blog post, today I’d like to demonstrate my implementation of the Taylor series in APL.
What is Taylor Series anyway?
⌗
Assuming that the
n
n
n
-th derivative at point
a
a
a
of
f
(
x
)
f(x)
f
(
x
)
computable, it is possible to express the function as an infinite sum of terms using the Taylor Series. Since infinite sums are generally not useful to numerical methods, we (almost) always use a partial sum formed by the first few terms of a Taylor series. Taylor polynomials (for a given
n
n
n
, where
n
+
1
n + 1
n
+
1
terms of a Taylor series is a polynomial of degree
n
n
n
) are approximations of a function, which become generally better as
n
n
n
increases.
A famours approximation of
sin
⁡
(
x
)
\sin(x)
sin
(
x
)
derived using Taylor Series is demonstrated below.
sin
⁡
(
x
)
≈
x
−
x
3
3
!
+
x
5
5
!
−
x
7
7
!
\sin(x) \approx x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!}
sin
(
x
)
≈
x
−
3
!
x
3
​
+
5
!
x
5
​
−
7
!
x
7
​
Implementing Taylor Series.
⌗
The general formula for Taylor series is fairly straightforward and it’s the basis for my implementation in APL:
f
(
a
)
+
f
’
(
a
)
1
!
(
x
−
a
)
+
f
’’
(
a
)
2
!
(
x
−
a
)
2
+
f
’’’
(
a
)
3
!
(
x
−
a
)
3
+
⋯
,
{\displaystyle f(a)+{\frac {f’(a)}{1!}}(x-a)+{\frac {f’’(a)}{2!}}(x-a)^{2}+{\frac {f’’’(a)}{3!}}(x-a)^{3}+\cdots ,}
f
(
a
)
+
1
!
f
’
(
a
)
​
(
x
−
a
)
+
2
!
f
’’
(
a
)
​
(
x
−
a
)
2
+
3
!
f
’’’
(
a
)
​
(
x
−
a
)
3
+
⋯
,
The first immediate concern is computing the values of the
n
n
n
-th derivative of
f
f
f
. Recalling the definition of a derivative:
f
’
(
a
)
=
lim
⁡
h
→
0
f
(
a
+
h
)
−
f
(
a
)
h
f’(a)=\lim _{h\to 0}{\frac {f(a+h)-f(a)}{h}}
f
’
(
a
)
=
h
→
0
lim
​
h
f
(
a
+
h
)
−
f
(
a
)
​
I arbitrarily pick a small value of
h
h
h
and thus approximate the derivative in point:
It’s not the end of the story just yet, though, since it’s not just the first derivative what’s needed. An important (and somewhat trivial) observation is that one can apply the
D
D
D
operator
n
n
n
times to get the
n
n
n
-th derivative!
Verifying the computations,
d
f
d
x
=
2
x
\frac{df}{dx}=2x
d
x
df
​
=
2
x
,
d
2
f
d
x
2
=
2
\frac{d^2f}{dx^2}=2
d
x
2
d
2
f
​
=
2
and finally
d
3
f
d
x
3
=
0
\frac{d^3f}{dx^3}=0
d
x
3
d
3
f
​
=
0
, so the results seem to be correct. Unfortunately, there is no way to apply an operator given amount of times to a function (analogically to the existing
⍣
for functions), so I had to roll my own recursive
n
n
n
-th derivative function:
In the end, it’s nothing too complicated - first derivative marks the end of recursion, the second derivative is the first derivative of the first derivative, and so on. Additionally, I decided to hardcode the degree of the Taylor polynomial that is going to be computed using
n←4
.
Assuming the
⍵
parameter to the
taylor
function is the point at which an existing taylor polynomial is evaluated, my implementation is almost ready:
The final line will map a function that generates Taylor polynomial terms to build the final approximation at point. Recalling the expression above, the implementation will diverge into two branches:
The 0-th term of the Taylor polynomial is always
f
(
a
)
f(a)
f
(
a
)
, while the next ones follow the standard formula:
f
(
n
)
(
a
)
n
!
(
x
−
a
)
n
,
{\displaystyle {\frac {f^{(n)}(a)}{n!}}(x-a)^{n},}
n
!
f
(
n
)
(
a
)
​
(
x
−
a
)
n
,
where
f
(
n
)
(
a
)
f^{(n)}(a)
f
(
n
)
(
a
)
is the
n
n
n
-th derivative of
f
f
f
at point
a
a
a
.
Testing
⌗
I test my implementation as follows:
It appears that my implementation is fairly close to being acceptably accurate, but I can make it better by increasing the Taylor polynomial degree to
n←7
:
Summary
⌗
I believe that this tiny Taylor Series implementation in APL is somewhat unique, since it conveys many concepts of mathematics in an almost verbatim way. There’s an incredibly obvious link to notice between the last line of my implementation:
… and the actual mathematical formula:
∑
n
=
0
∞
f
(
n
)
(
a
)
n
!
(
x
−
a
)
n
,
{\displaystyle \sum _{n=0}^{\infty }{\frac {f^{(n)}(a)}{n!}}(x-a)^{n},}
n
=
0
∑
∞
​
n
!
f
(
n
)
(
a
)
​
(
x
−
a
)
n
,
It’s a proof (or rather a demonstration) of sorts that APL is well-suited for representing concepts in mathematics that overlap with numerical methods and actual computation. Finally, the full source code follows:
