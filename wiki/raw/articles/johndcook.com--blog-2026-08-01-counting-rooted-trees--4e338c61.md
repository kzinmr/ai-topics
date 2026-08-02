---
title: "Counting rooted trees"
url: "https://www.johndcook.com/blog/2026/08/01/counting-rooted-trees/"
fetched_at: 2026-08-02T10:14:20.130453+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Counting rooted trees

Source: https://www.johndcook.com/blog/2026/08/01/counting-rooted-trees/

Combinatorial problems can be interesting for their own sake, but they are more interesting when there is a connection to a problem outside combinatorics, and the more unexpected the connection the better.
Counting the number of unlabeled rooted trees [1] with
n
nodes is a pure mathematics problem. Designing numerical methods for solving differential equations is an applied mathematics problem. And yet the two are closely linked.
Let
t
(
n
) be the number of distinct unlabeled rooted trees with
n
nodes. The diagram below shows that the first few terms of this sequence are 1, 1, 2, and 4.
In an
earlier post
I showed that designing a 4-stage explicit Runge-Kutta method required solving a system of 8 equations in 10 unknowns, leaving two degrees of freedom in the solutions.
The number of constraints
c
(
s
) needed to design an
s
-stage explicit RK method is equal to the number of rooted trees with up to
s
nodes:
c
(
s
) =
t
(1) +
t
(2) +
t
(3) + … +
t
(
s
)
This is because there is a one-to-one correspondence between constrains on the
n
th derivative of an RK formula and rooted trees, and an
s
stage method has to satisfy the constraints of all stages up to
s
. In the example of the 4th order RK method, we have
c
(4) =
t
(1) +
t
(2)  +
t
(3) +
t
(4) = 1 + 1 + 2 + 4 = 8.
The first few values [2] of
t
(
n
) are
1, 1, 2, 4, 9, 20, 48, 115, 286, 719, 1842, 4766, 12486, 32973, …
and so you can see that
t
(
n
) grows quickly. In fact, it grows exponentially [3].
However, the number of parameters in an
s
stage RK method is
s
(
s
+ 1)/2. The number of equations grows exponentially and the number of variables grows only quadratically, so at some point you have more equations than variables. That’s already the case for
s
= 5 because you have 17 constraints on 15 variables. The system has a solution because symmetry considerations render some of the equations redundant.
A 10th order RK method requires 17 stages. (See the
previous post
for why the number of stages exceeds the order when the order is greater than 4.) Designing such a method would require solving over a million equations in 153 variables, and yet it can be done. [4]
Related posts
[1] This is a slightly contradictory term. Unlabeled means the we don’t distinguish the nodes. But we do distinguish one node, namely the root.
[2] See OEIS
A000081
.
[2] Richard Otter proved in 1948 that the number of unlabeled rooted trees with
n
nodes is asymptotically
C
α
n
/
n
−3/2
where
C
= 0.4399… and α = 2.9557…. The cumulative sum is at least this large since Otter’s estimate gives the size of the last term in the sum.
[3] E. Hairer. A Runge-Kutta Method of Order 10. J. Inst. Maths Applics (1978) 21, 47-59
