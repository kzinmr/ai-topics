---
title: "Consensus Board Game"
url: "https://matklad.github.io/2026/03/19/consensus-board-game.html"
fetched_at: 2026-04-30T07:01:58.000962+00:00
source: "matklad.github.io"
tags: [blog, raw]
---

# Consensus Board Game

Source: https://matklad.github.io/2026/03/19/consensus-board-game.html

I have an early adulthood trauma from struggling to understand
          consensus amidst a myriad of poor explanations. I am overcompensating
          for that by adding my own attempts to the fray. Today, I want to draw
          a series of pictures which could be helpful. You can see this post as
          a set of missing illustrations for
Notes on Paxos
, or, alternatively, you can view
that
post as a more formal narrative counter-part for the
          present one.
The fundamental idea underpinning consensus is simple majority vote.
            If R0, … R4 are the five committee members, we can use the following
            board to record the votes:
A successful vote looks like this:
Here, red collected 3 out of 5 votes and wins. Note that R4 hasn’t
            voted yet. It might, or might not do so eventually, but that won’t
            affect the outcome.
The problem with voting is that it can get stuck like this:
Here, we have two votes for red, two votes for blue, but the
            potential tie-breaker, R4, voted for green, the rascal!
To solve split vote, we are going to designate R0 as the committee’s
            leader, make it choose the color, and allow others only to approve.
            Note that meaningful voting still takes place, as someone might
            abstain from voting — you need at least 50% turnout for the vote to
            be complete:
Here, R0, the leader (marked with yellow napoleonic bicorne), choose
            red, R2 and R3 acquiesced, so the red “won”, even as R1 and R4
            abstained (x signifies absence of a vote).
The problem with
this
is that our designated leader might
            be unavailable itself:
Which brings us to the central illustration that I wanted to share.
            What are we going to do now is to
multiply
our voting.
            Instead of conducting just one vote with a designated leader, the
            committee will conduct a series of concurrent votes, where the
            leaders rotate in round-robin pattern. This gives rise to the
            following half-infinite 2D board on which the game of consensus is
            played:
Each column plays independently. If you are a leader in a column,
            and your cell is blank, you can choose whatever color. If you are a
            follower, you need to wait until column’s leader decision, and then
            you can either fill the same color, or you can abstain. After
            several rounds the board might end up looking like this:
The benefit of our 2D setup is that, if any committee member is
            unavailable,
their
columns might get stuck, but, as long as
            the majority is available, some column somewhere might still
            complete. The drawback is that, while individual column’s decision
            is clear and unambiguous, the outcome of the board as whole is
            undefined. In the above example, there’s a column where red wins,
            and a column where blue wins.
So what we are going to do is to scrap the above board as invalid,
            and instead
require
that any two columns that achieved
            majorities
must
agree on the color. In other words, the
            outcome of the entire board is the outcome of any of its columns,
            whichever finishes first, and the safety condition is that no two
            colors can reach majorities in different columns.
Let’s take a few steps back when the board wasn’t yet hosed, and try
            to think about the choice of the next move from the perspective of
            R3:
As R3 and the leader for your column, you need to pick a color which
            won’t conflict with any past or
future
decisions in other
            columns. Given that there are some greens and blues already, it
feels
like maybe you shouldn’t pick red… But it could be
            the case that the three partially filled columns won’t move anywhere
            in the future, and the first column gets a solid red line! Tough
            choices! You need to worry about the future
and
the
            infinite number of columns to your right!
Luckily, the problem can be made much easier if we assume that
            everyone plays by the same rules, in which case it’s enough to only
            worry about the columns to your left. Suppose that you, and everyone
            else is carefully choosing their moves to not conflict with the
            columns to the left. Then, if you chose red, your column wins, and
            subsequently some buffoon on the right chooses green, it’s
their
problem, because you are to their left.
So let’s just focus on the left part of the board. Again, it seems
            like blue or green might be good bets, as they are already present
            on the board, but there’s a chance that the first column will
            eventually vote for red. To prevent that, what we are going to do is
            to collect a majority of participants (R0, R2, R3) and require them
            to commit to
not
voting in the first columns. Actually, for
            that matter, let’s prevent them from voting in
any
column
            to the left:
Here, you asked R0, R2 and R3 to abstain from casting further votes
            in the first three columns, signified by black x. With this picture,
            we can now be sure that red can not win in the first column — no
            color can win there, because only two out of the five votes are
            available there!
Still, we have the choice between green and blue, which one should
            we pick? The answer is the rightmost. R2, the participant that
            picked blue in the column to our immediate left, was executing the
            same algorithm. If they picked blue, they did it because they knew
            for certain that the second column can’t eventually vote for green.
            R2 got a different majority of participants to abstain from voting
            in the second column, and, while we, as R3, don’t know which
            majority that was, we know that it exists because we know that R2
            did pick blue, and we assume fair play.
That’s all for today, that’s the trick that makes consensus click,
            in the abstract. In a full distributed system the situation is more
            complicated. Each participant only sees its own row, the board as a
            whole remains concealed. Participants can learn something about
            others’ state by communicating, but the knowledge isn’t strongly
            anchored at time. By the time a response is received the answer
            could as well be obsolete. And yet, the above birds-eye view can be
            implemented in a few exchanges of messages.
Please see the
Notes
for further details.
