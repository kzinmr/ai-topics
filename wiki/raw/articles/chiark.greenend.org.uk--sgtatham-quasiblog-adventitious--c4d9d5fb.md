---
title: "Brute-forcing Langley’s geometry problem with field extensions"
url: "https://www.chiark.greenend.org.uk/~sgtatham/quasiblog/adventitious/"
fetched_at: 2026-04-27T07:00:45.530268+00:00
source: "chiark.greenend.org.uk/~sgtatham"
tags: [blog, raw]
---

# Brute-forcing Langley’s geometry problem with field extensions

Source: https://www.chiark.greenend.org.uk/~sgtatham/quasiblog/adventitious/

Brute-forcing Langley’s geometry problem with field extensions
[Simon Tatham, 2025-07-18]
Introduction
Langley’s
      Adventitious Angles
is a notoriously difficult problem in
      elementary geometry. The challenge is to determine the angle
θ
in this diagram:
Langley’s geometry problem
It’s relatively easy to chase angles around the diagram and get
      this far:
All the easy bits filled in
But after this, it suddenly becomes difficult to make any more
      progress. We’ve filled in an expression for every angle we’ve
      got, and everything seems to make sense: the angles in each
      triangle and on each straight line add up to 180°. But in all
      the angle sums involving
θ
, the instances of
θ
appear with opposite signs and cancel out. So each of those sums
      will add up to 180° no matter
what
the value
      of
θ
is – and so none of them helps us to narrow down to
      a single answer.
Once you reach this point, you might be tempted to wonder if
      there even
is
a single answer. When a
      problem
doesn’t
have a unique solution, this is often
      what it looks like: you eliminate all but one variable,
      expressing everything else in terms of the remaining variable,
      and all your constraints seem to stay true regardless of the
      value of that variable. This is often the signature of a
      situation in which you can make an arbitrary choice of the
      variable, leading to a whole space of equally valid
      solutions.
But that can’t be true here, because the locations of all the
      points in the plane are completely determined, at least provided
      you choose an initial location and size for the overall
      80°–80°–20° isosceles triangle. Each of the two lines from a
      base vertex to the opposite edge is at a known angle, so there’s
      only one possible place it can intersect the opposite edge. And
      once every point in the diagram has a unique location, there’s
      no way the desired angle can have more than one value.
So one way you could ‘solve’ the problem would be to construct
      the diagram on paper, using a protractor, as accurately as
      possible, and then
measure
the target angle. Another
      approach would be to do the same thing in a computer, using
      trigonometry to calculate the
x
and
y
coordinates
      of every point – or to get a tool like GeoGebra to do the heavy
      lifting.
If you try that, it turns out that the angle looks like a nice
      round number of degrees. But you haven’t
proved
that it
      has that exact value: the ‘draw it on paper’ method only gives
      you an approximate answer, up to the limits of your own ability
      to draw and measure precisely. And even the computer approach
      using trigonometry will be limited by floating-point accuracy.
      So all you can say after doing it this way is that it
looks
      as if
the angle is exactly [this many] degrees.
In fact the problem is sometimes set with a specific rule that
      says “don’t use trigonometry”, because there
is
a
      solution using elementary geometry, involving a clever choice of
      extra construction lines to add to the figure. The Wikipedia
      link above shows the answer (at the time of writing) – but
      beware that the choice of extra construction lines depends
      crucially on what the starting angles are. There are variants of
      this problem in which the two internal lines make different
      angles with the base of the triangle, and for each of those
      variants, you might need a
different
clever insight.
My aim in this article is to show how you can solve this
      problem
without
a clever
      insight
. The method I’ll show is hard
      work – hard enough that you’d surely want a computer to do the
      boring parts for you – but it’s systematic enough that it can
      handle different variants of the problem by exactly the same
      method, without needing a different clever construction in each
      case. And unlike the trigonometry approach, it
is
able
      to calculate the answer in an exact manner.
Set the problem in the complex plane
I’ll start by describing a method for solving the problem by
      using complex numbers to represent the locations of all the
      points.
In this section, I won’t worry about whether calculations are
      approximate or exact. You
can
follow this procedure in
      an approximate way, using any programming language that has
      complex numbers as a built-in type; I’ll show an example in
      Python at the end of the section. Then, in the next section,
      I’ll show a technique that lets you follow the same procedure in
      a way that gives an exact answer.
How to make a triangle with three known angles
We’re going to need to construct several triangles with
      particular angles, so our first job is to find a way of doing
      that easily with complex numbers.
The simplest way I know of is to make use of the geometric
      result that the angle at the centre is twice the angle on a
      chord. That is, given any two points
A
,
B
on the
      circumference of a circle, the angle
AOB
(where
O
is the centre of the circle) is twice
ACB
, where
C
is
any
third point on the circle’s
      circumference
.
Angles on a chord and at the centre
So, suppose we want to make a triangle with
      angles
α
,
β
,
γ
. Imagine drawing the
      circumcircle of that triangle, so that all three of the vertices
      are points on the circumference. Then each of the angles of the
      triangle
is
an angle on a chord, and therefore, the
      corresponding angle at the centre is twice that.
Angles at the centre of a triangle’s circumcircle
But this means we’ve reduced the problem to finding three
      points at the same distance from the centre of a circle, with
      angles 2
α
, 2
β
, 2
γ
at the centre between
      them. The simplest way to do that in the complex numbers is just
      to take numbers of unit magnitude, so that they’re all on the
      unit circle. It’s easiest to make one of them 1,
      say
A
= 1, and then choose the other two to be the right
      distances away from it round the circle, in opposite directions,
      so you’d have
B
=
e
2
γi
and
C
=
e
−2
βi
, for example (with the
      angles
β
,
γ
written in radians).
Make three of them and put them side by side
Now we know how to make triangles, let’s put some of them
      together to construct the points we need for the actual problem.
We don’t really need the point
C
, at the very apex of
      the whole triangle. All we really need is the lower
      quadrilateral
ABED
, which is divided into four triangles
      by lines to the extra point
X
in the middle. Three of
      those triangles have all known angles, so we can start by making
      those, and fitting them together. Then we’ll have all the points
      of the top triangle, whose angles we’re trying to measure.
The figure we want to construct
We begin by making the bottom triangle
ABX
. Let’s
      choose
X
to be the complex number 1. Using the idea from
      the previous section, the angle
XBA
is 50°, so we want
      the angle
XOA
at the origin to be twice that. That is, we
      want
A
to be a point on the unit circle, 100°
      anticlockwise from 1.
Here I’m going to introduce a shorthand for a complex number
      we’re going to use a lot. All the angles in this problem are
      multiples of 10°, so instead of talking about
e
to the
      power of fiddly imaginary numbers in radians, I’m going to
      define
t
to be the complex number that represents a 10°
      rotation anticlockwise. 10° is one 36th of a turn,
      so
t
=
e
2
πi
/36
.
Then any angle that’s an integer multiple of 10° corresponds to
      the corresponding integer power of
t
. For example, we
      want
A
to be 100° around the circle from the starting
      point
X
, so we just
      set
A
=
t
10
.
Similarly,
B
wants to be 120° round the circle in
      the
opposite
direction from
A
, because if the
      angle
XOB
= 120°, then that will make the
      angle
XAB
half that, which is 60°, which is the angle we
      want at
A
. So we also have
B
=
t
−12
.
(This arrangement of points won’t put the triangle
XAB
with the
AB
edge horizontal, as it is in the diagram
      above. But we don’t care. If the whole diagram is rotated by
      some arbitrary angle, the angles
within
the figure
      don’t change, so there’s no point going to the extra effort to
      put it any particular way up.)
OK, that’s one triangle. Now we need to make a second one –
      let’s do the triangle
XDA
next – and then put it in the
      right place relative to the first one.
Making the triangle is easy enough if we don’t mind it being in
      the wrong place and the wrong size. We just do the same trick
      again: let’s invent
      points
x
= 1,
d
=
t
4
,
a
=
t
−10
.
      (Then the angles
xOd
and
xOa
are 40° and 100°
      respectively, which makes the angles
xad
and
xda
half those, 20° and 50°.)
Now we need to scale and rotate the second triangle
xad
to fit it alongside the first one. In other words, we need to
      find a new point
D
, which goes with our original
X
and
A
to form a triangle
XAD
similar to
      the
xad
we just constructed.
We do this by ensuring that the
ratio
(
d
−
x
) / (
a
−
x
) is equal to the ratio (
D
−
X
) / (
A
−
X
). (A
      ratio of two complex numbers tells you how much you need to scale
      and rotate one to turn it into the other, which means it’s
      exactly what you need to know to check that two triangles are
      similar.)
So if we know all of
X
,
A
,
x
,
a
,
      and
d
, and we also want
      (
d
−
x
) / (
a
−
x
) = (
D
−
X
) / (
A
−
X
), then we can just solve
      that equation for
D
, to get
D
=
X
+ (
d
−
x
) (
A
−
X
) / (
a
−
x
)
Substituting in the values
x
= 1,
d
=
t
4
,
a
=
t
−10
, this gives us
D
=
X
+ (
t
4
− 1) (
A
−
X
) / (
t
−10
− 1)
Similarly, we can construct the point
E
by doing the
      same thing again: make a triangle inscribed in the unit circle
      with angles 30°, 40° and 110°, and place it so that two of its
      vertices coincide with
X
and
B
. Omitting the
      boring bits, this gives us
E
=
X
+ (
t
−6
− 1) (
B
−
X
) / (
t
8
− 1)
Divide two numbers to get the angle you want
Now we have all the points
D
,
E
,
X
involved in the topmost triangle of the diagram. So we can
      construct a complex number representing the ratio between two
      sides of that triangle:
z
= (
X
−
E
) / (
D
−
E
)
The modulus of
z
is uninteresting to us: it tells us the
      ratio between the lengths
EX
and
ED
, and nobody’s
      asking us to find those lengths or their ratio. But
      the
argument
of
z
is exactly the angle we want!
Divide by the complex conjugate to normalise to unit length
At this point, if we were happy to get an approximate solution,
      we could just stop there, and measure the argument of
z
.
      But I’m working towards an
exact
solution in the next
      section, and so I want to do one more thing: I want to modify
      the number
z
so that it has unit length. When we get to
      the end of the exact solution, you’ll see why that was
      useful!
We can do this by making the complex conjugate of
z
,
      which I’ll write
z
*
. This has the same modulus
      as
z
, but rotates the opposite way around the origin. So
      if we
divide
them, to make the
      quotient
q
=
z
/
z
*
,
      then
q
is guaranteed to have modulus 1.
This operation also doubled the argument, because
z
and
      1 /
z
*
both
have the same argument
      (namely the angle we want). So
q
is a complex number with
      unit modulus, and whose argument is exactly
twice
the
      angle we’re after.
Putting it all together
Let’s recap. Here are all the variables we defined, in order,
      with the later definitions depending on earlier ones:
t
=
e
2
πi
/36
X
= 1
A
=
t
10
B
=
t
−12
D
=
X
+ (
t
4
− 1) (
A
−
X
) / (
t
−10
− 1)
E
=
X
+ (
t
−6
− 1) (
B
−
X
) / (
t
8
− 1)
z
= (
X
−
E
) / (
D
−
E
)
q
=
z
/
z
*
If we could calculate all those complex
      numbers
exactly
, then we’d find that
q
was a
      unit-modulus number whose argument was twice the angle we want.
Just to demonstrate it works, here’s a transcription of that
      calculation directly into Python, without worrying about the
      rounding errors. So you can at least find out what the
      answer
is
:
import
cmath
import
math
t
=
cmath
.
exp
(
math
.
pi
*
2
j
/
36
)
X
=
1
A
=
t
**
10
B
=
t
**-
12
D
=
X
+
(
t
**
4
-
1
)
*
(
A
-
X
)
/
(
t
**-
10
-
1
)
E
=
X
+
(
t
**-
6
-
1
)
*
(
B
-
X
)
/
(
t
**
8
-
1
)
z
=
(
X
-
E
)
/
(
D
-
E
)
q
=
z
/
z
.
conjugate
()
arg
=
cmath
.
phase
(
q
)
*
180
/
math
.
pi
print
(
f
"Argument of q =
{
arg
}
°"
)
print
(
f
"So θ =
{
arg
/
2
}
°"
)
If you run this in Python, it prints:
Argument of q = 59.99999999999992°
So θ = 29.99999999999996°
See what I mean about the solution being approximate? It looks
      very much as if this ought to be exactly 30° but has suffered
      some rounding errors. So surely the final answer to the problem
      is that
θ
= 30° exactly. But if we want to impress a
      mathematician, we have to do better than “well, it looks right
      to about 13 decimal places”.
Now do it all by algebra
Now we need to find a way to do the same calculation, but
      without any approximation. We can’t use floating-point numbers:
      we’ll have to use integers, and rational numbers, which can be
      represented exactly.
This is a problem, because the coordinates of all the points in
      this problem
aren’t
rational numbers. But looking back
      at the calculation, they’re all derived from just
one
complex number with irrational components, which we used as our
      starting point: the
      number
t
=
e
2
πi
/36
. Everything
      we did after that looked like pretty simple arithmetic, without
      any irrational constants.
So the trick is going to be: carry through the calculation in
      such a way that we express all our intermediate results as
      algebraic expressions in terms of
t
. Then we can arrange
      that everything
else
in those expressions is a
      rational, and we can keep things exact.
In fact, we’re going to arrange that every intermediate result
      is a
polynomial
in
t
, and moreover, limit the
      degree of those polynomials.
Find the minimal polynomial of
t
The number
t
represents a 10° rotation about the origin.
      If you raise it to the power
n
, it represents a
      10
n
° rotation about the origin. So, in particular, if
      you raise it to the power 36, it represents a 360° rotation,
      which is the same as no rotation at all. That
      is:
t
36
= 1.
I said we were going to limit the degree of our polynomials.
      This is how: now that we know
t
36
= 1, it
      follows that if we have a
really big
polynomial,
      involving very large powers of
t
, we can reduce the
      larger powers to smaller ones, by
      replacing
t
36
with 1 wherever it appears, and
      more generally, replacing
t
36 +
n
with
t
n
. This allows us to ensure that
      when our calculations start generating polynomials in
t
,
      we can keep their degree less than 36.
But in fact we can do better than that. Another way to say
      that
t
36
= 1 is to say that
t
is a root
      of the polynomial
t
36
− 1. But that polynomial
      factorises:
t
36
− 1 = (
t
− 1) (
t
+ 1) (
t
2
+ 1) (
t
2
−
t
+ 1) (
t
2
+
t
+ 1) (
t
4
−
t
2
+ 1) (
t
6
−
t
3
+ 1) (
t
6
+
t
3
+ 1) (
t
12
−
t
6
+ 1)
Any given root of the left-hand side
t
36
− 1
      must be a root of
one
of the factors on the right-hand
      side. But nothing will be a root of
more than one
of
      those factors, or else they’d split further. So we can find out
      which factor the
t
we want is a root of, and then just
      use that one.
It turns out that our original
t
is a root of the final,
      largest
      factor:
t
12
−
t
6
+ 1. In
      other words,
t
has the property
      that
t
12
=
t
6
− 1.
So we can keep all our polynomials’ degrees less than 12,
      instead of the 36 I suggested earlier. Whenever we generate a
      new polynomial, we can reduce it by
      replacing
t
12
with
t
6
− 1
      wherever it appears, or more generally,
      replacing
t
12 +
n
with
t
6 +
n
−
t
n
,
      and keep doing that until there aren’t any terms bigger
      than
t
11
any more.
This is called the
minimal polynomial
of the
      number
t
: it’s the smallest-degree polynomial with
      rational coefficients that
t
is a root of. Any other
      polynomial which has
t
as a root must therefore be a
      multiple of it. (So if there were a smaller one,
      then
t
12
−
t
6
+ 1 would have
      to be a multiple of
that
, and it isn’t, because we
      already factorised it as far as it would go in rationals.)
This minimality means that we can reliably test our numbers for
      equality. If we have two polynomials in
t
, and the
      complex numbers they represent are
exactly equal
, then
      their difference is a polynomial in
t
which evaluates to
      zero, i.e. which has
t
as a root. Therefore it must be a
      multiple of
t
12
−
t
6
+ 1.
      But if we reduced both polynomials to degree less than 12, then
      their difference can’t be a multiple
      of
t
12
−
t
6
+ 1 unless it’s
      zero.
So, as long as we keep our polynomials fully reduced, we can
      easily tell when two polynomials represent the same complex
      number, because it only happens if they’re exactly the same
      polynomial. This is how we’re going to end up being sure that
      our answer is exactly right.
Addition and multiplication
All right, so we’re representing our numbers as polynomials
      in
t
, reduced
      mod
t
12
−
t
6
+ 1. Now we
      have to work out how to do arithmetic on numbers in that
      form.
Addition is easy. If you have two polynomials in
t
, then
      you add them by just adding together corresponding coefficients.
      No higher-order terms are ever generated, so if the two input
      polynomials had degree < 12, so does the sum. For example:
(
t
11
+ 3
t
9
+
t
) + (
t
9
−
t
+ 42) = (
t
11
+ 4
t
9
+ 42)
Multiplying two polynomials
can
generate terms of
      higher degree. But we already know what to do about that: reduce
      the product polynomial until it has degree < 12, by
      repeatedly reducing a large term
      using
t
12 +
n
=
t
6 +
n
−
t
n
. For example:
(2
t
7
+ 3
t
) × (4
t
8
+ 1) = 8
t
15
+ 12
t
8
+ 2
t
7
+ 3
t
= (8
t
9
− 8
t
3
) + 12
t
8
+ 2
t
7
+ 3
t
in which the multiplication generated a single oversized term,
      namely 8
t
15
, and then we reduced it by
      replacing that term with 8
t
9
−
      8
t
3
. So the final answer has no term larger
      than
t
11
.
Division
But addition and multiplication aren’t enough by themselves.
      The calculations shown in the
previous
      section
also involve division. And if you divide two
      polynomials, it’s not obvious that you can make the result back
      into a polynomial at all.
The first division that comes up in that calculation is an easy
      one: we set
B
=
t
−12
,
      i.e.
B
= 1 /
t
12
. But that one can be
      eliminated almost trivially: we know
t
36
= 1,
      so
t
−12
=
t
36−12
=
t
24
.
      And now that
is
a polynomial again (although its degree
      is too high, so we’ll have to reduce it).
But the next division, where we make
D
by dividing
      something by (
t
−10
− 1), isn’t nearly as easy
      to handle. We can turn the
t
−10
into
t
26
easily enough, but even so, how do we
      make something like 1 / (
t
26
− 1) back into a
      polynomial?
Suppose that we have some value
x
, expressed as a
      polynomial in
t
, and we want to find 1 /
x
.
That value
x
will have a
minimal polynomial
,
      just like
t
does. Let’s call
      it
P
x
. By definition, this is the
      lowest-degree polynomial (with rational coefficients) that
      has
x
as a root. (There must be one, because anything you
      can write as a polynomial in
t
is an algebraic number,
      and therefore a root of
some
polynomial – and then it’s
      just a matter of finding the smallest one.)
In general,
x
isn’t the only root
      of
P
x
. If
P
x
has degree greater than 1, then it will have other roots too,
      say
a
,
b
, …,
n
. If we could find
all
the roots of
P
x
(including
x
itself), then we could write the
      polynomial
P
x
as a product of linear
      terms, each one having one of the roots
      of
P
x
(negated) as its constant term.
      And if you imagine multiplying out that product, then the
      constant term of the whole thing is therefore the product of all
      the roots (up to maybe a sign flip). But it’s also equal to the
      constant term of
P
x
itself, i.e. a
      rational number.
But in that case, let
w
be the product of all the roots
      of
P
x
apart
from
x
itself. Then
wx
is a rational. But
      then
w
/
wx
is a polynomial divided by a rational,
      i.e. still a polynomial – and it’s clearly also equal to
      1 /
x
. So this
is
a way to write 1 /
x
as
      a polynomial.
That’s all very well, but
how
do you find the other
      roots of
P
x
? You
could
do it
      by directly calculating
P
x
and then
      trying to find its roots, but that’s a huge amount of effort.
      There’s a shortcut.
All you need is to know the other 11 roots
      of
P
t
=
t
12
−
t
6
+ 1,
      the minimal polynomial of
t
. Suppose that
u
is a
      root of
P
t
, but isn’t
t
itself.
      Then any equation between polynomials in
t
(saying that
      two of them work out to the same thing
      mod
P
t
) must also be true if you
      replace every occurrence of
t
with
u
, because the
      only
property
of
t
that the equation depends on
      is that it’s a root of
P
t
, and
      since
u
also has that property, the statement must still
      be true.
So you can make all the roots
of
P
x
by taking the
      polynomial
x
, and
evaluating
it at each
      root
u
of
P
t
in turn.
That is: we’ve been thinking of
x
as a
complex
      number
which just happens to be written as a polynomial
      in
t
. But we now switch to regarding it as
      a
function
given by the same polynomial, which can be
      given
any
complex number as input, and returns a
      weighted sum of powers of its input number. So evaluating the
      polynomial
x
at
t
gives us the value we had to
      start with – but we can also evaluate the same polynomial at
      some other number, such as
u
.
OK, but in order to evaluate
x
at all the other roots
      of
P
t
, we need to
know
the
      other roots of
P
t
. What are they?
Well,
P
t
was a factor
      of
t
36
− 1. So the roots
      of
P
t
must all be roots
      of
t
36
− 1, which means they’re complex
      numbers whose 36th power is 1 – and all such numbers are powers
      of
t
. And the powers we’re looking for are the ones which
      have no common factor with 36: the roots
      of
P
t
are
t
,
t
5
,
t
7
,
t
11
,
t
13
,
t
17
,
t
19
,
t
23
,
t
25
,
t
29
,
t
31
,
t
35
because when we factorised
t
36
− 1,
      the
other
factors are the ones that represent numbers
      which become 1 when raised to a
smaller
power than 36.
      The polynomial
t
12
−
t
6
+ 1
      is the one whose roots are the numbers whose 36th power is
      1
and no smaller power is
.
That was a lot of faff, so let’s bring it back down to earth.
      If you have a value
x
represented as a polynomial
      in
t
, then you can find the reciprocal 1 /
x
as a
      polynomial in
t
as follows:
Evaluate
x
at each of those powers of
t
(other than
t
itself) to make
x
(
t
5
),
x
(
t
7
), ...,
x
(
t
35
), each as a polynomial in
t
.
Multiply those 11 polynomials together to make a product
w
.
Then the product
wx
, reduced mod
t
12
−
t
6
+ 1, will work out to a rational number.
So
w
divided by the rational
wx
is a polynomial in
t
, and is also equal to 1 /
x
.
I’ve just about got room to show an example. Suppose
x
=
t
3
+
2t
+ 1. Then
x
(
t
5
) =
t
15
+
2t
5
+ 1 (you replace each power of
t
in the original expression with the corresponding power of
t
5
). Similarly,
x
(
t
7
) =
t
21
+
2t
7
+ 1, and so on until
x
(
t
35
) =
t
105
+
2t
35
+ 1.
Multiplying out the product
w
of all of those 11 polynomials
      gives a
huge
polynomial, with coefficients going up
      to
t
645
. But you’d reduce it
      mod
t
12
−
t
6
+ 1 as you went
      along, to keep the intermediate values small.
The product
w
, fully reduced, works out to
−5692
t
11
+ 2500
t
10
− 1129
t
9
+ 692
t
8
− 242
t
7
− 255
t
6
+ 5484
t
5
− 1748
t
4
+ 1800
t
3
− 1988
t
2
− 1852
t
+ 2176
Even reduced, that still looks like a horrible mess. But if you
      multiply that by the
      original
x
=
t
3
+
2t
+ 1 and
      reduce again, then just like magic
, the result comes out to just
14689
And therefore,
w
/ 14689 is a degree-11 polynomial
      in
t
, with rational coefficients, which is equal to
      1 /
x
. It can be done
!
Complex conjugate of a polynomial
One last awkwardness: in solving this problem, we also wanted
      to take a complex conjugate, to calculate
q
=
z
/
z
*
. How will we do
that
when
z
is one of these polynomials?
That’s not too hard. The complex conjugate of a single power
    of
t
is just the same power negated, because powers
    of
t
all have modulus 1:
    (
t
n
)
*
=
t
−
n
.
    So if you have some number
x
represented as a polynomial
    in
t
, you can take its conjugate by evaluating it
    at
t
−1
. For example,
    take
x
=
t
3
+
2t
+ 1 (the same
      example we just used for division). Then
x
*
=
x
(
t
−1
) =
t
−3
+
2t
−1
+ 1 =
t
33
+
2t
35
+ 1
because, again,
t
−
n
is the same thing as
t
36 −
n
. Now we just reduce that mod
t
12
−
t
6
+ 1 as usual, and that’s the complex conjugate of
x
.
Now do the actual calculation
Now we know how to do every arithmetic operation involved in
      our calculation, on numbers expressed as polynomials
      in
t
. It’s time to actually
do
the
      calculation!
As I said at the start, the amount of sheer polynomial-juggling
      in this procedure is large enough that you do want a computer to
      do the work for you. There are plenty of computer algebra
      systems that already have built-in libraries to work in
      polynomial quotient fields of this kind: I could show a piece of
      code in SageMath, for example, that isn’t much longer than the
      earlier approximate version in Python. Or an interactive session
      in Maxima. Or probably half a dozen other systems of that
      kind.
But just to show that you don’t
need
a million lines
      of Serious Computer Algebra to do a job like this, here’s an
      implementation in Python (
download the
      source
) that does all the polynomial arithmetic all by
      itself and still just about fits on a (large) monitor. The
      actual calculation is shown at the bottom, very like the
      previous representation except that all the starting values are
      instances of the
Value
class, instead of Python’s
      native complex number type:
import
fractions
class
Value
:
"Class representing a polynomial in t, mod t^12 - t^6 + 1"
def
__init__
(
self
,
coeffs
):
# coeffs is an array with coeffs[i] giving the coefficient of t^i.
# The input to this constructor can be any length; we'll reduce it.
while
len
(
coeffs
)
>
12
:
# Remove the highest-order coefficient
coeff
=
coeffs
.
pop
()
n
=
len
(
coeffs
)
# Popping that coefficient subtracted coeff * t^n.
# Add coeff * (t^(n-6) - t^(n-12)) to compensate.
coeffs
[
n
-
6
]
+=
coeff
coeffs
[
n
-
12
]
-=
coeff
# Pad with zeroes so that len(self.coeffs) is always exactly 12
self
.
coeffs
=
coeffs
+
[
0
]
*
(
12
-
len
(
coeffs
))
def
__add__
(
self
,
other
):
# Add corresponding coefficients
return
Value
([
u
+
v
for
u
,
v
in
zip
(
self
.
coeffs
,
other
.
coeffs
)])
def
scale
(
self
,
scalar
):
# Multiply every coefficient by the scale
return
Value
([
scalar
*
u
for
u
in
self
.
coeffs
])
def
__sub__
(
self
,
other
):
# Negate the RHS, then add
return
self
+
other
.
scale
(
-
1
)
def
mul_by_t
(
self
):
# Multiply by t by shifting all the coefficients upward by one
return
Value
([
0
]
+
self
.
coeffs
)
def
__mul__
(
self
,
other
):
total
=
Value
([])
# zero
other_times_power_of_t
=
other
# other * t^0
for
coeff
in
self
.
coeffs
:
# Add coeff * other * t^i to the total
total
+=
other_times_power_of_t
.
scale
(
coeff
)
# Multiply by t to make the next (other * t^i)
other_times_power_of_t
=
other_times_power_of_t
.
mul_by_t
()
return
total
def
evaluate_at
(
self
,
x
):
total
=
Value
([])
# zero
power_of_x
=
Value
([
1
])
# x^0
for
coeff
in
self
.
coeffs
:
# Add coeff * x^i to the total
total
+=
power_of_x
.
scale
(
coeff
)
# Multiply by x to make the next x^i
power_of_x
*=
x
return
total
@staticmethod
def
power_of_t
(
n
):
# t^36 = 1, so reduce mod 36, which also makes negative n positive
n
%=
36
# Make the literal polynomial t^n and let the constructor reduce it
return
Value
([
0
]
*
n
+
[
1
])
def
complex_conjugate
(
self
):
# Evaluate at t^-1
return
self
.
evaluate_at
(
self
.
power_of_t
(
-
1
))
def
reciprocal
(
self
):
# Evaluate at t^5, t^7, t^11, ..., t^35 and multiply them all together
w
=
Value
([
1
])
for
index
in
[
5
,
7
,
11
,
13
,
17
,
19
,
23
,
25
,
29
,
31
,
35
]:
w
*=
self
.
evaluate_at
(
self
.
power_of_t
(
index
))
# Check that w * x is a constant (all coeffs after the 0th are zero)
wx
=
self
*
w
assert
all
(
coeff
==
0
for
coeff
in
wx
.
coeffs
[
1
:])
# And divide by that constant, using fractions.Fraction for exactness
return
w
.
scale
(
fractions
.
Fraction
(
1
,
wx
.
coeffs
[
0
]))
def
__truediv__
(
self
,
other
):
return
self
*
other
.
reciprocal
()
def
__str__
(
self
):
# Format as a mathematical expression in Python syntax
return
" + "
.
join
(
f
"
{
u
}
"
if
i
==
0
else
f
"
{
u
}
*t"
if
i
==
1
else
f
"
{
u
}
*t**
{
i
}
"
for
i
,
u
in
enumerate
(
self
.
coeffs
)
if
u
!=
0
)
one
=
Value
([
1
])
X
=
one
A
=
Value
.
power_of_t
(
10
)
B
=
Value
.
power_of_t
(
-
12
)
D
=
X
+
(
Value
.
power_of_t
(
4
)
-
one
)
*
(
A
-
X
)
/
(
Value
.
power_of_t
(
-
10
)
-
one
)
E
=
X
+
(
Value
.
power_of_t
(
-
6
)
-
one
)
*
(
B
-
X
)
/
(
Value
.
power_of_t
(
8
)
-
one
)
z
=
(
X
-
E
)
/
(
D
-
E
)
q
=
z
/
z
.
complex_conjugate
()
print
(
"X ="
,
X
)
print
(
"A ="
,
A
)
print
(
"B ="
,
B
)
print
(
"D ="
,
D
)
print
(
"E ="
,
E
)
print
(
"z ="
,
z
)
print
(
"q ="
,
q
)
When this is run, it prints:
X = 1
A = 1*t**10
B = -1*t**6
D = 1 + 1*t**2 + -1*t**8 + 1*t**10
E = 1 + 1*t**2 + 1*t**4 + -1*t**6 + -1*t**8
z = 1 + -1*t**2 + 1*t**6 + 1*t**8 + -1*t**10
q = 1*t**6
The first five lines of this output give the locations of the
      five points in our geometric diagram, as polynomials
      in
t
. To show that this really works and isn’t abstract
      nonsense, here’s a diagram showing
how
those points are
      derived from those polynomials:
The points in our calculation, represented as polynomials
This diagram happens to be nice and simple, because all the
      coefficients in those polynomials worked out to ±1, for some
      reason. You can confirm for yourself that each arrow looks as if
      it’s at about the right angle (e.g. the arrow marked 1 points
      directly to the right, the
t
2
arrow is 20°
      anticlockwise from that, and if the −
t
6
arrow
      were reversed then it would be 60° anticlockwise from 1). And if
      you start from the black circle at the origin, you can follow a
      path of grey arrows to get to each of the
      points
X
,
A
,
B
,
D
,
E
, and if
      you add up the powers of
t
written on each arrow, you get
      the same polynomials shown above.
I showed those values purely for interest. But the key point is
      the final value:
q
=
t
6
.
That’s saying that
q
is
exactly
the complex
      number that represents a 60° rotation about the origin. And
      remember that in the previous section I said that
q
was
twice
the angle we were actually after.
So the final answer is that the angle
θ
, in the original
      diagram at the start of this article, is
exactly
30°.
      No surprises there: that’s the same value it
looked
as
      if it was going to be, after we ran the approximate version
      earlier. But this time we’re sure of it: the calculations have
      no approximation error, because we didn’t do anything
      approximate at all.
Afterthoughts
What if the answer isn’t nice?
I hope it’s now clear why I wanted to do that final step of
      calculating
q
=
z
/
z
*
. The
previous
value in the program’s output was
z
= 1 −
t
2
+
t
6
+
t
8
−
t
10
This represents a complex number whose argument is the desired
      angle 30°. But you wouldn’t know it just by looking at that
      polynomial! That nice simple argument is combined with
      a
magnitude
of something complicated which has to be
      represented as a sum of lots of powers of
t
pointing in
      other random directions, and therefore, you can’t
see
by eye what its argument is. But
q
, because it’s been
      reduced back to unit magnitude, is very simple by comparison,
      and it’s easy to check by eye that the answer is what you expect
      it to be.
But one caveat: this entire procedure only works out neatly,
      with
q
coming out as a really simple
      monomial,
because
the angle in question is a nice round
      number – a multiple of the same 10° unit that all the input
      angles are.
Langley’s problem is called “adventitious” because of the nice
      coincidence that using
those
particular input angles
      makes the output angle
θ
a nice exact value. With most
      other choices of the angles, that wouldn’t have worked, and the
      way you’d find out it hadn’t worked would be that the output
      value of
q
would look like some disgusting complicated
      polynomial, with many nonzero terms instead of a single one,
      probably with fractional coefficients as well. If you
      saw
that
output (and hadn’t made a mistake setting up
      the problem), then it would tell you the output wasn’t a nice
      round number, and the only thing to do was to calculate it
      numerically using trigonometry after all.
For example, here’s a variant version of the problem in which
      the angles don’t work out nicely:
A version that would make Langley wince
In this version, I’ve made the overall triangle
ABC
into
      a 70°–70°–40° triangle instead of its original 80°–80°–20°, and
      left the base triangle
ABX
the same.
If you run my polynomial-based calculation for
this
triangle, the answer you get as the final value
q
looks
      much nastier, and so do a lot of the intermediate values:
X = 1
A = 1*t**10
B = -1*t**6
D = 2/3 + 2/3*t**2 + 1/3*t**4 + -1/3*t**6 + -1/3*t**8 + 1/3*t**10
E = 3*t**2 + -2*t**4 + 2*t**6 + -3*t**8 + 1*t**10
z = 45/73 + -132/73*t**2 + 66/73*t**4 + 141/73*t**6 + 39/73*t**8 + -129/73*t**10
q = 6/73 + -3/73*t**2 + 38/73*t**4 + 48/73*t**6 + -24/73*t**8 + 12/73*t**10
But the answer isn’t
wrong!
It’s not presented in a
      helpful form, but it’s still
right
. If we did want to
      calculate the angle
θ
in this version of the problem,
      then one way would be to go back to the Python
      code
shown above
which did the whole job
      using floating point. But we can take a short cut by using the
      value of
q
that the polynomial code has computed, and
      just converting that back into a complex number using Python. If
      you do that, you find that it really does have unit magnitude
      (up to Python’s rounding errors), and that its argument is twice
      the angle
θ
in my modified diagram:
import
cmath
import
math
t
=
cmath
.
exp
(
math
.
pi
*
2
j
/
36
)
q
=
6
/
73
+
-
3
/
73
*
t
**
2
+
38
/
73
*
t
**
4
+
48
/
73
*
t
**
6
+
-
24
/
73
*
t
**
8
+
12
/
73
*
t
**
10
print
(
f
"Modulus of q =
{
abs
(
q
)
}
"
)
arg
=
cmath
.
phase
(
q
)
*
180
/
math
.
pi
print
(
f
"Argument of q =
{
arg
}
°"
)
print
(
f
"So θ =
{
arg
/
2
}
°"
)
Modulus of q = 0.9999999999999998
Argument of q = 46.727454823246°
So θ = 23.363727411623°
So this time we
had
to do some trigonometry at the end
      to get the angle – because it’s a horrible irrational, and we
      weren’t going to get it out of any amount of nice clean
      rational-number work. But the method was still
accurate
– the polynomial representation of that
q
is exactly
      correct, without any rounding error. The rounding errors only
      appear in the very last stage when you convert back into a real
      angle.
I did twice as much work as I really needed to
Looking at the intermediate values from the final calculation,
      you might notice that they all consist entirely of
even
powers of
t
. Nothing is ever an odd power. Not even in
      the disgusting modified version where the angle doesn’t work out
      neatly.
With hindsight, I should have been able to predict that,
      because all the angles we ever encounter are doubled! We
      construct a triangle with angles
α
,
β
,
γ
by
      doubling those angles and then making angles at the origin of
      2
α
, 2
β
, 2
γ
. And the final trick of
      multiplying
z
by its complex conjugate has the effect of
      doubling the output angle we’re trying to find. So nothing in
      the input or output of the calculation ever has to work with an
      angle
not
doubled.
Therefore, since all the angles in the problem are multiples of
      10°, all the angles the calculation ever has to work with are
      multiples of 20°. So I could have saved myself some time by
      starting from a different complex
      number,
T
=
t
2
representing a 20°
      instead of 10° rotation. The minimal polynomial of
that
is
t
6
−
t
3
+ 1 (also one of
      the factors of
t
36
− 1). So that would have
      let me limit all the polynomials in the calculation to degree
      less than 6, instead of less than 12.
But I didn’t think of that until I saw all the intermediate
      values at the end of the procedure, noticed all the exponents
      were even, and felt silly!
Have I cheated?
I mentioned in the introduction that there’s often a “no
      trigonometry” rule when this problem is set. Have I broken it?
Certainly I’ve obeyed the
letter
of the rule: I
      haven’t calculated a sine, cosine or tangent anywhere in this
      entire derivation
. But whether you think I’ve kept to
      the
spirit
of the rule is another matter, and in my
      opinion, the answer depends on what exactly you think the spirit
      of the rule
is
.
Why
did someone forbid trigonometric solutions to this
      problem? I can see two reasonable possibilities.
One answer is that the trigonometry approach is only
      approximate: you get an answer to some number of significant
      figures, but you can’t easily prove that it’s
exactly
the number of degrees it looks like. So you might have forbidden
      trigonometry because you wanted the answer calculated exactly,
      not just approximated. In that case, I haven’t violated the
      spirit of the rule: this method
does
calculate the
      exact answer.
But the other answer is that the aim of forbidding trigonometry
      was to force the puzzle solver to find the
clever
solution involving extra construction lines. If that’s what you
      think the point was, then I
have
violated the spirit of
      the rule: the method I’ve shown here is brute-force plodding,
      designed to avoid needing an insight of any kind. (Or, at least,
      an insight specific to the individual numbers; the trick for
      dividing by a polynomial in
t
certainly is clever, but
      it’s well known, and you only have to learn it once, and then
      it’s reusable in any situation of this kind.)
But here’s a third thought. One purpose of setting a student a
      problem in the first place is that they should learn something
      worthwhile from it. And what you learn from this algebraic
      method is indeed worthwhile. The whole technique can be reused
      unchanged in other computational contexts
      (
here’s an
      example!
), and also all of the ideas here are important to
      ‘real’ mathematics: this kind of algebraic extension of the
      field of rational numbers leads directly to Galois theory. If I
      had a student, and set them this problem, and they chose to
      learn about field extensions instead of constructing extra
      triangles in a diagram, I would think they’d made good use of
      their time!
With any luck, you should be able to read the footnotes of this
      article in place, by clicking on the superscript footnote number
      or the corresponding numbered tab on the right side of the page.
But just in case the CSS didn’t do the right thing, here’s the
      text of all the footnotes again:
1.
Perhaps you’re wondering
why
I might happen to be concerned with this problem and how to
      solve it without cleverness. Might it be because someone gave me
      the problem recently and I didn’t manage to find the clever
      answer? No comment.
2.
What if
C
is on
      the opposite side of the line from
O
? In that case, you
      have to switch to measuring the angle at
O
on the other
      side of the line, so that it’s 360° minus the angle shown
      here.
3.
I’ve
      glossed over a subtlety here: this procedure will always give 12
      values in total, including the original
x
,
      but
some
numbers represented as polynomials in
t
have a minimal polynomial of lower degree than 12. In that
      situation our 12 values will consist of multiple copies of each
      root of
P
x
, including multiple copies
      of
x
itself. But what we do with them next still works,
      because the product of all of them is still a rational – it’s
      just a
power
of
P
x
’s constant
      term, instead of the constant term itself.
4.
In
      fact, this is a generalised form of the same technique you use
      to divide by a complex number
a
+
bi
, by
      multiplying top and bottom by its complex
      conjugate
a
−
bi
so that the denominator turns
      into a real number. The principle is
      identical:
a
+
bi
is a polynomial in
i
; the
      minimal polynomial of
i
over ℝ
      is
x
2
+ 1, and the only other root of that
      polynomial is −
i
; so we evaluate
a
+
bi
at
      that other root to make
a
−
bi
, and then the
      product of that with the original number –
      reducing
i
2
wherever it appears – turns into a
      polynomial with only a constant term, which it’s easy to divide
      by. It all looks more complicated when you have 11 other roots
      rather than just one, but it’s exactly the same trick, just
      bigger!
5.
Another
      completely different approach to dividing by a
      polynomial
x
when working mod
P
t
is to use Euclid’s algorithm, the same as you would for modular
      arithmetic in integers. Find the greatest common divisor of the
      polynomials
x
and
P
t
; you expect
      this to be 1, because
P
t
is
      irreducible. As a by-product the algorithm will produce two more
      polynomials
λ
,
μ
such
      that
λx
+
μP
t
= 1. Another way
      of writing that is
λx
≡ 1
      mod
P
t
, so
λ
is precisely the
      inverse we wanted. I’ve chosen to do it this way instead for
      several reasons. First, because the idea of evaluating
x
at a different value will be reused in the next section; second,
      because Euclid’s algorithm requires dividing polynomials (in the
      more usual sense of delivering a quotient and a remainder),
      which is a more complicated primitive operation than evaluating
      them and multiplying them – especially since I’m going to show
      example code later. And thirdly, you can make this approach give
      you a
single
algebraic formula for calculating the
      reciprocal of any number mod
P
t
, which
      is more elegant than the way Euclid takes a variable number of
      steps depending on the inputs. But you
could
do it by
      Euclid if you preferred, and it would still
      work.
6.
All right, the
      Python code at the end of the first section
did
do
      trigonometry, in the form of complex exponentials and the
      Python
cmath.phase
function. So did the modified
      example where the angle didn’t work out nicely. But those aren’t
      part of the proper solution. The full solution to the original
      problem, delivering the answer of 30° exactly using nothing but
      polynomials, didn’t use either of those pieces of floating-point
      code.
