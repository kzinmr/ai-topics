---
title: "Writing a soluble-grid generator for Mines"
url: "https://www.chiark.greenend.org.uk/~sgtatham/quasiblog/mines-solver/"
fetched_at: 2026-04-27T07:01:09.260328+00:00
source: "chiark.greenend.org.uk/~sgtatham"
tags: [blog, raw]
---

# Writing a soluble-grid generator for Mines

Source: https://www.chiark.greenend.org.uk/~sgtatham/quasiblog/mines-solver/

Writing a soluble-grid generator for Mines
[Simon Tatham, 2019-08-26]
Recently, two people emailed me asking the same question about my puzzle collection: they wanted to know how it's possible for
Mines
, my Minesweeper implementation, to guarantee that every grid can be solved without guesswork.
So
 I wrote up a longish answer to that question, and sent it to both 
people. And it seems like a waste not to post it here too.
Both
 my correspondents were curious to know if there was some kind of 
mathematical characterisation of a soluble Minesweeper grid. It's 
certainly possible to
imagine
such a thing –
perhaps it might be along the lines of ‘avoid certain forbidden configurations of mine squares’.
If
 there were one of those, then Mines's generator would almost certainly 
be a lot simpler. But I don't know of any rule of that kind; I very much
 doubt that there's a fully general one (that leaves
every
soluble grid still permitted). You very likely could come up with a rule
 of that kind that errs on the side of caution, so that any pattern of 
mines it lets through is soluble. But I think it would almost certainly 
rule out a lot of legal grids that you didn't want ruled out: it would 
constrain layouts far more than necessary, reducing variety of gameplay,
 and worse still, constituting an extra hidden clue to the mine 
positions for anyone who knows how the generator is working.
(Perhaps
 there wouldn't be that many players who did know. But I'd be one of 
them, and not very surprisingly, I care about keeping these puzzles fun 
for
me
to play!)
So I didn't do anything like that. It's done in a completely different way.
The
 first part of the answer is: the code has to include an actual solver, 
which simulates a human playing the game, and performs the same types of
 deduction that the human can use, reliably and quickly. (Including 
tracking what the player does and doesn't know about the grid at a given
 moment, of course.)
That would be enough by itself to generate a guaranteed-
soluble
 grid at one of the standard Minesweeper settings (say, 16×16 with 40 
mines). You could just lay out mines at random, run the solver, and if 
it didn't succeed, regenerate a fresh random grid and try again. When 
you get one that the solver thinks is possible, you can return it to the
 user. At the standard settings, a large enough proportion of grids are 
soluble that you wouldn't expect to have to try very many times before 
getting lucky.
(All this thinking, of course, has to be delayed 
until the user places the first mouse click, because solubility depends 
critically on where you're starting from. It's very common that a grid 
which can be solved starting from
this
empty square can't also be solved starting from
that
one, even if both starting points would open up an area of more than one square.)
But
 my Mines doesn't stop there. There's another piece of machinery I put 
in to try to do better than brute force, by making small
changes
to the grid as the solver progresses. If the solver gets stuck part way
 through solving the grid, I don't just throw the whole thing away and 
try again from scratch. Instead, I rearrange mines in the parts of the 
grid the solver hasn't opened up yet, so as to make sure at least one 
new deduction can be made at the current frontier. So the solver gets to
 make more progress, and if it gets stuck again, another modification 
might be needed.
So the solving process proceeds, with the solver 
and perturber taking turns on the grid. When it comes to an end, they've
 managed to open up all the non-
mine squares. Are we now done? Well, not quite.
The reason why not is because I don't make any effort to
completely
guarantee that the perturbations I make are safe, in the sense of
provably
not introducing a problem somewhere else, or affecting a square that a 
deduction has already made use of. There are probably things I
could
do along those lines, but I decided it wasn't necessary: it's enough that perturbing the grid like this
usually
doesn't break solubility. (In that, if you do affect a square that a 
deduction has already used, there will often be a replacement deduction 
in the same area that can still be made, or some other way to get round 
to the same place from a different angle.) So there's always a chance 
that one of the tweaks to the grid will introduces a new blockage in the
 course of removing another one. This is especially likely if something 
has to be changed right at the
end
of the solving process: if 
the last 2 or 4 squares have a problem that needs a mine moving out of 
them, and there's no other covered square remaining to move it to, I 
just have to pitch the mine randomly into the already-
opened area and hope it doesn't cause trouble.
So, if the solver gets all the way through the grid but it needed at least one perturbation along the way, then it's not
completely
guaranteed that the grid is genuinely soluble. Therefore, at that 
point, I run the solver again, from the same starting point, and see if 
it can get all the way through
this
time without getting stuck!
If it can,
then
we return the grid to the user; otherwise, we try again, making more 
small random modifications in areas where things are blocked, and again,
 simply
hoping
that we solve more problems than we create, so that the next run will go better.
The
 very last resort, of course, is to give up completely and regenerate a 
fresh grid from scratch. I've tried hard to avoid that in favour of 
incremental modifications, but sometimes things do just keep going badly
 and you have to pick a completely new starting point. My strategy for 
that is: as long as each run of the solver requires fewer perturbations 
to the grid, we consider that things are still improving, but if a run 
through finds
more
problems than the previous run, we conclude that we're stuck in a local optimum with no clear path through to a working grid.
This is all very heuristic, of course. I didn't have rigorous reasons to be
sure
this particular strategy would work. I just thought it was worth a try,
 based on having tried similar things in other puzzles, using other 
algorithms from this general class which I think of as ‘discrete but 
imprecise’. The basic idea is that if you're trying to generate an 
object satisfying a complicated constraint, then as long as the
checker
is reliable, the code that generates candidates doesn't have to be: 
it's OK for it to have a nonzero failure rate, as long as the failures 
don't consume too much time. (In some puzzles that's achieved by going 
very fast, so that it doesn't matter if you fail often; in others, by 
taking great care to fail infrequently, at the cost of each attempt 
taking longer. It all depends.)
In fact, this one turned out to 
work so well that I was able to provide default settings with over twice
 the mine density of the Windows standard ones, and the algorithm still 
doesn't take too long before it finds a usable grid. That was actually a
 complete surprise to me –
I hadn't anticipated it before the code 
was finished! I had expected to get the normal Windows settings with 
less annoyance, and I did get those, but then I thought, ‘I wonder how 
much further I can turn up the density?’, and the answer was ‘much, much
 further than I expected!’
