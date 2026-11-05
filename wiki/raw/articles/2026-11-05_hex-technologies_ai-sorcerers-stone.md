---
title: "Building a self-improving AI agent at Hex"
source: "Hex Technologies Blog"
url: "https://hex.tech/blog/ai-sorcerers-stone/"
scraped: "2026-11-05T06:00:26.116652+00:00"
lastmod: "2026-11-04"
type: "sitemap"
---

# Building a self-improving AI agent at Hex

**Source**: [https://hex.tech/blog/ai-sorcerers-stone/](https://hex.tech/blog/ai-sorcerers-stone/)

Skip to main content
📈
A new era for Hex, and data
Announcing Hex 4.0, and a $100m fundraise building toward the agent-native future for analytics.
Blog
The AI sorcerer’s stone
What a summer of building a self-improving agent taught me about research, ephemerality, and curiosity.
Deena Sun
Engineering
Updated
November 4, 2026
Share:
twitter
linkedin
In this article
Building an agent to rebuild itself
The shifting sands in a world with AI
The stones are what you learn
The magic of ephemerality
Get started for free
As part of my summer internship at Hex, I built an agent in Hex designed to rebuild the agent in Hex. The code I merged will probably be changed by the very code I merged!
Seeing agents unlock this new level of recursive innovation and play a part in their own creative destruction has underscored something we think about a lot at Hex: what is stone and what is sand?
Building an agent to rebuild itself
Hero (
He
x
R
ecursive-self-improvement and
O
bservability) combines agentic observability with an autoresearch-like loop to continually improve Hex’s agents. Hero enables us to proactively notice novel, emerging issues via bottom-up discovery. After all, realistic evaluations are hard! We’ve researched a
lot
into how to make our
offline evals approximate the real world
as closely as possible, but nothing beats actually evaluating the real thing. Hero analyzes real threads made by real people, serving as a real-time complement to our offline evals research. The Hero cycle consists of 3 main steps.
First, we orchestrated agents to autonomously analyze threads from real-life Hex usage. Each analyzer agent deep-dives into an agent trajectory with the goal of finding issues in our agent harness, both hard failures (explicit errors, exceptions, and crashes) or soft failures (when an agent fails to do what the user expected/wanted).
Secondly, to understand patterns at scale and separate signal from noise, an aggregator agent hierarchically groups findings into clusters. Clusters connect issues
across
individual interactions, group recurring issues into themes, and tie problems back to root causes (from small fry like conflicting tool instructions to big fish like subagent handoff flow).
Finally, each cluster becomes a call-to-action we can triage with a PR. To close the self-improving loop, we collaborate with agents to remediate a cluster, using the findings as evidence and test cases. Then, the cycle begins all over again. The analyzer and aggregator agent actually reuse a lot of the same harness and agent platform code as our other Hex agents! So any changes to the Hex agent ecosystem that Hero leads to are also technically changes to parts of itself.
The shifting sands in a world with AI
Hero isn’t the only example of how AI has accelerated the innovation game. With agents,
writing code is a lot cheaper
(
but not necessarily always easier
).
More and more things are becoming ephemeral and temporary — AKA sand-like, as opposed to stone-like — with AI:
Models change from generation to generation, unlocking new modalities, capabilities, and behaviors.
Hex’s agent harness evolves constantly as our AI engineering team improves it and adapts to new research or model releases. Prompts, tools, and what’s “state of the art” all shift as we step towards new maxima. This summer, the Hex team merged an average of 215.9 PRs a week (+35% from last summer) and wrote/deleted an average of 105.2K lines of code a week (+133% from last summer). Even accounting for team growth, per-engineer PR throughput increased by 23%, and weekly lines-of-code per engineer more than doubled!
Hex’s product is transforming as what people want to be able to do with their data, and with their agents, changes.
This evolution is happening at a faster, faster, and
faster
pace every day. As far as anyone can tell right now, the second derivative is still positive.
So, on top of this entire stack of constantly-shifting Jenga bricks, I literally built a self-recursive agent system that’s supposed to change itself. Given that all this seems like quicksand, you may ask: will anything I did exist in 6 months? Well, the mind-bending reality is that if my intern project succeeds, you shouldn’t even be able to know it ever existed in the first place!
At least not in its current form :)
The stones are what you learn
Rather than getting lost in the sauce of the Ship of Theseus paradox à la software, I don’t think Hero’s, or any research’s value, necessarily comes from the lines of code that constitute it. My research project was less about researching the perfect code and more about researching the right ideas! In research projects, the path to finding the answer is just as hard, uncertain, and unknown as the answer itself. The journey usually looks a lot more like a stochastic ramble than a straight-line vector. AI still isn’t great at substituting in for the human knack of going, “huh, that’s weird!”, thinking laterally about what question to ask next when the current track isn’t panning out, or knowing what ideas are worth discovering.
I had to relearn what “progress” meant when code, PRs, and prototypes became so malleable. Instead of optimizing for lines of code, I anchored each week around the questions or hypotheses I wanted to answer; and what experiments, prototypes, or spelunking I needed to do to make progress towards them. My results were sometimes successes that worked, experiments that might not have panned out but that I learned something from, or an “I still don’t know.” But regardless of their outcome, the results informed the research questions I wanted to pursue in my next sprint.
Some examples of what I built over the course of my summer sprints:
A knowledge bank of lessons learned from experiments that didn’t work. For instance, chunking threads into disjoint parts for multiple subagents to analyze wasn’t worth the squeeze — multi-turn trajectories common in Hex workflows involve many causal steps and error-tracing requires having full context over how an agent might stumble but recover.
The mental muscle reps for what a full-fledged ecosystem of developmental agents within Hex might look like.
The ideological foundations for agentic observability and self-improving agents at Hex, which we are continuing to add to, apply, and expand upon even as our platform and the wider AI industry transform beneath our feet.
The “stone” part of research-driven engineering thus becomes more about what we learn, and how that feeds back into the wider corpus of knowledge. Even if AI research
feels
different, it’s still a science. And every experiment, success or failure, should be something that contributes back to this body of science.
I fell in love with the process of research: not necessarily the artifacts of the journey (the code, the daily background automations I configured, the tables in our database I modeled) but the ideas that spin out of it.
The magic of ephemerality
To some degree, software engineering has always meant embracing code’s ephemerality. As my manager Caitlin tells me, any engineer who’s been around long enough would shudder to imagine their code still in production! AI has just dramatically accelerated this ouroboric cycle such that it’s now visible even within the span of a summer internship.
As Hex’s intern, I’ve had the time of my life taking nascent ideas about recursive self-improvement, autoresearch, and evals… and shipping the research! One of the joys of building software is that “the programmer, like the poet, works only slightly removed from pure thought-stuff” (from Fred Brooks’ book The Mythical Man-Month). We think our magical thoughts, type out our mystical spells into our computer, and suddenly we’ve created programs that can do just about anything we dream of. Ultimately, the code is just a vehicle for the “pure thought stuff”, i.e. our ideas, questions, and curiosities. The joy of coming up with our pure thought stuff is something AI accelerates, not obliviates. When we embrace the ephemerality of code, we ready ourselves to adapt alongside innovation (which AI is just one example of in the grand scheme of technological change).
So I say, yes! Lean into the weightlessness that ephemerality unlocks, let yourself be pulled by the gravitational force of your curiosities. Embrace the pure thought stuff that comes from the process of building and rebuilding. Your
weird
, crazy ideas just might be the stones that make up the next magic mountain.
…or at least be another excuse for our CEO Barry to make a
short film
.
Share:
twitter
linkedin
This is something we think a lot about at Hex, where we're creating a platform that makes it easy to build and share interactive data products which can help teams be more impactful.
If this is is interesting, click below to get started, or to check out opportunities to join our team.
✨
Get started for free
👩‍💻
Open roles
More on Engineering
BLOG
Improving the Notebook Agent: error clustering
Charlene Chambliss
·
October 22, 2025
Why you should analyze your agent's reasoning, not just its errors
BLOG
The AI data sprawl
Barry McCardel
·
September 9, 2026
Nobody can trace it. The data team still owns the mess.
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
Company
About
Careers
Customers
Solutions
Media kit
Newsroom
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
