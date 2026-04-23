---
title: "Shopify’s AI Phase Transition: 2026 Usage Explosion, Unlimited Opus-4.6 Token Budget, Tangle, Tangent, SimGym - with Mikhail Parakhin, Shopify CTO"
url: "https://substack.com/app-link/post?publication_id=1084089&post_id=195067855&utm_source=podcast-email&play_audio=true&r=2flx6&utm_campaign=email-play-on-substack&token=eyJ1c2VyX2lkIjo0MDg3NDgyLCJwb3N0X2lkIjoxOTUwNjc4NTUsImlhdCI6MTc3Njg4NjQ5NSwiZXhwIjoxNzc5NDc4NDk1LCJpc3MiOiJwdWItMTA4NDA4OSIsInN1YiI6InBvc3QtcmVhY3Rpb24ifQ.RmFfx40qQnsPe18qeOnIIhcvpnZ97IxWVI8aCtykLjE&utm_source=substack&utm_medium=email&utm_content=play_card_show_title#play"
fetched_at: 2026-04-23T05:08:14.188931+00:00
source_date: 2026-04-22
tags: [newsletter, auto-ingested]
---

# Shopify’s AI Phase Transition: 2026 Usage Explosion, Unlimited Opus-4.6 Token Budget, Tangle, Tangent, SimGym - with Mikhail Parakhin, Shopify CTO

Source: https://substack.com/app-link/post?publication_id=1084089&post_id=195067855&utm_source=podcast-email&play_audio=true&r=2flx6&utm_campaign=email-play-on-substack&token=eyJ1c2VyX2lkIjo0MDg3NDgyLCJwb3N0X2lkIjoxOTUwNjc4NTUsImlhdCI6MTc3Njg4NjQ5NSwiZXhwIjoxNzc5NDc4NDk1LCJpc3MiOiJwdWItMTA4NDA4OSIsInN1YiI6InBvc3QtcmVhY3Rpb24ifQ.RmFfx40qQnsPe18qeOnIIhcvpnZ97IxWVI8aCtykLjE&utm_source=substack&utm_medium=email&utm_content=play_card_show_title#play

Early bird discounts for
the San Francisco World’s Fair
, the biggest AIE gathering of the year, end today - prices will go up by ~$500 tonight so do please lock in ASAP!
From near-universal AI tool adoption inside Shopify to internal systems for ML experimentation, auto-research, customer simulation, and ultra-low-latency search, Mikhail Parakhin joins us for a deep dive into what it actually looks like when
a 20-year-old, $200B software company goes all-in on AI
. We cover why Shopify has become much more vocal about its internal stack, what changed after the
December model-quality inflection
, and why the
real bottleneck in AI coding is no longer generation
, but review, CI/CD, and deployment stability.
We also go inside
Tangle
,
Tangent
,
SimGym
,
which are three major AI initiatives that Shopify is doing to make experimentation reproducible, optimization automatic, customer behavior simulatable, and search and catalog intelligence faster and cheaper at scale. Along the way, Mikhail explains
UCP
,
Liquid AI
, and why
token budgets
are directionally right but often measured badly, why AI-written code can still increase bugs in production, what makes Shopify’s customer simulation defensible, and what he learned from the
Sydney era at Bing
.
We discuss:
Mikhail’s path from running a major Microsoft business unit spanning Windows, Edge, Bing, and ads to becoming CTO of Shopify
Why Shopify is talking more publicly about AI now, and why staying at the frontier has become necessary for the company
Shopify’s internal AI adoption curve, the December inflection, and why CLI-style tools are rising faster than traditional IDE-based tools
Why Jensen Huang is directionally right on token budgets, but raw token count is still the wrong way to evaluate engineering output
Why the real unlock is not more agents in parallel, but better critique loops, stronger models, and spending more on review than generation
Why AI coding can still lead to more bugs in production even if models write cleaner code on average than humans
Why Shopify built its own PR review flow, and why Mikhail thinks most off-the-shelf review tools miss the point
How PR volume, test failures, and deployment rollback are becoming the real bottlenecks in the agent era
Why Git, pull requests, and CI/CD may need a new metaphor once code is written at machine speed
What Tangle is, and how Shopify uses it to make ML and data workflows reproducible, collaborative, and production-ready from the start
Why Tangle is different from Airflow, and why content-addressed caching creates network effects across teams
What Tangent is, and how Shopify is using auto-research loops to optimize search, themes, prompt compression, storage, and more
Why Tangent is becoming a democratizing tool for PMs and domain experts, not just ML engineers
Why AutoML finally feels real in the LLM era, and where auto-research still falls short today
Why Tangle, Tangent, and SimGym become much more powerful when combined into one system
What SimGym is, why simulated customers only work if you have real historical behavior, and why Shopify’s data gives it a moat
How SimGym evolved from comparing A/B variants to telling merchants what to change on a single live storefront to raise conversions
Why customer simulation is so expensive, from multimodal models to browser farms to serving and distillation costs
How Shopify models merchant and buyer trajectories, runs counterfactuals, and thinks about interventions like discounts, campaigns, and notifications
Why category-level behavior is so different across commerce, and why ideas like Chinese Restaurant Processes are showing up again in practice
Shopify’s new UCP and catalog work, including runtime product search, bulk lookups, and identity linking
Why Shopify is using Liquid AI, and why Mikhail sees it as the first genuinely competitive non-transformer architecture he has used in practice
Where Liquid already works inside Shopify today, from low-latency query understanding to large-scale catalog and Sidekick Pulse workloads
Whether Liquid could become frontier-scale with enough compute, and why Shopify remains pragmatic and merit-based about model choice
Who Shopify is hiring right now across ML, data science, and distributed databases
The Sydney story at Bing, why its personality was not an accident, and what Mikhail learned from deliberately shaping AI character early on
Mikhail Parakhin
00:00:00 Introduction: Mikhail Parakhin, Microsoft, and Shopify
00:01:16 Why Shopify Is Talking More About AI
00:02:29 Internal AI Adoption at Shopify and the December Inflection
00:06:54 Token Budgets, Jensen Huang, and Why Usage Metrics Can Mislead
00:10:55 Why Shopify Built Its Own AI PR Review System
00:12:38 AI Coding, More Bugs, and the Real Deployment Bottleneck
00:14:11 Why Git, PRs, and CI/CD May Need to Change for Agents
00:18:24 Tangle: Shopify’s Reproducible ML and Data Workflow Engine
00:21:19 Why Tangle Is Different from Airflow
00:26:14 Tangent: Auto Research for Optimization and Experimentation
00:30:07 How Tangent Democratizes Experimentation Beyond ML Engineers
00:33:06 The Limits of Auto Research
00:36:36 Why Tangle, Tangent, and SimGym Compound Together
00:37:20 SimGym: Simulating Customers with Shopify’s Historical Data
00:42:47 The Infra Behind SimGym
00:46:00 Why SimGym Gets Better with Real Customer History
00:47:30 Counterfactuals, HSTU, and Modeling Merchant Trajectories
00:51:55 CRPs, Clustering, and Category-Level Customer Behavior
00:53:30 UCP, Shopify Catalog, and Identity Linking
00:55:07 Liquid AI: Why Shopify Uses Non-Transformer Models
00:59:13 Real Shopify Use Cases for Liquid
01:03:00 Can Liquid Scale into a Frontier Model?
01:09:49 Hiring at Shopify: ML, Data Science, and Databases
01:10:43 Sydney at Bing: Personality Shaping and AI Character
01:13:32 Closing Thoughts
[00:00:00]
swyx
: Okay. We’re here in the studio, a remote studio, with Mikhail Parakhin, CTO of Shopify. Welcome.
[00:00:08]
Mikhail Parakhin
: Thank you. Welcome.
[00:00:10]
swyx
: I don’t even know if I should introduce you as CTO of Shopify. I feel like you have many identities. Uh, you led sort of the, the Bing ML team, I guess, uh, uh, or ads team. I, I don’t know, I don’t know, uh, you know, it’s, uh, people va-variously refer you as like CEO or, or, uh, I don’t know what that, that, that said previous role at Microsoft was.
[00:00:29]
Mikhail Parakhin
: Uh, that was... Yeah, my previous role w- at Microsoft was the-- I actually was the CEO of one of Microsoft’s business units, which included, as I, you know, as we discussed, all the things that people like to laugh about, uh, including Windows and Edge and Bing and ads and everything.
[00:00:47]
swyx
: Yeah, yeah. What a, what a, what a wild time.
You’ve obviously, uh, done a lot since you landed at Shopify. Uh, one of the reasons I reached out was because you started promoting more sort of internal tooling, uh, primarily Tangle, but also a lot of people have seen and adopted Tobi’s QMD, uh, and obviously, I think, uh, Shopify has always been sort of leading in terms of, uh, engineering.
I think more-- it’s just more recent that you guys have been more vocal about your sort of AI adoption. Is that, is that true?
[00:01:16]
Mikhail Parakhin
: Well, I think AI tools in general are fairly recent development, uh, and we’ve-- Shopify, you know, at this stage of its development, we’re developing AI in-in-house and other, uh, building tools that use AI and, you know, interfacing with the wider AI community, uh, you know, are on the sort of the, uh, runaway trajectory.
So it just did by sort of natural byproduct. We, we talk about it more also. We just, uh, just even yesterday, Andrej Karpathy was famous in tweeting about, oh, are there some, uh, ways, uh, that, that you can organize your agents to store the data and then, uh, look up the data so that you don’t have to research or, or lose context every- Yes
time. And a little bit tongue in cheek, I tweeted that, “Hey, we’ve, we’ve done it much earlier, and we even have different approaches, Tobi and I.” Tobi, of course, is a big fan of QMD, and I’m more of a SQL, SQLite fan. But, uh, yeah, very similar things that we’ve already done here. The point is, yeah, we’re very dynamic, you know, explosively growing company, and we have to be at the forefront of AI adoption, obviously.
[00:02:29]
swyx
: Yeah. Yeah. Um, you, your team kindly prepared some slides actually that we were gonna bring up on to, uh, the screen. I think I can, I can screen share, and then we can kind of go through some of the shocking stats that maybe, maybe put some numbers to what exactly is going on. So here we have, uh- An internal AI tool adoption chart.
What are we looking at here? What ?
[00:02:54]
Mikhail Parakhin
: Yeah, this is very interesting statistics. Uh, this is number of daily active workers, you know, think of, uh, DAO, basically the active users of-
[00:03:05]
swyx
: Yeah ...
[00:03:05]
Mikhail Parakhin
: AI tool as a percentage of all the people in the company, right? And then- Yeah ... different AI tools. And, uh, you could see two things here is that one is the green is total.
Uh, green is just total. So you could see that it approaches really % by now. It’s hard not to do your job now without interacting deeply, at least with one tool. You could see another interesting thing is just as many people commented in December was the phase transition when suddenly models gotten good enough that, that everything took off and started growing.
Uh, it, it was many people noticed that the thing is that small improvements accumulated into this big change in Sep- December roughly timeframe.
[00:03:52]
swyx
: Yeah.
[00:03:52]
Mikhail Parakhin
: The other thing I would claim you could see is that, uh, CLI-based tools and tools that don’t require you to look at the code becoming more popular, and you could see, yeah, various versions of, uh, Cloud Code and Codex and Pi and internal development tools taking off.
Uh, exactly, yeah, uh, and blue is our River, just internal agent for coding, where tools, uh, that require IDEs such as, uh, GitHub, Copilot or Cursor, they’re not exactly shrinking, but they’re not growing as fast. Like, uh, red, red line is, is the IDE kind of tools. So you could see that they’re, they’re not experiencing as, as fast of a growth.
[00:04:37]
swyx
: As I understand it, basically, every employee has their choice, right? Of choose whatever tool you use, and then you’re just kind of doing a, a daily sur-survey or something.
[00:04:47]
Mikhail Parakhin
: Exactly. And, uh, we- Yeah ... the, the push is to get your job done, you can use any tool, and we effectively fund unlimited tokens for everybody.
Uh, we, we do, we do try to control the models that, uh, people use, but from the bottom, not from top. Like we basically say, “Hey, please don’t use anything less than Opus four point six.”
[00:05:09]
swyx
: Oh .
[00:05:10]
Mikhail Parakhin
: Some people, some people end up using GPT five point four extra high. Some people use Opus four point six. Um, uh, you know, uh, there are some, uh, there are plus and minuses in going for full one million context window versus not.
But, uh, we try to discourage people from using anything less than that.
[00:05:28]
swyx
: Yeah, yeah. Got it, got it. Uh, I mean, uh, that’s, you know... The, the next chart here, it really kind of shows the expansion and the sort of December twenty twenty-five inflection, right? That, uh, people are using a lot of tokens. I think it’s also really interesting that no one was kind of abusing it in twenty twenty-five.
Like it was- Had comparatively, uh, to this year, there was almost no growth. I mean, it’s still like, you know, probably, probably gave fifty percent.
[00:05:56]
Mikhail Parakhin
: Yeah. This is just a different scale. It’s still exponential- Yeah, yeah ...growth at just a different- ...rate of expansion. Uh, there was inflection point, and Sean, I would claim the, the super interesting part here is that you could see that the distribution becoming more and more skewed.
Yes. The top percentiles grow faster. So that means- Yeah ...the people in the top ten percentile, they, their consumption grows faster than seventy-five and so forth. So, uh, the distribution skews more and more towards the highest users, which is... I don’t know what it tells me. It’s like it feels not ideal, to be honest.
Or maybe it’s okay. We’ll see.
[00:06:36]
swyx
: Why does it feel not ideal? Is, is it because of, um, quantity over quality, or what’s the concern?
[00:06:42]
Mikhail Parakhin
: Because take it to the limit. That means, you know, if, if this rate of separation continued- Ah, yes ...a year, there will be one person consuming all the tokens. So it’s just, it’s kinda strange.
[00:06:54]
swyx
: Yeah, I mean, um, uh, I, I think internal like teaching and all that, uh, will, will help sort of distribute things more widely. But in, in the early days, of course, the people who are sort of more AI-pilled will obviously find more ways to use it than the people who are less AI-pilled. Maybe let’s, let’s call it that.
I’ll just, I’ll just kinda quickly, uh, pause from the, the... You know, we will go back to the rest of the slides, but I just wanna, um, review, you know, there are a lot of CTOs of, of large companies like yourself where they’re all considering some kind of token budget, right? Like I think it’s something, something that Jensen Huang has been talking about, where like if your 200K engineer is not using 100K of tokens every year, like they’re, they’re underutilizing coding agents.
Of course, Jensen Huang would say that, but like it seems a very quantity over quality approach and like some, some people are basically saying like, well, is this comparable to judging engineer quality by lines of code, right? Which we also know is like kind of flawed, but better than nothing. So I, I don’t know if you have like a sort of management take here on, on how to view this kind of, uh, metrics.
[00:08:02]
Mikhail Parakhin
: Well, I mean, you’re, you’re baiting me. I, I like... This is my favorite topic. Uh, if you let me, I’ll probably talk for two hours on just this. I have a lot of things to say. Like I do think Jensen gotten a lot of bad press saying, “Oh, of course you’re, you know, this, uh, the- ...the cake seller says you don’t need enough cakes.”
You know? Like, of course. Uh, but, uh, I actually, uh, think that’s undeserved. I think he, he’s actually right. Uh, I do think- He,
[00:08:33]
swyx
: he’s directionally correct.
[00:08:35]
Mikhail Parakhin
: Yeah. Yeah. He’s directionally correct for sure. Uh-
[00:08:37]
swyx
: Who knows what the right number is? Yeah.
[00:08:39]
Mikhail Parakhin
: The thing that I do Uh, want to say, and this is something that we learned through trial and error and very important is like two things.
One is that it’s not about just consuming tokens. Uh, you can consume tokens and, and in fact, the anti-pattern is running multiple agents, too many agents in parallel that don’t communicate with each other. That’s almost useless, uh, compared to just fewer agents and burns tokens very efficiently. Uh, setting up the right critique loop, especially with the high quality models, where one agent does something, the other one, ideally with a different model, critiques it, uh, suggests ways to improve it, the agent redoes it with this critique and, and so it takes much longer.
So people don’t like it because latency goes up. You know, they, they have to wait until this debate is happening. But, uh, the quality of the code is much higher. And another thing, just since you mentioned like, look, uh, uh, yeah, the overall budget is just like, uh, lines of codes. Lines of codes are exploding for everybody right now, or partially because AI is really mover balls, but partially just because AI can write a lot more code, you know, doesn’t get tired.
And so you have to have to have a very strong narrow waist during PR review. Otherwise, just the number of bugs will go through the roof. It’s, uh, it’s this unexpected consequence of the just volume trumping everything. I would claim by now good model writes code on average with fewer bugs than, than the average human.
But since they write so much more of it, like more of it will make it into production. So you have to- You still
[00:10:26]
swyx
: have
[00:10:26]
Mikhail Parakhin
: more bugs. Yeah. Have to have a very rigorous PR reviews, also automated of course. But, uh, yeah, that to spend a lot budget there. Like this, this for me, for me, actually, the important metric is the ratio of budget spent during code generation versus, uh, spent, uh, expensive tokens like GPT, uh, five point four Pro or, uh, uh, Deep Think from Gemini, you know, checking on PR reviews.
[00:10:55]
swyx
: Yeah, totally. Uh, I noticed in your chart you didn’t have any review tools. Do you just use like, like let’s say a Claude code to review tools? Or do you have another set of review tools like the Greptiles, the Code Rabbits, uh, Devin Reviews has a review tool. I don’t know if you’ve had those specialist review tools.
[00:11:13]
Mikhail Parakhin
: You are a little bit jumping on my store tool right now because the graphs I was only showing public tools. Uh, uh, the-- I haven’t found a good PR review tool that, that does what I think should be done. And, uh, partially my, my thinking is because it’s so... It just goes against both what people feel like emotionally they prefer and, uh, some of the, uh, you know, frankly Even business models that, that the companies run.
At peer review tool, uh, time, you want to run the largest models. That means, I don’t know, Codex or, or, uh, Cloud Code is not gonna cut it. You need to have pro-level models if you really want to, uh, stand the tide of bots from going into production. And you need us to spend a lot of time, the models taking turns, but you don’t want, like, a big swarm of, uh, of, uh, agents.
So in fact, you end up in a different dual-dualistic world where you generate not that many tokens. You, in fact, generate few tokens, but it takes f-a long time because these are expensive models taking turns rather than many, many agents trying to do many things in parallel. So that’s, that’s why I feel like I haven’t found good tools, so we are using our own for peer review for now.
[00:12:33]
swyx
: Yeah. Yeah. I mean, uh, I think a lot of companies are building their own, uh, especially to their needs, right?
[00:12:38]
Mikhail Parakhin
: Mm-hmm.
[00:12:38]
swyx
: Um, I, uh, you also have a chart here going back to the slides on, uh, PR merge growth, where we’re now at thirty percent, uh, month on month rather than ten percent. Uh, and also the, the estimated complexity is going up.
You know, this is productivity, right? ‘Cause y- presumably there’s more stuff going into the code base and more, more features getting worked on. I’m curious about the backlog, right? Like the, the, the-- I actually don’t mind a pro-level model taking an hour or two hours to review my PR, because I’ve dealt with humans who take a week to review my PR, right?
And I keep pinging them on Slack, “Hey, hey, review my PR.” So, you know, I think there’s some trade-off here where, like, it still doesn’t make sense.
[00:13:18]
Mikhail Parakhin
: Exactly. That, that’s exactly m-my point. Uh, that on one hand, you can tolerate longer latencies at, uh, PR. On the other hand, like right now, the real problem is not in spending time waiting for PR.
It’s real problem is since there’s so much more code than- Yeah ... uh, probability of at least some tests failing going up, and then you, like, keep de-failing, then you have to find the offending PR, evict it, retest it without that PR, and so deployment cycle becomes much longer. Uh, so it actually, in terms of the overall time to deploy, it’s total time savings if you spend more time on a longer model, like thinking for an hour, because then, then you, you don’t have to spend all that time during testing and rolling, you know, rolling back the deployment.
[00:14:03]
swyx
: Yeah, totally. That’s still worth it. You know, you don’t look at the individual, look at the aggregate, and look at the, the, the change in the aggregate system.
[00:14:11]
Mikhail Parakhin
: Exactly.
[00:14:11]
swyx
: I’m kind of curious if, like, there’s this PR mentality and, like, c-- the, the, the CICD paradigm will be changed eventually. Some people are like, obviously a lot of people want new GitHub, but I even wonder if, like, Git is the problem, right?
Like, is that the bottleneck? Is the concept of a PR a bottleneck? Do you guys use stack diffs? I don’t know if, uh, that’s a, like, a merge queue stack diff type of thing.
[00:14:34]
Mikhail Parakhin
: We, we use, we use Stacks, we u- we use Graphite. We worked with, uh, Graphite a lot. Uh, so we use Stack, uh, PRs. I think, uh, like that’s clearly the overall CICD in general, and the interaction with the code repository right now is the, clearly the sort of the, the main issue and the bottleneck for us, uh, and highest top of mind.
I would say we probably need a different metaphor or different whole design of how to process it in new agentic world. I haven’t seen anything dramatically better yet. I, I think everybody right now is just trying to keep their head above the water ‘cause, ‘cause there, there’s so many PRs and then everybody’s CICD pipelines start creaking, the, the times are increasing, the number of bugs slipping by increasing, and you have to, have to clap on down.
And so we are a little bit in this situation when we need to first stabilize that story and then start thinking, hey, what, what it could be a completely different and new world, which I haven’t... I know some people working on it. I haven’t seen something, like anything super compelling yet, but clearly the old thing were designed for humans will need to be morphed into something new.
[00:15:53]
swyx
: One of the thing that I, I think about is kind of like the merge conflict is basically a global mutex on the whole system, right? And in, in hu- in human organizations, we do have something like that. It’s the company standup. But like, other than that, it’s like it’s actually fitting for us to be somewhat decentralized, somewhat plugged into one stream of information source, but somewhat lossy.
Like it’s okay, you know, that, that not every delivery is like atomic consistency. Like we’re not dealing with a database sometimes.
[00:16:27]
Mikhail Parakhin
: This is a very good point, uh, because since humans don’t write code too fast, you know that global mutex is not too bad. Once you-
[00:16:36]
swyx
: Yes ...
[00:16:37]
Mikhail Parakhin
: start writing code at the speed of machine, it becomes the, you know, the bottleneck.
Then what do you do? Maybe, and I can’t believe I’m saying this because I, I’m long-- lifelong opponent of, uh, microservices, and I always thought that was, like, a really bad idea. And now that you’re saying it, like, maybe in new guys like microservices will make a comeback, you know, because then you, you can ship things independently in tiny things and, and the managing all that complexity automatically will be much easier.
I don’t know. Like, we’ll s-- we’ll have to see.
[00:17:10]
swyx
: Yeah. I mean, I don’t know what the Microsoft or, or Shopify thing is, but I, I read this paper from Google where they have a monorepo that deploys into microservices, right? And then, uh, the other concept that I think about a lot is the Chaos Monkey concept from, from Netflix.
Being able to create, like, this robust system where, um, uh, you know, you, you have the service discovery, you have the, uh, the independent, independent microservices discovery and, and, uh, you know, probably going to be a fair amount of duplication. That’s how an organic system sort of scales, uh, that, that you have that...
I don’t know how you call it. Slack? Robustness? Depend-- uh, d-duplication. I, I, I forget the-- I, I’m-- And this-- those-- these are not exactly the terms- Hmm ... I’m looking for, but I c-can’t really think of the words. Okay. I was gonna go into Tangent and Tangle. Uh, so, uh, we, we sort of discussed the overall stats that, uh, Shopify has.
Uh, but, you know, I, I think some, some pretty cool stuff that you guys are working on is your ML experimentation, uh, and your, your sort of auto tr-research training pipeline. Presumably you’re much closer to this one because it’s, it’s a sort of personal hobby of yours. How, how would you explain them in, together?
I thought we have a slide that, like, uh, has the s- the system diagram.
[00:18:24]
Mikhail Parakhin
: Yeah. Tangle first and then Tangent as a-
[00:18:27]
swyx
: Yeah ...
[00:18:28]
Mikhail Parakhin
: as a thing on top of Tangle. And, uh, Tangle is the third generation, I claim, of, uh, systems of, uh, running any data processing, but a bit with a skew for ML experiments, but not necessarily. Any sort of data processing tasks where you need to iterate, share, and you have scale so that you want maximum efficiency.
You know how, like, normally you would work, you would-- Imagine you’re a data scientist or an ML practitioner, you would get Jupiter notebooks or, or maybe you would get, uh, you know, Pyth- your Python scripts, and you would manage the data, and you produce those TSV files, and you put them in some JFS or something.
Then you would notice that, oh, it has this, uh, weird missing values. You go and write another script that, uh, goes and replaces them with, uh-
[00:19:20]
swyx
: Ah ...
[00:19:21]
Mikhail Parakhin
: dash S. And then, then you, then you run some, some, uh, “Oh, I need to filter bots.” And so you run some light GBM model that, uh, removes the bots. And then, then you like-- And then you, you kind of like get into shape, and then you start experimenting, and you run multiple experiments, and then you’re like, “Oh my God,” like, “this experiment is worse.”
You undo, and you cannot get to previous result. And like, “Ah, what did I do?” Like that. Again, then, then you finally like get everything working. Then you like start throwing it over the fence to production. You, you replicate it, those things don’t work, and then sometimes you like don’t notice that you forgot some feature naming and the, the features don’t match.
But then, like imagine you, you did everything, and then six months later you’re like, have to repeat it because now there’s more data, or you wanted to do another pass, and you’re like, “What, what did I do?” Or like, or like, “This script crashes now,” or the, “the path has changed.” And then, then you’re trying to, like you spend another month just doing ar- digital archeology on your own, you know, history, right?
Now multiply that by many, many teams. Now imagine you got an intern that you wanna ramp up. Now you have to show that intern, “Oh, you know, look, here’s the folder, there’s the scripts, you know, ask your cloud agent to do, and then, uh, to, to figure it out.” And then cloud agent does something, and then you’re, “Ah, yeah, right, right, it was the wrong folder.
I forgot to tell you, I actually have this other thing I forgot myself.” And, and that’s, that’s the, like, the daily life we all, uh, all know it, uh, if, if you’re a data scientist, machine practitioner, ma- machine learning practitioner or, uh, or even like any data managing, uh, person.
[00:21:00]
swyx
: Yeah. So I, I used to do this, uh, f- uh, on the quant finance side, uh, in, in my hedge fund.
So we did this before Airflow, and then, uh, obviously Airflow came along and, uh, then more recently Dagster, uh, I would say is like, in my mind, what I would use for that shape of problem, uh, where you had to materialize assets and create a pipeline.
[00:21:19]
Mikhail Parakhin
: And that’s, that’s very good segue because... So Airflow is great, but Airflow is more about you, you have something and you wanna repeatedly run it in production on schedule.
It’s less about you as a team developing things and being able to share, and you grabbing the standard pipeline and saying, “Hey, I wanna change this tiny little component in the huge sea of data processing, and I don’t wanna-- I wanna run ten experiments on this, and I wanna do hyperparameter optimization.”
All that is very hard to do with Airflow. It’s very easy to do with Tango. Tango is m- more about, it’s everything about group of people Running experiments, it might be agents too nowadays. Uh, running experiments cheaply, collaborating, sharing results. Uh, you don’t need to understand fully. You, you grab-- you clone somebody else’s experiment or somebody else’s pipeline, uh, run, uh, change small piece, run it, be, like, get it to production state, and then ship in one click.
So then the... You don’t have to port it into any other system to, to run in production. You can just run the same experiment. It’s, it’s fully production ready. And, and it’s, uh, it has lots of... Again, as I said, it’s third generation system. The original one was, I would claim there was Ether and then, uh, at least in my career, Ether was the first, first, uh, that pioneered this type of approach.
And then there was, uh, Nirvana, which, uh, uh, at Yandex, which did kind of sec-second take on this. And now this one aggregates the, the learnings from all of those and, and Airflow as well to, to get to the state where you try it, it, it feels kind of magical. Uh, ‘cause now everything is based on content, uh, hashes.
So even if the version changed, but if the output didn’t change, nothing is being rerun. It’s very efficient. If you... Multiple people start experiment that needs the same sort of data preprocessing, it’s not repeated multiple times. It’s automatically done only once. If you start ten experiments that all require, you know, some, some data preparation first as the first step, and you don’t have to coordinate for that.
Like, you don’t have to know that other people are starting it. You now, it’s very easy compos-, uh, composability, any language you can u- uh, you wanna use, and it’s very visual. So you can see immediately, you can edit it easily, you can assemble small things with just even mouse clicks if you want to, and, uh, share, clone.
And everybody knows also it’s fully kind of static in the sense that we rerun it second time, it will exactly have the same results. Like, you will never have to do digital archeology. So full versioning and everything is also there.
[00:24:06]
swyx
: Uh, so, so people can, uh... It’s open source. Go to the GitHub repo and, and, uh, check it out.
Uh, and it is also a really good, uh, blog post about it. I think all these is, like, really appealing. The, the, the, the thing that I think sells me the most about it is that, um, sort of development to production transition, right? Which I think, um, a lot of people haven’t really solved that, uh, strictly, right?
Like, we develop really, really well in, in Python notebooks, but then, you know, that’s obviously not a sort of production ready process. I think that, like, any way in which that is solved, I think is, is very appealing. Then the other thing that you mentioned, which also raised my eyebrows, was content-based caching, which you mentioned is, is, um, you know, is ve-very much, uh, um, a sort of efficiency measure about, uh, you know, just like recalculation only on, on sort of content addressing Which I think makes sense.
Uh, it surprised me that the savings could be this much, but maybe I just haven’t worked at your scale where there’s so much duplication, uh, that people just rerun because they change a single ID upstream.
[00:25:10]
Mikhail Parakhin
: It does, yeah. But it’s not only you rerun. The, the main savings are coming from the fact that you ran it, you got your job done, and you moved on.
Then- Yeah ... somebody else in some department you don’t know existed runs the same task, but on a newer version.
[00:25:27]
swyx
: Yeah.
[00:25:27]
Mikhail Parakhin
: Like right now, you can’t, in, in most of the organizations, you can’t even find out about it so that you can’t even measure that you’re spending that time twice, right? Here- Yeah ... if everybody’s on Tango, that’s detected automatically and detected that the output is the same.
And then for that person, all it looks like is like experiment just suddenly moved, jumped forward, right? Uh, uh- Yeah ... so that’s because, because the, there’s network effect of multiple people helping each other.
[00:25:51]
swyx
: Yeah. This is one of those things where it’s designed to be a platform from the beginning rather than an individual developer’s tool from the beginning, right?
And, and everything’s gonna streams down from there. That is the sort of Tango, uh, orchestrator, and it’s, it manages jobs. We’ve seen a few versions of this, and this is obviously, uh, uh, the sort of, uh, unique approaches that you guys have, have, uh, figured out. And then there’s Tangent.
[00:26:14]
Mikhail Parakhin
: Yeah. And Tangent is basically an automatic auto research loop that can help and kind of do your work for you.
Uh- ... you know, uh, effectively, effectively, Andrej Karpathy recently popularized it with auto research. Yes. Remember he said like he was, uh, speed running this, uh... Yeah, uh, you know the story. The, here we’re basically bringing the same capability into Tango so that, uh, the, uh, Tangent can analyze it. It’s just an agent that can run multiple experiments, figure out what can be changed, and keep on rerunning it, keep on modifying until, uh, maximizing some goal, some loss function, whatever you need to, to achieve.
And in general, I would say if you’re not using auto research-like approach in whatever you do, like literally whatever you do, then you’re missing out. We saw at Shopify that taking like a wildfire, anything where you can put measurements can be done dramatically better. Our-
[00:27:19]
swyx
: Mm-hmm ...
[00:27:20]
Mikhail Parakhin
: uh, speed of, uh, templatization HTML, uh, completely new UX tem- uh, templatization of, uh, reducing latency for liquid themes.
Uh, we-- Our, uh, search, uh, recently we moved from It’s hard even, uh, quote from eight hundred QPS to forty-two hundred QPS with the same quality just by pure optimizations and not a research loop that kept running and changing code in our index serve on the same number of machines, just increasing the throughput.
We, we managed to improve the quality of gisting and machine learning process. Uh, you know, gisting is the prompt compression technique that
[00:27:59]
swyx
: allows for
[00:28:00]
Mikhail Parakhin
: lower latency and, and lower and, uh, actually higher quality slightly. So like literally whatever different walks of life, and it doesn’t have to be AI related.
Uh, we, we had a reduction in, uh, storage because the agents would go and find data sets that clearly are derivative, uh, and then you don’t need to store things twice. You know, we, we, we found somewhat embarrassingly that it was one of the largest tables was hashing random IDs into another random ID, and we literally- Oof
put only one. So it was translating, yeah, two random IDs hashed
[00:28:36]
swyx
: into
[00:28:37]
Mikhail Parakhin
: each. So, so
[00:28:37]
swyx
: it has access to the code as well, so it can, it can check the, like what, what the hell is it doing?
[00:28:42]
Mikhail Parakhin
: So there, there cou- it could be run in two levels. You, uh, you know, at the superficial level, it could just use ex-existing components and, uh, reshuffle them.
Uh, you know, like you can grab- Yeah ... uh, XGBoost, and you can grab some, some Py- PyTorch module, and then can grab some, you know, grab another tools and, and combine them. At a deeper level, since Tangle is all sort of CLI based underneath you, every, every component is a wrapped really CLI, uh, call and a YAML file, it can analyze code and create new components and, and, uh, keep on iterating as well.
So, so you can, you can both have quick modifications of existing t- uh, pipelines with the, with components that are already there pre-baked, or you can create new components, uh, and-
[00:29:29]
swyx
: Yeah ...
[00:29:29]
Mikhail Parakhin
: keep iterating on those. So auto research is, again, this is probably the, the thing I was excited the most in the last two months happening, and we see it taking like, like totally like a wildfire.
Just, uh, everybody, every day, every... well, every day, every minute, I would, uh, have somebody Slack message saying, “Oh, look how much better I made it.” And, uh, it’s all throughout the research.
[00:29:53]
swyx
: Is this democratized in some way in, in the sense that like is it your ML, uh, engineers and researchers doing this, or is it your regular PMs and software engineers also have the ability to auto-- to use Tangent?
[00:30:07]
Mikhail Parakhin
: This is an awesome question. Like, Tango in general and Tangent in particular are extremely democratizing. Like they- Yeah ... they are the main tools for- ‘Cause I don’t
[00:30:15]
swyx
: need the details.
[00:30:16]
Mikhail Parakhin
: Yeah. Exactly. Initially used by ML and AI engineers, but then literally, as you said, PMs are like the highest user right now is one of PMs on our org, uh, Sartak and he was, he was number one by, by usage of, of this ‘cause they’re just, uh, energetic and knowledgeable, and now it, it unlocks a lot of capability where you don’t have to co-change code manually.
[00:30:39]
swyx
: I mean, I mean, because it kind of cuts out the ML, ML engineer from the process because the, the, the PMs have the domain knowledge and the ability to think about, uh, from first principles about, okay, what, what results do I want? And they can-- they even have the access to the data that, that needs to go in.
So it’s like in some ways, like this is the magic black box that we’ve always wanted for, for training and, and for, uh, I guess, uh, uh, hill climbing, whatever.
[00:31:04]
Mikhail Parakhin
: It’s basically cloud code for your AI development- ... uh, situation, right? Like now, now you don’t have to know exactly how algorithms work. You can just, uh, bring your domain knowledge and expertise and product knowledge and iterate within Tangent until you’ve gotten the results that you need.
[00:31:21]
swyx
: In my previous roles, every time that someone has pitched AutoML, you know, I’ve always been like, “Uh, this is not, this is not gonna work. It’s, you know, it’s, it’s always gonna be a flop.” Somehow it’s working now. I mean, presumably the answer is now we have LLMs and it’s good enough, right? It’s, it’s an emergent property that we can do auto research, but like, it doesn’t feel that satisfying that how come we didn’t do this before, right?
Like we just did like parameter search and like, I don’t know. That’s maybe that’s it.
[00:31:48]
Mikhail Parakhin
: Yeah. Bayesian optimization and hyperparameter optimization was, was the one that, or facet of AutoML that was used very actively, which incidentally also built into, uh, Tango. But, you know, I know Patrice Simard very well, and, uh, he was such a, uh, such a proponent of AutoML, and he put, like literally spent careers trying to democratize it.
Without LLMs, it just turned out to be very hard. Like it, you, you would have flexibility within certain narrow domain, but it was hard to wider scale, and now with LLMs suddenly it’s like magic wand, and so suddenly everybody- ... is an AutoML expert.
[00:32:28]
swyx
: Yeah, I, I think it’s multiple things, right? Like I’m, I’m just gonna bring up the, the, the chart again, right?
Like LLMs can do the monitoring very well. That is the very potentially unbounded, super unstructured. It can do the analysis very well, it can do the... Uh, and basically it is much more intelligence poured into every single step. Uh, there’s maybe nothing structurally changed about AutoML, but this is just m-more intelligent and more unstructured.
[00:32:53]
Mikhail Parakhin
: Exactly.
[00:32:54]
swyx
: Any flaws that you’ve run into? Like everyone is like drinking the Kool-Aid, oh my God, time savings, uh, you know, performance improvements. Like what, what, uh, issues have you have, uh, come up?
[00:33:06]
Mikhail Parakhin
: This is really cool. It’s not a solution to all the world’s problems for sure. The limitations are usually the ones I-- And this is where we get into a bit of a subjective territory.
Uh, I can only share what I’ve, I’ve seen so far, and I’m sure the situation, uh, is changing, and, you know, maybe after I say it, like many people will reach out and say, “Hey, what about this?” And you don’t know that, and then, then we’ll be probably right. But what I’ve seen is auto research is very good at doing kind of obvious things that you don’t have bandwidth to do or you didn’t notice or maybe you’re not aware of like the-- some standard practices.
It is not good at doing something completely out of distribution, something that, you know, you have to think for, for multiple days, uh, and, and do something like none of this. So, so it’s, uh, I, uh, set an experiment once, uh, on, on my sort of, uh, hobby thing, and I let it run for, uh, ended up, uh, several weeks run, uh, you know, it’s like full production kind of scale, so it, you know, slow runs and, and it ex-- it performed in the end, uh, over four hundred experiments, and only one was successful.
I’m like, “Okay, that’s, that’s good.” But-
[00:34:18]
swyx
: But it saved time.
[00:34:19]
Mikhail Parakhin
: Yeah, I saved time. Like it, it was the, that thing. Yeah, if I, if I were doing four hundred experiments myself, my betting average, as I said, would have been much higher, I’m sure. But also, first of all, it would take me like three years to do four hundred experiments.
And, uh, I didn’t have to do them. Like the machines were just, uh, the price of electricity did that. So, and I got one improvement, uh, that in, uh, my, my-- Honestly, when I was starting that experiment, my thinking was to go and show that, “Hey, Andre, maybe you just don’t know how to optimize.” And I was super smart because in, in my pro-problem, it was optimized for many years, and it was like fully improved.
Uh, and I didn’t expect it, you know, auto research to find anything at all. Yet it did. So instead of making fun of Andre, I ended up, uh, a big, big supporter. Yeah, that’s exactly the tweet. Yes.
[00:35:10]
swyx
: You and Toby really, really go back and forth on-online a lot, which is really funny. Uh, think of it as, as an eval for the optimalness of the code it’s running on.
Uh, it’s almost like it reminds me of like a Kolmogorov complexity thing, but, uh, I guess it’s-- there’s some optimal thing that you’re trying to sort of reduce down to, I guess. Um, and so, so you, you, you know, you should congratulate yourself that you had, uh, you know, uh, ninety-nine percent, uh, optimality.
[00:35:36]
Mikhail Parakhin
: Exactly, yeah. I think Andre really deserves a lot of credit for popularizing this approach. This is, uh, this is incredibly, I think, powerful and cool and You know, the, uh, even him, him just mentioning it led to a lot of gains in a lot of places in the industry, so we should be thankful.
[00:35:56]
swyx
: Yeah. I think he also has a just...
I don’t know what it is. Like, um, you know, it, it is a simple self-contained project that people can take and apply to other things, which is, is, is one thing, but also just the name. Just like somehow no one, no one managed to call their thing auto research. It’s just naming things is very important. I think that that is mostly, uh, our coverage of Tango and, and, uh, Tangents.
I think obviously, you know, there’s a lot of, uh, ML infra at, at Shopify that people can, uh, dive into. We’re about to go into SimGym, but before I do that, any, any other sort of broader comments around this whole effort? Like where is it, where is it leading to?
[00:36:36]
Mikhail Parakhin
: As a segue to SimGym, like all those things start composing strongly.
And, uh, you could see a huge unlock when you can look at each one of the tools and, and you see, oh, they’re extremely useful. Uh, Tango is useful by itself. Auto Research is useful by itself. SimGym is useful by itself. If you combine all three, you create like synergetic effect. I think that’s why we wanted to even, uh, cover them today is because this is something that if you go back even, you know, five years ago, would’ve been unthinkable.
Uh, replicating that, uh, would, would be either incredibly costly or impossible, right? With probably thousands of people are required.
[00:37:20]
swyx
: Well, we have serverless human, uh, serverless intelligence, right? Like, uh, so yes, you do have thousands of hu-- of, of intelligences, not just, not humans. And that’s, that’s close enough, right?
Even if they’re not AGI, they’re, they’re close enough to do the, the task that you need them to do. And, and, you know, that’s, there’s plenty for, for a lot of routine work, knowledge work. Okay, let’s get into SimGym. Um, this is one of those things I, I was surprised to see actually it’s apparently your, uh, one of your most popular launches, and I think something that, uh, I think Sim AI, I think Yunjun Park, who did the Smallville thing, there’s a very small cottage industry of people trying to do like the simulate customer thing.
I think a lot of people maybe don’t super trust this yet because they’re like, well, obviously they would just do what you prompt them to do, right? But maybe just think, uh, tell us about the sort of inspiration or origin story.
[00:38:10]
Mikhail Parakhin
: That’s exactly actually the thing I wanted to cover, because if you don’t have the historical data, all you can do is prompt a-agents in a vacuum, and they will do exactly what you prompt them to do.
In fact, when I first proposed it, and this is a bit of, um, my brainchild initially, if I, I can boast, even Toby said like, “But wouldn’t they, they just repeat what, what you tell them?” And, uh, but I’m like, “Yes, except Shopify has decades of history of how people made changes and what there is, uh, there, what it resulted in terms of sales.”
So now what we can do is we can-- we have this... It’s not, it’s a noisy data. There’s a small, usually websites, uh, you know, like things, things are never in isolation. It’s almost never AB experiment. It’s always AA experiment when there’s has two meanings, but basically, you know, in different time you run two different things.
But if you aggregate in general, uh, like everything together, and you apply, uh, denoising and collaborative filtering like approach, you can extract a very clear signal. And then you can optimize your agents. And that’s why it took so long. It took almost a year of that optimization of just us sitting and fiddling, and, and we had this internal goals of correlation of hitting-- internal goal was to hit zero point seven correlation with, uh, add to cart events, for example.
Like that, that if we run real AB test experiment, that it should, it should go and, and rep-uh, replicate, uh, same sort of success that, that humans had or lack thereof. And it, it took forever, and I don’t think that’s easily replicatable because, uh, like who else would have that data? You have to have this historic, you know, decades, uh, worth of data.
And now, now the, like the other thing you need is in-infrastructure and the scale, right? Because, uh, w- again, what we found, uh, stat sig results, you need to run a lot of simulations, a lot of agents, and, and it’s-- Those are expensive things. Like you’re, you’re making actions in the browser because you want a real friction.
You want to, to be able to get the image like of what humans will see because you wanna, uh, detect effects like, “Hey, if I make my images larger, will I have more sales or l- uh, fewer sales?” And like usually people’s intuition here, by the way, is that I increase my images, I will have more because they look nicer.
You know, designers all look sparse and big images. Like usually your sales tank, right? But, but, uh, you know, from HTML, all the characters look the same only the, the size tag looks different, right? So it’s very hard. So you have to take visual information, you have to run this in simulated browser environment on the big farm and, and of course, you have to have, uh, like very, very expensive model, good model with multi-model model.
So all this it’s-- is what’s taken so long and, uh, to share my personal fail a little bit there, Sean, is like, you know, we always had this bias to-- for like large company bias. You know, we always, uh, whenever you-- we do, we’re like, “Hey, we’ll run an experiment,” right? We make, make a change, and we will run an experiment and then, uh, see, uh, see which one’s better or like, “No, this is worse,” and most of them are worse, so you discard it and keep iterating, hill climbing.
And we’re like, “Oh, like smaller merchants, they cannot get stat sig results. They cannot really run experiments simply because, you know, in a week there would be not enough data for them.” So we thought from this perspective. What we didn’t realize is that most people don’t have A and B, they just have one thing, and they need suggestions of What A and B should be.
So, uh, we first build this, hey, we run simulation on two separate teams and, and, uh, say, “Hey, which one is better?” We then morphed it into, and very recently just released it, when you have just your site, your theme, we run over it and we say, “Hey, here’s what predicted values of, of, uh, uh, conversions are, and here’s how we think you should modify it to increase your conversions.”
And then circling back to what you started with, the proof is in the pudding. Like, if we are not correlating with reality, like, people will not be using it. And, uh, thankfully, we see literally every day more users than the previous day. So, so right now, uh, right now- It’s working. Yeah. I’m-- Right now my problem is how to pay for it all because the so our major thing is how to optimize the LLMs, do distillation, how to run the headless browsers, uh, and handful browsers, uh, uh, cheaper so that we can accommodate the increase in traffic.
[00:42:47]
swyx
: Yeah. I, I understand that you, uh, you published a lot of technical detail at GTC, so I was just gonna bring it up a little bit. I think s- was this in, in con-conjunction with some kind of GTC presentation? Or something like that, right?
[00:42:59]
Mikhail Parakhin
: Well, we, yeah, we, we did it in several place, but yeah, we had the engineering- Yeah
blog, uh, as well. Yeah.
[00:43:05]
swyx
: Yeah. So you’re running, uh, GPT OSS. Uh,
[00:43:08]
Mikhail Parakhin
: the, this is an older version. You know, now we run multimodal model. But yeah- Yeah ... GPT OSS, we still run GPT OSS as well for
[00:43:15]
swyx
: And then you have the VMs, and you also have browser-based. I really like this one where it you said, “It violates almost every assumption that standard LLM serving is designed for.”
And then you had like, basically orders of magnitude differences between everything.
[00:43:29]
Mikhail Parakhin
: Exactly. Which is, which, uh, which was, you know, a bit of a challenge to implement, like when, like even simple things. Uh, be- since it violates all the assumptions, for example, multi-instance GPUs, like MIGs don’t work as well.
But we needed, uh, to get MIG to work because, ‘cause otherwise it’s way too expensive. And so we had to deal with the, yeah, with, uh, lots of infrastructure and, and, uh, work with, uh, uh, Fireworks and CentML, uh, you know, to help with optimizations and browser-based, as you mentioned. Yeah, like, takes a village.
[00:44:04]
swyx
: Okay. So there’s a lot of like, I guess, experimentation in the infrastructure so far, and you’ve published more or less what you have here. I guess I’m, I’m less familiar with CentML. I, I don’t do, uh, that much work in this, this part of the stack. But why was it the sort of preferred instance platform?
[00:44:22]
Mikhail Parakhin
: There are really three probably top companies. There used to be, uh, uh- Three top companies, uh, at least I was aware of that did, uh, LM optimization. You know, together Fireworks and Santa ML, not necessarily in that order. Santa ML recently got acquired by NVIDIA. Uh, what they did is if you have a model and you want to optimize it to a specific prof-- uh, profile of usage, uh, they would go and do it.
And, uh, we work with, with those companies, uh, this was work particularly in with Santa ML and NVIDIA to get them the best possible results out of it. And, and sometimes you, you have to retune depending on, like sometimes you want the maximum throughput, sometimes you want minimal latency, sometimes you want like the cheapest, right?
And, yeah, or some combination. And so yeah, these are people who would come and help you.
[00:45:14]
swyx
: I see. I see. Yeah, yeah. I’m familiar with these people for the LLM, you know, autoregressive stack. But the other interesting category of these optimizers is also the diffusion people, whereas like Fel and, you know, uh, Pruna recently has come up a lot as well, which I think is like really underappreciated, uh, at least by myself, because I, I thought, oh, all the workload would be LLMs, but actually there’s a lot of diffusion as well.
[00:45:38]
Mikhail Parakhin
: Exactly.
[00:45:38]
swyx
: There’s a lot here, so I, I, I... it’s, it’s, uh, it’s, it’s, it’s hard to cover. But I, I do think like people underappreciate the importance of customer simulation, basically. I think this is something that I’m candidly still getting to terms with. Uh, you know, uh, you also-- your team also like prepared this, like, really nice diagram.
Uh, I, I assume this is AI generated.
[00:46:00]
Mikhail Parakhin
: Yeah, it looks-
[00:46:01]
swyx
: Maybe it’s not.
[00:46:01]
Mikhail Parakhin
: Yeah, it looks, uh, Gemini-ish. Yeah, but, uh, uh, honestly, I, I don’t know where, where the hell they generated. It looks, look, uh, looks like it’s, uh, Google. But the interesting part, John, that, that, uh, we haven’t covered, but I, I wanted to mention is if your store had previous customers, rather than it’s a new store, you’re like new merchant just launching things, it helps tremendously in just correlation and forecast.
Yeah, we take your previous, uh, customer’s behavior, and we create agents that replicate those specific distribution of, of customers that you get, and then we a- we apply those to your changes, and then that, that raised raw, you know, the re-- uh, just correlation with the add to cart events or to-- with conversion or whatever it, it, it may be, uh, quite dramatically.
So, uh, replicating humans in general seems like an interesting, cool challenge.
[00:46:58]
swyx
: As a shareholder, I think this is the-- like if people are Shopify shareholders, they should really deeply understand this because this is basically the moat. The, the more you use Shopify, the more it will just automatically improve, right?
Like you’re, you’re doing the job for them.
[00:47:13]
Mikhail Parakhin
: Yeah, that’s what we started with. Like, uh- ... uh, otherwise, if you’re just a startup, I wouldn’t do it if, uh, you know, if it was my startup because Without the data, it, yeah, as, as you said, it’s, it’s exactly the case that, uh, whatever you say in prompt, that’s, that’s what the agents will be doing.
[00:47:30]
swyx
: The statistician in me wants to like really satisfy the sort of, um, statistical intuition, I guess. Um, to me it’s kind of, uh, the, the word that comes to mind is, um, ergodicity. Uh, so let’s say a, a customer takes this path, customer takes this path, customer takes this path, right? Um, the... In my mind, the way I explain it is like, okay, here, here’s the ninety-five percentile, here’s the five percentile, and here’s the median, right?
Um, but to me, what SimGym is potentially doing is that it can, uh, modify... It can sort of model the sort of in-between sort of journeys as well, that, that maybe are dependent on the previous states. This may be like a very RL-type conclusion where like basically the summary statistics, if you only did naive AB testing, you only have the, the statistics at, at, at a certain point, and you only judge based on the sort of overall summary statistics.
But here you can actually model trajectories. Does that make sense? Or-
[00:48:31]
Mikhail Parakhin
: That makes total sense because like, well, that, that makes even more sense that maybe even you realize bec- because-
[00:48:38]
swyx
: Okay. Please,
[00:48:38]
Mikhail Parakhin
: please. Yes ... we do-- Yeah. The, so internally, uh, we have this system, we talked about it briefly once at NeurIPS.
We have a huge HSTU-based system that models the whole companies, uh, and their possible paths. And like- Yeah ... what you are, what you are showing, like actually at any point of time, you can either model the user’s behavior or you mo- can also think about, uh, the whole merchant as a company, as the entity that acts in the world.
You can model that as well. And then you can do, can do counterfactuals. In your graph, like in your blue graph, uh, if you’re... Imagine in the center there, uh, somewhere in the middle, you would have an intervention. I give that person a coupon, or I don’t know, I send a personal thank you card, or give a discount in some- somewhere.
And then you can, uh, then you can do forward rollouts from that counterfactual. So what would have happened with that intervention or without the intervention? And you can even ch- change where that intervention, uh, in time can happen, right? Like some- where, where in this journey. So we, we do this at the Shopify scale for our merchants, and then if we notice that something that they can be fixing, like there’s a strong counterfactual, like we have Shopify policy, they basically get a notification like, “Hey, we think your...
something is wrong with your-” I don’t know, Canadian sales. Like, uh, it looks like it’s misconfigured. Here’s what you need to do. Or do you think like, uh, you have to set up this campaign with these parameters? And we do that at the buyer level to literally offer discounts or cashback or, or things to buyers.
So this is-- I’m getting very excited. Like this is my sort of area of, uh, interest, I guess, and, and hobby. But being able to m-model something complex as human beings or companies and model counterfactuals on it, where you can have interventions in the future and optimize when to make intervention, what kind inter-- uh, what kind of intervention to make.
It’s such an unlock that previously was completely impossible. Like the-- it was, it was always dreamed of, but never... Like how would you even simulate it without LLMs or HTUs? I think very, very exciting times.
[00:50:59]
swyx
: I just wanted to, uh, to maybe illustrate this. I, I’m not the best illustrator, but I, I am a conceptual statistics guy.
And y-you know, you cannot just do this. Like this is a dimensionality AB test doesn’t do, right? Like, uh, because it doesn’t have the, the, the change over time, uh, stochastic nature, uh, and it doesn’t have the sort of contextual like... Here’s all the context to this point. Um, okay, cool. Um, that’s SimGym.
You’re, you’re gonna burn a lot of tokens on this thing. But you’re, you’re one of the, the only scale platforms in the world that can, uh, that can do this across a huge variety of workloads, right? I’m even curious on a sort of human, uh, research level of like, well, do, does retail behave d-differently from like clothing sales?
D-does that behave differently from electronic sales? I, I don’t know. I don’t know what else you guys... The Kardashian shoppers, do they differ from like people who buy, uh, I don’t know, cars and, uh, whatever.
[00:51:55]
Mikhail Parakhin
: Well, very different, and different sensitivities and different modes of, uh, shopping and, and different levels of what’s important.
Now, to-totally, you can do aggregations at, uh, at a store level. You can do aggregations at a different, uh, category level. I don’t know if, uh, you know, for our statisticians among us, I couldn’t believe, but we-- recently we’re looking at it, and we had to bring back, uh, CRPs, you know, Chinese restaurant process.
It’s a, like, way of aggregating and, like, naturally grow clustering. So across... Specifically to answer questions that, uh, like you were just posing on how, how if, if buyers behave different categories. And I’m like, “I haven’t seen CRP since two thousand and one.” It’s
[00:52:37]
swyx
: so What? It’s so- What is... No, I haven’t, I haven’t seen this.
No. This is not in my training. Uh,
[00:52:44]
Mikhail Parakhin
: but, but yeah, it, uh, uh, it actually, like the, the-- there was a very popular kind of theory, popular neurips HTML circles in early two thousands, uh, kind of nice. And now, now it has practical applications, uh- Yeah ... that we were resurrecting.
[00:53:03]
swyx
: Yeah, amazing. Uh, I, I can see, I can see how this is like a, uh, a fun job for you where you get to apply all these things.
Um, yeah, yeah, so super cool. Super cool. So, okay, so, so anyone who, who knows what CRPs are and has always wanted to use them at work, uh, they should, they should definitely join Shopify. Okay, so w-we have a lot and but I, I’m, I’m being mindful of the time. I, I do wanted to, to sort of cover some other things.
Um, I-I’ll give you a choice, UCP or Liquid?
[00:53:30]
Mikhail Parakhin
: Liquid. I think, I think on UCP, you know, like UCP is very important for us and, and it just we are-- UCP, we have a structured, uh, discussions, and you can read about them, and we have, uh, blog posts, and we have a big release this week, in fact, like with our catalog.
Oh,
[00:53:46]
swyx
: okay.
[00:53:46]
Mikhail Parakhin
: Uh, yeah,
[00:53:46]
swyx
: but- Le-I mean, we, we can, we can discuss the, the, the release briefly because we’ll release this after the-- after it’s already announced so whatever. There’s a catalog that you guys are doing?
[00:53:55]
Mikhail Parakhin
: Yeah. So we are, we are- Okay ... we are bringing in capabilities of a whole, uh, Shopify catalog.
Basically, you now you can search for products, you can do lookups by specific ID, you can do bulk lookups when you need to bring m-multiple products. You don’t need to know in ad-in advance what you’re trying to show or to sell or check out. Like, you can now, you can now have this decided at, at runtime, and this big area for investment for us for both non-personalized and personalized searches, trying to provide basically a win-window into whole universe of products that are being sold everywhere in the world.
And Shopify is really not exactly, but almost like a super set of any-anything being sold. Now we are bringing it into UCP and, uh, and, uh, identity linking is another big thing for us, uh, so that you, you can use, uh, like Google or whatever, whatever identity you have, uh, they’re minimizing friction.
[00:54:56]
swyx
: Yeah. So
[00:54:57]
Mikhail Parakhin
: yeah, big release for us.
But Liquid AI of course we never talk about, and the problem might be more, more aligned with what we d-discussed previously on this chat.
[00:55:07]
swyx
: Sure. The main thing that everyone understands about Liquid is that it is inspired by Worm, and I still don’t know why. I’m curious on your explanation. I think you, you, uh, you can make things very approachable.
And also I think like what is the potential of like the, the level of efficiency that you get out of Liquid?
[00:55:23]
Mikhail Parakhin
: You- we all familiar with transformer architectures. And, uh, for the longest time, there was a competing architecture, it’s called the state space models. So, so Sams, uh, you know, Chris, Chris Reyes, one of the pioneers and, and lots of startups, uh, trying to make those realities.
They have, uh, significant benefits being main being, uh, being much faster and, uh, lower footprint and not quadratic in length, you know, sort of, uh, linear in, in, uh, in your context length. But with state space models- They never quite made it. Like they’re used-- They have, uh, certain niches when they thrive, their hybrid architectures are useful, but they never quite made it.
And liquid neural networks are, you can think of them as a next step, like, uh, sort of, uh, state-space model square. It’s non-transformer architecture that’s more complicated than sta-state space and really difficult to code if you-- if I’m being honest. But it’s, um, very efficient. It’s, uh, subline-- sub, uh, quadratic in, in length of your context.
Uh, it’s very compact way to represent things, and that’s a liquid AI company. They... Their goal is to productize it, and very often you have this need, uh, when you need to have long context and small model, and you want to have low latency. Like in general, it’s basically on par with transformers, and if you do hybrids with transformers, it’s, it’s even better.
That’s why we at Shopify, when we tried multiple and we constantly try multiple models, multiple companies, we found that for small, particularly with low latency applications, when you have low latency and/or if you need longer context lengths, liquid was the best. And so we still use the whole zoo and always like obviously test and use everything, uh, every open source model and, you know, it feels like sometimes even every private model.
Uh, but liquid’s been taking quite a bit of, uh, at least internal Shopify share. And the reason I’m excited is, yeah, because it’s, it’s the only non-transformer architecture that I found being genuinely competitive. Uh, and, uh, you know, for we use it for search and for, for long context, uh, pulse distilling and others.
This is the overview. I don’t know how approachable Sha, sorry. Maybe, maybe still too obtuse.
[00:57:51]
swyx
: I, I mean, I think they haven’t been that open about their implementation details. I think the... I would say like liquid hasn’t been like if there’s a lot of technical detail published, I haven’t read like a, a formal sort of paper on the implementation details.
Uh, but I, I did get the sort of relationship between the SSMs and the others. This is one of the sort of, uh, charts that was, you know, showing the relationship between like full attention versus Something that’s, uh, more like a RNN type in terms of their, their efficiency. Um, and then the, the other chart was this old one, uh, where it compares versus, uh, some of the other models.
Uh, doesn’t exactly have the correct Y-axis, but close enough where you can see like it’s basically a, a step change difference in terms of the efficiency. I think the surprise to me was that you guys are, uh, actively using it already in internally inside of Shopify. And like I, I’m curious, like what are the constraints that you’re optimizing for, right?
Is it when you say smaller, is it like the 1B size? Uh, what kind of like latency constraint are you, are you optimizing for? What kind of context length, um, sort of considerations, right? Like I think for example, right, like in the audio kind, kind of use cases, the SSMs ef-effectively have unbounded context length because they, they just have to operate on like the most, the sliding window of the most recent stuff.
Uh, I’m just kinda curious, like w-what do you see the potential here?
[00:59:13]
Mikhail Parakhin
: Yeah. The SSMs are effectively because, yeah, because the state embeds all the, all the previous information needed, or that’s the assumption. SSMs effectively have infinite context length. The, the problem with, uh, with them is that expressiveness is not there.
The, uh, uh, Liquids are effectively souped up SSMs. We are much more expressive, m-uh, com-more complicated again to code. There is, there is a paper on it. You can, you can see it. Differential equation rolled out and, and then computed as a, uh, as really as a convolution. It’s a bit involved. The thing where we, we use it is specifically either for where we need super low latency, and we’re-- there was a lot of very fun project with, uh, Santa ML and Liquid AI themselves.
We run it at, uh, thirty milliseconds, a, a tiny model, like three hundred million parameters in, but we run it in thirty milliseconds, uh, end to end for search when you, when you type a query, and then we produce all the possible things what you, what you can mean by that query and some, you know, uh, not only synonyms, but, but, uh, a que-kind of full query understanding the, the whole tree of what you might need and including your personal personalization because you might have done like previous queries and lowering it all down into the search server so that the requirements on latency obviously they are very, uh, very strict.
So, so then we are able to run it under thirty milliseconds because, ‘cause at Liquid, you know, Qwen doesn’t run on this. And even Liquid, we had to work a lot with NVIDIA and to... because almost everything is not designed in CUDA for or in, in the current stack for, for low latency. Like small things that don’t matter with large models, you know, start mattering a lot, and we had to optimize it.
There is different end of the spectrum where this is maximum through, uh, bandwidth throughput for things like, for example, offline categorization when A new product appears. We need to do analysis. We need to assign where it is in taxonomy. We need to extract and normalize attributes. We need to do, uh, you know, clusters like, oh, it’s the same thing as that other merchant is selling, right?
That is like un-- like almost unbounded, uh, amount of energy you need to spend on it because it’s, uh, you know, it’s quadratic kind of, uh, problem, and we have billions and billions of products. So you don’t care about latency as much. You know, it’s kind of an overnight batch job, but you, you want to maximum throughput.
And you usually in those cases, you also sometimes like for, uh, Sidekick Pulse, you also need long context. These are... We are talking models in maybe seven, eight billion, uh, parameter range, uh, where we would, we would take a large model, like we would take something huge, largest we can, we can find. We would distill into liquid for a specific task, such as, for example, for our catalog, uh, formulation or for, for Pulse.
And then we run it at a very large scale, like in batch jobs. Because just running... And, and it beats in that situation beat very often beats, uh, Qwen or, yeah, Kimi is more on the reasoning side. So Qwen, Qwen I would say is probably their major alternative. That’s when we use it. I mean, not a, not a panacea, not, not really, uh, I wouldn’t say that it’s frontier model in the sense of it’s not gonna suddenly compete with, uh, GPT 5.4.
Uh, but, but, uh, uh, it is a phenomenal target for distillation, which is right now becoming more and more important with, uh, explosion of token usage.
[01:03:00]
swyx
: Is that a, a now only thing or do you think you give Liquid a hundred billion dollars and they will do... Is it, is it just more scale or like what, what is limiting it?
You know, what prevents it from running into the same issues that SSMs had?
[01:03:14]
Mikhail Parakhin
: Their scale is already much larger than the largest SSM I, I’m aware of. Uh, uh- Wow, okay. So yeah. So, uh, SSM was just, was just not expressive enough or in my opinion. Like, um, again, I’m sure I’ve-- I’ll get a lot of pushback and probably accurately so.
But in my opinion, SSMs are not expressive enough and, uh, liquid models are. I think, uh, especially in their hybrid form when with combined with the transformer, like in Mamba fashion, they probably the best architecture I’m aware of like period. But of course, Liquid AI is not at the scale of, uh, you know, Anthropic or, or Google or OpenAI in terms of compute.
So I don’t think, uh, they... I think if, if they, uh, if they had similar level of compute, they, they would be very competitive and maybe even beat the, uh, the largest models, at least from what I’ve seen. They don’t have, uh, this level of, uh, investment But they still have decent investment and, and it’s, uh, it’s, uh, definitely for this scenario of smaller models and distilling into their second to none very often.
We are very omnivorous, and we’re on purely merit-based. So the moment they will start being competitive, we’re like, we will switch to something else, and we constantly test. But, but so far, if you see progression, if I draw a graph of our workloads on Liquid versus our workloads on, I would say Qwen, which is another awesome model and probably, uh, another kind of standard within Shopfy, I would say, uh, Liquid’s been definitely taking share
[01:04:48]
swyx
: I think that’s very promising and probably the best explanation I’ve heard, uh, directly from, from someone involved in Liquid.
Um, I, I do have Maxime Lebon coming to, uh, my conference in London, uh, this week, so I, um, we’ll- Oh, that’s great ... hear more from him. I-- ‘cause, uh, there was this, like Liquid, uh, investor day or something like a, a year or, or a year and a half ago, and I, I think there just wasn’t that much technical detail that I think was, was sort of speaking to my crowd of like potential customers and users, right?
Which like, yeah, it’s fine. Like, you know, maybe, maybe, uh, there, uh, we, we still need to wait for more results that come out, uh, before, before this. But I think it would be news to a lot of people that you guys are actually actively already using it for high-frequency use cases. I also wanted to highlight Psychic Pulse, which, uh, we didn’t cover, and we probably don’t have time to cover, but it’s something that you also launched, uh, recently.
Basically REXIS, um, but also something that like I’ve-- the, the other REXIS trend I’ve been c- I’ve been covering a lot, uh, from like the YouTube side, even xAI’s, uh, REXIS has been LLM-based REXIS, right? Uh, which I think you are also effectively using liquid models for, but they are just throwing transformers at, at the problem.
And maybe this is, uh, eh, the sort of hybrid architecture shift that will happen in order to accommodate the kind of long context and, and lo- and high efficiency that, that you need. I don’t really have a strong opinion there, like apart from I would highlight to anyone the, the, the work that the LLM base-- LLM-based REXIS community is doing is, is also very interesting there.
[01:06:22]
Mikhail Parakhin
: Yeah. The-- again, the thing to get you excited is that it’s not just LLMs looking at things, it’s also HSTU model doing that counterfactual analysis- Yeah ... where we model the whole, uh, enterprise as an entity and, and its actions and then see what, what will, what will happen.
[01:06:39]
swyx
: Overall, I think it, it pre-- this all presents like, uh, an enormous like...
I think, uh, you know, uh, there, there was not that deep of a AI story to Shopify when it started. Uh, it was just a WordPress plugin, right? But now, you know, you are the sh- the, the storefronts, uh, e-commerce, you know, uh, guardians to s- like so many, so many people, and you’re, you’re really like applying all the AI, uh, methods and the state-of-the-art stuff.
Uh, so like I, I think, you know, our conversation like today has like really, uh, oh, I guess opened my eyes to a lot. So thank you for doing this. Uh, this is a really amazing, um, overview of, uh, what you’re doing.
[01:07:15]
Mikhail Parakhin
: Okay. Thank you for saying that, Shawn, and, uh, thank you for having me. Of course, it’s always a pleasure to talk to people who, you know, deeply technical and know what they’re talking about.
[01:07:25]
swyx
: Yeah. I mean, uh, very few people are as technical as you but at least I can, I, I can like somewhat fo-- uh, vaguely follow along. Yeah. So, so, okay, um, there, there is a hi- there’s a hiring call, uh, you know, uh, any, any particular roles that you’re looking for that you’re like, “Okay, if you know the-- how to solve, um, this problem, uh, reach out”?
[01:07:45]
Mikhail Parakhin
: Yeah. Uh, the, the things I would definitely call out that if you’re an ML person or if you’re data science person and, uh, uh, we, we, we have huge need for more, more people munching data, so to speak. Or surprisingly, if you’re a distributed database person and, uh, uh, you know, we, we think that there is a way to use LLMs to reimagine how we do distributed databases, and we’re working a lot with Yugabyte there.
And so if you’re-- have interest in those areas, we’ve-- like ShortFi might be the best place in the world for you. That’s pretty good place for other, you know, other disciplines as well.
[01:08:24]
swyx
: Cool. Um, I think that that was all the questions I had. I said I, I have one sort of a bonus thing if you, if you wanna indulge in, uh, some Bing history.
What is your, uh, I guess, takeaways or any, any fun anecdotes about Sydney?
[01:08:38]
Mikhail Parakhin
: Any fun anecdotes about Sydney? Well-
[01:08:41]
swyx
: Yeah, it was a very interesting, you know-- I, I think it, like, woke up people to, like, this personality that, that, that it w-- emerged.
[01:08:48]
Mikhail Parakhin
: The, the funny thing, like, I mean, the, the most interesting anecdote is that Sydney was first shipped, uh, in India for, uh-- and, uh, it was, uh, not noticed for a long time.
And first implementation of Sydney didn’t even have OpenAI model under it. It was, it was, uh, Turing Megatron, um, Microsoft, uh, and NVIDIA collaboration model. Uh, and there were, uh, yeah, exactly. That’s, that’s the, that’s the one people thought it was a prank, uh, because it was, like, not many people were familiar with the LLMs at, at that point yet, and thought like, “That cannot be automatic.
You, you must have, uh, you know, people thinking.” And then even they were complaining that, “Oh, the-- my-- this, this chatbot is gaslighting me.” And then, then people like what, what almost everybody doesn’t fully realize is that it wasn’t by accident that, uh, Sydney was Sydney. I mean, we spent a lot, a lot of effort on personality shaping.
Uh, we-- I mean, it, it was a bit of my Yandex legacy, where previously we did this Alice, uh, uh, digital assistant, uh, which we learned the- Chatbot, yeah ... yeah. We, we learned the importance of, uh, personality shaping, and so here we brought, did a lot of personality shaping. Uh, so it was not fully an emerging scenario.
It was, it was also a little bit edgy. What, what we learned in, in those experiments is you want to be polite, but you want to be a little bit on edge, and that draws people in. I haven’t seen, ever since the, uh, kind of those days, I haven’t seen anybody trying exactly that mode. I think we will see, we will see more of this at some point, but, uh, yeah.
A lot, lots of good memories, you know. And by the way, the very first Sydney dev lead Is, uh, uh, Andrew McNamara is working in ShopFind, uh, and the head of Sidekick and, and our-- and the Pulse- Oh. And lots of these are actually, yeah, in his pur-purview.
[01:10:53]
swyx
: Oh, okay. Uh, I-- That, that’s another fun fact. You’re, you’re- Yeah
assembling the team again. Yeah. Yeah, it’s cool. Like, I think a lot of, uh, people woke up to the, the idea of AI personality for the first time there. And, like, I think now with maybe OpenClaw, like explicitly prompting a, a fun personality, I think that, that is a real selling point for, for people, right? And then I, I guess maybe the only other time that it’s like really emerged into public consciousness is Go to Gate Clawed.
But yeah, I think, uh, you know, hopefully someday we’ll get Shopify Sydney.
[01:11:23]
Mikhail Parakhin
: Well, we have Sidekick. It’s a- Yeah ... it’s a different, different thing a little bit. Yeah.
[01:11:28]
swyx
: Yeah. Si-Sidekick was like your, your original big launch for, for AI stuff. Uh, yeah, cool. Uh, amazing. Uh, thank you so much. You guys do amazing work.
Uh, honestly, if I was a Shopify customer, Shopify investor, um, hearing all the work that you guys are doing o-on this technical side, it, like, m-makes me feel more confident in like, okay, just choose Shopify, right? Like, like you’re never gonna do this in-house, which is obviously what you want. But like, uh, yeah, I mean, like, that-that’s, that’s what an ideal platform is, like, that you’re doing all the things that no individual could do at their scale, but you can at your scale.
Uh, very exciting problems.
[01:12:01]
Mikhail Parakhin
: Exactly. Exactly. Yeah. And creating network effect and hard to disagree. If you’re not using Shopify, you should.
[01:12:09]
swyx
: Yeah, amazing. Okay, well, that’s it. Thank you so much.
