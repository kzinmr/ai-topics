---
title: "Reading today's open-closed performance gap"
url: "https://substack.com/app-link/post?publication_id=48206&post_id=194321302&utm_source=post-email-title&utm_campaign=email-post-title&isFreemail=true&r=2flx6&token=eyJ1c2VyX2lkIjo0MDg3NDgyLCJwb3N0X2lkIjoxOTQzMjEzMDIsImlhdCI6MTc3NjcwOTYzNSwiZXhwIjoxNzc5MzAxNjM1LCJpc3MiOiJwdWItNDgyMDYiLCJzdWIiOiJwb3N0LXJlYWN0aW9uIn0.4YTHN3eAeWvZljXBi2YGZthHtKtxGb-9PNyQNjtEipc"
fetched_at: 2026-04-20T18:27:24.614804+00:00
source_date: 2026-04-20
tags: [newsletter, auto-ingested]
---

# Reading today's open-closed performance gap

Source: https://substack.com/app-link/post?publication_id=48206&post_id=194321302&utm_source=post-email-title&utm_campaign=email-post-title&isFreemail=true&r=2flx6&token=eyJ1c2VyX2lkIjo0MDg3NDgyLCJwb3N0X2lkIjoxOTQzMjEzMDIsImlhdCI6MTc3NjcwOTYzNSwiZXhwIjoxNzc5MzAxNjM1LCJpc3MiOiJwdWItNDgyMDYiLCJzdWIiOiJwb3N0LXJlYWN0aW9uIn0.4YTHN3eAeWvZljXBi2YGZthHtKtxGb-9PNyQNjtEipc

It’s a clear, current equilibrium that open models will be in
perpetual catch-up of closed models
, but this gap being viewed as a single number, a “distance”, covers up a nuanced and crucial dynamic at what capabilities the models are covering. The most popular benchmark to comment on this gap is the
Artificial Analysis Intelligence Index
— a composite benchmark of ~10 sub-evals that they maintain over time to capture the “frontier” of current language model capabilities.
Particularly, I spend a lot of time understanding how dynamics that
feed into
that index are misunderstood by the natural tendency to reduce performance and trends to one number. Examples include:
How benchmarks evolve over time, becoming more or less correlated with how people actually use models,
How different models’ real-world performance relates to their benchmark rankings, and
How training regimes evolve over time to move said benchmarks.
Agentic benchmarks are in a decent place, but benchmarks are no longer as trusted as a correlate to real-world performance. A key example to this gray area is Gemini 3’s incredible benchmarks and remarkable irrelevance in where AI tools currently are being tested and deployed (agents). These trends point to obvious and lasting flaws in our measurements.
Share
At the root of this dynamic — the dance of correlating model real-world performance and benchmark scores — is the constant shift of the industry. As all the models, i.e. both open and closed, evolve over time, the topics of focus for benchmarking shifts about every 12 to 18 months. All of the domains of interest have very different training domains associated with them, especially in post-training. The longer a single paradigm goes on, the better the industry gets at measuring performance. In a new era of rapid post-training improvements, I’m at a relative minimum in my personal confidence in benchmarks.
Right after ChatGPT the focus was a mix of chat, math, and simple code. Instruction tuning and RLHF dominated. Chat capabilities saturated and faded quickly, then mathematics became less focal. Through 2025 and to today, especially once reasoning models became the default, the focus shifted to more complex coding and other simpler agentic tasks. We’re at the tail end of this first era. Recent training recipes are all dominated by reinforcement learning with verifiable rewards (RLVR), but the domains it is applied in have shifted dramatically from basic question-answer checking to complex environments.
What we’re seeing is that the closed, frontier labs are investing astounding sums of money in mastering these current foci — i.e. code, terminal tasks, etc. — while starting to push into more diverse knowledge work tasks. These newer tasks encompass specialized domains, such as accounting, law, healthcare, etc. They are still agentic, but require more expertise and often integrations with existing software or domain-specific tools.
We have very limited evidence on the true balance of capabilities of these newer domains, but these are the areas I’m focusing on when I say open models will struggle to keep up. The problem is that evaluating
complex
language model workflows is also a challenging research problem in itself.
The tasks are getting harder and the data needed to hillclimb on them is getting more private (relative to code, which has swaths of code on GitHub). Leading open model labs are helped by dynamics happening in the data industry that are economically similar to building chip fabs. The few, leading labs in the U.S. pay astronomical sums to buy new environments and datasets, then the fast-following labs (often in China), buy these later at a steep discount.
This is a key missed point — that the levers non-frontier labs pull to keep up constantly shift over time. A focus on distillation as the key lever to Chinese models’ progress reflects a blind-spot to the importance of RL environments to current training regimes. If an environment can be built either as a single evaluation in the Artificial Analysis Index, or to mirror it, currently the Chinese labs will be able to keep up.
The question worth dwelling on is: How crucial is the current set of tasks (again, coding and terminal tasks), where the likes of OpenAI and Anthropic have a massive business-adoption advantage over leading open weight models (and even Google alike), is crucial to maintaining revenue numbers? In order to maintain these record growth numbers and trajectories, there needs to keep being a meaningful edge in performance. Many companies would love to reduce their token expenditure cost if they can swap in a far cheaper, open model equivalent.
If agentic coding abilities saturate and the “frontier” of AI performance moves elsewhere, a large amount of the enterprise revenue could be reliant on well-formed customer relationships, inertia, and better product development, rather than the models being leaps and bounds better.
This precarious position is what I describe as the frontier labs needing to constantly reinvent themselves, and the field’s prospects, for monetizing the vast buildout of AI infrastructure. I still tend to fall on the side that the buildout will be worth it, and Anthropic and OpenAI will be astronomically profitable businesses, so I take this as a faith of a mix of them continuing to unlock compelling, new, valuable use-cases for the models, and that the benchmarks the open models are closing in on as
not being a complete signal
.
I operate with a sort of presumption where the leading open models from China are focused
slightly
more on benchmarks than the leading closed labs in the U.S. They’re incentivized to do so — they want to present the image as constantly being on the heels of the best closed models. Saying the Chinese labs are only in this narrative because they’re overfitting to benchmarks would be incredibly naive and incorrect. They’re genuinely strong models, and these dynamics of overselling and real innovation are a fine balance.
There are a few out-of-distribution benchmarks where open-weight models are very far behind, such as
WeirdML
or
ARC AGI 2
, but there are countless random benchmarks that show these open models as being unexpectedly strong. When you use the models, you can pick up on this lack of robustness (e.g. in long-context capabilities, and needing to reset your agent context more often than Claude/Codex), but they’re not a category error in the sense that they’re fundamentally different classes of models. They’re far closer than many would’ve expected.
