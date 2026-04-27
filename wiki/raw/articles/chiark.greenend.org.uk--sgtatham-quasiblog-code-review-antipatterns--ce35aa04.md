---
title: "Code review antipatterns"
url: "https://www.chiark.greenend.org.uk/~sgtatham/quasiblog/code-review-antipatterns/"
fetched_at: 2026-04-27T07:57:00.064890+00:00
source: "chiark.greenend.org.uk/~sgtatham"
tags: [blog, raw]
---

# Code review antipatterns

Source: https://www.chiark.greenend.org.uk/~sgtatham/quasiblog/code-review-antipatterns/

Code review antipatterns
[Simon Tatham, 2024-08-21]
Introduction
Code review seems like a great idea, right? Two developers
      looking at the same code means two chances to spot problems; it
      spreads understanding of the way the project is evolving; the
      reviewer can learn useful tricks from reading the author’s code
      in detail, or spot opportunities to teach the author a useful
      trick that they didn’t know already.
But that’s only for ‘light side’ code reviewers, who use it to
      try to improve the code base and the developers’ collective
      skills. Code review can also be a powerful tool for totally
      different purposes. When a code reviewer turns to the dark side,
      they have a huge choice of ways to obstruct or delay
      improvements to the code, to annoy patch authors or discourage
      them completely, or to pursue other goals of their own.
If you’ve only recently turned to the dark side, you might not
      have thought of all the possibilities yet. So here’s a list of
      code-review antipatterns, for the dark-side code reviewer who’s
      running out of ideas.
The antipatterns
The Death of a Thousand Round Trips
You start reading the code. As soon as you see a nitpick, you
      add a review comment pointing it out. Then you stop reading.
The developer conscientiously fixes your nitpick, and submits a
      revised patch.
You start reading that version. You spot another nitpick,
      independent of the first. You
could
perfectly well have
      mentioned it the first time, but you didn’t, because you didn’t
      get that far. So you point that out – and stop reading
      again.
And so on. Iterate until the developer loses hope.
If you’re in a very different time zone from the developer, you
      get a natural 24-hour round-trip time, so that the patch evolves
      as slowly as possible. If you’re in a nearby time zone, or the
      same one, then to delay the patch properly, you’ll have to
      arrange to be busy with several other things, so you have a good
      excuse for it taking you a day or two to get round to looking at
      each new version.
Resist the temptation to make any remarks like ‘This is
      looking much better now.’ If you hint that you’re getting closer
      to being satisfied, you’ll give them reason to keep trying!
The Ransom Note
This particular patch seems
especially
important to
      the developer who submitted it. (Maybe they said that outright,
      as part of their argument trying to persuade you to take the
      patch. Or maybe you just read between the lines.)
But this patch isn’t especially vital to you – so you’re in a
      position of power! Now you can hold the change they need hostage
      until they do lots of extra tangentially related work, which
      doesn’t really need to be in the same commit, but which is
      important to
you
.
‘If you ever want to see your beloved patch again …’
The Double Team
One patch. Two reviewers.
Every time one of you demands a change, the developer
      obediently makes it – and now the other one can complain
      instead!
Keep taking turns to make incompatible demands. But always
      direct your comments at the developer. Avoid arguing directly
      with
each other
on the review thread, and don’t
      acknowledge any suggestion from the patch author that the two of
      you should talk to each other and come to a consensus about what
      the patch is supposed to look like.
See how many times you can ping-pong the developer back and
      forth before they give up.
(In a real emergency, if you can’t find an accomplice, you can
      try contradicting
your own
previous review comments.
      But normally someone will notice. It works better with two
      reviewers.)
The Guessing Game
There’s a problem, and lots of different possible ways to
      solve it. A developer has picked one solution and submitted a
      patch.
Criticise that
particular
solution, on some grounds
      that don’t relate to whether or not it solves the problem. Keep
      your criticism vague and woolly: violation of an obscure design
      principle, perhaps, or incompatibility with some vapourware plan
      for future development in the same area. Make the criticism as
      irrelevant as possible to the thing they were really trying to
      achieve.
If you make it vague enough, the developer won’t be able to
      think of any way to adapt their existing patch that they’re
      confident will address your criticisms. Their best bet is to
      choose a totally
different
solution to the original
      problem, and try implementing that instead.
So now you can smack that one down too, in just as unhelpful a
      way!
Don’t let the developer trap you into any conversation like
      ‘ok, how do you think this problem
should
be solved?’,
      or give any hint at a solution you’d be happy with. Sooner or
      later, they’ll lose the will to keep guessing.
The Priority Inversion
In your first code review passes, pick small and simple nits.
      Variable names are a bit unclear; comments have typos in.
Wait for the developer to fix those, and
then
drop
      your bombshell: there’s a much more fundamental problem with the
      patch, that needs a chunk of it to be completely rewritten –
      which means throwing away a lot of the nitpick fixes you’ve
      already made the developer do in that part of the patch.
Nothing says ‘your work is not wanted, and your time is not
      valued’ better than making someone do a lot of work and then
      making them throw it away. This might be enough to make the
      developer give up, all by itself.
The Late-Breaking Design Review
An enormously complicated piece of work has been ongoing for
      weeks or months, in lots of separate patches. Half the work is
      already committed.
You personally don’t agree with the design of the entire piece
      of work, but you weren’t consulted in the original discussions.
      Or maybe you were, but you were on the losing side of the
      debate.
But now you’ve been asked to review a minor but important thing
      in the middle of it, like an easy fix for a bug that’s blocking
      lots of developers. This is your opportunity!
Demand justification for the entire design of the work so far.
      If the developer doesn’t know the answers, because they’re just
      working on one small part of the overall job, then shrug –
      that’s not your problem, and you’re not hitting the ‘Approve’
      button until you’re satisfied.
If you’re really lucky, perhaps you can even manipulate this
      developer into undoing some of the already-done work, by giving
      a plausible excuse why it’s necessary. Carefully avoid letting
      them know where to find the design discussions that contradict
      you.
The Catch-22
If there’s one big patch, then it’s too hard to read! Demand it
      be split up into self-contained sub-pieces.
On the other hand, if there are lots of little patches, then
      some of them make no sense on their own! So insist that they be
      glued back together.
With any large enough piece of work you can surely find a
      reason to make
one
of those complaints; it’s just a
      matter of deciding which.
It doesn’t have to be ‘number of patches in the pull request’.
      You can do this one with any kind of tradeoff that seems
      relevant in the particular case. For example, if the code is
      written legibly, it probably has unacceptably poor performance –
      or if it’s well optimised, it’s unreadable and hard to
      maintain.
The Flip Flop
There’s a type of change that people commonly make to the same
      part of the code, like adding an extra thing to a list. You’ve
      reviewed several of these changes before. Another one has just
      come along: the author has looked at the prior changes,
      carefully followed the existing pattern, and chosen you as a
      code reviewer because you’re clearly used to this area.
Keep everybody on their toes by suddenly objecting to an aspect
      of the change that you’ve never had a problem with before.
      Following the existing pattern just isn’t good enough! The
      author ought to have anticipated that you’ve recently changed
      your mind about what this type of change should look like.
What if the author points out your inconsistency, by showing
      the previous three identical changes where you didn’t raise this
      objection?
Then you say ‘You’re right, those should be changed too.’ Be
      careful not to take any personal responsibility
      –
you’re
not volunteering to change all the existing
      cases. If you’re really lucky the developer will interpret this
      as instructions to change the existing cases themself, and then
      you’ve saved yourself a lot of effort.
But seriously, folks …
Up to here, this article has been a joke.
(I’d hope I don’t even have to say that at all, but I’m
      sure
somebody
would have misunderstood otherwise.)
I’m not
really
intending to encourage code reviewers
      to be annoying and obstructive. And I’m not even really
      suggesting that code reviewers
do
do all these bad
      things, at least on purpose, at least most of the time. Most of
      the descriptions above are exaggerations of what the reviewer
      really does. Or not even that: just an exaggeration of what
      it
feels
like, when you’re the frustrated patch
      submitter, and your patch has been stuck in review for weeks,
      and doesn’t feel as if it’s getting any closer.
I really mean:
don’t
do these things! Try to minimise
      round trips, rather than maximising them. Ask for important
      rewrites (if needed)
before
picking all the trivial
      nits. When you criticise the patch, make constructive
      suggestions about what version of it you
would
accept.
      If you have opinions about the code base as a whole, raise them
      with all the developers in a general discussion, rather than
      being petty with the one developer whose patch you’re assigned
      to review. And if you do any of these things
by
      accident
, have some self-awareness about it: notice that
      you’ve made the developer’s life extra difficult by mistake,
      apologise, and try to compensate by being extra helpful. (Maybe
      even help to improve the actual code, either by writing your own
      revised version of this patch, or doing extra polishing in a
      followup patch of your own.)
Authority
But if there’s a serious point to make here, I think it’s this.
      When one developer becomes the code reviewer for another one’s
      patch, that relationship creates temporary
authority
.
      The reviewer has the power to prevent that particular patch
      being committed, even if they don’t have any kind of authority
      over the patch submitter the rest of the time.
With authority comes responsibility. You’re supposed to use the
      authority only for its intended purpose, and only as much as
      necessary. In this case, that’s to make the patch as good as
      possible, according to whatever definition of ‘good’ the
      development team as a whole has agreed on.
So most of these antipatterns (or the milder behaviours that
      they’re caricaturing) are
abuses of authority
. The
      reviewer is using that temporary power over another developer as
      leverage to pursue some other personal agenda, perhaps
      independent of the goodness of the patch, or perhaps actively
      opposed to it.
The personal agenda in question varies between these
      antipatterns. It could be some unrelated piece of work the
      reviewer is in favour of; it could be personal stylistic
      preferences that the reviewer hasn’t been able to get the rest
      of the team to adopt; it could be laziness, taking advantage of
      the opportunity to write a one-line description of what you want
      and let someone else do the hard work; it could just be plain
      resistance to change, or perhaps even a personal dislike of the
      patch submitter.
And that dislike might be quite justifiable, if the patch
      submitter has done any of these bad behaviours when it was
      last
their
turn to be the code reviewer! That’s another
      reason you should use the code reviewer’s authority sparingly.
      If developers manage to get locked into a cycle of revenge
      against each other, your software project is doomed.
Gatekeeping code review
Up to this point, I’ve been focused on
peer
code
      review. The code reviewer and the patch submitter are
      colleagues; neither is in charge of the other; neither has the
      final say over the code base in general. That’s why the
      authority you get in a code review is
temporary
:
      tomorrow, after this patch lands, you won’t have it any more.
      The day after that, it might be the other way round.
Also, in peer review situations, the code reviewer and the
      author are supposed to have basically the same goal. If there’s
      any serious disagreement about what features should go into the
      code at all, or how polished something needs to be before
      approval, or what the acceptable coding style is, it’s supposed
      to be dealt with outside the context of the code review.
But in other kinds of code review situation, that’s not quite
      the way it works. In particular, if an outsider to your software
      project sends you an unsolicited patch, that’s very different.
(This scenario usually comes up in free software, since anyone
      in the world can modify your source code, and some of them will
      try sending the changes back to you. But it can happen in other
      situations too – inside a company developing proprietary code, a
      developer in one team might try their luck sending a patch to
      another team’s project, if they particularly want a feature or
      fix that the other team hasn’t found effort for.)
In this situation, there’s a much bigger chance that the
      receiver of the patch will be unwilling to accept it at all,
      either because they don’t think that change should be made in
      the first place, or they disagree completely with the way it was
      done. And in this case, that’s
not
an abuse of the
      temporary authority granted by being a peer reviewer: it’s a
      legitimate exercise of the
permanent
authority of being
      the person or team in charge of the project. It’s my software
      project – I get to decide what direction it goes in.
When the code reviewer is in this ‘gatekeeping’ role, it’s not
      always wrong to criticise the patch on the grounds that it
      violates an existing general design principle or requirement
      (
The Guessing Game
), without
      suggesting how the same problem could be solved better. Maybe I
      don’t
know
how that problem could be solved in a way
      that’s consistent with the requirement. In fact, maybe that’s
      precisely the hard part, and the only reason why I haven’t
      already made the same change myself!
But even in a gatekeeping context, it’s rude to deploy ‘The
      Guessing Game’
without explaining
. When I do this, I
      generally try to explain how the developer has overlooked the
      hard part, and if I don’t know the answer myself, I’ll say so.
And, of course, there’s still no excuse
      for
passive-aggressive
obstructiveness
      like
The Death of a Thousand Round
      Trips
. If you genuinely don’t want the patch in the code at
      all, and you’re in a gatekeeping role with the legitimate
      authority to make that decision, you can
say so
in
      words, so the submitter doesn’t waste any more time on it!
Disclaimer
I’ve been collecting notes towards this article for many years,
      from code reviews I’ve participated in (on
both
sides),
      code reviews I’ve observed between others, and code reviews I’ve
      only heard about in conversation.
So it’s not aimed at any specific person who’s reviewed my code
      recently!
