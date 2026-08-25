---
title: "Irreducible loops"
url: "https://maskray.me/blog/irreducible-loops"
fetched_at: 2026-08-24T10:32:20.581635+00:00
source: "Fangrui Song (MaskRay)"
tags: [blog, raw]
---

# Irreducible loops

Source: https://maskray.me/blog/irreducible-loops

The
dominator tree
lets us
identify
natural loops
: a back edge
T->H
whose head
H
dominates its tail
T
defines a loop with the single entry
H
. This
works only for
reducible
control flow graphs. Optimized machine
code and decompiler output routinely contain
irreducible
loops,
which have more than one entry and thus no dominating header, so the
dominator-based method cannot see them.
This post builds a loop-nesting forest for an arbitrary CFG with the
single-pass depth-first search of 韦韬、毛剑、邹维、陈宇(Tao Wei, Jian
Mao, Wei Zou & Yu Chen)
A New Algorithm for Identifying Loops in
Decompilation
, SAS 2007 (The 14th International Static Analysis
Symposium).
Reducibility
A depth-first search from the entry classifies every non-tree edge
relative to the spanning tree. A
retreating edge
u->v
goes to an ancestor
v
of
u
on the DFS path. A
cycle
is a closed path in the
CFG, a graph-theoretic object with no distinguished entry; a
loop
is the control-flow structure built on top — a set of
nodes with a header, nested into a forest. A CFG is
reducible
when, in every DFS, each retreating edge is a
back edge
— its
head
v
dominates its tail
u
. Then every cycle
lies in a natural loop whose header dominates it, so control enters the
loop only through that header.
A CFG is
irreducible
when some cycle has two or more
entries: nodes with a predecessor outside the cycle. No single node
dominates the cycle, so there is no natural header. The smallest example
is the
irreducible core
:
The irreducible core: 0 enters the 1↔︎2
cycle at both nodes. Double circle = header (1, visited first); dashed =
the re-entry edge.
Node 0 branches to both 1 and 2, and
1 -> 2 -> 1
is a cycle entered at 1 (through
0->1
) and at 2 (through
0->2
). M.S. Hecht and J.D. Ullman proved that a CFG is
irreducible if and only if it contains this three-node pattern as a
subgraph, allowing each edge to be a path through other nodes.
Because no node dominates an irreducible cycle, the header is not
intrinsic — we must pick one of the entries. The standard choice (Havlak
and the algorithm below) is the node the DFS reaches first, i.e. the
loop member with the smallest preorder number. So the loop-nesting
forest of an irreducible CFG depends on the DFS order.
Loop-nesting forest
There is no agreed definition of the loop-nesting forest for
irreducible CFGs. Steensgaard, Sreedhar–Gao–Lee, Havlak, and Ramalingam
each give a different one; for the CFG in Wei et al.'s Fig. 3 they
report two, one, three, and one loops respectively. We adopt Havlak's,
the finest, because it gives each loop a single header and the fewest
goto
s when re-structuring, and it is what LLVM's
GenericCycleInfo
computes:
The outermost loops are the maximal strongly connected regions (with
at least one internal edge).
A loop's header is its minimum-preorder node.
Its inner loops are the loops of the subgraph induced on (loop nodes
− header), found recursively.
So nesting is set containment, not a reachability order: a subloop's
nodes are a subset of its parent's (minus the parent's header), and
since every loop is strongly connected, a loop and its subloops are
mutually reachable.
The forest has a compact encoding. For each node record its
innermost loop header
iloop_header
: the header of
the smallest loop containing it, or none. A header's own
iloop_header
is the header of its parent loop. Following
the
iloop_header
links from a node lists its enclosing
loops innermost-first — the "loop header list" of the paper. Which nodes
are headers, plus every node's innermost header, determines the whole
forest; that is what the program below prints.
Representing and querying
the forest
Building the forest is half the job; every consumer then asks two
questions repeatedly: is a node inside loop
L
, and is loop
L2
nested in
L1
? How the forest is stored
decides whether these are O(1).
The obvious layout gives each loop the set of all its nodes — its own
plus every descendant's. A membership test is one hash probe, but a node
nested
d
loops deep is stored
d
times, so
memory and build cost are
O(N * depth)
.
An Euler tour of the forest removes the duplication. Lay every node
into one shared array so each loop owns a contiguous slice
[begin, end)
nested inside its parent's. Each node then
appears once, memory is
O(N)
, and both queries become
interval tests:
is a node inside
L
: map the node to its innermost loop,
then test that loop's index against
L
's slice;
is
L2
nested in
L1
:
L1.begin <= L2.begin && L2.end <= L1.end
.
No per-loop set survives — the same trick
DominatorTree
uses for O(1) dominance (
DFSNumIn
/
DFSNumOut
),
and the direction
GenericCycleInfo
took.
The header needn't be stored separately either: it is the first block
of the loop's slice (the minimum-preorder member), so
begin
already locates it.
The contiguous slices suit a build-once analysis like
GenericCycleInfo
, but are costly to keep valid under the
in-place CFG edits
LoopInfo
allows — which is why the two
siblings compute the same forest yet store it differently.
Identifying loops in one DFS
pass
Natural loops need a dominator tree first. Wei et al. observe that a
single DFS with a little bookkeeping suffices for an arbitrary CFG — no
dominator tree, no UNION-FIND, no second bottom-up pass.
Let
p
be the current DFS path, the recursion stack from
the entry to the node being visited (
DFSP
in the paper).
pos[b]
is
b
's 1-based position on that path,
or 0 once
b
has been popped. Every node carries
iloop_header
, its innermost loop header discovered so far.
When visiting
b0
, each successor
b
falls into
one of five cases:
b
is unvisited — a tree edge. Recurse; the call returns
b
's innermost header, which we merge into
b0
's
chain.
b
is on the current path (
pos[b] > 0
) —
a back edge.
b
is a loop header; merge it into
b0
.
b
is finished and in no loop — a forward or cross edge
to a non-loop node; ignore it.
b
is finished, inside a loop whose innermost header
h
is still on the path —
b0
belongs to that
loop too; merge
h
.
b
is finished, inside a loop whose innermost header is
not
on the path — the edge
b0->b
enters the
loop below its header: a
re-entry edge
, and the loop is
irreducible
. Walk up
b
's header chain to the first
header that is on the path and merge that.
Merging a header (
tagLoopHeader
) splices it into the
node's innermost-to-outermost chain, ordered by DFS position; this
replaces the UNION-FIND of the classical Havlak–Tarjan algorithm. The
total cost is
O(N + k*E)
, where
k
is an
unstructuredness coefficient
that measures the case-(E) climbs
and the chain splices. On real code
k
is tiny (empirically
below 1.5), so the algorithm is near-linear. That near-linearity hides a
worst case: each
tagLoopHeader
splice is
O(depth)
, so on deeply nested loops
k
grows
toward
O(N)
and the algorithm turns quadratic, whereas the
UNION-FIND of Havlak–Tarjan stays near-linear even there. In benchmarks
Wei runs 2–4x faster on realistic CFGs but blows up on adversarial deep
nests.
Successor order matters within that bound. When one block has several
back edges to nested headers, visiting them outer-header-first
(ascending preorder) keeps each splice
O(1)
, whereas
innermost-first re-walks the chain every time —
O(d)
versus
O(d^2)
for that block. Iterating successors in reverse
postorder approximates the good order for free. But this only shifts the
constant: a spine of
d
nested loops with a single latch
each costs
O(d*E)
in every order, so the worst case
stands.
Havlak–Tarjan is not immune either; it just fails on different
inputs. On that reducible deep nest its UNION-FIND collapses each
single-entry loop, so it stays near-linear where Wei blows up — but its
backward flood re-scans an absorbed subloop's whole
entry
set,
so a deeply nested loop that is also multi-entry (a high-in-degree block
re-entered inside every level) costs it
O(E*depth)
too,
Ramalingam's classic critique of Havlak. Neither is universally
near-linear: Wei is quadratic on any deep nest, Havlak–Tarjan only on
irreducible ones.
The input format matches the natural-loops post:
n m
on
the first line, then
m
edges
u v
, with node 0
the entry. The program identifies the loops, then materializes the flat
Euler-tour layout described above: it prints the shared
layout
array, then walks the forest. Each loop shows its
slice
[begin, end)
— the full extent it and its subloops
span — then the blocks it owns directly, header first (these fill the
front of the slice, and the subloops' slices follow), and, if
irreducible, its non-header entries.
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
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
148
149
150
151
152
153
154
155
156
157
158
159
160
161
162
163
164
165
166
167
168
169
170
171
172
173
174
175
176
177
178
179
180
181
182
183
184
185
186
187
188
189
190
191
192
193
194
195
196
197
198
199
200
201
202
203
204
205
206
207
#
include
<algorithm>
#
include
<cassert>
#
include
<cstdio>
#
include
<utility>
#
include
<vector>
using
namespace
std;
struct
Node
{
int
ilh =
0
;
union
{
int
pos =
0
;
int
loopIdx;
};
bool
traversed =
false
;
bool
header =
false
;
};
vector<Node> nd;
vector<vector<
int
>> succ;
vector<
int
> preorder;
int
numHeaders =
0
;
vector<pair<
int
,
int
>> reentries;
void
tagLoopHeader
(
int
b,
int
h)
{
assert
(h !=
-1
);
while
(b != h) {
int
ih = nd[b].ilh;
if
(ih ==
-1
) {
nd[b].ilh = h;
return
;
}
if
(nd[ih].pos >= nd[h].pos)
b = ih;
else
{
nd[b].ilh = h;
b = h;
h = ih;
}
}
}
int
dfs
(
int
b0,
int
p)
{
nd[b0].ilh =
-1
;
nd[b0].pos = p;
nd[b0].traversed =
true
;
preorder.
push_back
(b0);
for
(
int
b : succ[b0]) {
if
(!nd[b].traversed) {
int
h =
dfs
(b, p +
1
);
if
(h >=
0
)
tagLoopHeader
(b0, h);
}
else
if
(nd[b].pos >
0
) {
if
(!nd[b].header) {
nd[b].header =
true
;
++numHeaders;
}
tagLoopHeader
(b0, b);
}
else
{
for
(
int
h = nd[b].ilh; h >=
0
; h = nd[h].ilh) {
if
(nd[h].pos >
0
) {
tagLoopHeader
(b0, h);
break
;
}
reentries.
push_back
({h, b});
}
}
}
nd[b0].pos =
0
;
return
nd[b0].ilh;
}
struct
Loop
{
int
header, childHead =
-1
, nextSibling =
-1
, ownCount =
1
;
int
begin =
0
, end =
0
;
};
vector<Loop> loops;
vector<
int
> layout;
vector<vector<
int
>> entries;
int
cursor =
0
;
void
tour
(
int
c)
{
cursor += loops[c].ownCount;
loops[c].begin = cursor;
for
(
int
ch = loops[c].childHead; ch >=
0
; ch = loops[ch].nextSibling)
tour
(ch);
loops[c].end = cursor;
}
void
dump
(
int
c,
int
indent)
{
Loop &L = loops[c];
printf
(
"%*sloop %d  slice [%d,%d)  own blocks:"
,
2
* indent,
""
, L.header,
L.begin, L.end);
for
(
int
i = L.begin; i < L.begin + L.ownCount; i++)
printf
(
" %d"
, layout[i]);
if
(!entries[L.header].
empty
()) {
printf
(
"  (non-header entries:"
);
for
(
int
e : entries[L.header])
printf
(
" %d"
, e);
putchar
(
')'
);
}
puts
(
""
);
for
(
int
ch = L.childHead; ch >=
0
; ch = loops[ch].nextSibling)
dump
(ch, indent +
1
);
}
int
main
()
{
int
n, m;
if
(
scanf
(
"%d %d"
, &n, &m) !=
2
)
return
0
;
succ.
assign
(n, {});
for
(
int
i =
0
; i < m; i++) {
int
u, v;
if
(
scanf
(
"%d %d"
, &u, &v) !=
2
)
return
1
;
succ[u].
push_back
(v);
}
nd.
assign
(n, Node{});
if
(n >
0
)
dfs
(
0
,
1
);
int
topHead =
-1
;
if
(numHeaders) {
loops.
reserve
(numHeaders);
for
(
int
v : preorder) {
if
(nd[v].header) {
nd[v].loopIdx = loops.
size
();
loops.
push_back
({v});
}
else
if
(nd[v].ilh >=
0
) {
nd[v].loopIdx = nd[nd[v].ilh].loopIdx;
++loops[nd[v].loopIdx].ownCount;
}
else
{
nd[v].loopIdx =
-1
;
}
}
for
(
int
c = (
int
)loops.
size
() -
1
; c >=
0
; c--) {
int
v = loops[c].header;
int
&head =
nd[v].ilh >=
0
? loops[nd[nd[v].ilh].loopIdx].childHead : topHead;
loops[c].nextSibling = head;
head = c;
}
for
(
int
c = topHead; c >=
0
; c = loops[c].nextSibling)
tour
(c);
layout.
assign
(cursor,
0
);
for
(
int
i = (
int
)preorder.
size
() -
1
; i >=
0
; i--)
if
(nd[preorder[i]].loopIdx >=
0
)
layout[--loops[nd[preorder[i]].loopIdx].begin] = preorder[i];
sort
(reentries.
begin
(), reentries.
end
());
reentries.
erase
(
unique
(reentries.
begin
(), reentries.
end
()), reentries.
end
());
entries.
assign
(n, {});
for
(
auto
[h, b] : reentries)
entries[h].
push_back
(b);
}
printf
(
"block layout:"
);
for
(
int
b : layout)
printf
(
" %d"
, b);
puts
(
""
);
for
(
int
c = topHead; c >=
0
; c = loops[c].nextSibling)
dump
(c,
0
);
return
0
;
}
Non-header entries occur only at case-E targets. Here is an
example:
flowchart TB
    n0((0)) --> n1((1))
    n1 --> n2((2))
    n2 --> n3((3))
    n1 --> n4((4))
    n3 -->|back| n2
    n3 -->|back| n1
    n4 -. "re-entry (E)" .-> n3

    classDef hdr stroke:#37c98b,stroke-width:3px;
    class n1,n2 hdr

    linkStyle 0,1,2,3 stroke:#4c8dff,stroke-width:2px
    linkStyle 4,5 stroke:#ff5d5d,stroke-width:2px
    linkStyle 6 stroke:#ffab40,stroke-width:2px,stroke-dasharray:5 4
Examples
The irreducible core:
1
2
3
4
5
6
7
8
% ./wei_blocks
3 4
0 1
0 2
1 2
2 1
block layout: 1 2
loop 1  slice [0,2)  own blocks: 1 2  (non-header entries: 2)
The header is 1 because the DFS reaches 1 first. List
0 2
before
0 1
and the header becomes 2
instead: the loop is the same set of nodes, but its header — and
therefore the forest — depends on the DFS order, unlike a natural
loop.
1
2
3
4
5
6
7
8
% ./wei_blocks
3 4
0 2
0 1
1 2
2 1
block layout: 2 1
loop 2  slice [0,2)  own blocks: 2 1  (non-header entries: 1)
A nested example: a reducible outer loop
{1,2,3}
(back
edge
3->1
) containing an irreducible inner loop
{2,3}
, entered at 2 (via
1->2
) and at 3
(via
1->3
):
The irreducible inner loop {2,3} (double
circles) nested in the reducible outer loop {1,2,3}; the dashed edge 1→3
is the re-entry.
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
% ./wei_blocks
5 7
0 1
1 2
1 3
2 3
3 2
3 1
3 4
block layout: 1 2 3
loop 1  slice [0,3)  own blocks: 1
loop 2  slice [1,3)  own blocks: 2 3  (non-header entries: 3)
Only the inner loop is irreducible; the outer loop has the single
entry 1. The nesting gives
3
's header list,
innermost-first: its innermost loop
{2,3}
(slice
[1,3)
) sits inside
{1,2,3}
(slice
[0,3)
).
Pipe any of these graphs through
awk 'BEGIN{print "digraph G{"} NR>1{print $1"->"$2} END{print "}"}'
to render them with graphviz.
Relation to natural loops
On a reducible CFG the first-visited node of a loop is exactly the
node that dominates it, so this algorithm's header coincides with the
natural-loop header and the two forests are identical. Running the
program on the
natural loops
example —
a reducible graph with a self-loop and an unreachable node — produces
the same loops as that post's dominator-based program, with none marked
irreducible (no non-header entries).
The Havlak–Tarjan algorithm reaches the same forest by a different
route: a top-down DFS to find back edges, then a bottom-up UNION-FIND
pass propagating headers from loop tails. Wei et al.'s contribution is
folding both passes into a single DFS, and their re-entry bookkeeping
(case (E)) is what marks the irreducible loops along the way.
Recent improvements to
LLVM's CycleInfo
LLVM's
GenericCycleInfo
computes this loop-nesting
forest — it just calls a loop a
cycle
. Several recent changes
rebuild it around the structure above.
Flat block layout.
Each cycle used to own a set of
its blocks, so a block nested
d
deep was stored
d
times (
O(N*depth)
). Now every in-loop block
lives once in a shared array, each cycle a contiguous slice nested
inside its parent's, making
contains
and nested-in interval
tests. The header is the slice's first block rather than a stored field,
and an irreducible cycle's extra entries are appended — the
layout
/
tour
/
dump
the program
above builds.
TODO
Single-pass construction.
The old code used a
multi-pass scheme: a DFS to number blocks, then a reverse-preorder flood
that grew each cycle from its back edges. It is now the single Wei DFS
above — one traversal tags every block's innermost header and records
the re-entries that make a cycle irreducible.
