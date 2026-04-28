---
title: "I hate bubblesort"
url: "https://www.chiark.greenend.org.uk/~sgtatham/quasiblog/bubblesort/"
fetched_at: 2026-04-28T07:01:34.241027+00:00
source: "chiark.greenend.org.uk/~sgtatham"
tags: [blog, raw]
---

# I hate bubblesort

Source: https://www.chiark.greenend.org.uk/~sgtatham/quasiblog/bubblesort/

I hate bubblesort
[Simon Tatham, 2023-12-06]
Many years ago, my employer used to use “Can you name any
      sorting algorithms?” as a quickie interview question.
I’m something of a sorting-algorithms nerd, which is a
      quality that often comes with strong opinions. My personal
      prejudice (although I did my best not to let it affect the
      outcome of the interview) was that I was always extra pleased if
      our candidate listed a handful of well-known algorithm names
      and
didn’t mention bubblesort
.
Why? Because I hate it. Bubblesort is an awful sorting
      algorithm, and I wish people would stop teaching it.
The sorting-algorithms landscape
Seen from a long way up in the air, the landscape of sorting
      algorithms consists basically of three categories:
Well-known
O
(
N
2
) algorithms
:
      insertion sort, selection sort,
      bubblesort.
Well-known
O
(
N
log
N
)
      algorithms
: quicksort, heapsort,
      mergesort.
More advanced stuff
: introsort,
      smoothsort, special-purpose things that rely on the keys being
      integers or uniformly distributed, etc.
(Yes, there are lots of ways you might quibble with this
      analysis. For example, what about the quadratic-time worst case
      of quicksort? And what about shellsort, somewhere in between the
      first two categories? And if you’re in a frivolous mood you
      might even object to me leaving out the joke algorithms,
      like
bogosort
and
slowsort
.
      So yes, this picture is a gross simplification, but it’s enough
      for my current purposes.)
An obvious question, looking at this list, is: what’s the point
      of the first category?
Why
would anyone use a
      quadratic-time algorithm when faster ones are available? Aren’t
      they just as pointless as the joke algorithms?
Reasons to use a quadratic sorting algorithm: simplicity
One obvious answer is that the quadratic-time algorithms are
      generally much simpler. They require less code; they’re easier
      to remember; there are fewer ways to get them wrong.
So if you’re coding under very serious space constraints, and
      trying to cram a sorting algorithm into the tiniest possible
      amount of space in some embedded device’s ROM, then it may be a
      better idea to implement, say, selection sort than heapsort,
      simply because it will fit.
And if in some highly improbable scenario you’re caught without
      a standard library, out of touch with your reference materials,
      and you need to sort something using only the knowledge
      currently in your brain, you might very well decide you have a
      better chance of not messing up one of those really simple
      three-line algorithms than getting all the edge cases right in
      heapsort.
A more realistic case is that if you’re
teaching
sorting algorithms, it makes sense to start your students off on
      a really simple one before diving into the complicated ones.
      (Especially since then they can do the experiment of comparing
      the running times of both, and see for themselves how one scales
      worse than the other.)
Reasons to use a quadratic sorting algorithm: as a subroutine
Also, some of the quadratic-time algorithms have genuinely
      practical uses, as subroutines in more complicated sorting
      operations.
Insertion sort is
O
(
N
2
) in the worst
      case for a fully general input list, but it guarantees far
      better performance than that in the situation where every
      element is at most a short distance from its correct position.
      For this reason, it’s used as the final pass of shellsort,
      because the effect of the previous passes was to get the array
      into exactly the kind of ‘nearly sorted’ state where insertion
      sort does perform well.
Insertion sort also has the great virtue of
      being
stable
: input items that compare equal are not
      reordered. (This can be important if the part of the object
      you’re using as the sort criterion is not the whole of the
      object.) That doesn’t help in shellsort, which has already
      broken stability in its earlier passes; but for this reason
      insertion sort (on small sublists of the input) is often used as
      the first pass of mergesort, which is a faster sorting algorithm
      that
does
preserve stability throughout.
Selection sort has neither of those advantages, but it has a
      totally different virtue: although it
      uses
O
(
N
2
)
comparisons
, you
      can implement it so that it uses
      only
O
(
N
)
swaps
. (Do nothing but
      comparisons until you’ve found the element you want to put in
      position 0; do a single swap to put it there; then never touch
      it again. Repeat on the rest of the array.) For this reason, it
      finds occasional uses in situations where you’re
      sorting
huge
objects by a simple criterion, so that the
      swaps are much more expensive than the comparisons.
For example: in at least one of the really complicated systems
      for making mergesort work in-place on the input array, there’s a
      step in which you divide the array of
N
elements into
      about √
N
blocks of size √
N
, and sort those entire
      blocks by their first element. In this case, selection sort is
      just what you want, because the cost of a swap scales with the
      input array, i.e. they can get unboundedly expensive. So you use
      selection sort in this ‘minimal swaps’ style, and that way, the
      total work done by all the swaps is linear in the total size of
      the array. And meanwhile, it doesn’t matter that selection sort
      uses a quadratic number of comparisons, because the number of
      elements it’s sorting is √
N
, and squaring that only gets
      you back to
N
. So this whole step runs in linear time,
      and it wouldn’t if you used any other sorting algorithm, not
      even the ones that look obviously better!
Bubblesort has no practical virtues
I’ve just listed some virtues of two of the well-known
      quadratic-time algorithms. But I didn’t list any similar virtues
      of bubblesort. That’s because, as far as I know, it has none, or
      at least none that the other quadratic-time algorithms don’t do
      better.
One way to look at bubblesort is that it’s essentially a form
      of selection sort, in that each pass brings another element to
      its final position and never moves it again. But it’s selection
      sort implemented with as
many
swaps as possible, rather
      than as few as possible – so it’s thrown away the only
      performance virtue of selection sort.
On the other hand, bubblesort tries to have some of the same
      virtues as insertion sort: it’s stable (if you write the
      comparison carefully), and it can terminate early if the input
      was already sorted, or ‘nearly sorted’, in that you can stop as
      soon as one of your passes performs no swaps. But insertion
      sort
also
has those properties, and its notion of
      ‘nearly sorted’ is more useful – the types of input list on
      which insertion sort can beat quadratic time are more likely to
      actually come up than the ones for which bubblesort terminates
      early.
So bubblesort isn’t useful as a subroutine in any other sorting
      algorithm that I know of, or in any other specialist situation.
      If it has any uses at all, it’s
only
useful for its
      simplicity.
Bubblesort isn’t even a good teaching sort
And indeed, the usual place that bubblesort comes up is in
      teaching, because people have the idea that it’s the simplest,
      or most intuitive, sorting algorithm, so they teach it
      first.
I don’t think even
that
is true!
I think that there’s nothing unintuitive about selection sort.
      “Find the smallest thing and move it to position 0. Then find
      the next smallest thing and move it to position 1, and so on.”
      This is surely one of the simplest, and most easily
      comprehensible, sorting concepts that you can imagine.
Compared to that, bubblesort is actually
more
      complicated
, because it works for the same reason (it
      essentially
is
a form of selection sort), but instead
      of that being instantly obvious from the algorithm description,
      it’s a property you have to prove. The “keep iterating until
      done” structure doesn’t even obviously guarantee that the
      algorithm
terminates
: that’s something you have to
      prove too (e.g. by showing that in every pass at least one
      element reaches its final position, or maybe by showing that
      every swap strictly decreases the total number of misordered
      pairs). Maybe that makes it a useful exercise in proof by
      induction, or something? But what it
doesn’t
make it is
      the simplest sorting algorithm.
I myself encountered bubblesort before any other sort, on the
      ZX Spectrum’s ‘Horizons’ educational software tape in the early
      1980s. Some years later (when I still hadn’t learned any fancy
      sort algorithms yet) I saw a school friend write a sort routine
      in BBC BASIC using two nested
FOR
loops containing
      a conditional swap, which turned out to be a form of selection
      sort. My friend didn’t know
why
it worked; he just knew
      that this was the easiest piece of code to
remember by
      rote
that will sort things properly. And I agreed – it’s
      easier to remember than bubblesort, and I switched to doing it
      his way!
If you want to start by teaching the
simplest possible
sorting algorithm, I think selection sort is it (without
      bothering to minimise swaps). If you prefer a
slightly
more interesting one so that you can talk about early
      termination and/or stability, insertion sort is good.
Conclusion
A quadratic-time sorting algorithm can be useful in teaching.
      But I think bubblesort isn’t the best choice.
Some quadratic-time sorting algorithms also have uses in
      special situations, where they unexpectedly become the best
      choice for something. But bubblesort is never the best choice in
      that situation either.
Bubblesort is never the best choice. For
      anything.
Let’s stop pointlessly filling up space in
      people’s minds with it!
Afterword
Shortly after I posted this, someone brought to my attention
      an
interesting
      blog post by Hillel Wayne
, also on the subject of whether
      bubblesort is ever useful, dated two days before this. I hadn’t
      seen that post when I wrote this one, and the close timing is
      purely coincidental! Nothing in this post is intended as a
      response to that one. But if you’d like further reading on this
      topic, there’s a link for you.
