---
title: "The Coming AI Compute Crunch"
url: "https://martinalderson.com/posts/the-coming-ai-compute-crunch/?utm_source=rss&utm_medium=rss&utm_campaign=feed"
fetched_at: 2026-05-01T07:02:07.022112+00:00
source: "martinalderson.com"
tags: [blog, raw]
---

# The Coming AI Compute Crunch

Source: https://martinalderson.com/posts/the-coming-ai-compute-crunch/?utm_source=rss&utm_medium=rss&utm_campaign=feed

There has been so much written about the "unsustainable" AI capex recently. Thinking through this recently it occurred to me this is potentially the wrong way to think about it, and it's actually more likely from my research we're going to experience a very significant crunch on compute in the coming years.
I think this is very pertinent as over the holiday season it seems nearly
everyone
who works in software engineering has finally figured out quite how good coding agents with the latest models have got - and really validates my thesis that as models continue to improve token consumption is going to explode.
My token consumption journey
Like I'm sure many of my readers, I was certainly an early adaptor of LLMs, especially once ChatGPT came out. I'd ask questions, get it to help with writing and various other simple (in hindsight) tasks - but probably no more than a few times a day. I'd estimate my token consumption around 5-10k tokens/day back then.
Once GPT4 (and later, Sonnet 3.5) came out, the "knowledge" of the models increased dramatically. This dramatically increased my token consumption - I basically always had one screen open with a chat UI, constantly asking questions and asking for help. I never really got into the VSCode Copilot 'autocomplete' workflow that many did - I found it distracting. But there was certainly an awful lot of copying and pasting code from one browser window to my IDE. I'd guess there was likely a 5 fold increase in my daily token consumption (and I started hitting free plan usage limits
hard
, purchasing what would be come one of many paid subscriptions for these tools).
Less than a year ago I started using Claude Code - I must admit like a lot of people I was highly sceptical of the concept at first. Within a few months I rarely opened my IDE and my token consumption absolutely skyrocketed - so much so within a week I was on the Max plans from Anthropic.
Now with Opus 4.5 it's increased even further. I'm far more confident leaving agents churning through stuff without constantly
babysitting them
, working in parallel, using millions upon millions of tokens. I've also started using them for more and more non-software engineering tasks,
using CLIs
to wrap loads of the products I use on a regular basis to give them an agentic compatible experience.
While I don't have detailed stats, I'd estimate in around 3 years my daily token consumption has increased 50x. And this
doesn't even
count the 'embedded' AI use I'm using in other products and not seeing (eg. Google AI overviews, or various other AI integrations, which are currently of questionable utility in a lot of cases).
This requires enormous amounts of compute
All these tokens need to be processed on a GPU or TPU to run it through the model. As such we're witnessing currently one of the largest rollouts of infrastructure in human history, with datacentres popping up to service this huge (and growing) demand.
Keep in mind also that the number of people using LLMs has exploded in step - most stats show around 1 billion active LLM users at the time of writing. While most of these won't be using the millions of tokens like me and many other software engineers, as the technical complexity of building and running agentic workflows drop I'm sure they'll start consuming more and more tokens individually.
This has led to huge increases in capex, especially from the hyperscalers of AWS, Azure and GCP. I would add that the hyperscalers were
already
spending many tens of billions of dollars each on capex before AI to service non-LLM workflows.
Over the past 6 months this has reached fever pitch, at one point with it seeming that every
day
another $10bn+ infrastructure deal was done by one of the companies involved.
This then caused an (understandable) amount of questioning from the media and financial analysts, asking exactly how this enormous capex bill could be spent, especially pointing out some of the strange looking circular financing deals. It's important to note that asset based lending from vendors is
very
common in capex heavy industry (Ford famously makes more money from asset financing than building cars), but it's certainly unprecedented at this level.
Where the narrative breaks down
So we've established that token consumption per user is exploding, and equally the number of users is also growing extremely rapidly, and there's $100bns of "committed" capex to build out the infrastructure to support this.
Where I think this starts diverging is the actual
ability
to deploy that capital. It's one thing proposing $500bn of infrastructure spending in the oval office, quite another to turn that into the physical infrastructure, power it and get it online and supporting the enormous token demand.
The first obvious constraint is electrical power - most countries already have a significant lack of grid capacity. That's certainly a major factor, but has been somewhat mitigated in the short term at least by these datacentres deploying behind the meter (not grid) gas turbines. Especially in major gas producing regions like Texas there is (was) considerable spare gas pipeline capacity, even if there wasn't high voltage transmission availability. This has led to a subsequent shortage of gas turbine gensets, but that's a story for another day.
The bigger issue in my opinion is much harder to work around - RAM. If you've been in the market for a new computer, you may have noticed the breathtaking increases in computer memory prices. OpenAI is rumoured to have bought 40% of the entire world's DRAM supply. We're starting to see the supply chains buckle under the demand - and a lot of the DRAM supply is locked up in long term supply contracts, so once they start rolling over in the coming months and years you'll likely see far more consumer impact.
But what really grabbed my attention is this note from Macquarie pointing out the current supply of DRAM will only support the rollout of 15GW of AI infrastructure.
This places a really hard constraint on how much capacity can be built. Regardless if the AI companies/hyperscalers buy from Nvidia, AMD or like in Google's case, build their own TPUs with Broadcom - they all require HBM DRAM memory to go into the finished product.
And even worse, it's very difficult to ramp DRAM capacity quickly. Building new fabs for high end DRAM takes years - and it's likely a lot of the equipment
they
need to build is in very short supply, with a shortage of lithography equipment. High end DRAM (like HBM3 and the upcoming HBM4) requires EUV equipment which only one Dutch company makes.
Running some napkin maths on this, 7.5GW is roughly the power consumption of 2 million GB200s chips, which might deliver something on the order of 500M tok/s combined on frontier models (this part gets difficult to estimate accurately with speculative decoding, batch efficiency and ratio of prefill to inference).
This would "only" support the growth of ~30m "hardcore" agentic users using a million tokens a day for a year (assuming 7.5GW deployment in 2026 and another 7.5GW deployment in 2027, to get the 15GW the research note points out).
Given that models and use cases are appearing all the time (and will continue to), I think globally that is very likely to be breached. Keep in mind this is assuming all the compute is going to agentic inference - we also have hugely compute hungry video, audio and 'world' models that will be competing for that too, plus training runs and other LLM workflows.
Even worse, prompt caching (which makes a lot of agentic workflows economically viable) is extremely RAM intensive. The memory crunch hits exactly the use case of the highest demand the hardest.
What's likely to happen
Simple economics would tell us if demand rises and supply doesn't keep pace, prices will increase. In a
previous blog post
I estimated that current AI usage actually
is
very profitable (on a pure hardware/infrastructure level). AWS did push out a significant price increase recently -
raising the price
of their GPU rental by 15%.
Having said that, there is still enormous pressure to maintain market share from the various frontier labs. I can't see that changing and I strongly suspect that they'll be significant resistance to raise prices substantially - the barrier of switching between providers is quite low.
What I do think is going to happen more and more is far more dynamic inference pricing, with 'off peak' times being
significantly
cheaper than when demand is at its highest through the day. I can also see free plans becoming far less generous than they currently are while they try and build up capacity in the background.
I'm sure this is already driving model efficiency research - a small percentage increase in tok/s throughput on hardware can drive enormous commercial value. And I wonder if a lot of the time that's currently being spent making
better
models and harnesses switches to
more efficient
models as we go through to 2027, until DRAM capacity ramps.
There's a couple of wildcards too - maybe we will see frontier labs reserving entire
models
for their own usage rather than giving them out to end customers to build upon. For example, Google reserving a future Gemini model
just
for their own products like agentic Gmail or AI overviews.
Or someone comes up with a better memory architecture - totally sidestepping these constraints. There will be unbelievable commercial value in coming up with this - and I think Nvidia's recent $20bn
acquisition
non exclusive inference licensing deal
with Groq really points in this direction (Groq's memory architecture doesn't use HBM DRAM - it uses SRAM - but diving into this is an article for another day).
Regardless, I am not seeing the risk that we
overbuild
AI capacity right now. Regardless of the deals done and non-binding trillion dollar commitments signed, the DRAM shortage is likely to define the industry in the next few years.
