---
title: "LLMs are eroding my software engineering career and I don't know what to do"
url: "https://human-in-the-loop.bearblog.dev/llms-are-eroding-my-software-engineering-career-and-i-dont-know-what-to-do/"
source_type: blog
date: 2026-06-07
fetched: 2026-06-08T11:08:39.464240
topic: LLM impact on software careers
content_length: 26711
extracted_text_length: 11079
http_status: 200
---

# LLMs are eroding my software engineering career and I don't know what to do

**Source:** https://human-in-the-loop.bearblog.dev/llms-are-eroding-my-software-engineering-career-and-i-dont-know-what-to-do/
**Fetched:** 2026-06-08T11:08:39.464249
**Content Length:** 26711 bytes

## Extracted Text

LLMs are eroding my software engineering career and I don&#x27;t know what to do | the human in the loop 
 
- 
 
 

 
 

 
 
 
 

 
 
 
 
 
 
 

 
 
 
 
 
 

 

 
- 
 
- 

 
 

 
 
 
 
 
 
 
- 
 

 
 

 
 
 
 
 

## 
 the human in the loop
 

## 
 
 
 

 Home Blog 

 
 
 
 

 

 
 

## LLMs are eroding my software engineering career and I don&#x27;t know what to do

## 

 

 
 
 06 Jun, 2026
 
 
 

 

 

I'm a software engineer, completing 10 years of professional experience this year. I started my career as a web frontend engineer (it was easier for me to debug frontend code back then, so I chose that path), but shortly transitioned to (web) backend and never looked back.

Through a series of coincidences, once I stepped into backend development, I ended up working in software development roles in the domains of finance, bookkeeping and payment processing, where I had great autonomy and a close and candid relationship with Product Managers and stakeholders.

I learnt a lot about the domain and how to effectively write programs for it: PCI compliance, double-entry ledgers, escrows, reconciliation, payment lifecycles, bank transfer idempotency, etc.

It was, then, obvious that I should focus my career on becoming an expert on that domain to stand out as a professional and differentiate myself in a field that showed signs of an increasing need for domain specialists.

## The first pillar to erode: domain-specific knowledge

## 

 

Last year, I got hired by a company in the finance workspace. So far, I had worked on companies that do have a strong payment and finance component to their operations/offerings, but that were not solely finance-focused companies.

That company also embraced AI wholeheartedly, so I got ChatGPT and Claude Enterprise accounts from day one and was encouraged to use them for my research, exploration, and even coding, albeit with a warning that I should still review and own every single line that made it into production.

One of my first projects involved reworking the legacy online payment system, which was a mess. They hired me for (among other things) my previous experience in building that and trusted me with the task.

Different from the other companies I had worked for so far, they wanted the "Design Docs" I write before coding to be readable by both engineers and product managers - so they shouldn't be a technical deep dive and more of an architectural view. I wrote my first one with minimal AI assistance - I even called LLMs "stochastic parrots" at the time, a view I no longer hold - and delivered it.

I valued my knowledge and thought no LLMs could replace it.

Then my manager reached out to me: even though you're delivering code at a good pace, you're taking too long to deliver those Design Docs. Are you using AI? You should use more AI.

"No way this will work", I thought in my head, but agreed. The models at that time were not as good as the ones we have now, but they did provide a good speed-up on my writing and even the decision-making.

And then I started realizing: all the knowledge I have accumulated over the years: the trade-offs between implementations, how acquiring works, how to structure idempotency to prevent double-charges, everything, was becoming useless. Even though the models still needed some steering, they could connect the dots on how to structure such systems, which was the hardest part that only develops in your brain after years of hands-on experience. That was my first shock .

But sure, I thought, they can do that because there's plenty of articles on the web on how that shit works along with all the technical documentation, and we have blog posts explaining how to apply the technical tools to the domain. For humans, it may take a long time to learn all that, but that's training data so the models can pick it up.

What the models will never be good at, and that's where humans will shine, is debugging! I had accumulated a good experience debugging race conditions and distributed systems in production. That was my ticket to long-term employability.

## The second pillar to erode: debugging and distributed systems

## 

 

So, after LLMs started getting good at writing docs and helping plan the actual implementations, they became good at coding. It started in the second half of 2025 with the Claude Code hype, then Codex came and so on. Although I was using LLMs for writing unit tests every day before that, I wasn't trusting them to write the full implementation yet.

The natural next step was to introduce more AI into writing code. And honestly, I liked it. I like shipping things to production and seeing users happy as much as I like coding, so I was trading one thing that I like for another one that I also like, it was fair.

LLMs were becoming good at coding, but it still couldn't debug the mess left behind (by then or by the humans), so I still had a role that was bigger than steering the robot - a ticket to employability.

Everything seemed fine.

Then came the MCPs, the agentic workflows and Claude 4.5 and the sky started to fall.

Claude 4.5, to be honest, wasn't that good. It solved like 60% of the bugs given a stack trace and some context (a Sentry link with Sentry MCP enabled was all it took in most cases). Sometimes it gave a solution that sounded plausible but was totally wrong.

This time, however, I stopped doubting the machines. I saw bugs that in the past would easily take 1 day of full-time debugging being one-shotted by Claude Code. Of course, not all of them yet , but the pattern was clear.

Then came 4.6, 4.7, GPT 5.5, Opus 4.8 and the DataDog MCP... Now I have CLIs that one-shots bugs across distributed systems for me. Bugs that I couldn't solve in the past. Bugs that would take 2 days of full-time debugging. Bugs across distributed systems that lack distributed observability. 90% of the bugs are one-shotted now, including bizarre race conditions, unexpected corner-cases, third-party integration issues, undocumented API edge cases, everything. I hardly have to intervene.

Of course, I'm still employable because someone has to review the code and steer the robot. But I'm just another off-the-shelf engineer now. I have no domain expertise that another Sr. engineer steering an LLM cannot match. All my finance and payment domain expertise, all the debugging intuition and distributed system knowledge earned through hours of sweat and tears, is now promptable .

We were taught that generalists and specialists will always have their roles. But now the market is shaping everyone into becoming a generalist. That's not a bad thing per se , until you look under the economics of supply and demand: if everyone is a generalist, the price of a generalist falls if there's no demand to match. And we all know the demand is drying up.

## The third pillar, the one that hasn't eroded yet: code quality and architecture

## 

 

I still have one pillar standing, though: code quality and software architecture - what's now being reduced to being called "taste" 1 .

Along the course of my career, I always liked to refactor, always prized good code, and negotiated time in the sprint for it. DDD, Hexagonal, Clean Architecture, you know all the buzzwords. I like this topic, I like to discuss the trade-offs and different ideas on how to shape codebases. I really like it.

This is the last pillar standing. Except that nobody cares anymore.

Agents do a really bad job at keeping codebases organized. If you don't steer them, they'll hit a circular dependency issue sooner than you think. Will duplicate code. Add unnecessary comments. Mix up pure functions and side-effects. Disregard the principles of SOLID.

That should keep humans employed, except that this skill is now being reduced to the word "taste". But it's not just a renaming, the industry is moving to a world where code organization is less important.

Sure, humans should steer the agent to prevent spaghetti codebases with circular dependency graphs. We don't want F -rated codebases that are impossible to touch without breaking something. But a C or D ? It's now fine. Nobody needs A or B -grade codebases anymore because they're being made for LLMs, not for humans to read.

I don't want to argue if this is inherently good or bad. If the source code is now written for machines to read and not humans, it may be actually ok to target them.

But that's another pillar of my expertise that's eroding. A good chunk of the knowledge I accumulated on that topic is not that valuable anymore. All the time I spent on it - reading books, doing real-world exercises, discussing with other engineers, writing ADRs - is becoming useless.

## What now?

## 

I'm still employed and I see myself employed (at least in that company) for a foreseeable future. But I don't know what to think about the long-term.

I spent 10 years (even more when you account for non-profession experience) getting good at things that are becoming less and less valuable. My last pillar of expertise is now reduced to a "taste" and will probably won't last long.

And I know that's not just me. About 8 months ago there was a layoff at my current company (not related to AI, according to them). Some brilliant ex-coworkers were laid off and are still looking for jobs. Most of them suffer from the same problem I outlined here: their domain expertise is not enough to stand out anymore.

The company is now hiring again for a few roles and domain familiarity is not a strong differentiator anymore. We used to list "Software Engineer - Area". Now it's just "Software Engineer" and the team assignment comes after the offer is accepted.

Of course, this is good for brilliant engineers that never had the chance to get deep into the domain and now have better chances at getting a job, but it's also sad to think that other brilliant engineers that spent their lives collecting domain knowledge are now competing on the same lane.

The only way out for keeping my employability in the long-term now seems to be shifting my domain expertise to something LLMs will not get good at so easily. But what's left?

I thought about going back to college, learning Math, Statistics, advanced Machine Learning and applying for research role at a frontier lab. Except that there are no frontier labs in my country, the few ones that exist are flooding with applications and I have family matters that makes moving to another country difficult. By the time I can afford to make that jump, RSI may have made researchers obsolete.

Maybe I should consider transforming my woodworking hobby into a profession...

 

 Update (Jun 7) : this post went viral. I wrote another post replying to some comments from social media and expanding some of my arguments. You can read it here .

 
 
 
 

- 

See this , this and this for reference. Don't take this as an endorsement of the content inside any of these posts. &#8617; 

- 
 
 

 

 
 
 

 
 #ai 
 
 #llm 
 
 #software engineering 
 
 

 

 
 
 
 
 

 
 
 

 

 
 &nbsp; 
 
 
 

 

 
 
 
 

 
 
 
 
 
 Powered by Bear ʕ•ᴥ•ʔ
