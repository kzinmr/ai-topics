---
title: "Writing a solver for Net"
url: "https://www.chiark.greenend.org.uk/~sgtatham/quasiblog/net-solver/"
fetched_at: 2026-04-27T07:57:15.461518+00:00
source: "chiark.greenend.org.uk/~sgtatham"
tags: [blog, raw]
---

# Writing a solver for Net

Source: https://www.chiark.greenend.org.uk/~sgtatham/quasiblog/net-solver/

Writing a solver for Net
[Simon Tatham, 2019-03-27]
I had mail yesterday from a computer science student asking how I went about writing the solver for the game
Net
in my
puzzle collection
.
 I took the question literally, i.e. not just ‘what is the algorithm?’ 
but ‘what was your thought process that allowed you to come up with the 
algorithm?’. I thought that was a good question, and so I wrote a fairly
 complete answer.
Having done that, of course, it seems a shame to
 only send it to a single recipient! So I'll post it here as well, in 
case anyone else is interested.
Generally, if
 I'm trying to write a solver for a puzzle game, my first step is to 
solve an instance of the same puzzle by hand (or more than one if I 
don't get the hang of it immediately), and watch my own thought 
processes. That tells me what kinds of deduction
can
be made, and once I know that, it's usually not too hard to automate them in a program.
Net
 was actually the very first puzzle in my collection, and I got into it 
by playing an existing version in the form of somebody else's Flash web 
game. (This was around 2002.) Initially I played it by unscientific 
trial and error –
just turn things so that they mostly fit 
together, and when you find a problem, try tweaking things and hope it 
makes them better. But after a while I started to notice individual 
deductions such as:
a T-
piece next to the grid edge can only go one way, because none of the three
connected
sides of it can point at the barrier. Similarly, a corner piece in the corner can only go one way, and so can a straight-
edge piece on the grid edge.
That lets you decide
for sure
what the orientation of a piece is, so you can lock it down and treat it as definite.
Then an unconnected edge of a locked piece (say, the other side of that straight-
edge) can be treated like a grid edge in turn (so that a T-
piece next to it can align only one way).
And a definite
connected
edge due to a locked piece gives you further things you can do. For 
example, an endpoint next to that edge now has only one way it can 
connect.
So that gave me the general idea that each piece 
eventually becomes ‘locked’ into a single orientation, and the more 
pieces are locked, the more you can deduce about other pieces using 
those as a starting point.
To model that in a computer, the obvious approach is to store a
set
of possible orientations for each piece. Initially every piece has a 
set consisting of all four possible orientations (except that the 
straight piece has only two, because it's 180-
degree symmetric). So
 you set up that data structure; keep iterating over the grid looking 
for reasons why a given orientation is ruled out; and when you stop 
being able to make any progress, you check to see how many possible 
orientations each piece has left. If any piece has
no
orientations then the puzzle has no solution (or your solver has a bug, 
of course); if any piece has more than one orientation, then either the 
puzzle has multiple solutions, or else one of them is not actually legal
 for a reason your solver hasn't spotted.
That's the basic stage 
of a solver for Net. Then you start trying to make it cleverer by adding
 more deductions, possibly with more stored data as well.
My next insight was that sometimes you can find out useful things without needing to lock a piece down completely:
if one edge of a corner piece is known to be connected, then the opposite side must be unconnected, and vice versa.
That suggested to me that it's also worth storing data for each
edge
of the grid, showing the set of possible states that edge might be in. 
(The two states are ‘connected’ and ‘unconnected’, so the four possible 
sets are ‘connected’, ‘unconnected’, ‘don't know yet’ and ‘help, I 
haven't got any possible state for this edge’.)
Once you have that
 data, it simplifies the deductive system: now you don't have to go 
through all possible cases for a square and its neighbour. Instead, you 
can repeatedly ask two questions:
Does my knowledge about the possible states of this square rule out any states of its bordering edges?
Does my knowledge about the possible states of this
edge
rule out any states of its bordering
squares
?
You
 can answer those questions by checking a single (square, edge) pair and
 just iterating over every possible state of the square. Any state of 
the square that would put that edge in a state you know to be impossible
 can be thrown away; conversely, any state of the
edge
that is not achieved by one of the remaining states of the square can be thrown away too.
And now you don't even have to write the code in a way that has a huge list of detailed special cases about how T-
pieces, corners, straights and endpoints each behave. It's all done in a completely uniform way.
Those
 are the ‘local’ deductions. Of course, Net has another pair of rules: 
you mustn't make a loop, and you must ensure everything is connected 
together.
Loop avoidance is dealt with by a bit of computer science. You may already have heard of the ‘union-
find’ data structure, also known as ‘disjoint-
set
 data structure’ or ‘Tarjan's disjoint set forest’ or other names along 
those lines. It lets you maintain information about a set of objects 
some of which are known to be ‘equivalent’ to one another in some way, 
under the conditions that everything starts out considered to be 
separate, and sometimes you find out a new piece of information that 
means objects X and Y are now known to be equivalent. And it tracks 
transitivity, so if you previously knew A=B and X=Y, and then you tell 
it that B=X, then the query interface will automatically know all of 
A=Y, B=Y and A=X as well.
That structure is tailor-
made for 
tracking connectivity in a graph, if it's ‘incremental’ (that is, edges 
are always added, never subtracted). So the solver's third piece of 
stored data is a disjoint-
set forest whose elements are the squares
 of the grid, in which two elements are considered equivalent if there's
 a path of known connected edges linking those squares to each other. 
Then you get two new deductive rules in the solver:
Whenever you rule out the ‘unconnected’ state for an edge, unify the two squares it separates in the dsf.
Conversely, if you have an unknown edge for which the dsf tells you that the two squares it separates are
already
connected to each other, you must rule out the ‘connected’ state for 
that edge, because connecting that edge would make a second path between
 those two squares, i.e. would form a loop.
That leaves the rule about all the squares being connected together. That was actually the most difficult one.
Going
 back to my original plan of playing the game by hand and watching the 
techniques my own brain came up with, I initially found that the 
connectedness requirement made me think of local deductions such as:
Two endpoints next to each other cannot be connected together. (Otherwise, they couldn't connect to anything
else
).
In particular, if a cluster of four endpoint squares is arranged in a T-
shape, then the one at the centre of the T must connect to the only one of its edges that
doesn't
go to another endpoint.
A
 straight edge between two endpoints cannot be oriented so that it links
 them together, because again, those three squares would form a closed 
subgraph.
A corner piece bordering three endpoints must be connected on the fourth edge, otherwise it would link together two endpoints.
I
could
have coded each of those local deductions separately, but I preferred 
to try harder to find a single underlying rule that they're all special 
cases of.
One important point is that unlike the earlier set of 
local deductions, these all have exceptions. Suppose your entire Net 
grid is 2×1 in size. Then two endpoint squares
can
connect together –
indeed, they
must
! So it's not quite as simple as ‘these configurations are disallowed’: it's more that they're disallowed
unless
the resulting subgraph would be as big as the whole grid.
As
 I continued to play by hand, I found I was forming an intuitive notion 
of a ‘dead end’. A dead end is an oriented edge (that is, a particular
side
of a particular edge of the grid) which has the property that if that 
edge is in the ‘connected’ state, then the set of squares you can reach 
on that side of it can't possibly be the whole grid.
So I'd find myself mentally identifying larger and larger parts of the grid as ‘dead ends’:
Any edge going into an endpoint is a dead end
Any edge going into a straight piece is a dead end if the opposite  edge is a dead end in the outgoing direction
Any edge going into a corner piece is a dead end if
both
the adjacent edges of that corner are outgoing dead ends
Any edge going into a T-
piece is a dead end if
all
the other edges of that T-
piece square are outgoing dead ends
and
 then I'd be able to say to myself, ‘Both sides of this edge are dead 
ends, so if the edge is connected, then they'll link together into
some
kind of closed subgraph that isn't the whole grid.’
But,
 again, there's that exception. It's not actually enough to tag an edge 
as ‘dead end’ or ‘not dead end’: it's not a binary property. It matters
how big
is the set of squares you can reach –
and if it's the whole grid, then perhaps that dead-
end configuration is allowed after all.
After
 thinking this through for a while, I worked out how to make it 
rigorous. The right way to consider it is to store the following item of
 data for each direction of each edge:
If this edge is connected, then what is the
maximum
number of squares that could possibly be reachable from this side of it?
Initially,
 you can set all those values to the size of the whole grid, because 
obviously it won't be possible to reach more squares than
that
. But then you can start doing deductions:
An
 edge going into an endpoint: set the ‘maximum reachable’ value to 1. If
 you connect into that endpoint, there can't possibly be a path going 
onward from there into any other square.
An edge going into a 
straight piece: the ‘maximum reachable’ value can be at most the value 
of the opposite outgoing edge, plus 1 for the straight square itself.
An
 edge going into a corner: you have to consider two ways the corner 
could be oriented. (If it connects on this edge, its other connection 
could be either of the two adjacent edges.) If
both
of those possibilities give you a small maximum value –
or if one of them is ruled out completely –
then you can bound the maximum for this edge.
And
 eventually I worked out that this boils down to a general rule you can 
apply to any kind of square, and all of those are special cases of it:
Given
 an edge E going into a square S, iterate over all orientations of S 
that aren't ruled out yet. For each one, find all the connected edges of
 S
other
than E; then the maximum number of reachable squares 
from edge E with S in that state is given by summing the max values for 
those outgoing edges, and adding 1 for S itself. Then the max for E is 
bounded by the largest one of those values you worked out for any 
orientation of S.
With the dead-
end avoidance code in
that
form, it's nicely rigorous, and takes the special cases in its stride. 
Give it a 2×1 grid and it will happily connect the two endpoints 
together without complaining that they're an illegal dead end; give it 
any larger grid and it will know that you
can't
connect any two endpoints together.
That's
 all the deductions I've implemented so far. There is another one I use 
quite often in play, and I haven't got round to adding it to the solver 
yet:
If you can find a loop of
edges
in the grid 
with only one of them in an unknown state, then you can determine the 
state of that edge by parity. Add up the degree of every square in the 
region enclosed by the loop (1 for an endpoint, 3 for a T-
piece, 2 for straights and corners); then any connection
within
that region reduces the count by 2, but nothing can change whether the 
count is odd or even. So the number of times the solution graph crosses 
your loop must be odd if and only if the sum of degrees inside the 
region is odd, and even otherwise.
The difficult part of implementing that technique is efficiently identifying an edge that you
can
nail down in that way, and the corresponding region in which you have to count up parities. I do know how to do that –
but I'll leave it as an exercise for the reader!
