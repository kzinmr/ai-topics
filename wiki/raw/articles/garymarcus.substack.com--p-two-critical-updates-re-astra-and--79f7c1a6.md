---
title: "Two critical updates re: Astra and mathematics"
url: "https://garymarcus.substack.com/p/two-critical-updates-re-astra-and"
fetched_at: 2026-08-04T10:18:16.302072+00:00
source: "garymarcus.substack.com"
tags: [blog, raw]
---

# Two critical updates re: Astra and mathematics

Source: https://garymarcus.substack.com/p/two-critical-updates-re-astra-and

First, abstracting from all the words
in my long analysis on OpenAI Astra yesterday
, the overall point was that Astra may not be the breakthrough that OpenAI wants you to think it was. I expressed concerns about how little they revealed about what they did. Moreover, I thought I didn’t stress it there, we all know they are facing huge economic and competitive pressures; they need a win. I am often left with the feeling that their public facing communications are better marketing than they are science.
My jaw dropped a couple hours after my own post, reading this from
Levent Alpöge
, an accomplished mathematician who works at Anthropic:
so after 24h i have half of them with fable

i didn’t see much discussion of prompting in the announcement but this is a similar setup as with my e.g. unit distance announcement:

totally autonomous,
generic prompt,
no internet
(+ paranoia to ensure no information leaked)
Sebastien Bubeck
@SebastienBubeck
yes, nonsofic groups exist: this statement is one of many new beautiful results proved by Astra, our next major model.

We're releasing 10 such Astra proofs, complete with lean certificates and CoT walkthroughs for each of them. The results are wide-ranging, from von Neumann
9:59 AM · Aug 2, 2026
·
288K Views
52 Replies
·
45 Reposts
·
894 Likes
One
(obviously smart) guy at Anthropic was able to “replicate” (as best he could given OpenAI’s very sparse report of what they actually did) half of OpenAI’s results within 24 hours.  And not with Astra or some other new model, but with the already publicly-released Fable.
I had a couple reactions to this.
a. Alpöge’s fast partial replication made me wonder whether OpenAI’s real advance here was finding (through AI)
which open problems were amenable to a certain kind of search and verify technique
.  OpenAI’s Noam Brown acknowledged, without much detail, that there were failures on some (and maybe many) others:
And yes we did try other major problems without success. Sadly no Millennium Prize problems (yet).

But also, we didn’t spend a lot on each problem. It’s possible to push test-time compute much further.
9:01 AM · Aug 1, 2026
·
259K Views
66 Replies
·
82 Reposts
·
1.99K Likes
Unfortunately, beyond that OpenAI does not report which problems they tried and failed at. They have given us a numerator without a denominator, always a worrisome sign.
This doesn’t take away from OpenAI’s accomplishment - if the system solved a bunch of open problems that’s very impressive – but it again raises questions about what the scope is: all math? A certain subset of problems that can be searched in a certain way?
Maybe once that subset has been flagged, maybe many systems can do them. That’s kind of what Levent Alpöge‘s partial replication shows.
And many what was most critical was not some innovation in Astra per se but the idea (probably from a human) to do this particular search.
b.  Alpöge‘s fast partial replication undermines the widespread presumption that Astra is a major breakthrough. Astra is an obviously an advance to some degree, but that degree may well turn out to be merely incremental relative to other recent models.
Related to this, I was interested to read in
The Information
this morning that OpenAI hasn’t decided whether to call Astra (which was an internal code name) GPT 6 or GPT 5.7. If OpenAI truly thought Astra was a quantum leap,, I doubt that would be such a hard choice.
How good Astra is in open-ended real-world problems very much remains to be seen.
§
Second, a longtime reader of this newletter, Ihor Gowda, pointed me to
a fantastic lecture given by Terence Tao
, by any measure one of the world’s leading mathematicians; many see Tao as
the
leading mathematician. His lecture is lucid, accessible, and genuinely important.
What’s more you don’t need to be a professional mathematician to read it. It should be mandatory reading for anyone thinking about how AI will affect mathematics,  and strongly recommended for anyone who cares about AI’s impact on the world.
One of the issues that he raises he calls “proof indigestion”; what happens if AI creates a lot of stuff, much of it true, but not necessarily
useful
:
Tao’s July 26th lecture, written before the Astra announcement, also prefigures another key point that I made yesterday:
being good at creating certain sorts of proofs doesn’t mean that an AI system can contribute to all (or even most) of the goals of mathematics
. He too distinguishes between solving open problems (which Astra seems strong at, perhaps with some important limits) and building theory (no evidence thus far that Astra can do that):
Tao is no Luddite, or even anti-AI. He is very open to AI, and eager to find a place for it in mathematics.
His lecture
is a beautiful read on how to do just that — to bring AI into mathematics, as thoughtfully as possible. Highly recommended.
P.S. Cartoon of the day, illustrating
Brandolini’s law
:
Noawadays, as the engineer Wouter Vreugdenhil, who brought the cartoon to my attention, points out, “that’s the game.”
Wouter Vreugdenhil
@WouterW_Vreug
OpenAI sustain investor faith with minimal effort. Proving them wrong takes years and expertise most people lack. That's the game.🤷‍♂️
6:46 AM · Aug 3, 2026
·
3.55K Views
1 Repost
·
8 Likes
