---
title: "Patcher Part 5 : Aside for some proofs"
url: "http://cbloomrants.blogspot.com/2023/09/patcher-part-5-aside-for-some-proofs.html"
fetched_at: 2026-05-05T07:01:47.788379+00:00
source: "Charles Bloom"
tags: [blog, raw]
---

# Patcher Part 5 : Aside for some proofs

Source: http://cbloomrants.blogspot.com/2023/09/patcher-part-5-aside-for-some-proofs.html

Just for my own entertainment, a brief aside to prove some facts we used in the last post.
After drawing N random numbers in [0,1] , the chance that the next number you draw is a new minimum is 1/(N+1)
which is also equivalent to :
The expectation (mean) of the min of N random numbers in [0,1] is 1/(N+1)
this is important to us because it means the branch for the min changing in the core CDC loop is rare.
The proof is very simple.  On a set of N random numbers, the change of each number being the min is equal,
therefore when you draw a new number and have (N+1), the chance that the new one is the min is 1/(N+1).
This then also gives you the mean of the min, since the change of drawing a new min in [0,1] is just equal
to the mean of the min.
So eg. the mean of the min of 2 draws is 1/3
I think this is a fun proof because it's much more direct (and doesn't use any calculus) than the straightforward
way, in which you construct the CDF of the min being t and then integrate over t.  If you do that (CDF method)
you'll wind up with an integral of t^N which gives you the 1/(N+1).  All the other discussion of this topic I could
find on the net uses this more brute force approach, eg :
the-expectation-of-the-minimum-of-iid-uniform-random-variables
and
expectation-of-minimum-of-n-i-i-d-uniform-random-variables
Next :
If you draw random numbers in [0,1], stopping when one is below (1/N), you will stop on average after N draws
this one is just a very straightforward property of the geometric distribution.
Going through the detail :
you stop after 1 if you draw a random < (1/N) , which is probability (1/N)

P(1) = (1/N)

to stop after 2, you have to first not stop after 1, so that's probability (1 - (1/N))
then stop with probabily (1/N)

P(2) = (1/N) * (1 - (1/N))
P(3) = (1/N) * (1 - (1/N))^2
etc.

P(i) = (1/N) * (1 - (1/N))^(i-1)

set r = 1 - (1/N)

P(i) = (1-r) * r^(i-1)
i >= 1

P(i) is a geometric distribution

The average stopping len is :

L = Sum_i { i * P(i) }

L = (1-r) * Sum_i { i * r^(i-1) }
L = (1-r) * S

where S is a sum we need to compute :

S = Sum_i { i * r^(i-1) } = 1 + 2*r + 3*r^2 + ...

Use the usual trick for geometric distributions :

r*S = r + 2*r^2 + 3*r^3 + ...

S - r*S = 1 + r + r^2 + .. = G
S = G /(1-r)

G is the classic geometric sum :

G = Sum_i>=0 { r^i } = 1/(1-r)

S = G/(1-r) = 1/(1-r)^2

L = (1-r)*S = 1/(1-r) = N

The average stopping len is N
Which is just the mean of the geometric distribution.
BTW The alternate way to get "S" is a bit quicker :

S = Sum_i { i * r^(i-1) } = d/dr Sum_i { r^i } = d/dr G

S = d/dr 1/(1-r) = 1/(1-r)^2
Just for some laughs.
Aside on the aside : Just to stick this note somewhere :
I mentioned an alternative scheme to using the min might be to reduce the target len N as you go.
(recall, this is to prevent degenerate cases where the condition hash < (1/N) is not being hit for a long
time, much more than N steps).
In fact, you can do :
div = 2 * N;

make hash

threshold = (~0ULL)/div;

if ( hash < threshold ) break; // <- found a split

div--;
Making "div" lower after each step, which effectively targets a shorter average chunk length (hence easier
to hit).
In practice you would want to avoid the divide, since you can't just precompute it the way you would in the
normal scheme :
make 32-bit hash

if ( hash*div < (1ULL<<32) ) break; // <- found a split

div --;
After 2N steps, this makes "div" go to zero, so your fragment len is strictly limited in [0,2N] ,
and the probability of each length is uniform!
P(L) = 1/2N

average len = N
That's kind of neat.  However, it's not clear this is a good scheme.  It makes the natural cut condition
not entirely location independent, because we aren't checking the same threshold all the time, it does
not depend only on the value of the local neighborhood of bytes.  Instead, the threshold used here always
depends on where the search started, so you have a non-local distance affecting the cut decision.
Whether that is bad in practice is unknown, I have not tried this scheme in the real patcher.  It also is
perhaps slower in the inner looop, but does avoid the need to track the min, so YMMV.
Showing the uniform probability :

let D = initial "div" = 2*N

stop at len 1 if initial (1/D) check is true :

P(1) = 1/D

then we would do div-- , so checking 1/(D-1) next
so we must have that the len is not 1, and also the next 1/(D-1) check is true :

P(2) = (1 - 1/D) * (1/(D-1))

(1 - 1/D) = (D-1)/D

P(2) = ((D-1)/D) * (1/(D-1)) = 1/D

similarly for P(3), we must have not the initial 1/D and also not the next 1/(D-1),
and then meet the 1/(D-2) condition, so :

P(3) = (1 - 1/D) (1 - 1/(D-1)) * (1/(D-2))
P(3) = ((D-1)/D) * ((D-2)/(D-1)) * (1/(D-2)) = 1/D

etc.
