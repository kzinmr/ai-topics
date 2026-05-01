---
title: "Two algorithms for randomly generating aperiodic tilings"
url: "https://www.chiark.greenend.org.uk/~sgtatham/quasiblog/aperiodic-tilings/"
fetched_at: 2026-05-01T07:00:58.457864+00:00
source: "chiark.greenend.org.uk/~sgtatham"
tags: [blog, raw]
---

# Two algorithms for randomly generating aperiodic tilings

Source: https://www.chiark.greenend.org.uk/~sgtatham/quasiblog/aperiodic-tilings/

Two algorithms for randomly generating aperiodic tilings
[Simon Tatham, 2023-04-10]
[Part of a series:
Penrose and hats
|
Spectres
|
finite-state transducers
|
more transducers
|
refining tilings
]
Introduction
In the 1970s, Roger Penrose discovered several sets of polygons
      which will tile the plane, but only
aperiodically
,
      without the tiling repeating in a fixed pattern.
Samples of his two best-known tiling types, called P2 and P3,
      are shown below. P2 is composed of quadrilaterals usually
      referred to as ‘kite’ and ‘dart’; P3 is composed of two sizes of
      rhombus, known as ‘rhombs’ in this context for some reason:
P2 tiling: kites and darts
P3 tiling: thin and thick rhombs
(Strictly speaking, any one of these polygons
can
tile
      the plane periodically, because so can any quadrilateral at all.
      The tiling is only forced to be aperiodic if you restrict the
      ways the tiles can connect. You could do this by putting
      jigsaw-piece protrusions and holes on the edges, but that’s
      ugly, so people normally prefer to show the plain quadrilaterals
      and let the matching rules be implicit. In this article I’ll
      ignore this detail just like everyone else.)
In 2023, a long-open question was answered: can you force
      aperiodicity in the same way using only
one
type of
      tile, instead of Penrose’s two? You can! The shape in question
      is described as a ‘hat’ by its discoverers Smith, Myers, Kaplan
      and Goodman-Strauss, and a sample of its tiling is shown
      below:
Hat monotiling
(There’s a quibble with this one too: the hat shape is
      asymmetric, and in order to tile the whole plane, you need to
      use it in both handednesses. For some purposes this still means
      you need two types of tile! But from a mathematical perspective
      it’s more natural to regard reflections as not a fundamentally
      different shape.)
One of the games in my
puzzle
      collection
, namely “Loopy” (also known as Slitherlink), can
      be played on a lot of different tilings of the plane. Most of
      them are periodic, but all three of these aperiodic tilings are
      also perfectly feasible to play Loopy on. So the question
      arises: how do you best get a computer to generate pieces of
      these tilings?
One really obvious option would be to pre-generate a fixed
      patch of each tiling, and set Loopy puzzles on that by just
      varying the puzzle solution (the closed loop you’re trying to
      reconstruct from clues). But that’s boring – surely the whole
      point of a tiling that
does not repeat
is that it
      shouldn’t be the same every time! So when you request a new
      game, you should get a different patch of the
tiling
      itself
, as well as a different loop to find in it.
So our mission goal is:
given an output region and a source
        of random numbers, generate a randomly selected patch of each
        of these three aperiodic tilings.
In this article I’ll discuss two very different algorithms for
      doing this, and say which one I prefer. (Spoiler: there will be
      a very definite one that I prefer.)
Substitution systems
All three of the tilings we’ll discuss here can be generated
      recursively by the same basic method.
For each of these tilings, there’s a system for starting with
      an existing tiling, and then substituting each tile for smaller
      tiles according to a fixed rule. This generates a new tiling,
      using the same set of tiles, but more of them at a smaller
      scale.
Because the output tiling is of the same type, it follows that
      you can substitute that in the same way, and so on. So if you
      repeat this many times, you can start from a single initial tile,
      and expand it into as large a region of the plane as you like.
One slight complication, in every case, is that the most
      convenient substitution system is not based on the actual tiles
      you want to end up with. In each case, you have to substitute
      a
different
system of tiles, and after you’ve done that
      enough, convert the result into the final tiles you want as
      output.
Penrose tilings: half-tile triangles
The substitution systems for the Penrose P2 and P3 tilings work
      in very similar ways, so I’ll describe both of them
      together.
In both cases, the most convenient way to think of the
      substitution system is to imagine each of the starting tiles
      being divided in half, to make two isosceles triangles. That
      way, the substitution can replace each of those triangles with
      either two or three smaller triangles, exactly filling the same
      area as the original triangle. (If you didn’t do this, then most
      smaller tiles would half-overlap two larger tiles, and it would
      be more awkward to keep track of which tiles you’d expanded from
      where.)
The divisions for each tile type look like this. For the P2
      tiling, the kite and dart are each divided down their line of
      symmetry. For the P3 tiling, the thin rhomb is cut along its
      short diagonal, and the thick one along its long diagonal:
P2 tile divisions
P3 tile divisions
(Therefore, in the P2 tiling, the acute isosceles triangles are
      larger than the obtuse ones, whereas in the P3 tiling,
vice
        versa
.)
The two halves of each original tile are shown in different
      colours, because they will be treated differently by the
      substitution rules. Specifically, they will be mirror images of
      each other.
Here are the substitution rules for each of those types of
      triangle:
To see the complete system in action, select the radio buttons
      below to see the effect of running a different number of
      iterations, starting from a single obtuse triangle of each
      tiling. In each step, you can see that every large triangle
      transforms into smaller ones in accordance with the rules
      above.
Interactive demo of iterated P2 and P3 substitution
So one way to generate Penrose tilings is to expand a starting
      triangle like this, and when you’ve expanded it enough times,
      glue each pair of adjacent half-tiles back together into a
      single kite, dart or rhomb.
Hat tiling: a system of four metatiles
The hat tiling can also be generated by a substitution system.
      In this case, however, the system is based on a set of four
      tiles that have no obvious relation to the actual hat shape!
The paper refers to these as “metatiles”, to avoid confusion
      with the hat itself (the single
tile
). The four
      metatiles are shown below, with their substitution rules:
Hat metatile substitution rules
The arrows on three of the metatile types indicate orientation:
      those three metatiles are symmetric, but in the final conversion
      to hats, each one will generate an entirely asymmetric pattern
      of hats. So the substitution process has to remember what every
      metatile’s orientation should be, in order not to get the last
      step wrong.
(The remaining metatile is already asymmetric, so it doesn’t
      need an arrow.)
In these substitution diagrams, the area of the original large
      metatile is completely covered by the smaller ones, and the
      smaller ones also overlap the edges. This means that when two
      metatiles are placed next to each other, their expansions will
      overlap too. In fact, they will always overlap in a way that
      causes some of the resulting metatiles to coincide.
Here’s an illustration of the expansion in action, expanding a
      single starting metatile for a few levels of recursion:
Interactive demo of iterated hat metatile substitution
So, similarly to the previous section, if you want to generate
      a large patch of hat tiling, you can start with a single
      metatile and expand it repeatedly until you think it’s big
      enough. Finally, each metatile is converted into either 1, 2 or
      4 hats according to the following rules:
Rules for converting hat metatiles to hats
(Incidentally, the hat in the centre of the cluster of four
      expanded from the hexagonal metatile, shown here in the darkest
      red colour, is the only one of these hats that is reflected
      compared to the rest. So you can readily identify the rare
      reflected hats in this tiling, if you’re generating it using
      this metatile system.)
However, beware! The final expansion step isn’t quite as easy
      as it looks, because the expansion into hats
      is
distorting
.
As I’ve drawn the metatiles here, the substitution of one set
      of metatiles for a smaller set is geometrically precise: each
      large metatile from one iteration of the algorithm can be
      overlaid on the next iteration and the vertices will align
      exactly as shown in the diagrams above. But when each metatile
      expands into a cluster of hats, the clusters aren’t quite
      exactly the same sizes as the metatiles they replace. So the
      precise positions in the plane will vary in a nonlinear way, and
      there’s no simple formula that matches a metatile’s
      coordinates to the coordinates of its hats.
The paper offers an alternative version of this scheme in which
      the smallest level of metatiles
do
match up
      geometrically to the hats they turn into – but in that version,
      the downside is that each size of metatiles is not precisely the
      same shape as the next size. Instead, the metatiles themselves
      gradually distort as they expand.
Either way, this makes it more difficult to perform the overall
      procedure. With the fixed-shape metatiles as shown here, in the
      final conversion to hats, you can’t just iterate over each
      metatile and independently write out the coordinates of its
      hats; with the alternative version, you have the same problem
      during the expansion of metatiles into smaller ones. In each
      case, you have to do some kind of a graph search (breadth-first
      or depth-first, whichever you find easiest), choosing one
      metatile to start with and processing the rest in an order that
      guarantees that each metatile you process is adjacent to one
      you’ve already placed. That way you can figure out the location
      of each output hat or metatile, by knowing of an existing
      adjacent thing it has to fit together with.
Here’s an example, which also illustrates the distortion. This
      shows the same set of metatiles as in step 2 of the iteration
      above, and its expansion into hats. The top left corners of the
      two images are aligned – but you can see that at the other end,
      the corresponding pieces of tiling are quite offset from each
      other.
Interactive demo of converting hat metatiles to hats
Choosing a random patch from a fixed expansion
In the previous section, I’ve shown how all three of our
      aperiodic tiling types (P2, P3, hats) can be generated by
      repeated subdivision of a starting tile, followed by a final
      postprocessing step. (In the two Penrose cases, gluing
      half-tiles back together into whole ones; in the hat case,
      substituting the four metatiles for their hat clusters.)
This is all very well if you want to generate a
fixed
piece of tiling. But what if you want a different piece every
      time?
One obvious answer is:
make a fixed patch of tiles much
        larger than you need, and select a small region from it at
        random.
This works basically OK in principle. But if you implement it
      naïvely, it’s very slow, because you spend a lot of effort on
      generating all the fine detail in huge regions of the tiling
      that you’re just going to throw away. And the more uniform a
      probability distribution you want for your output region, the
      larger the fixed region you have to generate, and the more
      pointless effort you waste.
We can save a lot of that effort by not being quite so naïve
      about the procedure. Suppose that, instead of generating a patch
      of tiling and
then
deciding which part of it to return,
      we instead decide
in advance
where our output region is
      going to be within the starting tile. Then, in
each
      iteration
, we can identify a tile that’s completely outside
      the output region and won’t contribute any tiles to it, and
      discard it early, before we waste any more time expanding it
      into lots of subtiles that will all be thrown away.
For example, here’s an illustration of how much work this might
      save when selecting a small rectangle from the same P3 example
      pictured above:
Interactive demo of P3 substitution pruned for the target area
At every stage, we identify triangles – large or small – that
      are out of our region, and stop bothering to expand them any
      further. This bounds the wasted effort at a much more acceptable
      level. Compare the number of triangles in the final pruned
      output with the number in the unpruned version!
This technique is easy to apply for Penrose tilings, because
      the expansion process is geometrically exact. At every stage of
      the process, the outline of each triangle is exactly the
      boundary of the region that will contain all its eventual output
      tiles. So it’s easy to identify
whether
a triangle
      intersects the target region.
But in the hats tiling, where the expansion process is
      geometrically distorting, it’s not so easy. In order to work out
      whether a given metatile is going to contribute to your target
      region, first you have to work out what coordinates in the
      current layer of metatile expansion
correspond
to the
      target region in the final hat tiling. This is computationally
      tricky: even if you could find an exact formula that translates
      each
corner
of your target region into its coordinates
      at the current iteration, then you’re not done, because it’s
      also not guaranteed that the image of a straight line between
      two of those corners will still be straight after the distortion
      is applied. In other words, if you’re trying to construct a
      patch of hats to fill a specific rectangle, you might find the
      region of metatiling you need to keep isn’t even
      rectangular!
It might be possible to get this technique to work regardless,
      by computing a conservative approximation to the target region.
      That way maybe you do a
little
more work than you need,
      computing a few metatiles that never contribute hats to the
      output but your approximation couldn’t quite prove it; but the
      effort saving would still be large compared to the naïve
      approach. But this is likely to be tricky, and has plenty of
      room for subtle bugs. Err in one direction, and you do more work
      than you need; err in the other direction and you generate wrong
      output.
This entire approach has another downside. As I mentioned
      above, if you want your random patch of tiling to be
      selected
uniformly
from the limiting probability
      distribution of finite pieces of tiling over the whole plane,
      then you can’t achieve it this way, in an exact manner. You can
      only approximate, by running a large enough number of iterations
      that the huge patch you’re selecting a rectangle from is
      close
enough
to that limiting distribution. And the
      closer you want the distribution, the more you have to expand,
      and the more work you have to do.
More subtly, this means you have to figure out
in
        advance
how many iterations you want to run, based on the
      size of your target region and the error threshold you’re
      prepared to tolerate in probability distribution. That
      involves a fiddly formula which is easy to get wrong,
      introducing subtle bugs you’ll probably never spot.
In the next section, I’ll describe a completely different
      approach that avoids
all
these problems, and works for
      hats as easily as it does for Penrose tiles.
Combinatorial coordinates
The alternative approach begins with the following observation.
Suppose that, in any of these recursive substitution systems,
      whenever we substitute one larger tile for a number of smaller
      ones, we assign a different label to each smaller tile.
For example, in the P2 tiling, an acute triangle expands into
      three smaller triangles; so we could number them 0, 1, 2 in some
      arbitrary but consistent way. And an obtuse triangle expands
      into just two, which we could call 0 and 1. Or, perhaps more
      elegantly, we can observe that no two triangles expanded from
      the same larger triangle are the same type (counting reflections
      as different), so we could simply label each triangle by one of
      the four types (two types of acute, two types of obtuse).
For the metatiles in the hat system, each metatile has between
      7 and 13 children, and some of them are the same type as each
      other. So the problem is larger – but not more difficult. We can
      still just assign each child a numeric label in an arbitrary
      way, so that the hexagonal metatile has children labelled from 0
      to 12 inclusive, the triangle from 0 to 6, etc.
Then, after you’ve run the expansion process some particular
      number of times, each tile of the output can be uniquely
      identified by the sequence of labels it generated as it was
      expanded. You could identify some particular tile by saying
      something like: “From the starting tile, take the child
      with
this
label; from there, take the child
      with
that
label, then the child with
the other
label, …” and after you’ve listed the label at every step of
      the expansion, your listener knows exactly how to find the same
      tile you were thinking of.
Now, supposing I tell you the coordinates of one particular
      output tile, specified in this way. Can you figure out the
      coordinates of one of its
neighbours
, sharing an edge
      with it?
Assuming the tile you want is not on the very edge of the giant
      starting tile, yes, you can. And you can do it entirely by
      manipulating the string of labels, without ever having to think
      about geometry.
Penrose tilings: indexing triangle edges
We’ll tackle the Penrose tilings first. In this system, the
      smallest unit we ever deal with is a single half-tile triangle,
      so we’ll assign coordinates to each of those.
I’ll label the tile types with letters. For the P2 tiling, the
      two handednesses of acute triangle are called A and B; for the P3
      they’re C and D. The obtuse triangles in P2 will be U and V; the
      ones for P3 will be X and Y.
Here’s an illustration that shows the coordinates of each
      output triangle for the first few layers of expansion, in both
      tiling types. The coordinates are written with the label of the
      smallest triangle first, followed by its parents in increasing
      order of size. (This matches the natural way to store them in an
      array, because that way, the fixed array index 0 corresponds to
      the real output triangles.) So whenever a triangle is divided
      into two or three smaller triangles, the coordinates for each
      smaller triangle are derived from the original triangle by
      appending a new type label to the
front
.
Interactive demo of iterated P2 and P3 substitution with combinatorial coordinates
We’ll also need to index the
edges
of each triangle in
      a unique way, so as to describe unambiguously which neighbour of
      a triangle we’re going to ask for. For example, we could say
      that we always assign index 0 to the base of the isosceles
      triangle, and the two equal sides are assigned indexes 1 and 2,
      in anticlockwise order from the base. So when you want to know
      about a particular neighbour of your starting tile, you’ll
      identify which neighbour by giving the index of an edge: “What
      triangle is on the other side of edge {0/1/2} of my current
      one?”
Then, for each substitution rule, we can make a map of which
      smaller triangles border on which others, and which of their
      edges correspond:
P2 substitution rules, with edge and type labels
P3 substitution rules, with edge and type labels
From these maps, with a little
      recursion, you can work out everything you need.
For example, suppose you’re in a type B triangle, and you want
      to see what’s on the other side of its edge #0. Look at the type
      of its parent triangle. If the parent is type A or type U, then
      the maps above for those triangle types show that edge #0 of the
      type-B sub-triangle is also edge #1 of a type-U triangle. So you
      can adjust the lowest-order label in your coordinate list to
      specify a different sub-triangle, and return success.
More symbolically:
to move across edge #0 of any triangle
        whose coordinate string begins with BA or BU, just replace the
        initial B with a U.
On the other hand, suppose your type-B triangle is expanded
      from
another
type-B triangle. In that case, the map for
      the parent triangle says it doesn’t know what’s on the far side
      of your edge #0 – that’s off the edge of the map.
But that’s all right: recurse further up to find a map on a
      larger scale! We know that going out of edge #0 of the smaller
      type-B triangle means going out of edge #1 of the larger type-B
      triangle. So ask the same type of question one layer further up
      (perhaps recursing again, if necessary).
When the recursive call returns, it will give you an entire
      updated set of coordinates identifying the
second
smallest triangle you’re going to end up in, and which edge of
      it is on the other side of this one’s edge #1. So, finally, you
      can append the lowest-order coordinate to that, by figuring out
      which of the
smaller
triangles of the new large
      triangle is the one you need to end up at.
In our example case, there’s one final step. Going out of edge
      #0 of our original B meant going out of edge #1 of the larger B.
      But that edge is divided into two segments, each belonging to a
      different sub-triangle. So we need to remember
which
segment of the larger edge we were crossing: were we to the left
      or the right of the division?
We’ll always expect to find that the incoming edge of the new
      large triangle is subdivided into segments in the same way, and
      the map for that triangle will let us find which sub-triangle
      corresponds to each segment of the outer edge. So you can still
      figure out which sub-triangle you end up in.
For example, suppose we had coordinates ending BB, and our
      recursive call (“we’re going out of edge #1 of a B, what happens
      next?”) rewrote the second B to an A (perhaps modifying further
      labels above that) and told us we were coming in along edge #2
      of the A. Then we consult the A map, and we see that its edge #2
      is indeed divided in two, and coming in via the right-hand one
      of those segments leads us in the A child. So we end up with AA
      as our new lowest-order coordinates (plus whatever rewrites
      were made at higher orders by the recursion).
(You can check these examples in the expansion shown above. In
      the 3-iteration P2 diagram, there are triangles labelled BABU
      and BUUU, and as described above, the edge #0 of each one – that
      is, its short base edge – connects to UABU or UUUU respectively,
      with only the lowest-order label differing. But the triangle
      labelled BBBU is a more difficult case, requiring a rewrite at
      the second layer: its edge #0 connects to a triangle labelled
      AABU.)
Hats: indexing kite edges, and dealing with non-uniqueness
For the hats tiling, indexing the edges of the tiles isn’t
      quite so convenient. The hat polygon itself has 13 edges, and
      the maps for which ones border on each neighbouring hat are
      pretty complicated. Not only that, but because the metatile
      expansions overlap each other, every tile potentially has
      multiple different, equally legal, lists of coordinates. And the
      metatiles don’t necessarily meet edge-to-edge, in the sense that
      one edge of
this
metatile might join up with the edges
      of two other metatiles.
To solve the first of those problems, I found the easiest thing
      is to stop considering a whole hat at a time, and use a smaller
      and more regular unit. The hat tiling can be made to align
      neatly with a periodic tiling of the plane with kites, shaped so
      that six of them joined at the pointy ends make a regular
      hexagon and three joined at the blunt ends make an equilateral
      triangle:
A hat aligned to its underlying grid
If you align the hats to this tiling, then every hat occupies
      exactly eight whole kites, as shown above. And the kites are
      simply shaped, with just four edges. So I found it’s easier to
      consider each
individual kite
to have a set of
      combinatorial coordinates, and to devise an algorithm that will
      tell you the coordinates of a neighbouring kite, given the
      coordinates of the starting kite and which of the four edges you
      want to head out of.
The coordinates of an individual kite look something like this:
“I am the
k
th kite in a hat …
which is the
h
th hat expanded from a first-order
      metatile of type
m
…
which is the
c
th child of a second-order
      metatile of type
m
2
…
which is the
c
2
th child of a third-order
      metatile of type
m
3
…”
and so on. At the highest-order end, this terminates with you
      knowing the outermost metatile
type
, but not anything
      about its parent, or which child of that parent it might be.
To navigate this coordinate system, we’ll make a set of giant
      lookup tables. But first, we’ll have to assign numeric indexes
      to all three of the expansion processes involved: metatiles to
      smaller metatiles, then to hats, then to kites. It doesn’t
      matter how we do this, as long as we do it consistently.
Metatiles with child metatile indexes
Metatiles with hat indexes
Single hats with kite indexes
The first type of lookup table we’ll need, I call
      a
kitemap
. For each type of second-order metatile (i.e.
      each possible value of
m
2
), you expand it into
      its set of first-order metatiles, and then into hats, and then
      into kites, and you keep the coordinate labels you generated at
      each stage. To illustrate this, here’s the kitemap for the
      triangular metatile. (It makes a manageable example, because it’s
      the smallest. The others are similar but larger.)
Interactive demo of building one of the four kitemaps
From this visual map, you can read off the coordinates of each
      kite adjacent to a starting kite. For example, consider the kite
      labelled 7.3.0, at the top left of the central hat in this
      diagram: you can see that the four kites bordering it are 0.0.0,
      6,3,0, 3.1.3 and 4.1.3, and you can identify which edge of the
      kite takes you to each of those neighbours. So if the
      coordinates of your current kite started with
      (
k
,
h
,
c
) = (7, 3, 0), then you would know
      how to generate the coordinates of each neighbouring kite,
      simply by rewriting those three low-order labels.
The version of the kitemap used by the algorithm is not a
      visual map like this: it’s a lookup table, or rather one for
      each of the four metatile types. Each table is indexed by the
      triple (
k
,
h
,
c
) and a particular kite
      edge, and it tells you the new values of
      (
k
,
h
,
c
) corresponding to the kite on the
      far side of that edge.
So, to compute the coordinates of a neighbouring kite, you
      start by choosing the kitemap lookup table corresponding to the
      metatile type
m
2
, and look up
      (
k
,
h
,
c
, kite edge) in it. If it has an
      answer, you’re done – just replace the three low-order indices
      in your input coordinates with the ones you got out of the
      kitemap lookup table, and you’ve got a set of coordinates for
      the new kite.
(Of course, when you rewrite
c
in the coordinates, you
      must also rewrite
m
to match the type of the new
      first-order metatile. To do this, you just need a much simpler
      lookup table of which type of metatile each child is.)
But sometimes this doesn’t work. For example, suppose you’re in
      the kite labelled 0.0.4 in the above map, right at the bottom.
      Then traversing one of the four kite edges will take you inwards
      to 1.0.4, but for the other three, this map has no answer. In
      cases like this, the entry in the kitemap lookup table for “what
      happens if I head in
this
direction
      from
here?
” will be a special value meaning “don’t
      know, that’s off the edge of the map.”
By analogy with the Penrose case, an obvious thing to try here
      might be to specify (in some way)
which edge
of the
      kitemap you’re stepping off, and then recurse to a higher layer
      to find out where you’ve come back in to some other kitemap. If
      we had made smaller kitemaps based only on a
      single
first
-order metatile (i.e. just containing 1, 2
      or 4 hats), then we would have no choice but to do exactly this,
      because all first-order metatiles’ hat expansions are disjoint.
      But hat expansions of metatiles have extremely twiddly and
      complicated edges, and that sounded like a very tricky thing to
      get right.
And we don’t have to! There’s a nicer way, based on the fact
      that the metatile expansions overlap each other. If we’re about
      to head off the outermost border of the kitemap, that must mean
      that we’re near the edge of the expansion of our second-order
      metatile
m
2
. So the
first
-order
      metatile we’re in must be one of the outermost metatiles in that
      expansion – which means it overlaps with the expansion of
      another second-order metatile, or maybe even two of them. And
      among the second-order metatiles whose expansions contain this
      particular first-order one, there must be at least one in which
      we’re about to step
inwards
towards the centre, not
      outwards towards the edge.
In other words, the fact that there are multiple valid
      coordinates for the same kite is not a problem after all. It’s
      an opportunity! If we can rewrite two layers
      of
metatile
child index in our coordinate system, then
      we can find an
equivalent
representation of our current
      kite, which places it in a kitemap that we’re not about to step
      off the edge of. And now we’ve completely avoided having to deal
      with those long crinkly complicated edges of all the maps.
To implement this step, we make a second type of map, which I
      call a
metamap
. This time, take
      each
third
-order metatile type
m
3
,
      and expand it twice, into second- and then into first-order
      metatiles. As you do that, keep track of all the different ways
      that each first-order metatile is generated (there will be more
      than one if it’s in the overlap between the expansions of two or
      three second-order metatiles). So we end up with a map in which
      some metatiles have multiple coordinates:
Interactive demo of building one of the four metamaps
Finally, we translate that map into a lookup table indexed by
      any of the coordinate pairs in this diagram, giving all the
      other coordinate pairs equivalent to it. This lookup table
      allows you to rewrite the part of the coordinate system that
      says
“… metatile type
m
, which is
      child
c
of type
m
2
, which is
      child
c
2
of
m
3
…”
by selecting the metamap for tile type
m
3
,
      and looking up the pair (
c
,
c
2
) in it.
      The metamap might return you one or two alternative
      (
c
,
c
2
) pairs, and for each one, you
      can substitute those in your coordinates (which doesn’t change
      which kite you’re referring to). This will also give you a new
      value of
m
2
, so you’re representing your
      existing location relative to a different kitemap which overlaps
      the previous one. Now you can try looking up your new
      (
k
,
h
,
c
) triple in it (using the rewritten
      value of
c
), and this time, perhaps you’re not on the
      edge of the map any more, and can find the coordinates of the
      neighbouring kite successfully.
If even
that
doesn’t work, it’s because you’re on the
      outer edge of the metamap, meaning you’re near the edge of the
      expansion of the third-order metatile
m
3
.
      And
now
every layer above this looks the same – so you
      can try applying the same kind of metamap rewrite one layer up,
      by looking up (
c
2
,
c
3
) in
      the metamap for
m
4
and seeing if that permits
      a more useful rewrite one layer down. If even that doesn’t help,
      try further up still, and so on.
Making it up as you go along
In both of the previous sections, I’ve described a technique
      for computing the coordinates of each smallest-size element of
      the tiling (a Penrose half-tile, or a single kite), using a
      recursive algorithm which looks at higher- and higher-order
      labels in the coordinate system as necessary.
Of course, there’s one obvious way this can fail. You can only
      store a finite number of coordinates. What if the recursion tries
      to go all the way off the top, and look at a higher-order
      coordinate than you have
at all?
One obvious option is:
report failure
. If for some
      reason you had decided in advance that you were
only
interested in some specific fixed patch of tiling, and that
      nobody should ever go beyond the edges of that at all, then a
      failure of this type should be interpreted as “Clonk! You have
      run into the wall, and can’t go that way.”
(Perhaps if you had decided to set a text adventure game in the
      7-level expansion of a type-A Penrose half-tile, or something
      along those lines, then this might be what you’d actually want!
      Each individual triangle would correspond to a room, and not all
      rooms would have exits in all three directions.)
But in the main situation I’m discussing here, we don’t ever
      want to report failure. Our aim is to generate a randomly
      selected patch of tiling to cover a particular target rectangle.
      Just because that rectangle turns out to protrude over the edge
      of the highest-order tile we currently know about doesn’t mean
      there’s
no possible way
to extend the tiling in that
      direction; it just means we haven’t yet made a decision
      about
which
way to extend it.
If you imagine an infinite tiling of the
entire plane
in any of our tiling systems, then in principle, any given
      element has a set of coordinates that go on
forever
to
      higher- and higher-order, larger and larger, supertiles. If we
      had started by inventing an
infinite sequence
of
      coordinates for our starting element, then there would be no
      problem with running out of coordinates during the recursion –
      we could recurse as high as necessary.
Of course, you can’t invent infinitely many things up front in
      a computer. But what you
can
do is to invent them
lazily
, by inventing the first few, and being prepared
      to generate a new one as and when it’s requested.
So this is what we do. In our algorithm, we invent some random
      coordinates of our original starting element, up to a certain
      point. And then, if the recursion ever tries to go beyond the
      level we know about, we simply invent another layer, on demand,
      append it to the coordinates of the starting element,
      and
pretend it was there all along
, and that our
      starting element has
always
had that extra coordinate.
      So if any other coordinate list lying around elsewhere in the
      software is shorter than the current coordinates of the starting
      position, then we can extend it by appending the extra elements
      that have been appended to the starting position since it was
      generated. (Because it has the semantics “When we last got here,
      we didn’t know what the next few levels looked like, but now we
      do know”.)
Of course, when you make up a parent coordinate at random, you
      have to make it consistent with the rules about which tiles can
      be parents of which other tiles. In the Penrose system, for
      example, you can see from the maps in a previous section that
      the type-B triangle can be a child of A or U or another B, but
      it can’t be a child of a V. So if your current topmost tile type
      is B, then you must select the next one up by randomly choosing
      from the set {A, U, B}, and not from all four tile types.
      Similarly in the hats system, not all metatiles can appear as
      children of other metatiles: the triangular
      metatile
only
appears in the expansion of the hexagonal
      one, so if your current topmost metatile is a triangle, then you
      only have one choice for what the next larger one will be. And
      even if your current metatile occurs as a child of
all
the metatile types, you also have to decide what its child index
      will be relative to its parent, and that index must be chosen in
      a way that matches the tile types.
Better still, once you’ve finished generating your output patch
      of tiling, you can retrieve the full set of coordinates you
      ended up having to invent for the starting position – and those
      can act as a short and convenient identifier that allows another
      person running the same algorithm to generate the identical
      piece of tiling, because
they
should never find
      themselves needing a coordinate you hadn’t already generated.
      That would only happen if they tried to extend your tiling into
      a larger region than you had tried yourself.
Another thing you can do here is to choose the next parent
      using a deliberately biased probability distribution, to match
      the limiting distribution over the whole plane.
In each of these tiling systems, there’s a system of linear
      equations that tells you how many tiles of each type you have
      after an expansion, if you know how many tiles of each type you
      started with. By eigenvalue/eigenvector analysis, you can
      process these equations to determine the proportions of the
      various tile types occurring overall – or, more precisely, the
      limit of the proportions in a very large finite patch, as the
      patch size tends to ∞.
This overall distribution of tile types, in turn, can be
      processed into a set of
conditional
probabilities, each
      answering a question of the form “Of all the tiles of
      type
t
in the plane, what proportion are child #
n
of tile type
u
?” So if you work out all those
      probabilities, then you can select the next coordinate pair
      (
n
,
u
) in a way that matches that limiting
      distribution.
(Also, when you randomly select your
initial
tile, you
      should do it according to the original, unconditional, version
      of the limiting distribution.)
The effect of this refinement is that our piece of tiling will
      be generated as if the coordinates of the starting element had
      been chosen
uniformly at random from the whole plane!
That’s normally a meaningless concept, but in this case it (just
      about) makes sense, because the number of output patches of
      tiling you could possibly return is finite, and the distribution
      of
those
converges to a limit if you choose uniformly
      from larger and larger regions of the plane.
Compare this to the recursive-expansion technique for
      generating tilings. In that technique, your output distribution
      is – by construction – the one you’d get by choosing from
      an
actual
fixed patch of tiling of a finite (if large)
      size, because that’s exactly what you
are
doing. If you
      start from a larger and larger patch, your output
      distribution
approaches
the idealised limit, but in
      order to get it closer and closer, you have to do more and more
      work. Here, we can directly generate a tiling
      from
precisely
the limiting distribution, and we didn’t
      have to do any extra work at all to get there!
Generating the output tiling
So, now we have a method for moving around a tiling and
      determining a string of coordinates describing each
      smallest-sized element we come to. What do we
do
with
      that?
Our ultimate aim is to actually generate a set of tiles that
      cover the specified target area. For this, we don’t really need
      the full set of higher- and higher-order coordinates at all. We
      only need to know the lowest-order tile type labels: enough to
      know
which kind of thing appears next in the tiling.
Those low-order labels are the
output
of the algorithm.
      The higher-order parts of the coordinate system are just an
      internal detail of how the algorithm keeps track of where it had
      got to. (Also, as I mention in the previous section, they can
      also act as an identifier to make a particular run
      repeatable.)
So, to use this technique to actually generate a Penrose
      tiling, a simple approach is to use a graph search (say,
      breadth-first). Pick an initial starting triangle, and place it
      somewhere in your target area (the centre is an obvious choice,
      but anywhere will do). Then, repeatedly, find some triangle edge
      that you don’t know what’s on the other side of yet, and compute
      the combinatorial coordinates of the triangle on the other side,
      by starting from the coordinates of the triangle you already
      have. The lowest-order label in the new triangle’s coordinates
      will tell you which shape of triangle it is (acute or obtuse),
      and which of its edges corresponds to the edge you just
      traversed. That’s enough information to calculate the
      coordinates of the new triangle’s third vertex, starting from
      the two endpoints of that edge. Now add the two new edges of
      that triangle to your queue of edges to try later. Then go back
      and pick another edge to explore, and so on.
At every stage, if you generate a triangle that’s completely
      outside the target area, there’s no need to store it or to queue
      up its other edges. If you discard out-of-bounds triangles as
      you get to them, then this search process will eventually
      terminate, because the queue of edges that still need exploring
      has run out, and you’ve covered the whole target region in
      half-tile triangles.
Every time you generate the coordinates of a triangle, you find
      out which of the
four
triangle types it is: not just
      whether it’s acute or obtuse, but also which
handedness
it is. So you know which half of an output tile each triangle
      is. Therefore, as you go along, you can also generate the full
      output Penrose tile corresponding to every triangle. This will
      generate most of them twice (any tile with both halves inside
      the target area), but as long as you notice that and
      de-duplicate them, that’s fine.
For generating the hat tiling, you
could
do the same
      kind of thing – but there’s an even easier approach that doesn’t
      need a graph search at all, using the fact that the whole tiling
      lives on a fixed grid of kites.
For the hat tiling, the easiest approach is to specify your
      target region as a connected set of kites, and simply iterate
      over that set in some fixed way. For example, to fill a
      rectangular region, you might process the kites in the region in
      raster order, iterating along each row from left to right and
      then going on to the next row. Or you might find it easier to
      process alternate rows in opposite orders. As long as you
      process the kites in an order that means every kite (after the
      first one) is adjacent to a kite you’ve already found the
      coordinates of, anything will work. At the end of the iteration,
      you know the combinatorial coordinates of every kite in your
      region.
Once you’ve done that, you can generate the output in whichever
      way is easiest. For every kite in the region, you know which
      kite it is out of the 8 making up its containing hat, and that
      (together with knowing whether the hat is a reflected one) is
      enough to generate its complete outline. So you could do that
      for every kite in the region, and discard duplicates.
But an even easier way than that is to only generate an output
      hat when the iteration finds a kite which was #0 in its hat, and
      even then, discard it if that whole hat doesn’t fit in the
      output area. This guarantees to generate every valid output
      hat
exactly once
, so no de-duplication is even
      needed.
(If you need to generate hats that
cover
your output
      area, instead of the subset of hats that fit entirely inside it,
      then that algorithm can still be used – just expand the output
      region by the maximum width of a hat on each side, so that any
      hat that intersects the true region must fall entirely within
      the expanded one.)
As long as you’re only looking at the three coordinates
      (
k
,
h
,
m
) of each kite (which kite it is,
      in which hat, of which
type
of first-order metatile),
      it doesn’t matter that multiple different coordinates can refer
      to the same location, because they’ll all agree on those three
      points. The lowest-order coordinate index that can differ
      is
c
, the question of which child of which second-order
      metatile the first one is. So the information you really need
      (kite index, and whether the hat is reflected) is easy to read
      off reliably.
Advantages
I’ve mentioned in passing a few ways that this combinatorial
      coordinate technique is superior to recursive expansion. But
      let’s bring them all together:
Uniform distribution
. By generating each
      coordinate with the correct probability distribution, you can
      arrange that your output patch of tiling is chosen
      from
precisely
the overall limiting distribution, and
      not just some approximation to it based on a large finite
      region.
No need to engage with geometry of higher-order
      tiles
. The question of what
points in the
      plane
might be the vertices of any higher-order tile just
      never comes up, in this system. The only thing we ever track
      about the higher-order tile layers is
      their
combinatorial
nature: what tiles exist at all,
      which ones are children of which, which ones are adjacent to
      which, which ones overlap which. This isn’t such a huge
      advantage in the Penrose tilings, where the higher-order
      geometry was still fairly easy. But in the hats system, the
      distortion of the metatiles is made completely irrelevant by
      treating them purely combinatorially, so we never have to worry
      about it at all.
No risk of overflow
. In the recursive
      expansion technique, we need to generate actual coordinates for
      all the tiles at every layer. If we’re choosing a small output
      region from a really big patch, this might mean we have to worry
      about floating-point precision loss in the largest scales – or
      alternatively integer overflow, if we use exact integer-based
      coordinates (see the appendix below). But in this system, the
      only output points we ever generate are the ones in the actual
      output region, so we only need to ensure that our number
      representation is accurate enough for
that
. The much
      larger tiles surrounding the output region are still described
      in this algorithm, but instead of being described by very large
      single numbers (representing vertices in the plane), they’re
      described by a long string of small numbers (the labels in the
      combinatorial coordinate list). It’s as if we had transferred
      the working state from machine integers or floats into a bignum
      representation – just a slightly weird two-dimensional
      mixed-base one.
No manual tuning needed
. In the recursive
      expansion technique, you have to think about the size of output
      region you want, and choose up front how many recursion levels
      you’re going to perform (also based on what error you’re
      prepared to tolerate from the ideal probability distribution).
      But in this system, you
find out
after the algorithm
      finishes how many levels of coordinates it turned out to need to
      invent. You don’t have to make a decision up front at all, which
      means you don’t need to debug the code that does it.
(In particular, you might not end up with the
same
number of coordinate labels, in two runs on the same target area
      with different random numbers. It will depend on whether the
      starting element’s randomly chosen coordinates happened to put
      it close to a high-order tile boundary.)
Close to linear time
. The number of coordinate
      labels we end up dealing with is variable. But on average it
      will be proportional to the log of the number of output tiles.
      For each output tile we generate, we perform a bounded number of
      operations that step from the coordinates of one element to an
      adjacent one. Each of those steps will
      take
O
(log
n
) time, or
      maybe
O
(log
2
n
) for the hats system
      which might need to recurse back and forth rewriting metatile
      labels. But that’s only an upper bound:
most
coordinate
      rewrites will be able to succeed by adjusting only the
      lowest-order labels, and the occasions of recursing higher up
      will become progressively rarer as you ascend the layers.
I don’t have a formal proof that the average overall running
      time is any better
      than
O
(
n
log
2
n
). But it seems
      intuitively clear that it will in practice be much closer to
      linear time than that expression makes it look!
Only needs to use logarithmic memory
. If you’re
      generating a hats tiling to cover a rectangular region by
      iterating over the kites in that region, you can arrange to keep
      a very small number of coordinate lists live at one time – just
      two or three is enough to guarantee that every kite you process
      is adjacent to one of a small number of past kites that you’re
      still keeping the coordinates for. There’s no need to store the
      full coordinates of
every
kite for the duration of the
      algorithm: you can emit each hat as you come to it in a
      streaming manner, and forget nearly everything about the ones
      you’ve already generated.
So this system is suitable for generating
absolutely
        enormous
patches of hat tiling, with only a modest cost
        in memory usage. The running time is close to linear in the
        number of output hats, and the average memory usage is
        just
O
(log
n
). Probably whatever is printing out
        the hats after you generate them will have higher cost than
        that!
I
think
it should be possible to work this way in the
      Penrose case too, even without a convenient underlying grid to
      iterate over. But it would be fiddly. I think you could do it by
      iterating along a sequence of horizontal lines of the output
      region, at a spacing small enough to guarantee any triangle must
      intersect
at least
one line. Then, instead of adding
both
of each new triangle’s outgoing edges to a queue,
      instead choose just one of them to traverse next, by picking the
      one that intersects the horizontal line you’re currently
      following. Meanwhile, a similar iteration in the perpendicular
      direction is finding all the triangles on the left edge of the
      region, to begin each horizontal iteration at. To avoid emitting
      any triangle twice, check to find how far above the lowest point
      of the triangle the current line hits it; if that’s greater than
      the line spacing then you know a previous sweep must have
      already caught it.
I’m fairly sure this would work, but I haven’t tried generating
      Penrose tilings in this low-memory mode. I’ve only tried the
      more obvious breadth-first search. Also, this would be slower by
      a constant factor in payment for the memory saving – you’d visit
      most triangles more than once.
Conclusion
I’ve presented two algorithms for generating aperiodic tilings
      at random. The first algorithm, picking a random region from a
      large fixed area, is efficient enough for Penrose tilings, but
      works rather badly for hats because of the distortion problem.
      The second, combinatorial coordinates, is efficient for both
      types of tiling, and
especially
so for hats, where the
      other algorithm performed worse. Also, it has many other
      assorted advantages, listed in the previous section.
The combinatorial coordinates system described here is in use
      in the live version of Loopy for generating hat tilings, and is
      working very nicely.
The Penrose tilings in Loopy are generated by the other
      algorithm, picking a random region from a fixed patch. At the
      time Penrose tilings were implemented in Loopy, neither I nor
      the implementor had thought of the combinatorial coordinates
      system.
Now that I have thought of it, it’s tempting to rewrite Loopy’s
      Penrose tiling code using the shiny new algorithm. But on
      balance I’m not sure that I want to, because its textual game
      descriptions are based on specifying the coordinates of the
      random sub-region. So if I threw out the existing code, then
      existing game descriptions and save files would stop
      working.
(I could
keep
the old code, solely for parsing old
      game descriptions, and switch to combinatorial coordinates for
      new ones. But that seems wasteful in another sense – I’d end up
      with
two
pieces of complicated code where only one is
      really needed!)
However, I have implemented a combinatorial-coordinate Penrose
      generator as prototype code, and it’s pretty convenient. If I
      were starting from scratch in Loopy with no backwards
      compatibility considerations, I’d certainly choose that
      algorithm now!
Appendix: exact coordinate systems
In both the Penrose and hat tilings, it’s useful to have a
      representation for storing the coordinates of vertices of the
      tiling which allows you to compute without floating-point
      rounding errors. That way, you can easily check whether a vertex
      of the Penrose tiling is the same one you’ve seen before, or
      keep track of the coordinates of the current kite in the
      underlying grid of the hats tiling, without having to deal with
      the awkwardness that when you get back to something that
      logically
should
be the same tile or vertex, its
      coordinates have changed a tiny bit.
Complex roots of unity
For the Penrose tiling, one neat approach is as follows.
      Consider the coordinates to be
complex numbers
, rather
      than just 2-element vectors. Then let
t
be the complex
      number cos(
π
/5) +
i
sin(
π
/5), which has
      modulus 1 and argument
π
/5. Then, multiplying any other
      number by
t
has the effect of rotating it by exactly a
      tenth of a turn around the origin.
Therefore, we know that
t
5
= −1,
      because rotating by a tenth of a turn five times must rotate by
      half a turn, exactly negating the number you started with.
      So
t
is a zero of the
      polynomial
z
5
+ 1. This polynomial
      factorises as
      (
z
+ 1)(
z
4
−
z
3
+
z
2
−
z
+ 1),
      and
t
is not a zero of the first factor (or else it would
      just be −1). So it must be a zero of the second factor, meaning
      that
t
4
=
t
3
−
t
2
+
t
− 1.
So, suppose you have two complex numbers, each expressed as a
      linear combination of the first four powers of
t
,
      say
a
+
bt
+
ct
2
+
dt
3
and
w
+
xt
+
yt
2
+
zt
3
.
      Then you can multiply those polynomials together, multiply out
      the product, and reduce every term
      containing
t
4
or higher by applying the
      identity
t
4
=
t
3
−
t
2
+
t
− 1.
      This gives you the product of the two numbers,
also
in
      the form of a linear combination of the first four powers
      of
t
. Better still, if the the two values you’re
      multiplying have all four coefficients integers, then so does
      the product.
Also,
t
has further useful properties. It turns out
      that
t
+ 1/
t
=
φ
, the golden ratio. This is
      also the ratio of the two side lengths of the triangles making
      up a Penrose tiling. And 1/
t
is
      just
t
9
= −
t
4
= 1 −
t
+
t
2
−
t
3
.
      So
φ
itself has a representation in this system, with all
      four coordinates
      integers:
φ
= 1 +
t
2
−
t
3
.
      So does its inverse, because
      1/
φ
=
φ
− 1 =
t
2
−
t
3
.
      So you can scale a vector length up or down by a factor
      of
φ
, by simply multiplying by an appropriate tuple of
      four integers, and
still
leave all four of its
      coordinates as integers in this system.
This gives you everything you need to calculate the vertices of
      Penrose tilings without rounding error, using
either
of
      the methods described in this article (recursive subdivision of
      a large starting tile, or breadth-first search via combinatorial
      coordinates). The coordinates of a single triangle can all be
      computed from each other by a combination of rotating
      by
t
and scaling up or down by
φ
; once you have
      one triangle, you can similarly compute the coordinates of the
      triangle next to it; and in the subdivision process the
      different sizes of triangle are scaled by
φ
each time.
      And every coordinate you need will be described by a tuple
      (
a
,
b
,
c
,
d
) of four integers, so
      they’re easy to check for equality!
The hat tiling is simpler, because it lives entirely on the
      underlying kite tiling. There are lots of ways to represent the
      coordinates of vertices of that tiling, and they need not be
      mathematically clever; any old
ad hoc
approach will be
      good enough. However, a similar trick to the above is a
      particularly nice approach:
      let
s
= cos(
π
/3) +
i
sin(
π
/3)
      represent a sixth of a turn around the origin, in which
      case
s
2
=
s
− 1 for similar reasons to
      above. Then you can represent all your vertices as integer
      combinations of 1 and
s
, and compute products in the same
      way as before, so you can rotate a sixth of a turn by
      multiplying by
s
or by
      1/
s
=
s
5
= −
s
2
= −
s
+ 1.
Separate
x
and
y
coordinates using √5
One thing that
isn’t
convenient, in the above Penrose
      representation using
t
, is checking whether a vertex is
      inside or outside your intended target rectangle. The four
      coordinates in the tuple
      (
a
,
b
,
c
,
d
) are pretty abstract,
      and have no obvious relation to
x
and
y
coordinates in the plane.
Eventually, of course, you’ll have to convert them back to
      actual complex numbers, to plot your tiling on the screen or the
      page. This is done by these formulae, which give you separate
      real and imaginary parts (i.e.
x
and
y
coordinates) for all the numbers involved:
t
= cos(
π
/5) +
i
sin(
π
/5)
t
2
= cos(2
π
/5) +
i
sin(2
π
/5)
t
3
= cos(3
π
/5) +
i
sin(3
π
/5)
So you could just use those formulae to convert all your
      coordinates into floating point as you generate the tiling, and
      use the floating-point coordinates to decide whether any part of
      a tile is inside your output rectangle.
But if you’d rather do even
that
check without
      rounding error, there’s a more exact method available. It
      happens that cos(
π
/5) =
φ
/2 = (√5 + 1)/4, and
      cos(2
π
/5) = (√5 − 1)/4. The sines appearing in the
      imaginary parts don’t have nearly such nice algebraic
      representations (in fact they’re roots of a horrible quartic),
      but their
ratio
does: the ratio
      sin(2
π
/5)/sin(
π
/5) turns out to be just
φ
again.
(The
t
3
term can be reduced to the existing
      numbers by observing that sin(3
π
/5) = sin(2
π
/5),
      and cos(3
π
/5) = −cos(2
π
/5).)
So if we define
X
= 1/4 and
Y
= sin(
π
/5)/2
      to be our basic units of distance in the
x
and
y
directions respectively, then the formulae above reduce to
t
= (1 + √5)
X
+ 2
iY
t
2
= (−1 + √5)
X
+ (1 + √5)
iY
t
3
= (1 − √5)
X
+ (1 + √5)
iY
in which each of the
x
and
y
coordinates is
      expressed as an integer combination of 1 and √5 (times some
      fixed scale unit which we mostly ignore).
In
this
representation, you can exactly compare two
      numbers of that form to determine which is greater. Start by
      subtracting the two, giving a single number of the
      form
a
+
b
√5; then the problem reduces to testing
      its sign. If
a
and
b
have the same sign as each
      other, then the answer is obvious; if they have opposite sign,
      then you just need to know which of
a
and
b
√5 has
      greater magnitude, which is the same as asking which
      of
a
2
and 5
b
2
is bigger. And
      you can do that calculation in integers!
So if you scale your output rectangle just once to write its
      width as a multiple of
X
and its height as a multiple
      of
Y
, then you can do the entire process of tiling
      generation, including bounds checking, in exact integer
      arithmetic, and convert back to floating point only for the
      final job of actually plotting the points.
(You could also choose to use these √5-based coordinates for
      the whole job, instead of converting from the
t
representation. It’s slightly more inconvenient to do rotation
      and scaling by
φ
in this system, because some of the
      operations you need will involve integer division, whereas in
      the
t
representation, it’s all just multiplication and
      addition. But the divisions will be by small constant integers,
      and if you generate correct coordinates then they’ll never leave
      a remainder. So you might decide that this is less hassle
      overall than having
two
complicated coordinate systems
      and a conversion in between. It’s up to you.)
Appendix: interleaving the Penrose tiling types
Here’s an interesting thing about the P2 and P3 tilings.
Both tiling types have substitution systems that involve the
      same two types of isosceles triangle, each in two mirror-image
      forms: one with an acute apex angle, and one obtuse.
In P2, the acute triangle is the larger one, and the
      substitution step divides it into three smaller triangles – but
      two of them are the same two triangles that the
obtuse
triangle divides into. So you could imagine dividing the acute
      triangle first into a smaller acute triangle and an obtuse
      triangle of the current size, and then completing the procedure
      by dividing all the obtuse triangles.
In P3, the situation is exactly reversed. The obtuse triangle
      is larger, and its three substituted tiles include two that
      could also have been obtained by first making an acute triangle
      and then subdividing that.
It turns out that, by separating each tiling’s subdivision into
      these two phases, they can be interleaved! Here’s a single set
      of substitution rules that divide both acute and obtuse
      triangles into just two pieces:
Interleaved P2/P3 substitution rules
The rule with this substitution system is that, in each
      iteration, you only use the rules for one type of triangle –
      whichever one is currently larger. If you have larger obtuse
      triangles than acute, then you only divide up the obtuse
      triangles; this makes the obtuse triangles smaller and leaves
      the acute ones the same size (including the extra ones you just
      made). That means, in the next iteration, the acute triangles
      are larger, so this time you only subdivide those ones. So in
      each iteration, you use whichever rule you didn’t use the
      previous time.
Here’s an illustration of the resulting interleaved
      substitution system. In each iteration, the appropriate
      boundaries between mirror-image triangles are drawn fainter, so
      you can see that in alternate iterations they combine into kites
      and darts, or into rhombs, depending on which tile type is
      currently the larger one:
Interactive demo of interleaved P2/P3 substitution
This isn’t of practical use while constructing the tilings, but
      isn’t it
pretty?
References
Some useful links if you’d like to know more:
