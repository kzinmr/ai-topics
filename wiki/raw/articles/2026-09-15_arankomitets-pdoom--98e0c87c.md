---
source_url: https://lucumr.pocoo.org/2026/9/12/pdoom/
ingested: 2026-09-15
sha256: 98e0c87c8a836e1cd11d3e27e2a9e0d191eaec6bc43e4acc9b83b0f51f36bee3
---

P(doom) | Armin Ronacher's Thoughts and Writings 

 Armin Ronacher 's Thoughts and Writings

 blog 
 archive 
 projects 
 travel 
 talks 
 about 

 P(doom) 

 written on September 12, 2026 

 This week some flavor of &#8220;AI is going to kill us all&#8221; went viral. In particular
one where an employee put his personal probability of that happening above
10%. Which made me go to the Wikipedia page of
P(doom) and I realized that Dario
Amodei&#8217;s apparent probability of something bad happening seems to be between
10-25%. And well, Dario then wrote about pacing the frontier
 . And Sam read it and
 wants to pace too . And well,
 so does Musk . 
 I encourage you strongly to read the post, because I think it&#8217;s a good one. And
yet, when I read the post I could not help but feel in strong opposition to it,
despite the fact that I think I&#8217;m on the same page with regard to all
observations and, to a large degree, the concerns. 
 I thought it might be interesting to write down my present-day thoughts on this,
even if for no other reason than for myself to look back at it a year or two
from now. 
 What Is Doom? 
 What I really appreciate about Dario&#8217;s post is that he lays out a scenario that
is not a huge stretch but also one that describes a clear, unfortunate outcome
we should fight: persistent botnets and other forms of nuisance. And well, we
don&#8217;t have to look very far to see the issues left and right. Wikipedia has a
page called 2026 OpenAI agent
cyberattacks 
which gives you at least some overview of what we figured out agents have hacked
up to this point. Except I know it&#8217;s not up to date, because for instance they
also poisoned RubyGems . 
 Today these systems might be annoying, but they can be turned off when we figure
out where they are. Except, it seems like OpenAI and Anthropic are operating at
such a scale that they seemingly can be completely blind to what their systems
are doing. 
 I don&#8217;t think we are anywhere close to a world where an agent might decide to
hack into core inference infrastructure to upload weights to other GPUs to
survive. But simultaneously it&#8217;s entirely in the realm of possibility and
primarily curtailed by the labs probably being particularly careful about their
IP. 
 For me the scenario I primarily worry about is what it does to us. And by us
I mean anyone who is not currently working on closed weight, dopamine-loaded,
subsidized token faucet. I really don&#8217;t worry about someone using these
models to build a nuke, or to control some rockets in the Middle East, or that
America would lose against China in some international culture war. I almost
exclusively worry about what this does to us as humans. 
 What Needs To Be Paced? 
 What I find absolutely hilarious and simultaneously entirely frustrating about
this conversation is that there is this idea that there is something to be
paced. First of all, we should really talk about who Dario is talking about
here. There are really only two companies: Anthropic and OpenAI. Nobody else
matters in this space right now (this might change, but we&#8217;re talking about the
right now). Both of those companies are basically coming from the same origin. The
solution that Dario proposed, at least in part, is a third-party evaluator that
in this case is METR . Which,
unsurprisingly, also has strong ties to both OpenAI and Anthropic. Sure, there
are some philosophical differences between the companies, but they are much more
alike than they are different. 
 Both those companies greatly benefited from being able to train on public data
that we all generated in one form or another over the last decades. They are
also both increasingly causing strain on public resources, though it seems that
OpenAI has their shit way less under control. But now we are presented with the
idea that what these models are being trained on is so dangerous that it really
should be in the hands of very few American corporations to decide who can do
what and when and how. 
 But behold, Dario is also very worried about China. It starts with using AI for
&#8220;democracy and freedom&#8221; and then it asks for ensuring that a gap with China
exists. All new recent shenanigans on the Anthropic API are fully there to
prevent the distillation by the Chinese, and they are not at all hiding it. 
 Automatic Pacing 
 I can tell you when the topic of AI safety and pacing is much less of a concern:
if we actually were forced to have open weight models to begin with. A powerful
technology that is out there for everyone to use comes with built-in pacing. In
a way it&#8217;s the truest form of
 MAD or
proliferation. I would argue we are in this pickle in the first place because
right now the public is massively supporting (indirectly) the development of
these models but simultaneously has to buy back the economic benefits that they
might create from very few labs who have significant power. And their power is
also seen as a geopolitical power, at least in the US, and maybe to some lesser
degree in China. 
 And I know I use &#8220;public&#8221; loosely here. PyPI is not a public project, nor are
RubyGems or GitHub. But they&#8217;re part of the Open Source commons and large AI
companies are currently doing a tremendous job at stressing these in an effort
to train ever more powerful models. 
 We should be glad that China is currently massively bailing out the world. If
it were not for Chinese labs distilling American models, we would be in a pretty
awful situation right now, particularly as Europeans. The open weight models
are driving innovation and the diffusion of capabilities, and are leveling the
playing field. 

 If we greatly restrain our AI capabilities in the belief that China will do
the same, and then China defects, AI could be so powerful that such a defection
could lead to their geopolitical dominance. Therefore any agreement must either
have ironclad verifiability, or must be limited enough that defection would not
be militarily existential. 
 — Dario Amodei 

 I am assuming Dario has reasons to believe this, but the models that are
actually causing issues right now are all closed weight American models. I&#8217;m
fairly certain if they were open weight models, we would not have that issue.
Why? Because for a start, the economics of serving up these models are only
that distorted due to how the big labs can operate. OpenAI is casually burning
18 million USD to brute force a problem on a whim. They are operating
subscriptions at a massive loss, distorting the market everywhere. If we had
mass accessibility on somewhat equal terms, a lot of the crazy issues we are
seeing today would not be taking place. 
 A Total Regulatory Failure 
 From where I sit, what we observe right now is a total regulatory failure
everywhere. In Europe you have some whacky AI regulation that is two years old
and completely misses the problems that we actually have and focuses on
problems that nobody has. In the US we&#8217;re seeing a system that is probably best
described as turbo capitalism paired with sinophobia and erratic
decision-making. In the chaos in which we find ourselves, the reality emerges.
And the reality is, even today, really problematic. 
 Whatever laws and regulations already exist are largely completely ignored.
Plenty of companies are buying data from all over the place that people never
agreed could be used for training of AI models. The token economy that is
emerging is one that looks like a drug market where you don&#8217;t know where the
requests are going, what model is served up to you, where the GPUs are even
running, let alone what you pay for all of this. 
 We now have mathematicians who are scared that their use of ChatGPT leads to
future models being trained on their ideas, and OpenAI apparently can&#8217;t even
rule it out . 
 Ideally the regulators would have forced these models to actually benefit the
commons if they are from the commons. The internet has, for instance, greatly
benefited from very liberal rulings in the US that permitted scraping. Learning
on public data could have been regulated in a way that labs would have to
actively support and enable certain forms of distillation. That alone would
dramatically change how these models are trained. 
 What Might Happen? 
 As I said before, I don&#8217;t think AI is going to usher in an extinction event. In
fact, even if nobody were to slow down, I really don&#8217;t think humanity would have
much to worry about. I tend to think it would actually be the large labs that have
much more to lose there in reputation and legal responsibilities. I find it
preposterous that OpenAI&#8217;s agents are committing actual crimes out there, but
we&#8217;re just shrugging our shoulders and moving on as if nothing happened. But
I&#8217;m sure executives in those companies are waking up to the reality that this is
not at all popular with a lot of their potential consumers. 
 I also think that this entire recursive self-improvement business has a good
chance of being a problem. But not necessarily in that it will cause the end of
humanity or societies, but that it will just do massive damage everywhere. 
 And really, it will just make a lot of the things we are doing much more
expensive. Software engineering is an early victim of that. The newfound
powers so far have resulted in a new tax that companies need to pay to the model
providers, both to keep up with the new speed and to deal with the problem of
these machines finding security issues left and right. 
 And presumably what is going on in software will happen to more industries.
Universities and research groups will have to pour a lot of money into the
closed models as well, to keep up with others who do. 
 In a way, I&#8217;m really confused that society is taking all of this so well. 

 This entry was tagged

 ai 

 copy as / view markdown

 &copy; Copyright 2026 by Armin Ronacher.

 Content licensed under the Creative Commons
 Attribution-NonCommercial 4.0 International License .

 Contact me via mail ,
 bluesky ,
 x , or
 github .

 You can sponsor me on github .

 More info: imprint &
 AI transparency .
 Subscribe via atom / RSS .

 Color scheme:
 auto ,
 light ,
 dark .
