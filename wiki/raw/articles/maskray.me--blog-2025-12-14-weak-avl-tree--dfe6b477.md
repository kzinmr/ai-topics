---
title: "Weak AVL Tree | MaskRay"
url: "https://maskray.me/blog/2025-12-14-weak-avl-tree"
fetched_at: 2026-05-05T07:01:44.906040+00:00
source: "Fangrui Song (MaskRay)"
tags: [blog, raw]
---

# Weak AVL Tree | MaskRay

Source: https://maskray.me/blog/2025-12-14-weak-avl-tree

tl;dr: Weak AVL trees are replacements for AVL trees and red-black
trees.
The 2014 paper
Rank-Balanced
Trees
(Haeupler, Sen, Tarjan) presents a framework using ranks
and rank differences to define binary search trees.
Each node has a non-negative integer rank
r(x)
. Null
nodes have rank -1.
The rank difference of a node
x
with parent
p(x)
is
r(p(x)) − r(x)
.
A node is
i,j
if its children have rank differences
i
and
j
(unordered), e.g., a 1,2 node has
children with rank differences 1 and 2.
A node is called 1-node if its rank difference is 1.
Several balanced trees fit this framework:
AVL tree: Ranks are defined as heights. Every node is 1,1 or 1,2
(rank differences of children)
Red-Black tree: All rank differences are 0 or 1, and no parent of a
0-child is a 0-child. (red: 0-child; black: 1-child; null nodes are
black)
Weak AVL tree (new tree described by this paper): All rank
differences are 1 or 2, and every leaf has rank 0.
A weak AVL tree without 2,2 nodes is an AVL tree.
1
AVL trees ⫋ weak AVL trees ⫋ red-black trees
Weak AVL Tree
Weak AVL trees are replacements for AVL trees and red-black trees. A
single insertion or deletion operation requires at most two rotations
(forming a double rotation when two are needed). In contrast, AVL
deletion requires O(log n) rotations, and red-black deletion requires up
to three.
Without deletions, a weak AVL tree is exactly an AVL tree. With
deletions, its height remains at most that of an AVL tree with the same
number of insertions but no deletions.
The rank rules imply:
Null nodes have rank -1, leaves have rank 0, unary nodes have rank
1.
Insertion
The new node
x
has a rank of 0, changed from the null
node of rank -1. There are three cases.
If the tree was previously empty, the new node becomes the
root.
If the parent of the new node was previously a unary node (1,2
node), it is now a 1,1 binary node.
If the parent of the new node was previously a leaf (1,1 node), it
is now a 0,1 binary node, leading to a rank violation.
When the tree was previously non-empty,
x
has a parent
node. We call the following subroutine with
x
indicating
the new node to handle the second and third cases.
The following subroutine handles the rank increase of
x
.
We call
break
if there is no more rank violation, i.e. we
are done.
The 2014 paper isn't very clear about the conditions.
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
p = x->parent;
if
(
rank_diff
(x) ==
1
) {
}
else
{
for
(;;) {
Promote p.
x = p;
p = p->parent;
if
(!p)
break
;
d = p->ch[
1
] == x;
if
(
rank_diff
(x) ==
1
) {
break
; }
auto
sib = p->ch[!d];
if
(
rank_diff
(sib) ==
2
) {
auto
y = x->ch[d^
1
];
if
(y &&
rank_diff
(y) ==
1
) {
Perform a
double
rotation involving `p`, `x`,
and
`y`.
}
else
{
Perform a single rotation involving `p`
and
`x`.
x is now a
1
,
1
node
and
there is no more violation.
}
break
;
}
}
}
Insertion never introduces a 2,2 node, so insertion-only sequences
produce AVL trees.
Deletion
TODO: Describe deletion
1
2
3
if (!was_2 && !x && !p->ch[0] && !p->ch[1] && p->rp()) {
// p was unary and becomes 2,2. Demote it.
}
Implementation
Since valid rank differences can only be 1 or 2, ranks can be encoded
efficiently using bit flags. There are three approaches:
Store two bits representing the rank differences to each child. Bit
0: rank difference to left child (1 = diff is 2, 0 = diff is 1). Bit 1:
rank difference to right child
Store a single bit representing the parity (even/odd) of the node's
absolute rank. The rank difference to a child is computed by comparing
parities. Same parity → rank difference of 2. Different parity → rank
difference of 1
Store a 1-bit rank difference parity in each node.
FreeBSD's
sys/tree.h
(
https://reviews.freebsd.org/D25480
, 2020) uses the first
approach. The
rb_
prefix remains as it can also indicate
Rank-Balanced
:) Note: its insertion operation can be futher
optimized as the following code demonstrates.
https://github.com/pvachon/wavl_tree
and
https://crates.io/crates/wavltree
use the second
approach.
The third approach is less efficient because a null node can be
either a 1-child (parent is binary) or a 2-child (parent is unary),
requiring the sibling node to be probed to determine the rank
difference:
int rank_diff(Node *p, int d) { return p->ch[d] ? p->ch[d]->par_and_flg & 1 : p->ch[!d] ? 2 : 1; }
https://maskray.me/blog/2025-12-14-weak-avl-tree
is a
C++ implementation covering both approaches, supporting the following
operations:
insert
: insert a node
remove
: remove a node
rank
: count elements less than a key
select
: find the k-th smallest element (0-indexed)
prev
: find the largest element less than a key
next
: find the smallest element greater than a key
Node structure:
ch[2]
: left and right child pointers.
par_and_flg
: packs the parent pointer with 2 flag bits
in the low bits. Bit 0 indicates whether the left child has rank
difference 2; bit 1 indicates whether the right child has rank
difference 2. A cleared bit means rank difference 1.
i
: the key value.
sum
,
size
: augmented data maintained by
mconcat
for order statistics operations.
Helper methods:
rd2(d)
: returns true if child
d
has rank
difference 2.
flip(d)
: toggles the rank difference of child
d
between 1 and 2.
clr_flags()
: sets both children to rank difference 1
(used after rotations to reset a node to 1,1).
Invariants:
Leaves always have
flags() == 0
, meaning both null
children are 1-children (null nodes have rank -1, leaf has rank 0).
After each insertion or deletion,
mconcat
is called
along the path to the root to update augmented data.
Rotations:
The
rotate(x, d)
function rotates node
x
in
direction
d
. It lifts
x->ch[d]
to replace
x
, and updates the augmented data for
x
. The
caller is responsible for updating rank differences.
Misc
Visualization:
https://tjkendev.github.io/bst-visualization/avl-tree/bu-weak.html
