---
title: "Minimal Boolean Formulas"
url: "https://research.swtch.com/boolean"
fetched_at: 2026-05-05T07:01:01.895102+00:00
source: "Russ Cox (research.swtch)"
tags: [blog, raw]
---

# Minimal Boolean Formulas

Source: https://research.swtch.com/boolean

Minimal Boolean Formulas
Russ Cox
May 18, 2011
research.swtch.com/boolean
Posted on Wednesday, May 18, 2011.
28
.
That's the minimum number of AND or OR operators
you need in order to write any Boolean function of five variables.
Alex Healy
and I computed that in April 2010.  Until then,
I believe no one had ever known that little fact.
This post describes how we computed it
and how we almost got scooped by
Knuth's Volume 4A
which considers the problem for AND, OR, and XOR.
A Naive Brute Force Approach
Any Boolean function of two variables
can be written with at most 3 AND or OR operators: the parity function
on two variables X XOR Y is (X AND Y') OR (X' AND Y), where X' denotes
“not X.”  We can shorten the notation by writing AND and OR
like multiplication and addition: X XOR Y = X*Y' + X'*Y.
For three variables, parity is also a hardest function, requiring 9 operators:
X XOR Y XOR Z = (X*Z'+X'*Z+Y')*(X*Z+X'*Z'+Y).
For four variables, parity is still a hardest function, requiring 15 operators:
W XOR X XOR Y XOR Z = (X*Z'+X'*Z+W'*Y+W*Y')*(X*Z+X'*Z'+W*Y+W'*Y').
The sequence so far prompts a few questions.  Is parity always a hardest function?
Does the minimum number of operators alternate between 2
n
−1 and 2
n
+1?
I computed these results in January 2001 after hearing
the problem from Neil Sloane, who suggested it as a variant
of a similar problem first studied by Claude Shannon.
The program I wrote to compute a(4) computes the minimum number of
operators for every Boolean function of n variables
in order to find the largest minimum over all functions.
There are 2
4
= 16 settings of four variables, and each function
can pick its own value for each setting, so there are 2
16
different
functions.  To make matters worse, you build new functions
by taking pairs of old functions and joining them with AND or OR.
2
16
different functions means 2
16
·2
16
= 2
32
pairs of functions.
The program I wrote was a mangling of the Floyd-Warshall
all-pairs shortest paths algorithm.  That algorithm is:
// Floyd-Warshall all pairs shortest path
func compute():
    for each node i
        for each node j
            dist[i][j] = direct distance, or ∞

    for each node k
        for each node i
            for each node j
                d = dist[i][k] + dist[k][j]
                if d < dist[i][j]
                    dist[i][j] = d
    return
The algorithm begins with the distance table dist[i][j] set to
an actual distance if i is connected to j and infinity otherwise.
Then each round updates the table to account for paths
going through the node k: if it's shorter to go from i to k to j,
it saves that shorter distance in the table.  The nodes are
numbered from 0 to n, so the variables i, j, k are simply integers.
Because there are only n nodes, we know we'll be done after
the outer loop finishes.
The program I wrote to find minimum Boolean formula sizes is
an adaptation, substituting formula sizes for distance.
// Algorithm 1
func compute()
    for each function f
        size[f] = ∞

    for each single variable function f = v
        size[f] = 0

    loop
        changed = false
        for each function f
            for each function g
                d = size[f] + 1 + size[g]
                if d < size[f OR g]
                    size[f OR g] = d
                    changed = true
                if d < size[f AND g]
                    size[f AND g] = d
                    changed = true
        if not changed
            return
Algorithm 1 runs the same kind of iterative update loop as the Floyd-Warshall algorithm,
but it isn't as obvious when you can stop, because you don't
know the maximum formula size beforehand.
So it runs until a round doesn't find any new functions to make,
iterating until it finds a fixed point.
The pseudocode above glosses over some details, such as
the fact that the per-function loops can iterate over a
queue of functions known to have finite size, so that each
loop omits the functions that aren't
yet known.  That's only a constant factor improvement,
but it's a useful one.
Another important detail missing above
is the representation of functions.  The most convenient
representation is a binary truth table.
For example,
if we are computing the complexity of two-variable functions,
there are four possible inputs, which we can number as follows.
X
Y
Value
false
false
00
2
= 0
false
true
01
2
= 1
true
false
10
2
= 2
true
true
11
2
= 3
The functions are then the 4-bit numbers giving the value of the
function for each input.  For example, function 13 = 1101
2
is true for all inputs except X=false Y=true.
Three-variable functions correspond to 3-bit inputs generating 8-bit truth tables,
and so on.
This representation has two key advantages.  The first is that
the numbering is dense, so that you can implement a map keyed
by function using a simple array.  The second is that the operations
“f AND g” and “f OR g” can be implemented using
bitwise operators: the truth table for “f AND g” is the bitwise
AND of the truth tables for f and g.
That program worked well enough in 2001 to compute the
minimum number of operators necessary to write any
1-, 2-, 3-, and 4-variable Boolean function.  Each round
takes asymptotically O(2
2
n
·2
2
n
) = O(2
2
n+1
) time, and the number of
rounds needed is O(the final answer).  The answer for n=4
is 15, so the computation required on the order of
15·2
2
5
= 15·2
32
iterations of the innermost loop.
That was plausible on the computer I was using at
the time, but the answer for n=5, likely around 30,
would need 30·2
64
iterations to compute, which
seemed well out of reach.
At the time, it seemed plausible that parity was always
a hardest function and that the minimum size would
continue to alternate between 2
n
−1 and 2
n
+1.
It's a nice pattern.
Exploiting Symmetry
Five years later, though, Alex Healy and I got to talking about this sequence,
and Alex shot down both conjectures using results from the theory
of circuit complexity.  (Theorists!)  Neil Sloane added this note to
the
entry for the sequence
in his Online Encyclopedia of Integer Sequences:
%E A056287 Russ Cox conjectures that X
1
XOR ... XOR X
n
is always a worst f and that a(5) = 33 and a(6) = 63. But (Jan 27 2006) Alex Healy points out that this conjecture is definitely false for large n. So what is a(5)?
Indeed.  What is a(5)?  No one knew, and it wasn't obvious how to find out.
In January 2010, Alex and I started looking into ways to
speed up the computation for a(5).  30·2
64
is too many
iterations but maybe we could find ways to cut that number.
In general, if we can identify a class of functions f whose
members are guaranteed to have the same complexity,
then we can save just one representative of the class as
long as we recreate the entire class in the loop body.
What used to be:
for each function f
    for each function g
        visit f AND g
        visit f OR g
can be rewritten as
for each canonical function f
    for each canonical function g
        for each ff equivalent to f
            for each gg equivalent to g
                visit ff AND gg
                visit ff OR gg
That doesn't look like an improvement: it's doing all
the same work.  But it can open the door to new optimizations
depending on the equivalences chosen.
For example, the functions “f” and “¬f” are guaranteed
to have the same complexity, by
DeMorgan's laws
.
If we keep just one of
those two on the lists that “for each function” iterates over,
we can unroll the inner two loops, producing:
for each canonical function f
    for each canonical function g
        visit f OR g
        visit f AND g
        visit ¬f OR g
        visit ¬f AND g
        visit f OR ¬g
        visit f AND ¬g
        visit ¬f OR ¬g
        visit ¬f AND ¬g
That's still not an improvement, but it's no worse.
Each of the two loops considers half as many functions
but the inner iteration is four times longer.
Now we can notice that half of tests aren't
worth doing: “f AND g” is the negation of
“¬f OR ¬g,” and so on, so only half
of them are necessary.
Let's suppose that when choosing between “f” and “¬f”
we keep the one that is false when presented with all true inputs.
(This has the nice property that
f ^ (int32(f) >> 31)
is the truth table for the canonical form of
f
.)
Then we can tell which combinations above will produce
canonical functions when f and g are already canonical:
for each canonical function f
    for each canonical function g
        visit f OR g
        visit f AND g
        visit ¬f AND g
        visit f AND ¬g
That's a factor of two improvement over the original loop.
Another observation is that permuting
the inputs to a function doesn't change its complexity:
“f(V, W, X, Y, Z)” and “f(Z, Y, X, W, V)” will have the same
minimum size.  For complex functions, each of the
5! = 120 permutations will produce a different truth table.
A factor of 120 reduction in storage is good but again
we have the problem of expanding the class in the
iteration.  This time, there's a different trick for reducing
the work in the innermost iteration.
Since we only need to produce one member of
the equivalence class, it doesn't make sense to
permute the inputs to both f and g.  Instead,
permuting just the inputs to f while fixing g
is guaranteed to hit at least one member
of each class that permuting both f and g would.
So we gain the factor of 120 twice in the loops
and lose it once in the iteration, for a net savings
of 120.
(In some ways, this is the same trick we did with “f” vs “¬f.”)
A final observation is that negating any of the inputs
to the function doesn't change its complexity,
because X and X' have the same complexity.
The same argument we used for permutations applies
here, for another constant factor of 2
5
= 32.
The code stores a single function for each equivalence class
and then recomputes the equivalent functions for f, but not g.
for each canonical function f
    for each function ff equivalent to f
        for each canonical function g
            visit ff OR g
            visit ff AND g
            visit ¬ff AND g
            visit ff AND ¬g
In all, we just got a savings of 2·120·32 = 7680,
cutting the total number of iterations from 30·2
64
= 5×10
20
to 7×10
16
.  If you figure we can do around
10
9
iterations per second, that's still 800 days of CPU time.
The full algorithm at this point is:
// Algorithm 2
func compute():
    for each function f
        size[f] = ∞

    for each single variable function f = v
        size[f] = 0

    loop
        changed = false
        for each canonical function f
            for each function ff equivalent to f
                for each canonical function g
                    d = size[ff] + 1 + size[g]
                    changed |= visit(d, ff OR g)
                    changed |= visit(d, ff AND g)
                    changed |= visit(d, ff AND ¬g)
                    changed |= visit(d, ¬ff AND g)
        if not changed
            return

func visit(d, fg):
    if size[fg] != ∞
        return false

    record fg as canonical

    for each function ffgg equivalent to fg
        size[ffgg] = d
    return true
The helper function “visit” must set the size not only of its argument fg
but also all equivalent functions under permutation or inversion of the inputs,
so that future tests will see that they have been computed.
Methodical Exploration
There's one final improvement we can make.
The approach of looping until things stop changing
considers each function pair multiple times
as their sizes go down.  Instead, we can consider functions
in order of complexity, so that the main loop
builds first all the functions of minimum complexity 1,
then all the functions of minimum complexity 2,
and so on.  If we do that, we'll consider each function pair at most once.
We can stop when all functions are accounted for.
Applying this idea to Algorithm 1 (before canonicalization) yields:
// Algorithm 3
func compute()
    for each function f
        size[f] = ∞

    for each single variable function f = v
        size[f] = 0

    for k = 1 to ∞
        for each function f
            for each function g of size k − size(f) − 1
                if size[f AND g] == ∞
                    size[f AND g] = k
                    nsize++
                if size[f OR g] == ∞
                    size[f OR g] = k
                    nsize++
        if nsize == 2
2
n
return
Applying the idea to Algorithm 2 (after canonicalization) yields:
// Algorithm 4
func compute():
    for each function f
        size[f] = ∞

    for each single variable function f = v
        size[f] = 0

    for k = 1 to ∞
        for each canonical function f
            for each function ff equivalent to f
                for each canonical function g of size k − size(f) − 1
                    visit(k, ff OR g)
                    visit(k, ff AND g)
                    visit(k, ff AND ¬g)
                    visit(k, ¬ff AND g)
        if nvisited == 2
2
n
return

func visit(d, fg):
    if size[fg] != ∞
        return

    record fg as canonical

    for each function ffgg equivalent to fg
        if size[ffgg] != ∞
            size[ffgg] = d
            nvisited += 2  // counts ffgg and ¬ffgg
    return
The original loop in Algorithms 1 and 2 considered each pair f, g in every
iteration of the loop after they were computed.
The new loop in Algorithms 3 and 4 considers each pair f, g only once,
when k = size(f) + size(g) + 1.  This removes the
leading factor of 30 (the number of times we
expected the first loop to run) from our estimation
of the run time.
Now the expected number of iterations is around
2
64
/7680 = 2.4×10
15
.  If we can do 10
9
iterations
per second, that's only 28 days of CPU time,
which I can deliver if you can wait a month.
Our estimate does not include the fact that not all function pairs need
to be considered.  For example, if the maximum size is 30, then the
functions of size 14 need never be paired against the functions of size 16,
because any result would have size 14+1+16 = 31.
So even 2.4×10
15
is an overestimate, but it's in the right ballpark.
(With hindsight I can report that only 1.7×10
14
pairs need to be considered
but also that our estimate of 10
9
iterations
per second was optimistic.  The actual calculation ran for 20 days,
an average of about 10
8
iterations per second.)
Endgame: Directed Search
A month is still a long time to wait, and we can do better.
Near the end (after k is bigger than, say, 22), we are exploring
the fairly large space of function pairs in hopes of finding a
fairly small number of remaining functions.
At that point it makes sense to change from the
bottom-up “bang things together and see what we make”
to the top-down “try to make this one of these specific functions.”
That is, the core of the current search is:
for each canonical function f
    for each function ff equivalent to f
        for each canonical function g of size k − size(f) − 1
            visit(k, ff OR g)
            visit(k, ff AND g)
            visit(k, ff AND ¬g)
            visit(k, ¬ff AND g)
We can change it to:
for each missing function fg
    for each canonical function g
        for all possible f such that one of these holds
                * fg = f OR g
                * fg = f AND g
                * fg = ¬f AND g
                * fg = f AND ¬g
            if size[f] == k − size(g) − 1
                visit(k, fg)
                next fg
By the time we're at the end, exploring all the possible f to make
the missing functions—a directed search—is much less work than
the brute force of exploring all combinations.
As an example, suppose we are looking for f such that fg = f OR g.
The equation is only possible to satisfy if fg OR g == fg.
That is, if g has any extraneous 1 bits, no f will work, so we can move on.
Otherwise, the remaining condition is that
f AND ¬g == fg AND ¬g.  That is, for the bit positions where g is 0, f must match fg.
The other bits of f (the bits where g has 1s)
can take any value.
We can enumerate the possible f values by recursively trying all
possible values for the “don't care” bits.
func find(x, any, xsize):
    if size(x) == xsize
        return x
    while any != 0
        bit = any AND −any  // rightmost 1 bit in any
        any = any AND ¬bit
        if f = find(x OR bit, any, xsize) succeeds
            return f
    return failure
It doesn't matter which 1 bit we choose for the recursion,
but finding the rightmost 1 bit is cheap: it is isolated by the
(admittedly surprising) expression “any AND −any.”
Given
find
, the loop above can try these four cases:
Formula
Condition
Base x
“Any” bits
fg = f OR g
fg OR g == fg
fg AND ¬g
g
fg = f OR ¬g
fg OR ¬g == fg
fg AND g
¬g
¬fg = f OR g
¬fg OR g == fg
¬fg AND ¬g
g
¬fg = f OR ¬g
¬fg OR ¬g == ¬fg
¬fg AND g
¬g
Rewriting the Boolean expressions to use only the four OR forms
means that we only need to write the “adding bits” version of find.
The final algorithm is:
// Algorithm 5
func compute():
    for each function f
        size[f] = ∞

    for each single variable function f = v
        size[f] = 0

    // Generate functions.
    for k = 1 to max_generate
        for each canonical function f
            for each function ff equivalent to f
                for each canonical function g of size k − size(f) − 1
                    visit(k, ff OR g)
                    visit(k, ff AND g)
                    visit(k, ff AND ¬g)
                    visit(k, ¬ff AND g)

    // Search for functions.
    for k = max_generate+1 to ∞
        for each missing function fg
            for each canonical function g
                fsize = k − size(g) − 1
                if fg OR g == fg
                    if f = find(fg AND ¬g, g, fsize) succeeds
                        visit(k, fg)
                        next fg
                if fg OR ¬g == fg
                    if f = find(fg AND g, ¬g, fsize) succeeds
                        visit(k, fg)
                        next fg
                if ¬fg OR g == ¬fg
                    if f = find(¬fg AND ¬g, g, fsize) succeeds
                        visit(k, fg)
                        next fg
                if ¬fg OR ¬g == ¬fg
                    if f = find(¬fg AND g, ¬g, fsize) succeeds
                        visit(k, fg)
                        next fg
        if nvisited == 2
2
n
return

func visit(d, fg):
    if size[fg] != ∞
        return

    record fg as canonical

    for each function ffgg equivalent to fg
        if size[ffgg] != ∞
            size[ffgg] = d
            nvisited += 2  // counts ffgg and ¬ffgg
    return

func find(x, any, xsize):
    if size(x) == xsize
        return x
    while any != 0
        bit = any AND −any  // rightmost 1 bit in any
        any = any AND ¬bit
        if f = find(x OR bit, any, xsize) succeeds
            return f
    return failure
To get a sense of the speedup here, and to check my work,
I ran the program using both algorithms
on a 2.53 GHz Intel Core 2 Duo E7200.
————— # of Functions —————
———— Time ————
Size
Canonical
All
All, Cumulative
Generate
Search
0
1
10
10
1
2
82
92
< 0.1 seconds
3.4 minutes
2
2
640
732
< 0.1 seconds
7.2 minutes
3
7
4420
5152
< 0.1 seconds
12.3 minutes
4
19
25276
29696
< 0.1 seconds
30.1 minutes
5
44
117440
147136
< 0.1 seconds
1.3 hours
6
142
515040
662176
< 0.1 seconds
3.5 hours
7
436
1999608
2661784
0.2 seconds
11.6 hours
8
1209
6598400
9260184
0.6 seconds
1.7 days
9
3307
19577332
28837516
1.7 seconds
4.9 days
10
7741
50822560
79660076
4.6 seconds
[ 10 days ? ]
11
17257
114619264
194279340
10.8 seconds
[ 20 days ? ]
12
31851
221301008
415580348
21.7 seconds
[ 50 days ? ]
13
53901
374704776
790285124
38.5 seconds
[ 80 days ? ]
14
75248
533594528
1323879652
58.7 seconds
[ 100 days ? ]
15
94572
667653642
1991533294
1.5 minutes
[ 120 days ? ]
16
98237
697228760
2688762054
2.1 minutes
[ 120 days ? ]
17
89342
628589440
3317351494
4.1 minutes
[ 90 days ? ]
18
66951
468552896
3785904390
9.1 minutes
[ 50 days ? ]
19
41664
287647616
4073552006
23.4 minutes
[ 30 days ? ]
20
21481
144079832
4217631838
57.0 minutes
[ 10 days ? ]
21
8680
55538224
4273170062
2.4 hours
2.5 days
22
2730
16099568
4289269630
5.2 hours
11.7 hours
23
937
4428800
4293698430
11.2 hours
2.2 hours
24
228
959328
4294657758
22.0 hours
33.2 minutes
25
103
283200
4294940958
1.7 days
4.0 minutes
26
21
22224
4294963182
2.9 days
42 seconds
27
10
3602
4294966784
4.7 days
2.4 seconds
28
3
512
4294967296
[ 7 days ? ]
0.1 seconds
The bracketed times are estimates based on the work involved: I did not
wait that long for the intermediate search steps.
The search algorithm is quite a bit worse than generate until there are
very few functions left to find.
However, it comes in handy just when it is most useful: when the
generate algorithm has slowed to a crawl.
If we run generate through formulas of size 22 and then switch
to search for 23 onward, we can run the whole computation in
just over half a day of CPU time.
The computation of a(5) identified the sizes of all 616,126
canonical Boolean functions of 5 inputs.
In contrast, there are
just over 200 trillion canonical Boolean functions of 6 inputs
.
Determining a(6) is unlikely to happen by brute force computation, no matter what clever tricks we use.
Adding XOR
We've assumed the use of just AND and OR as our
basis for the Boolean formulas.  If we also allow XOR, functions
can be written using many fewer operators.
In particular, a hardest function for the 1-, 2-, 3-, and 4-input
cases—parity—is now trivial.
Knuth examines the complexity of 5-input Boolean functions
using AND, OR, and XOR in detail in
The Art of Computer Programming, Volume 4A
.
Section 7.1.2's Algorithm L is the same as our Algorithm 3 above,
given for computing 4-input functions.
Knuth mentions that to adapt it for 5-input functions one must
treat only canonical functions and gives results for 5-input functions
with XOR allowed.
So another way to check our work is to add XOR to our Algorithm 4
and check that our results match Knuth's.
Because the minimum formula sizes are smaller (at most 12), the
computation of sizes with XOR is much faster than before:
————— # of Functions —————
Size
Canonical
All
All, Cumulative
Time
0
1
10
10
1
3
102
112
< 0.1 seconds
2
5
1140
1252
< 0.1 seconds
3
20
11570
12822
< 0.1 seconds
4
93
109826
122648
< 0.1 seconds
5
366
936440
1059088
0.1 seconds
6
1730
7236880
8295968
0.7 seconds
7
8782
47739088
56035056
4.5 seconds
8
40297
250674320
306709376
24.0 seconds
9
141422
955812256
1262521632
95.5 seconds
10
273277
1945383936
3207905568
200.7 seconds
11
145707
1055912608
4263818176
121.2 seconds
12
4423
31149120
4294967296
65.0 seconds
Knuth does not discuss anything like Algorithm 5,
because the search for specific functions does not apply to
the AND, OR, and XOR basis.  XOR is a non-monotone
function (it can both turn bits on and turn bits off), so
there is no test like our “
if fg OR g == fg
”
and no small set of “don't care” bits to trim the search for f.
The search for an appropriate f in the XOR case would have
to try all f of the right size, which is exactly what Algorithm 4 already does.
Volume 4A also considers the problem of building minimal circuits,
which are like formulas but can use common subexpressions additional times for free,
and the problem of building the shallowest possible circuits.
See Section 7.1.2 for all the details.
Code and Web Site
The web site
boolean-oracle.swtch.com
lets you type in a Boolean expression and gives back the minimal formula for it.
It uses tables generated while running Algorithm 5; those tables and the
programs described in this post are also
available on the site
.
Postscript: Generating All Permutations and Inversions
The algorithms given above depend crucially on the step
“
for each function ff equivalent to f
,”
which generates all the ff obtained by permuting or inverting inputs to f,
but I did not explain how to do that.
We already saw that we can manipulate the binary truth table representation
directly to turn
f
into
¬f
and to compute
combinations of functions.
We can also manipulate the binary representation directly to
invert a specific input or swap a pair of adjacent inputs.
Using those operations we can cycle through all the equivalent functions.
To invert a specific input,
let's consider the structure of the truth table.
The index of a bit in the truth table encodes the inputs for that entry.
For example, the low bit of the index gives the value of the first input.
So the even-numbered bits—at indices 0, 2, 4, 6, ...—correspond to
the first input being false, while the odd-numbered bits—at indices 1, 3, 5, 7, ...—correspond
to the first input being true.
Changing just that bit in the index corresponds to changing the
single variable, so indices 0, 1 differ only in the value of the first input,
as do 2, 3, and 4, 5, and 6, 7, and so on.
Given the truth table for f(V, W, X, Y, Z) we can compute
the truth table for f(¬V, W, X, Y, Z) by swapping adjacent bit pairs
in the original truth table.
Even better, we can do all the swaps in parallel using a bitwise
operation.
To invert a different input, we swap larger runs of bits.
Function
Truth Table (
f
= f(V, W, X, Y, Z)
)
f(¬V, W, X, Y, Z)
(f&0x55555555)<< 1 | (f>> 1)&0x55555555
f(V, ¬W, X, Y, Z)
(f&0x33333333)<< 2 | (f>> 2)&0x33333333
f(V, W, ¬X, Y, Z)
(f&0x0f0f0f0f)<< 4 | (f>> 4)&0x0f0f0f0f
f(V, W, X, ¬Y, Z)
(f&0x00ff00ff)<< 8 | (f>> 8)&0x00ff00ff
f(V, W, X, Y, ¬Z)
(f&0x0000ffff)<<16 | (f>>16)&0x0000ffff
Being able to invert a specific input lets us consider all possible
inversions by building them up one at a time.
The
Gray code
lets us
enumerate all possible 5-bit input codes while changing only 1 bit at
a time as we move from one input to the next:
0, 1, 3, 2, 6, 7, 5, 4,
12, 13, 15, 14, 10, 11, 9, 8,
24, 25, 27, 26, 30, 31, 29, 28,
20, 21, 23, 22, 18, 19, 17, 16
This minimizes
the number of inversions we need: to consider all 32 cases, we only
need 31 inversion operations.
In contrast, visiting the 5-bit input codes in the usual binary order 0, 1, 2, 3, 4, ...
would often need to change multiple bits, like when changing from 3 to 4.
To swap a pair of adjacent inputs, we can again take advantage of the truth table.
For a pair of inputs, there are four cases: 00, 01, 10, and 11.  We can leave the
00 and 11 cases alone, because they are invariant under swapping,
and concentrate on swapping the 01 and 10 bits.
The first two inputs change most often in the truth table: each run of 4 bits
corresponds to those four cases.
In each run, we want to leave the first and fourth alone and swap the second and third.
For later inputs, the four cases consist of sections of bits instead of single bits.
Function
Truth Table (
f
= f(V, W, X, Y, Z)
)
f(
W, V
, X, Y, Z)
f&0x99999999 | (f&0x22222222)<<1 | (f>>1)&0x22222222
f(V,
X, W
, Y, Z)
f&0xc3c3c3c3 | (f&0x0c0c0c0c)<<1 | (f>>1)&0x0c0c0c0c
f(V, W,
Y, X
, Z)
f&0xf00ff00f | (f&0x00f000f0)<<1 | (f>>1)&0x00f000f0
f(V, W, X,
Z, Y
)
f&0xff0000ff | (f&0x0000ff00)<<8 | (f>>8)&0x0000ff00
Being able to swap a pair of adjacent inputs lets us consider all
possible permutations by building them up one at a time.
Again it is convenient to have a way to visit all permutations by
applying only one swap at a time.
Here Volume 4A comes to the rescue.
Section 7.2.1.2 is titled “Generating All Permutations,” and Knuth delivers
many algorithms to do just that.
The most convenient for our purposes is Algorithm P, which
generates a sequence that considers all permutations exactly once
with only a single swap of adjacent inputs between steps.
Knuth calls it Algorithm P because it corresponds to the
“Plain changes” algorithm used by
bell ringers in 17th century England
to ring a set of bells in all possible permutations.
The algorithm is described in a manuscript written around 1653!
We can examine all possible permutations and inversions by
nesting a loop over all permutations inside a loop over all inversions,
and in fact that's what my program does.
Knuth does one better, though: his Exercise 7.2.1.2-20
suggests that it is possible to build up all the possibilities
using only adjacent swaps and inversion of the first input.
Negating arbitrary inputs is not hard, though, and still does
minimal work, so the code sticks with Gray codes and Plain changes.
