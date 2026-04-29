---
title: "What's the deal with Euler's identity?"
url: "https://lcamtuf.substack.com/p/whats-the-deal-with-eulers-identity"
fetched_at: 2026-04-29T07:02:09.122392+00:00
source: "lcamtuf.substack.com"
tags: [blog, raw]
---

# What's the deal with Euler's identity?

Source: https://lcamtuf.substack.com/p/whats-the-deal-with-eulers-identity

Perhaps the most famous equation in pop mathematics is Euler’s identity:
The equation is deemed profound because it combines not one, not two, but five “special” mathematical constants:
e
,
π
, 0, 1, and the imaginary unit
i.
The identity is a special case of an equation known as Euler’s formula:
\(e^{i \alpha} = cos(\alpha) + i \cdot sin(\alpha)\)
The identity form is what you get if you choose an angle of
α
=
π
in radians (180°). This makes the cosine expression equal to -1 and the sine part equal to zero, so the final result of the substitution is:
Now, four “special” values is still weak sauce, so we move -1 to the left to increase the profoundness factor by another 25%.
There are multiple “easy” proofs of Euler’s formula you can find on YouTube, but they all involve sleight of hand: they make unobvious assertions about infinite series and function derivatives, or rely on a circular definition of complex numbers. I don’t have a proof that will fit on a napkin, but I think there’s a reasonably intuitive way to reason about what the equation does.
Imagine a point in a Cartesian coordinate system that lies on the horizontal axis at a distance
l
from the center. If you wish to rotate this point by an angle
α
in radians, you can calculate the new
(x, y)
coordinates using simple trigonometry:
\(\begin{align}
x_{rotated} = l \cdot cos(\alpha) \\
y_{rotated} = l \cdot sin(\alpha) 
\end{align}\)
Less obviously, there is also a way to rotate points without trigonometric functions. If we take point
(x, y)
and flip the signs of the individual coordinates —
(-x, -y)
— we always achieve what looks like a rotation by 180°:
180° rotation by multiplying coordinates by -1.
The sign-flipping operation is equivalent to multiplication by -1. Changing the magnitude of the negative multiplier doesn’t result in a different rotation angle; it’s the “negative unit" itself (-1) that appears to be doing the hard work. If we want to achieve a rotation by 360°, we need to multiply the coordinates by -1 twice; the pattern extends in a pretty obvious way:
\(\begin{align}
(x, y) \cdot (-1)^0 &\rightarrow 0^\circ \\
(x, y) \cdot (-1)^1 &\rightarrow 180^\circ \\
(x, y) \cdot  (-1)^2 &\rightarrow 360^\circ \\
(x, y) \cdot  (-1)^3 &\rightarrow 540^\circ \\
(x, y) \cdot  (-1)^4 &\rightarrow 720^\circ \\
... \\
(x, y) \cdot  (-1)^m &\rightarrow 180^\circ \cdot m \\


\end{align}\)
This leads to a peculiar realization: it would appear that to achieve rotations of less than 180°, we could raise -1 to a fractional power. In particular, to obtain 90°, we seemingly need an exponent halfway between (-1)
0
and (-1)
1
. In other words, we need to multiply the coordinates by (-1)
½
. This multiplier, known as
i,
can be also written as √(-1).
The number
i
is not a real. That’s not to say that it doesn’t exist; it just isn’t a member of the set of real numbers, ℝ. The construct lets us represent the coordinates of any point (
x, y
) as a single compound (“complex”) number:
The first part corresponds to the distance along the horizontal axis. The second (
i-
coupled) value is a number that’s evidently “rotated” by 90° — i.e., it represents the distance along the vertical axis.
This might sound unhinged, but the result is a coherent model of 2D geometry, and standard algebra extends to this
i
-containing realm in a pretty straightforward way. For the most part, you just work on the two halves of a complex number separately, keeping in mind that
i · i = -1.
With the
z = x + iy
construction in tow, let’s go back to the earlier method of rotating a segment of length
l
by an angle
α:
\(\begin{align}
x_{rotated} = l \cdot cos(\alpha) \\
y_{rotated} = l \cdot sin(\alpha) 
\end{align}\)
Nothing stops us from combining these coordinates into a single complex number
z
that represents the
x
and
y
coordinates of the rotated point:
\(z = \underbrace{l \cdot cos(\alpha)}_{\substack{\textrm{horizontal} \\ \textrm{distance}}} + i \cdot \underbrace{l \cdot sin(\alpha)}_{\substack{\textrm{vertical} \\ \textrm{distance}}}\)
Equivalently, as discussed earlier on, we can express rotation by
m
· 90° by multiplying the starting length
l
by the correct power of
i
:
In the first equation, the angle of rotation (
α)
is expressed in radians, so a full 360° turn is achieved when
α = 2π
. In the second version, it’s expressed in 90° increments, so a full rotation is
m =
4. To reconcile these equations, we need to toss in the appropriate scaling factor. If we do it on the
i
m
side to settle on radians, we get:
\(l \cdot i^{2/ \pi \cdot \alpha} = l \cdot [ cos(\alpha) + i \cdot  sin(\alpha) ]\)
This can be further simplified by choosing
l
= 1, essentially building a model of a point moving along a unit circle with a radius of one:
\(i^{2/ \pi \cdot \alpha} = cos(\alpha) + i \cdot sin(\alpha)\)
The equation is already in the same ballpark as Euler’s formula, but we’re not quite done yet.
In the realm of real numbers, exponentiation that uses one positive base other than 1 can be rewritten in another base simply by tossing in an appropriate scaling factor in the exponent. For example, we can write the following:
The scaling factor is just the logarithm of the old base in the new base:
log
2
(8)
= 3.
Logarithms can be seamlessly extended to complex numbers, allowing us to move between real and imaginary bases in exponentiation. As a trivial example, if
(-1)
½
= i
, we can infer that
log
-1
(i)
= ½
. Knowing this, we can apply the earlier rule to convert between an imaginary base
i
and a real base -1, with unsurprising results:
In the same vein, there exists a logarithm that nets us a scaling factor to move from base
i
to base 10
:
\(i^x = 10^{log_{10}(i) \cdot x}\)
The value of
log
10
(i)
can’t be a real number because if we choose
x =
2, the left-hand side works out to -1, and there’s no real
c
for which 10
c
is negative. That said, we can make this equivalence work with imaginary-number solutions, netting us a coherent algebra without any overt contradictions.
In that system, the value of
log
10
(i)
would need to work out to roughly 0.682·
i
, but we don’t need to know how to calculate it just yet. The point is just that the two earlier forms —
i
x
and 10
<some i-containing constant>·x
— can be considered equivalent. They both represent rotation by a chosen angle
in a two-dimensional space.
Before the segue into the properties of exponentiation, we established the following formula that equated two methods of rotating a point:
\(i^{2/ \pi \cdot \alpha} = cos(\alpha) + i \cdot sin(\alpha)\)
On the left side of the equation, we needed to toss in a 2/
π
scaling factor to convert from 90° increments to radians. It would be nice to switch to a different, real-number base
n
that naturally has the same rotation speed as the
cos + sin
expression. This would let us simplify the formula to:
\(n^{i \alpha} = cos(\alpha) + i \cdot sin(\alpha)\)
The
cos + sin
expression is drawing a circle with a radius of 1, completing one rotation every
2π
radians. The circumference of the unit circle is
2π
, so there is a 1:1 correspondence between the parameter of the expression (α) and the distance traveled by the moving point.
Again, we’d like to meet that rotation on the left side of the equation by choosing the right
n
so that there is a 1:1 relationship between the increment in α and the travel of the coordinate produced by exponentiation (
n
iα
).
As luck would have it, there is a well-known real base for which there is a 1:1 correspondence between the increment of
n
x
and the increment of the exponent near
x = 0
. It is, by definition, the mathematical constant
e
. If you’re unfamiliar with this property, it’s easy to show it numerically; if we choose a small Δ
x
= 0.0001 and calculate the rate of change near
x
= 0, we get:
\(\begin{array}{r l}
n = 2: & {{2^{\Delta x} - 2^0} \over \Delta x} \approx 0.69 \\
n = e: & {{e^{\Delta x} - e^0} \over \Delta x} \approx 1.00 \\
n = 4: & {{4^{\Delta x} - 4^0} \over \Delta x} \approx 1.39 \\
\end{array}\)
We can also illustrate this on a plot of
y
=
e
x
. The slope of the resulting curve is 45° near
x =
0, suggesting that the function briefly behaves the same as
y = x:
In the domain of real numbers, the rate of change of e
x
increases in tandem with the value of
x
; that’s the nature of exponential growth. But in the realm of complex numbers, we have already asserted that a real value raised
to an imaginary power results in constant-speed rotation, not runaway growth. We must conclude that the rate of change is dialed in solely by the real part of the exponent, which is always zero in the formula we’re trying to build.
This means that the scaling-factor-free solution we’re looking for is just:
\(e^{i \alpha} = cos(\alpha) + i \cdot sin(\alpha)\)
The observation also gives us the value of
log
e
(i) = ln(i)
. Per the earlier discussion, switching from
i
to base
e
entails multiplying the exponent by
log
e
(i).
In this instance, the multiplication evidently cancels out the 2/
π
factor associated with the original base, so
ln(i)
must be
π/2 · i
, or about
1.571 · i.
That’s it. Again, it’s not a real proof: the argument contains a couple of appeals to intuition. That said, I like this chain of thought better than the usual explanations found on the internet.
As to why all these constants come together, the basic answer is that complex numbers are a two-dimensional geometry — and that radians, i,
e,
and
π
describe similar things.
👉 For more articles about math,
visit this page
. In particular, you might enjoy:
I write well-researched, original articles about geek culture, electronic circuit design, algorithms, and more. If you like the content, please subscribe.
