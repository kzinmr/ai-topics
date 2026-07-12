---
title: "Irreducible loops"
url: "https://maskray.me/blog/2026-07-12-irreducible-loops"
fetched_at: 2026-07-12T07:01:17.803494+00:00
source: "Fangrui Song (MaskRay)"
tags: [blog, raw]
---

# Irreducible loops

Source: https://maskray.me/blog/2026-07-12-irreducible-loops

The
dominator tree
lets
us identify
natural loops
:
a back edge
T->H
whose head
H
dominates its
tail
T
defines a loop with the single entry
H
.
This works only for
reducible
control flow graphs. Optimized
machine code and decompiler output routinely contain
irreducible
loops, which have more than one entry and thus no
dominating header, so the dominator-based method cannot see them.
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
nodes with a header, nested into a forest. (LLVM draws the same line:
LoopInfo
represents natural loops, while the
GenericCycleInfo
used below generalizes them to irreducible
control flow.) A CFG is
reducible
when, in every DFS, each
retreating edge is a
back edge
— its head
v
dominates its tail
u
. Then every cycle lies in a natural
loop whose header dominates it, so control enters the loop only through
that header.
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
Because no node dominates an irreducible cycle, its header is not
intrinsic — we must pick one of the entries. The standard choice
(Havlak, LLVM, and the algorithm below) is the node the DFS reaches
first, i.e. the loop member with the smallest preorder number. So the
loop-nesting forest of an irreducible CFG depends on the DFS order.
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
tag_lhead
) splices it into the node's
innermost-to-outermost chain, ordered by DFS position; this replaces the
UNION-FIND of the classical Havlak–Tarjan algorithm. The total cost is
O(N + k*E)
, where
k
is an
unstructuredness
coefficient
that measures the case-(E) climbs and the chain
splices. On real code
k
is tiny (empirically below 1.5), so
the algorithm is near-linear.
The input format matches the natural-loops post:
n m
on
the first line, then
m
edges
u v
, with node 0
the entry. The program prints each node's innermost loop header, then
the forest, then any re-entry edges.
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
-1
;
int
pos =
0
;
bool
traversed =
false
;
bool
header =
false
;
bool
irreducible =
false
;
};
vector<Node> nd;
vector<vector<
int
>> succ;
vector<pair<
int
,
int
>> reentry;
void
tagLoopHeader
(
int
b,
int
h)
{
if
(h ==
-1
)
return
;
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
(nd[ih].pos >= nd[h].pos) {
b = ih;
}
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
nd[b0].traversed =
true
;
nd[b0].pos = p;
for
(
int
b : succ[b0]) {
if
(!nd[b].traversed) {
tagLoopHeader
(b0,
dfs
(b, p +
1
));
}
else
if
(nd[b].pos >
0
) {
nd[b].header =
true
;
tagLoopHeader
(b0, b);
}
else
if
(nd[b].ilh <
0
) {
}
else
if
(nd[nd[b].ilh].pos >
0
) {
tagLoopHeader
(b0, nd[b].ilh);
}
else
{
reentry.
push_back
({b0, b});
int
h = nd[b].ilh;
nd[h].irreducible =
true
;
while
((h = nd[h].ilh) >=
0
) {
if
(nd[h].pos >
0
) {
tagLoopHeader
(b0, h);
break
;
}
nd[h].irreducible =
true
;
}
}
}
nd[b0].pos =
0
;
return
nd[b0].ilh;
}
void
emitLoop
(
int
h,
const
vector<vector<
int
>> &members,
const
vector<vector<
int
>> &children)
{
for
(
int
c : children[h])
emitLoop
(c, members, children);
printf
(
"loop %d%s:"
, h, nd[h].irreducible ?
" (irreducible)"
:
""
);
printf
(
" %d"
, h);
for
(
int
v : members[h])
printf
(
" %d"
, v);
for
(
int
c : children[h])
printf
(
" (loop %d)"
, c);
puts
(
""
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
for
(
int
v =
0
; v < n; v++)
printf
(
"%d: %d\n"
, v, nd[v].ilh);
vector<vector<
int
>>
members
(n),
children
(n);
vector<
int
> roots;
for
(
int
v =
0
; v < n; v++) {
if
(nd[v].header)
(nd[v].ilh <
0
? roots : children[nd[v].ilh]).
push_back
(v);
else
if
(nd[v].ilh >=
0
)
members[nd[v].ilh].
push_back
(v);
}
for
(
int
h : roots)
emitLoop
(h, members, children);
if
(!reentry.
empty
()) {
printf
(
"re-entry edges:"
);
for
(
auto
&e : reentry)
printf
(
" %d->%d"
, e.first, e.second);
puts
(
""
);
}
return
0
;
}
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
9
10
11
% ./wei
3 4
0 1
0 2
1 2
2 1
0: -1
1: -1
2: 1
loop 1 (irreducible): 1 2
re-entry edges: 0->2
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
9
10
11
% ./wei
3 4
0 2
0 1
1 2
2 1
0: -1
1: 2
2: -1
loop 2 (irreducible): 2 1
re-entry edges: 0->1
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
13
14
15
16
17
% ./wei
5 7
0 1
1 2
1 3
2 3
3 2
3 1
3 4
0: -1
1: -1
2: 1
3: 2
4: -1
loop 2 (irreducible): 2 3
loop 1: 1 (loop 2)
re-entry edges: 1->3
Only the inner loop is irreducible; the outer loop has the single
entry 1.
3
's header list is
2, 1
: its
innermost loop is
{2,3}
, enclosed by
{1,2,3}
.
Pipe any of these graphs through
awk 'BEGIN{print "digraph G{"} NR>1{print $1"->"$2} END{print "}"}'
to render them with graphviz.
Relation to natural loops
On a reducible CFG the first-visited node of a loop is exactly the
node that dominates it, so this algorithm's header coincides with the
natural-loop header and the two forests are identical. Running the
program on the
natural
loops
example — a reducible graph with a self-loop and an
unreachable node — produces the same loops as that post's
dominator-based program, and reports no re-entry edges.
The Havlak–Tarjan algorithm reaches the same forest by a different
route: a top-down DFS to find back edges, then a bottom-up UNION-FIND
pass propagating headers from loop tails. LLVM's
GenericCycleInfo
(
llvm/include/llvm/ADT/GenericCycleImpl.h
) computes the
same forest with its own two-pass scheme — a DFS that numbers blocks,
then a reverse-preorder scan that seeds each header from a back edge and
gathers the cycle body by walking predecessors backward (no UNION-FIND).
Wei et al.'s contribution is folding both passes into a single DFS, and
their re-entry bookkeeping (case (E)) is what marks the irreducible
loops along the way.
