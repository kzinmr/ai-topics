---
title: "How I think about reducing AI costs"
url: "https://martinalderson.com/posts/how-i-think-about-reducing-ai-costs/?utm_source=rss&utm_medium=rss&utm_campaign=feed"
fetched_at: 2026-08-17T10:30:54.473118+00:00
source: "martinalderson.com"
tags: [blog, raw]
---

# How I think about reducing AI costs

Source: https://martinalderson.com/posts/how-i-think-about-reducing-ai-costs/?utm_source=rss&utm_medium=rss&utm_campaign=feed

AI inference costs are something I've been
writing
about
for
a
while
. It's clear that for many companies this is becoming a huge problem:
AI spend per employee per month. Source:
Ramp AI Index
via a16z, 12 August 2026.
I've heard from a lot of readers that reducing this cost is becoming a hot topic internally.
So, here's
how
I think about this problem at a high level.
Audit costs
You
need
to have a good handle on what is driving your bill. I've met a lot of companies who have a pretty fragmented understanding of the costs - they can be siloed over many different teams, business units and roles.
At a minimum, you need to know - business-wide - how much you are spending on AI
and
importantly, key stats on how that breaks down. There are two main dimensions on this.
Firstly, the model in use. I see
a lot
of people running ancient, poor value for money models. The tech debt is real here! For example, GPT-4o is $2.50/$10 per million tokens, but is
drastically
worse than GPT-5.6 Luna, which is 10% of the cost. It's
really
important to know what models you are using.
GPT-5.6 Luna scores over 4x higher than GPT-4o on the
Artificial Analysis
intelligence index, and costs a tenth as much.
The second dimension is how your spend breaks down by the three main components of token costs - cached input, uncached input and output. As I wrote
recently
, with agents the distribution of these costs is rarely what you'd expect.
Keep in mind you need to collect this data for
all
your usage. This includes LLM usage via API or similar, coding agents and any other autonomous/business agents you have running. A key mistake I see is people focussing on their API spend, but not looking at their enormous coding agent spend for their dev team, which is out of control, or vice versa.
Low hanging fruit
Once you've got this done, the next thing is to look for obvious cost savings. As I mentioned before, it's usually quite easy to swap out legacy models with something cheaper
from the same provider
- though it should involve a verification stage, because you can risk regressions this way. It can result in a lot of the 'hacks' you've perhaps used for a less intelligent model backfiring.
The other key thing to look for is models that are 'overpowered' for the use case you are working on.
I often see teams using the 'largest' models for use cases where a much smaller and cheaper model would do. This is not as intuitive as it looks, and takes quite a lot of experience to realise what
can
and
can't
be switched out intelligence-wise. But certainly if you have large bills coming from certain workflows, it's definitely worth experimenting with them.
Move providers
The more "drastic" option is to switch away from OpenAI/Anthropic/Google models to a different provider that can host open weights models for you.
Whether this is worth it really depends on your spend. If it's a fairly minimal level of spend, it may not be worth the procurement and data privacy reviews your company may have. But for most, this is often where the meat of the savings comes from. It's also important to say you don't need to move
everything
off at once. I've seen some token-hungry workflows that account for a huge proportion of spend - these can be moved off while you keep everything else with the frontier labs, reducing the amount of upfront work dramatically while maximising savings.
There are a
lot
of companies based in the US (and Europe!) offering hosted open weights models at attractive prices, and they can offer high-quality SLAs and meet data residency requirements. Expect to have to break the myth internally that DeepSeek (for example) is "based in China". While
their own
API is, many providers offer that same model in your jurisdiction.
While the models move too fast to keep the article up to date, there's more on my
token cost optimization
page if you want to get in touch and get some thoughts on which open weights models and providers may be best for your use case.
Agent/LLM optimisation
The final lever for optimising your spend is going much deeper into what each of your workflows is actually doing.
This is a more involved process and I'd recommend starting with your ten highest cost workflows and seeing if you can identify issues. While this can be extremely nuanced, I'll list some common failure modes below so you can see if these map to yours.
Firstly, a problem I see a lot is putting
far
too much into the prompt. For example, including pages and pages of documents that may or may not be relevant to the user's prompt. With tool use these days it's often far more token efficient to give the LLM a tool it can use to
search
for relevant documents, rather than putting hundreds of pages of documents in the prompt just in case.
Ironically, the second issue I see over and over again is incredibly poorly optimised tools
themselves
. These can be either internal or third-party, but often MCPs return tens of thousands of characters of JSON back to the agent. This absolutely burns through tokens and a few small tweaks to your tool definitions can really help.
Intuit's official
QuickBooks Online MCP server
is a good example, and it's worth saying it isn't sloppy work - the code is careful, the tests are real, and the security thinking is better than most repos I read. It's a token disaster anyway.
It ships 142 tools. Serialised, that's roughly 21,000 tokens of tool definitions going up on
every
request, before the user has typed anything at all.
Search results come back as raw dumps.
search_invoices
hands back every field of every invoice it finds, straight from the QuickBooks API, with no filtering and no summarising. Ask a broad question and you can pull an entire ledger into context verbatim.
And
get_invoice_pdf
returns the PDF base64-encoded as text. A 100KB invoice becomes something like 33,000 tokens of noise that the model can't read and can't compress. That one call could cost you more than the rest of the conversation put together.
The other category of issues is around tool
failures
which then drive up agentic token spend as the agent has to try and retry them or work around them. This requires good monitoring. This can be
incredibly
expensive for longer running agents, especially tool call failures towards the end of a run (where cache read costs start exploding).
There are
many
other weird and wonderful ways teams manage to use LLMs inefficiently, but hopefully this gives you a good overview of the main ones I see.
It's a fast moving space
The final issue is that as AI is developing so quickly, you have to keep up with best practice. Best practice from even a year ago can often be actively harmful now. And with the plethora of models coming out, you need to stay on top of model trends as well.
I'd recommend teams schedule at least a quarterly review of their token spend and how the model/agent landscape has changed and what mitigations can be applied.
Finally, I do have some slots for companies that want to bring my experience in, and I help show them how to do this. The recent results I've got are extremely positive, reducing one company's token bill by over 50% in three weeks. If you'd like to
reach out
, I'd be happy to do a deep dive into your token spend.
