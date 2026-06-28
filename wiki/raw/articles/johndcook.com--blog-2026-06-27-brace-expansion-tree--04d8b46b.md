---
title: "Brace expansion tree"
url: "https://www.johndcook.com/blog/2026/06/27/brace-expansion-tree/"
fetched_at: 2026-06-28T07:01:23.173818+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Brace expansion tree

Source: https://www.johndcook.com/blog/2026/06/27/brace-expansion-tree/

Here’s a crazy bash one-liner I found via an
article
by Peter Krumins:
echo {w,t,}h{e{n{,ce{,forth}},re{,in,fore,with{,al}}},ither,at}
This prints 30 English words:
when, whence, whenceforth, where, wherein, wherefore, wherewith, wherewithal, whither, what, then, thence, thenceforth, there, therein, therefore, therewith, therewithal, thither, that, hen, hence, henceforth, here, herein, herefore, herewith, herewithal, hither, hat
This post will explain how the one-liner works.
Bash brace expansion iterates through all possibilities listed within curly braces, with possibilities separated by a comma. Note that the comma is a
separator
and not a
terminator
. And so, for example, the expression
{w,t,}
is effectively
{w,t,""}
.
When bash sees two brace expressions, these expand to the cartesian product of the two expressions. For example,
echo {A,B}{1,2,3}
produces
A1 A2 A3 B1 B2 B3
In the expression above we have
{w,t,}h{e…,ither,at}
So the expansion will enumerate all possibilities of
{w,h,}
multiplied by all possibilities of
{e…,ither,at}
where
e…
is itself a brace expression.
A diagram will help a lot.
The brace expansion does a depth-first traversal of this tree.
