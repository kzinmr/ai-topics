---
title: "Closed-form solution nonlinear pendulum w/ Jacobi functions"
url: "https://www.johndcook.com/blog/2026/04/25/exact-solution-nonlinear-pendulum/"
fetched_at: 2026-04-27T07:56:47.336385+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Closed-form solution nonlinear pendulum w/ Jacobi functions

Source: https://www.johndcook.com/blog/2026/04/25/exact-solution-nonlinear-pendulum/

The
previous post
looks at the nonlinear pendulum equation and what difference it makes to the solutions if you linearize the equation.
If the initial displacement is small enough, you can simply replace sin θ with θ. If the initial displacement is larger, you can improve the accuracy quite a bit by solving the linearized equation and then adjusting the period.
You can also find an exact solution, but not in terms of elementary functions; you have to use Jacobi elliptic functions. These are functions somewhat analogous to trig functions, though it’s not helpful to try to pin down the analogies. For example, the Jacobi function sn is like the sine function in some ways but very different in others, depending on the range of arguments.
We start with the differential equation
θ″(
t
) +
c
² sin( θ(
t
) ) = 0
where
c
² =
g
/
L
, i.e. the gravitational constant divided by pendulum length, and initial conditions θ(0) = θ
0
and θ′(0) = 0. We assume −π < θ
0
< π.
Then the solution is
θ(
t
) = 2 arcsin(
a
cd(
c
t
|
m
) )
where
a
= sin(θ
0
/2),
m
=
a
², and cd is one of the 12 Jacobi elliptic functions. Note that cd, like all the Jacobi functions, has an argument and a parameter. In the equation above the argument is
ct
and the parameter is
m
.
The last plot in the previous post was misleading, showing roughly equal parts genuine difference and error from solving the differential equation numerically. Here’s the code that was used to solve the nonlinear equation.
from scipy.special import ellipj, ellipk
from numpy import sin, cos, pi, linspace, arcsin
from scipy.integrate import solve_ivp

def exact_period(θ):
    return 2*ellipk(sin(θ/2)**2)/pi

def nonlinear_ode(t, z):
    x, y = z
    return [y, -sin(x)]    

theta0 = pi/3
b = 2*pi*exact_period(theta0)
t = linspace(0, 2*b, 2000)

sol = solve_ivp(nonlinear_ode, [0, 2*b], [theta0, 0], t_eval=t)
The solution is contained in
sol.y[0]
.
Let’s compare the numerical solution to the exact solution.
def f(t, c, theta0):
    a = sin(theta0/2)
    m = a**2
    sn, cn, dn, ph = ellipj(c*t, m)
    return 2*arcsin(a*cn/dn)
There are a couple things to note about the code. First,SciPy doesn’t implement the cd function, but it can be computed as cn/dn. Second, the function
ellipj
returns four functions at once because it takes about as much time to calculate all four as it does to compute one of them.
Here is a plot of the error in solving the differential equation.
And here is the difference between the exact solution to the nonlinear pendulum equation and the stretched solution to the linear equation.
