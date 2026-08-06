---
title: "Enumerating trees and circles"
url: "https://www.johndcook.com/blog/2026/08/05/enumerating-trees-and-circles/"
fetched_at: 2026-08-06T10:18:23.990286+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Enumerating trees and circles

Source: https://www.johndcook.com/blog/2026/08/05/enumerating-trees-and-circles/

A few days ago I wrote a post on
counting rooted trees
. That post looked at the sequence
c
(
n
) which counts the number of rooted trees with
n
nodes. Here one node is distinguished as the root, but the nodes below the root are not distinguished from each other; all that matters is how the nodes are connected.
The number of rooted trees with
n
nodes is the same as the number of ways to configure
n
− 1 non-overlapping circles. Not only are the counts the same, there is a natural correspondence between the trees and the circles. It’s not obvious that there should be such a correspondence, with the right notation the correspondence is sort of a pun.
The standard way to represent unlabeled trees is as a
multiset
of their children. We use a multiset, not a set, because some elements will be repeated. We represent a leaf as a pair of parentheses:
()
.
There is only one rooted tree with one node:
()
.
There is only one rooted tree with one two nodes:
(())
. Here the outer parentheses represent the root node and the inner parentheses represent its child.
There are two rooted trees with three nodes, and we can represent them as
((()))
and
((),())
. The first is the straight line tree: a node that has a single child node that has a single child node. The second is a node that branches to two nodes. (Here’s where we need multisets.)
The four rooted trees with four nodes can be represented as
(((())))
,
((((),()))
,
((),(()))
, and
((),(),(),())
.
Here are the nine rooted trees with five nodes:
((((()))))
((((),())))
(((),(())))
(((),(),()))
((()),(()))
((),((())))
((),((),()))
((),(),(()))
((),(),(),())
The correspondence with non-overlapping circles removes the outer parentheses then joins the rest to form circles, with nested parentheses corresponding to concentric circles. A more geometric way to see the correspondence is to start at the bottom of the tree, replace leaves with circles, then work your way up circling connected components.
