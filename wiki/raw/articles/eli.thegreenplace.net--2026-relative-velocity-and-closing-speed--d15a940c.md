---
title: "Relative velocity and closing speed"
url: "https://eli.thegreenplace.net/2026/relative-velocity-and-closing-speed/"
fetched_at: 2026-08-04T10:18:16.519223+00:00
source: "eli.thegreenplace.net"
tags: [blog, raw]
---

# Relative velocity and closing speed

Source: https://eli.thegreenplace.net/2026/relative-velocity-and-closing-speed/

August 03, 2026 at 20:01
Tags
Math
In Physics simulations or game engines it’s sometimes useful to
determine the speed with which two objects are approaching each other.
This post will discuss the concept of
closing speed
, which is the
normal component
of the
relative velocity
of two objects.
Relative velocity and its components
Suppose we have objects A and B  with velocity vectors
\vec{V_A}
and
\vec{V_B}
. The
relative velocity
of B
w.r.t. A is:
\[\vec{V}_{B|A}=\vec{V}_B-\vec{V}_A\]
Put differently, it’s the velocity of B in A’s frame of reference.
This relative velocity is a vector, and we can split it into orthogonal
components. Obviously, the nature of such a split depends on the basis
we want to use. We could look at the vector’s x an y components (we’ll
be using
- two dimensional space, but everything
here applies to 3D as well), but for this post we’re interested in
something slightly different:
We draw a line connecting the two objects. The component of
\vec{V}_{B|A}
in the direction of this line is called the
normal component
of relative velocity, while the component
perpendicular to this direction is called the
tangential component
.
Computing the normal component
How do we find the component of a vector in the direction of a specific
line? By using a
vector
projection!
.
We’ll represent the line by a vector, and find the projection of
\vec{V}_{B|A}
onto this vector.
The positions of A and B can also be seen as vectors:
\vec{P}_A
and
\vec{P}_B
. The line connecting them can then be expressed as
the vector
\vec{P}_B-\vec{P}_A
:
All we need from this position difference vector is its direction, not
its magnitude, however . So we’ll use the
unit vector
of
\vec{P}_B-\vec{P}_A
, denoted as:
\[\widehat{P}=\frac{\vec{P}_B-\vec{P}_A}{|\vec{P}_B-\vec{P}_A|}\]
Finally, to find the projection of
\vec{V}_{B|A}
onto
\widehat{P}
, we compute :
\[S_c=\vec{V}_{B|A}\cdot\widehat{P}=(\vec{V}_B-\vec{V}_A)\cdot\widehat{P}\]
Where the multiplication operator between the vectors is the
dot
product
. Note that the result of the dot product is a scalar;
therefore, the quantity
S_c
is called the
closing speed
- it
expresses the rate at which the relative distance of the two objects is
changing. If it’s positive, the objects are drifting farther apart; if
it’s negative, the objects are getting closer together. Therefore the
term "closing speed" may be slightly confusing; alternatively, this has
been called a "signed separation speed", or "normal relative speed" .
The signs in these calculations can be tricky to get right, so we have
to be very careful. Let’s see a few examples that will help us make
these computations more concrete.
Examples
To build up some intuition and get some practice with the equations,
we’ll review the following examples:
Example I
: We’ll start by computing the relative position unit
vector
\widehat{P}
:
\[\widehat{P}=\frac{\vec{P}_B-\vec{P}_A}{|\vec{P}_B-\vec{P}_A|}=\frac{\langle 4,0\rangle}{|\langle 4,0 \rangle|}=\langle1,0\rangle\]
Then, the closing speed is:
\[S_c=(\vec{V}_B-\vec{V}_A)\cdot\widehat{P}=\langle -3,0\rangle\cdot\langle1,0\rangle=-3\]
Based on our convention, the negative sign of
S_c
means that the
objects are approaching each other. Due to the simple nature of the
example, this result is easy to verify, as it can be immediately guessed
just by looking at the diagram.
Example II
: Here
\widehat{P}
is the same as in the previous
example. The closing speed is:
\[S_c=(\vec{V}_B-\vec{V}_A)\cdot\widehat{P}=\langle 3,0\rangle\cdot\langle1,0\rangle=3\]
Same magnitude, but different sign from before, because the objects are
moving farther apart.
Example III
This example is to demonstrate that we get consistent
results even if B is to the left of A. Here the relative position unit
vector is:
\[\widehat{P}=\frac{\vec{P}_B-\vec{P}_A}{|\vec{P}_B-\vec{P}_A|}=\frac{\langle -2,0\rangle}{|\langle -2,0 \rangle|}=\langle-1,0\rangle\]
And the closing speed:
\[S_c=(\vec{V}_B-\vec{V}_A)\cdot\widehat{P}=\langle 3,0\rangle\cdot\langle -1,0\rangle=-3\]
Which is the same as in example I, as expected. The direction of
\widehat{P}
flipped, but so did the direction of the relative
velocity vector, so the result has the same sign.
Example IV
: Finally, an example showing more arbitrary positions and
velocities.
\[\widehat{P}=\frac{\vec{P}_B-\vec{P}_A}{|\vec{P}_B-\vec{P}_A|}=\frac{\langle 3,4\rangle}{|\langle 3,4 \rangle|}=\langle0.6,0.8\rangle\]
Then:
\[S_c=(\vec{V}_B-\vec{V}_A)\cdot\widehat{P}=\langle -3,-6\rangle\cdot\langle 0.6,0.8\rangle=-6.6\]
This example is a good opportunity to demonstrate something important
about
S_c
: it’s time-dependent, because positions change with
time. Here, -6.6 is the closing speed at the exact moment when A’s and
B’s positions and velocities are as stated in the example. In the next
time step, the position of A will be
\langle2,5\rangle
and the
position of B will be
\langle2,3\rangle
, while their velocities
remain the same. The
S_c
then will be quite different. This is a
good segue to the next topic - which is a more physical view of closing
speed.
Closing speed as a function of time
The computation shown so far represents a static view of the world;
perhaps the right word to use is
instantaneous
. Given the positions
and velocities at a given moment, what is the closing speed between the
objects
at that exact moment
?
But there’s no reason to not generalize this using a more standard
physical interpretation of velocity.
First, let’s state the position vectors of A and B as a function of
time:
\vec{P}_A(t)
and
\vec{P}_B(t)
. The relative
position vector between the objects is also a function of time:
\[\vec{R}(t)=\vec{P}_B(t)-\vec{P}_A(t)\]
Now we’ll define the scalar distance as the magnitude of this vector:
\[r(t)=|\vec{R}(t)|=|\vec{P}_B(t)-\vec{P}_A(t)|\]
We’re interested in
\frac{dr(t)}{dt}
- the change in this
distance over time. Let’s start by breaking
R(t)
down to its
constituents:
\[\begin{aligned}
    \vec{R}(t)&=\langle x(t),y(t)\rangle \\
    r(t)&=\sqrt{x(t)^2+y(t)^2}
\end{aligned}\]
By the chain rule :
\[\begin{aligned}
    \frac{dr(t)}{dt}&=\frac{\frac{d}{dt}(x(t)^2+y(t)^2)}{2\sqrt{x(t)^2+y(t)^2}}\\
    &=\frac{2x(t)x'(t)+2y(t)y'(t)}{2\sqrt{x(t)^2+y(t)^2}}
    =\frac{x(t)x'(t)+y(t)y'(t)}{\sqrt{x(t)^2+y(t)^2}}
\end{aligned}\]
Switching back to the vector representation: since
\vec{R}(t)=\langle x(t),y(t)\rangle
, the numerator of the
fraction above is then a dot product between
\vec{R}(t)
and
\vec{R}'(t)
, we can write this as:
\[\frac{dr(t)}{dt}=\frac{\vec{R}(t)\cdot\vec{R}'(t)}{|\vec{R}(t)|}=\hat{R}(t)\cdot\vec{R}'(t)\]
But
\hat{R}(t)
is precisely
\hat{P}
from the earlier
section, as a function of time. Moreover:
\[\vec{R}'(t)=\vec{P}'_B(t)-\vec{P}'_A(t)=\vec{V}_B(t)-\vec{V}_A(t)\]
Because velocity is the time derivative of position. Therefore, we end
up with the same equation, just as a function of time:
\[\frac{dr(t)}{dt}=\hat{P}(t)\cdot(\vec{V}_B(t)-\vec{V}_A(t))\]
This formulation is more precise because it makes it very obvious that
all the quantities we’re dealing with are time dependent.
