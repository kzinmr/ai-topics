---
title: "Estimating branch probabilities"
url: "https://maskray.me/blog/estimating-branch-probabilities"
fetched_at: 2026-08-24T10:32:20.506195+00:00
source: "Fangrui Song (MaskRay)"
tags: [blog, raw]
---

# Estimating branch probabilities

Source: https://maskray.me/blog/estimating-branch-probabilities

LLVM's
BranchProbabilityInfo
assigns every
multi-successor terminator a probability distribution over its
successors. This post describes the estimation used when no profile is
available and reimplements it as a standalone program.
The cascade
BranchProbabilityInfo::calculate
tries each source of
information in turn and takes the first that succeeds:
1
2
3
4
5
6
7
8
9
10
11
12
13
if
(BB->
getTerminator
()->
getNumSuccessors
() <
2
)
continue
;
if
(
calcMetadataWeights
(BB))
continue
;
if
(
calcEstimatedHeuristics
(BB))
continue
;
if
(
calcPointerHeuristics
(BB))
continue
;
if
(
calcZeroHeuristics
(BB, TLI))
continue
;
if
(
calcFloatingPointHeuristics
(BB))
continue
;
calcMetadataWeights
translates
!prof
branch
weights, so with a PGO profile the distribution comes straight from
metadata. Every later step exists for functions that have none.
The last three heuristics each inspect one condition — a pointer
comparison, a test against a constant, ordered versus unordered floats —
and decide one branch in isolation. They and the loop branch heuristic
behind the
LBH_
constants below come from Ball and Larus's
Branch Prediction for Free
(PLDI 1993), though nothing in the
tree cites it. Wu and Larus combined such heuristics into probabilities
with Dempster–Shafer evidence; LLVM takes the first that succeeds.
calcEstimatedHeuristics
is the odd one out, and the
subject of this post. No paper stands behind it: it arrived in 2020,
unifying what had been separate unreachable, cold-call, loop, and invoke
heuristics. It is a whole-function analysis because branch probability
is not a local property: given
br i1 %c, label %a, label %b
, nothing at the terminator
distinguishes the two edges — what distinguishes them is what
%a
and
%b
lead to. So it classifies blocks
first, then reads a branch's probabilities off the classifications of
its successors. The classification is a pure function of the CFG and its
loops: blocks known to be bad — unreachable,
noreturn
, cold
— pull probability away from the branches that lead to them, and loops
are treated as units so that staying in a loop is far likelier than
leaving it. This is the only step that needs the loop structure, and the
only one expressible over a bare CFG; the others need the instructions.
The program below implements it, omitting the other heuristics and
computeUnlikelySuccessors
, a refinement that analyses
induction variables through PHI nodes.
That
BlockFrequencyInfo
consumes
BranchProbabilityInfo
might suggest a circularity, but the
two run in opposite directions: BFI propagates forward from the entry
and needs probabilities to do it, while the estimated heuristic
propagates backward from syntactically bad blocks and needs only the
dominator trees and the loop forest. Nothing it reads comes from a
probability.
Estimating block weights
In outline:
Seed unreachable,
noreturn
, unwinding, and cold blocks
with fixed weights.
Propagate each seed up the dominator tree, to every dominator the
seeded block post-dominates.
Weight a loop by the maximum over its exit edges, floored at
LOWEST_NON_ZERO
.
Run two worklists to a fixpoint: a block whose successor edges are
all known takes their maximum, which propagates like a seed.
At each branch, divide loop-exiting edges by an assumed trip count,
default unknown weights, and normalize.
Weights come from a small fixed scale. Despite the name, a
BlockExecWeight
is not an execution estimate but one of
four ordered labels; the magnitudes exist only so a branch can compare
two successors and normalize.
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
enum class
BlockExecWeight
: std::
uint32_t
{
ZERO =
0x0
,
LOWEST_NON_ZERO =
0x1
,
UNREACHABLE = ZERO,
NORETURN = LOWEST_NON_ZERO,
UNWIND = LOWEST_NON_ZERO,
COLD =
0xffff
,
DEFAULT =
0xfffff
};
Blocks not seeded start unweighted, and are treated as
DEFAULT
only when a branch needs a number.
DEFAULT
is a floor, not a seed: it never propagates.
How far a seed flows backwards is the interesting part. It is not
simply pushed to all predecessors:
propagateEstimatedBlockWeight
walks
up the dominator
tree
from the seeded block and assigns the weight to each dominator
that the seeded block
post-dominates
. The
post-dominance condition is what makes this meaningful: a branch that
merely
can
reach a
noreturn
block may take the
other edge, whereas one that cannot avoid it is genuinely unlikely. The
weight therefore spreads through the region where the bad outcome is
unavoidable, and stops where a bypass exists — or at a loop boundary,
since a loop is weighted as a unit.
The rest is three mutually recursive definitions over edges:
1
2
3
4
5
weight(u→v)    = weight(L)   if u→v enters loop L (L does not contain u)
weight(v)   otherwise
weight(loop L) = max weight over L's exit edges (u inside, v outside),
raised to LOWEST_NON_ZERO if ZERO
weight(b)      = its seed, else the max weight over b's successor edges
An edge entering a loop takes the loop's weight because its target is
a header, whose own weight says nothing about how often the loop runs. A
loop is as hot as the hottest thing it can fall out to, and entered at
least once even if it never exits — hence the maximum and the floor. A
block's maximum is all-or-nothing — if any successor edge is still
unknown, the block stays unknown — so a block counts as unlikely only
when
every
path out is unlikely; one ordinary escape keeps it
ordinary. Each maximum, once known, propagates up the dominator tree
like a seed; the recursion settles in a fixpoint over two worklists, the
code below enqueuing exactly the blocks and loops each new weight can
affect.
From weights to
probabilities
A branch takes the weight of each successor edge, applies two
adjustments, and normalizes.
The first adjustment: an edge
exiting
a loop is scaled down
by an assumed trip count.
1
2
3
4
static
const
uint32_t
LBH_TAKEN_WEIGHT =
124
;
static
const
uint32_t
LBH_NONTAKEN_WEIGHT =
4
;
...
uint32_t
TC = LBH_TAKEN_WEIGHT / LBH_NONTAKEN_WEIGHT;
TC
is 31, so a loop is assumed to run 31 iterations and
leaving it is weighted at 1/31 of staying. This is the single number
behind almost every "the loop body is hot" conclusion LLVM draws without
a profile.
The second: an edge whose weight is still unknown falls back to
DEFAULT
, which is what makes
DEFAULT
a floor
rather than a seed. If no successor has an estimate at all, or every
weight is
ZERO
, the heuristic declines: it returns false,
the branch is left alone, and the next step of the cascade gets its
turn.
The stored value is a
BranchProbability
, a rational
whose denominator is a compile-time constant, so only the numerator is
kept:
1
2
3
4
5
6
7
class
BranchProbability
{
uint32_t
N;
static
constexpr
uint32_t
D =
1u
<<
31
;
static
constexpr
uint32_t
UnknownN = UINT32_MAX;
A probability is therefore one 32-bit word, and comparing or scaling
two of them is integer arithmetic.
D
is 2^31 rather than
2^32 so that the numerator of 1.0 still fits in a
uint32_t
,
which also leaves
UINT32_MAX
free as the "unknown"
sentinel. Constructing from any other denominator rescales with
rounding, so
BranchProbability(1, 3)
stores 715827883 — and
a three-way even split shows up in the dumps as that number three times,
not as 0.333.
Why irreducible loops
have to be kept
The heuristic asks only three things about the loop structure: is
this block in a loop, is this edge entering or exiting that loop, and
does one loop contain another. It never asks whether a loop is
reducible.
So it wants the full
loop-nesting
forest
— every maximal strongly connected region, nested by
containment — not just its single-entry loops. A natural loop is one
whose header dominates it, which is exactly the reducible case.
Restricting to those loses not just the irreducible loops but the
nesting
around
them, because the reduction has to attribute
their blocks somewhere.
An analysis limited to natural loops therefore needs a fallback for
irreducible regions, and the obvious one — maximal strongly connected
components — is flat. A flat SCC merges an inner loop into its outer
one, and the heuristic then scales the wrong set of exit edges.
A note on names, because LLVM's are confusing here.
LoopInfo
had already come to mean
natural
loops,
so when the general notion was added it could not also be called a loop
and was named
CycleInfo
instead. The new word marks the
different definition, not a different object: a
CycleInfo
cycle is a loop in the sense of the previous post. It is also the weaker
name — a cycle is a closed path with no distinguished entry, whereas the
DFS discovers a header and a nesting — so the program below says loop
throughout, keeping cycle for the graph-theoretic sense. Both are now
built by the same single-pass DFS, and
LoopInfo
then
reduces the irreducible loops to natural-loop subsets — which is why the
dominator tree it takes is, in the words of the source, "needed only for
an irreducible CFG".
Containment is the query that has to be fast, and the flat block
layout from the previous post makes it an interval test rather than a
set probe.
The program
Three structures feed the analysis; two are the programs already
published, so they are not reprinted. The loop-nesting forest comes from
the single-pass DFS of
irreducible
loops
— visiting successors last-in-first-out, as LLVM's iterative
DFS does, since for irreducible loops the forest depends on that order —
and the dominator tree from the semi-NCA routine of
natural loops
. The post-dominator tree is
new and shown below.
Input format, extending the previous posts' by one optional
section:
1
2
3
n m
u v      (m directed edges u->v; node 0 is the entry)
b K      (0+ lines: block b has kind K in {U unreachable, R noreturn, C cold})
After parsing, predecessor lists are reversed: LLVM's
predecessors()
walks the use list, which is the reverse of
construction order, and a later section shows this order is
observable.
The weight scale, the seeds, and the two sparse weight maps:
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
const
uint32_t
W_UNREACHABLE =
0x0
;
const
uint32_t
W_LOWEST =
0x1
;
const
uint32_t
W_COLD =
0xffff
;
const
uint32_t
W_DEFAULT =
0xfffff
;
const
uint32_t
TC =
124
/
4
;
static
vector<
char
> kind;
static
vector<
long
long
> estBlock;
static
vector<
long
long
> estLoop;
static
long
long
seedWeight
(
int
b)
{
switch
(kind[b]) {
case
'U'
:
return
W_UNREACHABLE;
case
'R'
:
return
W_LOWEST;
case
'C'
:
return
W_COLD;
default
:
return
-1
;
}
}
Edge classification reduces to containment of the endpoints'
innermost loops — here a parent-chain walk rather than the interval
test:
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
static
vector<
int
> loop;
static
vector<
int
> parentLoop;
static
vector<vector<
int
>> entries;
static
vector<vector<
int
>> exits;
static
bool
loopHasLoop
(
int
outer,
int
inner)
{
for
(
int
x = inner; x >=
0
; x = parentLoop[x])
if
(x == outer)
return
true
;
return
false
;
}
static
bool
loopHasBlock
(
int
L,
int
b)
{
for
(
int
x = loop[b]; x >=
0
; x = parentLoop[x])
if
(x == L)
return
true
;
return
false
;
}
static
bool
entering
(
int
u,
int
v)
{
if
(loop[v] <
0
)
return
false
;
if
(loop[u] <
0
)
return
true
;
return
!
loopHasLoop
(loop[v], loop[u]);
}
static
bool
exiting
(
int
u,
int
v)
{
return
entering
(v, u); }
static
long
long
edgeWeight
(
int
u,
int
v)
{
return
entering
(u, v) ? estLoop[loop[v]] : estBlock[v];
}
static
long
long
maxEdge
(
int
u,
const
vector<
int
> &dsts)
{
long
long
mx =
-1
;
for
(
int
v : dsts) {
long
long
w =
edgeWeight
(u, v);
if
(w <
0
)
return
-1
;
mx =
max
(mx, w);
}
return
mx;
}
computeIdom
is the semi-NCA routine made generic over
(succ, pred, root)
, with the reverse post-order falling out
of its DFS; post-dominators are its output on the reverse CFG, rooted at
a virtual exit:
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
static
vector<
int
> idom, rpo, ipdom;
static
int
VEXIT;
static
void
computePDT
()
{
VEXIT = n;
vector<
char
>
seen
(n,
0
)
;
vector<
int
> roots;
auto
markReaching = [&](
int
s) {
for
(vector<
int
> stk{s}; !stk.
empty
();) {
int
b = stk.
back
();
stk.
pop_back
();
if
(seen[b])
continue
;
seen[b] =
1
;
for
(
int
p : pred[b])
stk.
push_back
(p);
}
};
for
(
int
b =
0
; b < n; b++)
if
(succ[b].
empty
())
roots.
push_back
(b),
markReaching
(b);
for
(
int
b =
0
; b < n; b++) {
if
(seen[b])
continue
;
vector<
char
>
tmp
(n,
0
)
;
vector<
int
> order;
for
(vector<
int
> stk{b}; !stk.
empty
();) {
int
x = stk.
back
();
stk.
pop_back
();
if
(seen[x] || tmp[x])
continue
;
tmp[x] =
1
;
order.
push_back
(x);
vector<
int
> ss = succ[x];
sort
(ss.
begin
(), ss.
end
());
for
(
int
s : ss)
stk.
push_back
(s);
}
roots.
push_back
(order.
back
());
markReaching
(order.
back
());
}
vector<vector<
int
>>
rsucc
(n +
1
),
rpred
(n +
1
);
for
(
int
b =
0
; b < n; b++)
rsucc[b] = pred[b], rpred[b] = succ[b];
for
(
int
r : roots)
rsucc[VEXIT].
push_back
(r), rpred[r].
push_back
(VEXIT);
ipdom =
computeIdom
(n +
1
, rsucc, rpred, VEXIT);
}
static
bool
postDominates
(
int
a,
int
b)
{
for
(
int
x = b; x !=
-1
&& x != VEXIT; x = ipdom[x])
if
(x == a)
return
true
;
return
false
;
}
The propagation and the worklist fixpoint:
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
static
vector<
int
> blockWL, loopWL;
static
bool
updateBlockWeight
(
int
b,
long
long
w)
{
if
(estBlock[b] >=
0
)
return
false
;
estBlock[b] = w;
for
(
int
p : pred[b]) {
if
(
exiting
(p, b)) {
if
(estLoop[loop[p]] <
0
)
loopWL.
push_back
(loop[p]);
}
else
if
(estBlock[p] <
0
)
blockWL.
push_back
(p);
}
return
true
;
}
static
void
propagate
(
int
bb,
long
long
w)
{
if
(idom[bb] ==
-1
)
return
;
for
(
int
d = bb;;) {
if
(!
postDominates
(bb, d))
break
;
if
(!
entering
(d, bb) && !
exiting
(d, bb)) {
if
(!
updateBlockWeight
(d, w))
break
;
}
else
if
(
exiting
(d, bb) && loop[d] >=
0
)
loopWL.
push_back
(loop[d]);
if
(d ==
0
|| idom[d] ==
-1
)
break
;
d = idom[d];
}
}
static
void
estimateWeights
()
{
estBlock.
assign
(n,
-1
);
estLoop.
assign
(nLoop,
-1
);
for
(
int
b : rpo)
if
(
long
long
w =
seedWeight
(b); w >=
0
)
propagate
(b, w);
while
(!blockWL.
empty
() || !loopWL.
empty
()) {
while
(!loopWL.
empty
()) {
int
L = loopWL.
back
();
loopWL.
pop_back
();
if
(estLoop[L] >=
0
)
continue
;
long
long
lw =
maxEdge
(entries[L].
empty
() ?
0
: entries[L][
0
], exits[L]);
if
(lw <
0
)
continue
;
if
(lw <= (
long
long
)W_UNREACHABLE)
lw = W_LOWEST;
estLoop[L] = lw;
for
(
int
e : entries[L])
for
(
int
p : pred[e])
if
(!
loopHasBlock
(L, p) && estBlock[p] <
0
)
blockWL.
push_back
(p);
}
while
(!blockWL.
empty
()) {
int
b = blockWL.
back
();
blockWL.
pop_back
();
if
(estBlock[b] >=
0
)
continue
;
if
(
long
long
mw =
maxEdge
(b, succ[b]); mw >=
0
)
propagate
(b, mw);
}
}
}
Per-branch normalization:
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
static
void
printProbabilities
()
{
for
(
int
b =
0
; b < n; b++) {
if
((
int
)succ[b].
size
() <
2
)
continue
;
vector<
uint32_t
>
val
(succ[b].size())
;
bool
found =
false
;
for
(
size_t
i =
0
; i < succ[b].
size
(); i++) {
int
s = succ[b][i];
long
long
w =
edgeWeight
(b, s);
if
(
exiting
(b, s) && w != (
long
long
)W_UNREACHABLE) {
uint32_t
base = (w <
0
) ? W_DEFAULT : (
uint32_t
)w;
w =
max
(W_LOWEST, base / TC);
}
if
(w >=
0
)
found =
true
;
val[i] = (w <
0
) ? W_DEFAULT : (
uint32_t
)w;
}
uint64_t
total =
0
;
for
(
uint32_t
v : val)
total += v;
bool
uniform = idom[b] ==
-1
|| !found || total ==
0
;
printf
(
"  block %d ->"
, b);
if
(uniform)
printf
(
"  [no estimate: uniform]"
);
printf
(
"\n"
);
for
(
size_t
i =
0
; i < succ[b].
size
(); i++) {
int
s = succ[b][i];
const
char
*tag =
entering
(b, s) ?
" enter"
:
exiting
(b, s) ?
" exit "
:
"      "
;
double
p = uniform ?
100.0
/ succ[b].
size
() :
100.0
* val[i] / (
double
)total;
printf
(
"      -> %d %s  weight=%-8u  p=%6.2f%%\n"
, s, tag, val[i], p);
}
}
}
Examples
The minimal loop first. No block is seeded, so every weight is
DEFAULT
and the only signal is the loop itself:
1→3
leaves it, so its weight is divided by 31, and the
branch at the header splits 31:1.
1
2
3
4
5
6
7
8
9
10
11
12
13
14
% ./bpi
5 5
0 1
1 2
1 3
2 1
3 4
loops, indented by nesting:
loop 0 [reducible]  blocks { 1 2 }  innermost { 1 2 }  entries { 1 }  exits { 3 }  loopWeight=-1
estimated block weights (unknown blocks default to 1048575 at a branch):
branch probabilities:
block 1 ->
-> 2         weight=1048575   p= 96.88%
-> 3  exit   weight=33825     p=  3.12%
(The division is exact:
0xfffff
is 2^20−1, and 2^5 ≡ 1
(mod 31) makes 2^20−1 divisible by 31.)
Next, a cold call two blocks deep. Block 3 is cold and block 1 cannot
avoid it, so the seed climbs from 3 to 1 — 3 post-dominates it — and
stops at 0, which has the bypass through 2.
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
% ./bpi
6 6
0 1
0 2
1 3
3 5
2 4
4 5
3 C
loops, indented by nesting:
(none)
estimated block weights (unknown blocks default to 1048575 at a branch):
block 1 = 65535
block 3 = 65535
branch probabilities:
block 0 ->
-> 1         weight=65535     p=  5.88%
-> 2         weight=1048575   p= 94.12%
The branch at 0 reads the propagated weight:
COLD
against
DEFAULT
is about 1:16, the gap the enum builds
in.
Nested loops:
{2,3}
inside
{1,2,3,4}
. Each
loop scales its own exit —
2→4
leaves only the inner loop,
4→5
only the outer — so both branches split 31:1
independently, even though 4 is still inside the outer loop.
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
% ./bpi
6 7
0 1
1 2
2 3
2 4
3 2
4 1
4 5
loops, indented by nesting:
loop 0 [reducible]  blocks { 1 2 3 4 }  innermost { 1 4 }  entries { 1 }  exits { 5 }  loopWeight=-1
loop 1 [reducible]  blocks { 2 3 }  innermost { 2 3 }  entries { 2 }  exits { 4 }  loopWeight=-1
estimated block weights (unknown blocks default to 1048575 at a branch):
branch probabilities:
block 2 ->
-> 3         weight=1048575   p= 96.88%
-> 4  exit   weight=33825     p=  3.12%
block 4 ->
-> 1         weight=1048575   p= 96.88%
-> 5  exit   weight=33825     p=  3.12%
Finally, an irreducible dispatch: block 0 can enter at any of 1–5,
each arm returns to the dispatcher 5, and 5 branches back to every arm
or exits.
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
% ./bpi
7 14
0 5
0 1
0 2
0 3
0 4
1 5
2 5
3 5
4 5
5 6
5 1
5 2
5 3
5 4
loops, indented by nesting:
loop 0 [IRREDUCIBLE]  blocks { 1 2 3 4 5 }  innermost { 4 }  entries { 1 2 3 4 5 }  exits { 6 }  loopWeight=-1
loop 1 [IRREDUCIBLE]  blocks { 1 2 3 5 }  innermost { 1 2 3 5 }  entries { 1 2 3 5 }  exits { 4 6 }  loopWeight=-1
estimated block weights (unknown blocks default to 1048575 at a branch):
branch probabilities:
block 0 ->  [no estimate: uniform]
-> 5  enter  weight=1048575   p= 20.00%
-> 1  enter  weight=1048575   p= 20.00%
-> 2  enter  weight=1048575   p= 20.00%
-> 3  enter  weight=1048575   p= 20.00%
-> 4  enter  weight=1048575   p= 20.00%
block 5 ->
-> 6  exit   weight=33825     p=  1.05%
-> 1         weight=1048575   p= 32.63%
-> 2         weight=1048575   p= 32.63%
-> 3         weight=1048575   p= 32.63%
-> 4  exit   weight=33825     p=  1.05%
The forest nests two irreducible loops: the DFS reaches 4 first
(successors are visited LIFO), so 4 heads the outer loop, and removing
the header leaves the strongly connected
{1,2,3,5}
as an
inner one — the recursion of the previous post. From 5, the edges to 1,
2, 3 stay inside the inner loop, but
5→4
leaves it, so it
is scaled like the true exit
5→6
even though 4 is still
inside the outer loop. The nesting, and therefore these numbers, is what
a flat SCC destroys.
What changed when BPI
moved to CycleInfo
Before
#210301
, the
heuristic used natural loops as its primary structure and a flat Tarjan
SCC pass as the irreducible fallback, glued together by a two-headed
LoopBlock = {natural loop, SCC id}
. Reducible loops nested
correctly: a natural loop has a single entry, so containment orders them
unambiguously. Irreducible ones did not: a maximal SCC cannot nest, so
every loop in an irreducible region collapsed into one unit.
With the full loop-nesting forest both cases are handled by the same
structure, and irreducible loops nest. On the four-armed dispatch of the
last example the difference is visible in the probabilities:
reducible
irreducible
full loop-nesting forest (
CycleInfo
)
nested
nested —
5→1,2,3
32.63%,
5→4
and
5→6
1.05%
natural loops + flat SCC (
LoopInfo
+
SccInfo
)
nested
flat —
5→1..4
24.80%,
5→6
0.80%
Matching LLVM bit-for-bit
Two details decide exact agreement: one the source mentions only in
passing, one it contradicts.
The first is ordering: seeds are applied in reverse post-order and
the first weight to reach a block wins, so where two propagations
collide the outcome is decided by seed order.
The second is a comment that is wrong.
estimateBlockWeights
drives two worklists and says:
Order is important. Consider two loops where one's exit edge enters
the other: the first loop's weight depends on the second's, and it is
never re-queued when that weight later lands. The pop order of
LoopWorkList
therefore shows up in the output, and that
order follows predecessor iteration order — which for LLVM is use-list
order, the reverse of construction order. A model that iterates
predecessors in the natural order matches on almost every CFG and
disagrees on this one shape.
Machine-level branch
probability
At the machine level the same information is stored, not computed.
MachineBasicBlock
carries the probabilities of its own
out-edges:
1
2
3
4
std::vector<BranchProbability> Probs;
so
MachineBranchProbabilityInfo
is a view rather than an
analysis. Its
run
does not look at the function at all:
1
2
3
4
5
MachineBranchProbabilityAnalysis::Result
MachineBranchProbabilityAnalysis::run
(MachineFunction &,
MachineFunctionAnalysisManager &)
{
return
MachineBranchProbabilityInfo
();
}
Probabilities are computed once on IR and carried down, rather than
re-estimated.
