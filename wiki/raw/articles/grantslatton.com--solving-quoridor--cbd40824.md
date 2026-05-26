---
title: "Solving the board game Quoridor"
url: "https://grantslatton.com/solving-quoridor"
fetched_at: 2026-05-26T07:14:42.950093+00:00
source: "grantslatton.com"
tags: [blog, raw]
---

# Solving the board game Quoridor

Source: https://grantslatton.com/solving-quoridor

Solving Quoridor
This post significantly improves the state of the art in solving the board game Quoridor. I describe novel techniques that enable fully solving almost all board configurations with area ≤ 28 (e.g. 5x5, 8x3, 7x4, etc) for most wall counts on a consumer laptop.
Background
I was introduced to the board game
Quoridor
back in 2014 and was immediately taken by it.
I usually spend a weekend returning to Quoridor once every couple years, writing different forms of AI bots to play it. This last weekend, I made a breakthrough that enables both much stronger bots, and much more complete solving.
Rules
The game is pretty simple:
Pawns start on opposite sides of the 9x9 board
Your goal is to get your pawn to the far side
You have 10 walls
On your turn, you can move your pawn 1 square, or place a wall
You can jump over the opponent's pawn
You can't place a wall that makes it impossible for a pawn to get to its goal
That last rule is where all the performance complexity comes from. You might be planning on blocking your friend's straight shot — making him take the long way around — but he places a wall that cuts off the long route, so now it's illegal for you to block the short route!
The "pawn jumps over opponent's pawn" rule creates interesting
parity
/
zugzwang
situations.
In addition to the typical 9x9 board with 10 walls,
many
papers
have
analyzed
smaller boards and wall counts, since the full game is currently intractable.
Major Results
Parity Advantage vs Tempo Advantage
Many
have
speculated
that Quoridor might be a 2nd player win on odd-height boards due to pawn jump parity. This work shows that odd-height Quoridor boards are
not
always 2nd player wins.
They
are
always 2nd player wins with few walls, but typically turn into 1st player wins at a sufficiently high wall count. For example, 5x5 is a 2nd player win at ≤4 walls per player, but 1st player win at >4 walls.
The intuition here is that odd-height boards have a jump parity advantage for 2nd player, but 1st player still has a tempo advantage, so a sufficient number of walls makes the 1st player tempo advantage dominate the 2nd player's jump advantage.
There are a few notable exceptions discussed below.
Relatedly, we find that even-height boards are uniformly 1st player wins at all wall counts because 1st player has the jump parity advantage
and
the tempo advantage.
Forced Draws
It
was known
that forced draws by repetition were possible to contrive, but this work shows that the 8x3 board with 3 walls per player is a draw
from the starting position
.
Both players must just dance left and right forever. If either player deviates from this repetition, the other player has a forced win, therefore the optimal strategy is draw by repetition.
Weird geometries
There are some geometries with outlier results. For example:
4x7 is a 2nd player win for 0 or 1 wall, 1st player win for 2 walls, then back to 2nd player for 3 walls, then 1st player beyond that.
7x3 never transitions into a 1st player win at any wall count.
3x5 is a 2nd player win at all wall counts
except
3
8x3 is a 2nd player win at all wall counts except 3 (where it's a draw, as noted above).
Full results table
Note: even-heights omitted, they are all 1st player win at all wall counts and geometries.
W x H
0
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
2 x 3
2
1
1
1
1
1
1
1
1
1
1
3 x 3
2
2
2
2
2
2
2
2
2
2
2
4 x 3
2
2
2
1
1
1
1
1
1
1
1
5 x 3
2
2
2
1
1
1
1
1
1
1
1
6 x 3
2
2
2
2
1
1
1
1
1
1
1
7 x 3
2
2
2
2
2
2
2
2
2
2
2
8 x 3
2
2
2
D
2
2
2
2
2
2
2
9 x 3
2
2
2
2
2
2
2
1
1
1
1
2 x 5
2
2
2
2
2
2
2
2
2
2
2
3 x 5
2
2
2
1
2
2
2
2
2
2
2
4 x 5
2
2
2
2
1
1
1
1
1
1
1
5 x 5
2
2
2
2
2
1
1
1
1
1
1
2 x 7
2
2
1
1
1
1
1
1
1
1
1
3 x 7
2
2
2
2
2
1
1
1
1
1
1
4 x 7
2
2
1
2
1
1
1
?
?
?
?
2 x 9
2
2
2
2
2
2
2
2
2
2
2
3 x 9
2
2
2
2
2
1
1
1
1
?
?
You can reproduce the results of this work by running the code in
this repository
. The smaller configurations finish almost instantly, the largest ones in the table take up to 30 minutes on my M3 MacBook Pro. I have 128GB of RAM and the largest configurations use a sizeable chunk of that to store all the precomputed data and transposition table.
Complexity
Quoridor has two main complexifiers.
The "illegal to fully block goal" rule makes enumerating legal moves hard. Naively, you have to do a pathfinding search for every candidate move. This means move generation is several orders of magnitude slower than a game like chess.
Adding to this pain, the branching factor pretty high. On any given turn there are typically 4 pawn moves and about 100 possible wall moves. So not only are the wall moves super slow to check the legality of, there are also a ton of them.
This huge branching factor makes naive alpha-beta
negamax
pretty weak. It takes a decent amount of work to get a bot searching to depth 6 or so.
Beyond the giant branching factor, the
horizon effect
is harder to deal with. In chess, you can deal with the horizon effect pretty easily with
quiescence search
where you search only the "interesting" moves (i.e. captures, checks) until no such moves remain and the position is "quiet".
In Quoridor, there are very few quiet positions because walls can be placed anywhere on the board at any time.
In addition to not being able to look too deep, once you bottom-out on depth, evaluating a position is really hard. You have a short path, great. Can it be cut? Can you block it from being cut? You have walls, awesome — will you be able to effectively use them, or is your opponent in a safe-from-walls corridor? Etc.
All these complexities make me think Quoridor would be really amenable to an
AlphaZero
type approach which shines on games with high branching factors and difficult evaluation functions.
Miscellaneous optimization tricks
A few tricks I've picked up over the years of hacking on Quoridor bots. Some are highly specific to Quoridor, others are well-known in e.g. the computer chess community. Not all of these were used or are applicable to the full solver, but are nonetheless interesting or applicable to a general Quoridor bot.
Wall legality heuristic
If you place a wall floating off in an open area, it's always possible to go around it, so no legality check is needed.
Further, if you place a wall and it's only touching another wall (or board edge) at a single point, it's also always possible to go around it, so no legality check is needed.
You only need to do a legality check if the wall touches another wall or edge at at least 2 of the 3 points the wall touches.
Quoridor wall legality heuristic contact cases
One 9 by 9 Quoridor board showing candidate walls with zero, one, and two contacts.
0 contacts
skip
1 contact
skip
2 contacts
path check!
Most walls are legal
It's almost guaranteed your evaluation function uses path length as an input. This requires running a path algorithm.
Since you are already going to do this for your leaf-node evaluation function, you should skip it during all move generation. Move moves are legal!
Just recurse
assuming
all wall moves are legal, and if you discover at the leaf node that
whoops
we are in an illegal branch, that's fine, just return null instead of a score to mark that this node is invalid.
If you're at an inner node and your very first child returns null,
then
do a path check to see if the inner node is illegal, and fast-return null if it is.
This optimization only works because illegality is monotonic in Quoridor. Once you are in an illegal state, you cannot get to a legal state.
Bitboards
Standard Quoridor is a 9x9 cell board, but walls are length 2, so there are only 8x8 places to place a wall. This means you can represent all the horizontal walls as a 64 bit integer, and all the vertical walls as a 64 bit integer. Getting candidate wall moves can now be done with just a few ops.
Transposition
Transposition table is an easy 2x win. Add in horizontal symmetry for another 2x. You don't even really need to use
Zobrist hashing
since the board state is so few bits, you can either use it as a key outright or hash it in just a few ops.
Solving
Breakthrough optimization
There is one trick that makes solving boards like 5x5 Quoridor fast and easy, and it falls out of these two observations:
There are only 2,532,560 total possible wall configurations on a 5x5 board
If you have all the possible wall configurations, you can precompute legality bitboards for both players for all possible wall states
That is, for each wall state, you floodfill from each player's goal row to make a mask that contains the set of legal cells that player's pawn can be on.
This allows for extremely cheap legality checks. To check if a wall move is legal, you just look up the configuration in the table, and check that both players' pawns are on floodfilled cells.
Below is an example of a board in a legal state vs illegal state from just one player's point of view.
Floodfill mask lookup for Quoridor wall legality
Two 5 by 5 Quoridor boards. The left board is legal because the pawn is inside the floodfilled goal mask. The right board is illegal because the pawn is outside that mask.
Legal state
pawn is inside the precomputed mask
Illegal state
pawn is outside the precomputed mask
Combined with the other tricks, this allowed me to fully solve 5x5 Quoridor in just a few minutes on my laptop.
Unfortunately this solution does not scale to the full 9x9 board which has 10
20
possible wall configurations.
It's likely tractable to spend a few hundred dollars of cloud compute to solve the next frontier of board sizes if someone wants to throw money at the problem.
6x6 is not really interesting since it's almost guaranteed to be a 1st player win due to even height, but e.g. 7x5 would probably be interesting.
Wall Configurations by Board Size
Line graph showing log base 10 of wall configurations with at most 2N minus 1 walls for square boards from 2x2 through 9x9.
Wall Configurations by Board Size
0
5
10
15
20
2
3
4
5
6
7
8
9
Board Size
log
10
wall configurations
Proof search
Previous
work
has
largely focused on using
retrograde analysis
to solve small Quoridor variants.
This work largely uses an algorithm closely related to
proof-number search
which, as far as I can find, appears to have never been applied to Quoridor.
I was not aware of proof-number search before this work, and accidentally re-invented it by modifying the negamax algorithm until it was essentially a proof search.
I had initially started with normal
iterative-deepening
negamax with (-∞, ∞) alpha-beta bounds and win/loss evaluation function, but you can get
significantly
more
beta-cutoffs
by initializing with (0, ∞) alpha-beta bounds.
At each depth, you do a search assuming 1st player wins, and if that doesn't find a forced win, do a search assuming 2nd player wins, and if that doesn't find a forced win, try it all again at the next depth.
Because of this structure, traditional alpha-beta techniques like
move ordering
can significantly speed up the search.
I had gone into this conjecturing that this always terminates and there were no forced draws from the start position. I found the forced draw for 8x3 with 3 walls when the max depth kept ticking up indefinitely, then I added a retrograde solver fallback which proved the draw. The various optimizations mentioned in this work make retrograde analysis tractable for this size.
Additional implementation details
While precomputing all wall configurations and legality masks, you can squeeze out more performance by precomputing a bit more information for any wall configuration:
All legal moves. Move generation is much cheaper with the legality masks, but you can still get a nice constant factor improvement by just precomputing it all upfront.
Distance to goal. This is useful for move ordering which helps alpha-beta. You wanna try moves that help yourself or hurt your opponent first.
Future work
Enumerating wall frontiers instead of whole wall configurations
You really shouldn't actually care about the
full
wall state. You really only care about the exact illegality frontier. That is, the minimal set of walls on the current board that causes the illegality.
Quoridor illegality frontier
A 9 by 9 Quoridor board with a minimal teal wall frontier crossing the board and unrelated slate gray walls elsewhere.
Because illegality is monotonic, once you have such a minimal set, any additional walls are not making the board "more illegal".
So a better algorithm is to enumerate all possible such minimal illegality frontiers instead of all possible wall configurations. Then, implement some clever datastructure that can efficiently check if any illegality frontier is a subset of the current wall state.
Unfortunately, this probably still isn't enough to solve 9x9 Quoridor, the branching factor is still too high even if you could do legality checks in 1 nanosecond.
This method could probably be squeezed to scale to 6x6 or maybe even 7x7 though.
Enumerating all possible paths instead of walls
Rather than enumerating all possible wall configurations or frontiers, you can enumerate all possible paths, then perhaps there is a clever way to efficiently prune the set of valid paths given a current wall configuration. If the set of valid paths is empty, the state is illegal.
I've thought less hard about this one but I feel there is probably something there. The number of possible paths from all squares is pretty tractable for 7x7 — just a few billion.
Divide-and-conquer tiles
There is probably something to be done where you divide the 9x9 board into smaller tiles, e.g. nine 3x3 tiles.
Then you can precompute every possible tile. Each tile is keyed by its wall configuration + goal-reachability situation. A tile's goal-reachability situation is a function of its wall configuration + its neighbors' wall configurations and reachability situations.
This turns your 9x9 pathfinding into a 3x3 pathfinding which should be around 10x faster. It's unclear to me if this is useful for solving, but is probably useful for playing.
Closing thoughts
I'll keep thinking about this problem in the shower every few months and hopefully have some more insights.
It's interesting that the top LLMs — even tasked with grinding on this problem overnight in a harness — don't come close to this insight (tried with gpt-5.5-xhigh in codex CLI). It would be interesting to keep this as a private eval out of the training data, but publishing it is also valuable. It will be interesting to see if future LLMs can improve on this result.
I did of course use coding agents to implement all the code for the most recent version of this project, after providing them the high-level insights described above. I've implemented enough Quoridor bitboards for one lifetime and wouldn't have spent such time revisiting this project without that accelerant.
Call for others
If any enterprising young person is confident they can train an AlphaZero style Quoridor bot for a few hundred dollars of cloud GPU, reach out to me with your proposal and I'd be interested in funding it. I'm really curious what superhuman Quoridor looks like.
Play
