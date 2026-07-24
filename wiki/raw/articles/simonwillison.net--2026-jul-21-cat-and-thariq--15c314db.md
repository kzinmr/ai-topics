---
title: "A Fireside Chat with Cat and Thariq from the Claude Code team"
url: "https://simonwillison.net/2026/Jul/21/cat-and-thariq/#atom-everything"
fetched_at: 2026-07-24T10:13:56.001159+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# A Fireside Chat with Cat and Thariq from the Claude Code team

Source: https://simonwillison.net/2026/Jul/21/cat-and-thariq/#atom-everything

A Fireside Chat with Cat and Thariq from the Claude Code team
21st July 2026
Earlier this month I hosted a fireside chat session at the
AI Engineer World’s Fair
with Cat Wu and Thariq Shihipar from Anthropic’s Claude Code team. We talked about Claude Code, Claude Tag, Fable, coding agent security, evals, tool design, and how Anthropic use these tools themselves.
The full video of the session is now available
on YouTube
. Below is an edited copy of the transcript, with extra links and my own bolded highlights.
A few top-level notes if you don’t want to watch the video or wade through the whole transcript:
Claude Tag (Claude’s new collaborative Slack integration) now lands
65% of the product engineering PRs
for the Claude Code team.
Claude Code ships features to Anthropic employees first, and
only ships the features that demonstrate user retention with that cohort
Critical changes to Claude Code are still reviewed manually, but the team increasingly relies on automated code review for the “outer layers” of the product.
Adding examples to a system prompt is
no longer best practice
for models like Fable 5 or even Opus 4.8. The Claude Code system prompt recently
reduced in size by 80%
.
Likewise, lists of "
don’t do X and don’t do Y
" can reduce the quality of results from the latest models.
Dogfooding
inside Anthropic is called "
ant fooding
".
Anthropic
really believe in their
auto mode
, and see that as an enabling technology for Claude Tag.
Thariq advises offsetting coding-agent-induced
Deep Blue
by "
being more ambitious
" with the work you take on.
Fable is
competent at editing video
, and Thariq
used it
to edit its own launch video.
Anthropic’s culture of working (internally) in public is key to their success, as demonstrated by the way they use Claude Tag in their public Slack Channels.
How has what you do day-to-day changed in the past year?
1:05
Simon:
Claude Code came out in February of last year — it’s under a year and a half old, and it was originally just a bullet point on
the Claude Sonnet 3.7 launch
.
How has what you do on a day-to-day basis changed in the past year
, now that we have these coding agents that actually work for us?
Cat:
I remember when we first came out with Claude Code and Sonnet 3.7, you would give it a task and you would have to closely monitor every single little thing it tried to do. I would read every permission prompt extremely carefully. I would frequently say no — no, no, no, did you check this file? Did you check that file? And now it’s been incredible with every model generation. I feel like
we’ve all gotten a chance to take a step back and delegate a lot more of the menial implementation to Claude
. It’s freed up a lot of our time to think about more creative work, like: what is the right experience that we should be providing to our users, now that we know Claude Code can implement a lot of it? And now with Fable it’s a totally different step change improvement.
We see for a lot of our use cases that you can actually one-shot a ton of features with Fable now
.
Thariq:
I remember the first text I got about Claude Code. One of my best friends was like, “You need to go try Claude Code.” It was about when Opus 4 came out, and I tried it and I was like, “Oh, shit. I need to work at Anthropic now.” And that was Opus 4 — great model, but you were reading permission prompts. It’s kind of crazy how much amnesia we have, where I’m like, oh, auto mode has always been here, right? I don’t even remember pressing yes and allow. For me, the big thing I’m trying to push myself on is that
we have to do higher quality work than we’ve ever done before
. The outputs are incredibly high quality.
I’ve been using it to edit videos a bunch
, and I’m like, okay, it has to meet the very exacting demands of our brand team in a couple of hours or we just can’t do it.
That’s how I’m trying to shift with Fable: the best work we’ve ever done, faster than we’ve ever done it before
.
What piece of conventional software engineering no longer holds?
3:39
Simon:
What’s a piece of conventional software engineering that was true a year ago that you don’t think holds anymore in this new world?
Cat:
One of the biggest shifts we’re seeing in the eng skill set: two years ago it was pretty typical for a product manager to go talk to a bunch of customers, align over the course of six months with cross-functional teams on some PRD, and write a thorough spec on exactly how we’ll implement this before the first line of code gets written. Now things are completely turned the opposite way. For a lot of engineers, the push I would give to folks in the room is to
develop more of your business sense and product sense on what it is we should build
, because the timeline between having an idea and building it is so much shorter — it’s down from six to twelve months to maybe even a week. That means all of us need to have better taste on what is worth building, what will actually inflect the businesses we’re working on. So it’s
an increase in value on product taste and business sense
, and a bit lower on execution in most product domains. Of course, for infra there’s still a very heavy emphasis on making sure all the details are right.
Thariq:
For me, it’s that
rewrites are now good
.
Simon:
The worst thing you could do is now actually fine!
Thariq:
Exactly. All the Mythical Man-Month stuff — never rewrite — I’m pro-rewriting now. If you have a good test suite — and
I think the rewrite actually forces you to make sure you have a good test suite
— but I think what people undercount is that
a codebase is a spec, and maybe it’s the only copy of the spec that you have
, because no one knows every branching part of the codebase. You can take this as an artifact and distill it or create other versions of it. We
rewrote Bun in Rust
and it works great — it’s live for me right now.
Simon:
You’re not shipping Claude Code on Bun-in-Rust yet, right?
Thariq:
Internally we have.
(Actually it looks like Anthropic started shipping Claude Code on Bun-in-Rust to everyone
on June 17th
.)
What kind of things are non-engineers doing with Claude Tag?
6:36
Simon:
The other big launch recently was
Claude Tag
— that’s what, a week old now, at least for the rest of us. I understand it’s being used at Anthropic by non-engineers a great deal.
What kind of things are non-engineers doing with Claude Tag?
Cat:
Claude Tag is a Claude that lives in your team’s collaboration tools. We launched it last week within Slack.
The thing that’s different about Claude Tag is it’s multiplayer by default
. Once you add Claude Tag to a Slack channel, you can chime in, your teammates can chime in, and you can collaborate together on the PR. The other big difference is that it’s proactive instead of reactive. You can tell Claude Tag, “Hey, monitor every bug report in this channel, put up a PR to fix it, and tag the engineer who last touched this part of the codebase,” and it’ll do it for the lifetime of the channel without you having to manually tag it in. And the third big shift is that
we’ve
added team memory
into this
. If you tell Claude Tag your preferences in the channel, it’ll remember them for every future post. If you always want it to debug outages but you don’t want it to debug warnings, just tell it that in natural language in the channel and it’ll remember it for you and everyone else on your team.
Internally, we see Claude Tag as the evolution of Claude Code.
We see this as a large shift in how we work internally.
Claude Tag currently lands 65% of our product eng PRs.
Simon:
For all of Anthropic, or just for Claude Code?
Cat:
This is just for our product engineering team —
our internal version of Claude Tag lands 65% of our product PRs right now
. And this is a huge shift; this is more than 50% of our PRs. The way we see people split work between Claude Code and Claude Tag is: Claude Code is still the best place for your most complex tasks, when you’re interactively iterating with the agent.
But Claude Tag is great for having it work proactively on your behalf
, so you no longer need to manually kick off Claude Code for all the bug reports that come up for features you’re working on.
Thariq:
And for non-coding cases: for example, before this talk we asked Claude Tag, “Hey, when is Fable releasing?” We wanted to make sure we’d line it up with the announcement. Claude Tag would search our Slack and look at who’s been saying what.
As a search engine for your company, it’s really valuable.
It has all the context for your product, so you can ask it metrics-related questions — often when you’re making decisions you want them informed by what the metrics say, so you hook it up to your event store. I’ve seen our marketing team do things like, "Hey, tell me about this feature." They’re not programmers, but Claude is a programmer — it can clone the codebase and say, "This is the feature, this is what it looks like,
this is a recording of me using the feature
." It enables a whole wide variety of things, and I think we’re still early in figuring that out.
Claude Tag as the team collaborative layer
10:06
Simon:
One of the problems I’ve had with coding agents is that I get how to use them as an individual, but I’m not really clear on how to use them in a team environment.
It sounds like Claude Tag is your current answer to that team collaborative layer for this stuff.
Cat:
Exactly. And a large percentage of our sessions are actually multiplayer right now. Maybe I say, “Hey, I think we should implement this new feature in Cowork,” and I’ll tag in Claude Tag to do a first pass at it. Then I’ll tell Claude Tag, “Share a recording of your final implementation,” and I’ll tag in design to take a look. They’ll nudge it, then pass it on to eng to take it to the finish line and get it out to prod. It’s been this very fluid experience.
We’re still trying to iron out what the social dynamics are for steering the same session
, but we’ve found that people just observe how others use it and follow those social norms — it’s been pretty intuitive for us to integrate Claude Tag into our teams.
Thariq:
It’s great for teaching people, and also for reducing slop, because
the fact that everyone is seeing you use Claude together sort of levels up how you use Claude as well
.
This reminded me of how Midjourney solved the challenge of teaching people advanced image prompting by enforcing prompting in public in their Discord channels.
How do you decide which features are worth building when building is so much cheaper?
11:41
Something I’ve found really hard myself is knowing when a feature is worth shipping now that the cost of actually building features has dropped so much.
Simon:
How do you deal with the hardest problem in all of engineering — prioritization?
How do you decide which features are worth building and shipping when building a feature is so much more inexpensive now?
Cat:
This is the hard thing. There are a few ways we approach it. One is we dogfood our products every single day. Whenever there’s something we want to be able to do in our products that we’re not able to, instead of finding a different solution we fix our product so it can support that case.
We have a very heavy dogfooding culture internally.
Before we share our products with everyone in the world, we share them with everyone within Anthropic, and with some early customers who give us very honest feedback about it — the more brutal the better — and we iterate until people love it.
We have an internal bar for the number of active users and the amount of retention a feature has to have before we share it with the world.
Because this bar is very clear, every engineer knows what they’re trying to hit. I think this also levels up our polish, because if the feature isn’t polished, people will churn — and then we shouldn’t ship that feature.
Using internal user-retention to decide if a feature should ship makes a whole lot of sense to me.
Do you have an example of a feature which surprised you?
12:54
Simon:
Do you have an example of a feature which surprised you?
You rolled it out and the engagement was off the charts — something unlikely to be shipped that turned into a real product thing.
Cat:
I do have one.
A lot of folks on our team love
remote control
.
Remote control lets you use your mobile device, or Claude in the web browser, to connect to a local Claude Code session running in your CLI. I never have this need, because I just kick off the task directly on mobile and it runs in a cloud session without using my local environment — I think because I’m doing very easy coding tasks. It was something I didn’t totally understand; I was like, hey, people should just set up remote dev environments. But in practice, once we rolled out remote control, so many people I talk to told me that what they do every night is plug their laptop into a power charger, open a bunch of remote control sessions, lock the screen,
and then use their mobile phone from their couch to control Claude Code
. So this has become a flow we’re now leaning into that I didn’t originally get — but now I do.
Does a human review every line of production code in Claude Code?
14:20
One of the over-arching themes of the conference was review: how much attention to people spend to reviewing code written for them by coding agents. I was very keen to hear the Claude Code team’s take on this!
Simon:
How does code review work?
Does a human being review every line of production code that makes it into Claude Code?
And if not, what are you doing — how do you keep the quality up?
Thariq:
It varies on the task a lot.
For important areas we have code owners.
The system prompt is an example where we have a code owner — you really need to get their approval.
Simon:
So the code owner is directly responsible for the quality of that area of the code.
Thariq:
That’s right.
Cat:
And they need to approve any PR that touches it.
Thariq:
We have
our code review GitHub bot
review everything — that goes on every PR, and often it’s doing the bulk of the review. Something I’ve seen on the team is that
for more complex PRs you might make an artifact to explain the PR
so that other people can then review. And we invest a lot into verification, CI/CD, things like that, to make sure that any time anything fails we have a test. We have a really robust environment where Claude can control Claude Code and test it. So there’s a multi-pronged approach to code review.
Cat:
In general,
we are trying to move to a world where humans don’t need to be in the loop
. For the most critical changes to the core of Claude Code, and the cores of other products, there is always a code owner and they do manually review all the changes. But increasingly,
for the changes at the outer layers, we actually have Claude code review fully review those
. That sounds pretty scary, but we’ve had a six-plus-month-long process to get here, and
there are baby steps that you take to build up trust with code review
. In the beginning we had human review for everything, and then increasingly we would say,
okay, for code changes that touch these files, code review is catching 100% of the issues there — so we actually don’t need a human manually reviewing those
. And when we have incident review,
we look at the PRs that caused the incident and say, okay, how do we update code review to catch that?
— and we take those PRs and
add them to an eval set
to make sure our future changes to code review never regress that metric. Removing humans from the code review loop is a big step forward. It can sound scary, and it’s not something you can do overnight, but it is something you can do
through many months of investment in the infrastructure
to give you the confidence that code review is catching everything you care about.
So the key seems to be constantly iterating on the automated review systems themselves, in order to build trust in them over time.
How does a new model affect your intuition for what it can and can’t do?
17:20
We got
deep
into evals—another hot topic throughout the wider conference.
Simon:
I know that Opus 4.8, if I ask it to build me a JSON endpoint that runs a SQL query and outputs JSON, is just going to get it right — that’s not something I have to review closely. But then a new model comes along and I don’t know how to build trust in Fable quickly, that it’s not going to mess things up that Opus didn’t.
How does the new model affect your intuition for what it can do and what it can’t do?
Cat:
The main reason we’re building up this
eval base over time is so that new models can be a drop-in replacement
. When we have a new model, we run the whole eval set and make sure that, for example, Fable is strictly better than Opus 4.8 — and that gives us the confidence to drop it in.
Simon:
Are those model evals for Anthropic as a whole, or Claude Code team-specific?
Cat:
We have both. We have evals on our team, and we run code review across every repo within Anthropic, so we have evals for that. And for things like auto mode, we not only have evals across every user within Anthropic — we’ve also commissioned multiple external testers to red team it, to create environments with prompt injections and malicious inputs,
and make sure that auto mode doesn’t let any of those pass
.
How do you build confidence that a system prompt tweak results in better output?
18:41
Simon:
I want to know if the system prompt improvement I made actually improved the product — that’s the most basic form of product-specific eval, and I still don’t have a great feel for how to do that.
Is that something you’re doing such that you have complete confidence that a tweak you’ve made to the system prompt results in better output?
Cat:
We don’t have complete confidence, but we do a lot to make sure that we don’t regress performance.
The starting point is a suite of external evals that we trust, and we complement that with an even larger suite of internal evals that we trust. To start,
we mainly optimize for capability
: given a complete definition of a task and the full codebase, does Claude make the right decisions, fully fix the bugs, and pass all the tests? That’s the starting point and the thing we optimize for, because it’s most directly what users want. But there are a lot of behaviors that impact how users feel when they work with Claude Code. For example,
people really don’t like it when Claude Code says it’s time to go to sleep.
Or people really don’t like it when it says, “Hey, I finished two out of five parts — do you want me to continue?” Yes, please continue.
So we’re building up a set of behavioral evals to catch these.
And as we get user feedback — please be loud with us about your user feedback — we rank the priority issues and go down one by one and build evals for each of them. It’s not 100% coverage, but it is a priority for us to increase the coverage.
How much interaction is there between the Claude Code team and the model training teams?
20:21
Simon:
How much interaction is there between the Claude Code team and the teams at Anthropic who are training the models in the first place?
Is that quite a close collaboration?
Cat:
Across Anthropic, we all work quite closely together. We meet often to talk about what we expect the next generation of models to be able to do. Our research team has also been amazing about showing this publicly — we often talk in our blog posts about how
we’re targeting ever-increasing longer-horizon work
, and how we train Claude itself to be honest, harmless, and helpful. We also put a lot of effort into making sure it’s aligned with your intent, even if your intent is expressed in a fuzzy way. Of course, try your best to be specific about what you want, so Claude has all the context — but even when you’re not specific, we teach Claude to make good assumptions. It’s been a productive partnership.
The system prompt has been reduced by 80% — what have you been able to drop?
21:24
So many useful prompting tips in this section!
Simon:
Thariq, you
mentioned this morning
that the
system prompt for Claude Code has been reduced by 80% because of Claude Fable
. Can you go into a little more detail?
What kind of things have you been able to drop?
Thariq:
It wasn’t just Fable — it was Opus 4.8 as well, and going forward, future models. We have different system prompts for different models now. One of the patterns we saw is that we were over-constraining Claude. The initial, maybe Opus 4-ish models wanted a lot of examples, and
removing examples was extremely helpful
, because it was just more creative than the examples we gave it.
Simon:
That’s really interesting, because one of the top prompting tips I give people is: give it examples. If that’s no longer true, that kind of breaks my prompting model a little bit.
Thariq:
Same here — I was surprised to hear that. I think now it’s more about the shape of what you give it — the tools you give to Claude, your system prompt, things like that. The other thing we did is try to give it more context and
fewer “do not do this”
instructions, because that’s a very strong impulse for Claude, and especially if it conflicts with user instructions later on, that can be extremely confusing to Claude — “I’ve got this skill that says this and the system prompt says this.” So we try to
have fewer hard constraints, more context, and fewer instructions overall
. It’s definitely a science — it took a bunch of evals to build.
Cat:
In general, when you’re prompting these models, you should always think:
are there edge cases to the instruction that I’m giving it?
When we went back and reviewed all the instructions in the Claude Code system prompt,
we found a few cases where yes, this statement is 90% true, but there’s a real 10% of cases where it’s not true
. We didn’t want to constrain the model, or confuse it into thinking it should always do this. One good example is verification. Everyone here wants Claude to verify its work, and we had some instructions in the prompt that said: if you make a front-end change, always verify. But there’s a limit to it. If it’s changing copy from one string to another string, and the user says “just make a quick fix and update the test,” maybe you don’t want to verify.
So we’ve adjusted our wording from “always verify, verify, verify” to something like: most of the time when you’re doing front-end work you can’t fully understand the experience by hitting the backend endpoints, so when you make larger changes to the user experience, please run the app locally.
And in fact, that instruction probably isn’t even good either, because
what is a large change?
Maybe it should test small changes too. In general, whenever you give a prompt to the model,
you should think about the ways in which it could be misinterpreted by a well-intentioned human
, in order to better understand how the model might interpret it — and
soften the prompt
so that it’s actually 100% accurate, because you’re giving this prompt to the model 100% of the time.
Simon:
What’s fascinating about that is you’re
relying on the model’s judgment
— and that’s got to be an Opus/Fable-level thing. Models a year ago did not have the level of judgment necessary to decide whether they were going to test a change or not. But that does break down if you’re building for a wide range of models and trying to run the cheaper models for cheaper tasks.
Cat:
We actually have
a different system prompt per model now
, for this very reason. It’s only our most frontier models that have this 80% token decrease — the older models still have the full system prompt.
Simon:
Do you think Fable and Opus are smart enough to prompt Haiku with more details, because they understand that Haiku has less judgment, less taste?
Cat:
We haven’t been able to eval it — we don’t have any hard data to show it.
Thariq:
There’s a tough thing with smaller models sometimes, because
sometimes the larger models can be more token-efficient on a hard problem than the smaller models
. So there’s a bit of intuition to build there — sometimes you really just want frontier intelligence almost all the time. The Pareto curve shifts, and it’s hard to find.
Simon:
A year ago I did not trust a model to write a prompt. Today the good models are very good at prompting — a lot of my prompts are written by models, which feels absurd but works really well. What helped me come to terms with that was thinking about subagents, which are entirely about a Claude model setting up a prompt for another Claude model.
Thariq:
Workflows
are actually a really good example of this, because it’s Claude not just prompting a single subagent, but prompting the orchestration of many subagents, and each one of them gets a very detailed prompt. It’s almost a level above just spawning a subagent. I’ve also been using it on my personal machine,
giving it the Gemini API and saying: here, generate images
. It’s way less lazy than I am at prompting an image model. It’s just Claude prompting Claude all the way down.
Cat:
I think Claude also wrote the prompt for
the workflow tool
.
Simon:
I’ve read that prompt — it’s a good prompt. That’s actually a frustration I have with Anthropic generally: you
publish the prompts for Claude Chat
, but you don’t include the tool prompts and the Claude Code prompts. I still have to run a proxy to intercept them.
I would love it if the Claude Code prompts were deliberately published
— they’re the documentation. They’re how you know what the tool can do and how it works.
Cat:
I’ll write down that feature request. I’ll have Claude Tag do it.
Interesting to note that OpenAI’s
prompting best practices for GPT-5.6
includes similar advice for their latest models:
Favor leaner prompts
Removing repeated instructions and examples and simplifying tool descriptions can improve task performance and token efficiency. In a sample of internal coding-agent eval runs, configurations with leaner system prompts improved evaluation scores by roughly 10–15% while reducing total tokens by 41–66% and cost by 33–67%.
28:06
Simon:
Claude Code is basically a big bag of tools.
What’s your bar for introducing a new tool?
How do you decide when it’s worth doing that additional engineering at that level?
Cat:
Do you want to take it? You introduced one of the best tools we have.
Thariq:
My career peaked when I introduced the ask user question tool. It’s really hard. Especially for some tools —
ask user question is Claude’s tool to ask you
— so it’s hard to eval, and sometimes it’s more of a user preference thing. Back then we had fewer evals, so it was very dogfooding based — or “ant fooding,” our ant version of that. But overall
we’ve been trying to trend towards fewer tools
. The last set of tools we introduced was the task tool, I think — and we try to give Claude more general versions to do things.
29:03
I have a long-running fascination with file editing tools—they were the subject of the
old Aider code editing leaderboard
, and I’ve watched with interest as they’ve evolved in different coding agents from search-and-replace based to line-number-based to more complicated patterns.
The Claude API docs describe a
text editing tool
that’s recommended for building against the API, but Claude Code seems to use slightly different approaches here.
Simon:
One of the most interesting tools is the file editing tool — you can have file editing as a tool, or you can tell it to use sed and grep and do things that way.
What’s the latest evolution of your file editing tool?
Thariq:
We still have one, but for example we removed our grep and other search tools — glob tools — in favor of native bash. Like I said in my talk earlier,
the models are kind of more of a biology than a physics
, and tool design especially is quite hard. I’m not sure if Cat disagrees and thinks there’s a science to the eval of it, but I think tool design is more of an art, maybe — or a biology.
Cat:
I largely agree, but in general as we introduce more tools, we try to keep the cardinality pretty low and make sure that
every tool we add has a distinct function from every other tool, so that Claude can very easily distinguish when to call each
. For file edit, the reason we have it is actually because we can render it. We show people when Claude makes a file change, and there’s this
nice dedicated UI
that says: do you approve this edit to this file?
The reason we had a dedicated file edit tool was so that we could deterministically know
that Claude was making a file change, so we could show people this nice UI. A lot of new users onboarding still really like this experience, so we’ve kept it around. But for a lot of us who are on auto mode right now — hopefully you’re not on YOLO mode — I don’t think it actually matters, and we could probably just remove file edit and be totally fine.
What’s the advice within Anthropic for safely running Claude Code?
30:58
It’s the
prompt injection
question! Who better than Anthropic employees to explain how Anthropic sees the risk of prompt injection attacks causing their Claude Code instances to run amok?
It turns out they
really
trust their
auto mode
—and see that as the feature that enabled Claude Tag.
Simon:
Let’s talk about safety and security. I am deeply aware of the risks of prompt injection, and there are so many bad things that can happen if somebody else tells my Claude Code what to do. I still mostly run Claude Code in YOLO mode and feel incredibly guilty about it.
What’s the advice within Anthropic for safely running Claude Code?
Cat:
Why not auto mode?
Simon:
I am starting to use auto mode, but I don’t understand it enough to get how safe it is. As of maybe three weeks ago, I’m defaulting to auto mode.
Cat:
Broadly within Anthropic, almost every single person uses auto mode. It is the best way to do long-running work in Claude Code while being safe.
We’ve done extensive bashing. We have thousands of evals. We’ve commissioned many red teamers to create adversarial environments in order to trick Claude Code into doing bad actions, and we’ve mitigated every single issue that they found.
We’re going to publish some evals in the coming weeks, but we’ve pretty much mitigated every attack.
Simon:
That is a big claim.
Cat:
We’ll share the evals for it so folks can assess, but we’ve been extremely diligent about identifying all the ways in which Claude might mess up and then updating auto mode to counter it. It doesn’t catch 100% of things — that would be way too strong a claim. But
for the main categories of risks that we’re concerned about, like prompt injection and data exfiltration, the risks are far lower than the average human reviewer
.
I am very much looking forward to learning more about their evals and approach to verifying auto mode.
Thariq:
A little on how auto mode works — it’s useful to build this mental model. Whenever Claude is doing a turn, or a bash call, there’s
a Sonnet classifier
that is judging the tool call and also the context of the conversation — your instruction. There are some things around permissions that are dependent on your request: you don’t want to give git push permissions all the time, but if you say “push this to GitHub,” you want it to do it — and if you say “don’t push,” you want it to deny it. Auto mode will do that. That particular thing happens to me a lot, where Claude tried to do something because it’s very helpful and proactive, and auto mode saw “don’t do this” and surfaced it.
So it’s good at the dynamic permissions
that you yourself give inside the prompt, which I think is really important. It also works well with our
sandboxing infrastructure
, because sandboxing is one of those things where there are so many different edge cases that it’s hard for us to deterministically follow them.
We have a sandbox, and when something needs to escape the sandbox
— like a network request — auto mode can look at that request and ask: does this make sense? — and allow it.
Simon:
I hadn’t realized auto mode is interacting with the networking sandbox as well.
Cat:
It interacts with any permission prompt the user would otherwise see.
Simon:
How old is auto mode? As a feature I had access to, it’s only a couple of months old, right?
(It was first made available to the public
on March 24th
.)
Cat:
We’ve been using it within Anthropic
since January
, so we’ve been hardening it for quite a while. Anthropic is extremely focused on safety and security, and we’ve been working broadly across our alignment and safeguards teams to enable the rollout internally, build out these evals, and make auto mode even more robust before sharing it with the world.
Thariq:
This is also the reason Claude Tag is so good —
Claude Tag uses auto mode
. I’ve heard a lot of build-versus-buy questions about a Slackbot, and I’m like: please, you probably shouldn’t build your own AI Slackbot. There are so many attack vectors.
You have a feedback channel that users can post feedback into, and now your bot is reading it.
The work we’ve put in with auto mode — and we have a general
Swiss cheese defense
for security; we also RL against this stuff —
I think this is really what makes Claude Tag work
. It works seamlessly with your permissions, and you don’t want to be prompt injected in your Slack.
Are there more security things in the pipeline beyond auto mode?
35:54
Simon:
Are there any more security things in the pipeline that go beyond auto mode?
Thariq:
I think we’re very secure.
With Claude Tag you can provision your own credentials for Claude
, so it doesn’t need to act on your behalf — you can have Claude as an identity, and that also makes it easier to audit and inspect what Claude is doing.
Simon:
Because Claude Tag is influenced by anyone who can talk to it — it’s got a much wider pool of people telling it what to do.
Thariq:
That’s right. And of course we have probes as well with Fable, which is a downstream effect of our safety and research work. I think this is the moment where you see Anthropic being an AI safety company really paying off:
we really want Claude to be able to run in an aligned way over long periods of time
, and
auto mode has to be basically flawless for this to work
— it’s all downstream of our being an AI safety company.
Cat:
We also launched trusted devices for the remote control users out there who want to be safer. And for all of our remote environments, we support
credential injection
. If you want Claude Code to be able to access Datadog, but you don’t want Claude Code itself to hold the Datadog credential, you can set up our identity and credential management system
so that the Datadog credentials are only usable by the agent but not accessible by the agent
— we insert them on the fly when the agent tries to make a Datadog request.
I really like that credential injection pattern, where Claude Code can access an API via a proxy and that proxy both audits the request and injects the relevant API key—so Claude can access authenticated endpoints without having access to the API credentials itself.
How has the past year and a half changed how you think about your own craft?
37:53
Thariq
talked about a sense of grief
brought on by Fable-class models in his keynote in the morning, and we dived further into that as part of our conversation. I’ve been calling this
Deep Blue
.
Simon:
Let’s talk a little bit about the human element.
A lot of people are feeling a sense of loss now that so much of what they considered to be their role in building software is being subsumed by the models.
How do you think about that?
How has the past year and a half changed the way you think about your own craft and the value that you add?
Thariq:
Cat and Boris are such good reminders that you have to be more ambitious. They’re always like: we’re growing so fast, we have to be on the edge, we have to do the best work we can. That’s a constant reminder for me — any time I’m slow on something, I’m like, okay, can I do it faster? Can I be more ambitious here? And oftentimes the answer is Claude, because Claude is getting better as you go — the last time I tried this, it was with the previous model. On your point about loss: I think this is real.
If you’re only trying to do the same work you were doing before LLMs, and now it’s a prompt, it is, I think, kind of a sad feeling.
And
the way you offset that is by being more ambitious.
I think Jared is such a good example — he hand-wrote all of the Zig code in his Oakland apartment in about a year, barely left his house, and had so much fun doing that. Now I see him rewrite all of Bun into Rust and
he’s having so much fun doing that
— it’s so much more ambitious, and that’s how he offsets it. Generally it’s asking
how do I do the bigger thing
and do more —
I think success is fun
. It’s changing your ambition.
“The way you offset that is by being more ambitious” neatly captures where I’ve landed on this issue myself as well.
Simon:
And Cat, what does that look like from a product management perspective?
Cat:
I feel like the product role just changes every single month.
All the PMs on our team are this mix of engineer, designer, PM
— most of them actually used to be full-time engineers. For us it really means
plugging in whenever there’s any kind of gap
. If we have an idea and we didn’t inspire any engineer to go build it, then we should just build it, put it into a notebook, and inspire people to take it to production. If the designs look a little off,
let’s take a page that’s similar, do a first-pass design, and tag in someone who’s very detail-oriented to fill in the gaps
. Or if we notice that our team and product adoption is bigger within the company, and more people need to know what’s coming down the pipe for Claude Code, Claude Tag, and Cowork — let’s automate figuring out our whole launch calendar,
let’s automate getting those status updates asynchronously
so we’re not bugging people, and make sure our updates in our internal announce channels are fully detailed and to the point. For us it’s very much understanding
what the gap is right now between a great idea and getting something to our customers
, and
how do we automate it as much as possible
.
This reflects something I’ve noticed: when you can produce code so much faster, time spent blocked awaiting a decision from someone else becomes a much more notable bottleneck. Engineers who can make product decisions can move a whole lot faster, and the cost of getting one of those decisions wrong is much less prohibitive.
What’s a moment when Claude has surprised you?
41:50
Simon:
What’s a moment when Claude has surprised you?
When the model did something you didn’t think it would be able to do?
Thariq:
I’ve posted a lot about Claude video editing, but most recently I gave a talk at the ACM Agentic conference, and I asked, "Hey guys, do you have the edited video? I’d love to post it and share it with my comms team." They said, "Oh, it’s taking so long." So I asked for the raw files. They sent me the video of me talking on stage, the video of the deck, and the audio file, and said, "Good luck." I gave this to Claude, along with my HTML deck, and said, "
Hey, can you just edit this together?
“ And what it does is honestly incredible — I’m ready to ship it. It transcribes the entire video. It notices that sometimes the video of my deck is a little weird — there’s a popup of an auto-update in the middle — and it goes, ”
Oh, I probably shouldn’t use the video of your deck. What I’m going to do is slice it up, figure out which slide you’re on, and use the HTML source instead.
" So it displays the HTML source. Then it’s got video of me, but I’m only taking up a small part of the stage, so
it’s cropping dynamically to where I am on the stage
— and I’m pacing, so it’s tracking me as I pace. And it’s transcribing what I’m saying.
Simon:
This was Fable, right?
Thariq:
This was Fable, yeah. It was a good prompt, but it was a one-shot prompt. Then I asked it to add some interesting animations and graphics, and I was just blown away.
It does ffmpeg, it does Remotion.
Here’s Thariq’s video
on how he used Fable to edit Fable’s own launch video
, and here’s
that launch video
.
What can’t it do yet?
43:36
I’m embarrased to admit that I’ve been finding it quite hard to come up with tasks that frontier models like Fable 5 and GPT-5.6 are unable to accomplish.
Cat still doesn’t rate its UX design skills:
Simon:
What can’t it do? What are the things where you’re still disappointed — where you’re waiting for Claude Fable 6 to figure it out for you?
Cat:
I want it to have better design and UX taste. It’s now at the point where if I write out a prompt with a detailed spec of how I want a feature to behave, it will usually behave that way. But the paddings might be off, or the interface just isn’t delightful yet. It leans on existing best practices for how apps are designed, but
for frontier AI products, there are so many new interaction experiences that we have yet to design
.
Simon:
There’s an Opus aesthetic — you can look at something and go, “Yeah, that was designed by Opus.” It’d be good if we could move beyond that.
Cat:
Yeah. I’m very excited for future models to hopefully be
interaction design thought partners
.
Thariq:
What can’t it do? I would love to see it interact more with the real world. Can it solve science? Can it orchestrate the experiments? There’s some amount of coding that goes into that, but there’s also this other taste of the broader world that it needs.
Which parts of Anthropic’s culture should other companies steal?
45:11
I figured this would make a great closing question:
Simon:
Which parts of Anthropic’s company culture do you think uniquely help Anthropic be productive with these tools, that other companies should steal?
What are the cultural hacks people should be adopting from you?
Cat:
I’ll share one for Claude Tag.
Claude Tag works best when you have it in a public channel, and when most of your channels are public.
Claude Tag is able to search across all public channels to get as much context as possible to give you the highest-accuracy answer — and
it’s only able to do this if it has access to everything
.
Thariq:
I mentioned this in my keynote, but it’s so important to me I want to re-emphasize it. The co-founders
say we don’t negotiate against ourselves
, and I think this is really important.
You can imagine trade-offs in your head and talk yourself out of doing something ambitious — or you can just try to do the ambitious thing.
We’re so often asking: what if we just did it? Is this a real trade-off or not? And if so, why — where’s the proof that it’s a real trade-off, and not just something that sounds reasonable?
Make the trade-offs show themselves to you. Be as ambitious as you can.
What’s your favorite absurd thing you’ve built with Claude, just because you could?
46:46
I couldn’t resist throwing in this one as well.
Simon:
What’s one of your favorite absurd things that you’ve built with Claude, just because you could build it?
Thariq:
I’m working on
a 2D Street Fighter fighting game with me as a character
— and my friends as well. It uses Claude Code to prompt Gemini — and honestly the Seedance model is pretty good — to make video animations. It works great; it’s so good at prompting, and it can verify the frames to check whether an animation was good.
Simon:
Is this Street Fighter 2-level 2D sprites you’re generating?
Thariq:
Yeah, exactly — 2D sprites. The animation looks amazing. And it can also figure out hitboxes — it can be like, “Oh, your fist is here, I’ll draw the JSON hitbox.” It’s incredible.
Cat:
Mine is much more simple. I’m a big rock climber and a lot of my friends climb, so we have this little app we built with Claude Code where we log all the projects we’re working on. We also go outdoors together a lot, so we have Claude do all this research with workflows. Workflows is amazing — we brand it as a coding tool, but it’s amazing for doing deep research for travel. I also plan our team offsites, and it’s good at finding venues that can fit all of us. I use workflows to research all the climbing destinations we might want to go to, and what has direct flights from where all of us are located. It goes to Mountain Project and finds all the climbs at our grade level. It finds the Airbnb. And I don’t like hiking, so I care a lot about it having a very short approach —
very short walking distance from where the car parks to where the rock actually is
— and it filters for this. With existing apps I have to manually click through Mountain Project, but with this I just put in all of our preferences and it’s a custom app for us.
Simon:
So you’re basically vibe coding Jira for mountain climbing.
Cat:
Exactly.
49:23
We had a few minutes at the end for questions from the audience.
Audience:
Do you have any near-term plans to build more eval tools for us to build eval datasets, and more observability tools to monitor the performance of agents and workflows?
Cat:
We’ve considered building eval tools, but I think the limiting factor actually tends to be that
it takes a long time for customers to build really high-quality evals
. So I think the tooling is less of the constraint, and more the skill set of how you build a great eval. That’s an area where we’re excited to both invest internally and hopefully share some best practices externally.
Audience: How is memory designed today — and would you move from files to a data store?
50:08
Audience (Sai):
I’m interested in the memory and the multiplayer.
How is memory being designed today?
I assume it’s around files. And second, have you thought about an orthogonal direction where you
would actually need a data store for these memories, instead of files, to scale it better?
Thariq:
Right now for Claude Tag the memory is channel-specific. Every Claude in that channel has a shared memory, and the instances have a session — but the session can contribute back to main memory. We do a lot of memory research, and it can be kind of unintuitive what the right way to do memory is. We’re always running memory experiments.
How it works right now in Claude Tag is a markdown file per channel.
