---
title: "Possibly all the ways to get loop-finding in graphs wrong"
url: "https://www.chiark.greenend.org.uk/~sgtatham/quasiblog/findloop/"
fetched_at: 2026-04-27T07:56:59.322518+00:00
source: "chiark.greenend.org.uk/~sgtatham"
tags: [blog, raw]
---

# Possibly all the ways to get loop-finding in graphs wrong

Source: https://www.chiark.greenend.org.uk/~sgtatham/quasiblog/findloop/

Possibly all the ways to get loop-finding in graphs wrong
[Simon Tatham, 2024-09-09]
Introduction
In
      my
puzzle
      collection
, there are many games in which you have to
      connect points together by edges, making a graph, and the puzzle
      rules say you must avoid making any loop in the graph. Examples
      are
Net
,
Slant
,
      and some configurations
      of
Bridges
(although not the default
      one).
Loopy
and
Pearl
also care about whether there’s a loop in a graph, although
      those two are more subtle: your
aim
is to make a loop,
      and only
wrong
loops must be rejected.
Therefore, those puzzle programs need to be able to check
      whether a graph has a loop in it, in order to decide whether the
      puzzle solution is correct. If there is a loop, they also have
      to identify the edges that make up the loop, in order to point
      out to the player why their solution hasn’t been accepted.
Examples of loops in Net and Slant, highlighted in
        red as errors
Over the years I’ve been developing these puzzles, I’ve gone
      through an amazing number of algorithms for doing that job. Each
      one was unsatisfactory for some reason, and I threw it away, and
      moved on to the next.
I might by now have collected
all
the ways to do this
      job wrong! So I thought I’d write up all my mistakes, as a case
      study in all the ways you can solve this particular problem
      wrongly – and also in how much effort you can waste by not
      managing to find the existing solution in the literature.
The algorithms
Vertex dsf
When one of these puzzles is
generated
, the generator
      will run an automated solving algorithm, to check that its
      solution is unique. So the solving algorithm needs to check
      whether it’s accidentally made a loop in the graph.
Or, more precisely, it’s better if the solver can tell whether
      it’s
about to
make a loop: when it’s considering adding
      some edge to the graph, it wants to know if that
      edge
would
form a loop. If so, it decides not to add it
      at all, which is more efficient than adding it first, finding
      you’ve made a mess, and having to undo your work.
My automated solvers generally handle this by using an
      implementation of
      the
disjoint-set
      forest
data structure, otherwise known as a ‘union-find’
      data structure, or just ‘disjoint-set data
      structure’
. My code refers to this as a ‘dsf’ throughout,
      which is much shorter, and I’ll follow that convention here
      too.
For those who haven’t encountered a dsf before, it’s a very
      fast data structure for tracking equivalence between elements of
      a set, as long as equivalences are added
incrementally
:
      you start with every element of the set being considered
      different, and you can update the data structure to make two
      elements equivalent to each other when they previously weren’t,
      but no elements ever
stop
being equivalent when they
      previously were. So the elements of the set are partitioned into
      equivalence classes, and an update can merge two classes, but a
      class never splits. You can efficiently add a new equivalence by
      telling the dsf that some pair of elements
a
and
b
will now be considered the same, and you can query it at any
      time to ask whether two elements are currently considered
      equivalent. It automatically tracks transitivity, so that (for
      example) if you’ve already told it that
a
=
b
and
      that
c
=
d
, and then you tell it
      that
b
=
c
, it will immediately know
      that
a
=
d
as well. It’s an absolute keystone of
      my entire puzzle collection: without that utility module most of
      it would fall down in a heap on the floor.
So when the automated solver
      for
Slant
– for example – is trying to solve a puzzle, it makes a dsf on
      the vertices of the grid. Every time it adds an edge, it tells
      the dsf to unify the two vertices at the ends of that edge. So
      the equivalence classes of the dsf precisely track the connected
      components of the graph: if two vertices are reachable from each
      other by a path, then the dsf will report them as ‘equivalent’,
      and if they aren’t, it won’t.
The dsf classes corresponding to a half-constructed
        graph
This means that
before
the solver adds an edge to the
      puzzle solution, it can query the dsf to see whether the two end
      vertices are considered equivalent. If the dsf says yes, then
      there’s already a path between those vertices, which can’t
      involve the edge we’re about to add (because we haven’t added it
      yet). Therefore, if we
did
add that edge, there would
      be two completely separate paths between the vertices – i.e. a
      loop.
Endpoints in the same dsf class:
adding this
            edge would create a loop
Endpoints in different classes:
this edge is
            OK (and merges the classes)
The automated solvers usually only add an edge to the graph if
      they’re sure it’s correct, which means they never need to change
      their mind and remove it again. So as they go along, they only
      need to maintain a single dsf, initialised at the start of the
      solving process when the grid is empty, and update it as they go
      along.
But to use the same system during play, when the player might
      add or remove edges in any way they like, you have to start from
      scratch every time you want to check for errors, i.e. every time
      the player makes a move. Each time, you make a new dsf; iterate
      through the player’s game state unifying the endpoints of each
      edge the player has filled in; in each case, check beforehand
      whether the endpoints were already equivalent, and if so,
      disallow the player’s solution, because it has a loop.
What’s wrong with it?
This algorithm is correct, and very efficient. For automated
      solving, there’s nothing at all wrong with it, especially
      because you get to keep just one dsf for the whole run of the
      solver. So the automated solvers in Puzzles still do their loop
      detection this way.
But it won’t generate the nicely highlighted loops I showed in
      the introduction. This algorithm can only report ‘yes’ or ‘no’:
      either there is a loop, or there isn’t. It can’t automatically
      identify
all
the edges of the loop, to light them up
      and show them to the player. At most, it can find
one
edge of the loop: whichever one was added last. If the loop is
      complicated and twisty, it can be difficult for the player to
      pick out the rest of it by eye – it’s like trying to solve a
      maze on screen.
So, when this was the only loop-detector I had, players would
      fill in what they
thought
was a correct solution to a
      Slant puzzle, and the game wouldn’t flash to indicate victory,
      and it would be hard to figure out why not.
This algorithm is fine as far as it goes – but it doesn’t go
      far enough.
Graph pruning
So our revised problem is: don’t just say
that
a loop
      exists, but identify every edge involved in it. Ideally, if
      there are multiple loops, identify
all
their edges.
My first attempt to solve this problem worked by iteratively
      pruning the graph. Find a vertex with only one edge coming in to
      it. Then that edge can’t be part of a loop. So we can remove it,
      without destroying any loops in the graph.
Once you start removing edges, you reduce the degree of further
      vertices, so now maybe more of them have degree 1. So keep
      pruning, until you can’t find any more degree-1 vertices.
Degree-1 vertices and their edges
Pruning those makes a new degree-1 vertex
No more to prune: what’s left is a loop
If the graph had no loops in it at all, then this procedure
      ends up having pruned away
all
the edges, leaving an
      empty graph, in which all the vertices are isolated. But if
      there is a loop, then no edge of the loop can possibly be
      pruned. So highlight all the remaining edges as errors.
What’s wrong with it?
This algorithm correctly identifies whether there’s a loop, and
      it guarantees to highlight every edge involved in any loop.
      Unfortunately, that’s not
all
that it highlights.
If the graph contains a ‘dumb-bell’ shaped subgraph consisting
      of two loops connected by a path, then the loops can’t ever be
      pruned, but neither can the connecting path. So that will be
      highlighted in addition to the loops themselves.
The red edges aren’t part of any loop.
But pruning
        still can’t remove them.
This algorithm highlights
too many
edges!
Loop tracing
So I thought about how to solve this ‘dumb-bell’ problem, and
      after some pondering, came up with a completely different
      approach.
To begin with, we go back to the ‘vertex dsf’ idea. To check
      the player’s solution for errors during play, we make a fresh
      dsf with all vertices separate, and iterate through the graph
      edges, unifying the two endpoints of each edge. Before each
      unification, we query the dsf to see whether the two endpoints
      were
already
connected to each other. If they were, we
      know that the edge we’re currently processing is part of a
      loop.
But this time, we don’t stop there. Once we’ve identified one
      edge that’s part of a loop, we do a graph search around the rest
      of the graph to find an alternative path between its endpoints.
      Then we’ve identified a specific loop involving that edge, and
      we can light up every part of that loop as an error.
Once you’ve done that, don’t stop there: return to the main
      iteration that adds the rest of the edges to the dsf, in case
      there are more loops you can find and trace round.
What’s wrong with it?
This algorithm solves the dumb-bell problem: it only ever
      lights up an edge when it’s found an actual loop in the graph,
      with that edge being part of it. So it definitely can’t light up
      any edge that is
not
part of a loop. The central bar of
      the dumb-bell graph is safe from accidental highlighting.
But I couldn’t convince myself that this technique would
      catch
all
the loops in the graph. What if there are
      several loops that touch, or intersect each other? If you’re
      looking for a path between the two endpoints of some particular
      edge, and there’s
more
than one such path, the tracing
      will only find one of them. Might there be a situation in which
      an edge is part of a loop, but we somehow missed it, because
every
tracing operation happened to choose some other
      route?
Loops big and small. Are we
sure
the tracer
        will walk round them all?
I never saw this happen – but I also never managed to convince
      myself that it
couldn’t
, and that was unsatisfying.
However, even supposing this algorithm has a flaw of that kind,
      it’s not
too
bad. It will at least reliably identify
      whether or not there are any loops at all. A loop-free graph
      will be correctly reported as OK, and a loopy graph will
      have
at least one
loop highlighted.
And I never saw the tracing algorithm miss a loop
in
      practice
, or had any report of a failure from a user. So
      this version stayed around for some years, until I had a better
      idea.
Face dsf
In 2008, a contributor sent me a patch making major changes
      to
Loopy
.
      Before the changes, it only supported playing on square grids,
      like conventional Slitherlink. Afterwards, it supported a wide
      variety of other periodic
tilings – triangular
      grids, hexagonal honeycombs, various tilings of mixed shapes,
      etc – using a general system for representing the game grid as a
      planar graph.
While I was discussing that patch with its author, I realised
      that there’s a neat algorithm for loop detection,
using
the fact that all the graphs involved are planar.
As well as vertices and edges, a graph embedded in the plane
      has a concept of ‘faces’: the regions of the plane separated by
      the graph edges. If a planar graph contains no loops, then
      there’s only one face: from any part of the plane you can reach
      any other part, without having to cross a graph edge. You might
      have to take a roundabout route, but there always
is
a
      route.
You can walk between the green circles on either side
        of an edge, by a roundabout route
Conversely, if a planar graph
does
contain a loop,
      then that loop separates the plane into two regions: the inside
      and the outside. To get from one to the other, you’d have to
      cross an edge of the loop.
You can’t walk between shaded and unshaded areas
        without crossing an edge
So my new idea was: instead of making a dsf on
      the
vertices
of the grid to find a loop
      that
joins
them to each other, we make a dsf on
      the
faces
of the grid – to find a loop
      that
separates
them from each other.
In detail: to scan a grid for loops, you divide the plane into
      regions that no grid edge can possibly intersect, and then you
      iterate over every edge of the
grid graph
. For each
      grid-graph edge that is
not
part of the user’s
      solution, you tell the dsf to merge the two regions on opposite
      sides of that edge, representing the fact that it’s possible to
      walk from one region to the other without having to cross a
      solution edge.
Player put an edge between these faces: don’t
            unify
No edge in the way: OK to unify
When you’re done, you’ve partitioned the regions into their
      connected components. Any two regions in the same component can
      be reached without crossing a solution edge. But regions
      in
different
components can’t be.
So the boundary of any component is precisely a loop. In other
      words: a solution edge is part of a loop
if and only if
the regions on either side of it are not equivalent in the dsf!
The loop edges are precisely the ones separating
        the shaded and unshaded dsf classes
For Loopy, it’s most obvious how to apply this principle. The
      ‘regions’ I discuss here are precisely the faces of the grid
      graph – the squares, hexagons, triangles (or whatever) of the
      starting grid, as in the diagrams above. For Net, it’s almost as
      simple: the solution graph connects the centres of grid squares,
      so the ‘regions’ must be offset from that: they’re squares
      centred on the grid
vertices
.
It’s slightly more complicated
      for
Slant
,
      because the set of possible solution edges
doesn’t
form
      a planar graph: the two different diagonals you can put in a
      square cross each other. But that’s OK: we can imagine turning
      it back into a planar graph by dividing each edge in two at the
      midpoint of the square, so that the player’s move fills in two
      of those half-edges in a single mouse click. Then the ‘regions’
      are the faces of that subdivided planar graph: each region is a
      diamond surrounding one of the original grid edges.
Unify the top and left red diamonds with each other.
Also unify the bottom and right green diamonds with each other.
The player’s diagonal edge prevents unifying the red ones with the green ones.
What’s wrong with it?
When I thought of this approach, I was really pleased with it!
      It’s the first algorithm in this list that I was 100% confident
      was right. It’s easy to prove that it picks out precisely the
      loop edges: no extra ones, and no missing ones. And it’s
      incredibly easy to implement: you just make a dsf (which I
      already had code for), and then do two simple loops over the
      grid: once to unify regions, and once to check each edge to see
      if it needs to be highlighted. I was convinced I’d finally put
      this long-term annoyance to rest.
Some years later, a friend of mine asked, “Simon, is there any
      chance you could
      make
Net
highlight loops as errors?” Net was one of the very first
      puzzles in my collection, and until this point, I’d never got
      round to going back to it and adding loop
      highlighting
.
Still full of confidence, I said something along the lines of
      “Sure! This will be no problem. I know exactly how to do loop
      highlighting now – I’ve already gone through all the ways to do
      it wrong, and I’ve finally found the right algorithm. It’ll be a
      breeze. I’ll have it done tomorrow.”
Of course, after I said that, you just
know
there had
      to turn out to be a problem! But I don’t feel too bad about it,
      because it was a pretty subtle one.
The problem with Net, compared to all the other puzzles in my
      collection, is that it has a ‘wrapping’ mode, in which the left
      side of the grid is considered to be connected to the right
      side, and the top connects to the bottom. In topological terms,
      this game mode is played on a torus, instead of a region of the
      plane.
A solved Net puzzle in wrapping mode
A torus has a property that makes it fundamentally different
      from a plane or a sphere, known in algebraic topology as a
      ‘nontrivial
H
1
homology group’. This is a
      fancy way of saying that on a torus, it’s possible to have a
      loop that
doesn’t
divide the surface of the torus into
      two separate components. ‘Local’ loops in a small part of the
      torus still do that, but a ‘global’ loop that goes all the way
      around the torus doesn’t, because you can get from one side of
      the loop to the other by walking at right angles to the loop,
      and going all the way round the torus in the
other
direction.
Loop that encloses a small region:
you
            can’t get in or out of the shaded area
Loop that doesn’t enclose anything:
you can
            walk from one side of it to the other
So my face-dsf loop detection algorithm would spot small
      localised loops, but not – for example – a loop that goes off
      the right side of the grid, comes back on to the left, and
      returns to its starting point. And those loops are some of the
      most difficult ones to spot by eye, so it’s
especially
unhelpful that the algorithm can’t point them out to the
      player.
You can walk from above this loop to below it by
        wrapping round the edges of the grid.
So the face dsf
        loop-finding algorithm wouldn’t detect it at all!
This incident is the current holder of my personal record for
      ‘most esoteric mathematical concept that I’ve ever seen cause a
      real software bug’. I’d learned about homology before, but I’d
      imagined it to be one of those abstract theoretical properties
      that you think about in order to prove theorems, but never find
      a practical application. I’d
never
have expected
      homology to be the cause of a bug!
I was quite embarrassed about getting this wrong when I’d been
      so confident. So I wanted to fix the bug in Net quickly.
      Therefore I looked for some kind of small change I could make to
      my existing idea – and found one.
In the previous section, where we saw a loop on a torus and a
      path from one side of it from the other, the path went
      a
long way away
from the loop – all the way round the
      far side of the torus, as far from the loop as you could
      possibly get. But where I showed a genuinely loop-free graph
      with a path from one side of an edge to the other, it would have
      been possible to walk that route staying close to the graph the
      whole time. So my idea was to use that difference to distinguish
      the two cases: find out whether you can reach one side of an
      edge from the other
without going a long way away from any
      edge
.
You can walk to the other side of this
            loop,
but you have to go a long way from the loop to
            do it
You can walk between these points
even if you
            stick close to the graph
Put another way: imagine that each edge of our graph becomes a
      road with a pedestrian footpath down each side, and we’re
      interested in where pedestrians can walk if they stick only to
      the footpaths, and never cross any road.
When multiple edges meet at a vertex, a pedestrian can walk
      between the footpaths on the near sides of an adjacent pair of
      edges, but must cross one of the roads if they want to get to
      any other footpath while staying near that vertex.
A degenerate case of this is that if only
one
edge
      meets a vertex, then its two footpaths count as adjacent to each
      other, so they’re connected.
You can walk between the footpaths facing each
            other.
But you’d have to cross the road to get
            anywhere else.
Special case: a degree-1 vertex, or
            cul-de-sac.
You can just walk round the dead
            end.
If a planar graph contains a loop, then the footpaths on one
      side of the loop are separated from the footpaths on the other
      side. That’s obvious, because the loop separates the
whole
      plane
into two components, and one footpath is on the
      inside and one on the outside. To get from one footpath to the
      other, you
have
to cross the road.
But if a graph doesn’t contain a loop, then all the footpaths
      around its edges are reachable from each other, because whenever
      you get to an endpoint with only
one
edge, you can walk
      round the end of the road and get to the footpath on the other
      side. This is also true of non-loop edges in constructions like
      the ‘dumb-bell’ graph that caused trouble
      in
a previous algorithm
.
Loop edges have different colours (dsf classes) on
        each side.
Non-loop edges have the same colour – even the
        dumb-bell centre.
So the new algorithm is to make a dsf on the segments of
      footpath on each side of each edge. At each vertex of the graph,
      you unify pairs of footpaths around the vertex. Then a graph
      edge is part of a loop iff its two footpaths are not in the same
      equivalence class.
This algorithm still works for planar graphs – and now it works
      for a graph on a torus too. Phew, Net was fixed!
This algorithm works for every puzzle currently in my
      collection – but I could already see a plausible way it might go
      wrong in future.
The footpath dsf technique doesn’t depend on a
      trivial
H
1
homology group. But it does depend
      on the graph being embedded in some kind of surface that
      is
orientable
: if you go round any loop and come back
      to your starting point, you haven’t been ‘flipped over’ so that
      the surface is now in mirror image.
Two well-known examples of
non
-orientable surfaces are
      a Möbius strip, and a Klein bottle. Both of those can be
      represented as a rectangle with opposite edges identified in
      particular ways – and it seemed quite plausible that some day I
      might end up with a puzzle game played on either or both of
      those surfaces.
And on a non-orientable surface, even this algorithm won’t
      work. A loop going all the way round a Möbius strip would return
      to its starting point the other way round, so that the footpaths
      on the two sides of it would become connected to each other –
      and so the algorithm would wrongly conclude that those edges
      weren’t part of any loop.
So this algorithm was fine as an emergency fix, but by now, I
      was convinced that I wanted to avoid depending on any kind of
      topological embedding of the graph at all, if I could.
Update, 2024-09-10
:
      a
comment
      on Mastodon
corrects me. It wasn’t fine: there’s still a bug
      in this algorithm, in the torus case. It won’t
      spot
this
pair of loops, going round the torus at right
      angles, and meeting at a point.
Two loops going round a torus in different
      directions, crossing each other
You can walk between the footpaths on either side of one of
      these loops, by turning at right angles and going round one of
      the footpaths of the other loop. In fact, if you trace round the
      footpaths of this pair of loops, you find they’re all one single
      rectangular footpath. So this algorithm would miss both of these
      loops. Good thing I’ve already moved on to another one!
Tarjan’s bridge-finding algorithm
At this point – much,
much
later than I probably
      should have – I stopped trying to solve the problem from scratch
      myself, and found a solution somebody else had already invented
      and proved correct.
One of the reasons I hadn’t found this algorithm before is that
      it’s phrased the opposite way round. A
bridge
in a
      graph is an edge which is the only way to get between some pair
      of vertices. So if you remove the bridge, those vertices become
      disconnected from each other. On the other hand, a loop edge is
      precisely one which, if you remove it,
doesn’t
disconnect any pair of vertices from each other, because there’s
      still some other route between its two endpoints.
In other words, an edge is a bridge if and only if it
      is
not
part of a loop. I was thinking in terms of
      ‘finding all the loops’, but of course finding all the edges
      that
aren’t
part of a loop is just as good – you just
      invert all the answers once you’re done.
Tarjan’s bridge-finding algorithm starts by finding
      a
spanning forest
of the graph – a
      spanning
tree
of each of its connected components. That
      is, we find a subset of the edges which provide a route between
      any two vertices that the original graph linked, but
      which
don’t
contain any loops.
A demonstration graph. Edges of the spanning forest
        are thicker and darker.
Once we’ve done that, every bridge
must
be one of the
      edges of the spanning forest, because a bridge is the only route
      between some pair of vertices, and whichever vertices those are,
      the spanning forest contains a path between them – so it must
      contain the bridge. So any edge
not
in our spanning
      forest can’t be a bridge – it must be a loop edge instead.
But that’s the easy part. The hard part is that some of the
      spanning-forest edges are
also
loop edges. So the
      problem is to identify which.
The next step is to
root
the spanning forest: for each
      component, choose a vertex (it doesn’t matter which one) to
      consider to be the root of the tree, so that every edge has an
      ‘upward’ direction (towards the root) and a ‘downward’ direction
      (away from it), and the
subtree
of that edge is all the
      vertices further ‘down’. Then an edge
e
is a bridge if
      and only if
nothing in its subtree connects to anything
      outside that subtree
, by any route other than leaving the
      subtree out of the very top, via
e
itself.
The same graph and spanning forest, reorganised so
        that the trees are rooted.
To determine that, you iterate over these rooted trees
      labelling each vertex with a number, in a way that makes every
      subtree into a consecutive interval, say containing numbers
      from
a
to
b
inclusive. Then, for each subtree, you
      find the smallest and largest labels of any neighbour of
      anything in the subtree, say
u
and
v
. From those
      bounds, you can immediately tell whether anything in the subtree
      has a neighbour outside it: if it does, then that neighbour will
      have a label outside the range [
a
,
b
], which will
      either make the smallest reachable label
u
smaller
      than
a
, or make the largest reachable label
v
larger than
b
.
So the edge at the top of the subtree is a bridge if and only
      if
a ≤ u ≤ v ≤ b
, and we’re done!
Vertices are labelled. The red subtree is labelled
      6–10 inclusive.
But the smallest label reachable from it is
      4, outside that range (via the edge from 8).
Therefore the
      blue edge upward from its root vertex 6 is
not
a
      bridge.
What’s wrong with it?
As far as I know, there’s nothing wrong with this algorithm.
      But then, I’ve
believed that before
and been wrong!
That previous time, the problem was that I was depending on an
      extra property of the graph, namely its planar embedding.
      Tarjan’s algorithm definitely doesn’t depend on any such thing:
      it’s a ‘pure’ graph algorithm, requiring nothing except a list
      of neighbours for each vertex. You could run it on a graph
      embedded on a torus, or on a Möbius strip, or even something
      inherently not two-dimensional like a
cubic
lattice in
      three-dimensional space, or
n
-dimensional space if you
      wanted. It wouldn’t care.
So, at the time of writing this, Tarjan’s algorithm lives in
findloop.c
in my puzzles’ source tree, and I
hope
not to discover
      any more fundamental problems that mean I have to throw it away
      and start again!
But after all that…
For one of the above algorithms, I didn’t list
      a
definite
flaw – only a possible one. I didn’t know
      for sure that the
loop tracing
approach wasn’t right, only that I hadn’t
proved
it was
      right. I switched from that to the face-dsf approach because the
      latter was much easier to be certain of.
But, since then, I’ve been thinking about it, and I think that
      with one tiny modification, the loop tracing
      algorithm
can
be proved correct.
The tweak is: when the dsf detects that the edge you’re
      currently adding is part of a loop, and you trace round the loop
      to highlight it, limit your trace to only the
already
      processed
edges – don’t use any edge that your iteration
      has yet to come to.
With that tweak, I’m convinced that this algorithm would
      highlight
every
edge that’s part of any loop at all. We
      can prove this by induction, by showing that at every stage in
      the algorithm that property is true for the set of edges we’ve
      already processed.
At the start of the algorithm, that’s vacuously true: there
      aren’t any loops at all in the set of edges we’ve processed, so
      of course we’ve highlighted all of them. When we find
      the
first
loop, it’s almost as easy: the previous edges
      form an acyclic graph, so if there’s a route between any two
      vertices at all, then it’s the
only
route. So the first
      time the dsf reports an edge as being part of a loop, there’s
      only one possible loop it can be part of, and the tracing step
      must find that one.
The hard case is: what happens later on, when we find an edge
      that has
more than one
path between its endpoints?
If there’s more than one path in a graph between two
      vertices
u
and
v
, then imagine taking the
      ‘symmetric difference’ of any two of them, eliminating edges
      common to both, and keeping only the edges in exactly one of the
      loops. This symmetric difference is a subgraph in which every
      vertex has even degree, which means its edges are the union of
      some set of loops. But, by the inductive hypothesis, that means
      we’ve already highlighted all of
those
edges. So the
      only possible
new
loop edges we haven’t highlighted yet
      are the ones that don’t appear in any such symmetric-difference
      graph – because they’re part of
every
possible route
      between
u
and
v
. And
those
edges are
      bound to be found by our current tracing step.
So if I’d only had that idea 19 years ago, I could have stopped
      there
4
!
However, Tarjan’s algorithm surely has better performance,
      because it processes each edge a bounded number of times. This
      tracing approach might need a full search of the graph every
      time it traces a loop. So the extra work wasn’t totally a waste
      – plus, it gave me this story to tell.
With any luck, you should be able to read the footnotes of this
      article in place, by clicking on the superscript footnote number
      or the corresponding numbered tab on the right side of the page.
But just in case the CSS didn’t do the right thing, here’s the
      text of all the footnotes again:
1.
I think, pedantically speaking,
      ‘disjoint-set forest’ refers to a specific
technique
for solving the problem of incremental equivalence tracking,
      whereas the other names without ‘forest’ in them refer to
      the
problem itself
without committing to a particular
      solution – in the same way that the Fast Fourier Transform is
      one particular algorithm for implementing the abstract
      mathematical operator called the Discrete Fourier Transform. In
      both cases, the distinction is often ignored, because the
      well-known algorithm is such a good way to solve the problem
      that nobody ever really wants to use a different
      one.
2.
Since then,
      Loopy has been enhanced further, so that not all the tilings are
      even
periodic
. You can also play Loopy on a fragment of
      Penrose tiling, or the Hat and Spectre tilings discovered in
      2023. I have a whole
series
of other articles about that!
3.
In one sense, Net doesn’t
      exactly
need
loop highlighting. In Net, the solution to
      the puzzle is an acyclic graph connecting all the squares of the
      grid. And if you manage to make any graph at all that connects
      all the squares, it
can’t
have a loop, because a graph
      on that many vertices with a loop would have the wrong number of
      edges, and the Net user interface doesn’t let you change how
      many edges exist. So if you do make a loop, you’ll find you
      can’t light up all the squares of the grid, so it will at least
      be obvious why the game doesn’t think you’ve won. But that
      doesn’t give you any help
finding
the loop – all it
      proves is that there must be one somewhere. So highlighting it
      is still useful for that.
4.
In fact, going back and looking
      at my original path-tracing code, it traced round the loop by
      the maze-solving technique of ‘keeping one hand on the wall’. So
      the way I actually wrote it, it also depended on having a planar
      embedding of the graph. To get the same generality as Tarjan’s
      algorithm, I’d have had to replace that with a general path
      search like BFS or DFS. But that wouldn’t have been
      hard.
