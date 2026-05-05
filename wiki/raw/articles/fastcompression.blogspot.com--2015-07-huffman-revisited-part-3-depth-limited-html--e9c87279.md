---
title: "Huffman revisited - Part 3 - Depth limited tree"
url: "http://fastcompression.blogspot.com/2015/07/huffman-revisited-part-3-depth-limited.html"
fetched_at: 2026-05-05T07:01:00.323092+00:00
source: "Yann Collet (LZ4/Zstd)"
tags: [blog, raw]
---

# Huffman revisited - Part 3 - Depth limited tree

Source: http://fastcompression.blogspot.com/2015/07/huffman-revisited-part-3-depth-limited.html

A non-trivial issue that most real-world Huffman implementations must deal with is tree depth limitation.
Huffman construction doesn't limit the depth. If it would, it would no longer be "optimal". Granted, the maximum depth of an Huffman tree is bounded by the
Fibonacci serie
, but that leave ample room for larger depth than wanted.
Why limit Huffman tree depth ? Fast huffman decoders use lookup tables. It's possible to use multiple table levels to mitigate the memory cost, but a very fast decoder such as Huff0 goes for a single table, both for simplicity and speed. In which case the table size is a direct product of the tree depth (
tablesize = 1 << treeDepth
).
For the benefit of speed and memory management, a limit had to be selected : it's 8 KB for the decoding table, which nicely fits into Intel's L1 cache, and leaves some room to combine it with other tables if need be. Since
latest decoding table uses 2 bytes per cell
, it translates into 4K cells, hence a maximum tree depth of 12 bits.
12 bits for compressing literals is generally too little, at least according to optimal Huffman construction. Creating a depth-limited tree is therefore a practical issue to solve. The question is : how to achieve this objective with minimum impact on compression ratio, and how to do it
fast
?
Depth-limited huffman trees have been studied since the 1960's, so there is ample literature available. What's more surprising is how complex the proposed solutions are, and how many decades were
necessary to converge towards an optimal solution.
(Note
: in below paragraph,
n
is the alphabet size, and
D
is the maximum tree Depth.)
It started with Karp, in 1961 (
Minimum-redundancy coding for the discrete noiseless channel
), proposing a solution in exponential time. Then Gilbert, in 1971 (
Codes based on inaccurate source probabilities
), still in exponential time. Hu and Tan, in 1972 (
Path length of binary search trees
), with a solution in O(n.D.2^D). Finally, a solution in polynomial time was proposed by Garey in 1974 (
Optimal binary search trees with restricted maximal depth
), but still O(n^2.D) time and using O(n^2.D) space. In 1987, Larmore proposed an improved solution using O(n^3/2.D.log1/2.n) time and space (
Height restricted optimal binary trees
). The breakthrough happened in 1990 (
A fast algorithm for optimal length-limited Huffman codes
), when Larmore and Hirschberg propose the
Package_Merge
algoritm, a completely different kind of solution using
only
O(n.D) time and O(n) space. It became a classic, and was refined a few times over the next decades, with the notable contribution of Mordecai Golin in 2008 (
A Dynamic Programming Approach To Length-Limited Huffman Coding
).
Most of these papers are plain difficult to read, and it's usually harder than necessary to develop a working solution by just reading them (at least, I couldn't. Honorable mention for Mordecai Golin, which proposes a graph-traversal formulation relatively straightforward. Alas, it was still too much CPU workload for my taste).
In practice, most fast Huffman implementations don't bother with them. Sure, when
optimal compression
is required, the PackageMerge algorithm is preferred, but in most circumstances, being optimal is not really the point. After all, Huffman is already a trade-off between optimal and speed. By following this logic, we don't want to sacrifice everything for an optimal solution, we just need a good enough one, fast and light.
That's why you'll find some cheap heuristics in many huffman codes. A simple one : start with a classic Huffman tree, flatten all leaves beyond maximum depth, then flatten enough higher leaves to maxBits to get back the total length to one. It's fast, it's certainly not optimal, but in practice, the difference is small and barely noticeable. Only when the tree depth is very constrained does it make a visible difference (you can read some relevant
great comments from Charles Bloom on its blog
).
Nonetheless, for huff0, I was willing to find a solution a bit better than cheap heuristic, closer to optimal. 12 bits is not exactly "very constrained", so the pressure is not high, but it's still constrained enough that the depth-limited algorithm is going to be necessary in most circumstances. So better have a good one.
I started by making some simple observations : after completing an huffman tree, all symbols are sorted in decreasing count order. That means that the number of bits required to represent each symbol must follow a strict increasing order. That means the only thing I need to track is the border decision (from 5 to 6 bits, from 6 to 7 bits, etc.).
So now, the algorithm will concentrate on moving the arrows.
The first part is the same as the cheap heuristic : flatten everything that needs more than
maxBits
. This will create a "debt" : a symbol requiring
maxBits+1
bits creates a debt of 1/2=0.5 when pushed to
maxBits
. A symbol requiring
maxBits+2
creates a debt of 3/4=0.75, and so on. What may not be totally obvious is that the sum of these fractional debts is necessarily an integer number. This is a consequence of starting from a solved huffman tree, and can be proven by simple recurrence : if the huffman tree natural length is
maxBits+1
, then the number of elements at
maxBits+1
is necessarily even, otherwise the sum of probabilities can't be equal to one. The debt's sum is therefore necessarily a multiple of 2 * 0.5 = 1, hence an integer number. Rince and repeat for
maxBits+2
and further depth.
So now we have a
debt
to repay. Each time you demote a symbol from
maxBits-1
to
maxBits
, you repay 1 debt. Since the symbols are already sorted in decreasing frequency, it's easy to just grab the smallest
maxBits-1
symbols, and demote them to
maxBits,
up to repaying the debt. This is in essence what the cheap heuristic does.
But one must note that demoting a symbol from
maxBits-2
to
maxBits-1
repay not 1 but 2 debts. Demoting from
maxbits-3
to
maxBits-2
repay 4 debts. And so on. So now the question becomes : is it preferable to demote a single
maxBits-2
symbol or two
maxBits-1
symbols ?
The answer to this question is trivial since we deal with integer number of bits : just compare the sum of occurrences of the two
maxBits-1
symbols with the occurrence of the single
maxBits-2
one. Whichever is smallest costs less bits to demote. Proceed.
This approach can be scaled. Need to repay 16 debts ? A single symbol at
maxBits-5
might be enough, or 2 at
maxBits-4
. By recurrence, each
maxBits-4
symbol might be better replaced by two
maxBits-3
ones, and so on. The best solution will show up by a simple recurrence algorithm.
Sometimes, it might be better to overshoot : if you have to repay a debt of 7, which formula is better ? 4+2+1, or 8-1 ? (the
-1
can be achieved by promoting the best
maxBits
symbol to
maxBits-1
). In theory, you would have to compare both and select the better one. Doing so leads to an
optimal
algorithm. In practice though, the positive debt repay (4+2+1) is most likely the better one, since distribution must be severely twisted for the overshoot solution to win.
The algorithm becomes a bit more complex when some bits ranks are missing. For example, one needs to repay a debt of 2, but there is no symbol left at
maxBits-2
. In such case, one can still uses
maxBits-1
symbols, but maybe there is no more of these symbols left either. In which case, the only remaining solution is to overshoot (
maxBits-3
) and promote enough elements to get the debt back to zero.
On average, implementation of this algorithm is pretty fast. Its CPU cost is unnoticeable, compared to the decoding cost itself, and the final compression ratio is barely affected (<0.1%) compared to unconstrained tree depth. So that's mission accomplished.
The fast variant of the depth limit algorithm is available in open source and can be grabbed at
github
, under the function name
HUF_setMaxHeight()
.
