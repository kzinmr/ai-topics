---
title: "Rotation revisited: A shocking discovery about gcc's unidirectional rotation algorithm"
url: "https://devblogs.microsoft.com/oldnewthing/20260603-00/?p=112378"
fetched_at: 2026-06-04T07:01:37.717251+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# Rotation revisited: A shocking discovery about gcc's unidirectional rotation algorithm

Source: https://devblogs.microsoft.com/oldnewthing/20260603-00/?p=112378

Last time, we looked at
the rotation algorithm used by gcc libstdc++ for random-access iterators
, and I concluded by noting that we’re going to make a shocking discovery.
As with all shocking discoveries, this one will
shock
disappoint
you.
The discovery is that the gcc libstdc++ algorithm is the same as
the forward-iterator algorithm
!
Let’s run both algorithms on a problem where the two blocks are A1, A2, A3, B1, B2, B3, B4, B5. I’ll put the old forward iterator algorithm on top and the new gcc libstdc++ algorithm below.
first
mid
last
↓
↓
↓
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
We swap at
first
and
mid
, then advance both pointers. The two algorithms agree until
first
reaches the end of the original A block.
first
mid
last
↓
↓
↓
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
The old algorithm recurses in order to exchange A1, A2, A3 with B4, B4. This happens by exchanging A1 with B4 and A2 with B5.
The new algorithm just keeps swapping
first
with
mid
, which also exchanges A1 with B4 and A2 with B5.
first
mid
last
↓
↓
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
last
mid
The old algorithm now recurses to swap the A3 block with the A1+A2 block. And that’s what the new algorithm does, too.
So it’s the same algorithm, just with a different point of view. It’s another case of
the geeky thrill of discovering that two things are really the same thing, just with different labels
.
Now, the two algorithms are not identical. The new algorithm is symmetric and performs its swaps from right to left if the larger block is on the right. The old algorithm always operates from left to right.
But the similarity is striking.
Next time, we’ll look at how clang performs rotation by decomposing into cycles.
