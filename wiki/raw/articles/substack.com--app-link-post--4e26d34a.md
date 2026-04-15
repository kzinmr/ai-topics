---
title: "Notion’s Token Town: 5 Rebuilds, 100+ Tools, MCP vs CLIs and the Software Factory Future - Simon Last & Sarah Sachs of Notion"
url: "https://substack.com/app-link/post?publication_id=1084089&post_id=194195821&utm_source=podcast-email&play_audio=true&r=2flx6&utm_campaign=email-play-on-substack&token=eyJ1c2VyX2lkIjo0MDg3NDgyLCJwb3N0X2lkIjoxOTQxOTU4MjEsImlhdCI6MTc3NjIxMzEwMCwiZXhwIjoxNzc4ODA1MTAwLCJpc3MiOiJwdWItMTA4NDA4OSIsInN1YiI6InBvc3QtcmVhY3Rpb24ifQ.HS47A2FYAnZ5kRaQrNAy8TImklEtaEFFB4efpfPDXQc&utm_source=substack&utm_medium=email&utm_content=play_card_duration#play"
fetched_at: 2026-04-15T00:31:55.697304+00:00
source_date: 2026-04-15
tags: [newsletter, auto-ingested]
---

# Notion’s Token Town: 5 Rebuilds, 100+ Tools, MCP vs CLIs and the Software Factory Future - Simon Last & Sarah Sachs of Notion

Source: https://substack.com/app-link/post?publication_id=1084089&post_id=194195821&utm_source=podcast-email&play_audio=true&r=2flx6&utm_campaign=email-play-on-substack&token=eyJ1c2VyX2lkIjo0MDg3NDgyLCJwb3N0X2lkIjoxOTQxOTU4MjEsImlhdCI6MTc3NjIxMzEwMCwiZXhwIjoxNzc4ODA1MTAwLCJpc3MiOiJwdWItMTA4NDA4OSIsInN1YiI6InBvc3QtcmVhY3Rpb24ifQ.HS47A2FYAnZ5kRaQrNAy8TImklEtaEFFB4efpfPDXQc&utm_source=substack&utm_medium=email&utm_content=play_card_duration#play

For all those who missed out on London, see you in
Miami
next week!
Notion, the
knowledge work decacorn
, has been building
AI tooling since before ChatGPT
, with many hits from
Q&A in 2023
and
unified AI in 2024
and
Meeting Notes in 2025
. At the end of their last Make user conference,
Ryan Nystrom teased Notion 3.0’s Custom Agents
- and they are finally embracing
the Agent Lab playbook
!
Sarah Sachs
and
Simon Last
of Notion
join us for a deep dive into how Notion built Custom Agents, why it took years and multiple rebuilds to get right, and what it means to turn a productivity tool into an agent-native system of record for enterprise work.
We go inside the product, engineering, evals, pricing, and org design decisions behind one of the most ambitious AI product efforts in software today — from early failed tool-calling experiments in 2022 to agent harnesses, progressive tool disclosure, meeting notes as data capture, and the long-term vision for software factories and agentic work.
We discuss:
Sarah and Simon’s path to launching Notion Custom Agents, and why the feature was rebuilt four or five times before it was ready for production
Why early agent attempts failed: no tool-calling standard, short context windows, unreliable models, and too much complexity exposed to the model
The “Agent Lab” thesis
: not just wrapping a model, but understanding how people collaborate and building the right product system around frontier capabilities
How Notion thinks about roadmap timing: not swimming upstream against model limitations, but also building early enough that the product is ready when the models are
Why coding agents feel like the kernel of AGI, and how Notion is thinking about “software factories” made up of agents that spec, code, test, debug, review, and maintain codebases together
How Sarah runs AI engineering at Notion (“
notes from Token Town
”): objective-setting over idea ownership, low-ego teams comfortable deleting their own work, and a culture designed to swarm around fast-changing opportunities
The “Simon Vortex,” company hackathons, and why security gets pulled in early rather than late
How Notion organizes AI: core AI capabilities and infrastructure, product packaging teams, and a broader company mandate that every product surface must increasingly work for both humans and agents
Why prototypes have become much easier to build internally, and how “demos over memos” changes product development inside a tool the whole company already uses every day
Notion’s eval philosophy: regression tests, launch-quality evals, and “frontier/headroom” evals that intentionally only pass ~30% of the time so the company can see where model capabilities are going
What a “Model Behavior Engineer” is, and why Notion treats eval writing, failure analysis, and model understanding as a distinct function rather than just software engineering
The changing role of software engineers in the age of coding agents, and why the new job looks less like typing code and more like supervising a rigorous outer system of agents, PRs, and verification loops
How the “software factory” should work: specs, self-verification, bug flows, subagents, and minimizing human intervention while preserving the invariants that matter
A live walkthrough of a Notion Custom Agent handling coworking space tenant applications by triaging email, enriching applicants with web search, and writing structured data into a Notion database
How agents compose inside Notion: shared databases as primitives, agents invoking other agents, “manager agents” supervising dozens of specialized agents, and memory implemented simply as pages and databases
Notion’s take on MCP vs CLI: why Simon is bullish on CLI’s self-debugging nature, where MCP still makes sense, and how Sarah thinks about capability, determinism, permissioning, and pricing alignment
The evolution of Notion’s internal agent harness: from early JavaScript coding agents, to custom XML, to Markdown and SQL-like abstractions, to tool definitions, progressive disclosure, and a much shorter system prompt
Why Notion cares about teaching “the top of the class,” building for sophisticated operators rather than abstracting away too much capability for everyone
How agent setup works today: agents that can configure themselves, inspect their own failures, and edit their own instructions — with guardrails around permissions
How Notion prices Custom Agents: credits as an abstraction over tokens, model type, serving tier, web search, and future sandbox costs; why usage-based pricing was necessary; and how “auto” tries to match the right model to the right task
Why Notion is not eager to train a foundation model, where they do fine-tune and optimize today, and why retrieval/ranking is one of the most important investment areas as more searches come from agents rather than humans
Why Meeting Notes became one of Notion’s strongest growth loops: not just as transcription, but as high-signal data capture that powers search, custom agents, follow-up workflows, and the broader system of record for company collaboration
Why Notion is more interested in being the place where collaboration data lives than in building hardware themselves — and how wearables or other capture devices may eventually feed into that system
Sarah Sachs
LinkedIn:
https://www.linkedin.com/in/sarahmsachs
X:
https://x.com/sarahmsachs
Simon Last
LinkedIn:
https://www.linkedin.com/in/simon-last-41404140
X:
https://x.com/simonlast
00:00:00 Introduction and launching Notion Custom Agents
00:01:17 Why Notion rebuilt agents four or five times
00:03:35 Building for where models are going, not just where they are
00:05:32 The Agent Lab thesis, wrappers, and product intuition
00:08:07 User journeys, leadership, and low-ego AI teams
00:13:16 The Simon Vortex, hackathons, and bringing security in early
00:16:39 Team structure, demos over memos, and building for agents
00:20:25 Evals, Notion’s Last Exam, and the Model Behavior Engineer role
00:27:37 Evals as an agent harness and the changing role of software engineers
00:30:42 The software factory: specs, verification, and agent workflows
00:32:18 Live demo: a custom agent for coworking space applications
00:35:08 Composing agents, manager agents, and memory as pages
00:38:15 Notion Mail, Gmail, native integrations, and tools
00:39:43 MCP vs CLI and the cost of capability
00:44:13 When Notion uses MCP vs building its own integrations
00:47:43 The history of Notion’s agent harness rebuilds
00:55:35 Power users, public tools, and the setup agent
00:58:01 Self-fixing agents, permissions, and “flippy”
01:01:13 Pricing, credits, and choosing the right model automatically
01:09:01 Why Notion isn’t training its own frontier model
01:14:07 Retrieval, ranking, and search built for agents
01:17:27 Meeting Notes as data capture and workflow automation
01:21:18 Wearables, hardware, and Notion as the system of record
01:23:45 Outro
[00:00:00] Alessio: Hey everyone. Welcome to the Latent Space podcast. This is Alessio founder of Kernel Labs and I’m joined by swyx, editor of the Latent Space.
[00:00:11]
swyx
: Hello. Hello. We’re back in the beautiful studio that, uh, Alessio has set up for us with Simon and Sarah from Notion. Welcome.
[00:00:18]
Sarah Sachs
: Thanks for having us.
[00:00:19] Alessio: Thanks for having us. Yeah.
[00:00:20]
swyx
: Congrats on the launch recently the custom agents, finally it’s here. How’s it feel?
[00:00:26]
Sarah Sachs
: We ship things slowly. So it had been in Alpha for a little bit and at the point at which is it’s an alpha, um, there’s a group of people that are making sure it’s ready for prod, and then there’s a group of people working on the next thing.
So sometimes some of these launches are a bit delayed satisfaction, so it’s quite nice to remind yourself all the work you did because we do have a habit of like. Being two or three milestones ahead. Uh, just ‘cause you have to be, you know, you can’t get complacent. Um, but it’s been great that people understood how this is helpful.
And I think that’s just easier in general building AI tools today than it was two, three years ago. People kind of get it and so that user education, um, there’s just, it was our most successful launch in terms of free trials and converting people and things like that. It was really successful, so yeah.
But there’s a lot to build.
[00:01:12]
swyx
: Making it free for three months helps.
[00:01:16]
Sarah Sachs
: Yep.
[00:01:17]
Simon Last
: It was definitely super exciting for me because it’s probably the fourth or fifth time that we rebuilt that.
[00:01:22]
swyx
: Yes.
[00:01:23]
Simon Last
: And I mean,
[00:01:24]
swyx
: you’ve been building this since like 20, 22.
[00:01:26]
Simon Last
: Yeah, I mean, like, it was even right when we got access to like GPT four in late 20 22, 1 of the first ideas we had is like, oh, okay, let’s make an agent that I, we used the word assistant at the time, there wasn’t really the word, the word agent yet, but, oh, we’ll give an access to all the tools the notion can do, and then it, we run in the background like, like do work for us.
And then we just tried that many times and it just. Was too early. Um,
[00:01:48]
swyx
: I need to force you to like double click on that. What is too early? What didn’t work?
[00:01:52]
Sarah Sachs
: We were fine to, like, before function calling came out. We were trying to fine tune with the Frontier Labs and with fireworks, like a function calling model on notion functions.
This is right when I joined. I joined because, um, we needed a manager as Simon was needed to be able to go on vacation. So, uh, that’s, that’s around when I joined, so you can speak much more to it.
[00:02:11]
Simon Last
: Yeah, we did partnerships with both philanthropic and open AI at different times, uh, to try to, at the time the, I mean, when we first tried, there wasn’t even a constant of like tools yet.
We, we sort of designed our own like, like tool calling framework and then we tried to fine tune the models to, uh, to use it over multiple turns. Um, and because it, it didn’t work well out the box, I think. Yeah. The models are just too dumb and the context thing was also way too short.
[00:02:37] Alsesio: Yeah.
[00:02:37]
Simon Last
: Um, and yeah, we just kind of banged our head against it for a long time.
Uh, unfortunately it was always like, there was always like sort of. Glimmers that it was working, but um, it never felt quite robust enough to be like a useful, delightful thing. Um, until I would say, uh, the big unlock was probably like Sonic 3.6 or seven, uh, early last year. And that’s when we started working on our agent, which we shipped last year.
Um, and then, and then uh, uh, custom agents, kinda a similar capability and that, that one just took longer because we, we just wanted to get the reliability up a lot higher. ‘cause it’s actually running in the background.
[00:03:14]
Sarah Sachs
: And the product interface of like permissions and understanding, you know, this custom agent is shared in a Slack channel with X group of people and has access to documents that are surfaced to Y group of people.
And the intersect experts, Y might not be whole. And so how do you build the product around making sure administrators understand that permissioning took multiple swings.
[00:03:35] Alsesio: Everything is hard back at the end of the day. Yeah. I’m curious, like when the models are not working, how do you inform the product roadmap of like, okay, we should probably build, expecting the models to be better at some reasonable pace, but at the same time we need to, you know, you had a lot of customers in 2022.
It’s not like you were a new company or like no user base.
[00:03:54]
Simon Last
: Yeah, I mean I think there’s always the balance of, you know, like you want to be a GI pilled and thinking ahead and building for where things are going. Uh, but also you wanna be like shipping useful things. And so we always try to like, like keep a balance there.
You know, we. We try to take clear, like a portfolio approach. You know, we’re always working on multiple projects and, and we’re always trying to work on, you know, maintaining things where that have already shipped, like, like shipping new things that are like eminently working well and make them really good.
And, and then we wanna always have a few projects that are a little bit crazy. Um,
[00:04:23] Alsesio: and what are the a GI peel projects that you have today? I’m curious about, uh, you don’t have to share exactly what you’re working on, but I’m curious what are things today that maybe in 18 months people will be like, oh, obviously this was gonna work
[00:04:35]
Sarah Sachs
: 18 months.
[00:04:37] Alsesio: Yeah, 18 months is, you know,
[00:04:37]
Sarah Sachs
: it’s a long time and Yeah. Yeah.
[00:04:39]
Simon Last
: I mean, there’s a number of things happening. I think one thing that’s becoming more clear is I think like, like, uh, coding agents are the kernel of EGI, sort of, everything is a coding agent. Mm-hmm. I think that’s, that’s sort of one, one direction.
Um, and then, yeah, the exciting thing about that is sort of your agent can sort of bootstrap its own software and capabilities and actually debug and maintain them. And so yeah, we’re, we’re, we’re thinking a lot about that. And then, yeah, like, like another category of things that I’m, I’m really excited about is like, uh, we call the software factory also.
People are using this, uh, this, this sort of word. Um, basically it just means can you create sort of like a, as automated as possible, a workflow for developing debugging. Mm-hmm. Merging, reviewing, and maintaining a code base and a service where there’s a bunch of agents working together inside, and like, like how does that work?
[00:05:28]
Sarah Sachs
: If you think back to your initial question, like, why did this take so long? I think something,
[00:05:32]
swyx
: I didn’t say that, but Yes. Okay. Go ahead.
[00:05:34]
Sarah Sachs
: Why, what, what changed over the three and half years of trying
[00:05:37]
swyx
: it? Exactly. Right. Because most people always say like, it didn’t work yet. Then reasoning models came, then it worked.
I was like, okay, let’s go a little
[00:05:43]
Sarah Sachs
: bit. That’s, I mean, that’s part of it, but I think the other part of it that I actually think is really what will set notion apart for every new capability is we have like. Two skills that are crucial when it comes to frontier capabilities. One is not letting yourself swim upstream.
So like quickly realizing if you’re just pressing against model capabilities versus not exposing the model to the right information, not having the right infrastructure set up. That and of itself is the skill of intuition. And the second is to see, okay, you’re not swimming upstream. Which direction is the river flowing and what is like, how do we think ahead about the product and start building it even if it’s not great yet, so that when it is there, we’re ready for it.
Right? And like those can sometimes feel like counterintuitive things. Like we can be trying to fine tune a tool calling model when they don’t exist yet. And that the trick is to not do that for too long, but realize that there was something there. And we’ve had a lot of things which like, um, we’re just like not swimming in the right direction with the streams.
I think we had multiple versions of transcription before we got meeting notes, right? Oh, I gotta talk
[00:06:39]
swyx
: about that. Yeah.
[00:06:40]
Sarah Sachs
: Yeah. Um, and so. I, I, I think that like we, we really closely partner with the Frontier Labs on capabilities and we also have to have strong conviction on, as those capabilities move.
Notion is about being the best place for you to collaborate and do your work. And how does that narrative change if the way that we work changes?
Yeah.
[00:06:58]
swyx
: Yeah. You told me you were a fan of the Agent Lab thesis, and this is, this is kind of it, right?
[00:07:02]
Sarah Sachs
: Right. I show that thesis to so many candidates. Like I have it as like micro chrome autofill.
Um, at this point, like it’s one of my most visitations
[00:07:10]
swyx
: because like, is this the, here’s why you should work in notion and not open, open eye. I, it’s like,
[00:07:14]
Sarah Sachs
: here’s, here’s what’s different about it.
[00:07:16]
swyx
: Yeah.
[00:07:16]
Sarah Sachs
: And here’s why. It’s not just a rapper. I actually think more and more people understand it’s not just a wrapper.
[00:07:21]
swyx
: Yeah.
[00:07:22]
Sarah Sachs
: Um, and by the way, like in the beginning, parts of what we build are wrappers on functionality. That works well, of course, but that’s not really the most, um. I would say that’s not the product that, that drives revenue. And that’s not necessarily always what users need.
[00:07:35]
swyx
: I mean, you know, notion is the AWS wrapper, but like the, the wrapper is very beautiful and like very, very well polished.
So
[00:07:40]
Sarah Sachs
: like the analogy,
[00:07:41]
swyx
: like
[00:07:42]
Sarah Sachs
: the analogy that I’ve been coming back to his Datadog in AWS
[00:07:45]
swyx
: Yeah.
[00:07:46]
Sarah Sachs
: So, uh, Datadog could not exist with, without cloud storage. Right. That it’s kind of fundamental that that works. Um, and AWS has like a CloudWatch product, but Datadog is an expert on understanding how people want observability on the products they launch.
And we’re experts in understanding how people wanna collaborate, and that’s really where our expertise lies.
[00:08:04]
swyx
: Totally.
[00:08:04]
Sarah Sachs
: Um, regardless of the tools that we use,
[00:08:07] Alsesio: I’m kind of curious how you think about implicit versus explicit expertise. I feel like Datadog is half and half implicit and explicit. It’s like they understand across markets and industries what engineering teams usually look for.
With notion, it’s almost like more of the expertise is at the edge because you as a platform, you’re like so horizontal that the end user is not really the same. Mm-hmm. Like with Datadog, the end user is always like, yeah, an engineering lead, a kinda like SRE related person with notion. It can be anything.
So I’m curious how you put that expertise into a product versus, you know, obviously it, WS cannot build notion. It’s, that doesn’t quite work in this case, but
[00:08:44]
Simon Last
: it’s, it’s a little bit differently shaped. I think, you know, a classic vertical SaaS, like the data is kind of like that. They understand their individual customer very deeply.
It’s kinda a narrow slice, um, notion has always been super horizontal. And our, our task has always been to sort of balance these two somewhat opposing forces of like, we’re listening to our customers and what they want us to build. It’s a broad slice. And then also we’re thinking about like, okay, how do we decompose what they want into, uh, nice primitives that are, that are really nice to use and we’ll, we’ll get us like as much bang for the buck as possible.
And then, you know. Maintain the whole system, make it all like, like super clean and nice to use.
[00:09:22]
Sarah Sachs
: We still have user journeys. I mean, we still focus on like core. I actually think the failure of our team is when we focus too much on what are cools that are, what are tools that are
[00:09:31]
Simon Last
: mm-hmm.
[00:09:31]
Sarah Sachs
: Cool tools. I actually think that’s when we make have the least velocity because you still need some sort of focus on a user journey.
So like for instance, we’ll all sit down every Friday and look at the P 99 of like the most token exhaustive custom agent transcript and just look at why it didn’t do well and cut a bunch of tasks. Like we still focus on like, this has, like this should work. Email triaging should work. Mm-hmm. Right. And similarly, like when we’re talking about before building, um, chatting, um, before we started filming about, okay, how can I do PDF export?
Well that’s functionality that then merits. Maybe we should build a tool that has access to a computer sandbox in a file system and the ability to write code. Right? Right. Um, but it’s because we’re thinking about the fact that our users to do their, to do their daily work, need to export PDFs, not because we’re like, Hmm, I think a computer tool could be cool.
Like, let’s just see what happens. Mm-hmm. Like we, we have to focus on some user journeys, otherwise we just don’t have like, enough strategy to, to prioritize.
[00:10:29]
swyx
: I think there’s a lot of like really strong opinions that you’ve had. Do you have like sort of like a towel of
Sarah Sachs
? Like, you know, like what, how do you run your team?
Like I feel like you just have accumulated all these strong opinions. Obviously part, part of this is your, your token town thing.
[00:10:43]
Sarah Sachs
: I think the TAs working with Service X is, um, you’d have to, it depends who you ask. Um, I think it depends if you’re on my team or a partner Right. Or a vendor.
[00:10:54]
swyx
: Yeah. There other people want to run their teams the way that you’re Yeah.
You’re like bringing these things. And then also similarly, uh, Simon, when you did the custom agents demo, you had like, well, we’ve been using custom agents and here’s the super long list of everything that we do. No humans ever read it. Right? That’s what you said. I was like,
[00:11:07]
Sarah Sachs
: yeah. So I think for, for me, um, something that I learned very quickly and became very comfortable with was that my job was not to be the ideas per person or the technical expert.
My job was to make it so that everybody understood the objective, had a resource to help prioritize what they should work on, and had an avenue to prioritize what they thought was important. And I think that’s true with all, all leadership, but I think especially on the AI team. Almost all of our best ideas come from prototypes, from people that have a cool idea because they saw a user problem, and it’s a huge disservice if all of those ideas have to pass, like the sniff test of what me and a product partner or Simon and Ivan decided were the direction, right?
Because a lot of what we’re doing is leaning into capabilities, so. I think that’s the first thing is like, I don’t really view like the role of engineering leadership as like, uh, hierarchical, nor has it ever been, but especially now, like very willing to change direction based on, um, like proof is in the pudding.
Yeah. And like, and I think we have rebuilt our harness three or four times. And when you do that, then the second rule of engineering leadership is like you need to build a team that’s comfortable deleting their own code and is very low ego and is driven by what’s best for the company. And, um, doesn’t write design docs because they think it’s their promotion packet.
Right. And that’s a culture that notion had long before I joined, but like our willingness to just swarm on different problems and um, redo things that we’ve built before because something has changed. Like, there’s a lot of friction that can happen at companies when you do that. And it doesn’t happen at Notion.
And because it doesn’t happen when new people join. Like they don’t wanna be the ones that are saying, we shouldn’t do this. I wrote that code. So then it’s, you know, you, you create a culture that everyone thoughts and that culture comes directly, I think from Simon and Ivan though, um, because they’re very open-minded.
[00:12:50]
swyx
: Anything that you,
[00:12:50]
Simon Last
: you’d add? I’m not a manager, like, like, like Sarah is. Um, a lot of my role is really to try to think a little bit ahead, make sure that we’re, we’re building on the right capabilities and then like the prototyping stuff. And yeah, it’s really, really critical to always just be starting again.
It’s like, okay, this is new thing. What does this mean? What if we just rethought everything or wrote everything? And so I, I’m, I’m basically just doing that in a loop every six months.
[00:13:16]
swyx
: Yeah. Do you believe in internal hackathons for this stuff?
[00:13:19]
Sarah Sachs
: I think there’s like two different versions. So one is like, we just have a, a, a solid bench of senior engineers that come and go on what we call the Simon Vortex and Productionizing what we built, right?
Because when you’re in the Simon Vortex, the velocity is super high. The direction changes daily, and it’s meant to be like the equivalent of a SC Works lab. We don’t need to do hackathons for that. We need to have senior engineers that we trust to come in and out of those projects. For instance, like management boundaries are really loose.
Like you report to him, but you work for her right now. Yeah. That’s something that when we hire managers, it’s important they don’t care about because we tend to form more structures. Yeah. Don’t be too
[00:13:54]
swyx
: territorial.
[00:13:55]
Sarah Sachs
: We form more. It’s after we ship things, not not before, just historically. Um, the second thing is we do have companywide hackathons.
Actually we just had our demos day for the hackathon we had last week this morning. That’s more for people that aren’t directly working on the project, feeling like they have the time to pause and learn how to make themselves more productive or how they would use notion custom agents to build something.
Or part of the hackathon was actually encouraging everyone across the company to build their own agentic tool loop, calling from scratch. Follow like an every blog post on how to do what I think because we want
[00:14:26]
swyx
: just with the compound engineering one. Yeah.
[00:14:28]
Sarah Sachs
: We want everyone to use cloud code in the company or whatever the coding agent they please and understand that fundamental.
So we set aside a day and a half. We’re all leadership, encourage everyone on their teams across the company to do it. So we have hackathons like that. I would say like kind of facetiously, like everything we build is a little bit like a hackathon until it graduates and puts on big boy pants and as a product ops rollout leader and has a assigned data scientists and stuff like that,
[00:14:54]
swyx
: security review enterprise stuff,
[00:14:56]
Sarah Sachs
: actually security reviews one of the things that we bring in first because it just slows us down way more and, um, causes a lot of tension and they build better product if they’re involved early.
So, um, that is probably the first person to get involved in something that’s the
[00:15:09]
swyx
: right PR approved answer.
[00:15:10]
Sarah Sachs
: No, but it’s not just PR approved. It like, um, um, it’s
[00:15:13]
swyx
: actually real. It’s actually real. It’s like, um, I’m just saying scar
[00:15:15]
Sarah Sachs
: tissue.
[00:15:15]
swyx
: Yeah,
[00:15:16]
Sarah Sachs
: because like, you know, my background’s also, I worked at Robinhood for a number of years.
Yes. So like, uh, compliance and things like that, um, are a little bit more, you learn the hard way when it doesn’t come naturally.
[00:15:26]
Simon Last
: Yeah. I think the. The hackathon is really important for uplifting the general population, but like, if that’s the only way you can build new things, you’re kind of toast. I mean, it, it has to be like the daily processes, like, you know, building these new things.
Um, and it has to be about, I think like, I think in the AI era a lot more leverage accumulates to the most curious and excited people. And so it’s like we’re all about just like activating that energy. You know, like if someone’s protesting something on the weekend that they’re excited about and it’s important, that should be the main thing that we’re doing.
Yeah. Um, it’s not a hackathon that we schedule once a quarter, it’s just like, yeah. Daily process. Part of the culture.
[00:16:02]
Sarah Sachs
: I mean, that’s how we shift image generation and notion now. It was always this thing that would be kind of nice to have, but it wasn’t really clear where that was necessarily aligned in product priorities.
It’d be a lot of work. And we had someone on the database collections team, Jimmy, who was like. I really wanna do image generation for cover photos and inside notion. And we’re like, if you wanna build it, like it’s, do it please. Like we encourage you. We gave ‘em all the resources of working directly with Gemini and being able to like track the token usage and it working through endpoints.
We gave them eval, support, everything, and then became a, a full project.
[00:16:34] Alsesio: Yeah.
[00:16:35]
Sarah Sachs
: That’s why you can’t have like ego as a, a leader. Like that’s, that’s how we work.
[00:16:39] Alsesio: What’s the size of the team today, both engineering and overall?
[00:16:43]
Sarah Sachs
: I manage, uh, the team. That’s what we’ll call it. Core AI capabilities and infrastructure.
That’s about 50 people. But then we have per i partner teams that do packaging. So how it shows up in the corner chat versus custom agents versus meeting notes, that’s another 30, 40 people. And, and then every team that has a product service at Notion that a user can interface with owns the tool that the agent interfaces with the editor team.
The team that did CRDT for offline mode is the same team that handles how two agents, um, edit competing blocks. Mm-hmm. Right? It’s the same problem. The team that built the underlying SQL engine is the same team that owns how the agent asks it to run a SQL query, and it does it performantly. And so from that regard, anyone working on product engineering is tasked with making them work for customers that are humans and agents because over time the majority of our traffic will be coming from agencies using in our interface, not humans.
And so. Our objective is to make it so that the whole product org is building for agents.
[00:17:40] Alsesio: Yeah. How has it changed internally? The activation bar is kind of lowered a lot. Like anybody can kind of create a prototype very, somewhat easily, especially if you’re like an existing code base. Have you raised the bar on like what type of prototype people need to bring forward to gonna be taken?
Not like seriously, but like, you know what I
[00:17:58]
Simon Last
: mean? Yeah. I think the bar is lowered in many ways. Be like, one thing our, uh, our team built that is really cool is our, uh, our, our design team made a whole separate GitHub repo, uh, called the, the design Playground. And it’s basically just to create a bunch of like, like helper components and you, uh, for, for quickly a throwing together UIs.
And it’s become like actually quite sophisticated. Like it has like an agent in there and like, uh, that’s pretty fun. So like, we pretty much, like, they don’t do mocks, they just make like, like full, full prototypes.
[00:18:27]
swyx
: Here it is. It works.
[00:18:28]
Simon Last
: They give you like a u rl. They’re like, okay, all right. So we have to make the, like the real production version of that.
Um, and then for engineers. A prototype looks like just making it a feature flag that actually works. Like that’s sort of the bar.
[00:18:39]
Sarah Sachs
: Something to understand that’s really unique about notion. One of the reasons I joined we’re super lucky is no one uses Notion in their job as much as people that work at Notion.
[00:18:46]
Simon Last
: Of course.
[00:18:47]
Sarah Sachs
: So I think there’s very few companies, maybe if you worked on Chrome I guess, but like everything that we ship, we ship internally first and get a lot of really quick feedback. And also sometimes our dev instance is totally borked and you have to change a bunch of flags to get things done. And that’s kind of like, but everyone, so people that do it ticketing, people that do supply chain procurement, recruiting, everyone is using the same instance of notion with like a lot of flags on for these prototypes people build.
Um, and so we have this, Brian Levin, one of the designers on our team, I think evangelize this concept of demos over memos.
[00:19:18]
swyx
: Ooh, too
[00:19:20]
Sarah Sachs
: good. Um, which has been, uh, very good for building demos, and I think it’s put a big pressure point on us to have really strong product conviction, because if anything can be demoed, you really need a strong filter of making sure that if you know, you’re doing X amount of work, you’re making the, you’re, you’re focusing on one tower, you’re not just building a really flat hill.
Right. That’s actually where I think there has to be more conviction from our PMs, um, and our designers and, and well, the company really to have conviction of what journey we’re going on.
[00:19:52]
Simon Last
: But overall, I feel like it works pretty well. Like people, almost all the engineers have good enough taste to realize that like, this prototype doesn’t actually make sense in the product, or, or it does.
So it’s not that common that I would see a prototype. It’s like, oh, this makes no sense. Mm-hmm. It’s like, you know, people are doing reasonable things and, and, and then it’s just a matter of. Which things we build first and then often just, just figuring out how to turn it on and off. There’s our, in the, in our like experimental chat ui, there’s this, there’s probably like, like a hundred check boxes in there.
[00:20:22]
Sarah Sachs
: Kills me
[00:20:23]
Simon Last
: the things you could turn on and off.
[00:20:25]
Sarah Sachs
: Uh, but I think that, okay, so that is kind of true, Simon, but like being the person that manages the evals team, like there is a level of intensity that it adds to the platform team. So, you know, if we’re gonna do image generation and notion, all of a sudden the way that we do attachments and the way that we, um, our LLM completion like cortex talks and expects tokens back and now it’s getting images back.
Like there’s a lot of platform work that we do need to, like solidify a little bit. So sometimes it’ll be in dev for a couple weeks before it makes it to prod just because we still have to like, make it robust, make it HIPAA compliant, ZDR compliant, figure out the right contracting with the vendor, whatever it is.
And we need to eval it because we want the team. To still maintain what they build. That’s the one thing is like if we have a bunch of prototypes, it can’t just be like a small group of people that then maintain whatever end prototypes. So we have invested a lot of people in an eval and model behavior understanding teams that, we call it agent dev velocity.
So your dev velocity building agents can be faster if we invest in that platform. And so we have a whole org dedicated to Asian, um, platform velocity so that you can build your own eval and then maintain it once you ship it. So if a new model release comes out and we, every
[00:21:38]
swyx
: team maintains their own eval,
[00:21:40]
Sarah Sachs
: we maintain the eval framework.
Every team owns their own evals and a lot of them we’ve integrated to Optin, to ci, or we run them nightly and we have a team, uh, a custom agent that triggers to a team to look at the major failures. That’s really critical because if we have like all these different surfaces now, a lot of it’s on the same agent harness, so it’s easier to maintain.
It’s just packaging of different agent harnesses, but new functionality of the agent. Let’s say that like we wanna update like. Uh, you know, they deprecated, sonnet, um, four or whatever it is and we need to auto update. Are
[00:22:11]
swyx
: they already? That’s so, okay. Yeah. Actually wasn’t that long ago.
[00:22:14] Alsesio: They
were
[00:22:14] Alsesio: just 3.5.
[00:22:15]
Sarah Sachs
: 3.537. Just got deprecated.
[00:22:18]
swyx
: 3 7, 5 0.2 or, yeah. No,
[00:22:20]
Sarah Sachs
: it’s not. 5.2 is five point. Five point no. Yeah, five four is 40% more expensive than five two. So if they deprecated five two, you would hear they can, you would hear from me about that one. Um, but, uh, another conversation to have.
[00:22:35]
swyx
: I have a cheeky evals question for you.
Have you noticed any secret degradation from any of the major model providers?
[00:22:40]
Sarah Sachs
: Secret degradation,
[00:22:42]
swyx
: like. During the War Bay, when it’s high traffic, it suddenly gets dumber.
[00:22:47]
Sarah Sachs
: Yeah. I mean, not just between the, I mean, we definitely notice flakiness, we’ve definitely noticed, particularly for some providers, that things are slower during working hours and
[00:22:57]
swyx
: there’s a latency argument.
Yes. Not a quality argument.
[00:22:59]
Sarah Sachs
: No. I think the quality difference that’s interesting is, um, even though companies that say they’re selling the same, a, it’s really into like quanti quantization, but like companies that say they’re selling the same model through different vendors, whether it be through first party or Bedrock, Azure, et cetera.
We do see different qualities sometimes, and that’s not necessarily what’s advertised.
[00:23:21]
swyx
: Yeah. Kidney went to the point of like, if we, they shipped like this, like eval across all the providers and it was like very obvious we were secret equalizing and it was very,
[00:23:28]
Sarah Sachs
: yeah. But
[00:23:29]
swyx
: that’s very embarrassing.
[00:23:30]
Sarah Sachs
: You know, um, we hire Subprocess to figure that out for us.
So we just wanna understand where it’s regressing or where it’s optimized. And sometimes we’re okay with regressions that optimize latency if they’re the appropriate regressions. Our job is to make sure we have the evals to understand the changes that are important to us. And even like when we’re partnering with labs on pre-releasees of models, they’ll send us multiple snapshots.
And this is less about quantization, but more just regressions. Like they have shipped models that were not the snapshots that we wanted, and they have changed the snapshots that they shipped based on the feedback that we give. Because our feedback tends to be more enterprise work focused and not coding agent focused.
And definitely those can be bummers, like, you know, uh, we know that this wasn’t the version you wanted, but we’ll help you make it work. I mean, we always make it work, but that definitely happens.
[00:24:16] Alsesio: Yeah. Do you have, um, failing evals that you’re just hoping, oh, that will have success eventually when a good model comes out?
[00:24:23]
Sarah Sachs
: Uh, I mean, yeah. So I think. I mean, I could talk about this for 60 minutes, so I will limit myself. I think it’s a real issue when people say evals and it’s just like, that’s quality, that’s like unit, I mean, it’s like saying testing. It’s not just unit tests, right? So. We have the equivalent of unit test.
Regression test. Those live in ci, those have to pass a certain percent, you know, within some stochastic error rate. Then we have, as you’re building a product, evals of these aren’t passing right now, and this is launch quality. So we have a report card and we need to, on these categories, you know, be it 80 or 90% of all of these user journeys to launch, and then what we have what we call frontier or headroom evals, where we actively wanna be at 30% pass rate.
And that’s actually been a effort that we took in partnership with philanthropic and OpenAI in the past maybe two or three months, because we actually hit a point where our evals were saturated and we weren’t able to really give insightful feedback other than it wasn’t worse. And not only is that not helpful for our partners, it’s not helpful for us to understand where the stream is going.
You know, going back to that analogy. And so we spent a lot of time thinking about. What notions last exam looks like, right? Mm-hmm. Not just humanities, last exam. Ooh, notions last exam. Mm-hmm. And, um, there’s a lot of, you know, dreams about what that would look like. I know we’ve talked a lot about benchmarking, um, swix, but, uh, yeah.
Notions last exam is a big thing inside the company and we have people, full-time staff to it exclusively. Mm. We have a data scientist, a model behavior engineer, and an full-time, um, evals engineer just dedicated to the evals that we pass 30% of the time.
[00:25:56]
swyx
: What you’re hiring for
[00:25:57]
Sarah Sachs
: MBEs? I am hiring
[00:25:58]
swyx
: What is an MBEA
[00:25:59]
Sarah Sachs
: model?
Behavior Engineer Model. Behavior engineers started with a title data specialist before I joined when they were working with Simon on like, uh, Google Sheets and like Simon just needed someone to look through Google Sheets and say, yes, no, this looks bad. This looks good. Right? And so we hired people with kind of diverse linguistics background.
We had like a linguistics PhD dropout. Mm-hmm. And a Stanford ate new grad. And they’re amazing. And they formed a new function basically. And over time we’ve built a whole team, um, with a manager who’s now kind of reinventing what that role is with coding agents. So they used to be kind of manually inspecting code.
Now they’re primarily building agents that can write evals for themselves or LLM judges. There’s a really funny day I can send you the picture where Simon, about a year and a half ago, was teaching them how to use GitHub. Um, and they’re on the whiteboard and it was like, okay, I think it would be so much faster if our data specialists learned how to use GitHub and like learned how to commit these things in Dakota.
And, and that was then and now I think, you know, coding has been a lot more accessible. Um, but moving forward it’s this mix of like data scientist PM and prompt engineer because there’s craft in understanding like even like what models can and can’t do things. How do we define like that headroom? How do we define like what a good journey is?
Um, is this model better or not? Why is this failing? There’s some qualitative work, but then there’s also like a lot of instinct and taste to it, and that’s not necessarily software engineering. And so we have like very firm conviction and we have had for a number of years now that that is its own career path and we have always welcomed the misfits, so to speak.
So we really firmly believe that you don’t need an engineering background to be the best at this job. And that’s what’s quite unique about this particular role.
[00:27:37]
Simon Last
: Yeah, this is something that I’ve been pretty excited about recently is we made an effort basically to treat the eval system as like an agent harness.
So if you think about it, like, you know, you should be able to have an agent end-to-end, download a dataset, run an eval, iterate on a failure, debug, and, and then implement a fix. And ultimately you should be able to, you know, drive the full time process with a human sort of observing the, you know, the outer uh, system.
So yeah, we went, went pretty hard on that. And that’s, that’s worked extremely well so far. It’s like basically just to turn it into a coding agent, uh, uh, problem.
[00:28:11]
swyx
: Your coding agent or just whatever
[00:28:13]
Simon Last
: harness No coding agent. Yeah, code, cloud code. It should be totally general. Yeah. I think if it would be a mistake to like, like fix it on any, any particular coding agent.
At the end of the day, it’s just like CLI tools.
[00:28:21]
Sarah Sachs
: It’s like the same way that you would’ve a coding agent write the unit test. You should have a coding agent write the eval.
[00:28:26]
swyx
: Yeah.
[00:28:26]
Sarah Sachs
: But there’s a lot of supervision in that still. We just don’t believe that supervision has to come from software engineers because a lot of it is like, um, kind of you XREE and whatever, and these are the people that also triage failures and tell us where we should be investing next.
[00:28:40]
swyx
: Yeah. I’m gonna go ahead and ask a spicy question. Is there a data, there are no software engineers at Notion.
[00:28:46]
Simon Last
: Um,
[00:28:46]
Sarah Sachs
: what does it mean to be a software engineer?
[00:28:47]
swyx
: Exactly.
[00:28:48]
Simon Last
: I mean, I think the way things are going is like we’re on some continuum where. If, if you look back three years ago, humans were typing all the code and then we had auto complete, you’re typing list of the code.
Then we had sort of like filling agents, filling lines, and now we’re getting into like agents doing longer range tasks where you can debug and implement a fix and then verify it works and you know, get your, get your PR even like, like Merion deployed. I think we’re sort of just moving up the abstraction ladder and then the human role becomes more about observing and maintaining the outer system.
There’s a string of agents flowing through, like me prs what’s going off the rails. Like what do I need to approve? Is there like a learning or memory mechanism that that works? So it’s kind of a hard engineering problem. There’s a, you know, there’s, there’s a lot to do there. I think we’re just sort of moving up stack
[00:29:34]
Sarah Sachs
: the same transition machine learning engineers have made, right?
Like I haven’t looked at a PR curve in a while.
[00:29:39]
swyx
: Yeah. You used to do this stuff and now, um, auto research can do it,
[00:29:42]
Sarah Sachs
: right? Like I think it depends on what you define as a software engineer.
[00:29:46]
swyx
: Yes. It’s, that’s changing for sure.
[00:29:49]
Sarah Sachs
: I think every software engineer in notion this summer went through like this, um, sheer, um, one of our engineering leads of the company called it, like every software engineer is going through the, the, uh, identity crisis that every manager goes through, where all of a sudden they realize their ability to write code is less important than their ability to delegate in context switch.
And I think that is a transition out of being a software engineer. But
[00:30:12]
Simon Last
: yeah. Yeah, there’s a critical difference to being a manager, which is that like, it is actually very deeply technical. The problem, you know, humans are very like, like, like fuzzy and you can’t like treat a team of humans like a, like a rigorous system where like, you know, prs like, like flow through and can be in like a block status and then what happens when they’re blocked, right.
With a set of agents, you actually can do that. And, and, and I think it’s actually, there’s a lot of interesting technical rigor that that goes into that it’s like it’s a technical design problem. Ultimately.
[00:30:42] Alsesio: What is the design of the software factory that you’re building?
[00:30:46]
Simon Last
: Yeah, I mean, I think we’re. Trying a lot of different things.
I mean, ultimately you want to design a system that requires as little human intervention as possible, but like still maintaining the in variance that, that you care about. So yeah, we’re exploring a lot different ideas there. I mean, I think I could talk about a few things I think are important there.
Like, one thing I think is really important is, um, having some kind of like specification layer you can just commit marked on files. Mm-hmm. That works pretty well, but
[00:31:15]
swyx
: it’s nice to be notion man. I’m just saying like the spec, like Yeah. The natural home for specs is notion.
[00:31:21]
Simon Last
: Yeah. Right. It can be a database of pages.
Yeah. I mean, it needs to be something that is, you know, human readable and I viewable and I think that’s pretty key. Another really key component is like the, the self verification loop. Yes. You need really, really good testing layers, basically. And that’s a really deep, uh, uh, problem. But by getting that right, you know, and then, and then it’s kinda like the workflow of like.
What happens when there’s a bug? How does it flow into the system? Like, is it like a subagent working on it? How does it make a PR and how does that get reviewed? And me, and then, you know, so there’s like the, the flow or process.
[00:31:56]
swyx
: Yeah. Cool. Uh, you know, one thing we did work out before you guys came in was this demo or this
[00:32:01]
Simon Last
: agents
[00:32:02]
swyx
: agent demo.
Uh,
[00:32:03]
Simon Last
: so every,
[00:32:04] Alsesio: every time we do an episode, we try the product. Right. I don’t think there’s ever been an episode that I haven’t tried. Yeah. Um,
[00:32:11]
swyx
: and we, we try, try is a, a big word. Like since day one lane space has been on Notion, but this is the, this is the net new thing. Yes.
[00:32:18] Alsesio: So this is for Nel Labs, which is the space we’re in.
So next week we’re opening applications for tenants. So there’s a web form, let me, we got this form done here. Uh, so, uh, before. Uh, the workflow would be I get an email, then I look at the person. It was like, should I spend time talking to this person? Then I respond, they respond back. So I build this. So the name it came up for on its own.
Can you maybe h how do, how does it come up with its own name?
[00:32:43]
Simon Last
: Yeah, that’s a pretty app name. It’s, it, it is just a random, it’s a random, a name generator.
[00:32:47] Alsesio: Oh, that’s funny. It just came,
[00:32:49]
Simon Last
: the fact that it picked that is, is kind of hilarious. I’m pretty sure it’s just determined,
[00:32:54]
Sarah Sachs
: resilient collector. I, I think I’ve never looked at the code for that.
I’ve never second guessed it. I think it’s kind of like a madlib situation.
[00:33:00]
Simon Last
: Yeah, I think you’re right. Yeah. It’s, it’s totally a, a deterministic. Oh, I thought it was great. Yes. Although, although when the, if you use the AI to set itself up, it can update its own name, so. Okay. Um,
[00:33:11]
Sarah Sachs
: how did you create it? It, did you just do
[00:33:12] Alsesio: classroom?
I,
[00:33:13]
Sarah Sachs
: okay.
[00:33:13] Alsesio: I did, yeah. I’ll say just check my inbox for applications for a coworking space. Keep a people, so it created the database for me. Which I have here. And I guess database is like an notion table because everything is notion. Um, and then whenever um, an email comes in, like here, it just creates a new role for the person.
Mm-hmm. And then it uses web search to enrich the mm-hmm. The profile. So it kind of like searches the web and it’s like, this is who this person is, this is when they say they wanna move in and kind of updates everything else. This is, I mean, it’s not a GI, but to me, I don’t wanna do this work. So it feels like, I mean, it took me maybe like 15 minutes to set up the whole thing.
Um, and I really like that most of the information should live here. You know, it is not like some other tool asking me
[00:34:01]
Sarah Sachs
: Yeah.
[00:34:01] Alsesio: To like, bring my stuff there. It’s like I would’ve probably already created an ocean thing.
[00:34:06]
Sarah Sachs
: Mm-hmm.
[00:34:06] Alsesio: So
[00:34:07]
Sarah Sachs
: most of our biggest use cases and gains are from. That extra layer of human involvement in the process to make it so right.
And so like one of our biggest use cases is bug triaging. So if someone posts something in Slack, can you just have a custom agent that lives there that has its own routing constitution of what team this belongs to, creates a task in your task database and then posts in that Slack channel, right? Like that’s like one of the first things that we built internally, I think.
And it’s completely changed the way that notion functions as a company. Nothing falls through, well, most things don’t fall through the crack. We don’t know what we don’t know. But it’s not replacing people, it’s replacing processes.
[00:34:44] Alsesio: Yeah.
[00:34:44]
Sarah Sachs
: Right.
[00:34:45] Alsesio: And I’m curious how you think about composability of these things.
So the other one I was working on is like a. These filler. So whenever somebody signs up as a tenant, kind of he’ll sell the lease for them. There should probably some agent that is like office manager agent mm-hmm. That can handle the request, make the lease, and then, uh, give them a ADA access to the office and all of that.
How do you think about that feature?
[00:35:08]
Simon Last
: Yeah, so I mean, there’s, there’s two ways you can compose. One way is by using like the data primitives. So you can, you know, you, you could give, you have one agent, uh, be writing to the database and there’s another agent that’s walked in the database. So that’s, that’s one way that they, they can coordinate that’s like a little bit more decoupled and mm-hmm.
Works really well. Or you, you can couple them. So I, I think it’s actually not released yet. Releasing it like next week is, uh, in the settings for an agent, you can give access to invoke any other agent.
[00:35:34]
swyx
: Hmm.
[00:35:34]
Simon Last
: So you can have them just. Just, uh, uh, talk directly. So
[00:35:37]
swyx
: you, was there a limit on like, number of recursions or just,
[00:35:40]
Simon Last
: um, probably,
[00:35:42]
swyx
: you know what I mean?
Like, you can just get an infinite loop that way there’s
[00:35:45]
Simon Last
: some kind of Yeah,
[00:35:46]
Sarah Sachs
: I think it’s, there is actually a number somewhere.
[00:35:49]
swyx
: I believe I’m just, you know, like, you’re, you’re, someone’s gonna screw up. You
[00:35:51]
Simon Last
: should you try to see
[00:35:53]
swyx
: Yeah. I mean, everything’s gonna be paperclips.
[00:35:55]
Simon Last
: Oh, yeah. Yeah. But, uh, but, but that’s really useful.
Yeah. So we, you know, like I just, I, I helped, uh, someone internally the other day, they had, they had built like over 30 custom agents for, uh, for our go to market team doing all kinds of different things. You know, for example, like researching, you know, like, like filling information about, about a customer or like, like triaging customer feedback or like, uh, something like that.
Literally over 30 of them. And, and then he, and then he even made like a database of all the agents and then he is like, okay, and, and now I’m getting 70, over 70 notifications per day with just the agents are blocked on various things. Uh, and then I was like, oh, okay, cool. You know, the obvious thing to do there is to make a manager agent,
[00:36:32]
Sarah Sachs
: right?
[00:36:33]
Simon Last
: That’s gonna sort of blocks be another abstraction layer in between your, your, uh, uh, 30 agents. Uh, so yeah, we, we send out with like a manager agent and then has access to invoke all the other agents and it’s sort of like, like watching and observing them and then it sort of, it just creates a layer of abstraction.
So instead of 70 notifications per day, it’s like, like five. And then, and then the manager agent can help like, uh, debug and fix any problems with the,
[00:36:54]
swyx
: does this is a concept of like an inbox or something like piece, you’re basically saying that they can message each other?
[00:37:00]
Simon Last
: Yeah.
[00:37:01]
Sarah Sachs
: Well
[00:37:01]
swyx
: they use the system of record, which, which is
[00:37:02]
Sarah Sachs
: notion, so we
[00:37:03]
Simon Last
: actually, yeah, we didn’t make any special concepts at all.
[00:37:06]
swyx
: They’re interested to the motion notifications that I would’ve got,
[00:37:09]
Sarah Sachs
: they can just like write a task to a database that the other agent’s task to listening to, or they can actually call a web book to the agent, like they can just add the agent. Okay.
[00:37:17]
Simon Last
: Yeah, I mean, this is something that, that we’re still working on.
I, I think we, you know, like, like generally, generally the way we do these things is, you know, you first make it possible, maybe like a sort of janky way. So I, I, I think the way I set ‘em up is like, you know, we created like a new database that was sort of like issues mm-hmm. That the custom agents were, were experiencing, and then gave them all access to file an issue and then the manager has access to, to read the issues.
Um, and that works pretty well, essentially like, like give it its own like internal issue tracker just for the agents. And then, you know, if that becomes a, a concept that seems useful, generally maybe we will think of how to package it in. But I mean, generally we try to just keep it to composing the primitive if we can.
You know, another example of this is we have no built-in memory concept. Memory is, is just pages and databases. And so if you wanna give a memory, just give it a page and give it. Edit access to that page and the
[00:38:03]
swyx
: human can edit it. Agent can edit
[00:38:04]
Simon Last
: it. Yeah. And so that works, that pattern works extremely well on it.
And you know, depending this case, you can have it be just a page or it could be an entire database with, you know, or, you know, I can have sub pages is is pretty on what you can do with that.
[00:38:15] Alsesio: So when I was setting this up, uh, I connected my inbox and it was like, do you wanna use Gmail or Notion Mail? And I’m like, I don’t wanna use Eater, I just want you to do it.
I’m curious how you think about, you know, notion, mail, notion, calendar, all of these kind of ui ux interfaces, full stack
[00:38:29]
Simon Last
: notion.
[00:38:30] Alsesio: Yeah. When like at the same time you have the agents abstracting them away from you in a way, you know, how do you spend like the product calories so to speak?
[00:38:37]
Simon Last
: Yeah, I mean, I think it’s pretty important that you don’t have to use, not your mail to connect to the mail capability.
So we can just connect to Gmail or, or whatever you want, uh, to use. And we’re thinking of the mail service as being really great to the extent that it’s really agent built, right? So maybe the mail app is just sort of a prepackaged agent that helps you automate your, your inbox.
[00:39:00] Alsesio: Yeah, the auto labeling is great.
Think
[00:39:03]
Sarah Sachs
: the, when we, um, integrate with Gmail for instance, we have a series of tools available that are available via MCP or API to Gmail. When we integrate with Notion Mail, we have the Notion Mail engineering team to build us the, um, exact right tools that optimize latency, optimize performance and quality.
They own that quality. Um, there’s product leads there. They’re directly thinking about the user problems that happen in mail. So it tends to be when we build integrations and connections, we build natively first. Um, and then think about, um, extending them generally just because it’s also easier. Mm-hmm. Um, um, to build natively first.
Um, so that tends to be how we phase things out.
[00:39:43]
swyx
: Talking about integrations, you prompted me, so I gotta ask. M-C-P-C-L-I. What’s going on? What’s the
[00:39:48]
Simon Last
: Yeah. Opinion. I think, I mean, I’m, I’m definitely bullish and excited about cli. I think there’s a few really cool things about cli. So one really cool thing is like, um, is that it’s in the terminal environment, so it gets a bunch of extra power.
So it, you know, for example, it can like, like paginating and cursor through like long outputs. Um, and it has a progressive disclosure inherently. Uh, so, you know, you don’t see all the tools at once. It’s just, you see the CLI wrapper and you can like use the, the help commands and, and, and read files. And then I think the most important thing that’s, that’s super cool is that there, it’s also inherently a, a bootstrapped.
So if there’s an issue, uh, the agent can debug and fix itself within the same environment that it uses the tool.
[00:40:30]
swyx
: Mm.
[00:40:30]
Simon Last
: Right. Like, you know, I think I saw a tweet this morning. Someone said, you know, my agent didn’t have a browser, so I asked it to make all a browser tool and within a hundred lines of code, it gave itself a little browser, like, like wrapping the, the, the chromium API, um.
That’s pretty incredible. And then if there was a bug, it would just immediately try to fix it. Mm-hmm. Right. On the other hand, if you use an, you know, if you use like of, of the Chrome dev tools, MCP, I’ve had this issue where like, like sometimes the transport gets like messed up. If it gets messed up, the agent has no way to fix itself.
It, it no longer has a browser, it’s, it’s not broken. Right. I think that’s, that’s pretty fundamental, but I would say like a lot of the, the bad things about it can be fixed. Uh, so I think like, as a progressive disclosure, that can be fixed with, with right harness. Like, it, it obviously doesn’t make sense to show it all the tools all the time.
That’s not really inherent to the MCP protocol. It’s just like how you wrap it and use it.
[00:41:16]
swyx
: There’s many poorly built MCPs because we didn’t know.
[00:41:19]
Simon Last
: Yeah, yeah. I mean it was just early, like, like the obvious thing is, uh, you know, to start with is, is to just show it all the tools and it’s like, okay, now we have a hundred tools.
Yeah. And like the tool calling actually works. So let’s of
[00:41:28]
swyx
: your success
[00:41:29]
Simon Last
: give it a way to like, like filter to source the tools. So yeah, I would say like broadly speaking, I’m really bullish on cli. I’m still bullish on CPS and in a certain environment. I think in, in particular, CP is really great for when you want sort of like a narrow, lightweight agent.
I think there’s, there’s definitely a lot of use cases where, where you don’t want like a full coding agent with a compute run time. And also you want it to be like more tightly permissioned. MCP inherently has a really strong permission model, like all you can do is call the tools. A CLI is a little bit murkier.
It’s like, can I access the, if PI token are you, like, properly sort of like re-encrypt the token so it can’t like exfiltrate it, it introduce a lot of like, like new issues, which are. Real and hard to solve. And MCP is just like the dumb simple thing that works and it that it’s pretty good.
[00:42:12]
Sarah Sachs
: I’ll add two more perspectives, not from it working well for Notion, but how notion like commits to both platforms.
Notion is dedicated to being the best system of record for where people do their enterprise work. So we will always support our MCP and so far as other people are using cps, right? So regardless of our perspective, we’ve put a lot of effort into our MCP and we have a fantastic team that we’re building, um, to do more there.
And the second thing I’ll say, I think, um, we all think a lot, but lately I’ve been thinking a lot about making sure there’s a value alignment and pricing, um, with capability.
[00:42:43]
swyx
: Literally our next question
[00:42:44]
Sarah Sachs
: and. Needing language to execute deterministic tasks feels wasteful and requiring on a language model to interface with third party providers seems wasteful for tasks that don’t require it.
And particularly because our custom agents are using usage-based pricing. We think of pricing as like the barrier of entry for use of our product, and we’re quite committed to making sure that it’s not wasteful. Um, not just because it’s a bad deal for our customers, but it’s also bad business. We wanna have as many buyers, like there’s a, there’s an elasticity of demand and so if we can have our agents properly execute code that calls on CLI deterministically, it’s a one-time cost, right?
Versus constantly having a language model integrate with an MCP over and over and over and paying those like repeated token fees and it’s happening outside the cash window, then you’re paying for it over and over and over and it’s just kind of unnecessary and less deterministic when it doesn’t have to be.
[00:43:36] Alessio: Yeah, the open-endedness I think is like, the main thing is like, well, if I go write code to just call an API, I would never use an MCP. But then you need an NCP sometimes when you know what to call, but you don’t want it to restart versus like, I think the it built a browser from scratch is like, it’s great when you’re doing it on your own, but like if your customers were having your AI write a browser from scratch every time and you had to pay the token cost of that, yeah.
You’d be like, no, no. The Chrome dev tools CP is actually pretty great. Just use that. I’m curious, how do you make that decision? Like should it be. Just straight API call very narrow. Should it be an MCP? Should it be super open-ended?
[00:44:10]
Sarah Sachs
: Do you mean for when we ship notion capabilities or when we add capabilities to
[00:44:13] Alessio: notion
[00:44:14]
Sarah Sachs
: AI or,
[00:44:14] Alessio: I mean, you might have a capability that the only way to do is an open-ended agent, like an agent with a coding sandbox.
[00:44:21]
Sarah Sachs
: Yeah. In Notion ai they’re not explicit, not We also ship an MCP.
[00:44:24] Alsesio: Yeah. Yeah. In B,
[00:44:25]
Sarah Sachs
: yeah.
[00:44:26] Alsesio: Internally. Okay. Like is there ever a discussion of like, we’re not gonna ship it because we’re not able to tie it down? Or are you happy to just like,
[00:44:33]
Sarah Sachs
: um, no. I mean, there are a lot of things where we choose not to use MCP because we wanna add more high touch to quality.
I think search an agent to find is like the largest instance of that, where we have. Um, slack and linear and Jira search and notion that is not using necessarily the search MCP functionality that is provided by those companies. And that’s because it’s quite critical we think, to how our agent trajectories work is for us to have a little bit more control on the functionality of the search journey.
And so it usually comes from quality and there’s a long tail of things and that’s why we built an MCP client or an MCP server, excuse me, so that people can connect whatever they want. There’s that long tail, right. But we, for search particularly, I would say that’s like the primary entry point, but there are other connections as well that it’s a little bit of secret sauce about when we are okay with like MCP functionality and user driven off.
And when we actually want to wanna carry a lot more ourselves.
[00:45:31]
Simon Last
: I think that there’s not really a conflict here. There’s just like different layers of the stack and different abstractions. I mean, if we were to like map it out, it’s like, you know, you’ve got CPS give you a, a way to, it’s a protocol for gaining access to tools.
It’s an open protocol, so you can, you can easily get like a long tail, many things. So if you open up our, like in the tool settings, oh, that’s saw the trigger. Actually, actually, that’s something that MCP can’t do. So if you scroll down and you, and yeah. The, the tools and access, so you’re gonna a connection.
Yeah. MCP is a really great way to gain access to tools or really well, but you just looked at the, the trigger why, for example, there’s no trigger protocol. And so those are things we had to build ourselves. And then there’s, there’s some integrations where we use MCP. Like, so for example, I think the, you know, the linear and the GitHub
mm-hmm.
[00:46:20]
Simon Last
: Use M ccp, but, but the Slack mail, er, those are actually ones they built in house. And we spent a lot of time really fine tuning all the tools to make the really good and also like building out the triggers. So it’s just like different layers of the stack. Some things make sense sometimes. And then, you know, we just have to like, like harness the right tool at the right time.
I don’t think there’s an inherent like. Strong conflict between these things.
[00:46:40] Alsesio: Do you have a canonical representation of these tools internally where like you wrap these things together, the MCP plus, the custom built?
[00:46:46]
Simon Last
: Yeah. Yeah. We have like internal abstractions for like what is a tool, what is an agent, what is a completion call?
Yeah.
[00:46:55]
Sarah Sachs
: We even have internal obstructions for like, what is a chat archetype, whether it be from teams or Slack.
[00:47:02]
swyx
: Yeah.
[00:47:02]
Sarah Sachs
: Right.
[00:47:02]
swyx
: It’s like the only
[00:47:03]
Sarah Sachs
: way a to
[00:47:03]
swyx
: build with, with ai ‘cause everything’s moving so quickly, you would have to attract it so that you can swap things up.
[00:47:09]
Simon Last
: Yeah. I mean, there’s always a dance.
We, we probably rebuilt our, our framework like, like I said, like, like five different times. Um, it’s always a dance of like, okay, how does this new thing work? Right? What should the abstraction be? Like, what is OpenAI giving us? What is that therapy giving us? Um, you know, like we’re trying to wrap over it. I think.
I think we’ve been pretty successful with that. It, it’s just a matter of like, like staying nimble. Yeah. And making sure that you always have like the simplest, dumbest obstruction you can, that you know, that the maps are different things. Yeah. So, so we have like a tool integration abstraction, for example.
And then MCP is like a, a type of integration.
[00:47:41]
swyx
: Yeah.
[00:47:42]
Simon Last
: That’s, that’s one of the,
[00:47:43]
swyx
: this might be a big ask, uh, um, but I’m gonna try, uh, which is, you said, you’ve said multiple times, you rebuild a few times, like five times through, I don’t know if the, what the right number is. Is there like a brief history of what was the each rebuild doing and Yeah, I know it,
[00:47:56]
Simon Last
: I can try to do that.
I
[00:47:57]
swyx
: mean,
[00:47:58]
Simon Last
: yeah, there’s
[00:47:58]
swyx
: interesting, you need, you need to rag over
[00:48:00]
Sarah Sachs
: archeology.
[00:48:00]
Simon Last
: I mean, the first version, the first version that we started building in like late 2022. Oh my gosh. Well, there’ve been many versions actually. Okay. Well the writers, the,
[00:48:08]
swyx
: I like the highlights. The,
[00:48:09]
Simon Last
: the
[00:48:10]
swyx
: like,
[00:48:10]
Simon Last
: oh
[00:48:10]
swyx
: wow.
[00:48:10]
Simon Last
: I mean the, the first version we built was actually a coding agent.
Yeah. So we’re like, oh, instead of building tools, let’s make everything be JavaScript and then we’ll just give it JavaScript APIs and we’ll just write code. And that’s how it speaks to the tools. Um, but at the time. It just sucked at writing code. It wasn’t that good. Uh, so then we moved to, uh, more of like a tool calling obstruction.
A tool calling didn’t exist yet, so we created this whole XML mm-hmm. Of representation. And a big, a big learning in that version is we were catering way too much to what made sense for notion and notions data model versus what the model wants. So as an example, we created this whole, uh, XML, uh, format that can losslessly mapped in notion blocks.
And the transformation between them is super easy to do. Uh, and then we created this sort of like mutation operations to, to add to pages. Um, but it sucked because the model didn’t know the XML format and also the, and you have to prompt it
[00:49:04]
swyx
: in and
[00:49:04]
Simon Last
: Yeah, to prompt it in and the team just more convenient.
And so yeah, we’re like, okay, well it has to be marked down. Uh, uh, the model’s no markdown, you know. So, uh, we did a whole project around basically, uh, uh, creating a notion flavored markdown where, uh, you know, the whole goal was like, it has to be just simple markdown at the core, and, and then we can add some enhancements.
And it doesn’t have to be a, a full lossless conversion. That was a big one we did. And, and then we did a whole similar learning to, uh, the, the database layer. So, so to query a database, I mean, in the notion API, the way you query a database is there’s a crazy JSON format and it’s, you know, kind of limiting, but it maps nicely to like how we represent things internally.
We scrapped all that and we’re like, okay, let’s just make it SQL light. Everything is a SQL Light database. You, you can query it just like a SQL light query. And the models are super good at that. So
[00:49:51]
swyx
: give the models what they want.
[00:49:52]
Simon Last
: That was another one. Yeah. Yeah. Give us what they want. I mean, that was, I would say that was a big learning is just, you know, really be, be savvy and really careful thinking about what the model wants in terms of, you know, its environment and, and, and cater around that.
And really try so hard not to expose it to any complexity about your system that, that’s unnecessary.
[00:50:12]
swyx
: Notions underlying database is Postgres, right? Not sql, right? Yeah. So I don’t know if there’s any mismatch there.
[00:50:18]
Simon Last
: That one was kind of a fortuitous thing because we actually already, um, had a big project, uh, going where, so, so we have this, um, when you query Notion database, it’s actually querying this like, uh, cluster of SQL databases.
[00:50:34]
swyx
: Mm-hmm.
[00:50:35]
Simon Last
: That’s something that we’d already been working on even before the agents came around.
[00:50:38]
swyx
: Yeah. You know, you guys had a fantastic blog post about it and like it’s, it is actually a really good database engineering knowledge to have that from you guys because where else would we get it?
[00:50:47]
Simon Last
: Yeah, yeah.
It’s a, it’s, it’s a crazy engineering problem when you want to have like millions and billions of tiny databases or where, where some of them are tiny, but some of ‘em are, are very large and want everything to be very fast.
[00:50:57]
swyx
: Yeah. And also like, not that hierarchical sometimes, you know, uh, so somewhat of a graph.
[00:51:02]
Simon Last
: Mm-hmm.
[00:51:03]
swyx
: I do like that history because I think that shows the evolution that you guys went through and the work that went into it,
[00:51:09]
Sarah Sachs
: that he just ended you a year and a half ago.
[00:51:11]
swyx
: Oh, okay. Okay. Oh,
[00:51:13]
Simon Last
: I need to, I need
[00:51:13]
swyx
: to hit continue.
[00:51:14]
Sarah Sachs
: If you’re curious. I mean, we can keep going. Just saying like, that’s really,
[00:51:18]
Simon Last
: that’s another one.
Yeah.
[00:51:19]
Sarah Sachs
: I lemme think. Well, no. ‘cause there was tool calling and then there was research mode, which wasn’t a fully agentic tool calling. Um, then we moved away from few shot prompting entirely to tool definitions. Um, and now we’re thinking about Agent 2.0.
[00:51:34]
swyx
: So no fusion prompts ever. Right.
[00:51:35]
Sarah Sachs
: Uh,
[00:51:36]
swyx
: okay. No, maybe not.
[00:51:37]
Sarah Sachs
: I know never, but
[00:51:38]
Simon Last
: yeah, that kind of went away. It’s an interesting thing,
[00:51:40]
swyx
: right?
[00:51:41]
Simon Last
: Yeah. I mean, so
[00:51:41]
swyx
: these just instruction follow really well,
[00:51:44]
Simon Last
: I would say if there’s been like a general arc where, you know, it’s like you gradually strip away everything. And it, it looks more a GI like. And so, you know, it it, it started out as like, it’s a one shot, one prompt.
There’s a few shot examples. And it became like, okay, actually let’s give it, let’s give it tools, but it’s still a few shot examples. And then it became actually like, no, no, no, let’s just give it a whole bunch of tools. One big, big shift that, uh, that we I’ve been working on recently that’s about to ship is, um, you know, what happens when you have a lot of tools?
[00:52:13]
swyx
: Yeah.
[00:52:13]
Simon Last
: So then tool search. Yeah. So then a, a progressive disclosure becomes really important. So, you know, we were, we sort of hit a bottleneck where our, our agent worked really well. Um, we hit a bottleneck where, um, it, it, it became pretty hard to. Add new tools. Mm-hmm. And we, and we became sort of worried about it, like, like breaking the model.
It’s like, okay, someone No, I
[00:52:32]
Sarah Sachs
: just heard it was like saying hello was like thousands and thousands and thousands
[00:52:35]
Simon Last
: Yeah.
[00:52:35]
Sarah Sachs
: Tokens. It was really slow.
I
[00:52:37]
Simon Last
: can see you’re the efficiency person here. Yeah. It’s, it was too many tokens. But also it’s a quality issue because it meant that like any engineer could introduce this, this new tool for some like, like niche feature.
And it would kind of like, like Nerf, the overall model by like causing it to call the tool too much and stuff like that. And so, um, it, uh, yeah, so we, uh, we had an effort basically to, to make our harness. Uh, implement progressive disclosure in, in a nice way. Um, that’s a big shift.
[00:53:00]
Sarah Sachs
: You said earlier, like everyone says reasoning models was the big shift.
Like what’s more there? When we went away from few shots to describing the goal of the tool in like goal-driven, basically moving from a DAG to like a, a true system with feedback, that’s something we could distribute tool ownership to the teams. Much better because when it was all few shots, it was everyone truly editing one string and things would o would compete.
And like the order, there were all this, all these papers about, oh, you know, not all context is created equal. The higher up it is in your examples, like the more the model listens and we’re trying really hard to like fight against the order and the selection of the few shot. And that really had to be a center of excellence and it didn’t scale with the number of people for the need the company had.
It was really just five or six people that were allowed to even touch that or had to approve it rather in our code base. And then now we can actually, with the right eval, setup, distribute, um, so that everyone owns their tool and their tool definition. And sometimes we have crazy things where like we write two tools that have the same title and the agent crashes and stuff like that.
So like, you know, there are issues actually, believe it or not, um, Andro couldn’t take it. Sonic couldn’t handle two tools with the same name and open AI GPT five point. Two, it was like, I can figure this out. So that was an interesting one that we learned by accident through a, a sev.
[00:54:17]
swyx
: But I mean, then, you know, the underlying representation is that’s a addict, right?
Clearly. Like that’s a safety. Yeah,
[00:54:23]
Sarah Sachs
: exactly. Exactly. Um, but so that was like a big shift for the company and velocity not immediate because the AI team that was the center of Excellence team that owned, you know, that one file of few shop prompts had to become a platform team overnight, and that wasn’t natural.
Yeah. Yeah. But I would say that in terms of like the velocity of how we contribute to the agent, beyond coding tools, obviously being a big velocity lever, um, being able to distribute tools and not have to all collaborate on like one very select string of system prompt is truly, I would say the biggest lever on how we’ve scaled.
[00:54:57]
Simon Last
: We’re fighting to keep the prompt as short as possible now and then, yeah. Yeah. It’s, uh, in the latest version of the agent, I, it’s not in custom agents yet, but it will be like, like next week, a week after or so, um, there’s now like over a hundred tools. Just for all, all the crazy notion stuff. So we’re able to, to really go deep and like,
[00:55:11]
swyx
: would you list those tools publicly?
Is this like IP or, uh,
[00:55:15]
Simon Last
: no, no, no. It’s, it’s totally public. You can ask,
we
[00:55:17]
Sarah Sachs
: can fine
[00:55:19]
Simon Last
: just ask. You can just ask the agent and, and we’ll tell you.
[00:55:21]
swyx
: I find,
[00:55:21]
Sarah Sachs
: and we’re gonna post a bench. I mean, like you’re
[00:55:23]
swyx
: post bench.
[00:55:24]
Sarah Sachs
: We don’t think our system prompt is our secret sauce.
[00:55:26]
swyx
: Yeah. Mm-hmm.
[00:55:27]
Simon Last
: Great. We don’t try to hide the tools at, at all.
I think it’s, I think it’s kinda important actually as an operator, you know?
[00:55:32]
swyx
: Yeah. As a power user, I wanna be like, oh, I can do this, this, this. Great.
[00:55:35]
Simon Last
: Yeah. Yeah. I mean, one thing that, one phrase we say internally in lot is to, to teach at the top of the class. You know, we wanna build like, like the customization’s, kind of like a power tool.
I mean, we try to make it as easy as possible to set up, but we want it to be pretty deep and sophisticated. And I think a huge part of that is the operator needs to be able to interrogate. The way the system works. And a big part of that is like, what are the tools? How do they work? You know, like, like how should I prompt it to use the tools in the right way?
[00:56:00]
Sarah Sachs
: I’d actually say we don’t try and make it as easy as possible to use. ‘cause the more we do that, the more we abstract away that interpretability, that Simon’s talking about, that basically nerfs the model or nerfs the agent from being super capable. So a huge. I would say turning point, I can think about like the week and a half that we all came together on this as we were building custom agents, was that alignment that we’re not trying to build for everyone here.
We’re not trying to build the model that, um, or build the user experience that anyone can figure out how to use. ‘cause the more we do that, the more we just diminish its capabilities. And that was a big, you know, everyone in a couple Slack messages aligned on that, that actually made us all work faster again.
Right? ‘cause we all were like more centralized on who we were building for
[00:56:40] Alsesio: what does the meta prom generator look like? So I looked in the system prompt that it, gen, for example, uses emojis. That’s not a, you know, obvious thing to be doing.
[00:56:50]
swyx
: Wait, did you just
[00:56:51] Alsesio: ask it? What’s your system prompt? Oh no. This is how to generate prompts.
[00:56:54]
swyx
: The
[00:56:54] Alsesio: prompts generate prompts.
[00:56:55]
Sarah Sachs
: We call it set. Then it’s
[00:56:56] Alsesio: a set.
[00:56:56]
Simon Last
: Well, well, so this is actually just the agent. So, so one thing we did that, that I really like with the custom agents is it can set itself up. So we not only give it access to use the tools than it has access to like send your emails or whatever, um, but it has more tools to set itself up and to debug itself.
And so when you ask it to write system prompt, it’s just your agent itself is doing that.
[00:57:16] Alsesio: So this is just the model preference. You’re not really injecting and then into the model too much.
[00:57:21]
Sarah Sachs
: No, no. We haven’t guide the same thing. Makes a good custom agent and Yeah.
[00:57:23] Alsesio: Yeah.
[00:57:24]
Sarah Sachs
: And things like that. And then, and, and it’s really nice too because like if it fails, you can ask it, why did it fail?
And then say, okay, update your instructions so it doesn’t fit again. Obviously we should build product of self-healing that’s, that’s next on our roadmap. But um, it actually, it creates a nice system.
[00:57:40]
Simon Last
: Yeah. We do essentially give it like a development guide. Here’s, you know, here’s how to make a custom agent.
Here’s how to like, like help the user test it end to end, you know, to, to help them gain confidence that it works. Stuff like that.
[00:57:49] Alsesio: Mm-hmm. Yeah. Yeah. The fixing thing work, I mean, it wasn’t automatic, but I, I miss set something up and then there works like a fix button and then just, yeah,
[00:57:58]
Simon Last
: yeah, yeah. One thing where
[00:57:59] Alsesio: fix agent makes more,
[00:58:01]
Simon Last
: it’s, it’s actually, it’s an interesting sort of permission problem.
So like, right. The thing about custom agents. That is that by default it has no permission to do anything and then you have to explicitly grant it all its permissions and that’s what lets you trust it can work in the background. Right? Like you can know like, oh, it, it can read my email but not send email.
Okay, I can trust that. Right. If you let it fix itself, you know, you’re, you’re breaking that, that version there, it, it is not allowed to edit its own permissions. But as, so, you know, in the current product you can sort of click a button to fix, but now you’re entering sort of an admin mode where, where, where you’re in a synchronous chat and, and you can, and you can see what it’s doing.
[00:58:35]
Sarah Sachs
: Yeah. And it, and it confirms before it
[00:58:37] Alsesio: changes.
[00:58:37]
Sarah Sachs
: Yeah.
[00:58:37] Alsesio: The thing that I really like that most people don’t do is like, the editing chat is the same thing as the using chat. Like you can message the agent to both edit it and use it, versus a lot of other products are like, I think
[00:58:49]
Simon Last
: that’s really key. I think, I
[00:58:50]
Sarah Sachs
: think a lot of designers will feel so happy you said that.
Yeah. ‘cause we spent, we, we call this flippy, um, uh,
[00:58:55]
Simon Last
: yeah. What is
[00:58:56] Alsesio: this?
[00:58:56]
Sarah Sachs
: What do you mean? This,
[00:58:57]
Simon Last
: this view of, well, yeah, so if you sort of, if you close that in like open settings, you can see sort of Yeah. This is, we. We call it flippy because you know, we started with sort of like the settings were the sort of the main page and then you can test the agent.
The a GI pill way to think about it is like, oh, it is just the agent. Everything’s the agent, right? It can set itself up, it can test itself and it can run the workflow that they want to run. Uh, so we flipped it. So the main view I was looking at is the chat and, and then the settings is more just like a side panel at, at sort of previewing the changes that it’s making.
So you can introspect on them or, or you can also make changes manually if you’d like. But, but we wanna design the experience from the get go. So you don’t have to ever any of the settings manually, you can just talk to it.
[00:59:39]
Sarah Sachs
: And the inside baseball is like how this works was probably the launch blocking part of this build.
Right. Um, especially ‘cause we had a lot of early adopters that were used to the old way and that’s like the benefit of adopting in public. But then changing how people think about setting up custom agents when they already had this flow in and of itself was difficult. Um,
[00:59:57]
Simon Last
: I mean that’s really fun ‘cause the, we, we ended up sort of uh, uh, painfully delaying the launch.
Mm-hmm. By.
[01:00:04]
Sarah Sachs
: A month?
[01:00:04]
Simon Last
: A few weeks. Yeah, definitely. Like, like a month or so. Um, but the whole team was super enthusiastic about it though. ‘cause it was just so much better. It was like, oh yeah, obviously you have to chat with it, right? Yeah, yeah, yeah. To set itself up. And everyone was super bullish on that, so it was like, like painful for a second.
But then everyone’s like,
[01:00:19]
Sarah Sachs
: right, and like back to, you know, organization design, which I probably care about more than Simon, but like the people that built this are three engineers from three different teams. Because we’re like, we need to launch this and we need to fix this. And then we’ve just built a company where then we just put people on it and no one complains, the manager doesn’t complain.
And we were able to unblock and just ship it.
[01:00:37] Alsesio: Yeah, yeah. But being in a failure chat and asking it to just fix yourself is amazing. Versus I gotta copy this and put in the settings chat. Mm-hmm. Mm-hmm. To do
[01:00:49]
Simon Last
: it. So yeah. Interesting. Like a trade off in there that, that we’re trying to explore, which is, you know, we wanna be like a business enterprise safe agent where you can delegate something and, and trust that it’s gonna work.
But also we want to get some of that sort of bootstrapping power that, that you feel like when you’re coding it is making a browser, like for itself, right. There’s something there. I think that’s, that’s really important. So it’s, we’re trying to sort of. Navigate that, that, that trade off and try to get you both.
[01:01:12] Alsesio: Now it’s free, it’s amazing. Uh, I’m worried about when I have to start paying. How do you think about, so you have notion credits as a payment for this, which is like separate from the usual tokens, uh, that the model generates. How do you design pricing, value-based pricing based on the task and things like that.
[01:01:30]
Sarah Sachs
: So they are, um, the credits and payment structures associated with the token usage. The reason that we had to make it not just throughput of tokens is that it’s not always priced that way. Like our, um, fine tuned and open source models are served on GPUs, right? Web search is priced differently. You know, if we were to host sandboxes, those are priced differently.
So we had to think of an abstraction above tokens. And it’s also not just tokens, it’s the token model. Um, and serving tier trade off, right? Mm-hmm. Because we can have priority tier processing, we can have asynchronous processing. The cash rate could be different, um, depending on who uses it when, right?
And so we wanted to, um, from the get go commit to making sure that customers were getting the fair deal. Not necessarily that we were making a ton of money off of it, but that customers were paying for what was reasonable. That’s the fundamental of where we started. And also, you know, we’re selling enterprise sa, so if we sell credit packs and you get discounts if you’re an enterprise and you buy a certain amount of credit packs and things like that.
So it also just helped the sales motion, um, work a little bit easier. So that’s the answer on the abstraction of credits to dollars. Now was the question how we decide how to price it or?
[01:02:34] Alsesio: Yeah, like, I mean, I think there’s, all tokens are not made equal, but yeah, we obviously get charged mostly equal. Like you can ask, uh, codex to create you a dumb tool for like, I created one for our StarCraft two land for people to like find a game.
Uh, but then people create it to build features and like billion dollar companies. But the token price is the same.
[01:02:53]
Sarah Sachs
: Yeah.
[01:02:54] Alsesio: Like for you, I can ask this to update my favorite recipes doc. I’ll do it, but I could ask it to like respond to an email from an investor and like the value is like very different, you know, and you could charge more, but you’re not necessarily doing it.
So I’m curious if there was any discussion.
[01:03:11]
Sarah Sachs
: I think, I think that, um, that’s not where the market is right now. Um, number one, the second reason that we’re not doing that, as it ended up being kind of complicated to figure out what was complicated or not. So we at first we were like, let’s just charge on agent runs.
And you know what, you went through all the different versions that ultimately just brought you back to a lot of complexity that mapped directly to token throughput. And so it, it’s also just simpler. Um, it’s quite difficult, um, to build those pricing systems. And, um, I actually think that one of the biggest reasons we want had usage based pricing for this capability is.
We’ve had our core agent for a while with a model picker and there were certain models, um, or certain functionality that we had margins to maintain. And if we wanted to ship this functionality, uh, you, we couldn’t afford it, it would bankrupt the company. If we let, for instance, like autofill or the database autofill feature, we’ll soon be agentic That will be associated with usage based pricing.
Because if every single autofill action was an agent running on Opus on every single database sell, it would be billions of dollars, right? And so we had to find a way for the customers that wanted to do more and wanted to give us their money and pay more to find the outlet for them to do it, that we didn’t have to apply to the lower end of the curve.
And also, not all knowledge work is equal. Like there’s different points. A lot of the agent workflows here really saturate model capabilities. Like you don’t need a complicated model for it. And so charging based on token usage, um. It, we couldn’t just decide for you that you wanted your email client to be dumb or not, right?
Like, we want you to decide if you want to have Opus Auto Triage all of your emails, we will actually give you nudges in the product to rethink if that’s the right choice. Right. Um, because also not every user, um,
[01:04:52] Alsesio: understand.
[01:04:53]
Sarah Sachs
: You’d be surprised in user interviews. People would be like, oh, I didn’t know that.
So now we actually have a little hover that tells you like if it’s expensive or not. Yeah. I mean, it’s also slower. So the thing that’s interesting is like people don’t care about speed and custom agents. And so the incentive of like, uh, haiku being faster, people don’t care when it’s asynchronous. Um, and so we want to only provide the service of extra, extra benefit that people want.
And the best way to do that is to incentivize them because it’s their own own money.
[01:05:21] Alsesio: It must be confusing for people that are not familiar. It’s like, why is there no 5.3. You know, you open this thing and it’s like, is there something missing? Manual. It’s not their fault. Not their fault.
[01:05:30]
Simon Last
: Yeah. That’s just the world we live in now.
[01:05:32] Alsesio: Yeah. It just radical jump point too, it’s like Cloud had that.
[01:05:35]
Sarah Sachs
: I mean, but auto is heavily, I think what’s actually been hard for us is to tell convince people that auto is not just our cheapest, dumbest model, but actually the model that’s best for the task that you wanna do. Um, alright. Steve.
[01:05:46]
swyx
: I mean,
[01:05:48]
Sarah Sachs
: exactly.
Nice. Um, and a lot of our job is actually figuring out auto because it’s like,
[01:05:54]
swyx
: this is the agent lab. Every agent lab has an auto. Mm-hmm.
[01:05:57]
Sarah Sachs
: Yeah. And
[01:05:58]
swyx
: that’s the job.
[01:05:58]
Sarah Sachs
: Exactly. Because if you think about, like I said, I come from Robinhood, like you could spend a lot of time keeping up with the markets or you could have a auto investing, right?
And you can have an index fund or you can have
[01:06:12]
swyx
: roboadvisors
[01:06:12]
Sarah Sachs
: of the robo advisor. And so like at a certain point we also can be roboadvisors and like we have a lot of people figuring out what model is best for the right task. And we now, we’re not using auto as a, as a margin maker, we’re just using it to kind of reduce stress.
It’s not opus, that’s for sure. Yeah. Because a majority of the tasks people are doing aren’t opus level, um, intelligence.
[01:06:34]
Simon Last
: The other thing I would say is the, um, you know, unlike a lab, we aren’t fully incentivized just for you to use as many tokens as possible. We’re actually really interested in. Giving you the right tool for the job.
A lot of the time, the right tool for the job is actually just writing code and not even using agent at all. So that’s, that’s something that we’re investing in a lot is like, you know, imagine your, your agent can actually automate itself out of a job. Right. We would love if that were true.
[01:06:58]
Sarah Sachs
: I feel very strongly about this because I don’t necessarily feel like that’s the SKUs that Frontier Labs give you.
I feel like they are just getting more and more capable and more and more expensive, which is fantastic for the use cases of when people wanna do really complicated things on Notion. Um, what’s difficult is like that market that I think right now is no man’s land of where reasoning models were six months ago, that the nano haikus, et cetera, haven’t caught up to, because now we’re just paying more for those, um, for like extra capability that we didn’t necessarily need and so are our customers.
Mm-hmm. And, um, labs aren’t necessarily incentivized, um, right now with how few players there are to be meeting the market everywhere. They just need to be the cheapest. They don’t need to be at value that the customer wants.
[01:07:41]
swyx
: Hmm.
[01:07:42]
Sarah Sachs
: If no one’s cheaper than them, then they’re the cheapest and that’s good enough.
Right. And so we’re doing a lot to make sure that we have the right optionality, um, to switch between models and also invest in open source because the open source models actually are, um, getting to be the place where reasoning models were three, four months ago. And, um, that’s what’s filling that gap right now.
So you’ll see we offer Mini Max and, um, we are collaborating a lot with different open source labs to think about notion’s last exam and how they can do better on these types of tasks. Mm-hmm. So that we can offer them for that intelligence to price to latency trade off. Because, you know, in that triangle of intelligence, price, um, intelligence, price and latency, excuse me, um, users get to choose where they are, but right now, um, there’s not, the whole triangle isn’t filled with models, right?
Yeah. And the more that different models build cluster triangle capability, everyone’s clustered in capability where everyone’s cluster. I mean, haiku’s not that much cheaper. No one’s really in the middle. Like people really tend to. Cluster round two. Mm-hmm. Like, this is really capable and it’s really fast made, it’s really expensive or whatever.
Right. And so we just wanna make sure that that triangle’s filled, um, and we wanna offer the models that fill it and we wanna, um, gate guide users to understand when they need it. Yeah. Um, which one,
[01:08:54]
swyx
: I mean, all I’m hearing is that someday you’re gonna change your model. You have lots of tokens.
[01:09:01]
Sarah Sachs
: I don’t know if, what do you mean by train your model?
You train
[01:09:03]
swyx
: your
[01:09:03]
Sarah Sachs
: own, train your own model. Don’t know. We have money to train a founda. I mean,
[01:09:06] Alsesio: you go raise
[01:09:07]
swyx
: it. Yeah. You, you can raise it.
[01:09:09]
Sarah Sachs
: That’s your job, Simon. No, I, I don’t think that that needs to be our core competency.
[01:09:14]
swyx
: This is usually the, the thought process that leads to like, well, no one else is doing it.
We, we will take a crack. You know,
[01:09:19]
Simon Last
: I think I’m, yeah. I mean, I feel like to the extent that we do anything like training in the other area I’m actually most excited about is, um. Less of like one big model for all the users, but like as, as, as it becomes more possible to do, you know, to make like a specific fine tuning that’s like really knows your context of, you know, your company, the people that work your company, what’s going on.
I think that’s, that’s pretty interesting because if you, if you had a model that really knows your company, I think that would be like a huge quality uplift.
[01:09:47]
Sarah Sachs
: We actually have some enterprise vendors that kind of ask about this, um, along with bring our own key. Like if I have a model that really understands like my enterprise that we’re training for all these reasons, these tend to be like quite large institutions thinking about how to let people bring their own models.
But those models have to function with like
[01:10:04]
swyx
: right
[01:10:04]
Sarah Sachs
: understanding how to call our tools. And that’s where again, having, um, more. Public system prompt is like beneficial to notion, right? Um, we want all models to plug into notion as, as, as well as they can. Um, that being said, like of course there are certain aspects of notion where we do fine tune and do reinforce and fine tuning on our own capabilities.
Um, but that’s not necessarily trained on user data. Um, you don’t need that, that much data, um, in the first place. And that’s where when we have like a data scientist and a, a model behavior engineer really understand where the capability gap is, that’s when we invest there.
[01:10:38]
Simon Last
: I personally burned a lot of time trying to train models.
Uh, and it’s tempting, right? It’s so tempting, retraining
[01:10:46]
Sarah Sachs
: every day.
[01:10:47]
Simon Last
: I was doing crazy amount. Yeah, I was doing a lot of different things. Um, and it, I
[01:10:50]
Sarah Sachs
: was the budget person that came and found out and I showed up and I heard that that was happening time
[01:10:55]
Simon Last
: out. You know, like a, a funny thing that ‘cause the sort of an arc that like looped on itself is, uh, you know, back when I was doing tons of training stuff, it takes a long time to do it.
Any kind of training run. And so. You end up operating like, like 24 7 around the clock. Like it becomes very important that before you go to sleep, like everything is watch intensive board, all the experiments are, are started. And then as I stopped training, that kind of went away. But now the coding agents have totally brought this back.
Mm-hmm. So now every night before I go to bed, I’m like, okay, did I start enough agents, you know, to get them done. I get everything done. So it, it’s, it’s a ding interesting heart,
[01:11:26]
swyx
: this balance of like, you have to try polyphasic sleep so you can wake up every two.
[01:11:29]
Simon Last
: Absolutely. Yeah. Yeah. We, uh, yeah, I have not gone there yet, but, but my goal these days is just to, before I go to bed.
The agents are running, and I’m confident that they won’t be done by the time I wake up. Really
[01:11:41]
swyx
: Eight
[01:11:42]
Simon Last
: hours.
[01:11:42]
Sarah Sachs
: There’s a, I won’t say which coding Frontier Lab, but there was a point where he had like outlived like the thread length and context length uhhuh that that coding agent provided. And I DMed you DMed them being like, Hey, I need, I need more.
And our account rep DMed me directly and they’re like, is Simon trying to prove string theory? Like what is he doing?
[01:12:00]
Simon Last
: Yeah. I, I had a single coating Asian thread going for I think it was like 17 days. Uh, pretty much continuously.
[01:12:06]
swyx
: Don’t, don’t they just compress? I mean, yeah.
[01:12:08]
Simon Last
: Yeah. It was actually just a bug.
It was a harness bug. Yeah. It, it had done compaction like a hundred times probably.
[01:12:13]
swyx
: Yeah. The
[01:12:14]
Sarah Sachs
: other thing that um, reminded me about fine tuning that I think you and I have aligned on is that. Our tools change really frequently, and right now we spend a lot of time rethinking and building tools for capability and fine tuning a model, um, to understand your tool.
Like we don’t have legal expertise or coding expertise. So if we were to fine tune a model, it would either be expertise about the enterprise and you know, we have ZDR, no data retention offerings for those enterprises. So we’d have to really rethink how we structure if an enterprise wanted to opt into that or it would be fine tuning and better capability on navigating our tools that doesn’t match with the velocity with which we create new tools.
And so it actually really slow us down, um, to have a model that was fine tuned on our tools because we’d have to retrain it and cut a new model every time we did that. And that’s not how we’re set up right now. Um, particularly with the way that we’re changing our, I, I guess we could fine tune a model to like search for tools.
It’s just. The, the amount of time it takes to do that, ship it, have the right system, you’re basically making a bet against a frontier capability not serving that, and the time it takes you to build it. Mm-hmm. And that, that time lag hasn’t happened for us yet. It hasn’t
[01:13:17]
Simon Last
: been, yeah. It’s just the wrong trade off.
I think. It’s just like you want Yeah. We literally change our tools every single day and if we notice an issue, we will, we’ll, we’ll, we’ll fix the problem. I think a, a good way to think about it, I think is pretty fruitful, is like, don’t focus too much on training. I would think of that as like, that’s an implementation detail.
Like what’s the outer loop, right? Like, like the outer loop is you have a model and then some harness or, or system where it’s interacting with the system that needs to work. And you know, if there’s a problem, the way to solve the problem isn’t necessarily to train a model. It’s like, oh, maybe there’s just a bug in one of the tools.
Right? And actually 99% of the time it’s a bug in one of the tools, right? And so just fix the bug. And then the outer loop thing that’s really fruitful to think about is like, how can you improve your, your velocity and robustness? Making really good tools, making a good harness, you know, like, like verifying it works.
Hmm.
[01:14:07]
Sarah Sachs
: The one place that we do invest more in model turning now necessarily though, is actually in retrieval because, um, we’re at a point right now in our business and enterprise, our AI enabled plans where. The search load and the search traffic. Majority of it’s coming from agents, not humans. And so for every query that’s hitting our elastic search or our vector indices, they’re not coming from humans.
And the queries are structured differently. And what’s returned has a different re requirement. Positional ranking matters less, but top K retrieval mode matters more. Right.
[01:14:34]
swyx
: Isn’t top KA form of position?
[01:14:36]
Sarah Sachs
: Of course it is. But um, when you’re training on like click through rate, it’s really, you know,
[01:14:41]
swyx
: yeah.
[01:14:41]
Sarah Sachs
: It matters much less.
Number one through number six is very different
[01:14:44]
swyx
: Yeah.
[01:14:44]
Sarah Sachs
: Than it needs to be in the top 100.
[01:14:45]
swyx
: Like the slope is just,
[01:14:46]
Sarah Sachs
: yeah.
[01:14:46]
swyx
: Higher.
[01:14:47]
Sarah Sachs
: It’s a different optimization function for retrieval, um, model. Similarly, uh, what snippet you include matters more or less. Right. So we are rethinking a lot of that functionality, um, to work with how the agents like to write queries and how, um, they wanna, uh, receive information.
Yeah. So we are doing like another kind of reinvestment into rethinking not only search for, um, how do agents do searches versus how humans do searches. Um, but we’re also investing in like. Indexing different things now because, uh, how are, how do you index, uh, the setup generator for Notion agent? It kind of breaks our block model entirely, um, where all blocks are nested in each other.
Same with meeting notes. Um, and so we do, we, I mean, so we’re hiring ranking engineers and model training engineers, but it’s primarily on ranking.
[01:15:32]
swyx
: Yeah. Does ranking maps to res for you? It does, right. Recommendation systems.
[01:15:36]
Sarah Sachs
: Yeah. Um, yes.
[01:15:38]
swyx
: Right. Okay. Say this, but I’m trying to promote res more in general ‘cause I is weirdly unpopular.
[01:15:45]
Sarah Sachs
: I don’t know why. Um, but the other thing is that, like, I I was just talking about this with a peer, like how much is ranking important versus like, uh, being able to do parallel exhaustive queries. Right. Um, so we’re also, they’re both important. They’re both important, but like they’re both two tools to the same user outcome or the same agent outcome.
Uhhuh. Right. And so, um, that. That’s something that we’re also rethinking a lot even on, we just did an experiment on, um, notion ranking at this point, um, for notion retrieval, vector embeddings are less and less.
[01:16:15]
swyx
: Did you see that? Yeah. Notion just, uh, to nine
[01:16:19] Alsesio: so long it became dark mode.
[01:16:21]
Sarah Sachs
: We’re working the night shift for you.
Right? Looks
[01:16:23]
Simon Last
: pretty good. I’m not seeing any bug.
[01:16:24]
swyx
: You know, I worked on this like parallel search thing where you, you found out to eight different queries, right? Yes. And so you actually need to use the model to work on query diversity so that you get right. Investment space.
[01:16:35]
Sarah Sachs
: And so like the people that are working on, um, ranking and retrieval are the same people working on what query generation is.
It’s all one, uh, journey. Yeah. We call it age agentic find. And we’re actually realizing, for instance, that it’s less about a selection. Like we don’t spend a lot of time trying to optimize what vector embedding we use anymore. That was a period of time, but that’s just not the right lever of optimization.
[01:16:55]
swyx
: Yeah. Right. Yeah. Okay. Uh, we’ve gone long. I have to talk about motion meeting minutes and then we’ll, we’ll, we can call it there. Uh, you, you, you just have a lot of comments. Uh, you, you, uh, I don’t know where you wanna start. Um, is it the audio side? Is it the sort of Oh, meeting notes, summarization? Yeah.
[01:17:12]
Simon Last
: Sort of like what makes it work or
[01:17:13]
swyx
: No, just like anything sort of interesting technically, right? Like I think you had, you had some, uh, book points. I always call these like check marks along the way when the, when a guest says something that we, they wanna return to later, I just like, check mark it. Yeah.
I’m like, okay. We’ll back to it. Um,
[01:17:26]
Sarah Sachs
: meeting notes was one of those things where at first we were nervous that we’d have to teach people a different way to work, and we were nervous that that was a lot of user friction. I think one of the reasons why, I mean, they’re one of our biggest growth lever. I think they’re one of the most like.
In terms of virality of adoption and retention, quite strong. Um, and so we’ve invested more and more as we did that. I think what’s really powerful about it is, again, notion is the system of record of where and how you work. The way that I use meeting notes is every one-on-one and meeting I have is meeting notes.
When I do my performance review for myself, myself, review, I say primarily look at all my conversations with my manager and like, write up what I did this year, right? Because if I didn’t talk about it in my one-on-one with my manager, it probably wasn’t relevant for my performance review. So it also just adds a ton of signal on prioritization that’s really helpful for a good system of record.
That’s really helpful for like our agent. It’s also like caused a lot of scaling for search and for the agent. Um, and you know, it’s, it’s just an explosion of content when you have transcripts like that. Um, how we do compaction. A lot of that was triggered by meeting notes passed into context, things like that.
Um, so it’s been a good impetus for us to think about. Longer form, um, content when you think of it as like a priority, primitive, but it’s been one of the most powerful signals for our agent. Um, because it’s
[01:18:44]
swyx
: unsurprising. Right? Right. And
[01:18:45]
Sarah Sachs
: you’re
[01:18:45]
swyx
: capturing a whole new thing.
[01:18:46]
Sarah Sachs
: So it’s like our own data. Like we want users like, or they’re creating their own data flywheel, right?
[01:18:51]
swyx
: Like it serves me to prefer notion, uh, to put all my stuff because it has my other stuff.
[01:18:57]
Sarah Sachs
: Totally. I mean, the way that, the way that like our teams run right now is. You know, there’s a custom agent that does a pre-read before standup. It looks through all of Slack and GitHub and just says, you know, it, it, it creates a summary and it creates a meeting note and it says Everyone do this pre-read.
Then we just press play. We have the meeting, we talk through the pre-read, we talk about what needs to happen next, and then we have a custom agent integrated with our calendar and triggers that then files task for tomorrow or today based on what we spoke about. And, um, sends off Slack messages that we decided in the meeting needed to be follow ups.
Like our meetings are hands off keyboard and we’re focused on, um, the root of the problem, not the bookkeeping around the problem.
[01:19:32]
Simon Last
: One thing that, uh, the me, us team had recently that was, but I’ve been blowing my mind, is they, we, uh, uh, they made it so it actually, when it makes the summary, we’ll actually app mention the people that were referenced oof in it.
So I, I, I now get notifications whenever someone talks about meeting. Yeah. I
[01:19:46]
Sarah Sachs
: feel like that one
[01:19:47]
Simon Last
: was, it’s like, it’s like, oh, you know. Simon is working on this. Okay, I’m gonna, it’s actually amazing how, because then I’m like, oh, okay, cool. I’m gonna go talk to them about that.
[01:19:55]
swyx
: Right? What, what if they’re two Simons?
[01:19:56]
Simon Last
: Um,
[01:19:57]
Sarah Sachs
: no wait, so wait. It’s powered by the agent. So it’s doing agentic. So if you look at it thinking, I don’t know if this is shipped yet. It will be, when you look at it thinking when it’s doing the summarization, it’s saying, figuring out who Simon
[01:20:07]
swyx
: is most probable Simon
[01:20:08]
Sarah Sachs
: is. Yeah. Um, and we also have like a people to people similarity cash and stuff like that.
Yeah, yeah. On the here’s we sort of like,
[01:20:15]
Simon Last
: we also like generate a profile for each person and like, and use that. Um, yeah. I mean of course I can get it wrong, but the goal is for not to get it
[01:20:22]
Sarah Sachs
: wrong. Meeting nuts is just like the agent primitive packaged on top of a transcription. Primitive. Yeah. Yeah. And then a vertical team.
It’s probably one of the only teams at Notion that’s completely a vertical team around quality and product like UX design. ‘cause it’s still a Tiger team. Um, with a fantastic manager, Zach, that joined recently, um, from Embr, but, um,
[01:20:40]
swyx
: Zachar.
[01:20:41]
Sarah Sachs
: Yeah.
[01:20:42]
swyx
: Yeah. I, uh, chatted with him when he was talking about with his working number.
[01:20:45]
Sarah Sachs
: Yeah. So he’s, he’s managing that team now and thinking about it as data capture. That’s what meeting notes is, is data capture it, get
[01:20:50]
swyx
: all
[01:20:51]
Sarah Sachs
: the kinds of kind of reframing, um, where meeting notes are valuable as a data capture problem and then working inside, um, like the summarization used to not be age agentic.
Yeah. Now it is because it does all the things like figure out who the right Simon is. And one day you can have a custom agent directly integrated in it that knows like what task database the meeting is referring to. And as you’re having the meeting perhaps update the tasks and things like that. Like there’s a, there’s a lot of that experience of where we do our work in meetings that we wanna invest in.
Making more seamless.
[01:21:18]
swyx
: Yeah. Uh, opening eyes, doing hardware. Uh, would you ever ship one of these?
[01:21:22]
Simon Last
: Yeah, probably not,
[01:21:23]
Sarah Sachs
: but one of those.
[01:21:23]
swyx
: But you know, this, this is meeting notes in person.
[01:21:25]
Simon Last
: Yeah. Yeah. I, I’d be excited about, I mean, I’m excited about that, that product category in general for sure. Yeah.
[01:21:31]
Sarah Sachs
: I think it’s like, it’s a, it’s a mechanism and it.
It, one of those needs to work really well with Notion. We would partner with whoever’s building one of those, I think. Yeah. This is
[01:21:40]
swyx
: be they, they were bought by Amazon. I don’t know. I I can refer you.
[01:21:43]
Sarah Sachs
: And there’s like, there’s some wild companies doing like really cool things that come to our partnerships team that I like to sit in on the demos of, of wearables.
I always like to send in on the demos ‘cause I think they’re Oh, okay. Pretty cool. And all of them want to make sure, not just notion, but like you can imagine the ones that talk to you. Yeah, yeah. Um, being able to do search and build context. So like if you’re entering like a conference, um, being able to like do like look at your CRM and do things like that.
Um, and you can utilize the Notion agent to do that. So we are in like the very beginnings of those partnerships. I think what’s unique about that particular technology is it goes against what I talked about with custom agents right now, which is the more simple it is, the harder it is to have like advanced controls over its capabilities.
Right? And so that would be a great investment for data capture, but not necessarily like our agent is workflows.
[01:22:26]
Simon Last
: It’s something with a different slice of the problem, I would say. Yeah. Like that’s gonna be deeply personal. Like, like your company’s not gonna force you to wear a risk. Wristband. Right. I, I think
[01:22:35]
Sarah Sachs
: it’s good to hear that from me.
From you. Yeah.
[01:22:38]
Simon Last
: Yeah. The, the CEO’s gonna force everyone to wear a wristband look, I mean, the slice of the problem that, that we care about is like, you know, can the company have all the context of what everyone said at every single meeting, and then use that to, yeah. To, to derive value for themselves.
[01:22:52]
Sarah Sachs
: It kinda reminds me, I remember once you.
Very strongly reminded me, our job is to not make the best harness for agentic work. Our job is to be the best place where people collaborate. It’s like our job isn’t to build the best wearable to capture meeting notes. Our job is to build the best place where meeting notes live. Right?
[01:23:11]
swyx
: Yeah. So it basically, you’re saying everyone else can just pipe to you and it’s fine, right?
Yeah, yeah, yeah. That’s, that’s a reasonable thing. All I’ll say is that people, there’s people walking around with notion tattoos on them. They, they’ll wear notion anything. So just, I don’t know, do a limited run.
[01:23:24]
Simon Last
: Yeah, yeah. No, I mean,
[01:23:27]
Sarah Sachs
: we have such understated swag that the idea, like our swag has so few notion lay logos on it.
The idea that people have notion tattoos is pretty antithesis to our design principles, so that’s pretty funny.
[01:23:38]
Simon Last
: Yeah.
[01:23:39]
Sarah Sachs
: Do you have one?
[01:23:40]
Simon Last
: No, not, I do not have a notion Tattoo too. I’ve, I’ve seen them. Yeah.
[01:23:44]
swyx
: Cool. Uh, well, thank you so much. This is such a great deep, deep dive. Actually. The chemistry between you two is amazing.
Like, I, I can’t believe, like
[01:23:51]
Sarah Sachs
: we work together a lot. Yeah. Different jobs. Work closely.
[01:23:55]
swyx
: Yeah.
[01:23:55] Alsesio: That’s it. Yeah. Thank you. Thank you.
[01:23:57]
Sarah Sachs
: Thanks. Thank you.
