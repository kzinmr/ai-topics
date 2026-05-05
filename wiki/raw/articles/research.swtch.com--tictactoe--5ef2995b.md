---
title: "Play Tic-Tac-Toe with Knuth"
url: "https://research.swtch.com/tictactoe"
fetched_at: 2026-05-05T07:01:02.032405+00:00
source: "Russ Cox (research.swtch)"
tags: [blog, raw]
---

# Play Tic-Tac-Toe with Knuth

Source: https://research.swtch.com/tictactoe

Play Tic-Tac-Toe with Knuth
Russ Cox
January 25, 2008
research.swtch.com/tictactoe
Posted on Friday, January 25, 2008.
Section 7.1.2 of the
Volume 4 pre-fascicle 0A
of Donald Knuth's
The Art of Computer Programming
is titled “Boolean Evaluation.”  In it, Knuth considers the construction of a set of nine boolean functions telling the correct next move in an optimal game of tic-tac-toe.  In a footnote, Knuth tells this story:
This setup is based on an exhibit from the early 1950s at the Museum of Science and Industry in Chicago, where the author was first introduced to the magic of switching circuits.  The machine in Chicago, designed by researchers at Bell Telephone Laboratories, allowed me to go first; yet I soon discovered there was no way to defeat it.  Therefore I decided to move as stupidly as possible, hoping that the designers had not anticipated such bizarre behavior.  In fact I allowed the machine to reach a position where it had two winning moves; and it seized
both
of them!  Moving twice is of course a flagrant violation of the rules, so I had won a moral victory even though the machine had announced that I had lost.
That story alone is fairly amusing.  But turning the page, the reader finds a quotation from Charles Babbage's
Passages from the Life of a Philosopher
, published in 1864:
I commenced an examination of a game called “tit-tat-to” ... to ascertain what number of combinations were required for all the possible variety of moves and situations.  I found this to be comparatively insignificant. ... A difficulty, however, arose of a novel kind.  When the automaton had to move, it might occur that there were two different moves, each equally conducive to his winning the game. ... Unless, also, some provision were made, the machine would attempt two contradictory motions.
The only real winning move is not to play.
