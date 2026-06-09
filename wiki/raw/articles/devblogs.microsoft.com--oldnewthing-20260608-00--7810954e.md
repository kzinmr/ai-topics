---
title: "Rotation revisited: Shuffling more than three blocks, and other small notes"
url: "https://devblogs.microsoft.com/oldnewthing/20260608-00/?p=112407"
fetched_at: 2026-06-09T07:01:22.228830+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# Rotation revisited: Shuffling more than three blocks, and other small notes

Source: https://devblogs.microsoft.com/oldnewthing/20260608-00/?p=112407

A few small notes on rotation before you get sick of it. (Too late!)
Reducing the number of rotations in the discontiguous swap problem
from three to two also shows how the solution can be generalized to shuffling an arbitrary number of variable-sized blocks: Given
k
blocks, of total size
n
, you can shuffle them arbitrarily in at most
kn
swaps in constant space: Take the block that goes first and rotate it to the front, which takes
n
swaps. Then recurse on what’s left.
You can reduce the number of swaps by comparing the sizes of the block that goes first and the block that goes last and choose to swap the larger block to the corresponding extreme.
I guess you could use this for sorting, but it’s probably enough of a hassle that you’ll just take the penalty of allocating a second block of memory rather than trying to be clever and doing it in-place.
In online discussion of this article, I saw a number of people say, “You can do this with the XOR trick,” but I’m not sure what XOR trick they are referring to. If they are talking about using XOR to swap two integer variables without introducing a third variable, that’s a cute trick I don’t see how it helps with moving variable-sized blocks around. It also doesn’t help with swapping non-integers, since it’s not clear how your XOR two strings or two Widgets.
Another note is that my unit of accounting was the “swap”, but really I should be counting “assignments” because the cycle decomposition algorithm doesn’t use swaps. For the purpose of accounting, I’ve been counting a single assignment as half a swap, though depending on how expensive the move constructor is, a single assignment/construction might only cost a third of a swap.
Finally, a clarification on my description of the solution as “constant space without allocation”: Clearly any algorithm requires
some
space: space for the parameters, return address, any registers used by the code, and any local variables and temporaries. As long as the number and size of these things is bounded by a constant, this is considered a “constant space” algorithm. Note that the size of an element is not known to the generalized algorithm, but once you implement the algorithm for a concrete element type, the size becomes a constant.
My description of this as “without allocation” is a shorthand for “without requiring dynamic memory allocation (because the amount of memory needed is known at compile time).”
I have a soft spot for algorithms that run in constant space (where the constant is reasonably small) because they remove the need to worry about how to recover if there is a memory allocation failure.
