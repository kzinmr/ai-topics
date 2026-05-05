---
title: "Sattolo's algorithm"
url: "https://danluu.com/sattolo/"
fetched_at: 2026-05-05T07:01:31.226102+00:00
source: "Dan Luu"
tags: [blog, raw]
---

# Sattolo's algorithm

Source: https://danluu.com/sattolo/

I recently had a problem where part of the solution was to do a series of pointer accesses that would walk around a chunk of memory in pseudo-random order. Sattolo's algorithm provides a solution to this because it produces a permutation of a list with exactly one cycle, which guarantees that we will reach every element of the list even though we're traversing it in random order.
However, the explanations of why the algorithm worked that I could find online either used some kind of mathematical machinery (Stirling numbers, assuming familiarity with cycle notation, etc.), or used logic that was hard for me to follow. I find that this is common for explanations of concepts that could, but don't have to, use a lot of mathematical machinery. I don't think there's anything wrong with using existing mathematical methods per se -- it's a nice mental shortcut if you're familiar with the concepts. If you're taking a combinatorics class, it makes sense to cover Stirling numbers and then rattle off a series of results whose proofs are trivial if you're familiar with Stirling numbers, but for people who are only interested in a single result, I think it's unfortunate that it's hard to find a relatively simple explanation that
doesn't require any background
. When I was looking for a simple explanation, I also found a lot of people who were using Sattolo's algorithm in places where it wasn't appropriate and also people who didn't know that Sattolo's algorithm is what they were looking for, so here's an attempt at an explanation of why the algorithm works that doesn't assume an undergraduate combinatorics background.
Before we look at Sattolo's algorithm, let's look at Fisher-Yates, which is an
in-place
algorithm that produces a random permutation of an array/vector, where every possible permutation occurs with uniform probability.
We'll look at the code for Fisher-Yates and then how to prove that the algorithm produces the intended result.
def shuffle(a):
    n = len(a)
    for i in range(n - 1):  # i from 0 to n-2, inclusive.
        j = random.randrange(i, n)  # j from i to n-1, inclusive.
        a[i], a[j] = a[j], a[i]  # swap a[i] and a[j].
shuffle
takes an array and produces a permutation of the array, i.e., it shuffles the array. We can think of this loop as placing each element of the array,
a
, in turn, from
a[0]
to
a[n-2]
. On some iteration,
i
, we choose one of
n-i
elements to swap with and swap element
i
with some random element. The last element in the array,
a[n-1]
, is skipped because it would always be swapped with itself. One way to see that this produces every possible permutation with uniform probability is to write down the probability that each element will end up in any particular location. Another way to do it is to observe two facts about this algorithm:
Every output that Fisher-Yates produces is produced with uniform probability
Fisher-Yates produces as many outputs as there are permutations (and each output is a permutation)
(1) For each random choice we make in the algorithm, if we make a different choice, we get a different output. For example, if we look at the resultant
a[0]
, the only way to place the element that was originally in
a[k]
(for some
k
) in the resultant
a[0]
is to swap
a[0]
with
a[k]
in iteration
0
. If we choose a different element to swap with, we'll end up with a different resultant
a[0]
. Once we place
a[0]
and look at the resultant
a[1]
, the same thing is true of
a[1]
and so on for each
a[i]
. Additionally, each choice reduces the range by the same amount -- there's a kind of symmetry, in that although we place
a[0]
first, we could have placed any other element first; every choice has the same effect. This is vaguely analogous to the reason that you can pick an integer uniformly at random by picking digits uniformly at random, one at a time.
(2) How many different outputs does Fisher-Yates produce? On the first iteration, we fix one of
n
possible choices for
a[0]
, then given that choice, we fix one of
n-1
choices for
a[1]
, then one of
n-2
for
a[2]
, and so on, so there are
n * (n-1) * (n-2) * ... 2 * 1 = n!
possible different outputs.
This is exactly the same number of possible permutations of
n
elements, by pretty much the same reasoning. If we want to count the number of possible permutations of
n
elements, we first pick one of
n
possible elements for the first position,
n-1
for the second position, and so on resulting in
n!
possible permutations.
Since Fisher-Yates only produces unique permutations and there are exactly as many outputs as there are permutations, Fisher-Yates produces every possible permutation. Since Fisher-Yates produces each output with uniform probability, it produces all possible permutations with uniform probability.
Now, let's look at Sattolo's algorithm, which is almost identical to Fisher-Yates and also produces a shuffled version of the input, but produces something quite different:
def sattolo(a):
    n = len(a)
    for i in range(n - 1):
        j = random.randrange(i+1, n)  # i+1 instead of i
        a[i], a[j] = a[j], a[i]
Instead of picking an element at random to swap with, like we did in Fisher-Yates, we pick an element at random that is not the element being placed, i.e., we do not allow an element to be swapped with itself. One side effect of this is that no element ends up where it originally started.
Before we talk about why this produces the intended result, let's make sure we're on the same page regarding terminology. One way to look at an array is to view it as a description of a graph where the index indicates the node and the value indicates where the edge points to. For example, if we have the list
0 2 3 1
, this can be thought of as a directed graph from its indices to its value, which is a graph with the following edges:
0 -> 0
1 -> 2
2 -> 3
3 -> 1
Node 0 points to itself (because the value at index 0 is 0), node 1 points to node 2 (because the value at index 1 is 2), and so on. If we traverse this graph, we see that there are two cycles.
0 -> 0 -> 0 ...
and
1 -> 2 -> 3 -> 1...
.
Let's say we swap the element in position 0 with some other element. It could be any element, but let's say that we swap it with the element in position 2. Then we'll have the list
3 2 0 1
, which can be thought of as the following graph:
0 -> 3
1 -> 2
2 -> 0
3 -> 1
If we traverse this graph, we see the cycle
0 -> 3 -> 1 -> 2 -> 0...
. This is an example of a permutation with exactly one cycle.
If we swap two elements that belong to different cycles, we'll merge the two cycles into a single cycle. One way to see this is when we swap two elements in the list, we're essentially picking up the arrow-heads pointing to each element and swapping where they point (rather than the arrow-tails, which stay put). Tracing the result of this is like tracing a figure-8. Just for example, say if we swap
0
with an arbitrary element of the other cycle, let's say element 2, we'll end up with
3 2 0 1
, whose only cycle is
0 -> 3 -> 1 -> 2 -> 0...
. Note that this operation is reversible -- if we do the same swap again, we end up with two cycles again. In general, if we swap two elements from the same cycle, we break the cycle into two separate cycles.
If we feed a list consisting of
0 1 2 ... n-1
to Sattolo's algorithm we'll get a permutation with exactly one cycle. Furthermore, we have the same probability of generating any permutation that has exactly one cycle. Let's look at why Sattolo's generates exactly one cycle. Afterwards, we'll figure out why it produces all possible cycles with uniform probability.
For Sattolo's algorithm, let's say we start with the list
0 1 2 3 ... n-1
, i.e., a list with
n
cycles of length
1
. On each iteration, we do one swap. If we swap elements from two separate cycles, we'll merge the two cycles, reducing the number of cycles by 1. We'll then do
n-1
iterations, reducing the number of cycles from
n
to
n - (n-1) = 1
.
Now let's see why it's safe to assume we always swap elements from different cycles. In each iteration of the algorithm, we swap some element with index >
i
with the element at index
i
and then increment
i
. Since
i
gets incremented, the element that gets placed into index
i
can never be swapped again, i.e., each swap puts one of the two elements that was swapped into its final position, i.e., for each swap, we take two elements that were potentially swappable and render one of them unswappable.
When we start, we have
n
cycles of length
1
, each with
1
element that's swappable. When we swap the initial element with some random element, we'll take one of the swappable elements and render it unswappable, creating a cycle of length
2
with
1
swappable element and leaving us with
n-2
other cycles, each with
1
swappable element.
The key invariant that's maintained is that each cycle has exactly
1
swappable element. The invariant holds in the beginning when we have
n
cycles of length
1
. And as long as this is true, every time we merge two cycles of any length, we'll take the swappable element from one cycle and swap it with the swappable element from the other cycle, rendering one of the two elements unswappable and creating a longer cycle that still only has one swappable element, maintaining the invariant.
Since we cannot swap two elements from the same cycle, we merge two cycles with every swap, reducing the number of cycles by 1 with each iteration until we've run
n-1
iterations and have exactly one cycle remaining.
To see that we generate each cycle with equal probability, note that there's only one way to produce each output, i.e., changing any particular random choice results in a different output. In the first iteration, we randomly choose one of
n-1
placements, then
n-2
, then
n-3
, and so on, so for any particular cycle, we produce it with probability
(n-1) * (n-2) * (n-3) ... * 2 * 1 = (n-1)!
. If we can show that there are
(n-1)!
permutations with exactly one cycle, then we'll know that we generate every permutation with exactly one cycle with uniform probability.
Let's say we have an arbitrary list of length
n
that has exactly one cycle and we add a single element, there are
n
ways to extend that to become a cycle of length
n+1
because there are
n
places we could add in the new element and keep the cycle, which means that the number of cycles of length
n+1
,
cycles(n+1)
, is
n * cycles(n)
.
For example, say we have a cycle that produces the path
0 -> 1 -> 2 -> 0 ...
and we want to add a new element,
3
. We can substitute
-> 3 ->
for any
->
and get a cycle of length 4 instead of length 3.
In the base case, there's one cycle of length 2, the permutation
1 0
(the other permutation of length two,
0 1
, has two cycles of length one instead of having a cycle of length 2), so we know that
cycles(2) = 1
. If we apply
the recurrence above
, we get that
cycles(n) = (n-1)!
, which is exactly the number of different permutations that Sattolo's algorithm generates, which means that we generate all possible permutations with one cycle. Since we know that we generate each cycle with uniform probability, we now know that we generate all possible one-cycle permutations with uniform probability.
An alternate way to see that there are
(n-1)!
permutations with exactly one cycle, is that we rotate each cycle around so that
0
is at the start and write it down as
0 -> i -> j -> k -> ...
. The number of these is the same as the number of permutations of elements to the right of the
0 ->
, which is
(n-1)!
.
Conclusion
We've looked at two algorithms that are identical, except for a two character change. These algorithms produce quite different results -- one algorithm produces a random permutation and the other produces a random permutation with exactly one cycle. I think these algorithms are neat because they're so simple, just a double for loop with a swap.
In practice, you probably don't "need" to know how these algorithms work because the standard library for most modern languages will have some way of producing a random shuffle. And if you have a function that will give you a shuffle, you can produce a permutation with exactly one cycle if you don't mind a non-in-place algorithm that takes an extra pass. I'll leave that as an exercise for the reader, but if you want a hint, one way to do it parallels the "alternate" way to see that there are
(n-1)!
permutations with exactly one cycle.
Although I said that you probably don't need to know this stuff, you do actually need to know it if you're going to implement a custom shuffling algorithm! That may sound obvious, but there's a long history of people implementing incorrect shuffling algorithms. This was common in games and on
online gambling sites in the 90s and even the early 2000s
and you still see the occasional mis-implemented shuffle, e.g., when
Microsoft implemented a bogus shuffle and failed to properly randomize a browser choice poll
. At the time, the top Google hit for
javascript random array sort
was
the incorrect algorithm that Microsoft ended up using
. That site has been fixed, but you can still find incorrect tutorials floating around online.
Appendix: generating a random derangement
A permutation where no element ends up in its original position is called a derangement. When I searched for uses of Sattolo's algorithm, I found many people using Sattolo's algorithm to generate random derangements. While Sattolo's algorithm generates derangements, it only generates derangements with exactly one cycle, and there are derangements with more than one cycle (e.g.,
3 2 1 0
), so it can't possibly generate random derangements with uniform probability.
One way to generate random derangements is to generate random shuffles using Fisher-Yates and then retry until we get a derangement:
def derangement(n):
    assert n != 1, "can't have a derangement of length 1"
    a = list(range(n))
    while not is_derangement(a):
        shuffle(a)
    return a
This algorithm is simple, and is overwhelmingly likely to eventually return a derangement (for n != 1), but it's not immediately obvious how long we should expect this to run before it returns a result. Maybe we'll get a derangement on the first try and run
shuffle
once, or maybe it will take 100 tries and we'll have to do 100 shuffles before getting a derangement.
To figure this out, we'll want to know the probability that a random permutation (shuffle) is a derangement. To get that, we'll want to know, given a list of of length
n
, how many permutations there are and how many derangements there are.
Since we're deep in the appendix, I'll assume that you know
the number of permutations of a n elements is
n!
what
binomial coefficients
are, and are comfortable with
Taylor series
.
To count the number of derangements, we can start with the number of permutations,
n!
, and subtract off permutations where an element remains in its starting position,
(n choose 1) * (n - 1)!
. That isn't quite right because this double subtracts permutations where two elements remain in the starting position, so we'll have to add back
(n choose 2) * (n - 2)!
. That isn't quite right because we've overcorrected elements with three permutations, so we'll have to add those back,
and so on and so forth
, resulting in
∑ (−1)ᵏ (n choose k)(n−k)!
. If we expand this out and divide by
n!
and cancel things out, we get
∑ (−1)ᵏ (1 / k!)
. If we look at the limit as the number of elements goes to infinity, this looks just like
the Taylor series
for
e^x
where
x = -1
, i.e.,
1/e
, i.e., in the limit, we expect that the fraction of permutations that are derangements is
1/e
, i.e., we expect to have to do
e
times as many swaps to generate a derangement as we do to generate a random permutation. Like many alternating series, this series converges quickly. It gets within 7 significant figures of
e
when
k = 10
!
One silly thing about our algorithm is that, if we place the first element in the first location, we already know that we don't have a derangement, but we continue placing elements until we've created an entire permutation. If we reject illegal placements, we can do even better than a factor of
e
overhead. It's also possible to come up with
a non-rejection based algorithm
, but I really enjoy the naive rejection based algorithm because I find it delightful when
basic randomized algorithms that consist of "keep trying again" work well
.
Appendix: wikipedia's explanation of Sattolo's algorithm
I wrote this explanation because I found
the explanation in Wikipedia
relatively hard to follow, but if you find the explanation above difficult to understand, maybe you'll prefer wikipedia's version:
The fact that Sattolo's algorithm always produces a cycle of length n can be shown by induction. Assume by induction that after the initial iteration of the loop, the remaining iterations permute the first n - 1 elements according to a cycle of length n - 1 (those remaining iterations are just Sattolo's algorithm applied to those first n - 1 elements). This means that tracing the initial element to its new position p, then the element originally at position p to its new position, and so forth, one only gets back to the initial position after having visited all other positions. Suppose the initial iteration swapped the final element with the one at (non-final) position k, and that the subsequent permutation of first n - 1 elements then moved it to position l; we compare the permutation π of all n elements with that remaining permutation σ of the first n - 1 elements. Tracing successive positions as just mentioned, there is no difference between σ and π until arriving at position k. But then, under π the element originally at position k is moved to the final position rather than to position l, and the element originally at the final position is moved to position l. From there on, the sequence of positions for π again follows the sequence for σ, and all positions will have been visited before getting back to the initial position, as required.
As for the equal probability of the permutations, it suffices to observe that the modified algorithm involves (n-1)! distinct possible sequences of random numbers produced, each of which clearly produces a different permutation, and each of which occurs--assuming the random number source is unbiased--with equal probability. The (n-1)! different permutations so produced precisely exhaust the set of cycles of length n: each such cycle has a unique cycle notation with the value n in the final position, which allows for (n-1)! permutations of the remaining values to fill the other positions of the cycle notation
Thanks to Mathieu Guay-Paquet, Leah Hanson, Rudi Chen, Kamal Marhubi, Michael Robert Arntzenius, Heath Borders, Shreevatsa R, @chozu@fedi.absturztau.be, and David Turner for comments/corrections/discussion.
