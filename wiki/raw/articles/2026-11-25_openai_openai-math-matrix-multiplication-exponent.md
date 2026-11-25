---
title: "OpenAI Math: The Matrix Multiplication Exponent Is Nine Fourths"
created: 2026-11-25
updated: 2026-11-25
type: article
source: "https://github.com/openai/math/tree/main/preprints/The-matrix-multiplication-exponent-is-nine-fourths-November-24-2026"
status: complete
sources:
  - "https://github.com/openai/math/tree/main/preprints/The-matrix-multiplication-exponent-is-nine-fourths-November-24-2026"
  - "https://news.ycombinator.com/item?id=50637220"
  - "https://github.com/openai/math/blob/main/preprints/The-matrix-multiplication-exponent-is-nine-fourths-November-24-2026/paper.pdf"
sha256: 439ee851b4131c5c0af5c4003e11cce95838556027bbb98b78888615e2c35ddb
---

# OpenAI Math: The Matrix Multiplication Exponent Is Nine Fourths

> PDF/repo pages are JS-rendered (fetch returned only chrome). Body below is the HN comment tree; paper title as posted: "The matrix multiplication exponent is nine fourths" (Nov 24 2026). HN title "Matrix Multiplication is Theta(n^2.25)" was contested in-thread as imprecise.

Source: https://github.com/openai/math/tree/main/preprints/The-matrix-multiplication-exponent-is-nine-fourths-November-24-2026

## Article

(not fetched)

## HN discussion highlights (item 50637220)

# HN matrix-mult — Matrix Multiplication is Θ(n^2.25) [pdf] (705 pts, item 50637220)
# url: https://github.com/openai/math/blob/main/preprints/The-matrix-multiplication-exponent-is-nine-fourths-November-24-2026/paper.pdf

[mmoskal] ...and 8 other results: https://github.com/openai/math/blob/3344da59991ed94f9ba71121... The matmul result is that omega is exactly 2.25, not just lower bound.
[vlovich123]     It’s not immediately obvious to me that argument is sound since we’re talking about the exact bound. I believe the lower bound for certain rectangular sizes is less than 2.25 while 2.25 remains an upper bound for rectangular matrices.
[im3w1l]     Obviously you can do that, but given how wasteful it is when the dimensions are very different, it seems like it should be possible to do better.
[orlp] Title is incorrect (it says O(n^2.25) at the time of writing), we already knew that, and that's not what this result describes. It should be Θ(n^2.25), or the original title "The matrix multiplication exponent is nine fourths".
[krackers]   >we already knew that Annoyingly the wikipedia page doesn't even mention the previous improved upper bound from their October results.
[pxx]   This should be fixed. The title of the submission is neither the title of the page it links to nor the correct statement.
[tczMUFlmoNk]   While "Θ(n^2.25)" is better, imho it's still misleading. Matrix multiplication is a problem that can be solved by algorithms whose running times (under various conditions) are functions . "Being Θ(n^2.25)" is a property of a function, not an algorithm, and not a problem. There are matrix multiplication algorithms commonly used whose worst-case running times are most certainly not Θ(n^2.25) (namely, all of them known before last month). One could precisely say that "an optimal algorithm for matrix multiplication has worst-case running time Θ(n^2.25)" or "optimal matrix multiplication takes time
[flowerthoughts]     "Problem" is just a shortcut for "the optimal algorithm(s)." It's well established? It implicitly requires that the algorithm(s) in question have been proven to be actually optimal for the problem.
[hansvm]     Is literally anyone confused by the notation? Constrained to this problem: There exists an algorithm achieving Θ(n^2.25) runtime. There does not exist an algorithm achieving o(n^2.25) runtime. If we want to be pedantic about function classes vs other extensions of Big-O notation then we can talk about the runtime of some specific class of algorithms associated with this problem and manufacture the function everyone is implicitly referring to. It's a perfectly fine shorthand phrasing, especially given that the domains are different for that overlap in vocabulary. The best/average/worst case stu
[henrymerrilees]     How's this for pedantry... problem vs algorithm vs function aside, the pesky epsilon in the upper bound means it isn't big-theta either!
[enedil]     I think you are unnecessarily pedantic. E.g. for decision problems it is established, that a problem is in O(f(n)) if there exists an algorithm running in O(f(n)) time and the same goes for small o and big theta.
[hinkley]   That bound is determined empirically as I recall. Every few years someone shaves a hundredth off of the best algorithm known at the time.
[jcelerier]   the paper is much bigger than this. The previous things were upper bounds with the assumption (hope) that the actual lower bound was 2 and that quadratic matmul was possible. This is the exact lower bound (and, sadly > 2).
[tliltocatl]     Given the constants for the known algorithms this is of little practical difference. And even if we find a practical n^2.25 algorithm one day, you would still need pretty large matrices for it to make any difference (i. e. billion rows matrices are only ~200x slower with n^2.25 than with quadratic).
[williamdclt]     maybe, hopefully, there's a useful subset of matrices with specific properties that can be matmul'd in quadratic time?
[orlp]   No it doesn't, it proves a lower bound of 2.25. The upper bound of 2.25 was found earlier https://github.com/openai/math/blob/main/preprints/Matrix-Mu... .
