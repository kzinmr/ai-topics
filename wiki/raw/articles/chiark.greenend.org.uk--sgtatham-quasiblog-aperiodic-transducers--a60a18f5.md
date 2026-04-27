---
title: "Beyond the wall: working with aperiodic tilings using finite-state transducers"
url: "https://www.chiark.greenend.org.uk/~sgtatham/quasiblog/aperiodic-transducers/"
fetched_at: 2026-04-27T07:00:57.344527+00:00
source: "chiark.greenend.org.uk/~sgtatham"
tags: [blog, raw]
---

# Beyond the wall: working with aperiodic tilings using finite-state transducers

Source: https://www.chiark.greenend.org.uk/~sgtatham/quasiblog/aperiodic-transducers/

Beyond the wall
Working with aperiodic tilings using finite-state transducers
[Simon Tatham, 2024-06-10]
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
In two articles last year, I described a very convenient
      recursive algorithm for generating random patches of aperiodic
      tilings in a computer program, using a system I called
      ‘combinatorial coordinates’.
The
      first article
introduced the idea, and applied it to the
      well-known Penrose tilings and the ‘hat’ tiling (newly
      discovered at the time). A few months later, the ‘Spectre’
      tiling was discovered, and I wrote
      a
second article
extending
      the technique to cover that one too.
In this article, I’ll present a variation of that algorithm,
      derived by applying regular-language theory and finite state
      machines to the combinatorial coordinate strings.
The resulting algorithm does the same job as the previous one,
      but faster and more simply. (Or rather, it’s faster and
      simpler
at run time
– but at the cost of a more
      complicated step building the lookup tables for the tiling you
      want to use. But you only have to do that part once, and I’ve
      provided software below that knows how!)
But it doesn’t just do the same thing better. It also
      does
more
. It can handle cases that would have made the
      previous algorithm fail and crash the program – in fact that’s
      why I started looking for it. Those cases include some
      particularly pretty instances of the tilings, so I’ll show lots
      of fun pictures along the way!
A couple of things before we start
This article is structured as a journey of discovery: I’m
      telling the story of how this happened to me, starting with a
      puzzle to solve, some techniques I invented to solve it, and
      other things I found out by applying those techniques once I had
      them. But I’m not claiming to have been the
first
discoverer or inventor of all of this: this isn’t an
      announcement of novel mathematical results. Some of the ideas
      here certainly
had
been thought of before:
      see
the references at the end
. So I
      only ‘discovered’ those parts in the sense that
I
hadn’t known them before, and there was no obvious place I was
      able to learn them before having to find them out the hard
      way.
A lot of the diagrams in this article are interactive, in the
      same style as the first of the two previous articles. When you
      see a diagram with radio buttons above it, then it’s really
      multiple diagrams: select different radio buttons to flip
      between images.
Previously on ‘Combinatorial Coordinates’…
I’m going to refer back to details of the two previous articles
      a lot, but I can at least give a
very quick
recap of
      the general ideas to begin with. If you’ve got the previous
      articles fresh in your mind already, you can safely skip this
      section. If this recap leaves you completely in the dark, the
      two previous articles are linked above.
All of these tilings are generated from substitution systems,
      in which one tiling is expanded into a smaller-scale one by
      replacing every tile with some particular combination of smaller
      tiles. The ‘combinatorial coordinates’ of a tile describe its
      position within this hierarchy, without reference to geometry:
      you say which tile type it is, and which type its larger parent
      is, and the parent of that, and so on.
Also, for each link in that chain, you have to
      specify
which child
of the parent each tile is. For
      Penrose tiles (at least, the way I’ve handled them by cutting
      each tile into two triangles), that doesn’t need any extra
      information, because no tile has two children of the same type,
      so the sequence of triangle types itself is enough. But for the
      hat and Spectre tilings, you have to assign a numeric index to
      each child tile in each expansion, and include those indices in
      the coordinate strings.
In a tiling of the whole infinite plane, each tile has an
      infinite sequence of combinatorial coordinates, because the
      parent tiles keep getting bigger without bound; alternatively,
      if you’re considering only a finite patch of tiling contained
      within some top-level supertile, then you have a finite string
      of coordinates describing each small tile’s location within that
      patch.
In the previous two articles, I developed a recursive algorithm
      that takes the combinatorial coordinates of a tile as input,
      plus a specification of one edge of that tile, and it calculates
      what’s on the other side of that edge, in the same form: it
      tells you the coordinates of the neighbouring tile, and says
      which edge of
that
tile connects to the specified edge
      of the input one. This is done by pure string processing,
      considering nothing but the coordinate strings themselves (plus
      a set of lookup tables describing the substitution system). The
      general idea (in the simplest case) is that at each step from a
      smaller tile to its supertile, you find your smaller tile in a
      map of the supertile’s expansion; if the edge you’re trying to
      traverse is inside the expansion then you know what tile (and
      which edge of it) is on the far side and you’re done; if it’s on
      the edge of the whole expansion then you work out which edge of
      the supertile it corresponds to, and recurse one level higher to
      ask the same kind of question again.
This made a very convenient system for generating random
      patches of tiling to play puzzle games on, because you don’t
      have to worry about the
geometric
coordinates of the
      higher-order tiles. In the hat and Spectre systems, those
      coordinates are distorted in a complicated way, so it’s a big
      advantage not to have to deal with them at all.
My code crashed, and the reason turned out to be
      interesting
I stumbled on the first clue that started this article purely
      by mistake. When I was writing the code to generate the Spectre
      tiling for the game ‘Loopy’
      in
my
      puzzle collection
, one of my half-written test programs
      crashed unexpectedly.
Well, not
very
unexpectedly. Half-written test
      programs crash all the time – that’s what makes them
      half-written. Normally you smite your forehead, fill in some
      immediately obvious missing bit, and carry on. And in one sense,
      this case was no exception: I fixed it quickly, and it didn’t
      slow me down for long in the process of getting Spectre tilings
      into Loopy.
But
after
I’d fixed it, I started thinking harder
      about the implications of what had happened.
How the crash had happened
The program in question was my first attempt to compute a full
      coordinate transition in the Spectre tiling. I’d written a first
      draft of the recursive transition algorithm, and it was time to
      test it. So I wrote a test program which contained a sample list
      of coordinates of a single Spectre tile, and told it to find the
      coordinates of one of the neighbouring tiles.
In the finished version of the code, the initial coordinate
      list is invented lazily, and
randomly
. That is, each
      higher-order coordinate is not generated until the first time
      the algorithm needs to know it, and then a random-number
      generator chooses from the possible options according to the
      right probability distribution. That way, you get your patch of
      tiling chosen uniformly from all the possibilities, and the
      output coordinate string describing the patch is exactly long
      enough to communicate everything you need, with no wasted
      space.
But this was my very first test of the transition code, and I
      hadn’t bothered to connect up the random number generator yet.
      So my ‘generate an extra coordinate’ function did something more
      trivial: given a list of legal outputs, it just picked the first
      one every time.
I thought that would be fine for a first attempt, and I could
      sort out the random numbers later. But in fact that turned out
      to be the reason my code had crashed. I
needed
the
      random numbers, for even the first test run to work!
At every step in the recursive transition algorithm, the
      recursion might terminate, or it might decide it needs to
      recurse again, depending on the state of the algorithm and the
      value of the next coordinate. When you generate coordinates
      randomly, this is reliable, because sooner or later, the random
      number generator will pick a coordinate that causes the
      recursion to terminate. But by making a fixed choice instead of
      a random choice, I’d caused the algorithm to
always
decide it needed to recurse again. So it went into a loop
      calling itself recursively, overflowed the stack, and crashed.
This didn’t take me long to figure out. As soon as I recognised
      the type of crash as a stack overflow, it was easy to spot that
      the algorithm was making the same decisions in every recursion,
      and therefore always recursing. I connected up the random number
      generator and tried again. No more problem.
Why that was interesting
That particular crash stuck in my memory, even after I’d fixed
      it, and I kept on thinking about it.
I’ve forgotten exactly what the coordinates were in the
      original crashing code, but it’s not too hard to
      reconstruct
some
input that causes an endless
      recursion. In fact, you can find cases where the code makes
      the
same
choice at every recursion level, in an
      unchanging endless loop.
I’ll show a specific example of how that could happen, starting
      from one of the diagrams
      from
the previous
      article
. This is showing one of the nine hexagonal metatile
      types (type Y), and how it expands into smaller hexagons.
Hexagon-to-hexagon substitution rule for the Y hex type
In this figure, the four edges labelled “0.4”, “1.4”, “2.4”,
      “3.4” in the diagram on the right correspond to the edge
      labelled “4” in the single hex on the left. And one of those
      edges is
also
edge #4 of a Y-type hex: edge 2.4 of the
      expansion diagram is also edge 4 of the hex labelled “7
      (Y)”.
So, suppose the coordinate transition algorithm is given a
      Y-type hex, and told to find out what’s on the other side of its
      edge #4. When it looks at the next coordinate up, it discovers
      that that Y hex is child #7 of another Y hex. In other words, it
      realises it’s not just in
any
Y hex: it’s in the one
      labelled “7 (Y)” on this diagram.
Edge #4 of that hex is on the outside of this map, so it can’t
      terminate the recursion. Instead, it must recurse to the next
      level to find out what larger hexagon lies next to this one.
But that puts it
back
in the position of trying to
      traverse edge #4 of a Y-type hex, which is exactly where it
      started!
It’s fine for this to happen a
finite
number of times
      during a run of the algorithm. In fact, it’s inevitable, on any
      large enough input. Within any full Spectre tiling of the plane,
      cases of this problem must occur infinitely often at every
      finite depth. There will always be
n
th-order Y hexes, for
      any
n
; each of those has a chain of Y-type children
      somewhere inside it, with each one being child #7 of the
      previous one. So, for any
n
, there will be cases where
      the recursive transition algorithm performs
n
successive
      steps leading it from “edge #4 of a Y” to “edge #4 of the next
      higher Y” – but after that, something different happens, the
      recursion terminates, and the algorithm completes the whole
      transition successfully.
The problem arises when the function that invents the next
      higher-order coordinate
always
returns the same value.
      If it decides that this Y is child #7 of another Y,
every
      single time
, then every recursive call to the transition
      function will recurse again into an identical one, and nothing
      different will
ever
happen to terminate the
      recursion.
So that explains the crash, in terms of the mechanism of the
      code. But what does this say about the
geometry of the
      tiling?
Suppose that we started with a single Y hex, and expanded it
      repeatedly, according to the rules in the previous article. We’d
      get a sequence of larger and larger patches of tiling made from
      the nine hex types. Each one would be the
n
th-order
      expansion of the original Y hex; each one would contain, within
      it, many Y hexes of the smallest size; and in each of these
      patches, one particular Y hex would be the one that was child #7
      of child #7 of child #7 of … of child #7 of the starting Y hex.
Expanding a Y hex twice, identifying the 7.7 child
Now suppose that we overlay all of these larger and larger
      patches on top of each other, so that the special ‘child
      #7
n
times’ hexes all occupy the same position, with the
      same orientation. When any two patches overlap, they must agree
      with each other, so you never get any tiles partially
      overlapping. Then we do the final expansion from hexes to
      Spectres, and the same thing happens. You can see the result
      being built up gradually here, by selecting the radio
      buttons to advance through the images:
Overlaying all the iterated expansions of Y via its child #7
(The expansion from hexes to Spectres has flipped the
      orientation of everything; sorry about that!)
The union of all those finite tiling
      patches covers an infinite region of the plane. Every tile in
      that region is
required
to exist, as a consequence of
      the original premise that there existed a tile whose infinitely
      long coordinate string repeated “child #7 of a Y” forever.
But it’s not the
whole
of the plane. There’s a
      complicated crinkly boundary, and
none
of our finite
      tiling patches specifies anything on the far side of it!
We already know that if you try to cross edge #4 of that
      original, central, lowest-order Y hex, the coordinate transition
      algorithm will recurse for ever. This isn’t an isolated
      phenomenon. It’s also true of every
other
edge on the
      same boundary. Every tile in this whole infinite region has
      coordinate string that is
eventually
of the form “Y
      that is child #7 of a Y” repeating out to infinity, and every
      edge on the boundary is part of edge #4 of a sufficiently
      high-order one of those Y hexes. As you move further and further
      around the region, more and more of the
low
-order
      coordinates vary, but only finitely many. Every tile’s
      coordinates eventually settle down to the same ultimate
      repetition, in the limit. So
any
attempt to get the
      recursive algorithm to cross that boundary will end up, sooner
      or later, trying to cross edge #4 of one of the higher-order
      expanded Y hexes, and get into the same infinite loop.
In my imagination, I like to think of the Spectre tiling as
      being like a landscape of fields, with shallow walls between
      them. Around the edge of the expansion of each lowest-order
      metatile, imagine a wall of height 1; around the edge of
      each
second
-order metatile, some of those walls grow to
      height 2; third-order metatile boundaries have height 3, and so
      on. If you imagine walking around that landscape using the
      recursive coordinate transition algorithm, the height of each
      wall indicates how many recursive steps the algorithm needs to
      make, before it can climb all the way over the wall to get to
      the other side.
Artist’s impression: walls the recursive algorithm must climb over
It’s easy to imagine that
all
the walls might have
      finite height. And in many of the possible tilings of the whole
      infinite plane with Spectres, that’s true. But in
      this
particular
tiling, containing our endless “child
      #7 of a Y” tile, it isn’t true. In
this
tiling, there’s
      an
infinitely high
wall, extending forever in both
      directions (although not in a straight line).
YOU CANNOT PASS! A wall the algorithm can’t climb at all
Now I hope you see why I was fascinated by this crash. A
      routine kind of question that I’ve been dealing with all my life
      – “why isn’t my program working?” – had turned into a much
      more interesting question.
What’s on the other side of that
      wall?
What’s on the other side of the wall?
Having asked myself that question, now I had to try to answer
      it!
If you’re investigating a particular tiling of the plane with
      Spectres (or Penrose tiles, or hats) and you find one of these
      infinite supertile boundaries barring your way, what does it
      mean? Can the partial tiling on one side of the boundary be
      extended to a tiling of the whole plane, filling in the far
      side? If so, is there a unique way to do it?
Existence?
A natural first thought is: who says there’s
anything
on the far side of the wall?
Perhaps, when you find an infinitely high boundary in your
      tiling, it’s an indication that your attempt to tile the whole
      plane has simply
failed.
Perhaps it will turn out that
      there’s
no
possible way to tile the whole plane by
      extending the partial tiling you’ve got so far. Perhaps the only
      thing you can do is to back up and try again, this time not
      choosing such a silly sequence of starting coordinates.
That’s certainly a possibility I considered. But I wasn’t
      convinced I believed it, for two reasons.
One reason has to do with the self-similarity of these tilings.
      For any
finitely long
section of the infinite wall in
      the previous section, you can find a finite patch of tiling
      containing a section looking just like it, by taking only a
      finite number of coordinates to be “child #7 of a Y”, and after
      that, choosing some other coordinate that makes the recursion
      terminate. And there will be a perfectly sensible answer to the
      question of what’s on the far side of that
finite
piece
      of wall.
In other words, you can find valid
pieces
of Spectre
      tiling that fit perfectly to the far side of the wall. Each of
      those pieces is finitely large, but they’re unbounded in size:
      you can find one with any finite size you like, no matter how
      big.
That doesn’t guarantee that all those finite pieces agree with
      each other. Or even that some
subset
of them agree with
      each other well enough to form a consistent tiling of the whole
      plane. But there’s no guarantee that they
don’t
,
      either. So we shouldn’t automatically assume that there’s no
      possible answer.
The other reason I had for optimism is that I thought of a case
      I
could
answer. If we swap from the Spectre tiling to
      one of the Penrose tilings, there are analogous cases in which
      there
definitely is
something you can put on the far
      side of the wall. I’ll show one.
In my
previous
      article
I handled Penrose tilings by dividing each one into
      two isosceles triangles, because that way the substitution
      system is particularly simple: each triangle expands into either
      2 or 3 smaller triangles exactly covering the same area. Here’s
      a reminder of the substitution rules for the P2 tiling (the one
      with kites and darts).
P2 substitution rules
Suppose we start with the type-A triangle, and expand it twice.
      Part way along the expansion of edge #1 of the original
      triangle, we see a smaller type-A triangle, with edge #1 on the
      exterior. Its coordinates within the larger triangle are AB:
      that is, it’s the A child of the B child of the larger A.
Expanding an A triangle twice, identifying the AB child
Now we do the same as we did with Spectres in the previous
      section. We iterate that double-expansion step repeatedly,
      obtaining larger and larger triangular patches of tiling; in
      each of those patches, we focus on the particular type-A
      triangle which has the above relationship to its parent in every
      double-expansion, so that its coordinates within the starting
      triangle are of the form ABAB…ABAB. Then we overlay all our
      finite patches in such a way that our designated triangle is
      always in the same place.
Overlaying P2 triangles expanded from prefixes of ABABAB…
Just as in the previous section, this construction
      covers
part
of the plane with P2 tiles. That central
      triangle has an infinite coordinate string consisting of endless
      repetitions of ABABAB… forever. All the other triangles in this
      half-plane have coordinate strings differing in the low-order
      components, but they all
eventually
settle down to
      repeating ABABAB forever. And the boundary of our half-plane –
      drawn in a thick line at the bottom of the image sequence above
      – is an infinitely high wall, which the recursive algorithm
      can’t step across, because as soon as it got to the trailing
      ABABAB… section of the coordinate string, it would be trapped
      into an endless recursion, just as in the Spectre case.
But the difference between this and the Spectre case is that
      for
this
partial tiling, we can easily construct
      something from first principles that fits on the other side of
      the line.
Just take the mirror image!
You can see from the expansion diagrams above that the four
      triangle types come in two mirror-image pairs: A and B are
      mirror images of each other, and so are U and V. And the edge
      constraints permit edge 1 of an A triangle to connect to edge 2
      of a B triangle, i.e. to its mirror image.
The expansions of the triangles are symmetric in the same way:
      the expansion of the mirror image of a triangle is the same as
      the mirror image of its expansion. Therefore,
      the
n
th-order
expansion
of an A triangle must be
      able to connect to the corresponding expansion of a B, in the
      same way: everything along that edge must fit correctly.
But
everything
along our boundary edge is part of an
      iterated expansion of edge 1 of an A triangle. That’s how we
      constructed it in the first place. So the
whole
      boundary
must be able to fit alongside its mirror
      image.
So if we simply reflect our half-plane of tiling in the
      boundary, transforming triangle types A↔B and U↔V in the
      process, we obtain a second half-plane that is guaranteed to fit
      alongside the original one:
Reflection-symmetric P2 tiling
So we’ve successfully constructed a Penrose tiling of the whole
      plane, extending the half-plane. If you try to move around this
      tiling using the recursive coordinate-transition algorithm,
      there’s still an infinitely high wall down the middle which the
      algorithm can’t climb over – but now the wall is transparent,
      and we can see through it to the mirror-image world on the far
      side. So at least we know there’s
something
there.
Moreover, we know what
combinatorial coordinates
must
      be of the triangles on the far side of the wall. They’re the
      mirror images of the ones on the near side.
What’s on the other side of the wall from that starting type-A
      triangle whose coordinates go ABABAB… forever? It’s a type-B
      triangle whose coordinates go BABABA… forever. The recursive
      algorithm can’t compute that, but it begins to look as if
      it’s
true
, none the less.
Perhaps we’re looking at a limitation of the recursive
      algorithm in particular, and not a fundamental uncomputability.
      Perhaps there’s a more sophisticated algorithm that we can use
      instead of the recursive one, which
can
step through
      these walls?
Uniqueness?
In that example, I haven’t really proved that
the
neighbour of ABABAB… is BABABA…. All I’ve proved is that
one
      possible
neighbour of ABABAB… is BABABA…. So the next
      question is: might there be other possibilities? Put another
      way: is it possible that
more than one
half-plane of P2
      tiling would fit perfectly next to the half-plane we constructed
      in the previous section?
To begin answering that question, let’s go back to something I
      said at the start of the previous section. I said: given any
      finitely long segment of one of these infinitely high (and
      infinitely long) boundaries, you can find finite patches of the
      tiling containing a
finitely
high boundary of the same
      shape as that segment. And it’s perfectly possible to use the
      recursive algorithm to cross
that
wall, because it only
      needs to recurse for finitely many steps. So perhaps we could
      generate some examples of those finite patches, and see if they
      all look consistent with each other.
This is an easy experiment to try, because all it needs is the
      code I already had for
randomised
coordinate
      transitions. We just make a set of coordinates that repeat
      ABABAB for some finite number of iterations, and then ask the
      randomised transition algorithm to tell us what’s on the other
      side of edge #1 of the lowest-order A triangle – under the usual
      rules that if (or rather, when) it recurses beyond the end of
      the finite coordinate string we’ve provided, it’s allowed to
      invent further parent tile types at random until it finds one
      that terminates the recursion. So the
input
coordinate
      string is extended by a few levels, and we get an output string
      that matches it.
If you try that, you get answers looking like this:
Input string
Output string
ABABABABABABABABABABABBBB
BABABABABABABABABABABAAAB
ABABABABABABABABABABABBA
BABABABABABABABABABABUUA
ABABABABABABABABABABABAVVB
BABABABABABABABABABABABAAB
ABABABABABABABABABABAVVB
BABABABABABABABABABABAAB
ABABABABABABABABABABABBBA
BABABABABABABABABABABAAAA
ABABABABABABABABABABAAV
BABABABABABABABABABAVVV
ABABABABABABABABABABABAAV
BABABABABABABABABABABAVVV
ABABABABABABABABABABAAB
BABABABABABABABABABAVVB
ABABABABABABABABABABAVBA
BABABABABABABABABABABUAA
ABABABABABABABABABABAVVV
BABABABABABABABABABABAAV
Example transitions across edge 1
        of
ABABABABABABABABABAB
with a random
        suffix
In this list,
every
output string starts with BABABA….
      So did the rest of the 1000 example strings I generated. And if
      you increase the number of copies of ABABAB at the start of the
      input string, then the number of BABABA at the start of the
      output string increases by the same amount.
If you interpret each of these random transitions as describing
      a finite patch of tiling with a line through it mimicking our
      infinite boundary, then this is saying that
all
those
      finite patches have something on the far side of that line
      matching our mirror-image half-plane.
This certainly makes it
look
as if the far side of the
      boundary is unique. If there were another equally valid
      half-plane of tiling we could put there, then surely we’d expect
      this random generation experiment to generate
some
patches consistent with the mirror-image half-plane, and some
      consistent with whatever the alternative was.
We can do the same experiment with the original Spectre
      example. I won’t list the example coordinate strings, because
      they’re longer and uglier in the Spectre system (you have to
      specify the child index
and
the parent type at every
      step, because just saying the tile type leaves some
      ambiguities). But the upshot is that if you generate random
      transitions across edge #4 of a Y hex that is child #7 of
      another Y, and so on for a large finite number of iterations,
      the answers all start off by saying that you come in to edge #3
      of an S hex that is child #3 of another S hex, and so on. So, in
      that situation too, it
looks
as if there might be a
      unique “other half” of the plane, that fits perfectly to the
      opposite side of our original wall.
But this is a long way from proving it! All we have here is
      some probabilistic experimental evidence.
Computing coordinate transitions on line
Let’s forget for a moment that we haven’t
proved
any
      of these observations, and think about what it might mean if
      they turn out to be true.
The recursive algorithm for computing coordinate transitions
      generates the very first symbol of the output
      string
last
. It recurses along the input coordinate
      string to the point where it finds a transition within a tile
      expansion (rather than off the edge of one), and then it turns
      round and unwinds its stack, generating the symbols of the
      output coordinate string in reverse order.
But in the previous section, it appeared that a transition
      across edge #1 of a Penrose half-tile with coordinates starting
      ABABAB…
always
delivers output starting with BABABA….
      Assuming that’s true, it shouldn’t be necessary to go all the
      way to the end of the recursion to find out how the output
      string starts. As soon as we’ve seen the first few symbols of
      the input string, we
already
know the output string is
      going to start with a B, no matter
what
happens later
      on in the string. At some point very
early
in the run,
      our algorithm has seen enough information that it “ought” to be
      able to know that, even though it won’t actually get round to
      working it out until the end of its run.
So it might be possible to rewrite our coordinate transition
      system as an
on-line algorithm:
one which can begin
      producing output even before it’s seen all of its input. You
      feed in the coordinates of your input string one by one, and at
      some point, it knows the first coordinate of the output string,
      and can print it. Keep feeding it input, and it keeps producing
      output.
The algorithm’s output certainly won’t be able to keep pace
      precisely with the input. Sometimes it will need to look a few
      symbols ahead in the input, before it can be sure of the next
      output symbol. So the output will lag behind the input.
But if things always work the way they seem to in this
      ABABAB… → BABABA… case, then we can hope the lag will be
      bounded. That is, there will be some number
k
such that
      we can always know the first
n
symbols of the output if
      we’ve seen
n
+
k
symbols of input.
If the lag is bounded, then that suggests that the algorithm
      should only need to remember a finite amount of information from
      what it’s already seen. In other words, maybe it can be modelled
      as a finite state machine.
Of course, this is all speculation: we haven’t proved that
      this
will
work. We’ve just seen some evidence
      suggesting that it
might
. But techniques for building
      finite state machines are self-checking: if they don’t work,
      they report failure or run for ever, and don’t output an
      incorrect result. So we don’t need to prove in advance that this
      idea will work. We can just
try
to construct a finite
      state machine for doing this job, and see if it
turns
      out
to work!
Building a finite-state transducer
The most common type of finite state machine, seen in regular
      language theory, is a
recogniser
: you feed it an input
      string, and the only output it generates is “yes” or “no”, at
      the end, if the string matched the language it recognises. But
      here, we want to convert our input string into an entire output
      string, so we need a different type of finite state machine,
      called a
transducer
. In a transducer, each state
      transition is annotated with a string of output (maybe one
      symbol, or more than one, or sometimes the empty string): when
      the machine’s input causes it to take that transition, it writes
      the corresponding output.
To build one of these, we use similar techniques to the
      standard NFA→DFA conversion used in regular language theory. But
      first we need some preparation.
Adjacency recogniser
We begin by making an ordinary (recogniser-style) finite state
      machine, whose job is to detect
whether
two input
      coordinate strings are adjacent to each other. That is, if you
      feed it both the input
and
the output of any successful
      run of the recursive algorithm, it should report “yes”, and if
      you feed it any other pair of coordinate strings, it should
      report “no”.
The recogniser will receive the two strings in an interleaved
      form, so that each ‘symbol’ consists of a pair of coordinates,
      one from each string. Also, the initial input symbol must
      include the edge indices of the input and output tile, because
      those are a vital part of the input and output of the transition
      algorithm, along with the tile coordinates.
We’ll continue to use P2 as our example tiling. Here’s a
      randomly generated input and output pair from the recursive
      algorithm: edge #1 of a triangle with coordinates ABBU should
      connect to edge #2 of a triangle with coordinates BUUU. If we
      fed that to our adjacency recogniser, it would receive a
      sequence of symbols looking something like this:
(A, 1, B, 2) – the type of the two lowest-order triangles,
        and which edges of the former and the latter are claimed to be
        adjacent
(B, U) – the first-order supertile type in each string
(B, U) – the second-order supertile type in each string
(U, U) – the third-order supertile type in each string
and, since that’s where the recursive algorithm finished having
      to recurse, we’d expect the adjacency recogniser
      to
accept
at this point, and report “yes, these two
      strings match correctly.”
This adjacency-recognising state machine is reasonably simple
      to generate directly, starting from the transition maps of the
      Penrose triangles, which I show again here for convenience:
P2 transition maps
The basic idea is that the state machine is divided into two
      similar parts, each one corresponding to
one
of the two
      input strings. Each sub-machine consumes the half of the input
      symbol that relates to its own string, and keeps track of what
      triangle type it’s in, and where in that triangle it is. Then
      they ‘compare notes’ at each step to make sure they remain
      consistent.
The best way to show this is to illustrate how the machine
      thinks, as it works through an example. Here’s the way it
      processes the string above:
Steps through the adjacency recogniser in an example case
What’s going on in those diagrams:
Receive the input symbol (A, 1, B, 2). So the left
        sub-machine is trying to go out of edge #1 of an A, and the
        right one is trying to go out of edge #2 of a B. So far, so
        good: those are the same
type
of edge – the tiling
        rules permit them to connect.
Receive the input symbol (B, U).
On the left, the A is now known to be part of a larger
            B; on the right, the B is part of a U. Both target edges
            are on an edge of the larger triangle; they’re part of the
            same edge type of the larger triangle; that edge is
            divided into two pieces in the expansion, and the two
            sub-machines agree on which part of the edge they’re going
            out of (namely the top half, when the two are shown facing
            each other as here). In other words, this looks good:
            everything matches.
So now we forget about the smaller triangles, and focus
            on the next layer up. All we remember is that the left
            sub-machine is trying to go out of edge #2 of a B, and the
            right out of edge #0 of a U.
Receive the input symbol (B, U).
On the left, the previous B is part of another larger B;
            similarly on the right, the U is part of a larger U.
            Again, we’re on the edge of the larger triangle in both
            cases (this time, the
whole
edge, not part of
            it), and the edge types match.
Again, forget about the smaller triangles and move up.
            Now the left sub-machine is trying to go out of edge #0 of
            a B, and the right out of edge #1 of a U.
Receive the input symbol (U, U). Now both sides are trying
        to make a transition in the
interior
of a U triangle.
        On the left, we’re trying to cross from the B sub-triangle
        into the U; on the right we’re going from the U into the B. In
        other words, the two sides are crossing the
same edge
inside the expansion, in opposite directions. Success! The
        machine accepts.
(Compare this with how the simpler recursive algorithm would
      handle the same coordinate transition. As it recurses deeper and
      deeper, it imagines the left-hand diagram in each of the above
      steps; when it reaches a transition within the top-level U
      triangle, it terminates the recursion, and as it unwinds its
      stack, it goes through the right-hand diagrams
in reverse
      order
, calculating the output coordinates from largest to
      smallest.)
In other words, each state of the adjacency recogniser consists
      of two (tile, edge) pairs, one for each of the input strings. To
      compute each state transition, you use each half of the input
      symbol to locate one of those (tile, edge) pairs in a supertile.
The first thing you find out is whether the edge of the
      previous tile is on the outside of the new expansion, or on the
      inside. If it’s on the inside (as in step 4 above), we’re making
      a transition entirely
within
a supertile – or, at
      least,
that
half of the machine thinks so. So you check
      that the other half agrees, and that the positions within the
      supertile match, and then accept.
Otherwise, you’re making a transition
out
of the
      supertile. So again you check that the other half agrees, and
      that the details of the new edges make sense, and then you make
      a state transition to two (tile, edge) pairs representing the
      supertiles, ready for the next input symbol.
If the states
aren’t
consistent, for any reason, then
      the adjacency recogniser rejects the input string. This can
      happen in lots of ways:
One half of the machine believes it’s trying to make a
        transition
within
its supertile, while the other half
        thinks it’s trying to step off the edge of its supertile.
Both halves are trying to make a transition within a
        supertile, but the two supertiles aren’t the same type.
The two supertiles are the same type, but the two positions
        within it don’t match – they’re not opposite sides of the same
        edge within the supertile’s expansion.
Both halves are trying to step off an edge of the supertile,
        but the types of the supertile edges don’t match – they aren’t
        edges that the tiling rules would ever allow to connect.
The supertile edge types do match, but that supertile edge
        is divided into multiple sub-edges in the expansion, and the
        two halves aren’t trying to cross the same sub-edge. For
        example, in step 2a above, if one side had been trying to
        cross the longer top section of the edge and the other the
        shorter bottom section.
We’ll need to add complications later, when we tackle more
      difficult tilings. But for Penrose tilings, which are the
      simplest, this is enough.
One last thing: the plan is for all this machinery to end up
      handling
infinitely long
sequences of coordinates. So
      after the machine ‘accepts’ after finitely many steps, as it did
      in step 4 in our example above, its job isn’t done! If you’ve
      found a pair of finite coordinate strings that map to each
      other, then a pair of
infinite
coordinate sequences
      starting with those prefixes are also legitimately
      adjacent,
as long as the remainder of the two sequences are
      identical
. So even the accepting states of the adjacency
      recogniser still need to do work: their remaining job is to
      receive an input symbol, check that the two halves of it are
      identical, and reject if not. (Also, check that it even makes
      sense – that is, the new supertile is consistent with the
      previous tile.)
Reinterpret the recogniser as
      a non-deterministic transducer
Now we’ve got a state machine that can take two input
      strings
s
and
t
, and tell us
whether
t
is the correct output of a coordinate transition
      starting from
s
. But what we want is a machine that can
      take
s
by itself as input, and generate
t
as
      output.
In a sense, we’ve already got one!
We take our adjacency-recognising machine, and
      simply
reinterpret
one of the strings as its output.
      That is, in each state transition triggered by a particular pair
      of symbols (
x
,
y
) from the two input strings, we
      pretend it’s a state transition triggered by just the
      input
x
, generating
y
as output.
The problem with this is that now our machine
      is
non-deterministic
. As an adjacency recogniser, it
      was deterministic: given any input symbol pair, there was only
      one transition the machine could possibly take. (Or none, if the
      input was illegal.) But there will be plenty of cases where
      inputs (
x
,
y
) and (
x
,
z
) both trigger
      different valid transitions from the same state
i
, say to
      states
j
and
k
respectively. So if we reinterpret
      the machine description so that only
x
is the input, then
      we have two possible transitions: we could go to state
j
and output
y
, or to state
k
and output
z
,
      and we don’t have enough information to know which is right.
Of course, this is what we expect. We already know that there
      are cases where the
n
th output coordinate can’t be
      determined from just the first
n
input coordinates; the
      algorithm will sometimes have to look further ahead to find out
      which of multiple possibilities is right. The nondeterminism in
      this machine exactly reflects that: we expect there to be
      exactly one correct output
in the end
, but at the
      moment we take a transition on each input symbol, we don’t
      always know what it is.
Then make it deterministic
How do you turn a non-deterministic finite state transducer
      into a deterministic one? Pretty much the same way you do for
      recognisers.
In regular language theory, there’s a standard construction
      that turns a non-deterministic recogniser (in this context often
      called ‘NFA’, for Nondeterministic Finite Automaton) into a
      deterministic one (‘DFA’). The trick is that each DFA state
      represents a
set
of possible states of the NFA, with
      the semantics “My NFA must be in
one
of these states,
      but I don’t know which.” You compute a transition between DFA
      states by going through every NFA state in the source set, and
      following
all
possible transitions from any of those
      states on the input character, to construct the set of NFA
      states you could possibly be in after seeing that character.
      Then you look for a DFA state corresponding to that set, or make
      a new one if it doesn’t already exist, and that’s the
      destination of this state transition in the DFA.
Essentially the same technique works for transducers, except
      that we have to deal with the extra complication of the output.
      If we collect a set of possible NFA transitions, and they don’t
      all produce output, or don’t all produce the
same
output, what do we do about it?
Answer: instead of each DFA state representing a set of NFA
      states, it represents a set of pairs (
i
,
p
),
      where
i
is a state of the NFA, and
p
is a string
      of
pending output
. The pending output was generated by
      whatever path through the NFA we followed to get here, but it
      hasn’t yet been emitted from the DFA, because we’re not yet sure
      whether
that
path was the right one.
Then, if our source set contains a pair (
i
,
p
),
      and NFA state
i
contains a transition on the input symbol
      which goes to NFA state
j
and outputs some data
x
,
      we enter the pair (
j
,
p
+
x
) into our
      destination set. So we haven’t actually
emitted
the
      output for that NFA transition: we’ve just appended it to the
      end of our “pending” string.
For example, here’s a tiny made-up fragment of nondeterministic
      transducer:
On each edge, the input symbol is written in black, and the
      output in red. So this says that from the start state 0, on
      receiving the input symbol ‘a’, we can either go to state 1 and
      output ‘x’, or to state 2 and output ‘y’.
When we make a deterministic machine out of this, we’ll have an
      initial DFA state {(0, “”)} (simply being in state 0 with an
      empty output string). On the input symbol ‘a’, it will
      transition to {(1, “x”), (2, “y”)}, which says that we followed
      one of those two transitions, but don’t know which yet. This
      also means we don’t yet know what the NFA’s output will turn out
      to have been – so our DFA can’t emit any output at all on this
      state transition. It has to wait to see what comes next before
      it knows which of ‘x’ and ‘y’ starts the output string.
Once we’ve constructed the complete set of pairs that
      correspond to our destination DFA state, we do one extra step.
      We collect together the pending output strings from all the
      pairs we have, and see if they all start with a common prefix.
      If they do, then that prefix is guaranteed to be the right thing
      to output next, no matter
which
of these NFA states
      we’re in. So we remove that common substring from the pending
      output of every pair, and write it into our DFA state transition
      as
actual
output.
Then
we find, or make, a DFA
      state corresponding to the set of pairs we have left. So the DFA
      we construct will produce each symbol of output as soon as it’s
      sure what it is – as soon as it’s ruled out every case where
      some other symbol might have been correct.
Suppose the example fragment above continued like this:
From the DFA state {(1, “x”), (2, “y”)}, what should we do on
      the input symbol ‘b’? From state 1 we can take the transition to
      state 3, outputting ‘z’, or to 4 outputting ‘w’; from state 2 we
      have no options at all. So we make the set
      {(3, “xz”), (4, “xw”)}. But in that set,
all
the
      possibilities have ‘x’ as the first character of the output. So
      we remove it from all of them, and emit it as output from the
      DFA, because we’re now sure of it. So instead of making a DFA
      state for {(3, “xz”), (4, “xw”)}, we make one for
      {(3, “z”), (4, “w”)}, and on the transition to it the DFA
      outputs ‘x’.
On the other hand, if we’re in {(1, “x”), (2, “y”)} and we see
      the symbol ‘c’, then there are no possible transitions from NFA
      state 1, and the only thing we can do is to travel from 2 to 4,
      outputting ‘y’. So we construct the set {(4, “yy”)}. But now
      everything in our set agrees that the first
two
characters of the output should be “yy”, because there’s only
      one thing in the set. So on this DFA transition we generate the
      two output characters “yy”, and move to a DFA state representing
      {(4, “”)}.
So the DFA fragment constructed from the NFA fragment above
      would look like this:
If we feed “ab” to this machine, then it outputs ‘x’ on the
      second transition, but still isn’t sure which of ‘z’ and ‘w’
      comes next. But if we feed it “ac” then it can produce the full
      output string “yy”, and end up with no output still buffered.
Then, just like the more usual subset algorithm for making
      recogniser DFAs, we keep on going: for every DFA state we’ve
      generated, we compute all the outgoing transitions, and whenever
      one goes to a DFA state we haven’t explored yet, we queue it up
      to investigate later. Repeat until we’ve explored all reachable
      states, and the algorithm terminates.
There’s only one problem with this algorithm: it’s
      not
guaranteed
to terminate!
When you do this for recognisers, it
is
guaranteed to
      terminate, because if the number of NFA states is finite, then
      so is the number of possible
sets
of NFA states. The
      DFA might be exponentially large compared to the NFA (and in
      occasional nasty cases that actually happens), but sooner or
      later, the construction algorithm will run out of ways to
      generate a new DFA state that doesn’t match any of the existing
      ones, so the algorithm will terminate, and the output machine
      will be finite.
But here, our DFA states aren’t sets of NFA states; they’re
      sets of pairs each containing an NFA state
and a
      string
. And strings can be as long as you like, so the set
      of possible pairs is infinite. So there’s no guarantee that the
      procedure terminates after constructing a finite number of
      states. It might continue forever, constructing DFA states
      containing longer and longer strings of unemitted pending
      output.
But it’s worth a try! We can run the algorithm and
see
if it works.
An example transducer
And it does! Running this algorithm on the triangle-based P2
      substitution system, it terminates and reports success.
The resulting state machine has 31 states. I show it as a
      Graphviz diagram here just to prove that it exists, but I don’t
      expect it to be very informative, because Graphviz makes an
      impenetrable tangle of it, and I haven’t found any nicer way to
      lay it out:
Transducer for P2 half-tile triangles
The starting state is state 0, at the top. As in the previous
      section’s examples, edges are labelled with their input symbol
      in black, and output symbols (if any) in red. The first input
      symbol consists of a tile-type letter and an edge number, like
      A2 or V1; after that, all further input symbols are just single
      letters. The same is true for the output symbols.
The four nodes at the bottom with double-circle outlines are
      accepting states. If you reach any one of these, then the
      transducer has reported success: it’s consumed enough of the
      input string to complete a coordinate transition, and generated
      the corresponding output, just the same as the recursive
      algorithm would.
Of course, your actual tile coordinate string might contain
      more coordinates than a given transition needed to modify. In
      that situation, you’d want to copy the remaining unchanged
      coordinates from the input into the output. For that purpose,
      the accepting states have those state transitions written out
      explicitly, so that if you prefer, you can keep running the
      state machine, ignoring the fact that it’s now in an accepting
      state.
(There are multiple accepting states so that each one can
      reject input coordinates that don’t make sense at all, such as
      claiming a U tile has parent B. There’s one accepting state for
      each triangle type, and each one has transitions for only the
      triangle types which can sensibly be a parent of its own type.
      So those four states between them form a little secondary state
      machine which recognises legal coordinate strings.)
Using the transducer
OK, now we’ve proved the concept, by successfully making a
      transducer for at least one tiling. What’s it good for?
A better alternative to the recursive
      algorithm
Firstly, and most obviously, you can use this in place of the
      recursive algorithm I described in my previous articles, if
      you’re trying to generate random patches of tiling.
That is: given a finitely long coordinate string of a tile and
      an edge of that tile to traverse, you feed it to the transducer,
      symbol by symbol, and concatenate the symbols that come out. The
      result will give you the coordinates of the neighbour tile, and
      which edge of that one is adjacent to the edge you originally
      specified.
If all goes well, the transducer reaches an accepting state.
      This should be a state of the DFA in which every (state, pending
      output) pair describes an accepting state of the adjacency
      recogniser, with the pending output string empty. In other
      words, the input and output strings so far are precisely a pair
      you could have got from the recursive algorithm – if you’d given
      it that input, it would have returned you that output, without
      having to look at any further symbols than the ones you’ve
      already seen. So you can proceed just as if the recursive
      algorithm had returned success: if there are any further
      coordinates in your input string, copy them to the output
      unchanged, and you’re done.
But, just as in the previous articles, there’s a risk that you
      reach the end of the finite coordinate string before that
      happens. So you respond in the same way as before: choose an
      extra higher-order supertile at random, pretend it was there all
      along, and feed it to the transducer as an extra input. If it
      still hasn’t accepted, do the same thing again. Sooner or later
      you’ll get lucky – just as, sooner or later, generating these
      same extra coordinates in the middle of the recursive algorithm
      would manage to find one that terminated the recursion.
What are the advantages of doing this job with a transducer
      instead of recursion?
Simpler lookup tables
. In the recursive
      algorithm you need multiple complicated tables, one way or
      another. At least one table per tile; maybe separate tables for
      transitions within a tile and transitions into it from outside;
      for the hat system’s overlapping metatiles you need those
      ‘metamaps’ that show how to compute the redundant
      representations of a coordinate string. Here, there’s
      just
one
lookup table, indexed by your current state
      and the next coordinate symbol.
Guaranteed linear time in the string length
.
      The recursive algorithms I’ve described sometimes need to
      recurse multiple times. In the hat tiling, you might need to
      recurse back and forth around the string rewriting coordinate
      pairs using the metamap, until you find one where you can make
      the lowest-level transition without falling off the edge of the
      kitemap. In the Spectre tiling, you might need a second
      recursive call due to the zero-thickness spur in one of the
      expansion diagrams. Only the Penrose tilings are simple enough
      not to have either of these problems.
But processing a string with a finite state
      machine
never
has to backtrack. If you feed it
N
input symbols, it gives you
N
output symbols
      in
O
(
N
) worst-case time, no matter what.
(However, those awkward properties of the tiling still make
      life difficult! But the difficulty happens at the point when
      you
construct
the state machine. Once you’ve managed
      that, using it at run time is the easy part. I’ll discuss the
      difficulties in later sections.)
Constant memory usage
. Of course, a recursive
      algorithm that recurses
N
levels deep
      requires
Ω
(
N
) stack to store the state of where it
      had got to. A finite state machine doesn’t need to remember
      where it was in all the previous characters of the string – it
      has already produced output for most of them and forgotten about
      them completely.
Unified algorithm for all systems
. There’s
      only one way to feed a string to a transducer. So you can write
      a single engine for doing it, and use it for any tiling system
      that this method can handle. No special-case code per tiling,
      like the metamap business in my original hat algorithm.
None of these is a
huge
advantage. The lower space and
      time costs are a nice improvement in theoretical terms, but in
      practice, your coordinate strings are all short enough that it
      doesn’t matter a great deal (because they grow like the log of
      the size of patch you’re generating). I think the software
      engineering advantages are more important than the performance:
      only one piece of code to handle all tilings, and it’s very
      simple.
But even if all these advantages are small, they all point in
      the same direction –
all
of them are in favour of using
      a transducer instead of recursion. So this is my new recommended
      approach for generating random tiling patches, if you’re in a
      position to use it.
Infinitary transition algorithm for eventually periodic coordinates
But I didn’t go to all this effort just to slightly optimise
      something I already had a way to do. I wanted to do the
      impossible! We wanted this transducer so that it can
bypass
      those infinitely high walls.
So, what happens if we ask this state machine to try to cross
      the wall in our symmetric Penrose tiling, by asking it to cross
      edge #1 of a tile whose coordinates are an infinitely long
      string endlessly repeating ABABABAB…?
We can go through the state machine diagram above, and figure
      it out:
Start in state 0.
Feed in the symbol A1 (starting tile type and edge to
        cross), which takes us to state 8, emitting no output yet.
Feed in B, which goes to state 23, outputting the symbol B2.
Feed in A, which goes to state 20, outputting A.
Feed in B, which goes to state 23, outputting B.
Now we’re back in state 23, which is the same state we were
        in two symbols ago; and we’re about to feed in another
        instance of AB, just as we did last time. So it’s clear that
        we’re going to repeat the previous two transitions and their
        output, and then keep doing that. So, from here on, we expect
        output A,B,A,B,… forever.
In other words, we’ve managed to describe the
infinite
output string corresponding to the infinite input we had in
      mind. If our input string goes A1 B and then repeats AB forever,
      then the output string starts B2 A, and then repeats BA forever.
      In other words, if you cross the infinite wall at edge #1 of the
      tile with coordinates ABABAB… then you end up coming in through
      edge #2 of a tile with coordinates BABABA….
And that’s exactly the string we thought it should be, from the
      symmetry argument. But this time, we
computed
it,
      without having to depend on symmetry. So this technique can
      still generate an answer in cases that aren’t symmetric.
To use this ‘infinitary’ version of the coordinate transition
      algorithm, you have to be able to represent an infinite input
      string in a finite amount of space, and also work out a
      representation for the output string. We did that in the example
      above by knowing that the string was going to end up repeating
      itself.
In other words, suppose you start with an
eventually
      periodic
coordinate string, represented by two finite
      strings (
s
,
r
), describing an infinite string that
      starts with a copy of
s
and then repeats
r
forever. Then you can feed any string of that form to this
      transducer, and generate an output string in the same form, by
      keeping track of both your position in
r
(once you reach
      it at all) and the current state of the transducer. When both of
      those variables are in a state they’ve been in before, you know
      that the machine will spend the rest of eternity generating more
      copies of whatever output it’s produced since the last time you
      were here. So you can express the output string in the same
      (
s
,
r
) form.
So now we’ve removed the randomness from the coordinate
      transition algorithm, and also eliminated the risk of infinite
      recursion. We can cross those infinitely high walls just as
      easily as finite ones!
Some pretty pictures: pentagonally
      symmetric Penrose tilings
I’ve made you suffer through a lot of maths and computer
      science, so let’s take a break for some pictures.
Using this technique, we can generate specific instances of the
      Penrose tilings, carefully chosen to have symmetry. With the
      recursive algorithm, these would have been difficult, because
      the symmetry tends to give rise to infinite supertile
      boundaries, causing the recursion to fail. But now we have this
      on-line algorithm which can handle infinite boundaries, that’s
      not a problem any more.
We’ve already seen an example of a P2 tiling chosen to have
      reflective symmetry about a single straight line. But we can do
      better than that. There are also two P2 tilings of the plane
      with pentagonal symmetry about a centre point – five-way
      rotational symmetry, and reflection in five axes.
To construct one of those using the new algorithm, all we have
      to do is to work out the combinatorial coordinates of one of the
      tiles at the centre. In this case, the trick is to start with a
      single triangle type, say A, and expand it
four
times.
      After that, one of the corners of the starting triangle will be
      occupied by the same corner of a smaller version of the same
      triangle. So then we iterate that quadruple expansion and
      overlay the larger and larger pieces, just as we did before.
The reason we have to expand four times is because the triangle
      type in that corner cycles through all four triangle types
      before coming back to its starting point. So the coordinate
      string for that triangle will also repeat with period 4. In fact
      it will be AVBUAVBUAVBUAVBU… forever.
Overlaying P2 triangles expanded from prefixes of AVBUAVBUAVBU…
In the previous two cases where we deliberately constructed an
      infinite boundary, it looked as if we’d made a partial tiling
      that filled “half” the plane, in the sense that we only expected
      to need one other partial tiling to fit to it. But in this case,
      we’ve fillled only “one tenth” of the plane – we’re going to
      need nine more rotated and reflected images of this infinite
      sector to fill the rest.
That’s all we need to generate a symmetric tiling: we just feed
      that repeating coordinate into the code, place the corresponding
      triangle somewhere in the middle of the picture, and hit ‘go’!
“Infinite sun pattern”: pentagonally symmetric P2 tiling of type AVBU
I said there were
two
P2 tilings with pentagonal
      symmetry. Given the cyclic coordinate string we have here, it’s
      easy to guess what the other one will be: surely we’ll obtain it
      by starting the same cyclic sequence of four tile types at a
      different point. And indeed, with coordinates VBUAVBUAVBUAVBUA…,
      we get
this
symmetric tiling, which has five darts
      around the centre point instead of five kites:
“Infinite star pattern”: pentagonally symmetric P2 tiling of type VBUA
You might ask: the sequence of coordinates AVBUAVBUAVBU…
      repeats with period 4. So maybe there are two more possibilities
      available by shifting twice more, to get coordinates starting
      with BUAV or with UAVB? Do those give further symmetric
      tilings?
No, they don’t: they give the same two again, rotated by a
      tenth of a turn. Each of the straight-line boundaries in these
      pictures is a line of reflection symmetry, like the one in the
      ABABAB… example in an
earlier section
.
      And just as in that case, the coordinates of each mirror-image
      tile is obtained by swapping A↔B and U↔V. So we’ve already seen
      a triangle with coordinates BUAVBUAVBUAV…: it’s the mirror image
      of AVBUAVBUAVBU…, which we used to generate the first of the two
      diagrams above. The ten sectors of that diagram alternate AVBU…
      and BUAV… as you go round the origin. Similarly, VBUA… is the
      mirror image of UAVB…, so those two tile types alternate around
      the origin of the second image.
That’s enough kites and darts. What about the other Penrose
      tiling, the P3 one made of thin and thick rhombs?
The transducer-constructing algorithm works just as well for
      the P3 tiling as it does for P2. (Not surprisingly, since as I
      mentioned in
      a
previous
      article
, the P2 and P3 tilings can be obtained from
each
      other
by performing a sort of ‘half-expansion’ at each
      step. So if one works, you’d expect the other one to work
      too.)
And just like the P2 tiling, P3 has two particular instances
      with pentagonal symmetry, and you can generate them using
      exactly the same technique. This time, the coordinates of a
      central triangle don’t cycle through the four triangle types:
      instead, they repeat XYYX XYYX XYYX…, or the cyclic variation
      YYXX YYXX YYXX….
As a result,
both
symmetric P3 tilings have five thick
      rhombs around the centre of symmetry, so they don’t look as
      obviously different from each other as the P2 ones! But if you
      look at the pattern near the centre, you can see that they’re
      not the same: in one of them, a ring of thin rhombs encircles
      the middle five thick ones, whereas in the other, ten thick
      rhombs point outwards in a sort of star shape.
Pentagonally symmetric P3 tiling of type XYYX, with a ring of thin rhombs around the centre
Pentagonally symmetric P3 tiling of type YYXX, with a star of thin rhombs around the centre
Building a transducer for the Spectre tiling
I began this article with an example of an infinite wall in the
      Spectre tiling, because that’s the one I noticed first, because
      it happened when I was writing a Spectre generator. But ever
      since then, I’ve been talking about Penrose tilings, because
      those are easier to work with and reason about.
So, now we’ve solved the easy case, it’s time to get back to
      the original more complicated one! Let’s build a finite state
      transducer for the Spectre substitution system.
Spurious construction failure
If you try that in the most obvious way, constructing an
      adjacency-recogniser state machine exactly the way I described
      in
a previous section
,
      something goes wrong. The construction runs successfully, and
      outputs a transducer … but it’s subtly
incomplete
.
      There are valid coordinate strings you can use as input, for
      which the recursive transition algorithm successfully generates
      a result, but which the transducer will reject, because at some
      point it reaches a state where it has no legal transition on the
      next symbol.
The problem arises because of
this
expansion rule in
      the Spectre system, which turns the S hex type into a Spectre,
      but has a zero-thickness ‘spur’ sticking out of one corner:
Hexagon-to-Spectre substitution rule for the S hexagon
As I described in
      the
previous
      article
, the recursive algorithm has to compensate for this
      spur by sometimes calling its recursive
      subroutine
twice
. You try to enter an S hex along edge
      #1, or the wrong part of edge #0, and when you consult the map
      above, you discover you haven’t landed in the actual Spectre,
      you’ve landed on one side of the spur – and so you have to call
      the next-level recursion
again
, to step straight back
      off the other side of the spur and see where you end up after
      that. Crossing the spur costs an extra function call.
But our adjacency recogniser doesn’t know anything about spurs,
      and isn’t set up to account for those extra function calls. So
      if you feed it the input and output of a run of the recursive
      algorithm that had to cross a spur, it will reject that pair of
      strings, when it should have accepted them.
This
particular
spur isn’t too hard to handle, because
      in the Spectre tiling system, the S hex
always
appears
      in that three-hex cluster with a G and D hex, always in the same
      relative orientation:
Expansion of the (G, D, S) hexagon cluster to Spectres, showing where the spur fits
This means that all the edges affected by the spur are on the
      interior of that G,D,S cluster of lowest-order hexes, and all
      three of those hexes will be expanded from the same larger hex.
      So any coordinate transition involving a spur is also going to
      finish without having to recurse higher.
Because of that convenient property, there are two different
      ways we could modify the substitution system itself to make this
      spur go away. We could replace the G, D and S hex types with a
      single combined ‘trihex’ tile, fusing together their expansion
      maps, so that the spur just became a pair of ordinary edges
      between two of the Spectres in the combined GDS expansion.
      Alternatively, we could merge the lowest two levels of the
      substitution system, so that instead of each second-order hex
      expanding into 7 or 8 first-order hexes each of which becomes
      either 1 or 2 Spectres, we’d have a set of transition maps that
      turn second-order hexes
directly
into 8 or 9 Spectres
      each – bypassing the intermediate stage where the spur lives.
But instead, I’m going to show an improvement to the method of
      constructing the adjacency recogniser, which allows it to handle
      this spur completely automatically, with no manual hacking
      needed. This will be useful later, because there will be more
      substitution systems with spurs!
To begin with, let’s see how the existing adjacency recogniser
      would think, if it saw a transition of this kind:
Simple Spectre adjacency recogniser being confused by a spur
What’s going on in the above diagrams:
We receive the starting symbol identifying the potentially
        matching edges: edge #6 of the left Spectre and edge #1 of the
        right.
We receive a symbol telling us that the left Spectre is
        expanded from a D hex, and the right Spectre is #1 of the two
        from a G hex. Edge #6 of the left Spectre is part of edge #0
        of the D hex, and edge #1 of the right Spectre is part of edge
        #4 of the G hex.
So now we’re expecting edge #0 of a D hex to match edge #4
        of a G. But the hex matching rules say they don’t. Reject the
        input string!
The recursive algorithm would also run into this difficulty,
      but it would know what to do. It would know what edge #0 of the
      D hex
does
meet: edge #1 of the S hex. So it would go
      down a layer to find out where in the S
Spectre
it had
      landed. It would find it had landed on the spur – and it would
      recurse back up again to see what was on the far side of the
      spur, and end up finding the G hex, after a detour.
But in this context, we don’t have the luxury of stepping down
      a layer and back up again. An adjacency recogniser has to run in
      a single pass. We have to do something at
this
layer
      that will stop us from being confused about the spur!
The answer is to consider the geometry of the tiles. If edge #6
      of one Spectre coincides with edge #1 of another Spectre, then
      several
other
pairs of edges are required to coincide,
      by the shapes of the tiles. And some of
those
pairs of
      edges correspond to edges of the hexes that
do
officially meet.
Enhanced Spectre adjacency recogniser getting round the spur
The revised algorithm’s thought process goes like this:
As before, we start by trying to match edge #6 of the left
        Spectre to edge #1 of the right.
We find out the parent hex types, and discover that edges #6
        and #1 of the Spectres don’t correspond to matching edges of the
        hexagon. But this time, we don’t give up…
We imagine how these tiles would fit together geometrically.
        If the specified pair of edges meet, then three other pairs of
        edges meet too – and
vice versa
. All four edge pairs
        meet, or none.
So the question “do edges #6 and #1 of these Spectres meet?”
        is equivalent to “do edges #4 and #3 meet?”, or “#5 and #2”,
        or “#7 and #0”. If we can get a positive answer
        to
any
of these questions, we’re good.
The promising edges are #4,#5 on the left and #3,#2 on the
        right, because those are expanded from a different pair of
        edges of the parent D and G hexes: edge #1 of the D and edge
        #3 of the G. It also looks promising that these are
        the
whole
expansion of that pair of edges.
So we pretend those were the edges we’d originally been
        asked about, and proceed on that basis. Now we’re trying to
        match edge #1 of the D to edge #3 of the G – and
        those
do
potentially match!
The adjacency recogniser has kind of ‘slid sideways’ along the
      edges of the two Spectres, to a different pair of edges that
      must meet if and only if the original edges met, and don’t have
      a spur in the way.
With that problem solved, I was able to build a working
      finite-state transducer for the Spectre tiling. The resulting
      state machine has 151 states – nearly five times as many as the
      state machine for Penrose P2 that
      I
exhibited in full above
! That’s
      some kind of a measure of how much more complicated the Spectre
      tiling is than the Penrose ones.
Testing that the transducer is complete
When I found out that my first Spectre transducer didn’t handle
      all possible inputs, it took me by surprise: an attempt to
      generate an actual tiling crashed. You don’t really want to wait
      until run time to find out that kind of problem. You’d rather be
      able to know in advance whether your transducer is complete.
So here’s a technique for testing exhaustively that it’s
      capable of handling all valid input coordinate strings.
You do this by first making a second state machine
      that
recognises
valid coordinate strings. Then you
      analyse the two state machines jointly, by doing a graph search
      over their Cartesian product – that is, the space of pairs of
      states, one from each machine. So you’re generating an
      exhaustive list of states the transducer can be in, for each
      state of the coordinate-recogniser. And then you expect that the
      transducer state should never fail to have a valid outgoing
      transition on a symbol, if the coordinate-recogniser state that
      goes with it has one.
And making a recogniser for valid coordinate strings is no
      trouble at all: you just need one state for every tile type, and
      a transition from each tile type to any tile type that can
      legitimately be its parent. It’s the simplest state machine in
      this whole article.
So now you can automatically
detect
whether your
      transducer is complete. And once I’d added the system above for
      handling spurs, this test passed, where it had previously
      failed. So I was
confident
that I had a working Spectre
      transducer.
It’s also possible to do this same check directly on the
      adjacency recogniser, to see if there’s any input for which it
      doesn’t know of any possible output. Simply discard one half of
      the input from every transition of the adjacency recogniser, and
      you’ve turned it into an ordinary recogniser NFA for the
      language of inputs it will accept. Then you can turn that into a
      DFA, or directly check it against the DFA for legal coordinate
      strings, in exactly the same way.
Crossing infinite walls in the Spectre tiling
Now we have a Spectre transducer, we can go straight to
      generating Spectre tilings using the infinitary algorithm I
      described in a
previous section
.
As before, we represent an infinitely long string of Spectre
      tile coordinates in a form consisting of an initial segment and
      a repeating segment, so that we can represent any infinite
      string as long as it’s
eventually periodic
. Then we
      use the finite-state transducer to convert an eventually
      periodic input string into an eventually periodic output string,
      by detecting when it starts repeating.
We’ll start with the case
      I
originally described
, where
      at every stage of the recursion you’re trying to exit edge #4 of
      a Y hex, and because each Y turns out to be child #7 of another
      Y, this continues forever. When I
      was
experimenting with the recursive
      algorithm
to try to guess what might fit on the other side
      of the resulting wall, it looked as if this boundary might match
      up to one where at every layer you’re trying to exit edge #3 of
      an S hex.
And indeed this is what happens. If we make a coordinate
      description in which each Y hex is child #7 of another Y, and
      ask the algorithm to cross a Spectre edge corresponding to edge
      #4 of the lowest-order Y, then it delivers an output string full
      of S hexes, in which each one is child #3 of another S, just as
      we’d guessed. The resulting full tiling of the plane is shown
      here: the Y side of the wall is the smaller top left region, and
      the rest of the picture is the previously unreachable S side.
Spectre tiling with an infinite (Y, 7) / (S, 3) boundary
Success! We’ve finally answered the original question of what
      was on the far side of the first infinite wall we found.
It’s almost a disappointment that it just looks like more of
      the same kind of Spectre tiling, isn’t it? There’s no obvious
      symmetry here; no noticeable change of quality between the two
      sides of the boundary. The boundary
itself
is the most
      interesting thing, with its self-similarly crinkly shape – but
      if I hadn’t drawn it in a thick line, you’d never have been able
      to pick it out, or even detect that this wasn’t a
perfectly
      ordinary
patch of Spectre tiling. There’s nothing special
      to be seen at all.
(And that’s not so surprising, given that any
finite
patch of this tiling, even one crossing the boundary, must
      exactly match a finite patch that occurs infinitely often
      in
every
infinite Spectre tiling of the plane. That
      must be true, because that’s how we
constructed
the
      transducer that computes transitions across the wall.)
So here’s a different example, which I didn’t discover until I
      was actually writing up this article. Let’s go back to the Y hex
      expansion and look at it again:
Hexagon-to-hexagon substitution rule for the Y hex type
Previously, I pointed out that edge #4 of the “Y (7)” subtile
      is part of edge #4 of the larger Y supertile. But there’s a
      second example of this phenomenon in the same diagram. Edge #5
      of the “Y (4)” subtile is part of edge #5 of the supertile. So
      if we make a set of coordinates that say that each Y is child #4
      of another Y, instead of child #7, then we should find another
      tiling with an infinite wall, different from the previous one.
And we do. But this one is more interesting, because if you ask
      the transducer to compute the coordinates of the neighbouring
      hex, you find … that the output is
exactly the same as the
      input!
The result of crossing edge #5 of a Y whose
      coordinates repeat (Y, 4) forever is that you find you’ve come
      back in to edge #5 of
another
Y hex, whose
      coordinates
also
repeat (Y, 4) forever.
So we’ve got two tiles in the plane with the same combinatorial
      coordinates: the same sequence of supertile types, and the same
      position within each of those supertiles. What are the
      consequences of that?
One consequence is that you have to avoid an embarrassing bug
      in your software. If you’re generating pictures of tilings and
      your code uses a data structure that maps the combinatorial
      coordinates of a tile to its position in the plane (perhaps so
      you can recognise a tile you’ve seen before by finding its
      coordinates in this map), then you’ll find it fails in this
      case, because two different tile positions need to occupy the
      same slot in your data structure. So instead you have to write
      the code the other way round, using positions in the plane as
      your keys, and combinatorial coordinates as values. Then it’s no
      problem to have multiple tiles with the same coordinate
      sequence.
(In fact, the same issue arises in the symmetric Penrose
      tilings I showed earlier. Each of those divides the plane into
      ten sectors with infinitely high walls between them, but there
      are only two
types
of sector, alternating around the
      origin. So for every tile, there are four others elsewhere in
      the plane with the same coordinate sequence.)
But another consequence is that the two sides of this wall must
      be
exactly the same shape
, because the coordinate
      string of our starting tile determines the entire shape of the
      boundary it’s on. So we expect that this boundary should have
      order-2 (180°) rotational symmetry, and not only that, so does
      the entire tiling that it bisects.
And it does! So, from first principles, we’ve constructed a
      Spectre tiling of the plane with order-2 rotational symmetry:
Spectre tiling with a symmetric infinite boundary where (Y, 4) meets itself
If I hadn’t happened to spot that from just this expansion
      diagram, here’s another way I could have found it. In
      the
previous Spectre
      article
I showed a randomly generated patch of tiling using
      the hexagons themselves, rather than the underlying Spectres.
      Here’s another one, without the distracting jigsaw edges I used
      in the previous article:
Tiling of Spectre metatile hexagons, with symmetric clusters marked
Looking at that patch, you can see cases where two Y hexes are
      adjacent to each other, with the orientation arrows on them
      pointing in directions 180° apart. I’ve marked one of them with
      a red circle.
So I could have started by spotting that in the diagram, and
      asking myself: “What if we take two Y hexes connected in that
      way, expand them repeatedly, and overlay the expansions with
      their points of symmetry aligned?” And you’d see that the two Y
      hexes connected to each other along edge #5, so you’d look at
      the Y expansion map to see what happened when you put edge #5 of
      the whole map next to another copy of itself, and that would
      tell you what sub-tile was at the centre of the edge. From there
      you could figure out how to do the expansion.
The infinitary transition algorithm for eventually periodic
      coordinates shortcuts the work of doing the actual expansion.
      With this algorithm ready to hand, we only need to make a
      starting coordinate string describing one of those hexes, and
      then the software does the rest automatically.
So let’s try another feature that I’ve marked with a circle on
      that same diagram: we can see
three
F hexes adjacent,
      with their arrows in 120° rotational symmetry: each F hex’s edge
      #4 connects to the next one’s edge #3. Looking at the F
      expansion map, that looks as if you’d need the F hex to be child
      #6 of another F. So we can immediately generate a Spectre tiling
      with
three
-way symmetry, by making a coordinate string
      repeating (F, 6) forever.
Similarly, there are triangles of three Y hexes with the arrows
      all pointing outwards, i.e. with each Y’s edge #2 connecting to
      the next one’s edge #1, which suggests that a different
      three-way symmetric Spectre tiling is obtained by repeating
      (Y, 1).
And here they are: two different
      three-way symmetric Spectre tilings.
Three-way symmetric Spectre tilings from two different supertiles
The hats tiling
We’ve successfully built transducers for the Penrose tilings
      (both P2 and P3), and for the Spectre tiling. But we haven’t
      tackled the hat tiling yet. Obviously, that’s the next thing to
      do!
A non-overlapping substitution system
      for hats
But we
can’t
do this using the standard substitution
      system for the hats tiling, as described in the original paper,
      and as I used in
      my
previous
      article
for randomly generating patches of hat tiling. Why
      not? Because, in that system, the expansions of adjacent
      metatiles overlap each other, so that the same hat can have many
      different possible coordinates, all valid at once.
In the previous article, I found that overlap quite useful. It
      allows a kind of ‘atlas’ of the tiling: for any direction you
      might try to step off a hat, you can find
some
metatile
      expansion in which that step doesn’t take you off the edge of
      the expansion, and if that’s not the metatile expansion your
      current coordinates describe, there’s a simple way to translate
      coordinates between all the patches that overlap at any given
      point. So you can convert one coordinate string into an
      equivalent one when necessary. That way I completely avoided
      having to work out how all the complicated crinkly edges of the
      metatile expansions matched up to each other.
But here, our test of a successful transducer construction is
      that it should deliver a
unique
output for any input –
      so if there fundamentally
isn’t
a unique coordinate for
      the neighbour of any input hat, then that test would report
      failure, even if the construction had really succeeded.
So the first thing we need is a different substitution system
      for the hat tiling, in which the tile expansions don’t overlap,
      so that every hat has a unique coordinate string.
The original hat paper mentions the existence of one. In the
      diagrams of the metatiles’ expansions, some of the sub-metatiles
      are shown with dotted lines, meaning that if those are omitted,
      then the overlaps go away. But it’s not described in full: the
      details of how the edges fit together are left to the reader to
      work out. That was exactly the part I didn’t feel like doing
      when I first looked at the paper, which is why I used the
      overlapping system instead and found a way to deal with the
      overlaps…
… but happily, since then, someone
else
has figured it
      out and written down all the details, so I still didn’t have to
      work it out myself! The
      paper
“Dynamics and
      topology of the Hat family of tilings”
contains just the
      missing details I wanted: in their Figure 4 they’ve divided the
      boundary of each metatile into edges of five different types,
      and their Figure 5 shows exactly how each of those edge types
      expands to multiple edges when the metatiles are expanded. (And
      the caption for Figure 5 suggests that the authors of that paper
      agreed with me that it wasn’t trivial!)
Given those details, we can
      calculate all the edge mappings in a way that’s very similar to
      the Spectre system. These diagrams assign an index to each part
      of every metatile’s boundary (often regarding a single straight
      edge of the polygon as divided into more than one segment). The
      expansion diagrams number all the internal edges of the tiles,
      so that you can see which pairs of edge segments of neighbouring
      tiles meet; and each edge segment on the perimeter is assigned a
      two-part number indicating which edge of the higher-order tile
      it counts as part of, and which smaller segment of that edge’s
      expansion it is. These diagrams contain enough information to
      make a set of lookup tables that would let you run the recursive
      algorithm for the hats tiling using this non-overlapping form of
      the substition system.
Non-overlapping hat metatile substitution rules
The substitution rules for turning each metatile into hats are
      the same as before, except that now we also have labels on all the
      edges showing how they match up to the next metatile:
Non-overlapping metatile-to-hat substitution rules
Looking at those diagrams, we can see a few of those awkward
      zero-thickness spurs again, like the one we saw above in the
      Spectre system. They appear when two adjacent edges of a
      higher-order metatile expand to paths of lower-order edges in
      such a way that one path starts by retracing the last step of
      the other one. This happened only once in the Spectre tiling,
      but it happens multiple times here: once in the expansion of the
      P metatile into hats, twice in the expansion of T to hats, and
      three times in the expansion of H to other metatiles.
This is the point where it’s a good thing I automated the
      spur-handling technique I
described earlier
.
      With that technique done automatically rather than manually,
      these spurs are no more trouble than in the Spectre tiling, even
      though they occur at an infinite number of levels of the system
      (every time metatiles are expanded from more metatiles) instead
      of only a single level (hexagons to Spectres). With the same
      spur-handling code I described above, the adjacency matcher
      passes the
exhaustive
      completeness test
: it knows of at least one legal neighbour
      string for every valid input string.
Great! Now we try to build a deterministic transducer from
      that.
Ambiguity
When I described the
technique
for converting an adjacency recogniser into a deterministic
      transducer, I mentioned that the algorithm wasn’t guaranteed to
      terminate. If it turns out that there’s no limit to how far the
      algorithm might need to look ahead in order to decide the next
      output, then the attempt to construct a finite-state transducer
      will fail, because the number of states just isn’t finite: the
      algorithm just keeps making more and more states containing
      longer and longer strings of pending output with different first
      symbols, and doesn’t reliably reach a point where it can decide
      that one of them is wrong and start emitting the other one.
For the Penrose tilings and the Spectre tiling, this possible
      failure didn’t happen. But for the hats tiling, it does!
      There
are
cases where the coordinate transition
      algorithm needs to look ahead by an unbounded distance to
      determine the next output coordinate.
When I saw this result, I wasn’t sure that I was looking at a
      real phenomenon and not a bug. So my next job was to find ways
      to cross-check it.
First, I had to find out what input string can trigger this
      problem, and what the two different possible outputs might be.
      To find that out, I ran the transducer construction with
      diagnostic printouts, so that it would display the full details
      of each state it discovered and what transition reached it.
      Then, when it reached a state with lots of buffered output, I
      could see what input would lead to that state, and what possible
      outputs it was considering.
The diagnostics showed that the problem input (or at least one
      of them) was a coordinate string starting like this:
(hat, 11), (F, 0), (F, 5), (F, 5), (F, 5), (F, 5), (F, 5), (F, 5),
…
That is, we’re trying to cross edge #11 of a hat, which is hat
      #0 expanded from an F metatile, which is child #5 of a bigger F,
      which is child #5 of a still bigger F, and so on, with each
      subsequent F being child #5 of a bigger one.
Cross-referencing those numbers to the expansion diagrams above
      which list all the child and edge indices, we find that edge #11
      of hat #0 of an F metatile is part of the expansion of edge #0
      of the F itself. In the next level of diagrams, we look at edge
      #0 of an F which is child #5 of a larger F: that’s part of edge
      #1 of the larger F. And in the next level, edge #1 of an F which
      is child #5 of another F is
still
part of edge #1 of
      the larger F.
So we’ve reached another situation like the one in the Spectre
      diagram I showed right at the start, in which you’re trying to
      cross edge #1 of an F, and you recurse one level up and find
      that now you’re trying to cross edge #1 of the next larger F, so
      you’re back in the same case again. In other words, this
      coordinate string surely identifies a point on an infinite
      supertile boundary: if we tried to process it with the recursive
      algorithm, it would recurse forever. And that’s just the kind of
      place where we might expect a problem in constructing a
      transducer – so that’s a good sign, because this seems to be
      making sense so far!
So, if the input identifies an infinite supertile boundary, and
      the machine doesn’t seem to be able to decide what to output …
      maybe that indicates that we’ve found an infinite boundary
      with
two
things that could fit to the far side?
My diagnostics also showed me the two output strings that the
      machine couldn’t decide between. They were:
(hat, 4), (H, 0), (H, 7), (H, 7), (H, 7), (H, 7), (H, 7), (H, 7),
…
(hat, 0), (H, 2), (H, 8), (H, 8), (H, 8), (H, 8), (H, 8), (H, 8),
…
in which not only does every higher-order metatile coordinate
      disagree, but we aren’t even sure of
which edge
of the
      neighbouring hat we’re going to find. The two possible outputs
      describe hats that aren’t in the same orientation, with edge #11
      of the input hat meeting edge #4 or #0 respectively of the
      output one.
Of course, the diagnostics didn’t show these strings continuing
      in the same fashion all the way to infinity, because I had to
      interrupt the program after it had only buffered a finite amount
      of output. So I only had evidence that a large
finite
number of (F, 5) pairs in the input appeared to be able to match
      output in either of these two forms, with a similar number of
      (H, 7) or (H, 8) pairs.
But when I printed out the state machine for the adjacency
      recogniser itself and followed the transitions it would make on
      each of those (input, output) pairs, I found that it did
      recognise both of them as legitimate, and for each one, ended up
      in a state where a further pair of coordinates from that input
      would cause it to remain in the same state. So it really does
      look as if the
infinite
string that extends the above
      input can go with
either
of the infinite strings
      extending those two possible outputs.
We can also check this using the recursive algorithm, which is
      older and simpler technology, and doesn’t have any difficulty
      with spurs, so it doesn’t depend on any of the horribly
      complicated code I wrote to try to work around them. Just as I
      did for Penrose tilings during
my earlier
      investigation
, we can give the recursive algorithm a
      finitely long string of (F, 5) pairs as input, and let it
      produce some possible outputs by extending that string with
      random extra coordinates.
So I did that, and the results confirmed my previous
      observations:
Input string
Output string
(hat,11), (F,0), (F,5),
…
, (F,5), (P,4), (H,5)
(hat,0), (H,2), (H,8),
…
, (H,8), (H,6), (H,8)
(hat,11), (F,0), (F,5),
…
, (F,5), (F,5), (F,4), (P,0), (F,2)
(hat,0), (H,2), (H,8),
…
, (H,8), (H,8), (F,3), (H,0), (F,3)
(hat,11), (F,0), (F,5),
…
, (F,5), (P,0), (F,2), (H,4), (H,8)
(hat,0), (H,2), (H,8),
…
, (H,8), (F,1), (P,4), (F,2), (H,4)
(hat,11), (F,0), (F,5),
…
, (F,5), (H,2), (H,6)
(hat,4), (H,0), (H,7),
…
, (H,7), (P,3), (H,5)
(hat,11), (F,0), (F,5),
…
, (F,5), (H,0), (H,8)
(hat,4), (H,0), (H,7),
…
, (H,7), (H,7), (H,6)
(hat,11), (F,0), (F,5),
…
, (F,5), (H,0), (H,6)
(hat,0), (H,2), (H,8),
…
, (H,8), (H,6), (H,7)
(hat,11), (F,0), (F,5),
…
, (F,5), (F,5), (F,4), (F,5), (H,2), (F,1)
(hat,0), (H,2), (H,8),
…
, (H,8), (H,8), (F,3), (F,4), (P,4), (F,2)
(hat,11), (F,0), (F,5),
…
, (F,5), (F,4), (P,4), (H,5)
(hat,0), (H,2), (H,8),
…
, (H,8), (F,3), (H,2), (H,6)
(hat,11), (F,0), (F,5),
…
, (F,5), (H,4), (H,6)
(hat,4), (H,0), (H,7),
…
, (H,7), (F,3), (H,0)
(hat,11), (F,0), (F,5),
…
, (F,5), (F,0), (P,0), (F,2), (H,0), (H,6)
(hat,0), (H,2), (H,8),
…
, (H,8), (H,6), (F,3), (P,0), (H,5), (H,7)
Example transitions from a finite prefix of the
        ambiguous input string
No matter how long a string of (F, 5) coordinates I put in the
      input, the recursive algorithm was still able to generate output
      strings full of (H, 7)
or
full of (H, 8), depending on
      what random coordinates it made up to put on the end of my input
      string. This is completely different from the results in the
      earlier table, where I did this for Penrose tilings, and found
      that the output always started with the
same
coordinates, no matter what random things were appended to the
      end.
So I believe it. The hat substitution system has a
      fundamentally different character from the Penrose and Spectre
      ones in the following respect: when you encounter an infinitely
      high wall in this system, there
isn’t
always a unique
      answer to the question of what’s on the other side!
A wall with two possible other sides
Of course, the next question is: what do the two possible far
      sides of this wall
look like?
The first question is how to find out the answer! After all,
      the whole point is that I didn’t manage to generate a useful
      transducer this time, which is usually the tool that makes this
      job easy.
You could do it by generating a finite approximation to each
      version, whose coordinates are a finitely long prefix of the
      full infinite string, and just use a long enough prefix that the
      wrong parts round the outside are too far away to appear in the
      picture.
But there’s a nicer way. Even if you don’t manage to build a
      transducer, you can use the adjacency recogniser by itself
      to
try
to find out the neighbour of a specific infinite
      coordinate string
C
. You do this by another
      automaton-manipulation exercise: start from the adjacency
      recogniser, and construct a subset of it by constraining one of
      the two input strings to be
C
. This gives you a much
      smaller DFA that matches
every possible
infinite string
      that could be a neighbour of
C
. Then you can analyse that
      to find out whether the output is unique, by removing dead-end
      states until there are none left, and then just tracing forward
      from the start state to generate output, stopping if you still
      have multiple choices.
This is pretty slow. For
every coordinate transition
you have to build a new state machine! But it works for normal
      coordinate transitions which only cross a finitely high
      boundary. It can even cross infinite boundaries if there’s only
      one choice of what can go on the far side. The only time it
      fails is when crossing an infinite boundary where the far side
      is ambiguous. And even then, it will notice, and report failure,
      instead of recursing forever.
So you can use that technique to draw any tiling involving an
      ambiguous boundary, by providing it with a starting tile
      from
each
side of the boundary. Then it wouldn’t matter
      if the algorithm wasn’t able to cross the border, because every
      hat in the plane would be reachable from
one
of the
      starting hats.
In fact I didn’t even have to do that, because of another
      curiosity. The (F, 5) coordinate string I started with has two
      possible neighbours, containing infinitely many (H, 7) or
      (H, 8). But it turns out that each of
those
strings
      only has
one
possible neighbour – it can
only
go with the (F, 5) string!
So I was able to generate both of the diagrams below from
      just
one
starting hat – the one on the variable side of
      the boundary. This NFA-pruning transition algorithm can cross
      the boundary in
one
direction, to get to the invariant
      (F, 5) side. It just can’t cross back again to the side it
      started from – but that’s all right, because it doesn’t need
      to.
Anyway, here are the actual pictures. When
      I saw them, they took me completely by surprise.
Most
of the two alternative far sides match exactly! There’s just one
      path of hats that differ between the two, and that path meanders
      through the image on a self-similar course – rather like the
      boundary itself, but touching it only once and then wandering
      off in a different direction. Here I show the boundary in the
      usual thick black line, and I’ve also shaded the hats that
      aren’t the same between the two versions:
The two possible infinite hat supertiles that can go with (F, 5)
I wasn’t 100% sure what I’d expected to see, but it wasn’t
      that! I’d definitely imagined that, somehow,
everything
on one side of the wall would manage to be completely different
      between the (H, 7) and (H, 8) layouts, and only the (F, 5)
      layout on the other side would be constant. But in fact the path
      on which the two versions differ seems to have nothing much to
      do with the boundary. In fact, just as in the other tiling
      types, you wouldn’t be able to spot where the infinitely high
      boundary was, if I hadn’t marked it with a thick line. It isn’t
      the interesting part of
this
picture!
However, now that we’ve seen what this looks like, it’s
      possible to derive it again from first principles. Let’s go back
      to the original, overlapping, form of the hat metatile system,
      and look at the expansion of the H metatile:
Overlapping substitution rule for the H metatile
The expansion diagram is very close to symmetric under a 120°
      rotation. All the tile types remain the same, and only the
      directions of the orientation arrows change. And not even all
      of
those
: if you rotate 120° anticlockwise, then the
      new topmost H tile is still oriented with its arrow downwards,
      and the P in the upper left is still oriented with its arrow
      inwards, because the H and P pair in the bottom right rotate
      into those same orientations when you move them up to the top.
The same H substitution rule, rotated 120° anticlockwise
So, let’s imagine that we made two tilings of the whole plane
      by starting with an H metatile in each of those two
      orientations, and repeatedly expanding it, at every stage
      identifying the previous patch of tiling with the expansion of
      the H in its bottom left (since in both cases that H has the
      same orientation as the larger starting one). A lot of the
      first-order expansion would be the same as before, and that
      similarity would be repeated on larger and larger scales,
      leading to very large sections of the whole plane matching
      perfectly.
Another thing we can see from this analysis is that we expect
      every part of the tiling to be covered by the same
type
of metatile in both variants. The only thing that should differ
      is the
orientation
of metatiles. And not even all the
      metatiles: the F metatiles don’t change position
at all
between these rotated expansions – and a good job too, because
      they’re completely asymmetric.
And, indeed, that matches what we see in the tilings above. The
      path of varying tiles is composed of hats expanded only from H,
      T and P metatiles; all the blue hats (from F metatiles) are
      invariant. Each pair of green hats (from a P) reverses into a P
      pointing the other way; yellow hats from a T rotate by 120°;
      groups of four red hats from an H rotate by 120°, which only
      alters three of the actual hats, because – just like the
      metatiles – one of the hats rotates into exactly the position
      that another has rotated out of.
Someone who was paying proper attention to the expansion
      diagrams could probably have spotted this possibility from first
      principles in March 2023, without needing any help. (Indeed,
      probably someone else
has
found this pair of tilings by
      now, although I haven’t heard of it.) But I didn’t. I had to
      discover it the hard way, by trying to make a transducer, having
      it fail, looking up the coordinates that went wrong, and trying
      to relate those back to the original diagrams!
An alternative substitution system
It’s very interesting that we’ve found this pair of extremely
      similar instances of the hat tiling. It’s pretty cool that we
      were led to it by regular language theory (even if, with
      hindsight, there were easier ways). But practically speaking,
      it’s an inconvenience! As I said
      in
a previous section
, now that
      I’ve developed this transducer technique, I think it’s a really
      nice way to handle tiling generation –
even better
than
      the recursive algorithm I’ve been enthusing about in the
      previous two articles. So my first emotion, when I found I
      couldn’t make one for the hat tiling,
      was
disappointment
rather than fascination. I wanted to
      be able to recommend this state-machine technique for general
      use across all of these tiling types!
But it’s too early to give up hope. There’s an important
      question we haven’t answered: is the ambiguity in the hat tiling
      a property of the tiling itself, or just a property of the
      particular substitution system I’m using? In other words: is
      there a
different
substitution system for the hat
      tiling that avoids the ambiguity?
I spent a while trying to find modifications of the HTPF tiling
      system that encoded just enough extra information to
      disambiguate that ambiguous case. I wasn’t successful.
But in May 2024, somebody else was! Bowen Ping and Brad Klee
      have derived a completely different substitution system for the
      hat tiling, which looks a lot more like the Spectre one than the
      original HTPF system. The metatiles are all hexagonal; each one
      expands to just one hat, except for a single metatile that
      expands to two hats, one of which is the rare reflected one. And
      it turns out – although as far as I know this wasn’t anything to
      do with the problem the authors were trying to solve –
      that
this
system for generating hat tilings avoids the
      ambiguity, and allows the successful generation of a
      transducer!
I’ll show the 10-hex expansion rules in full. First, here are
      the rules for expanding each hex to more hexes. Every input hex
      delivers 7 output hexes in the same pattern, except for the M
      hex, which has one missing:
Hex-to-hex substitution rules for the 10-hex hat system
(The letters I’ve used for these hex types are my own choices.
      I’ve avoided I for the usual reason that it can be confused with
      a digit, and avoided F and H because those are metatile names in
      the
other
hat system.)
And here are the rules for expanding each hex into an output
      hat – again, except for the M hex, which expands to two hats,
      with the one on top being the reflected ‘antihat’. They all look
      very similar, but the important point isn’t the single hat in
      each case (except M): it’s the specification of which edges of
      the hat correspond to which edges of the hexagon.
Hex-to-hats substitution rules for the 10-hex hat system
Again, there are some zero-width spurs. Quite a lot of them, in
      fact: seven of the hex types have a spur in their expansion to
      hexes, and the D hex has a spur in its expansion to hats as
      well. But the same technique I described
for the
      Spectre tiling
is enough to deal with them, and construct an
      adjacency matcher that passes
      the
completeness test
: it
      knows at
least
one legal output for any input. And when
      I tried to convert it to a deterministic transducer, that was
      successful too: this system has
exactly one
legal
      output for any input. Success!
For Penrose tiles and Spectre tiles, the first thing I did at
      this point was to figure out input coordinate strings that would
      generate patterns with rotational or reflective symmetry,
      because they’re pretty. But in this case, that wasn’t
      the
first
thing on my mind. The first thing was: how
      does this substitution system deal with the ambiguous pair of
      hat tilings in the previous section?
By eyeball comparison, I managed to work out a few things about
      how the HTPF system matches up to this one. The result was
      enough to find a pair of infinite coordinate strings
      that
both
correspond to the (F, 5) infinite supertile.
      One is to take the A hex type and make it child #2 of another A
      hex forever; the other is to do exactly the same thing with the
      E hex type. These two supertiles correspond to versions of
      (F, 5) that go with the (H, 7) and (H, 8) variants
      respectively.
Here are the two resulting images. As before, I’ve shaded the
      path of hats that are different in shape and layout between the
      two tilings:
The two infinite hat supertiles that go with (F, 5), rendered via the 10-hex system
There’s lots of interesting stuff here!
My first question was: how has this substitution system avoided
      the ambiguity?
In the infinite supertile at the bottom of the picture,
      corresponding to the invariant (F, 5) section, there’s just one
      visible difference: the topmost hat on the left is a different
      colour, indicating that it’s expanded from a different
      first-order hexagon type. (Its higher-order hexagon types are
      all different too, of course; it’s just that I only used the
      lowest-order one to decide the hat colour.)
In fact, looking more closely, quite a lot of
      hats
near
the varying path change colour. It’s as if
      the path of changing actual hats has a sort of ‘aura’ around it,
      composed of hats that change
colour
but not shape. And
      that aura extends just far enough to cross the infinite boundary
      – so you can disambiguate which version of the path you want to
      see, by specifying what colour that one corner hat should be,
      because it will be different in the two cases.
But also: look what the infinite boundaries are doing!
In the HTPF version of this picture, there was
      just
one
infinite supertile boundary, separating the
      invariant (F, 5) supertile from the two alternative ones (H, 7)
      and (H, 8) that fitted to it. But in this system, each of those
      two alternatives is itself divided into two infinite supertiles,
      so that the diagram as a whole contains three. Not only that,
      but the boundary between them isn’t in the same place in both
      versions. In fact the
connectivity
between the regions
      isn’t the same either: in the (E, 2) picture one region
      separates the other two, but in the (A, 2) picture there’s a
      point where all three regions connect. Even
more
interestingly, it looks as if
half
of that extra
      boundary is the same, and only the part on the left changes!
I have no idea what the mathematical significance of any of
      that is (if any), but it’s fascinating, and
again
not
      what I’d have expected!
You might wonder what the other supertiles
are
, in
      these two diagrams. In the (A, 2) diagram – corresponding to
      (H, 7) in the HTPF version – the other two supertiles are (D, 0)
      on the left, and (K, 2) in the upper right. In the (E, 2)
      diagram, corresponding to (H, 8), they’re (M, 0) in the middle
      and (D, 2) at the top. (My notation for an infinite supertile
      with eventually periodic coordinates is to simply list the
      eventually-repeating section. If it has length >1 – which
      we’ve seen in the Penrose examples, and there will be a couple
      more below – then it makes sense to list it starting at a
      multiple of its own length, to distinguish supertiles whose
      repeating sections are rotations of each other.)
Finally, I’ll show some symmetric instances of the hat tiling,
      just as I’ve done for the other two tilings earlier. Looking at
      the HTPF system, it’s always seemed clear to me that there are
      two instances of the hat tiling with order-3 rotational
      symmetry: if you start by putting three F metatiles with their
      points together, and expand that figure once, you find the
      expansion still has three F around the centre point but this
      time with their
other
120° corners meeting. Expanding
      again, the Fs turn round again and you’re back to having the
      points together. So you expect two symmetric hat tilings, by
      choosing which of those orientations to take as the lowest order
      of metatiles and expand to hats.
In the 10-hex system, the corresponding coordinates also
      involve a two-way alternation. You need a G hex, which is child
      #6 of an E, which is child #2 of a G, and so on. By taking the
      lowest-order hex to be one or the other of those, we can
      generate the pair of symmetric tilings using our nice efficient
      10-hat transducer.
There’s one more symmetric hat tiling, which occurs when two F
      metatiles meet back to back. Expanding that figure repeatedly
      about its centre gives a tiling with 2-way rotational symmetry.
      In the 10-hex system, it corresponds to a G hex being child #4
      of another hex forever.
So here are the three symmetric instances of the hat tiling:
Three hat tilings with rotational symmetry
What does all of this mean, in mathematical terms?
In this article so far, I’ve talked a lot about the mechanism
      of constructing and using these transducers, but not a lot about
      what it
means
that we can build one, or can’t.
To begin with: do we even have any guarantee that a tiling
      constructed by using a transducer to cross an infinite supertile
      boundary is
consistent?
It looks plausible in the
      examples so far, but can we be sure that if you walk a certain
      number of steps along the boundary from your starting tile,
      and
then
cross it using an infinitary step, then you
      get the same coordinate string that you’d have got if you
      crossed at the original location and then walked along the far
      side of the boundary to the same place?
Also, in tilings where you can construct a transducer, does
      that
really
prove that there’s only one possible way to
      extend a tiling of the plane to the other side of an infinite
      supertile boundary? Or might the transducer be restricting
      itself to a subset of the possibilities, so that there might be
      a completely different answer that the transducer could never
      generate?
The second of those questions is the easier one to start
      answering, because we’ve already seen an example! Consider the
      case of the two very similar instances of the hat tiling. Even
      in the 10-hex substitution system, there’s an infinite supertile
      – the one shown at the bottom of the image – in which all the
      hats are exactly the same in both versions. The only thing that
      differs is the sequence of types of hexagonal supertile.
But that doesn’t stop the
actual hats
from fitting
      together on the two sides of the boundary!
Suppose you’d never heard of the HTPF substitution system, and
      you
only
knew of the 10-hex system for the hat tiling.
      Suppose you’d written a hat tiling generator, using the
      recursive algorithm, with coordinates based on the 10-hex
      system. Suppose it crashed the first time you tested it, for the
      same reason my Spectre one did – you hadn’t connected up the
      random numbers yet, and you’d accidentally fed in a fixed
      sequence of coordinates that defined an infinite supertile
      boundary. And suppose, by really bad luck, your fixed coordinate
      sequence described
that
infinite supertile boundary,
      from our HTPF ambiguous pair.
You might wonder the same thing as I did: whether the far side
      of the boundary existed, and whether it was unique. You might do
      exactly what I did – figure out how to build a transducer. And
      since you’re using the 10-hex hat system, you’d find the
      transducer was successfully constructed (as I did, in the
      Spectre case). You’d use it to generate what you thought was the
      unique far side of your boundary. And then somebody would come
      along and exhibit a different pattern of hats that also fits to
      the far side of your original boundary, and you’d be completely
      startled. Perhaps you’d even be angry. The transducer has
      somehow let you down – it promised uniqueness, and didn’t
      deliver!
What’s the loophole? The answer is that the transducer promises
      a unique
sequence of coordinates
that’s the neighbour
      of a given input
sequence
. But maybe what we really
      wanted to know is whether there’s a unique
layout of
      tiles
that’s the neighbour of some
      existing
layout
. And in this case, there
      are
two
sequences of coordinates that give rise to
      exactly the same layout of hats on the near side of the
      boundary. The transducer gives you a unique neighbour for your
      sequence, and for the other sequence, but really, each one also
      fits to the other.
But wait – how do I know that’s not true for Spectres? For all
      I know, the example I originally found could be in exactly this
      situation, and I might just not have found the other sequence
      yet!
So the existence of a finite-state transducer doesn’t guarantee
      everything we’d like it to. What
does
it guarantee?
      What
can
we say about tilings for which a transducer
      exists?
We derived our transducer from a state machine that recognises
      the language of pairs of
finite
coordinate strings that
      the original recursive algorithm can transform into each other:
      that is, the relative coordinates of two neighbouring sub-tiles
      within the (iterated) expansion of some individual high-order
      (but finite-order) supertile. So any pair of strings that appear
      as the input and output of the transducer must have the property
      that each
finite prefix
of the pair of strings must
      also be a prefix of some valid finitely long coordinate
      transition. Otherwise the adjacency recogniser would have
      rejected the pair before that prefix was complete, and the
      transducer wouldn’t have generated it as output.
There’s probably a better name, but I think of this property as
      “local plausibility”: the pair of neighbouring tiles is
      surrounded by larger and larger neighbourhoods in which the
      context –
including
the supertile types – looks like
      things you’d also see in ordinary finite situations.
The good news is that I think this “local plausibility”
      property
does
mean that the resulting tiling is
      consistent. If you walk any finite number of steps along one
      side of the boundary, then there’s some finite supertile that
      contains all the steps you’ve taken. And the counterpart of that
      finite supertile on the far side of the boundary must fit to it,
      because of local plausibility: there’s some ordinary finite
      situation in which the same two supertiles are adjacent in the
      same way. So if you walk in a loop across the boundary and back,
      you should never find an inconsistency.
What about uniqueness? The transducer can only tell us that
      there’s a unique
locally plausible
extension of the
      half-tiling we started with, because locally plausible tilings
      are all it knows about. So it can’t tell us what other
      possibilities might exist that
aren’t
locally
      plausible.
And that’s what went wrong in this case of the ambiguous hat
      tiling. There are two ways to extend the original infinite
      supertile to a full hat tiling of the plane; but in the 10-hex
      system, you have to make a choice about which coordinate string
      you use to represent the supertile, and whichever one you pick,
      only one of the extensions is locally plausible.
So there’s a unique
locally plausible
extension, but
      that doesn’t mean there’s a unique extension of
any
kind.
So,
does
a case like this also exist in the Spectre
      tiling? I have no idea! I’d be interested in ways to find out.
Other possible applications for state machines
I came up with this transducer idea as a means of investigating
      those infinitely high walls. I think it’s also a good system for
      generating finite patches of tiling – I recommend it over the
      previous recursive algorithm.
But I don’t think that’s the only thing a transducer – or even
      the simpler adjacency recogniser – can possibly be useful for.
      Here are some other thoughts.
Generating coordinates from a tiling patch
My main use of transducers is to generate a patch of tiling,
      starting from a string of coordinates. I think it should also be
      possible to use them to go in the other direction.
Suppose somebody shows me a patch of Penrose or Spectre or hat
      tiling, without any coordinate labels attached. I’d like to be
      able to find a string of coordinates in my preferred
      substitution system which give rise to precisely that patch,
      containing the same tiles connected in the same ways. (For
      example, that would let me recreate the same patch in my own
      software, and also find legal ways to extend it.) But I wasn’t
      given any coordinates at all: all I have is a complicated
      drawing that shows the lowest-level tiles, and how they connect
      to each other.
If I have a transducer for my substitution system, I think I
      could use it to answer this question, in the following way.
I maintain a DFA that matches a regular language of coordinate
      strings. I choose a starting tile of the tiling patch, and
      initialise my DFA to the one that matches any legal coordinate
      string for the type of that starting tile.
Now I walk around the tiling patch I’m given, stepping from one
      tile to the next, until I’ve visited every tile. Every time I
      step from a tile
t
to another tile
u
, I combine my
      DFA of possible coordinate strings for
t
with my
      transducer, to produce a DFA of possible coordinates
      for
u
, under the constraint that the first symbol of the
      output (giving the lowest-level tile type, and saying which edge
      of it corresponds to the edge of
t
I just stepped off)
      must match what’s in the input tiling patch. This should be a
      simple exercise in DFA manipulation.
So, as I walk around the patch, my DFA is updated in two ways.
      Firstly, it updates with my current position. But it also
      becomes more and more refined, because it has to match only the
      coordinates that could have given rise to
every
tile
      I’ve visited so far.
So when I’ve covered the whole patch, I don’t just
      have
one
possible coordinate for the tile I end up at.
      I have a DFA that recognises the language of
all
the
      possible coordinates! And it’s easy to pick an arbitrary one to
      return.
(It would be nice if we could combine this coordinate-finder
      idea with coordinate generation, to produce a system that can
      translate a string of coordinates between two substitution
      systems for the same tiling. I’m pretty sure you could do
      that
slowly
for a finite patch, by generating the whole
      patch of interest in one system and walking around all of it
      with the coordinate finder I describe above. But whether you can
      do it
fast
, or for infinite coordinate sequences, is
      another matter. The translations I’ve done in this article,
      between the HTPF and 10-hex systems for hats, were done by hand,
      based on the coordinates in question being particularly
      simple.)
Choosing coordinates with interesting
      properties
Another use of a finite state machine that understands your
      coordinate system is that you can explore it to find interesting
      corners.
I’ve shown several examples of the Spectre and hat tilings with
      rotational symmetry. These all have the property that, at the
      centre of symmetry, two or three tiles meet which
      have
identical
combinatorial coordinates – two copies
      of the same infinite supertile share a boundary, and their apex
      tiles share an edge.
If I hadn’t already known or guessed that some symmetric
      instances of these tilings existed, I could have found them in
      an automated way, by searching the adjacency recogniser state
      machine. Like several previous examples in this article, you do
      this by constraining its input – but instead of
      constraining
one side
of the input to a fixed string
      and seeing what comes out as the other, you constrain the two
      sides of the input to be the same as
each other
(apart
      from the edge indices at the start). This search will deliver a
      DFA that matches the full set of coordinate strings of tiles
      that can possibly meet another copy of themselves.
In fact, one of the tilings in this article was found that way.
      I spotted the three symmetric Spectre tilings by eye, and I’d
      already guessed that the two 3-way symmetric hat tilings must
      exist, but I overlooked the 2-way symmetric hat tiling, until
      this search pointed it out to me.
Another search of this kind lets you find strings of
      coordinates that give rise to infinite supertile boundaries in
      the first place. If I hadn’t started this whole investigation by
      stumbling on one, could I have found it by a systematic
      search?
Yes, I could. If you delete all the
accepting
states
      from an adjacency recogniser, then any infinite walk in the
      remaining directed graph spells out a pair of infinite
      coordinate strings that have an infinitely high wall between
      them, because precisely the criterion for a wall
      being
finitely
high is that the adjacency recogniser
      enters an accepting state. So it would be easy to find any of
      the infinite walls I’ve mentioned already: for the ones in which
      a single coordinate is repeated forever, you just look for any
      vertex with an edge back to itself, and for the ones with longer
      period (like ABAB… or AVBUAVBU… in the P2 tilings) you look for
      a longer circuit.
This analysis also shows that there must exist an uncountable
      number of other infinite supertile boundaries, whose
      coordinates
aren’t
periodic: as soon as you can find
      more than one different circuit from the same vertex back to
      itself, you can construct a coordinate string interleaving those
      circuits in any pattern you like. I’ve only been showing
      boundaries derived from strings with a short period here because
      those tend to be the pretty ones. There are lots of others.
Future possibilities
What’s left to do with all of this?
I’d like to have a try at writing the coordinate-finder
      I
mentioned just now
. I expect
      the DFA manipulation to be reasonably easy, but the hard part
      would be finding a practical way for a user to input an existing
      patch of tiling that they wanted to determine
      coordinates
for
. (You wouldn’t want to type in edge
      indices all the time!)
Another thing I’d like to improve is the techniques for
      handling spurs and other awkwardnesses in tiling descriptions.
      The technique I
described in detail above
was enough to cope with all the spurs in the Spectre 9-hex
      system, the hat HTPF system, and the new hat 10-hex system – but
      it doesn’t cope with
everything
. In particular, here’s
      a substitution system that my software still can’t build a
      working adjacency recogniser for:
Substitution rules for Penrose P2 whole kites and darts
This substitution system generates the same Penrose P2 tiling
      we’ve already got working, but this time I haven’t done my usual
      trick of cutting each kite and dart into two triangles. Instead
      I’ve left them whole, which makes life easier for an end user
      trying to generate the tiling – they wouldn’t have to do the
      postprocessing step of expanding each triangle into its full
      tile and discarding duplicates.
This system works fine if you’re using the basic recursive
      algorithm: it might have to recurse back and forth crossing
      spurs, but it gets there in the end. But I haven’t been able to
      build a working adjacency recogniser for it, and I’ve tried
      fairly hard – I added lots of extra sophistication to my code to
      handle the awkward cases that come up, but never got the result
      to pass my completeness check. There always seemed to be another
      awkward case I hadn’t handled yet.
(Why’s it hard? I’m not sure I even have a complete list of the
      problems. But one example is that, in this system, two tiles
      sharing an edge can be expanded from higher-order tiles that
      only share a vertex, because the darts in the expansions stick
      out by such a long distance from the original tile outlines.)
And
this
system, doing the same for the P3 tiling, is
      perhaps even worse, because in a sense, one of the expansions
      isn’t even connected:
Substitution rules for Penrose P3 whole rhombs
Maybe one day I’ll have another try.
Software
If you’d like to play with all of this stuff yourself, I’ve
      uploaded my software for general substitution-system handling
      into my git repository collection. It’s written
      in
Sage
, an extension of
      Python to be (among other things) a symbolic algebra system.
You can clone my git repository with this command:
git clone https://git.tartarus.org/simon/tilings.git
Or you can browse the repository
on the web
.
I warn you that this isn’t quite up to my usual standards of
      solid production code! This is
research
code: when I
      wrote it I was trying to find out whether things would work at
      all, so I didn’t optimise or refactor or polish very much, for
      fear that I’d waste my time. I’ve written some hasty
      documentation
      in
README.txt
,
      but for more detail, you might have to examine the example
      tiling files yourself, or the code. Or ask me specific
      questions, and I’ll try to extend the documentation to include
      answers to them.
Perhaps the most immediately useful thing you could do with
      that software is to generate the actual working transducers for
      Penrose P2 and P3, Spectre 9-hex, and hat 10-hex. If you want to
      actually use the transducer algorithm to generate tilings,
      calculating those state machines is the hard part of the job,
      and my software will do it for you. The rest of the algorithm is
      just a matter of processing strings using the transducer, making
      up random extra coordinates if you need to, and plotting the
      output in whatever graphics system you want to use.
This software will do all of that too – you can use it to
      directly generate pretty pictures – but it’s quite slow. To make
      a significantly large piece of tiling I’d probably want to write
      the output engine in a faster language!
Acknowledgments and references
I’m indebted to Robin Houston for helpful discussions while I
      was investigating this, and for reading the draft article.
I’m also grateful to Bowen Ping and Brad Klee, firstly for
      inventing their 10-hex substitution system for the hat tiling,
      and secondly for kindly permitting me to publish it here.
      Without that system, this article would have been very
      different, and would have ended in a shamefaced apology that
      this really nice algorithm only worked properly for two of the
      three aperiodic tilings I’ve been discussing.
As I said in the introduction, I’m not claiming to have
      discovered all the mathematical ideas here for the first time. I
      thought of them by myself, but at least some of them had been
      thought of independently before. The first paper I link to below
      describes the concept of ‘addresses’ in a substitution tiling,
      which are equivalent to the thing I’ve been calling
      ‘combinatorial coordinates’; it mentions the possibility of
      infinite-order supertiles that aren’t the whole plane; and it
      describes something very like my adjacency-recogniser state
      machine, specifically mentioning the possible application of
      using it to match up infinite supertiles whose boundaries fit
      together. So I definitely don’t get credit for any of those
      ideas – they predate my investigation here by 25 years.
Some other useful resources:
Aperiodic
          hierarchical tilings
A 1999 paper by Chaim Goodman-Strauss (24 years before
        co-discovering the hat tiling), discussing substitution
        tilings in general and the notion of addressing a tile by its
        place in the hierarchy.
An aperiodic
          monotile
The paper introducing the hat tiling, and showing the
        original (overlapping) substitution system of H,T,P,F
        metatiles.
Dynamics and
          topology of the Hat family of tilings
I haven’t used the main subject of this paper, but in
        passing, it provides full details of the non-overlapping
        version of the H,T,P,F substitution system.
A chiral
          aperiodic monotile
The paper introducing the Spectre tiling, with full details
        of its substitution system.
HatHexagons
and
HatHexagonalTiling
in the Wolfram Function Repository
Bowen Ping and Brad Klee’s own code exhibiting the 10-hex
        substitution system for the hat tiling.
Appendix: Batman turns up where you least expect him
The previous two articles both ended with an irrelevant but
      pretty appendix. Let’s do that again!
In
a previous section
I derived
      the combinatorial coordinate representation of the two
      pentagonally symmetric instances of the P2 tiling. Those aren’t
      new, of course: they’re well known in the Penrose tiling
      literature, usually under the names “infinite sun pattern” (the
      one with a decagon of five kites at the centre) and “infinite
      star pattern” (with a star of five darts).
That wasn’t too hard, because the coordinates system makes it
      easy to work out the representation of a pattern that’s
      completely symmetric. But there’s another quite famous P2 tiling
      instance (for example, Martin Gardner chose it to be the cover
      of a book) which is
very nearly
symmetric, but not
      quite. It’s known as the “cartwheel pattern”:
The cartwheel pattern
From a distance it looks as if this pattern has the symmetries
      of a decagon: 10-way rotational symmetry,
and
reflection. But it’s not
quite
true. The whole pattern
      really does have reflective symmetry about the vertical axis,
      but the rotational symmetry isn’t quite complete. If you rotate
      the whole picture a tenth of a turn at a time, the blue figure
      inside the central decagon – known as ‘Batman’ – will gradually
      turn upside down. And the ten radiating ‘spokes’, highlighted
      here in red, aren’t quite symmetric either: they come in two
      different handednesses, arranged in an irregular pattern around
      the circle. So when you rotate the whole picture,
some
of the spokes rotate into the place of one with
      the opposite handedness.
I thought it would be fun to try to figure out the
      combinatorial coordinates of a tile in this pattern, so that it
      would be easy to draw it at large scale. When I did it, I got a
      surprise.
Since this picture is mostly symmetric, it makes sense to start
      by wondering: what happens if we expand each half-tile triangle
      via the usual expansion rules? We’d surely get another picture
      with the same ‘mostly symmetric’ property, and maybe after some
      number of iterations it would look like the same one again?
The easiest way to try that is to start from the central
      ‘Batman in a decagon’ figure, divide its kites and darts into
      the triangles I use for my coordinate system, and expand it a
      few times to see what happens:
Iterated expansion of the central decagon + Batman figure
Just what we were hoping for! Expanding this decagon once, we
      get a pattern that has a smaller copy of the same decagon figure
      again at its centre – but upside down. Expanding a second time,
      it’s the right way up again. And repeating the expansion twice
      more, we see that this procedure by itself is producing the
      spokes and symmetric sectors on the outside.
Of course, I haven’t
proved
that that will continue.
      But we can at least see that the essential symmetry is likely to
      continue: since expanding the original decagon 4 times produces
      a lot of mostly-symmetric exterior with a decagon at the centre,
      it follows that expanding another 4 times will introduce the
      same chunk of tiles in place of the smaller central decagon, and
      expand the mostly-symmetric exterior we already have into more
      mostly-symmetric stuff. So it’s pretty convincing.
What about actually finding the coordinates? This is another
      exercise of the same type we’ve done several times in this
      article. Choose a triangle in the middle of the largest Batman;
      expand twice to get a smaller Batman the same way up; determine
      the coordinates of the corresponding triangle of the smaller
      Batman inside the larger original triangle; then we’ll have a
      finite string of coordinates that we can repeat forever, to
      obtain the infinite coordinate sequence for that triangle in the
      whole plane. Since the two triangles will share an edge, we also
      expect that there will be an infinite supertile boundary down
      the vertical axis, but that’s fine, our transducer can cope with
      that.
Great! So let’s try it. We’ll choose the type-A triangle in the
      middle of Batman, just to the right of the centre line.
Iterated expansion of Batman, showing coordinates in one triangle
The smaller instance of the same triangle is an A, which is a
      child of a B, which is a child of the larger A we started with.
      Iterating this forever, that must mean the type-A triangle in
      the middle of the Batman figure has the infinite coordinate
      sequence ABABAB…
Wait … that looks
very
familiar, doesn’t it? It’s
      exactly the same coordinate sequence I
      chose
as my arbitrary starting example
earlier, when I was trying to convince myself that it was even
      possible for an infinite supertile boundary to have something on
      the far side at all. It was the first example I found, because
      it’s a particularly simple way to expand a triangle and choose a
      similarly oriented sub-triangle part way along one of its edges
      – you only have to expand by two steps, which is the fewest
      possible.
In the course of doing this investigation and writing this
      article, I’d
already
found the coordinates describing
      the cartwheel pattern, completely by accident – and I’d never
      noticed! If you took that ‘simplest possible’
      reflection-symmetric P2 tiling I showed in the previous section,
      turned it 90° so that the axis was vertical, and coloured it
      correctly, it would
be
the cartwheel pattern.
Batman was hiding behind me all the time!
