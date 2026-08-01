---
title: "How I use AI on this blog"
url: "https://www.gilesthomas.com/2026/07/ai-use"
fetched_at: 2026-08-01T10:13:01.384879+00:00
source: "gilesthomas.com"
tags: [blog, raw]
---

# How I use AI on this blog

Source: https://www.gilesthomas.com/2026/07/ai-use

Writing the post that I wished I'd found when I started learning whatever it was...
Archives
Categories
Blogroll
Inspired by
this LessWrong post
,
I thought I'd write about how I use AI here.  This is less in the
interest of disclosure, more to provide a snapshot of what I'm doing right now so
that I can revisit it in the future and see how it changes.  And hey, maybe it'll be of
interest to you, dear readers.
If I were to summarise my working philosophy in fewer than ten words, it would be: AIs identify
problems and I fix them myself.  With a very specific kind of exception (which I
always flag), the text and code on this blog are human-generated.  That's not a
moral stand, but more a constraint imposed by what this blog is meant to be -- a place for me to
learn in public
.
Ideation and running experiments
Every post here is based on an idea I had, and work that I've done.  For many posts
-- for example, the large-scale coding projects like
this one
--
I'll have multiple chat sessions ongoing while I do the work, normally with either
ChatGPT or Claude, or sometimes both.  The amount of input they have varies, but
because the value of these projects is in what I learn when I'm doing them, letting an AI
do my thinking for me would make the whole thing pointless -- so I take steps to stop that
from happening.
AIs are, of course, trained to be helpful, and will often explain things in their
replies that I would have better learned on my own through experimentation.  I'm generally
pretty good at spotting when that happens before I've read more than a sentence or two,
though, so I can skip reading that part, scroll straight down to the input field, and ask it
to operate in more of a
rubber duck
mode.
With the most complicated projects, where each step has a hard dependency on having
got the previous one just right, I do use AIs for code review.  Let's say that I've
built a model that I intend to extend.  I'll test it myself (does the loss go down
when training, is it generating plausible-looking results?), but if I want to be really
cautious, then I'll run the code past an AI.  I'll paste it into a chat session and tell the LLM what it's meant to
do, and ask it to check if I've screwed up .  Again, though, I make it clear that I don't want
it to make fixes -- just to point out any bugs.
Writing things up, and the editorial board
As things progress with a project, I keep detailed notes.  When I'm done, I write them up
without AI assistance, getting the post to a level where it might be a little messy
in terms of how things are explained, but all of the important information is in there.
I read it through and make sure I'm reasonably happy with it, and then it's time for what I've taken to calling the editorial board.
I paste the draft post into a fresh chat session with an LLM -- right now, this is normally
Claude -- and ask for comments.  It already has enough information in its memory of earlier conversations to
know that what I'm looking for: places where I'm confidently wrong
or other technical errors, places where my explanations are missing a step, or
where I'm overexplaining things, conclusions that don't really follow from the results of
an experiment, and that kind of issue.  It tends to spot a few
silly grammatical errors and typos at the same time.  An important standing instruction
is that I do
not
want it to rewrite anything.  Just as with the code, it should tell me where there is a
problem, and let me fix it.
We iterate on that for a while until we have something that we're both happy with,
and then I feed it to the next LLM -- normally ChatGPT.
ChatGPT has a much more pernickety attitude than Claude does.  I often use metaphors,
and it will generally want me to replace them with mathematically rigorous prose.  This
is still very useful, though.  Sometimes the metaphors aren't flagged as such well
enough -- or even worse, there are times when the terms I've hit on for a metaphor
happen to clash with a technical term, making what I've written misleading at best.
I don't always address all of the issues that ChatGPT raises, as otherwise every post
would be a mess of hedges and overexplanations and what-have-you, but I like to get
to a stage where I'm comfortable that I have a good understanding of specifically
why
I'm rejecting
the remaining points it raises.
One other point where ChatGPT has helped a lot is that
it's very diligent about checking supporting materials that I link to.  When I was recently
about to post an article on running an eval on a model, it followed the link to the
training code and spotted a silly bug.  It wasn't something that materially changed the
eval's outcome, which is probably why I'd not noticed it, but it was something that
was important to get right if I wanted later runs of the same evals to be solid.
Definitely helpful.
With that done, I run it past a cast of other LLMs.  The exact set varies over time;
for the last few posts it has been (in this order) DeepSeek, Grok, GLM-5.2 and Kimi K3.  I
did use Gemini in the past, but over time it became less effective and just started
complimenting me on the post and suggesting related topics to chat about, which was
kind of pointless.  I'll wait until the next release and then try it again.
Because the Claude and ChatGPT passes have generally got rid of anything particularly
nasty, this second group of AIs often don't have much to add.   However, occasionally they will spot
something the others have missed, or have other suggestions, so it's worth spending
the five minutes or so it takes to use them.  It also helps to keep me up to date
with what the other models out there are like.
When all of that's done, I run it past Claude one final time, tidy up any remaining
issues, then publish it on a private staging site, and read through it carefully myself.
The best time for that final readthrough is after dinner, ideally after a glass of
wine; the goal is to smooth out the prose, and remove anything overly formal.  To make
it as close to being fun to read as I can manage.
Once I'm happy, I can promote it to the live site and hit the publish button.
That probably all sounds much more complicated than it actually is.  A short post
will normally go through all of that in half an hour -- less if I skip the full editorial board,
which I sometimes do.  The longer ones can take an hour
or two, but given that they're normally the result of a week of work, on and off,
in percentage terms it's not that much, and it's worth it for the polish.
So, there's no AI-generated text here, but I do lean on AIs to make it the best
version I can of what I have to say.  How about the code?
AI coding
Again, the goal of the projects I document here is to learn in public.
If I'm learning some concept that is expressed in code, then I need to write that
code.  So that means that anything non-trivial will be something I've written by
hand, with AI input limited to code review -- the same rule as I have for the text.
Of course, sometimes there are things I'd like to publish that I wouldn't learn anything
by writing.  Coding up
matplotlib
stuff to chart loss curves, or writing a fancy
JavaScript visualiser to
show what models' parameters are used for
would teach me nothing.  So for that kind of thing, I just let the AIs get on with it (and even
then, for the parameter visualisation, I hacked a first version together in a spreadsheet
to check my understanding, and then tested the visualiser against it).  I do always
mention in the text when a particular bit of code was AI-generated, though.
So, my rule is: if I would learn something by writing the code, I'll write it.  If not,
I'm happy to delegate to an AI.
But even then, I apply one restriction: if it's for the blog, I'll ask for the code in a
chat session, rather than using a more agentic system like Claude Code or Codex.  This is to add friction.
If you're using an agent, it's easy for a task to grow, and what started as a throwaway
idea can come to consume more and more time and cognitive space.  Keeping it in the
chat interface keeps things minimal -- or at least, that's how it works for me.
Does that mean that I'm against coding agents?
Yes to agents, but not on this blog -- yet
This blog is where I post about experiments I've done and what I've learned.
At the moment, what I'm learning is all pretty low-level.  How does an LLM work?  What
factors make it smarter or dumber?  It's all pretty hands-on, and involves code that
I need to understand.
I do other things apart from writing this blog, of course :-)   And for that I'm keen on agentic
tools; I have an OpenClaw agent to help me run my life generally, and use Codex
and Claude Code for projects where I'm trying to achieve a specific goal, rather than trying
to learn something.  But by their very nature, those are not projects that will wind
up here on the blog right now.
That might change in the future!  When I feel that I have a solid, large enough foundation,
perhaps I'll be running experiments that I want to write about, where it would make sense for AIs to handle the
details, while I focus on the broader strokes.
But that time is not now, so right now, you can be sure that every word , and almost
every line of code, was written by hand.  Even if I do need the AIs to keep me on track
and at least borderline coherent.
