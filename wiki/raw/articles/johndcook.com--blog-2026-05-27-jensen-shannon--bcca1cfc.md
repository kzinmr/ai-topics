---
title: "Kullback-Leibler divergence"
url: "https://www.johndcook.com/blog/2026/05/27/jensen-shannon/"
fetched_at: 2026-05-28T07:00:50.039391+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Kullback-Leibler divergence

Source: https://www.johndcook.com/blog/2026/05/27/jensen-shannon/

Kullback-Leibler divergence
Kullback-Leibler divergence is defined for two random variables
X
and
Y
by
K-L divergence is non-negative, and it’s zero if and only if
X
and
Y
have the same distribution. But it is not a metric, for reasons explained
here
. For one thing, it’s not symmetric.
Jeffreys divergence
We can fix the symmetry problem by defining
The
J
above stands for Jeffreys, for Harold Jeffreys.
J
is called either the symmetrized K-L divergence or Jeffreys’ divergence. It’s still a divergence, not a distance.
A distance (metric)
d
has to have four properties:
d
(
x
,
x
) = 0
d
(
x
,
y
) > 0 if
x
≠
y
d
(
x
,
y
) =
d
(
y
,
x
)
d
(
x
,
z
) ≤
d
(
x
,
y
) +
d
(
y
,
z
)
K-L divergence satisfies the first two properties. Jeffreys’ divergence satisfies the first three, but not the last one, the triangle inequality.
To show that
J
doesn’t satisfy the triangle inequality, let
X
,
Y
, and
Z
be Bernoulli random variables with
p
equal to 0.1, 0.2, and 0.3 respectively. Then the following Python code shows that the divergence from
X
to
Y
, plus the divergence from
Y
to
Z
, is less than the divergence from
X
to
Z
. This would be like saying you could get from LA to NYC faster by having a layover in Denver rather than taking a direct flight.
from math import log

kl = lambda p, q: p*log(p/q) + (1-p)*log((1-p)/(1-q))
j  = lambda p, q: kl(p, q) + kl(q, p)

a = j(0.1, 0.2)
b = j(0.2, 0.3)
c = j(0.1, 0.3)
print(a + b, c)
This prints 0.135 and 0.270.
Jensen-Shannon distance
Jensen-Shannon distance turns K-L divergence into a metric as follows. First, define the random variable
M
to be the average of
X
and
Y
. Then average the K-L divergence from
M
to each of
X
and
Y
. This defines the Jensen-Shannon
divergence
. It’s still not a metric, but it’s square root is, which defines the Jensen-Shannon
distance
.
The following code gives an example of Jensen-Shannon distance satisfying the triangle inequality.
def d(p, q):
    m = 0.5*(p + q)
    jsd = 0.5*kl(p, m) + 0.5*kl(q, m) 
    return jsd**0.5

a = d(0.1, 0.2)
b = d(0.2, 0.3)
c = d(0.1, 0.3)
print(a + b, c)
This prints 0.1817 and 0.1801. Now a layover makes the trip longer.
