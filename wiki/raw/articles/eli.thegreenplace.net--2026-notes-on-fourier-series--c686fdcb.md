---
title: "Notes on Fourier series"
url: "https://eli.thegreenplace.net/2026/notes-on-fourier-series/"
fetched_at: 2026-05-28T07:00:50.616803+00:00
source: "eli.thegreenplace.net"
tags: [blog, raw]
---

# Notes on Fourier series

Source: https://eli.thegreenplace.net/2026/notes-on-fourier-series/

May 27, 2026 at 19:30
Tags
Math
The trigonometric Fourier series is a beautiful mathematical theory that
shows how to decompose a periodic function into an infinite sum of
sinusoids. These are my notes on the subject, with some examples and the
connection to linear algebra in Hilbert space.
Coefficients of Fourier series
Let’s assume that
is a
well-behaved
2L
-periodic 
function and that we can find coefficients
a_n
and
b_n
such that:
\[f(x)=\sum_{n=0}^{\infty}\left(a_n cos\frac{n\pi x}{L}+b_n sin\frac{n\pi x}{L}\right)\]
Then we say that the
Fourier series
on the right-hand side converges
to
. We’ll talk more about the assumptions mentioned above
and convergence in the next section.
Note that when
n=0
, the sum becomes just
; therefore
it’s customary to write the series starting with
n=1
, with a
separate constant component (which is the function's average over
one period). To make computations nicer, this constant is typically
called
a_0 / 2
, so:
\[f(x)=\frac{a_0}{2}+\sum_{n=1}^{\infty}\left(a_n cos\frac{n\pi x}{L}+b_n sin\frac{n\pi x}{L}\right)\]
Our goal is to find the coefficients
a_n
and
b_n
that
satisfy this equation. We’ll do this in three steps.
Step 1:
Integrate both sides of the equation between
-L
and
L
.
\[\int_{-L}^{L}f(x)dx=\int_{-L}^{L}\frac{a_0}{2}dx+\sum_{n=1}^{\infty}\bigg (\int_{-L}^{L}a_n cos\frac{n\pi x}{L}dx+\int_{-L}^{L}b_n sin\frac{n\pi x}{L}dx\bigg )\]
Per Appendix A, all integrals within the sum are zero, so we’re left
with:
\[\int_{-L}^{L}f(x)dx=\int_{-L}^{L}\frac{a_0}{2}dx=\bigg[\frac{x\cdot a_0}{2}\bigg]_{-L}^{L}=a_0\cdot L\]
And thus we find
:
\[a_0=\frac{1}{L}\int_{-L}^{L}f(x)dx\]
Step 2:
Multiply both sides by
cos\frac{m\pi x}{L}
(
m
is a positive integer constant) and integrate between
-L
and
L
.
\[\begin{aligned}
    \int_{-L}^{L}f(x)cos\frac{m\pi x}{L}dx&=\int_{-L}^{L}\frac{a_0}{2}cos\frac{m\pi x}{L}dx\\
    &+\sum_{n=1}^{\infty}\bigg (\int_{-L}^{L}a_n cos\frac{n\pi x}{L}cos\frac{m\pi x}{L}dx+\int_{-L}^{L}b_n sin\frac{n\pi x}{L}cos\frac{m\pi x}{L}dx\bigg )
\end{aligned}\]
Looking at the right-hand side, the first integral is zero per Appendix
A, and the last integral is zero per Appendix B. We’re left with:
\[\int_{-L}^{L}f(x)cos\frac{m\pi x}{L}dx=\sum_{n=1}^{\infty}\int_{-L}^{L}a_n cos\frac{n\pi x}{L}cos\frac{m\pi x}{L}dx\]
Per Appendix B, the integral on the right is zero for all
n\neq m
, and
L
for
n=m
. Therefore, we can write:
\[\int_{-L}^{L}f(x)cos\frac{m\pi x}{L}dx=a_m\cdot L\]
Recall that
m
is an arbitrary integer, just like
; for
consistency, we’ll replace
m
by
and isolate
a_n
:
\[a_n=\frac{1}{L}\int_{-L}^{L}f(x)cos\frac{n\pi x}{L}dx\]
Step 3:
Hopefully it’s clear where this is going now; multiply both
sides by
sin\frac{m\pi x}{L}
and integrate between
-L
and
L
. Using a very similar reasoning to step 2, we’ll end up
with:
\[b_n=\frac{1}{L}\int_{-L}^{L}f(x)sin\frac{n\pi x}{L}dx\]
We’ve just found a way to calculate all the coefficients of our Fourier
series for
:
\[f(x)=\frac{a_0}{2}+\sum_{n=1}^{\infty}\left(a_n cos\frac{n\pi x}{L}+b_n sin\frac{n\pi x}{L}\right)\]
Where:
\[\begin{aligned}
    a_0&=\frac{1}{L}\int_{-L}^{L}f(x)dx\\
    a_n&=\frac{1}{L}\int_{-L}^{L}f(x)cos\frac{n\pi x}{L}dx\\
    b_n&=\frac{1}{L}\int_{-L}^{L}f(x)sin\frac{n\pi x}{L}dx
\end{aligned}\]
Conditions on
f
and convergence of Fourier series
The previous section discusses Fourier series for a function
that is
well-behaved
- but what does that mean? The full
answer would lead us deep into analysis, which I’d like to avoid here.
So I’ll keep it brief.
We typically assume that
is
square
integrable
,
which is denoted as
L^2
. Moreover, we assume that the function
is
piecewise
smooth
: each
segment of the function has continuous derivatives. A very simple
example of a piecewise smooth function is
f(x)=|x|
. Another is
the triangular wave function used in the example below.
These conditions hold for pretty much any reasonable function we want to
approximate using Fourier series, so they aren’t a serious burden.
For a function
that satisfies these conditions, it’s
guaranteed to have a Fourier series that
pointwise converges
to it.
This means that at every continuous point of
, the Fourier
series converges to it exactly; at every jump point, the Fourier series
converges to the mid-point of the jump.
Cosine and Sine series
Sometimes, additional properties of the function
can help
us simplify the Fourier series for it. If
f_e(x)
is an
even
function
,
then we know that:
\[b_n=\frac{1}{L}\int_{-L}^{L}f(x)sin\frac{n\pi x}{L}dx=0\]
Because the function inside the integral is odd, and integrating an
odd function over a symmetric interval results in 0.
Therefore, the Fourier series for such
f_e(x)
is a
cosine
series
:
\[f_e(x)=\frac{a_0}{2}+\sum_{n=1}^{\infty}a_n cos\frac{n\pi x}{L}\]
With coefficients
and
a_n
given as before.
Similarly if
f_o(x)
is an
odd
function, then its
and
a_n
are 0, and its Fourier series is a
sine series
:
\[f_o(x)=\sum_{n=1}^{\infty}b_n sin\frac{n\pi x}{L}\]
Fourier series for a non-periodic function defined on an interval
So far we’ve been talking about
2L
-periodic functions that can
be faithfully represented by Fourier series. But what if we have a
non-periodic function defined on a finite interval?
E.g. suppose we have
f(x)=x
on the interval
[0,L]
. Can
we approximate it with a Fourier series?
Yes! First, we have to make a choice of how to extend the function to
the negative interval
[-L,0]
. Then, we simply repeat the
function every
2L
- this is called a
periodic extension
. Note
that the Fourier series calculation only cares about the range
[-L,L]
. The resulting series will approximate the generated
periodic function in its entirety, and in particular will also converge
to it in the
[0,L]
interval (except maybe the endpoints,
depending on the mode of extension).
There are several natural ways to extend a function defined on
[0,L]
into the interval
[-L,0]
:
Direct periodic repetition: we simply repeat
every
L
:
f(x+L)=f(x)\ \forall x
.
Even extension:
f(|x|)
Odd extension:
when
x\ge 0
and
-f(-x)
when
x<0
.
Here’s an example of extending our sample function
f(x)=x
onto
the full interval
[-L,L]
and then repeating it periodically
every
2L
:
Your browser does not support the HTML5 canvas tag.
Note that the Fourier series for these extended functions will be
different. However, they will all converge to
in the
interval
[0,L]
. Typically, even and odd extensions have the
benefit of producing either cosine or sine series, correspondingly (as
discussed in the previous section).
We’ve seen that Fourier series work well for periodic functions and also
non-periodic functions defined on a finite domain (because we can extend
these periodically). But what about aperiodic functions defined on the
entire real line? This is where we’ll have to leave Fourier series
behind and move on to their generalization - the
Fourier transform
;
this will be a topic for a separate post.
Example
Let’s take the following triangular function
t(x)
:
Your browser does not support the HTML5 canvas tag.
t(x)
is periodic with period 4. We can define it by starting
with a formula on the interval
[0,2]
:
\[t(x)=
\begin{cases}
    x     &  0 \leq x \leq 1 \\
    2-x   &  1 < x \leq 2  \\
\end{cases}\]
Then making an odd extension into
[-2,0]
and repeating it
periodically. Now we can go ahead to calculate its Fourier coefficients.
Since this function is odd, we know that we’ll get a
sine series
, as
a_n
are going to be 0 for all
. Let’s calculate
b_n
; in our case
L=2
(half the period).
\[b_n=\frac{1}{2}\int_{-2}^{2}t(x)sin\frac{n\pi x}{2}dx\]
Since
t(x)
is odd and so is the sine, we’re integrating an even
function over a symmetric interval. Therefore, we only have to integrate
on the positive half of the range and multiply the result by two:
\[b_n=\int_{0}^{2}t(x)sin\frac{n\pi x}{2}dx\]
Let’s set
k=\frac{n\pi}{2}
:
\[b_n=\int_{0}^{2}t(x)sin(kx)dx\]
And split up the integral for the different segments of
t(x)
:
\[b_n=\int_{0}^{1}x\cdot sin(kx)dx+\int_{1}^{2}(2-x)sin(kx)dx\]
The first integral, by the method described in Appendix C:
\[I_1=\int_{0}^{1}x\cdot sin(kx)dx=\bigg[\frac{-x cos(kx)}{k}+\frac{sin(kx)}{k^2} \bigg]_{0}^{1}=\frac{sin(k)}{k^2}-\frac{cos(k)}{k}\]
The second integral can also be split into two:
\[I_2=\int_{1}^{2}2sin(kx)dx - \int_{1}^{2}x\cdot sin(kx)dx\]
The first of these is trivial to calculate; the second can once again
use Appendix C. After some tedious but straightforward calculations 
we’ll get:
\[I_2=\frac{cos(k)}{k}+\frac{sin(k)-sin(2k)}{k^2}\]
Adding
I_1+I_2
, we get:
\[\begin{aligned}
b_n=I_1+I_2&=\frac{sin(k)}{k^2}-\frac{cos(k)}{k}+\frac{cos(k)}{k}+\frac{sin(k)-sin(2k)}{k^2}\\
&=\frac{2sin(k)-sin(2k)}{k^2}
\end{aligned}\]
Now let’s substitute
k=\frac{n\pi}{2}
back. This makes
sin(2k)
zero because the sine of an integer multiple of
\pi
is always zero:
\[b_n=\frac{2sin \frac{n\pi}{2}}{\left (\frac{n\pi}{2}\right )^2}=\frac{8sin \frac{n\pi}{2}}{n^2\pi^2}\]
We have
b_n
, so the Fourier series for our
t(x)
is:
\[t(x)=\sum_{n=1}^{\infty}\frac{8}{n^2\pi^2}sin\frac{n\pi}{2}sin\frac{n\pi x}{2}\]
Note that for even values of
,
sin \frac{n\pi}{2}
is
zero, so only the odd terms remain:
\[t(x)=\frac{8}{\pi^2}\bigg[ sin\frac{\pi x}{2}-\frac{1}{3^2} sin\frac{3\pi x}{2}+\frac{1}{5^2}sin\frac{5\pi x}{2}-\cdots\bigg]\]
Here’s an interactive chart showing how the series
t(x)
converges to our triangular function. You can set the number of terms in
the Fourier series and see the effect (red line). Note that all even
coefficients are zero so it will look the same for
as for
n-1
when
is odd.
Your browser does not support the HTML5 canvas tag.
Compact formula using a single phase-shifted sinusoid
We’ve written the Fourier series for
as follows so far:
\[f(x)=\frac{a_0}{2}+\sum_{n=1}^{\infty}\left(a_n cos\frac{n\pi x}{L}+b_n sin\frac{n\pi x}{L}\right)\]
We can rewrite this in a somewhat more compact form, using a single
sinusoid with a configurable phase at each
:
\[f(x)=\frac{a_0}{2}+\sum_{n=1}^{\infty}q_n\cdot cos\left(\frac{n\pi x}{L}+\theta_n\right)\]
Based on Appendix D,
q_n
and
\theta_n
can be computed as
follows:
\[\begin{aligned}
    q_n&=\sqrt{a_n^2+b_n^2}\\
    \theta_n&=\operatorname{atan2}(-b_n,a_n)
\end{aligned}\]
When Fourier series are used in the context of signal processing, this
formulation is easier to reason about because it represents the
magnitude and phase shift of each harmonic of
in the
frequency domain
Complex Fourier series
It should not come as a surprise that the Fourier series, being a
combination of trigonometric functions, can also be represented with
complex exponential functions.
Specifically, we’ll show that our
can be approximated as
follows:
\[f(x)=\sum_{n=-\infty}^{\infty}C_n\cdot e^{in\pi x/L}\]
Let’s calculate
C_n
. We proceed in a manner similar to before,
by multiplying both sides of the equation by
e^{-im\pi x/L}
and
taking an integral in the range
[-L,L]
:
\[\begin{aligned}
\int_{-L}^{L}f(x)e^{-im\pi x/L}dx&=\sum_{n=-\infty}^{\infty}\int_{-L}^{L}C_n\cdot e^{in\pi x/L}e^{-im\pi x/L}dx\\
&=\sum_{n=-\infty}^{\infty}\int_{-L}^{L}C_n\cdot e^{i(n-m)\pi x/L}dx
\end{aligned}\]
By Appendix A, the sum elements are all zero when
n\neq m
. When
n=m
, we get:
\[\int_{-L}^{L}f(x)e^{-im\pi x/L}dx=\int_{-L}^{L}C_m\cdot 1 \cdot dx=2LC_m\]
Therefore, renaming
m
to
(since it’s just an arbitrary
integer constant):
\[C_n=\frac{1}{2L}\int_{-L}^{L}f(x)e^{-in\pi x/L}dx\]
We’ve found an alternative formulation to Fourier series, using complex
exponentials instead of trigonometric functions. While this was a direct
derivation, another way to achieve the same result is to use the
Euler
Formula
to derive:
\[\begin{aligned}
    cos\theta&=\frac{e^{i\theta}+e^{-i\theta}}{2}\\
    sin\theta&=\frac{e^{i\theta}-e^{-i\theta}}{2i}
\end{aligned}\]
And substitute these into the original Fourier series formula. I’ll
leave this as an exercise for the diligent reader; eventually, the
result will be the same. Moreover, it’s possible to show a direct
correspondence between
a_n
,
b_n
and
C_n
, for
n>0
:
\[\begin{aligned}
    C_0&=\frac{a_0}{2}\\
    C_n&=\frac{a_n-ib_n}{2}\\
    C_{-n}&=\frac{a_n+ib_n}{2}\\
\end{aligned}\]
Note that
C_{-n}=C_n^*
when both
a_n
and
b_n
are
real (which is the case for a real-valued
). This helps
explain why the complex formulation has negative frequencies in the sum;
when the function is actually real, each negative frequency is paired up
with a positive frequency and the result is real :
\[\begin{aligned}
C_n e^{in\pi x/L}+C_{-n} e^{-in\pi x/L}&=C_n e^{in\pi x/L}+C_n^* e^{-in\pi x/L}\\
&=C_n e^{in\pi x/L}+\left(C_{n} e^{in\pi x/L}\right)^*\\
&=2\operatorname{Re}\bigg(C_{n} e^{in\pi x/L}\bigg)
\end{aligned}\]
So, for a real function we only need to account for positive
frequencies:
\[f(x)=C_0+\sum_{n=1}^{\infty}2\operatorname{Re}\bigg(C_{n} e^{in\pi x/L}\bigg)\]
We can take it further.
C_n
is a complex number, so let’s
represent it in polar form as
C_n=\frac{q_n}{2} e^{i\theta_n}
(the factor of half will make sense soon). Then:
\[\begin{aligned}
\operatorname{Re}\bigg(C_{n} e^{in\pi x/L}\bigg)&=\operatorname{Re}\bigg(\frac{q_n}{2} e^{i\theta_n}e^{in\pi x/L}\bigg)\\
&=\frac{q_n}{2}\operatorname{Re}\bigg(e^{i(n\pi x/L + \theta_n)}\bigg)\\
&=\frac{q_n}{2} cos\bigg(\frac{n\pi x}{L}+\theta_n\bigg)
\end{aligned}\]
And substituting back into the sum:
\[f(x)=C_0+\sum_{n=1}^{\infty}q_n cos\bigg(\frac{n\pi x}{L}+\theta_n\bigg)\]
This is precisely the compact formulation from the previous section!
Fourier orthogonal basis in Hilbert space
The most beautiful aspect of Fourier theory is that it doesn’t just
happen to work by chance, and is deeply connected to linear algebra.
Please read
my post on Hilbert
space
before proceeding.
The space of real-valued square integrable functions
L^2
forms a
Hilbert space, in which we can define the inner product (assuming real
functions):
\[\langle f,g \rangle=\int_{-L}^{L}f(x)g(x) dx\]
We’ve demonstrated that the family of functions:
\[1,\qquad cos\frac{n\pi x}{L},\qquad sin\frac{n\pi x}{L}\]
Are all mutually orthogonal, because their pairwise inner products are
zero! We’ve also shown that any function in
L^2
can be
represented as a weighted sum of these functions:
\[f(x)=\frac{a_0}{2}+\sum_{n=1}^{\infty}\left(a_n cos\frac{n\pi x}{L}+b_n sin\frac{n\pi x}{L}\right)\]
So these functions form a
basis
for
L^2
. When we think of
these functions as vectors (in an infinite Hilbert space), much of what
we did in this post starts feeling like "normal" linear algebra. For
example, when we have a set of basis vectors and we want to know how to
represent some vector
in this basis, we usually find the
coefficients by
projecting
it
onto the basis. E.g. with a basis vector
e_1
, the coefficient of
:
\[c=\frac{\langle v, e_1\rangle}{\langle e_1, e_1\rangle}\]
Similarly, when we calculate the coefficient
b_n
for some
function
, we project
onto the basis vector
sin\frac{n\pi x}{L}
by calculating:
\[b_n=\frac{\langle f(x), sin\frac{n\pi x}{L}\rangle}{\langle sin\frac{n\pi x}{L}, sin\frac{n\pi x}{L}\rangle}\]
From Appendix B, we know that the denominator is
L
, and we’ve
just denoted:
\[\langle f(x), sin\frac{n\pi x}{L}\rangle=\int_{-L}^{L}f(x)sin\frac{n\pi x}{L}dx\]
So we get:
\[b_n=\frac{1}{L}\int_{-L}^{L}f(x)sin\frac{n\pi x}{L}dx\]
Which should look familiar!
This is the core linear-algebra idea behind Fourier series: the
functions
1
,
cos\frac{n\pi x}{L}
, and
sin\frac{n\pi x}{L}
play the role of orthogonal basis vectors,
while the Fourier coefficients are coordinates of
in this
basis. The integral formulas for
a_n
and
b_n
are not
mysterious tricks; they are projections, just like dot products with
basis vectors in ordinary Euclidean space.
Fourier series therefore let us decompose a function into independent
orthogonal directions, much like decomposing a vector into its
,
, and
z
components.
Appendix A: Integrals of sinusoids
For any integer
n\neq 0
and an arbitrary constant L, we have:
\[\begin{aligned}
\int_{-L}^{L}cos\frac{n\pi x}{L}dx&=\bigg[\frac{L}{n\pi}sin\frac{n\pi x}{L}\bigg]_{-L}^{L}\\
&=\frac{L}{n\pi}(sin(n\pi)-sin(-n\pi))=0
\end{aligned}\]
Similarly:
\[\begin{aligned}
\int_{-L}^{L}sin\frac{n\pi x}{L}dx&=\bigg[\frac{-L}{n\pi}cos\frac{n\pi x}{L}\bigg]_{-L}^{L}\\
&=\frac{-L}{n\pi}\left(cos(n\pi)-cos(-n\pi)\right)=0
\end{aligned}\]
Using these, we can calculate the integral of a complex exponential
function for an integer
n\neq 0
:
\[\begin{aligned}
\int_{-L}^{L}e^{in\pi x/L}dx=\int_{-L}^{L}\bigg[ cos\frac{n\pi x}{L} +i\cdot sin\frac{n\pi x}{L}\bigg] dx=0
\end{aligned}\]
Appendix B: Integrals of products of sinusoids
We’ll start with the product of two sines, for any positive integers
m
and
:
\[ss=\int_{-L}^{L}sin\frac{m\pi x}{L}\cdot sin\frac{n\pi x}{L}dx\]
Using the trigonometric identity for a product of sines, we can write:
\[\begin{aligned}
    ss&=\frac{1}{2}\int_{-L}^{L}\bigg(cos\frac{(m-n)\pi x}{L}-cos\frac{(m+n)\pi x}{L}\bigg)dx\\
    &=\frac{1}{2}\int_{-L}^{L}cos\frac{(m-n)\pi x}{L}dx-\frac{1}{2}\int_{-L}^{L}cos\frac{(m+n)\pi x}{L}dx
\end{aligned}\]
Now let’s focus on two different scenarios,
m\neq n
and
m=n
.
If
m\neq n
, then each of the integrals constituting
ss
are 0
(see on Appendix A), so
ss=0
.
If
m=n
, then the second integral is still 0, but the first one
isn’t:
\[\begin{aligned}
    ss&=\frac{1}{2}\int_{-L}^{L}cos\frac{0\pi x}{L}dx\\
    &=\frac{1}{2}\int_{-L}^{L}1dx=L
\end{aligned}\]
Therefore:
\[ss=\int_{-L}^{L}sin\frac{m\pi x}{L}\cdot sin\frac{n\pi x}{L}dx=
\begin{cases}
    L      & m = n \\
    0      & m \neq n
\end{cases}\]
We can use exactly the same approach to show that:
\[cc=\int_{-L}^{L}cos\frac{m\pi x}{L}\cdot cos\frac{n\pi x}{L}dx=
\begin{cases}
    L      & m = n \\
    0      & m \neq n
\end{cases}\]
One more variant to cover:
\[sc=\int_{-L}^{L}sin\frac{m\pi x}{L}\cdot cos\frac{n\pi x}{L}dx\]
Since sine is an odd function and cosine is an even function, their
product is an odd function. And the integral of an odd function over a
symmetric interval is 0 (see
this post for more
details
).
Therefore:
\[sc=\int_{-L}^{L}sin\frac{m\pi x}{L}\cdot cos\frac{n\pi x}{L}dx=0\]
Appendix C: A useful integral
Let’s calculate the indefinite integral:
\[I=\int x\cdot sin(kx) dx\]
For some constant
k
. We’ll use integration by parts:
\[\int u\cdot dv =u\cdot v - \int v\cdot du\]
Here
u=x
, so
du=dx
. Also
dv=sin(kx)
, so
v=-\frac{cos(kx)}{k}
.
Putting it together:
\[I=\frac{-x\cdot cos(kx)}{k}+\int \frac{cos(kx)}{k} dx=\frac{-x\cdot cos(kx)}{k}+\frac{sin(kx)}{k^2}\]
Appendix D: Sinusoid with phase as a sum of sin and cos
Let’s take a general sinusoid with magnitude
q
, frequency
and phase
:
\[s(x)=q\cdot cos(wx+\theta)\]
We’re going to show that
s(x)
can be represented as a sum of a
sine
and a
cosine
with no phase. This is related to
my earlier post
on the sum of same-frequency
sinusoids
.
Let’s start by expanding
s(x)
using a trigonometric identity:
\[s(x)=q\cdot cos(\theta)cos(wx)-q\cdot sin(\theta)sin(wx)\]
Now we’ll denote:
a=q\cdot cos(\theta)
and
b=-q\cdot sin(\theta)
, so:
\[s(x)=a\cdot cos(wx)+b\cdot sin(wx)\]
We have
a
and
b
in terms of
q
and
, but what about the other way around?
Let’s take the equations:
\[\begin{aligned}
    a&=q\cdot cos(\theta)\\
    b&=-q\cdot sin(\theta)
\end{aligned}\]
Square both of them and add together:
\[\begin{aligned}
    a^2+b^2&=q^2\cdot(cos^2(\theta)+sin^2(\theta))=q^2\\
    &\Rightarrow q=\sqrt{a^2+b^2}
\end{aligned}\]
Now we’ll take the equations for
b
and
a
and divide one
by the other:
\[\begin{aligned}
    \frac{b}{a}&=\frac{-sin(\theta)}{cos(\theta)}\\
    &\Rightarrow\theta=\operatorname{atan2}(-b,a)
\end{aligned}\]
Where
the atan2 function
is
careful to take into account the sign of both numerator and denominator.
Also it’s worth mentioning that
is determined up to
additions of
2\pi
.
To conclude, for any
q
,
and
:
\[q\cdot cos(wx+\theta)=a\cdot cos(wx)+b\cdot sin(wx)\]
With the aforementioned conversion formulas for
a
,
b
.
