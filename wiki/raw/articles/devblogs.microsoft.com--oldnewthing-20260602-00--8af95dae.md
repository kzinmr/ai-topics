---
title: "Rotation revisited: Another unidirectional algorithm"
url: "https://devblogs.microsoft.com/oldnewthing/20260602-00/?p=112376"
fetched_at: 2026-06-03T07:01:40.842548+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# Rotation revisited: Another unidirectional algorithm

Source: https://devblogs.microsoft.com/oldnewthing/20260602-00/?p=112376

Some time ago, we looked at the problem of
swapping two blocks of memory that reside inside a larger block, in constant memory
, and along the way, we learned about
std::
rotate
which swaps two
adjacent
blocks of memory (not necessarily the same size).
I noted in a postscript that
clang’s libcxx
and
gcc’s libstdc++
contain specializations of
std::
rotate
for random-access iterators that view the operation as a permutation and decomposes the permutation into cycles.
I was mistaken.
The implementation in gcc’s libstdc++ has special cases for single-element rotations, but in the general case, it uses a different algorithm.
Let’s call the blocks of memory to be exchanged A and B, where A is made up of elements A1, A2, A3, and so on; and block B has elements B1, B2, B3, and so on. Without loss of generality, suppose the A block is smaller. (If not, we can just mirror the algorithm.) And for concreteness let’s say that the elements are A1, A2, A3, B1, B2, B3, B4, B5.
A1
A2
A3
B1
B2
B3
B4
B5
↑
↑
↑
first
mid
last
Exchange elements at
first
and
mid
, then move both iterators forward. After the first step, we have this:
B1
A2
A3
A1
B2
B3
B4
B5
↑
↑
↑
first
mid
last
After three steps, we have moved all of the A’s out and replaced them with an equal number of B’s.
B1
B2
B3
A1
A2
A3
B4
B5
↑
↑
↑
first
mid
last
But don’t stop. Keep on going until
mid
reaches
last
.
B1
B2
B3
B4
B5
A3
A1
A2
↑
↑
first
mid
last
All of the B’s have been swapped to their final positions, but the A’s are jumbled.
But you can predict the exact nature of the jumbling. The A block is in two chunks. If we let
n
be the total number of elements |A| + |B| and
a
be the number of elements in A, then the first chunk has the final
n
%
a
elements, and the second chunk has the initial
a
− (
n
%
a
) elements.
Therefore, we can recursively rotate the two pieces of the A block to finish the job. Move
mid
to
first
+ (
n
%
a
) and restart the algorithm.
This algorithm performs
n
− 1 swaps. You can calculate this inductively by observing that we perform |B| swaps, and then recursively rotate |A|. Or you can calculate this directly by observing that each swap moves one element to its final position, except that the final swap moves two elements to their final position.
The locality of this algorithm fairly good. The
first
iterator moves steadily forward, and the
mid
iterator moves forward most of the time, with at most
O
(log (min(|A|, |B|)) backward resets.
Next time, we’ll make a shocking discovery about this algorithm.
