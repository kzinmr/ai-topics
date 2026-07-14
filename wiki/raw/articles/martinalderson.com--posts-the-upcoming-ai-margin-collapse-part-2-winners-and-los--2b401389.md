---
title: "Winners and losers in the coming AI margin collapse (part 2)"
url: "https://martinalderson.com/posts/the-upcoming-ai-margin-collapse-part-2-winners-and-losers/?utm_source=rss&utm_medium=rss&utm_campaign=feed"
fetched_at: 2026-07-14T07:01:12.706617+00:00
source: "martinalderson.com"
tags: [blog, raw]
---

# Winners and losers in the coming AI margin collapse (part 2)

Source: https://martinalderson.com/posts/the-upcoming-ai-margin-collapse-part-2-winners-and-losers/?utm_source=rss&utm_medium=rss&utm_campaign=feed

This is the second article in a two part series focusing on what I believe is perhaps the least understood upcoming shift in AI economics. If you haven't read it yet, I'd recommend starting with
part one
. As always, if you enjoy my writing I'd love it if you subscribe to my
newsletter
or
RSS feed
.
As always a week is a long time in AI. In the previous article I discussed the impact of "good enough" models for many agentic workflows - focusing on GLM5.2. In the brief spell of time since I wrote that, Grok 4.5 was released with similar capabilities
and
is also aggressively priced, which strongly hints at a glut of similar quality models coming out.
Your margin is my opportunity
This is one of Bezos's most famous quotes, and for good reason. It illustrates the dynamic in highly competitive markets - any margin becomes a
weakness
that others can exploit.
I think Grok 4.5's aggressive pricing - at $6/MTok output, it's being offered at a similar cost to hosted GLM5.2 - shows this up. While xAI is unlikely to beat OpenAI or Anthropic at the very frontier of intelligence, it shows exactly where they can get some traction - price.
It's going to be telling to see what happens to pricing over the next few months. It feels like the market is bifurcating into two -
expensive
very high end models (Fable, and perhaps GPT5.6 Sol) - and then a broad swath of good (~Opus), cheap models. While this has always been the case - a lag between the frontier and everyone else - I strongly believe the dynamic has switched a bit with these models now becoming
good enough
for many agentic tasks.
The winners
There is no doubt to me the real winners in all this are semiconductor companies and the entire downstream supply chain to LLM inference. Memory, GPUs, datacentres and the power and cooling needed continue to be
severely
supply constrained
. And with cheaper models, microeconomics tells us that demand
increases
. But my guess is that the value increasingly accrues to the
hardware
layer
of the value chain, not the
software
layer.
This isn't what we've typically seen in tech, and is a significant adjustment for many working or analysing the space. Typically hardware was viewed as the ugly duckling value wise - with punishingly low margins and poor ability for suppliers to differentiate products in the market for the most part. Software would sit on top and take all the margin.
Now, by no means am I suggesting that hardware will take
all
the value. But compared to previous technology waves, perhaps with the limited exception of Apple and the iPhone's cash generation ability, this has very much been the exception to the rule.
Apart from the hardware supply chain itself, there are opportunities for the hyperscalers/neoclouds and hosted inference providers to take
some
value from serving these lower cost models. Serving models like this at serious scale is still difficult, and proprietary efficiency improvements these companies can come up with will give them a competitive advantage. And the quality of these companies relationships with the underlying hardware providers do give them an edge, at least until/if supply starts to catch up with demand.
The most interesting case here is the coding agents - the Cursors of the world. For a long time they faced a brutal path forward: they were reselling frontier inference bought at close to
retail API prices
, which left them with wafer-thin (or outright negative) margins on their heaviest users. "Good enough" cheap models flip that overnight. A coding agent can now offer something 90% of the way to Opus on a model costing a fraction of the price - and actually make money doing it. But the bigger prize is the data they sit on top of: a firehose of real-world agentic usage - which prompts work, which edits developers accept or throw away, and exactly where the model gets stuck. That is the kind of signal a model provider would kill for to train the next generation. It's no wonder xAI bought Cursor - not for the IDE, but for the cheap-model economics and the analytics flywheel underneath it.
But, I think the real winners out of all this are the users and consumers of LLM inference. Being able to access such high quality intelligence for such a relatively low price is hugely exciting. Back when inference APIs were in their infancy, it looked quite possible that there might be
just
OpenAI providing inference to any reasonable quality, now we have a multitude of models with substantially better intelligence than GPT4 available for 5-10% the price of that model.
The losers
This is where it gets tricky. You're probably expecting for me to say the frontier AI labs, but I'm extremely torn on this.
Predicting AI market dynamics is tough. On one hand, I
do
believe that there are suddenly a large chunk of AI use cases that can be moved over to open/cheaper models with little to no loss of quality. This is no doubt a real problem - Anthropic reportedly earns
around 80% of its revenue
from API usage - which does leave them exposed to people switching out their models for cheaper ones.
On the other hand, I think there are two wildcards at play.
Firstly, I strongly suspect that the frontier labs will increasingly move to not releasing their most powerful models to "everyone". And I
don't
mean for security/safety reasons, though no doubt that is one factor - and may be one explanation for this move.
I can definitely see a world in the near future where you can only access these frontier models through a higher level of abstraction with no API
and
no direct coding agent use. Instead, to use these models you have to use their
managed agent platforms
, which makes it
much
harder to swap out other models - you don't have true control of the harness. And it substantially reduces the risk of
model distillation
, which makes it a lot harder for the Chinese providers to keep up.
Secondly, this also assumes that "good enough"
is
good enough for long. It's highly likely that in a few months we'll get a new set of frontier models which are
another
leap forward
that makes the current set of models look like an antique - either in intelligence terms, or perhaps with some other breakthroughs (speed, context length, continual retraining, who knows).
And if we got these leaps forward then suddenly the way we do and think about agentic workflows totally changes
again
, much like the leap from chat UIs to coding agents.
In essence, I think it comes down to if the frontier labs
can
keep innovating, and arguably if they can
increase
their lead over the open weights models. It feels
right now
to me that isn't happening and the lead is shrinking, but I don't think it's a good bet to make - we've seen so many shifts and changes.
The B2C wildcard
The other wildcard I've been thinking about is the now
very
overlooked B2C market. With the explosive growth of coding agents and related use cases, the AI market in general has massively shifted to B2B (and really, enterprise) over the past 12 months.
I think the one thing to keep an eye on is if
anyone
cracks LLM adjacent advertising. OpenAI have rolled this out, Anthropic have ruled out (as far as I know) running ads, and (surprisingly) I'm barely seeing any ads in my Gemini chat sessions from Google.
There are at least 1 billion MAUs of ChatGPT alone - and while this growth has plateaued - this alone represents an enormous amount of
consumer
engagement which still hasn't been monetised past subscriptions.
If someone does crack this, expect the hype pendulum to start swinging back to B2C again - changing habits of B2C users is often
very
difficult, as Google's complete and persistent dominance of web search for so long proved.
Conclusion
So where does this leave us? If I had to bet, the margin in pure model inference is heading towards zero. "Good enough" open models, plus a brutally competitive hosting market, see to that. Bezos's line still holds - but the opportunity is being captured either side of the model layer, not by it. Underneath, by the hardware and power supply chain everyone is scrambling over. And on top, by the users and consumers now getting what would have been unthinkable intelligence a couple of years ago for pennies.
The frontier labs are the one group I'd be wary of betting against. They have two ways out of the commodity trap: keep the intelligence lead wide enough that people happily pay a premium for it, or wall the best models off behind managed platforms where you can't simply swap in something cheaper. My hunch is they'll try both. Whether it works comes down to one thing - whether that lead stops shrinking. Right now, it doesn't look like it is.
