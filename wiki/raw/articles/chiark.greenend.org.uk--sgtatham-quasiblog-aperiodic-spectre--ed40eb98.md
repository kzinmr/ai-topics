---
title: "Combinatorial coordinates for the aperiodic Spectre tiling"
url: "https://www.chiark.greenend.org.uk/~sgtatham/quasiblog/aperiodic-spectre/"
fetched_at: 2026-04-28T07:01:35.241796+00:00
source: "chiark.greenend.org.uk/~sgtatham"
tags: [blog, raw]
---

# Combinatorial coordinates for the aperiodic Spectre tiling

Source: https://www.chiark.greenend.org.uk/~sgtatham/quasiblog/aperiodic-spectre/

Combinatorial coordinates for the aperiodic Spectre tiling
[Simon Tatham, 2023-06-16]
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
In March 2023, four
      mathematicians
discovered
a polygon they called a ‘hat’, whose isometric images can tile
      the plane, but cannot do so periodically.
Hat monotiling: the darkest red hats are reflected
This answered a long-open question in mathematics, of whether
      forced aperiodicity could be achieved with only one shape of
      tile. (Roger Penrose
      had
previously
      managed it
with two tile shapes.)
The wording of the problem –
isometric
images –
      permits the tiles to be reflections of each other, as well as
      rotations and translations. The hat tiling made use of this
      freedom: the hat shape is asymmetric, and the tiling requires it
      to be used in both handednesses (though with one handedness
      nearly 7 times as common as the other).
To put it mildly, a lot of people on the Internet weren’t very
      happy with that. Some people felt that the problem conditions
      were wrong on principle – that it’s simply
more natural
to consider the reflected forms of an asymmetric shape to be two
      different shapes. Other people had more practical objections: “I
      want to tile my bathroom with these, but bathroom tiles need
      different surfaces on the front and back, so I
      definitely
do
need to order two different types of
      tile!”
The discoverers of the hat
could
quite reasonably have
      answered “shut up all of you, we’ve solved the problem that was
      actually posed”. But they did better. Two months later, the same
      authors
announced
that they’d found a variant form of their tile which solved the
      revised problem. The modified tile – called the ‘Spectre’ – is
      still asymmetric, but it can tile with only a single
      handedness.
Spectre chiral monotiling: nothing is reflected
Shortly after the hat tiling was announced, I had implemented
      support for it in
      my
puzzle
      collection
, adding it to the collection of grid types on
      which you can play the puzzle “Loopy”. In the course of this, I
      came up with an algorithm for generating random patches of that
      tiling, which also generalises to the aperiodic Penrose tiles,
      which I felt was so good it deserved
      a
writeup article
.
So, now the Spectre tiling has been discovered, the natural
      question is: does the ‘combinatorial coordinates’ algorithm
      described in my previous article work for Spectres as well?
The answer is yes, it does. But the structure of the tiling is
      different enough that the details had to be worked out all over
      again. In this article I present the method.
The Spectre tile
The shape of the Spectre tile is very similar to the hat. In
      fact, the only thing you have to do to turn a hat into a Spectre
      is to make all the edges the same length.
The hat tile has two different lengths of edge, differing by a
      factor of √3. If you stretch the short edges so that they become
      the same length as the long ones, nothing goes wrong (the loop
      of edges still comes back to its starting point without
      crossing), and the result has all its edges the same length.
(At least, from a certain point of view. This is only true if
      you count the longest edge of each shape as being divided at its
      midpoint, so that it’s really two consecutive edges that happen
      to point in the same direction. This is an unusual way to think
      about polygons, but fits well with the ways the tiles connect
      together in both tilings, as well as the grid of kites
      underlying the hat tiling.)
The Hat and Spectre tile shapes
All of the angles between consecutive edges of the Spectre tile
      are either 90° or 120° (or 180° at the straight vertex in the
      middle of the double-length edge):
The Spectre, with right angles marked with a square and 120° angles with an arc
There’s a small quibble with the definitions (as there seems to
      be with every interesting aperiodic tiling). If you take this
      polygon at face value, it
does
permit periodic tilings
      in a way that the hat tile doesn’t, because making all the edges
      the same length allows chains of tiles oriented the same way to
      interlock:
The Spectre polygon tiling periodically. Spectres in adjacent columns are reflections of each other.
But didn’t we just say that the Spectre
only
permits
      aperiodic tilings?
Well, that’s down to definitions. The polygon I show here is
      what the discoverers call a ‘weakly chiral’ aperiodic monotile:
      the only way to tile the plane with
only one handedness
of tiles of this shape is non-periodic. But allowing both
      handednesses introduces additional periodic tilings like the
      above (as well as transformations of the mixed-handedness hats
      tiling) …
… unless you also constrain which edges of the polygon are
      allowed to join to which other edges. If you number the 14 edges
      of the Spectre consecutively around the polygon, and require
      that any two tiles that meet must join an odd edge to an even
      edge, then the tile becomes ‘strongly chiral’: even if you’re
      allowed to use
both
handednesses, the only tilings of
      the whole plane (respecting the connection rules) are both
      non-periodic and involve only one of the handednesses.
This is exactly the same rule tweak we’ve already accepted for
      Penrose tiles (which also have the property that they’d admit
      periodic tilings too the way they’re usually drawn, since
      they’re just quadrilaterals). And just like Penrose tiles,
      you
can
avoid having to impose artificial restrictions
      if you make the tile more complicated instead. Distorting the
      shapes of the tile edges a tiny bit is enough to prevent the
      unwanted extra tilings, and produce a tile which rules out all
      but single-handedness non-periodic tilings of the plane by its
      shape alone.
The distortion can be anything you like: the precise shapes
      don’t matter, as long as they match.
      The
paper
suggests curving the edges alternately inward and outward, but
      if you prefer a straight-edged polygon, you can just add a
      jigsaw-piece style tab or hole on each edge, and that will work
      just as well:
Strongly chiral variants of the Spectre: rule that the arrows must match, or change the shape
Here’s the example tiling image from the previous section,
      redrawn with the curved version of the Spectre shown here:
A tiling of curved Spectres
As I say above, Penrose tiles have the same quibble – they too
      need to be either distorted or given extra constraints in order
      to rule out periodic tilings. The usual practice is to ignore
      this detail when displaying the tilings: just show the tiles as
      simple quadrilaterals without any distortion, and let the
      matching rules be implicit. That keeps the diagrams simpler, and
      also prettier.
For the rest of this article, I’ll follow the same convention,
      and display Spectres as plain 14-sided polygons.
Hexagonal metatiles
In the
previous
        article
I discussed the general idea of ‘substitution
      systems’ for generating the other types of aperiodic tiling.
      Generally there will be some system of multiple types of
      ‘metatile’, and a set of rules for expanding each metatile
      into multiple metatiles, to produce a larger patch of
      meta-tiling. You can do that as many times as you like, and
      then there will be a final step that converts the metatiles
      into the final output tiles.
For Penrose tilings I found it convenient to take the metatiles
      to be triangles obtained by cutting each actual Penrose tile in
      half, so that the final output step consisted of gluing pairs of
      metatiles back together. For the hats tiling, the paper
      presented a system of four metatile types, all differently
      shaped polygons.
The Spectre tiling can also be generated by the same general
      method. But even though the tile itself is so similar to the
      hat, the structure of the
tiling
is totally different
      (or else you'd have reflected Spectres just like the hats). So
      the metatile substitution system is completely different too!
The substitution system we’ll use for the Spectre tiling is the
      most complicated so far, in one way: it consists
      of
nine
different types of metatile, where the hats had
      only four, and the Penrose tiles had four (but in two
      mirror-image pairs). However, it's the simplest in another way:
      all nine metatiles are the same shape as each other!
Specifically, the metatiles are all regular hexagons, and they
      fit together into a hexagonal tiling.
How do you tell nine tile types apart when they're all the same
      shape? You assign them letters, of course. The paper assigns
      them the capital Greek letters Γ, Δ, Θ, Λ, Ξ, Π, Σ, Φ, Ψ.
With apologies to the authors of the paper, I’m going to change
      those names, because Greek letters are awkward on an Anglophone
      keyboard, and not well supported in all software contexts
      either. Latin letters that fit within ASCII have the best chance
      of being usable in identifiers in a wide set of programming
      languages. So for this presentation I’ll rename the tiles to G,
      D, J, L, X, P, S, F, Y respectively.
(Why those letters? The LaTeX ‘
babel
’ package
      defines a mapping of Latin to Greek letters, for typesetting
      documents containing Greek from ASCII source. These are the
      letters that
babel
maps to the paper’s original
      names.)
As presented in the paper, the nine hexagon types come with
      markings on their edges to constrain which ones can connect to
      which other ones. If you turned those markings into jigsaw-piece
      tabs and holes of different shapes, then the nine resulting
      jigsaw pieces would constitute an aperiodic tiling system in
      their own right.
Hexagons with example jigsaw edges
An example patch of aperiodic tiling with those hexagons
(Of course the jigsaw shapes, if you add any, are completely
      arbitrary, just like the ones shown on the Spectre tile itself
      in the previous section. You can make up edge shapes however you
      like, as long as they match. The shapes above don’t come from
      the original paper – I invented them myself to be easy to
      draw.)
The expansion system turns each of these hexagons into a
      pattern of either 7 or 8 hexagons, all in more or less the same
      layout. I won’t show the full set of expansions here – they’ll
      be in the next section with all the edges numbered – but here
      are the first two types, as examples:
Examples of hexagon-to-hexagon substitution
        rules
Looking at these diagrams, the first thing you probably notice
      is that the right-hand side of each one isn’t very
      hexagon-shaped. How do the expansions of these hexagonal tiles
      fit together?
(In particular: the right-hand sides of both those diagrams
      show a G and D hexagon adjacent to each other. So
      the
expansions
of G and D must also fit together
      somehow. But looking at those diagrams by themselves, it’s not
      at all obvious which part of the border of those two assemblies
      of hexagons fit to each other! The answer will be shown in a
      later section.)
The answer is: it depends on the tile. Each of the different
      types of edge (shown here by a different jigsaw shape) turns
      into a different path of edges along the outline of one of these
      expansion diagrams. And they don’t all expand to the
same
      length
paths of edges: they range from length 2 to 6. So
      the way the expansions fit together into a full tiling is very
      complicated!
Fortunately,
we
don’t need to worry about all that
      complexity. The mathematicians who discovered the tiling have
      proved that it all works, and that if you just follow the
      expansion rules, everything will fit together. To implement the
      generation algorithm, we don’t need to go through the proof
      ourselves: we just have to trust it.
In fact, we don't even need to worry about the different types
      of hexagon edge fitting together correctly, because the
      expansion system will automatically arrange that the hexagons
      only connect in approved ways. So I’ll leave the edge markings
      out of all the following diagrams. They’ll be complicated enough
      already!
Just like the metatile systems for other aperiodic tilings,
      this hexagon-to-hexagon expansion step can be iterated as many
      times as you like. But eventually you end up wanting to convert
      your final set of hexagons to the output Spectre shapes, to
      generate the
one-tile
aperiodic tiling that was the
      purpose of the whole exercise.
In this setup, eight of the nine hexagon types expand to just
      one Spectre. The exception is the G tile, which expands to two.
      I’ll show the full expansion rules in the next section.
Numbering everything
As we did for the Penrose and hat tilings, we’re going to
      develop a system for generating Spectre tilings using
      combinatorial coordinates. That is, for each Spectre in the
      tiling, we’ll track what hexagon type it was expanded from (and,
      in the case of the G hex, which of the two Spectres belonging to
      that hex it is); which child of what hexagon type
that
was expanded from, and so on for as many layers as we need. And
      then we’ll show an algorithm for transforming the coordinates of
      one tile into the coordinates of a specified neighbour, so that
      by repeating the transformation you can walk around the whole
      tiling one step at a time.
For this coordinate system, the smallest unit we’re going to
      deal with will have to be a single output Spectre tile. In the
      hats tiling we subdivided each hat into 8 cells of the
      underlying kite tiling, but Spectres don’t fit on any such
      tiling in the same way; for Penrose tiles we subdivided each
      output tile into two half-tile triangles because those were our
      metatiles, but here the metatiles are larger than a single
      Spectre rather than smaller. So, for the first time, we’ll use
      the output tiles themselves as the finest granularity in our
      coordinate system.
How do we specify which neighbour we want to transition to? In
      both previous systems, we did this by indexing the edges of the
      smallest-size cells: the three sides of a Penrose half-tile
      triangle, or the four sides of a kite. Here, we’ll do the same –
      but our smallest cell is the Spectre, which
      has
fourteen
edges (counting the long edge as two
      normal edges, which is much more convenient).
So, we start by numbering absolutely everything. We must number
      the edges of a hexagon; the edges of a Spectre; the hexagons
      appearing in the expansion of each higher-level hexagon; and the
      two Spectres appearing in the expansion of the G hex. The
      locations of these numbers are basically arbitrary – the
      algorithm will work just as well no matter what you choose, as
      long as you do it consistently. Here are the numberings I’ve
      used in my implementation:
Numbering all the things
(In the above expansions, the Spectre number 1 – shown with a
      dotted outline – appears only in the expansion of the G hex.
      Hexagon number 7, conversely, appears in the expansion of every
      hex
except
the G hex.)
With all those numbers allocated, we can now show the full
      expansion rules for the hexagon step.
As well as showing the pattern of hexagons (each with an
      orientation) that each original hexagon transforms to, we must
      also show how the edges match up. To do that, I’ll mark six
      circular blobs on the border of each figure, with a larger blob
      at the ‘starting’ vertex at the top of the original hexagon, and
      the same for the corresponding point on the output map.
Hexagon-to-hexagon substitution rules
In the above diagrams, I’ve marked all the edge numbers of the
      hexagons on the right-hand side. This enables you to
      compute
internal
transitions between hexagons within
      one of these maps.
For example, suppose your coordinates identify a G hex that is
      child #2 of a Y hex, and you want to find the coordinates of the
      hex on the other side of its edge #3:
Example transition within a single level
The expansion map for the parent Y hex shows that edge #3 of
      child hex #2 is adjacent to edge #1 of child #5 (type D). So if
      you were computing that transition, you’d rewrite the number 2
      in the coordinate string to be a 5. We’d also know that we came
      into that D hex via its edge #1, which will be an important
      thing to know during recursion.
What if you want to step
outside
one of these maps?
      For example, suppose you were in that same G hex but wanted to
      traverse edge #0?
For this, I’ve also marked two-part edge numbers on
      the
outside
of the diagrams. Each edge of the large
      hexagon on the left-hand side corresponds to a sequence of edges
      on the right-hand side between two of the circular blobs. Each
      exterior edge of these maps is marked with a pair of
      numbers
a
.
b
, where
b
indicates an edge of
      the larger hexagon, and
a
is the index of a particular
      edge within that. So between any two circular blobs, all the
      indexes have the same second component, indicating that they all
      correspond to the same edge of the larger hex.
Example transition recursing to the second level
In this example, edge #0 of the “2 (G)” hex has “0.1” written
      on the far side. This indicates that it’s part of the segment of
      boundary corresponding to edge #1 of the larger Y hex.
So, first, we recursively compute a transition for the next
      size of hexagon up, using the same algorithm. In this example,
      I’ve shown our second-order Y hex as child #1 of a P hex.
      Referring to the P map in turn, edge #1 of that Y is adjacent to
      edge #4 of the S hex at child #3. So at the second level of
      hexagons, we’ve just stepped out of a Y via its edge #1, and
      entered an S via its edge #4.
In the Y map, we can see that there are three edges of the map
      marked
a
.1 for some
a
: they’re marked 0.1, 1.1 and
      2.1. The edge of the map we’re leaving along (corresponding to
      edge #0 of the G, our original example case) is marked 0.1.
The matching rules should arrange that the boundary segment on
      which we’re entering the S map is the same shape. And it is:
      there are three edges marked
a
.4, in the same way. So an
      instance of the Y and S map must appear in the overall hexagon
      tiling with those edges adjacent. This is shown in the diagram
      above, and you can see that the numbers match up in reverse
      order, so that 0.1, 1.1 and 2.1 on the Y map fit to 2.4, 1.4 and
      0.4 respectively on the S map.
So
now
we know we’ve stepped off the 0.1 edge of the Y
      map and come in on the 2.4 edge of the S map – which lands us in
      its hex marked “7 (X)”, having come in via edge #4 of that hex.
Transitions between Spectres
That’s how to compute transitions between the hexagonal
      metatiles. But at the lowest level of the coordinate system we
      must deal with the actual output Spectre tiles. So we also have
      to consider how each lowest-order hexagon maps to
      Spectres.
This mapping is
mostly
regular. Seven of the nine
      hexagon types turn into a single Spectre, in a consistent
      orientation (relative to the hexagon’s own orientation), and the
      only thing that changes is how the edges of the Spectre map to
      the edges of the hexagon. In the following diagrams I’ve
      numbered the internal edges of the Spectre, and the external
      edges to show what segment of the Spectre boundary corresponds
      to each edge of the hexagon, in the same way as the diagrams in
      the previous section:
Hexagon-to-Spectre substitution rules: the simple ones
Similarly to the previous section, this allows us to start by
      deciding which edge of one Spectre to cross, and find out which
      edge of another Spectre we’ve come in along.
For example, suppose we had coordinates describing a Spectre
      expanded from the X hexagon, and wanted to leave by – say – its
      edge #4. The diagram shows this to be marked 1.1, in a boundary
      segment containing three Spectre edges, labelled 0.1, 1.1 and
      2.1. So we’d call the routine for computing a hexagon
      transition, which might tell us (for example) that edge #1 of
      this particular X hexagon was adjacent to edge #4 of a D.
Therefore, we’d expect there to be three edges on the D diagram
      marked as
a
.4 – and there are. Again, they fit together
      in reverse order (imagine actually rotating the diagrams to
      bring those boundary segments together), with 0.1, 1.1 and 2.1
      on the X Spectre matching up to 2.4, 1.4 and 0.4 on the D
      Spectre. So if we leave the X via 1.1, we enter the D via 1.4,
      and the D map shows that this corresponds to its edge #11.
Those seven hexagon types are the easy ones. The final two are
      more complicated, so I’ve left them until last.
I’ve already mentioned that the G hex turns into two Spectres
      rather than one:
Hexagon-to-Spectre substitution rule for the G hexagon
If your coordinates identify a Spectre expanded from a G hex,
      they must also say which of the two it is (via the numbers 0 and
      1 at the centre of each Spectre). And not
every
transition within a G hex will go to a neighbouring hex:
      sometimes it will just transfer between the two Spectres within
      this hex. For example, if you’re in Spectre #0 of a G, and leave
      by edge #11, the diagram shows that that’s adjacent to edge #6
      of Spectre #1 of the same G, and you can return immediately
      without having to recurse to compute a hexagon transition.
But the S hex does something even stranger:
Hexagon-to-Spectre substitution rule for the S hexagon
What’s going on
here?
What’s that weird spur sticking
      out on the left of the S Spectre?
That spur should be considered as
four
additional
      boundary edges: if you imagine walking around the edge of the
      diagram starting on edge #0 of the Spectre itself, you walk
      along edges #0, #1, #2 and #3, then walk out along the spur for
      two steps, turn round and walk two steps back, then turn left
      and carry on to edge #4 of the Spectre. The two edges on the
      bottom side of the spur correspond to edge #1 of the S hexagon;
      the two edges on the top side of the spur correspond to part of
      edge #0.
When you’re computing an
outgoing
transition from an S
      Spectre, you can ignore this completely. If you want to leave an
      S spectre by edge #3, that corresponds to exterior edge 0.2, so
      you compute the transition out of edge #2 of the S hex in the
      usual way. If you want to leave by edge #4, that’s marked 3.0,
      so you compute a transition out of edge #0. In both cases, the
      spur doesn’t get involved.
But the spur gets involved when you compute an
inward
transition. Suppose some hexagon transition told you you were
      coming in along edge #1 of an S hexagon – say, the edge marked
      0.1 (which must fit to 1.
something
in the Spectre you
      just left). You consult the map and discover that 0.1 is on one
      side of the spur, and the opposite side of the same edge is
      marked 5.0. Now what?
Now you simply call the hexagon transition
      algorithm
again
, to ask what’s on the other side of
      edge #0 of this S hexagon. In other words, if you step into an S
      Spectre in such a way that you land on the spur, the rules
      require you to step straight back out again.
(You never need to iterate this procedure more than twice.)
Generating the whole tiling
I’ve presented a system for tracking the combinatorial
      coordinates of a particular Spectre, within the infinite
      hierarchy of metatiles.
Just as in the previous article, the next step is to use this
      to iterate over all the Spectres in a given area of the plane,
      so as to construct an actual patch of tiling. There are two
      reasonable methods for this.
One approach is a graph-based search – breadth-first or
      depth-first, whichever you prefer. Choose a location for your
      starting Spectre, and its coordinates in the plane; then explore
      every edge of that Spectre, by doing the coordinate
      transformation to discover the Spectre on the far side of it.
      Each of those transformations will tell you which edge of the
      new Spectre adjoins that edge of the old one; that’s enough
      information to compute all the rest of the vertex coordinates of
      the new Spectre. So you check if the new Spectre is within your
      target area; if so, add all the remaining edges of that Spectre
      in turn to your list of transitions that need to be explored,
      and keep going until you’ve covered your whole target area.
The other approach is to traverse your area in a raster
      fashion, avoiding having to keep a queue of edges yet to explore
      (for breadth-first search), or recurse to high depth (for
      depth-first). You can generate all the Spectres along a
      particular horizontal or vertical line, by calculating which
      edge of the Spectre the line leaves through, and using that to
      calculate your next transition. One loop of this kind can be
      made to generate all the Spectres intersecting (say) the
      left-hand edge of your target rectangle, and from that, you
      start a series of secondary loops along horizontal lines, spaced
      close enough together that every Spectre must be intersected by
      at least one line. This allows you to store a bounded number of
      coordinate strings, and still (if you’re careful) generate every
      output tile exactly once, by automatically detecting whether any
      previous iteration would have encountered that tile.
The second approach is good in terms of asymptotic complexity:
      you can generate an arbitrarily large patch of tiling in
      essentially linear time and essentially constant space
      (discounting the size of the coordinate strings). But it
      involves more fiddly computational geometry than the graph
      search – and the graph search also has the virtue of being
      self-testing, in that if two paths through the tiling generate
      inconsistent results, you have a chance of noticing by failing
      an assertion, so that you can fix the bug in one of your lookup
      tables (or whatever).
Just as in the previous article, you don’t have to generate a
      lot of coordinates up front for your starting tile. Instead, you
      can generate just enough to get started, and every time a
      recursive transition computation needs a coordinate you haven’t
      generated yet, make it up as you go along, according to the
      limiting frequency distribution of the nine hex types.
Also as in the previous article, you can make a run of the
      algorithm reproducible by storing the full set of coordinates
      you
ended up
generating for the starting tile, once
      you’ve covered the whole area. Then another run with those
      parameters should generate the identical patch.
Conclusion
The advantages of the combinatorial-coordinate system are even
      more clear in this case than in the hats case, because the
      distortion imposed by the metatiling system is even more
      profound than it was for the hats. The four hat metatiles only
      distort
slightly
as you expand them recursively; if you
      wanted to use the simpler algorithm of recursively generating a
      large fixed patch of tiling and picking out a randomly chosen
      area of it, it might still have been possible to track the
      distorted images of the target area (with some uncertainty) and
      prune branches of the recursive expansion that would never land
      in it. The hexagons are much stranger, so an algorithm that
      avoids thinking about their geometry at all is extremely
      helpful!
In particular, there’s a detail of the metatile system I didn’t
      mention in the previous sections. The expansion rules for the
      nine hexagons reverse their handedness! If you go back and look
      at the expansion diagrams, you’ll see that each individual hex
      has its edges numbered 0, 1, …, 5
anticlockwise
round
      the edge, but in the expansion, the edge markings go 0.0, 1.0,
      …, 0.1, …,
n
.5
clockwise
. I didn’t mention this
      while describing the algorithm, because the algorithm doesn’t
      need to know or care! As long as it knows which hexes are
      connected to which other hexes by which edge (identified by a
      purely arbitrary numbering system), that’s all it needs.
The two combinatorial coordinate algorithms described in my
      previous article, for the Penrose and hat tiling, have a
      fundamental difference, because of the overlap between metatile
      expansions in the hat tiling. The Penrose algorithm was always
      stepping off the edge of one of its triangle maps and having to
      match that edge up to the edge of some other map to see where it
      had entered that one; this wasn’t too hard, because the map
      edges are all simple straight lines and are divided into at most
      two segments. The hat algorithm involves much larger maps with
      very complicated crinkly edges, but luckily, it never needed to
      step off the edge of one of those maps and figure out how that
      corresponds to some other equally crinkly edge – because the
      maps overlap, so instead we can recompute an equivalent
      coordinate for the same point which is
already
in the
      new map.
But the Spectre metatile expansions don’t overlap, and they do
      have complicated crinkly edges. So this algorithm
did
have to care about how the edges of one map match up to the
      edges of another.
Luckily, that still wasn’t very difficult, because the authors
      of the paper had worked it out already, and included all the
      necessary data in their proofs! The segments of the map edges
      are clearly marked in the paper’s own diagrams. So there was no
      trouble there.
In summary, the combinatorial-coordinates technique works just
      as well for the Spectre tiling as it does for the Penrose and
      hat tilings. I prepared an implementation of all this for my
      puzzle game Loopy at the same time as writing this article, and
      it’s working very well.
Appendix: exact plane coordinates
All the edge lengths in the Spectre tiling are the same
      (counting the long edge of the tile as two normal edges
      end-to-end), and all its angles are multiples of 30°.
This allows us to track the coordinates of all the necessary
      points in the plane using a system based on complex numbers,
      similarly to
      the
methods I
      presented in the previous article
.
In this case, we’ll let
d
be the complex number
      cos(
π
/6) +
i
sin(
π
/6), so that multiplying
      by
d
has the effect of a 30° rotation (or one twelfth of
      a full turn). This number is a root of the
      polynomial
z
4
−
z
2
+ 1 (the
      12th
cyclotomic
      polynomial
). So if you have two numbers expressed as
      polynomials in
d
, and multiply them to get a larger
      polynomial, then you can reduce the polynomial to degree at most
      3, by substituting
d
4
for
d
2
− 1 everywhere it appears (and
      similarly
d
5
becomes
d
3
−
d
, etc, for higher
      powers). And if your original polynomials had all their
      coefficients integers, then the same is true of the reduced
      product.
In this way, you can generate an exact representation of every
      point that you can reach by starting from the origin and
      travelling a series of unit-distance steps in directions that
      are multiples of 30°. In particular, every vertex of a Spectre
      tiling can be expressed this way. So you can recognise the same
      vertex when you come back to it by another route, by simply
      comparing two tuples of 4 integers.
To convert back to separate
x
and
y
coordinates,
      we can use the formulae
d
= cos(
π
/6) +
i
sin(
π
/6) = √3/2 + (1/2)
i
d
2
= cos(2
π
/6) +
i
sin(2
π
/6) = 1/2 + (√3/2)
i
d
3
= cos(3
π
/6) +
i
sin(3
π
/6) =
i
so that if you have a general value
a
0
+
a
1
d
+
a
2
d
2
+
a
3
d
3
then your output coordinates are simply
x
=
a
0
+ (√3/2)
a
1
+ (1/2)
a
2
y
=
a
3
+ (√3/2)
a
2
+ (1/2)
a
1
in which, if the (
a
i
) were all integers,
      these coordinates are all integer multiples of 1/2.
And, just as in the previous article, this coordinate
      representation allows you to test a value to see if it’s within
      a given range, without needing floating point and its rounding
      errors, because the problem is equivalent to testing the sign of
      a general number of the form
u
+
v
√3. If
u
and
v
have the same sign, or if either or both is zero,
      then the answer is obvious; if
u
and
v
have
      opposite signs, then the answer is determined by which one has
      the larger magnitude, which you can decide by finding out which
      of
u
2
and 3
v
2
is bigger, in
      integer arithmetic.
Appendix: four-colourings of the Hats and Spectre tilings
In the previous article I finished off with an appendix
      containing
      an
irrelevant
      but pretty aside
. That seemed like fun, so let’s do it
      again!
Any tiling of the plane can be coloured with four colours, so
      that no two tiles of the same colour share an edge (a ‘proper’
      four-colouring). This is a consequence of the
      famous
Four-Colour
      Theorem
(which guarantees this for
finite
maps in
      the plane), and
      the
De
      Bruijn–Erdős theorem
which extends it to the infinite
      case.
But those theorems between them don’t guarantee that a proper
      four-colouring is
easy
to construct – only that, in an
      abstract mathematical sense, one
exists
. So if you want
      an
actual
four-coloured instance of even a large finite
      patch of one of these tilings, it might be computationally hard
      to find one.
It might be – but it isn’t. In fact, there’s a simple technique
      for generating a natural four-colouring of each of the Hats and
      Spectres tilings. This particular four-colouring is easy to
      specify mathematically, and if you’re already generating the
      tiling itself based on the combinatorial coordinate system I
      describe in this article and the previous one, you can do it in
      practice as you go along, with a minimal amount of extra
      information to keep track of, and no increase in the
      computational complexity. The techniques for the two tilings are
      even quite similar to each other.
The basic idea is: for each tiling, you can identify a class of
      ‘special’ tiles, spaced widely enough apart that no two are
      adjacent, and with the property that if you imagine gluing each
      special tile to a particular one of its neighbours, then the
      remaining tiling of the plane is topologically equivalent to a
      tiling with regular hexagons. (Of course, the tiles will be
      differently
shaped
from hexagons, but each one will be
      adjacent to exactly six neighbours in the same pattern that
      hexagonal tiles connect.)
A tiling of the plane with regular hexagons can be coloured
      with only
three
colours. The colouring is essentially
      unique (up to permuting the three colours), and easy to compute.
      So we now colour the Hat or Spectre tiling with four colours, by
      colouring every tile according to the hexagon that it’s part of
      – except that our ‘special’ tiles are coloured in the fourth
      colour.
To put that another way: if you start by colouring the special
      tiles blue, and then just
try
to colour the rest of the
      tiles with the remaining three colours, you’ll find that it
      always turns out to work, and there’s only one choice of how to
      do it.
So, what
are
the ‘special’ tiles in question?
For the hats tiling: the hats appear in both handednesses, with
      one handedness being common and the other one being rare. The
      special tiles are the rare reflected hats: the original paper
      about the hats tiling observes that fusing each reflected hat
      with one of its neighbours leads to a tiling isomorphic to a
      hexagonal one.
(Using the index system from
      my
previous
      article
, a reflected hat is precisely a hat which has index
      3 in the expansion of a red hexagonal metatile, and the hat you
      fuse it with is the one with index 2. It’s easy to check from
      the metatile expansion diagrams that no two of these fused hat
      pairs can ever be adjacent in the overall tiling.)
For the Spectres tiling, of course, there aren’t any reflected
      Spectres: the whole point is that they all have the same
      handedness! But there is still a class of unusual Spectres,
      based on orientation. All nine of the hexagon types expand to a
      Spectre which has the same orientation relative to the hexagon,
      but the G hex also generates a second Spectre rotated by 30°.
      And all the hexagons’ orientations, of course, differ by
      multiples of 60° from each other. So it follows
      that
most
of the Spectres in the tiling have an
      orientation that’s an even multiple of 30° (taking the reference
      point to be any Spectre not expanded from a G hex), but a small
      number – precisely the Spectres with index 1 in a G hex – have
      an orientation that’s an
odd
multiple of 30°. Those are
      the special ones.
So, if we’re generating one of these tilings via combinatorial
      coordinates, how do we also generate a consistent four-colouring
      according to this principle as we go?
For the hats tiling, the simplest approach I found is to
      pre-compute a working four-colouring for each of the four
      ‘kitemaps’ (showing the expansion of one second-order metatile
      to first-order metatiles, their contained hats, and the kites
      making up each hat). In this four-colouring, the reflected hats
      are coloured with our special fourth colour (say, blue), and the
      rest are coloured in any consistent way with the other three
      colours.
When an instance of this kitemap appears in the overall tiling,
      the colours won’t always match. But the blue tiles will match
      (because they’re the easily distinguished reflected hats), and
      the other three colours will be permuted in some way between the
      real colouring and the kitemap’s prototype colouring.
So, as we step around the coordinate system, we need to keep
      track of a
permutation
that tells us how our
      three
real
(non-special) colours relate to the
      prototype colouring of the kitemap we’re currently in. Given
      that, we can work out what colour to make each hat we come to:
      look up its colour in the prototype kitemap colouring, and apply
      the permutation.
In order to keep track of this permutation, we need to know how
      to update it when the coordinate transformation steps us from
      one kitemap to the next. It turns out that whenever this
      happens, you’ll be able to find a pair of adjacent non-blue hats
      in the overlap between the two kitemaps. Since they’re adjacent,
      they’ll have different colours, which means now you know
      how
two
of your real colours map to the kitemap you’ve
      just stepped into – and by elimination, you know the third. So
      this is no trouble to compute.
For the Spectres tiling, it’s even easier. Our first-order
      Spectre metatiles are precisely the hexagonal tiling that you
      get if you fuse each odd-orientation Spectre with its neighbour
      (specifically, the one making up the other half of its G hex).
      So as we step around the tiling we can directly track the
      three-colouring of the first-order hexagons, and use that to
      determine the colour of every Spectre: if it’s a G1 then it’s
      blue, otherwise it’s coloured the same as its hexagon.
The reason why a three-colouring of the hexagonal tiling is
      essentially unique is because if a given hex has one colour, say
      A, then the other two colours B and C must alternate around it.
      So all we need to keep track of is what colour our current
      hexagon is, and which of the other two colours goes with the
      odd-numbered edges and which the even.
And then, in each coordinate transition between Spectres, we
      need to find out whether it’s moving to a different hexagon (and
      not just between the two Spectres in a G hex), and if so, which
      edge of the old hexagon it left by, and which edge of the new
      hex it came in from. That’s enough to decide on the new hex’s
      colour (by knowing which edge we left from), and figure out how
      the colours are arranged around it (by knowing which edge of the
      new hex leads back to the old one, whose colour we remember).
      And those pieces of data are computed already by the transition
      algorithm – so no trouble!
And here are some examples of both:
Example patches of both tilings with systematic four-colouring
I don’t currently know of any comparably simple rule for
      generating a four-colouring of a
Penrose
tiling as you
      move around it via combinatorial coordinates. If anyone else
      does, I’d be interested to hear of it!
