---
title: "Runge-Kutta: over versus stages"
url: "https://www.johndcook.com/blog/2026/08/01/butcher-barrier/"
fetched_at: 2026-08-02T10:14:20.347900+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Runge-Kutta: over versus stages

Source: https://www.johndcook.com/blog/2026/08/01/butcher-barrier/

The textbook version of the Runge-Kutta method for solving differential equations has 4 stages and has 4th order error. For lower order versions of RK the number of stages
s
also matches the order of the error
p
. But in order to achieve error on the order of
p
≥ 5, you need more than
p
stages. This is known as the Butcher barrier.
Before going any further, let’s back up and say what we mean by stages and by order.
Stages
The number of stages in an RK method to solve the equation
is the number of evaluations of the function
f
on the right-hand side. For example, the textbook RK4 method estimates the solution at each step by
where
which requires four stages, i.e. four evaluations of
f
.
Order
A differential equation solver is said to have order
p
if the local error, the error after one step of size
h
, is
O
(
h
p
+ 1
). Then after solving an ODE over a period of time
T
with
N
=
T
/
h
steps, the global error is
O
(
h
p
). So, for example, if
p
= 4, you would expect that cutting your step size
h
in half would cut your error at
T
by a factor of 16.
More stages than the order
John C. Butcher proved that an explicit RK method of order
p
requires
s
stages where
s
>
p
if
p
> 4.
An important example is the Dormand-Prince method. It is a version of RK that has order 5 and 7 stages. The clever thing about this method is that you can make a 4th order solver out of a subset of its function evaluations.
That means that after you’ve evaluated one step of the 5th order method, you can also evaluate a 4th order method essentially for free. And by comparing them, you can get a sense of the error. If the solutions given by the two methods are substantially different, you have probably taken too big a step and need to back up. If the two solutions essentially agree, you’re probably good to take the next step.
For an explict RK method to have order 5, 6, or 7 you need at least 6, 7, or 9 stages respectively.
