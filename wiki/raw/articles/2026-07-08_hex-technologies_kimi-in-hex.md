---
title: "Kimi K2.7 in Hex: Opus-level Analytics at a Fraction of the Cost"
source: "Hex Technologies Blog"
url: "https://hex.tech/blog/kimi-in-hex/"
scraped: "2026-07-08T06:00:55.384749+00:00"
lastmod: "2026-07-08"
type: "sitemap"
---

# Kimi K2.7 in Hex: Opus-level Analytics at a Fraction of the Cost

**Source**: [https://hex.tech/blog/kimi-in-hex/](https://hex.tech/blog/kimi-in-hex/)

Skip to main content
📊
AI analytics use case:
how Mercor unlocked $100M in revenue
🤯
Generative data apps:
Gorgeous, interactive dashboards and apps you can build with just a prompt
📖
State of Data Teams 2026
discover key insights from data leaders
🙏
It's just "Hex"!
Not "HEX" or "Hex dot tech"
📊
AI analytics use case:
how Mercor unlocked $100M in revenue
🤯
Generative data apps:
Gorgeous, interactive dashboards and apps you can build with just a prompt
📖
State of Data Teams 2026
discover key insights from data leaders
🙏
It's just "Hex"!
Not "HEX" or "Hex dot tech"
📊
AI analytics use case:
how Mercor unlocked $100M in revenue
🤯
Generative data apps:
Gorgeous, interactive dashboards and apps you can build with just a prompt
📖
State of Data Teams 2026
discover key insights from data leaders
🙏
It's just "Hex"!
Not "HEX" or "Hex dot tech"
📊
AI analytics use case:
how Mercor unlocked $100M in revenue
🤯
Generative data apps:
Gorgeous, interactive dashboards and apps you can build with just a prompt
📖
State of Data Teams 2026
discover key insights from data leaders
🙏
It's just "Hex"!
Not "HEX" or "Hex dot tech"
📊
AI analytics use case:
how Mercor unlocked $100M in revenue
🤯
Generative data apps:
Gorgeous, interactive dashboards and apps you can build with just a prompt
📖
State of Data Teams 2026
discover key insights from data leaders
🙏
It's just "Hex"!
Not "HEX" or "Hex dot tech"
📊
AI analytics use case:
how Mercor unlocked $100M in revenue
🤯
Generative data apps:
Gorgeous, interactive dashboards and apps you can build with just a prompt
📖
State of Data Teams 2026
discover key insights from data leaders
🙏
It's just "Hex"!
Not "HEX" or "Hex dot tech"
Blog
Kimi K2.7 in Hex: Opus-level analytics at a fraction of the cost
Open models have finally caught up to their closed counterparts
Matt Redmond
Data teams
July 8, 2026
Share:
twitter
linkedin
In this article
Why now?
The open-weights tradeoff
The high cost of cheap tokens?
Evaluation results and discussion
No free lunch
What’s next
Get started for free
Kimi K2.7 takes more turns than Opus. It second-guesses itself, re-checks its own work, and usually finishes slower. So why does it cost less to answer the same questions — and get more of the hard ones right?
Today we’re excited to announce that Kimi K2.7 is available in Hex, hosted on US-based infrastructure! We believe this model performs at an intelligence level comparable to Opus 4.7, despite consuming 2.2x fewer credits on average.
We find Kimi is empirically most effective on easier, non-visual questions. Reach for it on semantic-layer questions, BI questions, or any analytically hard work. Stick to Opus+ or GPT-5 class models for now on large, complicated visual understanding tasks.
Kimi K2.7 is just the first piece of a deliberate, long-term bet we're making on open-weight models in general. We've been waiting for this inflection point for a long time, and have some really cool things coming soon!
Why now?
Data analytics has proven to be a weirdly difficult domain for agents. For the last year or so, whenever we've tested a Cool New Model in Hex that's not the latest big-lab frontier hotness, we've been disappointed. Overthinking, misunderstanding intent, unnecessary churning tool calls, poor instruction following, and other generally bad analytical behaviors were rife.
Even models that performed competitively on public coding and math benchmarks were inadequate on our
internal analytical benchmark
. The messy context and vague, almost-but-not-quite verifiable tasks endemic to data workflows seem to be a perfect storm for LLMs — and particularly seem to throw smaller "benchmaxxed" reasoning models into paroxysms of overthinking, a failure mode exhibited not just by open-weight models but also by recent generations of Claude Sonnet.
Open weight models are now good!
An open model can be as cheap and fast as it wants, but speed means nothing if it confidently hands you the wrong number when you ask how many
turboencabulating
widgets you made in Q3 last year. We feel that with Kimi K2.7, we finally have an open model that’s on par with Opus and GPT-5.5 at data tasks.
The open-weights tradeoff
But why open models?
Large language models in agent harnesses can be compared on three attributes: price per task, time per task, and success rate per task. These attributes directly map onto the concepts “economic efficiency”, “system speed”, and “model intelligence”.
There is no free lunch in this space - only tradeoffs. Would you buy a 20% speedup for 80% more cost? Would you sacrifice 5% model intelligence for answers that arrive 50% sooner?
Anthropic and OpenAI offer a few guided choices in this tradeoff space— Fable is an “expensive, slow, but very smart” model intended for your hardest tasks, Haiku is the “cheap, quick, but less intelligent” model intended for easier ones. Sonnet and Opus exist in between.
Open-weight models make available a completely new region of this tradeoff space. With our initial release of Kimi K2.7, you can choose lower credit usage at the expense of an increase in total end-to-end latency, without much of an intelligence haircut.
And this is just for starters! Because we host this model ourselves, we can keep experimenting with new ways to configure these tradeoffs - this is the foundational promise of open-weight models. We could potentially offer a significantly faster Kimi at an increased cost, or a radically cheaper “batch” mode for slower async tasks. We chose Kimi for the native multimodality, but as other open models like GLM-5.2 approach the frontier, we can explore those too.
The high cost of cheap tokens?
It's tempting to reason about cost through the lens of model input/output token pricing, but in the agentic multi-turn world, that lens is too reductive. A brilliant model with "expensive" tokens can sometimes (often!) end up cheaper
per task
than a bargain-bin model with "cheap" tokens, simply because the smarter model is clever enough to get in, answer the question, and get out with fewer tokens and turns. We see this constantly.
This paradox poses a problem for our open model initiative: our goal is to give you another point in the tradeoff space that’s competitive with the frontier labs, but “cheaper per token” isn’t sufficient. The model has to be smart enough to do the whole
task
cheaply - being cheaper per token doesn’t matter if you ramble.
And boy, can they ramble. We’ve watched cheaper models fumble their way through our harness, racking up expensive trajectories despite the ostensibly friendlier sticker prices on tokens. The most encouraging thing we can say here is that the gap is closing fast: as open-weight models get better, both their per-token pricing and total token usage have trended down, making them a more competitive option empirically in our testing. We’re also co-evolving our harness with models over time, making the affordances more in-distribution with how the models want to use them.
We haven’t fully mitigated the rambling— Kimi K2.7 will sometimes yap more than Opus 4.7 - but it’s a lot better than previous large open-weight models, and we believe it’s crossed the threshold into “useful for most day-to-day analytics work” without being TOO annoyingly verbose. Most importantly, the per-token economics are sufficiently strong such that most tasks end up cheaper
despite
incurring more token usage.
Evaluation results and discussion
Across our evals, some patterns emerge: Kimi is slower to finish tasks end-to-end, using more tokens and turns than Opus. However, due to favorable per-token economics, the price-per-task ends up substantially better in all domains except visualization, where it’s only slightly better.
The
semantically modeled questions
evaluation set contains tasks that a good semantic model can basically answer on its own - the bread-and-butter BI questions like “how many customers do we have”. Here, Kimi and Opus do effectively the same. In fact, this set is effectively saturated now, and we’ll be retiring it soon. This is one of the strengths of Kimi - quick, straightforward questions that you expect to be well modeled in your ecosystem will be inexpensive.
The
semantically unmodeled questions
evaluation set contains tasks which cannot be answered by semantic models. It measures the agent’s ability to “go off road” and explore the data warehouse directly. Opus is decisively better than Kimi at this task, winning by eight percentage points.
The
core visualization
evaluation set measures how well the agent creates and interprets charts. This is the least favorable price comparison for Kimi - verifying data visually seems to be a difficult thing to do efficiently, so the turn count is larger. We’re working on better harness support here, but for now this is the one domain where Kimi’s economic efficiency is least impressive compared to Opus.
The
analytically hard
evaluation set measures how well the agent is able to answer questions where the core complexity is in the
analysis
- even when context retrieval is easy. On this eval set, Kimi scores
better
than Opus, but takes about twice as long in the median case. This is due to an interesting emergent qualitative behavior: Kimi is a capital-W Worrier. K2.7 spends extra turns in validation and verification, second-guessing its own assumptions and re-checking its hypotheses. This pays off in correctness - it gets more questions right than Opus - but it also takes quite a bit longer.
The
contextually hard
evaluation set measures how well the agent is able to answer questions when the analysis path is straightforward, but identifying the appropriate resources and context is difficult. On this set, Kimi performs about the same as Opus.
Overall, Opus tasks take about 0.65x as long as Kimi tasks, but cost 2.22x as much.
No free lunch
K2.7 has a smaller context window than most frontier models. We serve a 256k token context window for K2.7, but Anthropic and OpenAI’s models have a 1M token context window. This means that threads will automatically compact more frequently on K2.7 than they would on a closed weight model, which means that some details from your working session may be compressed or forgotten earlier than they would otherwise.
As mentioned, we also observed that while the
average economic case
is better with K2.7, there are still agent trajectories where K2.7 exhibits substantially longer reasoning behavior and incurs more agent turns than the closed weight models do. This appears in the long tail of the distributions - “most” Kimi agent runs are more efficient, but the rare ones that are worse are often quite a bit worse.
What’s next
We're excited to bring open-weight models to the Hex ecosystem, and Kimi K2.7 is the first experimental step rather than the finish line - it’s unlocking deeper nodes on the tech tree for us. As always, we'll keep claims grounded in the data - when something gets faster, cheaper, or smarter, we'll show you the numbers.
Share:
twitter
linkedin
This is something we think a lot about at Hex, where we're creating a platform that makes it easy to build and share interactive data products which can help teams be more impactful.
If this is is interesting, click below to get started, or to check out opportunities to join our team.
✨
Get started for free
👩‍💻
Open roles
Made with
🍩
☕
🥟
🍺
🍰
🔮
🔒
🥖
🍷
🛌
💜
🥨
🛹
🍤
🧄
🍞
🥥
⛳
🤞
🔊
🎧
on
🌎
.
Company
About
Careers
Customers
Solutions
Media kit
Newsroom
Platform
AI and agents
Agentic notebooks
Conversational self-serve
Context Studio
Hex CLI
Exploratory analysis
Embedded analytics
Data apps
Integrations
Changelog
Resources
Pricing
Switching to Hex
Enterprise
Docs
Blog
Events
Templates
Compare
Trust Center
Status
Connect
Contact sales
Request a demo
Technical support
LinkedIn
X (Twitter)
YouTube
©
2026
Hex Technologies Inc.
Privacy policy
Terms & conditions
Modern slavery statement
