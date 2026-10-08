---
title: "Hill climbing to glory: using evals to improve AI error rate by 7x"
source: "Hex Technologies Blog"
url: "https://hex.tech/blog/we-used-evals-to-improve-ai-feature/"
scraped: "2026-10-08T06:00:41.098071+00:00"
lastmod: "2026-10-08"
type: "sitemap"
---

# Hill climbing to glory: using evals to improve AI error rate by 7x

**Source**: [https://hex.tech/blog/we-used-evals-to-improve-ai-feature/](https://hex.tech/blog/we-used-evals-to-improve-ai-feature/)

Skip to main content
📊
AI analytics use case:
how LangChain migrated from legacy BI and enabled 100% of their team to self-serve data
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
how LangChain migrated from legacy BI and enabled 100% of their team to self-serve data
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
how LangChain migrated from legacy BI and enabled 100% of their team to self-serve data
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
how LangChain migrated from legacy BI and enabled 100% of their team to self-serve data
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
how LangChain migrated from legacy BI and enabled 100% of their team to self-serve data
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
how LangChain migrated from legacy BI and enabled 100% of their team to self-serve data
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
Hill-climbing to glory: using evals to cut AI errors 7x
How 1,800 evals showed us AI feature quality improvements go beyond prompting
David Wilson
Engineering
October 8, 2026
Share:
twitter
linkedin
In this article
Start from the product experience
Write evals from real usage, then extend
The harness mattered more than the prompt
Make sure improvements are real
Fast evals mean faster product iteration
Product experience should drive your evals
Get started for free
Hex's Generative Apps let you build fully custom data apps by chatting with the Hex agent. Last week we launched
Quick Edits
, which uses a small model to let you restyle charts 20X faster and cheaper than with the full agent.
We've
used evals
to build AI features at Hex for a while. They're the only reliable way to tell whether a change actually made a feature better when the model's output is non-deterministic. We took a different approach with Quick Edits: we used evals to drive its development from the beginning, not just as a QA step at the end.
Initially, we wrote a few hundred eval cases, and went on to create 1,800 total cases as the feature evolved. Coding agents then tested hundreds of changes against those evals and kept only the ones that scored higher. That process, called hill-climbing, took our wrong-edit rate from 21% to 3%. Surprisingly, most of the gains came from the harness around the model, not the prompt.
If you're interested in taking a similar approach, Anthropic's
guide to eval design and hill-climbing
is a good starting point. Here's what worked for us beyond what they shared:
Start from the product experience
How the feature works
Quick edits use a small model (GPT-6 Luna/Claude Haiku 4.5) to read a user's request – "make the Enterprise line green" – and propose edits to chart properties in one shot.
If the user's request is too complicated – "why didn't the numbers go up??? make them go up!" – it hands off to the Hex agent, which can make more complex changes to the app.
Our evals focused on making sure the small model gets these edits and handoffs right.
Picking the right metric to optimize
There are two ways our feature, and therefore our evals, can fail:
Wrong edit: making an edit the user didn’t ask for.
Incorrect handoff: handing a request to the Hex agent that the small model should have been able to handle.
It’s tempting to want to minimize both kinds of failures, and maximize overall pass rate. But for this feature, it was much more important for us to minimize incorrect edits than incorrect handoffs.
A wrong edit would change the user's chart in a way they didn't ask for, which is jarring and erodes trust. A wrong handoff just results in the main agent making the right edit slower, which is less bad.
For example, we adopted GPT-6 Luna even though its overall pass rate was about 1 percentage point lower than GPT-5.6 Luna’s, because it made 20% fewer wrong edits at half the cost.
When we began hill climbing, our “wrong edit” rate was 21%, by the end, it was 3%. In real-world usage for our customers we expect the wrong edit rate to be much, much lower than that – we intentionally made our evals as challenging as possible.
Write evals from real usage, then extend
Rich eval cases
We built a suite of more than 1,800 eval cases, starting with a few hundred drawn from real chart-edit requests from internal users. We wanted examples of the kinds of edits people ask for, and the specific words (and languages) they use.
We extended those core cases to cover all the different types of chart edits (and hand-offs) we wanted to handle.
I read and gave feedback on the first 150-ish synthesized cases, which was enough for LLMs to do a great job synthesizing the rest.
I had GPT-6 Astra generate new cases and used Claude Fable 5.1 to fill in any gaps. Using multiple models gives us confidence the examples are diverse and comprehensive.
We made sure that many of the test cases are difficult and ambiguous, which gave us more runway to hill-climb against. We wanted to test whether the model could tell which requests it should handle and which it should hand off. A few examples:
“make it pop” → hand off (nobody knows what this means, including the model)
“make it weekly” / “hazlo semanal” → hand off (that’s a data change dressed up as a style change)
“hide the legend and only show 2025” → hand off, even though half of it is doable (partial edits are worse than no edit)
“make all the lines gray except Canada, hide the legend and make the lines thicker” → apply all three (and don’t touch Canada’s color)
“format the y axis as dollars” on a horizontal bar chart → hand off (because the Y-axis is the category axis there)
Handling fixtures
Each eval case includes the "user request" and a "fixture" – context about the chart that we send to the model along with the user request.
For this feature, fixtures represent the starting state of a chart in JSON, including previous edits, to handle prompts like "no, I liked the old color better".
Fixtures like these can be surprisingly complex and detailed, and are harder to make. We used ~50 base charts, with many variants and edit histories, once again inspired by real usage and extended by Astra/Fable.
The harness mattered more than the prompt
Validator > prompt
The validator is code that checks and cleans up the model's output before we use it to edit the chart.
For example, the model might return the right hex color but leave out the quotation marks our code expects. We were rejecting those responses even though the model had understood the request. We changed the validator to accept them.
Surprisingly, more than 50% of our hill-climb improvements came from expanding the validator to handle more almost-right outputs, such as:
Fixing small formatting mistakes, like missing quotation marks, or values returned in the wrong type
Rounding numbers to the nearest allowed values
The validator also enforces rules the model might get wrong: min below max, ISO dates, whether a property can actually take effect on this chart…
Validator improvements increased pass rates by 7 percentage points on Luna and 10 on Haiku. They cut Haiku’s hard errors (outputs our code couldn’t accept) by 99%!
An unintuitive lesson we learned was that prompt changes weren’t nearly as impactful as we expected they would be. The
vast
majority of pure prompt tweaks failed our evals. In fact, we ended up taking things
out
of the prompt and putting them into the validator, or into the chart property descriptions and labels the model reads.
The model regularly confused the axes on horizontal charts, for example. Adding “(x axis)” to the relevant property labels and improving their descriptions helped it choose the right setting. We hadn’t been able to fix that with prompt changes.
Handling different models
We evaluated both Luna and Haiku to make sure any tweaks work well with multiple models across multiple providers, ensuring this feature worked across our customer base no matter their model setup.
For example, we initially had a "no change" option for the model to say the chart already matched the request. Luna handled it well, but Haiku overused it, with 30X more wrong "no change" responses than correct ones. This is another example of behavior we couldn’t fix with prompting; we removed the option and pushed that logic into the validator instead.
Make sure improvements are real
"Holdout" cases to avoid overfitting
In our experience, it’s critical to keep a meaningful number of eval cases hidden from the agent doing the hill climbing so that it doesn’t overfit (over-optimize for your evals). Without these holdouts, it’s like a student memorizing the answers to a practice test. They might ace the test, but struggle when the questions change.
Our holdout cases were almost 40% of the eval suite. We only accepted proposed changes when the holdout results improved.
Tuning noise and attempts
You also need to consider what it will take to ensure quality eval data. In our case, we found that running only 3 attempts per case was too noisy. Re-running the same suite differed by approximately 8 wrong edits. 10 attempts per case was the sweet spot for us, bringing holdout noise down to 0.2 percentage points.
It's worth asking the agent to rerun the same
eval set
a few times to see how much results vary before changing anything.
Fast evals mean faster product iteration
Even at 18,000 attempts per full run (1,800 × 10), a run costs less than $10 on Luna and takes a few minutes at high concurrency.
That meant the evals weren’t just a final step. We ran them after every change to every part of the feature: the prompt, the validator, the chart properties, the handoff rules, the UX.
We changed the charts’ underlying properties three times in ten days while the hill-climb was running. Each time, we reran the suite and could immediately see if anything had broken or needed improvement.
It worked in the other direction too. When the model kept getting something wrong, the fix was often not in the prompt. We renamed a property, added a description, or changed a handoff rule, then reran to check it helped.
We iterated on the AI and the rest of the feature at the same time, against the same evals.
Product experience should drive your evals
We rooted our eval cases, fixtures, metrics to hill-climb, and everything else in the ways we see people using Hex today, and the product experience we wanted to enable for them.
So if you're building evals, my overall advice is to think carefully about that product experience and design your evals from there.
(Also, feel free to copy this post and paste it into your agent, so it can make use of what we learned, too.)
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
✨
🔊
🎧
🌊
🍀
🤠
🎷
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
Conversational analytics
Context Studio
Data apps
Hex CLI
Business intelligence
Exploratory analysis
Embedded analytics
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
Request a demo
Technical support
Contact us
LinkedIn
X (Twitter)
YouTube
©
2026
Hex Technologies Inc.
Privacy policy
Terms & conditions
Modern slavery statement
You have opted out of data tracking
