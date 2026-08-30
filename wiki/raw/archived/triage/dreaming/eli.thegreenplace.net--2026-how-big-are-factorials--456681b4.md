---
title: "How big are factorials?"
url: "https://eli.thegreenplace.net/2026/how-big-are-factorials/"
fetched_at: 2026-08-28T10:01:35.787611+00:00
source: "eli.thegreenplace.net"
tags: [blog, raw]
---

# How big are factorials?

Source: https://eli.thegreenplace.net/2026/how-big-are-factorials/

August 27, 2026 at 18:52
Tags
Math
The other day, I found myself wondering how big 52! (52 factorial) is,
and that led me to ponder how these could be estimated without a
calculator or a computer.
It turns out there’s some fairly interesting math behind being able to
estimate the size (number of digits) of a factorial reasonably
accurately. This post will start by stating how to do the estimate, and
if you’re curious you can read on for the math background.
Without further ado, the approximation is:
\[\text{number of digits in n!}\approx n\log_{10}\left(\frac{n}{e}\right)+2\]
As an example, let’s use my original question, by estimating this for
52!
Well, 52 divided by
e
is... 20-ish? And
\log_{10}(20)
is
about 1.3  ; therefore our estimate comes out to:
\[\text{number of digits in 52!}\approx 52\cdot 1.3 +2 \approx69\]
The real answer is 68, so this is very close! In estimates like this -
when you’re dealing with enormous numbers - being off by a couple of
digits usually isn't a big deal.
The Gamma function
The Gamma function for real
n>0
is defined  as:
\[\Gamma(n)=\int_{0}^{\infty}x^{n-1}e^{-x}dx\]
This integral does not have an analytic expression in the general case,
but it does have a very useful property that we can take advantage of.
Let’s see what
\Gamma(n+1)
is:
\[\Gamma(n+1)=\int_{0}^{\infty}x^{n}e^{-x}dx\]
And now use integration by parts with:
\[u=x^n\qquad v=-e^{-x}\]
Then:
\[du=nx^{n-1} dx\qquad dv=e^{-x}dx\]
So:
\[\begin{aligned}
    \Gamma(n+1)&=\int_{0}^{\infty}x^{n}e^{-x}dx\\
    &=\left. -x^n e^{-x}\right|_{0}^{\infty}-\int_{0}^{\infty}-e^{-x}n x^{n-1}dx\\
    &=n\int_{0}^{\infty}x^{n-1}e^{-x}dx
\end{aligned}\]
But notice that the last integral is just
\Gamma(n)
; therefore,
we’ve shown that:
\[\Gamma(n+1)=n\Gamma(n)\]
Let’s also calculate
\Gamma(1)
- it’s a special case that has an
analytical solution:
\[\Gamma(1)=\int_{0}^{\infty}e^{-x}dx=\left. -e^{-x}\right|_{0}^{\infty}=1\]
This helps establish an induction argument:
\[\begin{aligned}
    \Gamma(2)=1\cdot\Gamma(1)&=1!\\
    \Gamma(3)=2\cdot\Gamma(2)&=2!\\
    \Gamma(4)=3\cdot\Gamma(3)&=3!\\
    \dots\\
    \Gamma(n+1)=n\cdot\Gamma(n)&=n!
\end{aligned}\]
In other words - the Gamma function is an interpolation of the factorial
over all positive reals. Here’s a plot of the Gamma function over a
small range; note that the y axis is log-scale because of the function’s
fast growth:
Stirling’s approximation
You may have encountered Stirling’s approximation before:
\[n!\approx\sqrt{2\pi n}\cdot\left(\frac{n}{e} \right)^n\]
It’s a great approximation that works reasonably well even for small
. This section is a brief overview of how Stirling’s formula is
derived from the Gamma function.
Taking:
\[n!=\Gamma(n+1)=\int_{0}^{\infty}x^n e^{-x}dx\]
We’ll start by massaging the integrand a bit:
\[n!=\int_{0}^{\infty}x^n e^{-x}dx=\int_{0}^{\infty}e^{n \ln x} e^{-x}dx\]
And making a change of variables
x=ny
, which means that
dx=ndy
:
\[\begin{aligned}
    n!&=\int_{0}^{\infty}ne^{n\ln(ny) - ny}dy=n\int_{0}^{\infty}e^{n(\ln n+\ln y-y)}dy\\
    &=ne^{n\ln n}\int_{0}^{\infty}e^{n(\ln y-y)}dy
\end{aligned}\]
These steps make the integral amenable to applying
Laplace’s
method
, which allows
us to approximate definite integrals of the form:
\[\int_{a}^{b}e^{nf(x)}dx\]
Where
is a twice-differentiable function and
some
large number. By Laplace’s method, such integrals can be approximated
by:
\[\int_{a}^{b}e^{nf(x)}dx\approx\sqrt{\frac{2\pi}{n|f''(x_0)|}}e^{n f(x_0)}\]
Where
is the global maximum of
.
Let’s see how to apply this method  to the latest equation we have
for
n!
(renaming the dummy integration variable back to
x
):
\[n!=ne^{n\ln n}\int_{0}^{\infty}e^{n(\ln x-x)}dx\]
In our case,
f(x)=\ln x - x
. It’s easy to show that this
function is twice differentiable and has a global maximum at
. Moreover:
\[\begin{aligned}
    f(x_0)&=-1\\
    f''(x_0)&=-1\\
\end{aligned}\]
Substituting these into the proper places in Laplace’s approximation, we
get:
\[\begin{aligned}
    n! &\approx ne^{n\ln n}\sqrt{\frac{2\pi}{n}}e^{-n}\\
    &\approx \sqrt{2\pi n}\cdot e^{n(\ln n - 1)}\\
    &\approx \sqrt{2\pi n}\cdot \left(\frac{n}{e}\right)^n\quad\blacksquare
\end{aligned}\]
Number of digits from Stirling’s approximation
We can calculate the number of digits in
n!
by taking the
base-10 logarithm of Stirling’s formula:
\[\begin{aligned}
\text{number of digits in n!}&\approx \log_{10} \left(\sqrt{2\pi n}\cdot
 \left(\frac{n}{e}\right)^n\right)\\
&\approx \log_{10}\left(\sqrt{2\pi n}\right)+ \log_{10}\left(\frac{n}{e}\right)^n\\
&\approx \log_{10}\left(\sqrt{2\pi n}\right)+ n\cdot \log_{10}\left(\frac{n}{e}\right)
\end{aligned}\]
Note that the first term is not multiplied by
itself;
therefore, as
grows, it will become less and less noticeable.
That said, it still adds a couple of digits - so you should take it into
account if you want a more accurate approximation
