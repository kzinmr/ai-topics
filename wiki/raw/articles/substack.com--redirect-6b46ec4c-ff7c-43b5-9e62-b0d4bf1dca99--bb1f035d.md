---
title: "Every Agent Needs a Box - Aaron Levie, Box"
url: "https://substack.com/redirect/6b46ec4c-ff7c-43b5-9e62-b0d4bf1dca99?j=eyJ1IjoiMmZseDYifQ.6O_iC1_GWCzChnbrHzSrs1hMpJpoODTUJm_FAk3tf6E"
fetched_at: 2026-04-15T03:06:24.427406+00:00
source_date: 2026-04-15
tags: [newsletter, auto-ingested]
---

# Every Agent Needs a Box - Aaron Levie, Box

Source: https://substack.com/redirect/6b46ec4c-ff7c-43b5-9e62-b0d4bf1dca99?j=eyJ1IjoiMmZseDYifQ.6O_iC1_GWCzChnbrHzSrs1hMpJpoODTUJm_FAk3tf6E

The reception to
our recent post on Code Reviews
has been
strong
. Catch up!
Amid a maelstrom of discussion on whether or not
AI is killing SaaS
, one of the top publicly listed SaaS companies in the world has just reported record revenues,
clearing well over $1.1B in ARR for the first time with a 28% margin
. As we comment on the pod, Aaron Levie is the rare public company CEO equally at home in both worlds of Silicon Valley and Wall Street/Main Street, by day helping 70% of the Fortune 500 with their Enterprise Advanced Suite, and yet by night is often found in the basements of early startups and tweeting viral insights about the future of agents.
Now that both Cursor, Cloudflare, Perplexity, Anthropic and more have made Filesystems and Sandboxes and various forms of “Just Give the Agent a Box” cool (not just cool; it is now one of the single hottest areas in AI infrastructure growing 100% MoM), we find it a delightfully appropriate time to do the episode with the OG CEO who has been giving humans and computers Boxes since he was a college dropout pitching VCs at a Michael Arrington house party.
Enjoy our special pod, with
fan favorite returning guest/guest cohost Jeff Huber
!
Note: We didn’t directly discuss the AI vs SaaS debate - Aaron has done many, many, many other podcasts on that, and you should read
his definitive essay on it
. Most commentators do not understand SaaS businesses because they have never scaled one themselves, and deeply reflected on what the true value proposition of SaaS is.
We also discuss
Your Company is a Filesystem
:
We also shoutout
CTO Ben Kus
’ and the AI team, who talked about the technical architecture and will return for
AIE WF 2026
.
00:00 Adapting Work for Agents
01:29 Why Every Agent Needs a Box
04:38 Agent Governance and Identity
11:28 Why Coding Agents Took Off First
21:42 Context Engineering and Search Limits
31:29 Inside Agent Evals
33:23 Industries and Datasets
35:22 Building the Agent Team
38:50 Read Write Agent Workflows
41:54 Docs Graphs and Founder Mode
55:38 Token FOMO Culture
56:31 Production Function Secrets
01:01:08 Film Roots to Box
01:03:38 AI Future of Movies
01:06:47 Media DevRel and Engineering
Aaron Levie:
Like you don’t write code, you talk to an agent and it goes and does it for you, and you may be at best review it. That’s even probably like, like largely not even what you’re doing. What’s happening is we are changing our work to make the agents effective. In that model, the agent didn’t really adapt to how we work.
We basically adapted to how the agent works. All of the economy has to go through that exact same evolution. Right now, it’s a huge asset and an advantage for the teams that do it early and that are kinda wired into doing this ‘cause you’ll see compounding returns. But that’s just gonna take a while for most companies to actually go and get this deployed.
swyx:
Welcome to the Lane Space Pod. We’re back in the chroma studio with uh, chroma, CEO, Jeff Hoover. Welcome returning guest now guest host.
Aaron Levie:
It’s a pleasure. Wow. How’d you get upgraded to, uh, to that?
swyx:
Because he’s like the perfect guy to be guest those for you.
Aaron Levie:
That makes sense actually, for We love context. We, we both really love context le we really do.
We really do.
swyx:
Uh, and we’re here with, uh, Aaron Levy. Welcome.
Aaron Levie:
Thank you. Good to, uh, good to be [00:01:00] here.
swyx:
Uh, yeah. So we’ve all met offline and like chatted a little bit, but like, it’s always nice to get these things in person and conversation. Yeah. You just started off with so much energy. You’re, you’re super excited about agents.
I love
Aaron Levie:
agents.
swyx:
Yeah. Open claw. Just got by, got bought by OpenAI. No, not bought, but you know, you know what I mean?
Aaron Levie:
Some, some, you know, acquihire. Executive
swyx:
hire.
Aaron Levie:
Executive hire. Okay. Executive hire. Say,
swyx:
hey, that’s my term. Okay. Um, what are you pounding the table on on agents? You have so many insightful tweets.
Aaron Levie:
Well, the thing that, that we get super excited by that I think is probably, you know, should be relatively obvious is we’ve, we’ve built a platform to help enterprises manage their files and their, their corporate files and the permissions of who has access to those files and the sharing collaboration of those files.
All of those files contain really, really important information for the enterprise. It might have your contracts, it might have your research materials, it might have marketing information, it might have your memos. All that data obviously has, you know, predominantly been used by humans. [00:02:00] But there’s been one really interesting problem, which is that, you know, humans only really work with their files during an active engagement with them, and they kind of go away and you don’t really see them for a long time.
And all of a sudden, uh, with the power of AI and AI agents, all of that data becomes extremely relevant as this ongoing source of, of answers to new questions of data that will transform into, into something else that, that produces value in your organization. It, it contains the answer to the new employee that’s onboarding, that needs to ramp up on a project.
Um, it contains the answer to the right thing to sell a customer when you’re having a conversation to them, with them contains the roadmap information that’s gonna produce the next feature. So all that data. That previously we’ve been just sort of storing and, and you know, occasionally forgetting about, ‘cause we’re only working on the new active stuff.
All of that information becomes valuable to the enterprise and it’s gonna become extremely valuable to end users because now they can have agents go find what they’re looking for and produce new, new [00:03:00] value and new data on that information. And it’s gonna become incredibly valuable to agents because agents can roam around and do a bunch of work and they’re gonna need access to that data as well.
And um, and you know, sometimes that will be an agent that is sort of working on behalf of, of, of you and, and effectively as you as and, and they are kind of accessing all of the same information that you have access to and, and operating as you in the system. And then sometimes there’s gonna be agents that are just.
Effectively autonomous and kind of run on their own and, and you’re gonna collaborate and work with them kind of like you did another person. Open Claw being the most recent and maybe first real sort of, you know, kind of, you know, up updating everybody’s, you know, views of this landscape version of, of what that could look like, which is, okay, I have an agent.
It’s on its own system, it’s on its own computer, it has access to its own tools. I probably don’t give it access to my entire life. I probably communicate with it like I would an assistant or a colleague and then it, it sort of has this sandbox environment. So all of that has massive implications for a platform that manage that [00:04:00] enterprise data.
We think it’s gonna just transform how we work with all of the enterprise content that we work with, and we just have to make sure we’re building the right platform to support that.
swyx:
The sort of shorthand I put it is as people build agents, everybody’s just realizing that every agent needs a box. Yes.
And it’s nice to be called box and just give everyone a box.
Aaron Levie:
Hey, I if I, you know, if we can make that go viral, uh, like I, I think that that terminology, I, that’s the
swyx:
tagline. Every agent
Aaron Levie:
needs a box. Every agent needs a box. If we can make that the headline of this, I’m fine with this. And that’s the billboard I wanna like Yeah, exactly.
Every agent needs a box. Um, I like it. Can we ship this? Like,
swyx:
okay, let’s do it. Yeah.
Aaron Levie:
Uh, my work here is done and I got the value I needed outta this podcast Drinks.
swyx:
Yeah.
Aaron Levie:
But, but, um, but, but, you know, so the thing that we, we kind of think about is, um, is, you know, whether you think the number 10 x or a hundred x or whatever the number is, we’re gonna have some order of magnitude more agents than people.
That’s inevitable. It has to happen. So then the question is, what is the infrastructure that’s needed to make all those agents effective in the enterprise? Make sure that they are well governed. Make sure they’re only doing [00:05:00] safe things on your information. Make sure that they’re not getting exposed. The data that they shouldn’t have access to.
There’s gonna be just incredibly spectacularly crazy security incidents that will happen with agents because you’ll prompt, inject an agent and sort of find your way through the CRM system and pull out data that you shouldn’t have access to. Oh, we
Jeff Huber:
have God,
Aaron Levie:
right? I mean, that’s just gonna happen all over the place, right?
So, so then the thing is, is how do you make sure you have the right security, the permissions, the access controls, the data governance. Um, we actually don’t yet exactly know in many cases how we’re gonna regulate some of these agents, right? If you think about an agent in financial services, does it have the exact same financial sort of, uh, requirements that a human did?
Or is it, is the risk fully on the human that was interacting or created the agent? All open questions, but no matter what, there’s gonna need to be a layer that manages the, the data they have access to, the workflows that they’re involved in, pulling up data from multiple systems. This is the new infrastructure opportunity in the era of agents.
swyx:
You have a piece on agent identities, [00:06:00] which I think was today, um, which I think a lot of breaking news, the security, security people are talking about, right? Like you basically, I, I always think of this as like, well you need the human you and then there you need the agent. You
Aaron Levie:
Yes.
swyx:
And uh, well, I don’t know if it’s that simple, but is box going to have an opinion on that or you’re just gonna be like, well we’re just the sort of the, the source layer.
Yeah. Let’s Okta of zero handle that.
Aaron Levie:
I think we’re gonna have an opinion and we will work with generally wherever the contours of the market end up. Um, and the reason that we’re gonna have an opinion more than other topics probably is because one of the biggest use cases for why your agent might need it, an identity is for file system access.
So thus we have to kind of think about this pretty deeply. And I think, uh, unless you’re like in our world thinking about this particular problem all day long, it might be, you know, like, why is this such a big deal? And the reason why it’s a really big deal is because sometimes sort of say, well just give the agent an, an account on the system and it just treats, treat it like every other type of user on the system.
The [00:07:00] problem is, is that I as Aaron don’t really have any responsibility over anybody else’s box account in our organization. I can’t see the box account of any other employee that I work with. I am not liable for anything that they do. And they have, I have, I have, you know, strict privacy requirements on everything that they’re able to, you know, that, that, that they work on.
Agents don’t have that, you know, don’t have those properties. The person who creates the agent probably is gonna, for the foreseeable future, take on a lot of the liability of what that agent does. That agent doesn’t deserve any privacy because, because it’s, you know, it can’t fully be autonomously operated and it doesn’t have any legal, you know, kind of, you know, responsibility.
So thus you can’t just be like, oh, well I’ll just create a bunch of accounts and then I’ll, I’ll kind of work with that agent and I’ll talk to it occasionally. Like you need oversight of that. And so then the question is, how do you have a world where the agent, sometimes you have oversight of, but what if that agent goes and works with other people?
That person over there is collaborating with the agent on something you shouldn’t have [00:08:00] access to what they’re doing. So we have all of these new boundaries that we’re gonna have to figure out of, of, you know, it’s really, really easy. So far we’ve been in, in easy mode. We’ve hit the easy button with ai, which is the agent just is you.
And when you’re in quad code and you’re in cursor, and you’re in Codex, you’re just, the agent is you. You’re offing into your services. It can do everything you can do. That’s the easy mode. The hard mode is agents are kind of running on their own. People check in with them occasionally, they’re doing things autonomously.
How do you give them access to resources in the enterprise and not dramatically increased the security risk and the risk that you might expose the wrong thing to somebody. These are all the new problems that we have to get solved. I like the identity layer and, and identity vendors as being a solution to that, but we’ll, we’ll need some opinions as well because so many of the use cases are these collaborative file system use cases, which is how do I give it an agent, a subset of my data?
Give it its own workspace as well. ‘cause it’s gonna need to store off its own information that would be relevant for it. And how do I have the right oversight into that? [00:09:00]
Jeff Huber:
One thing, which, um, I think is kind interesting, think about is that you know, how humans work, right? Like I may not also just like give you access to the whole file.
I might like sit next to you and like scroll to this like one part of the file and just show you that like one part and like, you know,
swyx:
partial file access.
Jeff Huber:
I’m just saying I think like our, like RA does seem to be dead, right? Like you wanna say something is dead uhhuh probably RA is dead. And uh, like the auth story to me seems like incredibly unsolved and unaddressed by like the existing state of like AI vendors.
But
Aaron Levie:
yeah, I think, um, we’re, I mean you’re taking obviously really to level limit that we probably need to solve for. Yeah. And we built an access control system that was, was kind of like, you know, its own little world for, for a long time. And um, and the idea was this, it’s a many to many collaboration system where I can give you any part of the file system.
And it’s a waterfall model. So if I give you higher up in the, in the, in the system, you get everything below. And that, that kind of created immense flexibility because I can kind of point you to any layer in the, in the tree, but then you’re gonna get access to everything kind of below it. And that [00:10:00] mostly is, is working in this, in this world.
But you do have to manage this issue, which is how do I create an agent that has access to some of my stuff and somebody else’s stuff as well. Mm-hmm. And which parts do I get to look at as the creator of the agent? And, and these are just brand new problems? Yeah. Crazy. And humans, when there was a human there that was really easy to do.
Like, like if the three of us were all sharing, there’d be a Venn diagram where we’d have an overlapping set of things we’ve shared, but then we’d have our own ways that we shared with each other. In an agent world, somebody needs to take responsibility for what that agent has access to and what they’re working on.
These are like the, some of the most probably, you know, boring problems for 98% of people on, on the internet, but they will be the problems that are the difference between can you actually have autonomous agents in an enterprise context
swyx:
Yeah.
Aaron Levie:
That are not leaking your data constantly.
swyx:
No. Like, I mean, you know, I run a very, very small company for my conference and like we already have data sensitivity issues.
Yes. And some of my team members cannot see Yes. Uh, the others and like, I can’t imagine what it’s like to run a Fortune 500 and like, you have to [00:11:00] worry about this. I’m just kinda curious, like you, you talked to a lot like, like 70, 80% of your cus uh, of the Fortune 500, your customers.
Aaron Levie:
Yep. 67%. Just so we’re being very
SE
swyx:
precise.
So Yeah. I’m not
Aaron Levie:
Okay. Okay.
swyx:
Something I’m rounding up. Yes. Round up. I’m projecting to, for
Aaron Levie:
the government.
swyx:
I’m projecting to the end of the year.
Aaron Levie:
Okay.
swyx:
There you go.
Aaron Levie:
You do make it sound like, like we, we, well we’ve gotta be on this. Like we’re, we’re taking way too long to get to 80%. Well,
swyx:
no, I mean, so like. How are they approaching it?
Right? Because you’re, you don’t have a, you don’t have a final answer yet.
Aaron Levie:
Well, okay, so, so this is actually, this is the stark reality that like, unfortunately is the kinda like pouring the water on the party a little bit.
swyx:
Yes.
Aaron Levie:
We all in Silicon Valley are like, have the absolute best conditions possible for AI ever.
And I think we all saw the dke, you know, kind of Dario podcast and this idea of AI coding. Why is that taken off? And, and we’re not yet fully seeing it everywhere else. Well, look, if you just like enumerated the list of properties that AI coding has and then compared it to other [00:12:00] knowledge work, let’s just, let’s just go through a few of them.
Generally speaking, you bring on a new engineer, they have access to a large swath of the code base. Like, there’s like very, like you, just, like new engineer comes on, they can just go and find the, the, the stuff that they, they need to work with. It’s a fully text in text out. Medium. It’s only, it’s just gonna be text at the end of the day.
So it’s like really great from a, from just a, uh, you know, kinda what the agent can work with. Obviously the models are super trained on that dataset. The labs themselves have a really strong, kind of self-reinforcing positive flywheel of why they need to do, you know, agent coding deeply. So then you get just better tooling, better services.
The actual developers of the AI are daily users of the, of the thing that they’re we’re working on versus like the, you know, probably there’s only like seven Claude Cowork legal plugin users at Anthropic any given day, but there’s like a couple thousand Claude code and you know, users every single day.
So just like, think about which one are they getting more feedback on. All day long. So you just go through this list. You have a, you know, everybody who’s a [00:13:00] developer by definition is technical so they can go install the latest thing. We’re all generally online, or at least, you know, kinda the weird ones are, and we’re all talking to each other, sharing best practices, like that’s like already eight differences.
Versus the rest of the economy. Every other part of the economy has like, like six to seven headwinds relative to that list. You go into a company, you’re a banker in financial services, you have access to like a, a tiny little subset of the total data that’s gonna be relevant to do your job. And you’re have to start to go and talk to a bunch of people to get the right data to do your job because Sally didn’t add you to that deal room, you know, folder.
And that that, you know, the information is actually in a completely different organization that you now have to go in and, and sort of run into. And it’s like you have this endless list of access controls and security. As, as you talked about, you have a medium, which is not, it’s not just text, right? You have, you have a zoom call that, that you’re getting all of the requirements from the customer.
You have a lot of in-person conversations and you’re doing in-person sales and like how do you ever [00:14:00] digitize all of that information? Um, you know, I think a lot of people got upset with this idea that the code base has all the context, um, that I don’t know if you follow, you know, did you follow some of that conversation that that went viral?
Is like, you know, it’s not that simple that, that the code base doesn’t have all the knowledge, but like it’s a lot, you’re a lot better off than you are with other areas of knowledge work. Like you, we like, we like have documentation practices, you write specifications. Those things don’t exist for like 80% of work that happens in the enterprise.
That’s the divide that we have, which is, which is AI coding has, has just fully, you know, where we’ve reached escape velocity of how powerful this stuff is, and then we’re gonna have to find a way to bring that same energy and momentum, but to all these other areas of knowledge work. Where the tools aren’t there, the data’s not set up to be there.
The access controls don’t make it that easy. The context engineering is an incredibly hard problem because again, you have access control challenges, you have different data formats. You have end users that are gonna need to kind of be kind of trained through this as opposed to their adopting [00:15:00] these tools in their free time.
That’s where the Fortune 500 is. And so we, I think, you know, have to be prepared as an industry where we are gonna be on a multi-year march to, to be able to bring agents to the enterprise for these workflows. And I think probably the, the thing that we’ve learned most in coding that, that the rest of the world is not yet, I think ready for, I mean, we’re, they’ll, they’ll have to be ready for it because it’s just gonna inevitably happen is I think in coding.
What, what’s interesting is if you think about the practice of coding today versus two years ago. It’s probably the most changed workflow in maybe the history of time from the amount of time it’s changed, right? Yeah. Like, like has any, has any workflow in the entire economy changed that quickly in terms of the amount of change?
I just, you know, at least in any knowledge worker workflow, there’s like very rarely been an event where one piece of technology and work practice has so fundamentally, you know, changed, changed what you do. Like you don’t write code, you talk to an agent and it goes and [00:16:00] does it for you, and you may be at best review it.
And even that’s even probably like, like largely not even what you’re doing. What’s happening is we are changing our work to make the agents effective. In that model, the agent didn’t really adapt to how we work. We basically adapted to how the agent works. Mm-hmm. All of the economy has to go through that exact same evolution.
The rest of the economy is gonna have to update its workflows to make agents effective. And to give agents the context that they need and to actually figure out what kind of prompting works and to figure out how do you ensure that the agent has the right access to information to be able to execute on its work.
I, you know, this is not the panacea that people were hoping for, of the agent drops in, just automates your life. Like you have to basically re-engineer your workflow to get the most out of agents and, uh, and that, that’s just gonna take, you know, multiple years across the economy. Right now it’s a huge asset and an advantage for the teams that do it early and that are kinda wired into doing this.
‘cause [00:17:00] you’ll see compounding returns, but that’s just gonna take a while for most companies to actually go and get this deployed.
swyx:
I love, I love pushing back. I think that. That is what a lot of technology consultants love to hear this sort of thing, right? Yeah, yeah, yeah. First to, to embrace the ai. Yes. To get to the promised land, you must pay me so much money to a hundred percent to adopt the prescribed way of, uh, conforming to the agents.
Yes. And I worry that you will be eclipsed by someone else who says, no, come as you are.
Aaron Levie:
Yeah.
swyx:
And we’ll meet you where you are.
Aaron Levie:
And, and, and and what was the thing that went viral a week ago? OpenAI probably, uh, is hiring F Dees. Yeah. Uh, to go into the enterprise. Yeah. Yeah. And then philanthropic is embedded at Goldman Sachs.
Yeah. So if the labs are having to do this, if, if the labs have decided that they need to hire FDE and professional services, then I think that’s a pretty clear indication that this, there’s no easy mode of workflow transformation. Yeah. Yeah. So, so to your point, I think actually this is a market opportunity for, you know, new professional services and consulting [00:18:00] firms that are like Agent Build and they, and they kind of, you know, go into organizations and they figure out how to re-engineer your workflows to make them more agent ready and get your data into the right format and, you know, reconstruct your business process.
So you’re, you’re not doing most of the work. You’re telling agents how to do the work and then you’re reviewing it. But I haven’t seen the thing that can just drop in and, and kinda let you not go through those changes.
swyx:
I don’t know how that kind of sales pitch goes over. Yeah. You know, you’re, you’re saying things like, well, in my sort of nice beautiful walled garden, here’s, there’s, uh, because here’s this, here’s this beautiful box account that has everything.
Yes. And I’m like, well, most, most real life is extremely messy. Sure. And like, poorly named and there duplicate this outdated shit
Aaron Levie:
a hundred percent. And so No, no, a hundred percent. And so this is actually No. So, so this is, I mean, we agree that, that getting to the beautiful garden is gonna be tough.
swyx:
Yeah.
Aaron Levie:
There’s also the other end of the spectrum where I, I just like, it’s a technical impossibility to solve. The agent is, is truly cannot get enough context to make the right decision in, in the, in the incredibly messy land. Like there’s [00:19:00] no a GI that will solve that. So, so we’re gonna have to kind of land in somewhere in between, which is like we all collectively get better at.
Documentation practices and, and having authoritative relatively up-to-date information and putting it in the right place like agents will, will certainly cause us to be much better organized around how we work with our information, simply because the severity of the agent pulling the wrong data will be too high and the productivity gain of that you’ll miss out on by not doing this will be too high as well, that you, that your competition will just do it and they’ll just have higher velocity.
So, uh, and, and we, we see this a lot firsthand. So we, we build a series of agents internally that they can kind of have access to your full box account and go off and you give it a task and it can go find whatever information you’re looking for and work with. And, you know, thank God for the model progress, but like, if, if you gave that task to an agent.
Nine months ago, you’re just gonna get lots of bogus answers because it’s gonna, it’s gonna say, Hey, here’s, here are fi [00:20:00] five, you know, documents that all kind of smell like the right thing. And I’m gonna, but I, but you’re, you’re putting me on the clock. ‘cause my assistant prompt says like, you know, be pretty smart, but also try and respond to the user and it’s gonna respond.
And it’s like, ah, it got the wrong document. And then you do that once or twice as a knowledge worker and you’re just never
swyx:
again,
Aaron Levie:
never again. You’re just like done with the system.
swyx:
Yeah. It doesn’t work.
Aaron Levie:
It doesn’t work. And so, you know, Opus four six and Gemini three one Pro and you know, whatever the latest five 3G BT will be, like, those things are getting better and better and it’s using better judgment.
And this sort of like the, all of these updates to the agentic tool and search systems are, are, we’re seeing, we’re seeing very real progress where the agent. Kind of can, can almost smell some things a little bit fishy when it’s getting, you know, we, we have this process where we, we have it go fan out, do a bunch of searches, pull up a bunch of data, and then it has to sort of do its own ranking of, you know, what are the right documents that, that it should be working with.
And again, like, you know, the intelligence level of a model six months ago, [00:21:00] it’d be just throwing a dart at like, I’m just, I’m gonna grab these seven files and I, I pray, I hope that that’s the right answer. And something like an opus first four five, and now four six is like, oh, it’s like, no, that one doesn’t seem right relative to this question because I’m seeing some signal that is making that, you know, that’s contradicting the document where it would normally be in the tree and who should have access.
Like it’s doing all of that kind of work for you. But like, it still doesn’t work if you just have a total wasteland of data. Like, it’s just not, it’s just not possible. Partly ‘cause a human wouldn’t even be able to do it. So basically if a, if a really, really smart human. Could not do that task in five or 10 minutes for a search retrieval type task.
Look, you know, your agent’s not gonna be able to do it any better. You see this all day long. So
swyx:
this touches on a thing that just passionate about it was just context engineering. I, I’m just gonna let you ramble or riff on, on context engineering. If, if, if there’s anything like he, he did really good work on context fraud, which has really taken over as like the term that people use and the reference
Aaron Levie:
a hundred percent.
We, we all we think about is, is the context rob problem. [00:22:00]
Jeff Huber:
Yeah, there’s certainly a lot of like ranking considerations. Gentech surgery think is incredibly promising. Um, yeah, I was trying to generate a question though. I think I have a question right now. Swyx.
Aaron Levie:
Yeah, no, but like, like I think there was this moment, um, you know, like, I don’t know, two years ago before, before we knew like where the, the gotchas were gonna be in ai and I think someone was like, was like, well, infinite context windows will just solve all of these problems and ‘cause you’ll just, you’ll just give the context window like all the data and.
It’s just like, okay, I mean, maybe in 2035, like this is a viable solution. First of all, it, it would just, it would just simply cost too much. Like we just can’t give the model like the 5,000 documents that might be relevant and it’s gonna read them all. And I’ve seen enough to, to start believing in crazy stuff.
So like, I’m willing to just say, sure. Like in, in 10 years from now,
swyx:
never say, never, never.
Aaron Levie:
In, in 10 years from now, we’ll have infinite context windows at, at a thousandth of the price of today. Like, let’s just like believe that that’s possible, but Right. We’re in reality today. So today we have a context engineering [00:23:00] problem, which is, I got, I got, you know, 200,000 tokens that I can work with, or prob, I don’t even know what the latest graph is before, like massive degradation.
16. Okay. I have 60,000 tokens that I get to work with where I’m gonna get accurate information. That’s not a lot of tokens for a corpus of 10 million documents that a knowledge worker might have across all of the teams and all the projects and all the people they work with. I have, I have 10 million documents.
Which, you know, maybe is times five pages per document or something like that. I’m at 50 million pages of information and I have 60,000 tokens. Like, holy shit. Yeah. This is like, how do I bridge the 50 million pages of information with, you know, the couple hundred that I get to work with in that, in that token window.
Yeah. This is like, this is like such an interesting problem and that’s why actually so much work is actually like, just like search systems and the databases and that layer has to just get so locked in, but models getting better and importantly [00:24:00] knowing when they’ve done a search, they found the wrong thing, they go back, they check their work, they, they find a way to balance sort of appeasing the user versus double checking.
We have this one, we have this one test case where we ask the agent to go find. 10 pieces of information.
swyx:
Is this the complex work eval?
Aaron Levie:
Uh, this is actually not in the eval. This is, this is sort of just like we have a bunch of different, we have a bunch of internal benchmark kind of scenarios. Every time we, we update our agent, we have one, which is, I ask it to find all of our office addresses, and I give it the list of 10 offices that we have.
And there’s not one document that has this, maybe there should be, that would be a great example of the kind of thing that like maybe over time companies start to, you know, have these sort of like, what are the canonical, you know, kind of key areas of knowledge that we need to have. We don’t seem to have this one document that says, here are all of our offices.
We have a bunch of documents that have like, here’s the New York office and whatever. So you task this agent and you, you get, you say, I need the addresses for these 10 offices. Okay. And by the way, if you do this on any, you know, [00:25:00] public chat model, the same outcome is gonna happen. But for a different kind of query, you give it, you say, I need these 10 addresses.
How many times should the agent go and do its search before it decides whether or not, there’s just no answer to this question. Often, and especially the, the, let’s say lower tier models, it’ll come back and it’ll give you six of the 10 addresses. And it’ll, and I’ll just say I couldn’t find the other
swyx:
four.
It, it doesn’t know what It doesn’t know. It
Aaron Levie:
doesn’t know what It doesn’t know. Yeah. So the model is just like, like when should it stop? When should it stop doing? Like should it, should it do that task for literally an hour and just keep cranking through? Maybe I actually made up an office location and it doesn’t know that I made it up and I didn’t even know that I made it up.
Like, should it just keep, re should it read every single file in your entire box account until it, until it should exhaust every single piece of information.
swyx:
Expensive.
Aaron Levie:
These are the new problems that we have. So, you know, something like, let’s say a new opus model is sort of like, okay, I’m gonna try these types of queries.
I didn’t get exactly what I wanted. I’m gonna try again. I’m gonna, at [00:26:00] some point I’m gonna stop searching. ‘cause I’ve determined that that no amount of searching is gonna solve this problem. I’m just not able to do it. And that judgment is like a really new thing that the model needs to be able to have.
It’s like, when should it give up on a task? ‘cause, ‘cause you just don’t, it’s a can’t find the thing. That’s the real world of knowledge, work problems. And this is the stuff that the coding agents don’t have to deal with. Because they, it just doesn’t like, like you’re not usually asking it about, you’re, you’re always creating net new information coming right outta the model for the most part.
Obviously it has to know about your code base and your specs and your documentation, but, but when you deploy an agent on all of your data that now you have all of these new problems that you’re dealing with
Jeff Huber:
our, uh, follow follow-up research to context ride is actually on a genetic search. Ah. Um, and we’ve like right, sort of stress tested like frontier models and their ability to search.
Um, and they’re not actually that good at searching. Right. Uh, so you’re sort of highlighting this like explore, exploit.
swyx:
You’re just say, Debbie, Donna say everything doesn’t work. Like,
Aaron Levie:
well,
Jeff Huber:
somebody has to be,
Aaron Levie:
um, can I just throw out one more thing? Yeah. That is different from coding and, and the rest [00:27:00] of the knowledge work that I, I failed to mention.
So one other kind of key point is, is that, you know, at the end of the day. Whether you believe we’re in a slop apocalypse or, or whatever. At the end of the day, if you, if you build a working product at the end of, if you, if you’ve built a working solution that is ultimately what the customer is paying for, like whether I have a lot of slop, a little slop or whatever, I’m sure there’s lots of code bases we could go into in enterprise software companies where it’s like just crazy slop that humans did over a 20 year period, but the end customer just gets this little interface.
They can, they can type into it, it does its thing. Knowledge work, uh, doesn’t have that property. If I have an AI model, go generate a contract and I generate a contract 20 times and, you know, all 20 times it’s just 3% different and like that I, that, that kind of lop introduces all new kinds of risk for my organization that the code version of that LOP didn’t, didn’t introduce.
These are, and so like, so how do you constrain these models to just the part that you want [00:28:00] them to work on and just do the thing that you want them to do? And, and, you know, in engineering, we don’t, you can’t be disbarred as an engineer, but you could be disbarred as a lawyer. Like you can do the wrong medical thing In healthcare, you, there’s no, there’s no equivalent to that of engineering.
Like, do
swyx:
you want there to be, because I’ve considered software
Jeff Huber:
engineer. What’s that? Civil engineering there is, right? Not
Aaron Levie:
software civil engineer. Sure. Oh yeah, for sure. But like in any of our companies, you like, you know, you’ll be forgiven if you took down the site and, and we, we will do a rollback and you’ll, you’ll be in a meeting, but you have not been disbarred as an engineer.
We don’t, we don’t change your, you know, your computer science, uh, blame
Jeff Huber:
degree, this postmortem.
Aaron Levie:
Yeah, exactly. Exactly. So, so, uh, now maybe we collectively as an industry need to figure out like, what are you liable for? Not legally, but like in a, in a management sense, uh, of these agents. All sorts of interesting problems that, that, that, uh, that have to come out.
But in knowledge work, that’s the real hostile environments that we’re operating in. Hmm.
swyx:
I do think like, uh, a lot of the last year’s, 2025 story was the rise of coding agents and I think [00:29:00] 2026 story is definitely knowledge work agents. Yes. A hundred
Aaron Levie:
percent.
swyx:
Right. Like that would, and I think open claw core work are just the beginning.
Yes. Like it’s, the next one’s gonna just gonna be absolute craziness.
Aaron Levie:
It it is. And, and, uh, and it’s gonna be, I mean, again, like this is gonna be this, this wave where we, we are gonna try and bring as many of the practices from coding because that, that will clearly be the forefront, which is tell an agent to go do something and has an access to a set of resources.
You need to be responsible for reviewing it at the end of the process. That to me is the, is the kind of template that I just think goes across knowledge, work and odd. Cowork is a great example. Open Closet’s a great example. You can kind of, sort of see what Codex could become over time. These are some, some really interesting kind of platforms that are emerging.
swyx:
Okay. Um, I wanted to, we touched on evals a little bit. You had, you had the report that you’re gonna go bring up and then I was gonna go into like, uh, boxes, evals, but uh, go ahead. Talk about your genetic search thing.
Jeff Huber:
Yeah. Mostly I think kinda a few of the insights. It’s like number one frontier model is not good at search.
Humans have this [00:30:00] natural explore, exploit trade off where we kinda understand like when to stop doing something. Also, humans are pretty good at like forgetting actually, and like pruning their own context, whereas agents are not, and actually an agent in their kind of context history, if they knew something was bad and they even, you could see in the trace the reason you trace, Hey, that probably wasn’t a good idea.
If it’s still in the trace, still in the context, they’ll still do it again. Uhhuh. Uh, and so like, I think pruning is also gonna be like, really, it’s already becoming a thing, right? But like, letting self prune the con windows
swyx:
be a big deal. Yeah. So, so don’t leave the mistake. Don’t leave the mistake in there.
Cut out the mistake but tell it that you made a mistake in the past and so it doesn’t repeat it.
Jeff Huber:
Yeah. But like cut it out so it doesn’t get like distracted by it again. ‘cause really, you know, what is so, so it will repeat its mistake just because it’s been, it’s in
swyx:
the
Jeff Huber:
context. It’s
Aaron Levie:
in the context so much.
That’s a few shot example. Even if it, yeah.
Jeff Huber:
It’s like oh this
Aaron Levie:
is a great thing to go try even if
Jeff Huber:
it didn’t work.
Aaron Levie:
Yeah,
Jeff Huber:
exactly.
Aaron Levie:
So
Jeff Huber:
there’s like a bunch of stuff there. Just
Aaron Levie:
Groundhogs Day inside these models. Yeah. I’m gonna go keep doing the same wrong
Jeff Huber:
thing. Covering sense. I feel like, you know, some creator analogy you’re trying like fit a manifold in latent space, which kind is doing break program synthesis, which is kinda one we think about we’re doing right.
Like, you know, certain [00:31:00] facts might be like sort of overly pitting it. There are certain, you know, sec sectors of latent space and so like plug clean space. Yeah. And, uh, and
swyx:
so we have a bell, our editor as a bell every time you say that. So
Jeff Huber:
you have, you have to like remove those, like
swyx:
you shoulda a gong like TPN or something.
If
Jeff Huber:
we gong, you either remove those links to like kinda give it the freedom, kind of do what you need to do. So, but yeah. We’ll, we’ll release more soon. That’s
Aaron Levie:
awesome.
Jeff Huber:
That’ll, that’ll be cool.
swyx:
We’re a cerebral podcast that people listen to us and, and sort of think really deep. So yeah, we try to keep it subtle.
Okay. We try to keep it.
Aaron Levie:
Okay, fine.
swyx:
Um, you, you guys do, you guys do have EVs, you talked about your, your office thing, but, uh, you’ve been also promoting APEX agents and complex work. Uh, yeah, whatever you, wherever you wanna take this just Yeah. How you
Aaron Levie:
Apex is, is obviously me, core’s, uh, uh, kind of, um, agent eval.
We, we supported that by sort of. Opening up some data for them around how we kind of see these, um, data workspaces in, in the, you know, kind of regular economy. So how do lawyers have a workspace? How do investment bankers have a workspace? What kind of data goes into those? And so we, [00:32:00] we partner with them on their, their apex eval.
Our own, um, eval is, it’s actually relatively straightforward. We have a, a set of, of documents in a, in a range of industries. We give the agent previously did this as a one shot test of just purely the model. And then we just realized we, we need to, based on where everything’s going, it’s just gotta be more agentic.
So now it’s a bit more of a test of both our harness and the model. And we have a rubric of a set of things that has to get right and we score it. Um, and you’re just seeing, you know, these incredible jumps in almost every single model in its own family of, you know, opus four, um, you know, sonnet four six versus sonnet four five.
swyx:
Yeah. We have this up on screen.
Aaron Levie:
Okay, cool. So some, you’re seeing it somewhere like. I, I forget the to, it was like 15 point jump, I think on the main, on the overall,
swyx:
yes.
Aaron Levie:
And it’s just like, you know, these incredible leaps that, that are starting to happen. Um,
swyx:
and OP doesn’t know any, like any, it’s completely held out from op.
Aaron Levie:
This is not in any, there’s no public data which has, you know, Ben benefits and this is just a private eval that we [00:33:00] do, and then we just happen to show it to, to the world. Hmm. So you can’t, you can’t train against it. And I think it’s just as representative of. It’s obviously reasoning capabilities, what it’s doing at, at, you know, kind of test time, compute capabilities, thinking levels, all like the context rot issues.
So many interesting, you know, kind of, uh, uh, capabilities that are, that are now improving
swyx:
one sector that you have. That’s interesting.
swyx:
Uh, people are roughly familiar with healthcare and legal, but you have public sector in there.
Aaron Levie:
Yeah.
swyx:
Uh, what’s that? Like, what, what, what is that?
Aaron Levie:
Yeah, and, and we actually test against, I dunno, maybe 10 industries.
We, we end up usually just cutting a few that we think have interesting gains. All extras, won a lot of like government type documents. Um,
swyx:
what is that? What is it? Government type documents?
Aaron Levie:
Government filings. Like a tax
swyx:
return, like
Aaron Levie:
a probably not tax returns. It would be more of what would go the government be using, uh, as data.
So, okay. Um, so think about research that, that type of, of, of data sets. And then we have financial services for things like data rooms and what would be in an investment prospectus. Uhhuh,
swyx:
that one you can dog food.
Aaron Levie:
Yeah, exactly. Exactly. Yes. Yes. [00:34:00] So, uh, so we, we run the models, um, in now, you know, more of an agent mode, but, but still with, with kinda limited capacity and just try and see like on a, like, for like basis, what are the improvements?
And, and again, we just continue to be blown away by. How, how good these models are getting.
swyx:
Yeah, I mean, I think every serious AI company needs something like that where like, well, this is the work we do. Here’s our company eval. Yeah. And if you don’t have it, well, you’re not a serious AI company.
Aaron Levie:
There’s two dimensions, right?
So there’s, there’s like, how are the models improving? And so which models should you either recommend a customer use, which one should you adopt? But then every single day, we’re making changes to our agents. And you need to know
swyx:
if you regressed,
Aaron Levie:
if you know. Yeah. You know, I’ve been fully convinced that the whole agent observability and eval space is gonna be a massive space.
Um, super excited for what Braintrust is doing, excited for, you know, Lang Smith, all the things. And I think what you’re going to, I mean, this is like every enter like literally every enterprise right now. It’s like the AI companies are the customers of these tools. Every enterprise will have this. Yeah, you’ll just [00:35:00] have to have an eval.
Of all of your work and like, we’ll, you’ll have an eval of your RFP generation, you’ll have an eval of your sales material creation. You’ll have an eval of your, uh, invoice processing. And, and as you, you know, buy or use new agentic systems, you are gonna need to know like, what’s the quality of your, of your pipeline.
swyx:
Yeah.
Aaron Levie:
Um, so huge, huge market with agent evals.
swyx:
Yeah.
swyx:
And, and you know, I’m gonna shout out your, your team a bit, uh, your CTO, Ben, uh, did a great talk with us last year. Awesome. And he’s gonna come back again. Oh, cool. For World’s Fair.
Aaron Levie:
Yep.
swyx:
Just talk about your team, like brag a little bit. I think I, I think people take these eval numbers in pretty charts for granted, but No, there, I mean, there’s, there’s lots of really smart people at work during all this.
Aaron Levie:
Biggest shout out, uh, is we have a, we have a couple folks at Dya, uh, Sidarth, uh, that, that kind of run this. They’re like a, you know, kind of tag tag team duo on our evals, Ben, our CTO, heavily involved Yasha, head of ai, uh, you know, a bunch of folks. And, um, evals is one part of the story. And then just like the full, you know, kind of AI.
An agent team [00:36:00] is, uh, is a, is a pretty, you know, is core to this whole effort. So there’s probably, I don’t know, like maybe a few dozen people that are like the epicenter. And then you just have like layers and layers of, of kind of concentric circles of okay, then there’s a search team that supports them and an infrastructure team that supports them.
And it’s starting to ripple through the entire company. But there’s that kind of core agent team, um, that’s a pretty, pretty close, uh, close knit group.
swyx:
The search team is separate from the infra team.
Aaron Levie:
I mean, we have like every, every layer of the stack we have to kind of do, except for just pure public cloud.
Um, but um, you know, we, we store, I don’t even know what our public numbers are in, you know, but like, you can just think about it as like a lot of data is, is stored in box. And so we have, and you have every layer of the, of the stack of, you know, how do you manage the data, the file system, the metadata system, the search system, just all of those components.
And then they all are having to understand that now you’ve got this new customer. Which is the agent, and they’ve been building for two types of customers in the past. They’ve been building for users and they’ve been building for like applications. [00:37:00] And now you’ve got this new agent user, and it comes in with a difference of it, of property sometimes, like, hey, maybe sometimes we should do embeddings, an embedding based, you know, kind of search versus, you know, your, your typical semantic search.
Like, it’s just like you have to build the, the capabilities to support all of this. And we’re testing stuff, throwing things away, something doesn’t work and, and not relevant. It’s like just, you know, total chaos. But all of those teams are supporting the agent team that is kind of coming up with its requirements of what, what do we need?
swyx:
Yeah. No, uh, we just came from, uh, fireside chat where you did, and you, you talked about how you’re doing this. It’s, it’s kind of like an internal startup. Yeah. Within the broader company. The broader company’s like 3000 people. Yeah. But you know, there’s, there’s a, this is a core team of like, well, here’s the innovation center.
Aaron Levie:
Yeah.
swyx:
And like that every company kind of is run this way.
Aaron Levie:
Yeah. I wanna be sensitive. I don’t call it the innovation center. Yeah. Only because I think everybody has to do innovation. Um, there, there’s a part of the, the, the company that is, is sort of do or die for the agent wave.
swyx:
Yeah.
Aaron Levie:
And it only happens to be more of my focus simply because it’s existential that [00:38:00] we get it right.
swyx:
Yeah.
Aaron Levie:
All of the supporting systems are necessary. All of the surrounding adjacent capabilities are necessary. Like the only reason we get to be a platform where you’d run an agent is because we have a security feature or a compliance feature, or a governance feature that, that some team is working on.
But that’s not gonna be the make or break of, of whether we get agents right. Like that already exists and we need to keep innovating there. I don’t know what the right, exact precise number is, but it’s not a thousand people and it’s not 10 people. There’s a number of people that are like the, the kind of like, you know, startup within the company that are the make or break on everything related to AI agents, you know, leveraging our platform and letting you work with your data.
And that’s where I spend a lot of my time, and Ben and Yosh and Diego and Teri, you know, these are just, you know, people that, that, you know, kind of across the team. Are working.
swyx:
Yeah. Amazing.
Jeff Huber:
How do you, how do you think about, I mean, you talked a lot about like kinda read workflows over your box data. Yep.
Right. You know, gen search questions, queries, et cetera. But like, what about like, write or like authoring workflows?
Aaron Levie:
Yes. I’ve [00:39:00] already probably revealed too much actually now that I think about it. So, um, I’ve talked about whatever,
Jeff Huber:
whatever you can.
Aaron Levie:
Okay. It’s just us. It’s just us. Yeah. Okay. Of course, of course.
So I, I guess I would just, uh, I’ll make it a little bit conceptual, uh, because again, I’ve already, I’ve already said things that are not even ga but, but we’ve, we’ve kinda like danced around it publicly, so I, yeah, yeah. Okay. Just like, hopefully nobody watches this, um, episode. No.
swyx:
It’s tidbits for the Heidi engaged to go figure out like what exactly, um, you know, is, is your sort of line of thinking.
Sure. They can connect the dots.
Aaron Levie:
Yeah. So, so I would say that, that, uh, we, you know, as a, as a place where you have your enterprise content, there’s a use case where I want to, you know, have an agent read that data and answer questions for me. And then there’s a use case where I want the agent to create something.
And use the file system to create something or store off data that it’s working on, or be able to have, you know, various files that it’s writing to about the work it’s doing. So we do see it as a total read write. The harder problem has so far been the read only because, because again, you have that kind of like 10 [00:40:00] million to one ratio problem, whereas rights are a lot of, that’s just gonna come from the model and, and we just like, we’ll just put it in the file system and kinda use it.
So it’s a little bit of a technically easier problem, but the only part that’s like, not necessarily technically hard, it is just like it’s not yet perfected in the state of the ecosystem is, you know, building a beautiful PowerPoint presentation. It’s still a hard problem for these models. Like, like we still, you know, like, like these formats are just, we’re not built for.
They’re
swyx:
working on it.
Aaron Levie:
They’re, they’re working on it. Everybody’s working on it.
swyx:
Every launch is like, well, we do PowerPoint now.
Aaron Levie:
We’re getting, yeah, getting a lot, getting a lot of better each time. But then you’ll do this thing where you’ll ask the update one slide and all of a sudden, like the fonts will be just like a little bit different, you know, on two of the slides, or it moved, you know, some shape over to the left a little bit.
And again, these are the kind of things that, like in code, obviously you could really care about if you really care about, you know, how beautiful is the code, but at the end, user doesn’t notice all those problems and file creation, the end user instantly sees it. You’re [00:41:00] like, ah, like paragraph three, like, you literally just changed the font on me.
Like it’s a totally different font and like midway through the document. Mm-hmm. Those are the kind of things that you run into a lot of in the, in the content creation side. So, mm-hmm. We are gonna have native agents. That do all of those things, they’ll be powered by the leading kind of models and labs.
But the thing that I think is, is probably gonna be a much bigger idea over time is any agent on any system, again, using Box as a file system for its work, and in that kind of scenario, we don’t necessarily care what it’s putting in the file system. It could put its memory files, it could put its, you know, specification, you know, documents.
It could put, you know, whatever its markdown files are, or it could, you know, generate PDFs. It’s just like, it’s a workspace that is, is sort of sandboxed off for its work. People can collaborate into it, it can share with other people. And, and so we, we were thinking a lot about what’s the right, you know, kind of way to, to deliver that at scale.
swyx:
I wanted to come into sort of the sort of AI transformation or AI sort of, uh, operations things. [00:42:00] Um, one of the tweets that you, that you wanted to talk about, this is just me going through your tweets, by the way. Oh, okay. I mean, like, this is, you read
Aaron Levie:
one by one,
swyx:
you’re the, you’re the easiest guest to prep for because you, you already have like, this is the, this is what I’m interested in.
I’m like, okay, well, are
Aaron Levie:
we gonna get to like, like February, January or something? Where are we in the, in the timelines? How far back are we going?
swyx:
Can you, can you describe boxes? A set of skills? Right? Like that, that’s like, that’s like one of the extremes of like, well if you, you just turn everything into a markdown file.
Yeah. Then your agent can run your company. Uh, like you just have to write, find the right sequence of words to
Aaron Levie:
Yes.
swyx:
To do it.
Aaron Levie:
Sorry, is
that
swyx:
the question? So I think the question is like, what if we documented everything? Yes. The way that you exactly said like,
Aaron Levie:
yes.
swyx:
Um, let’s get all the Fortune five hundreds, uh, prepared for agents.
Yes. And like, you know, everything’s in golden and, and nicely filed away and everything. Yes. What’s missing? Like, what’s left, right? Like
Aaron Levie:
Yeah.
swyx:
You’ve, you’ve run your company for a decade. Like
Aaron Levie:
Yeah. I think the challenge is that, that that information changes a week later. And because something happened in the market for that [00:43:00] customer, or us as a company that now has to go get updated, and so these systems are living and breathing and they have to experience reality and updates to reality, which right now is probably gonna be humans, you know, kinda giving those, giving them the updates.
And, you know, there is this piece about context graphs as as, uh, that kinda went very viral. Yeah. And I, I, I was like a, i, I, I thought it was super provocative. I agreed with many parts of it. I disagree with a few parts around. You know, it’s not gonna be as easy as as just if we just had the agent traces, then we can finally do that work because there’s just like, there’s so much more other stuff that that’s happening that, that we haven’t been able to capture and digitize.
And I think they actually represented that in the piece to be clear. But like there’s just a lot of work, you know, that that has to, you just can’t have only skills files, you know, for your company because it’s just gonna be like, there’s gonna be a lot of other stuff that happens. Yeah. Change over time.
Yeah. Most companies are practically apprenticeships.
swyx:
Most companies are practically apprenticeships. Like
Jeff Huber:
every new employee who joins the team, [00:44:00] like you span one to three months. Like ramping them up.
Aaron Levie:
Yes. All
Jeff Huber:
that tat knowledge
Aaron Levie:
is
Jeff Huber:
not written down.
Aaron Levie:
Yes.
Jeff Huber:
But like, it would have to be if you wanted to like give it to an Asian.
Right. And so like that seems to me like to be
Aaron Levie:
one is I think you’re gonna see again a premium on companies that can document this. Mm-hmm. Much. There’ll be a huge premium on that because, because you know, can you shorten that three month ramp cycle to a two week ramp cycle? That’s an instant productivity gain.
Can you re dramatically reduce rework in the organization because you’ve documented where all the stuff is and where the answers are. Can you make your average employee as good as your 90th percentile employee because you’ve captured the knowledge that’s sort of in the heads of, of those top employees and make that available.
So like you can see some very clear productivity benefits. Mm-hmm. If you had a company culture of making sure you know your information was captured, digitized, put in a format that was agent ready and then made available to agents to work with, and then you just, again, have this reality of like add a 10,000 person [00:45:00] company.
Mapping that to the, you know, access structure of the company is just a hard problem. Is like, is like, yeah, well, you just, not every piece of information that’s digitized can be shared to everybody. And so now you have to organize that in a way that actually works. There was a pretty good piece, um, this, this, uh, this piece called your company as a file is a file system.
I, did you see that one?
swyx:
Nope.
Aaron Levie:
Uh, yes. You saw it. Yeah. And, and, uh, I actually be curious your thoughts on it. Um, like, like an interesting kind of like, we, we agree with it because, because that’s how we see the world and, uh,
swyx:
okay. We, we have it up on screen. Oh,
Aaron Levie:
okay. Yeah. But, but it’s all about basically like, you know, we’ve already, we, we, we already organized in this kind of like, you know, permission structure way.
Uh, and, and these are the kind of, you know, natural ways that, that agents can now work with data. So it’s kind of like this, this, you know, kind of interesting metaphor, but I do think companies will have to start to think about how they start to digitize more, more of that data. What was your take?
Jeff Huber:
Yeah, I mean, like the company’s probably like an acid compliant file system.
Aaron Levie:
Uh,
Jeff Huber:
yeah. Which I’m guessing boxes, right? So, yeah. Yes.
swyx:
Yeah. [00:46:00]
Jeff Huber:
Which you have a great piece on, but,
swyx:
uh, yeah. Well, uh, I, I, my, my, my direction is a little bit like, I wanna rewind a little bit to the graph word you said that there, that’s a magic trigger word for us. I always ask what’s your take on knowledge graphs?
Yeah. Uh, ‘cause every, especially at every data database person, I just wanna see what they think. There’s been knowledge graphs, hype cycles, and you’ve seen it all. So.
Aaron Levie:
Hmm. I actually am not the expert in knowledge graphs, so, so that you might need to
swyx:
research, you don’t need to be an expert. Yeah. I think it’s just like, well, how, how seriously do people take it?
Yeah. Like, is is, is there a lot of potential in the, in the HOVI?
Aaron Levie:
Uh, well, can I, can I, uh, understand first if it’s, um, is this a loaded question in the sense of are you super pro, super con, super anti medium? I
swyx:
see pro, I see pros and cons. Okay. Uh, but I, I think your opinion should be independent of mine.
Aaron Levie:
Yeah. No, no, totally. Yeah. I just want to see what I’m stepping into.
swyx:
No, I know. It’s a, and it’s a huge trigger word for a lot of people out Yeah. In our audience. And they’re, they’re trying to figure out why is that? Because why
Aaron Levie:
is this such a
swyx:
hot item for them? Because a lot of people get graph religion.
And they’re like, everything’s a graph. Of course you have to represent it as a graph. Well, [00:47:00] how do you solve your knowledge? Um, changing over time? Well, it’s a graph.
Aaron Levie:
Yeah.
swyx:
And, and I think there, there’s that line of work and then there’s, there’s a lot of people who are like, well, you don’t need it. And both are right.
Aaron Levie:
Yeah. And what do the people who say you don’t need it, what are they
swyx:
arguing for Mark down files. Oh, sure, sure. Simplicity.
Aaron Levie:
Yeah.
swyx:
Versus it’s, it’s structure versus less structure. Right. That’s, that’s all what it is. I do.
Aaron Levie:
I think the tricky thing is, um, is, is again, when this gets met with real humans, they’re just going to their computer.
They’re just working with some people on Slack or teams. They’re just sharing some data through a collaborative file system and Google Docs or Box or whatever. I certainly like the vision of most, most knowledge graph, you know, kind of futuristic kind of ways of thinking about it. Uh, it’s just like, you know, it’s 2026.
We haven’t seen it yet. Kind of play out as as, I mean, I remember. Do you remember the, um, in like, actually I don’t, I don’t even know how old you guys are, but I’ll for, for to show my age. I remember 17 years ago, everybody thought enterprises would just run on [00:48:00] Wikis. Yeah. And, uh, confluence and, and not even, I mean, confluence actually took off for engineering for sure.
Like unquestionably. But like, this was like everything would be in the w. And I think based on our, uh, our, uh, general style of, of, of what we were building, like we were just like, I don’t know, people just like wanna workspace. They’re gonna collaborate with other people.
swyx:
Exactly. Yeah. So you were, you were anti-knowledge graph.
Aaron Levie:
Not anti, not anti. So
swyx:
not non
Aaron Levie:
I’m not, I’m not anti. ‘cause I think, I think your search system, I just think these are two systems that probably, but like, I’m, I’m not in any religious war. I don’t want to be in anybody’s YouTube comments on this. There’s not a fight for me.
swyx:
We, we love YouTube comments. We’re, we’re, we’re get into comments.
Aaron Levie:
Okay. Uh, but like, but I, I, it’s mostly just a virtue of what we built. Yeah. And we just continued down that path. Yeah.
swyx:
Yeah.
Aaron Levie:
And, um, and that, that was what we pursued. But I’m not, this is not a, you know, kind of, this is not a, uh, it’s
swyx:
not existential for you. Great.
Aaron Levie:
We’re happy to plug into somebody else’s graph.
We’re happy to feed data into it. We’re happy for [00:49:00] agents to, to talk to multiple systems. Not, not our fight.
swyx:
Yeah.
Aaron Levie:
But I need your answer. Yeah. Graphs or nerd Snipes is very effective nerd.
swyx:
See this is, this is one, one opinion and then I’ve,
Jeff Huber:
and I think that the actual graph structure is emergent in the mind of the agent.
Ah, in the same way it is in the mind of the human. And that’s a more powerful graph ‘cause it actually involved over time.
swyx:
So don’t tell me how to graph. I’ll, I’ll figure it out myself. Exactly. Okay. All right. And
Jeff Huber:
what’s yours?
swyx:
I like the, the Wiki approach. Uh, my, I’m actually like, uh, you know, obviously I spent some my time at cognition, which, uh, you, you know very well.
Yep. And they’ve had a lot of success with Deep Wiki. Yeah. It powers a lot of Devrel and brain
Aaron Levie:
super powerful.
swyx:
And it’s super, it’s useful for humans, but it’s, oh my God, it’s useful for agents.
Aaron Levie:
Yes. Tell me if you think I’m, I’m wrong on this, but, but not much of an access control structure issue?
swyx:
No.
Aaron Levie:
There’s like the whole, you get the whole code base and everybody gets to,
swyx:
well, before, before I speak too much, there may be some enterprise controls on Sure.
The enterprise Deb offering that I’m not familiar with. Yeah. But yeah, I don’t, I don’t have any, anything on the public side. But, you know, I, I think like, almost like every agent should have its [00:50:00] own wiki that it’s updating and that’s. Persistent memory and yeah, that is a very weak knowledge graph.
Jeff Huber:
Yeah.
swyx:
And you, you could strengthen it if you want more structure, but you may not need it.
Jeff Huber:
Markdown files, having links and wiki style. Right. Yep. Very effective. Right, Lindy?
Aaron Levie:
Yep.
swyx:
I like that. As a, as a just general pattern. Um, okay. So, uh, last couple questions. Sure. But feel free to jump on in or, or if you want any rants.
Um, I see you as a very interesting and, and unusual founder where, like, you’ve been in a business and you are, you’re both like, you’re off like of two worlds, like you’re of Silicon Valley, but you’re also of the Fortune five hundreds. And like, I feel like your kind of founder mode is very different from the Brian Chesky founder mode.
And I’m just kinda curious if you have like ref reflections on like how you operate as a founder,
Aaron Levie:
what would his founder mode be?
swyx:
Don’t delegate.
Aaron Levie:
Ah, right. And what, how would you put me,
swyx:
you do delegate. Ah,
Aaron Levie:
okay. I, I, I, I see the, um, I think that I, I don’t know that Brian and I would be that far removed from each other when you get to the specifics.
swyx:
Okay.
Aaron Levie:
So there’s a whole bunch that I delegate, [00:51:00] 90%. Of the work that happens at Box is fully, you know, fully delegated. We’ve got great leaders running, running, all that stuff. It’s just too much for my brain to handle. And probably 70% of the work, I’m gonna make up all the numbers here, probably 70% of the work at Box or 70, 80% of the work at Box.
I only need to really look at about 5% of that for like, some high leverage decisions to be involved in, you know, what’s the marketing message that we think is gonna resonate with, with customers. So that’s a little bit of high leverage thing that, that, that we do in marketing. But most of marketing activities I don’t get involved in.
What’s our sales pitch? Maybe I’ll be involved in that a little bit. Or like what’s roughly the investments or push we’re gonna do in certain verticals. You know, that’s about 5% of like the total bandwidth of, you know, this, the, the key areas of sales or go to market. Okay. So like. 70, 80% of the company, I can just do about 5%.[00:52:00]
And then, and then just like operationally, we’ve got great leaders and they’re gonna execute on that, and we collaborate on the 5% anyway. It’s not like I’m just like making up a decision and, and saying to go and do it. Then there’s this part that is like the existential part of the business, which is if we don’t do this right, we’re out of business.
And, uh, by virtue of just being a founder, you get kind of sucked into that part of the work because you can feel it. Like, this is like, like you can just see how the AI tsunami could wipe you out if you make just 2, 3, 4, 5 wrong decisions in this space. Like couple wrong architecture decisions, couple wrong AI feature decisions, couple wrong API platform decisions, and, and you might be out of the game in a year from now and like, you just feel it in your bones.
You, you know, this, uh, like, it’s just like, like, like we feel this all day long in this space given what’s happening. Hmm. And so that, in that area. It’s, you can’t kind of delegate in a classic sense. You still need to make sure you’ve got great leaders and strong hires and people that, that are have high agency.
‘cause [00:53:00] they wanna be able to the own part of the, the strategy and the roadmap or else you can’t hire good people. But, but you know, there’s gonna be a lot of little micro forks in the road that they will compound to determine whether you’ve succeed or fail. And so your kind of founder energy just like automatically draws you into, into those because, because they are the determining decisions of, of your company’s future.
And that’s kind of where I spend my time and I, and you have to kind of, you know, do it in a collaborative way again, because if you are only dictatorial and just, you know, you just won’t, won’t eventually be able to hire the best people. ‘cause they won’t wanna work on that environment. But you also just can’t like.
Abdicate all the responsibility because the risks are, are just simply too high. Like, and so you have to somehow, obviously, add some value. And so the value I add is I’ve seen 20 years of this business, so I, I think I can kind of piece together what I expect the value propositions are gonna be and how customers will react to certain things.
So that’s what I can bring to the table. And then you have this kind of existential fear of, if I get it wrong, it’s all on me anyway. [00:54:00] I don’t get to blame, you know, you know, the engineer that was working on that project, like, it’s all, it’s, it’s, it’s my fault, right? Like at the end of the day, it’ll be my fault if it doesn’t work.
So by virtue of of that liability, uh, responsibility, you just get pulled into needing to make sure like it’s all going a according to, to kind of how you think it needs to end up. I don’t, I don’t know how Brian would answer that, I guess, but like I, I, yeah,
swyx:
it’s a long essay. It’s an interesting essay.
People should go and compare and contrast your answer versus his, uh, I do think that, um, systems have a way of letting entropy get to them. Yep. And you, you, if you step away for too long, you need to have a way to like check in and go like, well, do I need to come back in? Or are we good? And people are gonna tell you things are good, but they’re not good.
Yes,
Aaron Levie:
yes. A hundred percent.
swyx:
Yeah.
Aaron Levie:
And that’s actually, I’m, um, I’m a fan of actually process for the, that 70 to 80%.
swyx:
Yeah.
Aaron Levie:
So that 70 to 80% the process is you’re gonna do a, you know, a quarterly business review and you’re gonna have a brand check-in, and you’re gonna do [00:55:00] those, like, you’re gonna make sure that, that you’re seeing all the, the right episodes of, of what’s changing and, and how, and how it’s kind of, you know, evolving and, and make sure it’s kind of going the right direction.
And then there’s some areas which is like, no, it’s 24 7. Like, like I guarantee after this podcast at 11:00 PM I’ll be doing a Zoom with Ben, uh, and probably some other people. ‘cause we’re gonna be talking about agents and, and new platform features and like, that’s amazing. That’s your just in the cauldron, you know, kind of grinding on, on, on that side.
swyx:
Yeah. Yeah. That’s, uh, that’s extremely, um, realistic. Yeah. What is, what it’s like, and I just want to have people hear your perspective on what,
Aaron Levie:
and this is what you like, and this is the, this is this like, um, you read the post about, you know, everybody having agents running on the weekend and, um, and it’s like, uh, you know, you, you just.
I mean, first of all, anybody crazy enough to come to Silicon Valley? Like we don’t bring good news about the sort of like healthiness of our environment right now. Like, like, like you have to,
swyx:
and
Aaron Levie:
[00:56:00] you have to know what you’re signing up for. But like, like, you know, there, there’s a real issue, which is like, shoot, do I have enough agents running?
And, and
swyx:
oh yeah, I made a meme that was like semi viral for me about this. Exactly, yes. That was incredible. That’s,
Aaron Levie:
and, and, and that, that
swyx:
was, you can’t even enjoy a party these days. Becausecause, you’re working with your tokens.
Aaron Levie:
No. You just compute out there that you’re not utilizing,
swyx:
what the hell? Like,
so
Aaron Levie:
like there’s
swyx:
ad I paid for the $200, I’m gonna spend the $200.
Aaron Levie:
Yeah.
swyx:
Uh, I’m gonna spend $6,000 out of 200 bucks. Yeah, exactly.
Jeff Huber:
Exactly.
Aaron Levie:
We
Jeff Huber:
need to make anthropic very unprofitable. So,
swyx:
yeah. Yeah. We’re not doing a good enough job. Cool.
swyx:
I have a closing question. If you, unless you,
Jeff Huber:
I have a question. I’ve asked this question in private before, but I ask it again, which is, uh, it’s a question that Tyler Cowen asks his guests on his podcast, which is, uh, what is the Aaron Levy production function?
And, uh, uh
swyx:
Oh, I love
Jeff Huber:
that. I love this question because there’s so a few people that I think are good at both executing. Also like distilling and like, just putting good ideas into the ether. Mm-hmm. You put a lot of good ideas into the ether. And so like what is the air levee production function that allows you you to do that versus others?[00:57:00]
Aaron Levie:
How do I get that information? Or
swyx:
I, I can give you a, a, a variant. Yeah. Which is what goes into air and levee.
Aaron Levie:
Yeah.
swyx:
And what goes out and how does it turn inside? Yeah.
Aaron Levie:
I’m just trying to think of, ‘cause I mean, you know, there’s some very, I, I just read a lot of Twitter, uh, as well. And so like, I just, and you’ve, you
swyx:
spent a lot of effort
Aaron Levie:
too.
Jeff Huber:
Contrast, you don’t see like, great. Many essays from Brian Chesky every day.
Aaron Levie:
Uh,
Jeff Huber:
but you
Aaron Levie:
do
Jeff Huber:
from you.
Aaron Levie:
Oh, yeah. And you’re
Jeff Huber:
kind of weird in that way, so
Aaron Levie:
why? Maybe he’s, he, maybe he’s healthier than me. Actually. We should just like, we should just text him to see if, you know, he’s got a more I think he does
swyx:
work out.
Aaron Levie:
Yeah. He got bigger
swyx:
muscles.
Aaron Levie:
That’s the thing. I, I work out less than him and I tweet more than him. So, so that’s the, that’s how we’re balancing things out. I am, um, I mostly, the way I just think about it is, uh, is just, um, you know, there’s, there’s lots of work that’s happening in the business. I am getting to see the, all the problems that we are running into constantly.
And I am trying to, uh, be a little bit of a, create a flywheel between what we’re doing [00:58:00] internally, what, what, what. Then we talk about, uh, getting a feedback loop on that and seeing other people’s, you know, experiences of what they’re doing. Bring that back into the business. And, and so I just see, uh, like my job is as, you know, hopefully being able to kind of connect the dots.
Of, of what’s going on in the world with what’s going on in box. And then I just happened to tweet about that along the way.
swyx:
Yeah.
Aaron Levie:
Um, because
swyx:
it’s all you, there’s no like,
Aaron Levie:
yeah.
swyx:
Editor,
Aaron Levie:
there’s no,
swyx:
yeah.
Aaron Levie:
Yeah.
swyx:
Wow.
Aaron Levie:
The, uh, I got, um, there was a funny, uh, uh, my, I, I tried to get an internship in, um, between freshman and sophomore year of this company, and it was a, it was a film, uh, kind of production company in New York.
And, uh, I got the internship and then I emailed my liaison kind of guy who sponsored me for the internship and I said, Hey, I’d like to do a blog of my summer internship. Hmm. Where I blog about, you know, the, the being an intern at a production company in New York and. About like a, I dunno, half a day, a day later, [00:59:00] uh, they emailed me back saying they’ve rescinded the internship.
swyx:
No.
Aaron Levie:
Um, uh, yeah, because, because I showed a lack of judgment on, you know, professionalism, you know, or whatever. Like, like just even the, the idea that I would ask that question, red flags went up of like, who the fuck is this guy? So anyway, I, I only say that to say that like, like to me, just like, you know, building in public is just like a natural, is a natural thing.
And so I, so I just, you know, go through the day. We, we deal with interesting problems. I tweet about them. I get information back in the process. I, I see your work. I see your work. You know, I see a bunch of folks and, and try and, you know, kind of incorporate that back in the box. My job is to try and connect all these things together and, uh, and make, make it useful.
swyx:
And you’re, I mean, you’re the number one spokesperson, right? So you do have to be out there.
Aaron Levie:
Yeah, I, but I, I kind of would be doing it whether or not, like it’s, I don’t really think of it as a job requirement as much as like, I just like, I like social media.
Jeff Huber:
You’re so good at it.
Aaron Levie:
Yeah.
Jeff Huber:
It’s so hard to believe.
So like,
Aaron Levie:
okay, sorry.
Jeff Huber:
Do you get up at 5:00 AM [01:00:00] with coffee? Is that your secret? It’s like, how do you work or do you actually just like, in the back of Waymo’s, like, is, do you do it that way? Like how do you do this?
Aaron Levie:
It’s, it’s, no, it’s, it’s, it’s mostly that though. It’s mostly, uh, there’s a, you know, I, I, I have a commute home each night.
I try and see, you know, my kids’ most, most weekdays before I have to hop back online. So there’s like a 20 minute window there.
Jeff Huber:
Okay.
Aaron Levie:
Where I can kinda like distill the information that’s happened and nice. And be like, ah, is there anything I learned today that would be interesting to throw out there? Or anything that I saw.
And then probably somewhere between like seven 30 and 9:00 PM I finally get a chance to like look through the feed. Mm. And see like, did anything crazy happen in ai? And, um, uh, and then that’s, that will also kind of catalyze, you know, something Yep. As like, that’s the best I can kind of,
swyx:
you
Aaron Levie:
know, respect.
Yeah. Okay. Thanks.
swyx:
Uh, and now I know you, you cut off his 8:00 PM I will try to get AI news out before 8:00 PM so I can help him.
Aaron Levie:
Yeah.
swyx:
Do, do his thing.
Aaron Levie:
Ba basically, if, if I [01:01:00] don’t see it before eight to eight 30, I’m not gonna
swyx:
Yeah. It’s, I’m gonna
Aaron Levie:
be able to like court tweet or something.
swyx:
Yeah,
yeah.
Aaron Levie:
Uh, because, uh, because then I’m back on Zoom after that,
swyx:
so I wasn’t gonna plan on asking this, but you’ve mentioned, uh, you mentioned the film stuff.
Aaron Levie:
Yeah.
swyx:
And I know from one of my favorite parts of doing your research on you was that, uh, you got the idea for Box from like, the, the Paramount lot. Yeah. Uh, pushing paper. Uh, are you film guy? You, you’re a big,
Aaron Levie:
uh, I, I I, I, I would say I used to be more of a film guy.
swyx:
Yeah. What, what’s your, what what, what are your favorites?
If you have, you wanna list off any
Aaron Levie:
kind of the classic, uh, wannabe film student classics are, are you
swyx:
talking Scorsese?
Aaron Levie:
Yeah. Panino, pop Fiction, Magnolia. Requiem for a dream, basically. Like if there was an art house film in the nineties, uh, to early two thousands, that was my genre. Yeah. That got me into like, wow, wouldn’t it be cool to do, you know, you know, film.
And then I, I thought maybe I could connect digital into it. Like, could you, could you do film online? That just seemed too [01:02:00] hard from a licensing standpoint. And then obviously Netflix, you know, kind of existed. Um, so I, I never quite was able to fully connect the dots on these things. But the internship at Paramount, um, was one kind of catalyst for starting box because we were using just traditional enterprise software.
And I was like, wow. It’s like really hard to share data, you know, just like files going back and forth. Um, but the same thing was happening in school as well, and so that all led to, led the box basically.
swyx:
Um, well, a 24 is, uh, you know, kind of giving back the sort of resurgence of the independent film, I guess a
Aaron Levie:
hundred percent.
swyx:
Um, uh, in, in, in, in the face of all the Marvel slop.
Aaron Levie:
Uh, you know, I was thinking about this the other day, and a 24 is, you know, uh, certainly the best, uh, EE example I’m sure of, of this today. But, um, you know, they just don’t, you know, you, it’s hard to make a film, uh, like, you know, no country for old men or, um, there will be blood like, like what is that movie today?
swyx:
Yeah.
Aaron Levie:
Like what is a brand new movie that is just like original? [01:03:00] You just watch it and you’re like, what, what did I just watch? So
swyx:
my, my, you know, sixes movie bench is, uh, Forrest Gump.
Aaron Levie:
Okay.
swyx:
Which iconic in its time.
Aaron Levie:
Yep. A hundred percent.
swyx:
Never again.
Aaron Levie:
Yeah. Yeah. We, we did not make, we don’t know how to make Fors Gump anymore.
Um, they will try it with the sequel
Jeff Huber:
though, at some point.
Aaron Levie:
For sure. I, I honestly fors
swyx:
Gump two in 30
Aaron Levie:
years. I’ll be fine with it. No, that Fors Gump has a kid. Like he’s still right. Yeah, he’s still right. Exactly. Um, I think for Gump has a grandkid would be like a good movie. Like what is the grandkid of Forres Gump doing in, uh, in 2026
swyx:
goes tropical.
Aaron Levie:
Yeah. But, um, yeah, I definitely, let’s, I wanna see good, I wanna see more movies out there.
Aaron Levie:
You know, I’m a little bit conflicted on AI and film because,
swyx:
oh, that, let’s see that.
Aaron Levie:
Well, because I, uh, the world does not need more slop on, on AI entertainment, but I’m kind of like in a mode where I think that AI is, is, is gonna be, you know, generally a pure positive.
Because if I’m a, [01:04:00] if I was me 25 years ago in high school, for sure, I would be making a full production film. That had explosions and car chases and, but then there’d be like people that would show up there. So like I think that ability to, to just, you get to be Spielberg, you know, is, is, you know, completely amazing and, and democratizing.
That is incredible. And I, you know, I’m, I’m concerned about like, how do you make sure that we still get PT Anderson. Along the way and, and can we make sure that those, those guys exist? And then interestingly, I never, and I never saw it, but Darren Aronofsky, I, I believe, has either put out or gonna put out a, an AI film, you know, even some of the best artists are, are, you know, starting to adopt this.
But, um, uh, but yeah, I, I definitely don’t want to, what I don’t wanna do is just be like in this like TikTok feed of just films and it’s just like, oh, this film about the car chase that does this thing. And it says like, we don’t need that. Like, like, [01:05:00] like this should be a form of entertainment and art and let’s use AI to accelerate the production process.
Do the really hard CG work that, that you just, you had to spend way too much money on previously to do the, you know, kind of like, let’s, let’s use it to test out all new kind of plot ideas. Uh, yeah. Previs.
Jeff Huber:
Yeah, exactly. Like
Aaron Levie:
backgrounds and that’s incredible. Like whatever. Yeah. And all those things are super incredible.
I still like the, it’s very nostalgic, but I still like the idea of like. This is a camera and a person and a person that says, you know, action. Uh, and then, and let’s hopefully like surround AI around that. Yeah. We’ll, but we’ll, we’ll see how that plays out.
swyx:
Yeah. I think, you know, so one of the things that stability ai, uh, made an impression on me was like, well, you know, and at least now we can remake Game of Throne Season eight, and I can, you know, uh, like, like it was meant to be not, uh, not rushed.
Yeah.
Aaron Levie:
And then you watch, um, well I have a six and a half year old and I, you know, you see a lot of these kid movies and you’re like, yeah, that probably will be ai. I don’t totally know the job math ‘cause I don’t know how many animators there are today. [01:06:00] But I actually think, weirdly, I think we could be producing more high quality, maybe even slightly educational kids entertainment.
And so it’s maybe that’s a positive is like we could just have like more, like you could just have a Pixar for like, you know, things where kids learn stuff. And it used to be these like very, you know, lo-fi uh, you know, kinda lesson things.
swyx:
I mean, we had tellies, you know, that so slow.
Aaron Levie:
So, so we, we could have way more of that.
And, and maybe every animator that today is making a Pixar film is now, you know, we’re like, we fragment that out and uh, but now they’re responsible for more content and they’ve got AI agents running. So like, so, so I think there’s some optimistic scenarios on the entertainment side is like, there’s a lot of great use cases for being able to do, you know, generative media.
swyx:
Yeah. Yeah. Edu edutainment as well.
swyx:
I guess one question I is, it’s kind of like a self-serving one and almost like an advice, uh, side of the, the, the, the question, one of the things I just, uh, really enjoyed, uh, researching you was that, uh, Michael Arrington had some influence in the [01:07:00] box journey because he went to his house party.
Aaron Levie:
Yes.
swyx:
And, and that’s how you got funding.
Aaron Levie:
Yes.
swyx:
One of latent spaces. That’s a deep cut, right?
Aaron Levie:
Yeah. Very deep cut. That’s a oh six deep cut.
swyx:
Yeah. Uh, do, I mean, do you want to tell that story? I don’t know if you’ve told it very
Aaron Levie:
much. It’s not very much of the story. Yeah. Uh, because I probably just,
swyx:
it’s like a random intro, right?
Like,
Aaron Levie:
um, well, it was just he used to have house parties. Yeah. Uh, TechCrunch had had these house parties and, and it was, um, probably no different than somebody’s doing a house party in sf Uh, you know, just go, yeah. And you just go and you meet the VCs and founders and like, I’m gonna make up examples, so I don’t want to like, you know, there’d be like Chad Hurley over there pitching his, you know, YouTube to people.
And like, like that’s just like how it worked. And it was just like, wow. Like that was this era where all these new companies were, were emerging. And I met, uh, our first investor, uh, in Silicon Valley at one of these house parties, Emily Melton, who then brought us into D-D-D-F-J-D, that, that became our Series A.
So that was all because of Arrington’s, uh, backyard Party.
swyx:
One of my inspirations for late space is to be as helpful, influential, whatever as TechCrunch was. That’s [01:08:00] awesome. In the day.
Aaron Levie:
That’s Yeah.
swyx:
What would a new TechCrunch today look like? You know, what, what, what, what should I, what should I do? I think there used to be TechCrunch Disrupt.
Yeah. You know, I could do that with my conference, but I haven’t done it yet.
Aaron Levie:
Well, I mean, I think,
swyx:
um, useful. I don’t know.
Aaron Levie:
Uh, well, you know, actually interestingly, I would, I would argue Disrupt came after the period that was the, was that Deep cut period. Okay. So, so I think Di Disrupt, you know, ended up being, you know, you know, catalyzing.
I don’t even, I think Cloud Flare launched It disrupted, yes. Is that the story? Right.
swyx:
They were runners up.
Aaron Levie:
Okay. Okay. So like, so like, I think anytime. Anytime you can be in a, a launchpad is, is just great because it draws in people that are, that’s what I’m trying to do in that creative moment. And whether it needs to be a contest or, or just like everybody gets like five minutes and you’re fundraising.
I mean, who knows? But, but I mean, for what it’s worth, like, I don’t know, have that much advice. ‘cause I think you, you’re, you’re already doing it effectively. Like I, I just like watched the YouTube videos late at night. Um, uh, from the events. I haven’t [01:09:00] been to one of your events, but like from the, from the camera angles, it looks like everybody’s there trying,
Jeff Huber:
trying.
So
Aaron Levie:
what’s great is that people are gonna be in the audience as like two random people and they’ll be like, you know, the next, the next big AI company will come from, you know, people coming to a meetup. ‘cause they were like, ah, I came in from Chicago and I’m ah, from, you know. Poland and let’s go do a startup.
Like that’s
swyx:
the
Aaron Levie:
magic
swyx:
of
Aaron Levie:
the valley.
swyx:
Dix Hy found his co-founder at a IE Oh, and I know of at least one marriage. That’s, that’s, wow,
Aaron Levie:
you have marriages
swyx:
already. Yeah. Yeah.
Aaron Levie:
I
Jeff Huber:
don’t,
Aaron Levie:
I never heard that about,
swyx:
that’s my go, that’s my favorite. KPI.
Aaron Levie:
Wow. We have AI marriages at the, at the AI engineer conferences.
These are both
Jeff Huber:
humans. To be clear,
swyx:
that’s a very good clarification. I like that. You have to check.
Jeff Huber:
Yes. That’s a
swyx:
very good
Aaron Levie:
clarification.
swyx:
No, but I, I think you have, you’re, you’re insightful business leader with like, a lot of thoughts on media, so I just figured I would,
Aaron Levie:
I mean, media is such an interesting space right now because, because I, you know, with the go direct model, every company is gonna have to be a media company.
You
swyx:
are going, you are the og. Go direct.
Aaron Levie:
Yeah. But, but, but you know, we [01:10:00] we’re, we’re still like. Like, I think, I think what, what you guys are doing, and I don’t even know all the overlapping relationships, but like I watch your guys’ videos of your events, watch your event videos, but like, it’s clearly like this is the new format, right?
Companies have to become channels to communicate with audiences. Yeah. I think the resurgence, resurgence maybe is a bad word ‘cause it implies it decline, but like, Devrel is hot. Yeah. Like the hottest thing of all time right now. I like if you could produce a fricking factory of Devrel people, like there’s just like unlimited jobs right now on the other end of that.
Yeah.
Jeff Huber:
Yeah.
Aaron Levie:
Um, ‘cause we’re gonna, everybody needs their services and APIs to be used by agents. And so we have to all find a way to like, like, Hey, look at me. Like, like agent over, oh please come over here agent. And that’s gonna, that’s a content game. Like how do you get the agents to see your stuff
swyx:
Yeah.
Aaron Levie:
And know your APIs and like, this is like a new world that, that we are in. And uh, it’s gonna be a. It’s, it’s gonna completely be a [01:11:00] digital marketing, you know, kind of world that we’re in.
swyx:
Yeah. Uh, for what it’s worth, I’m trying to help by doing little writing bootcamps and basically turn into a Devrel bootcamp.
Um, where, you know, well, it’s a demand and supply problem. There’s, there’s huge demand. Yeah. There’s no supply. Wow. All this increase
Aaron Levie:
supply. Why is your no supply?
swyx:
The one, the really good ones were for themselves.
Aaron Levie:
Uh huh.
swyx:
Creator economy screwed, screwed you over.
Aaron Levie:
So, so I see so, so Substack and Yes. YouTube payouts.
And that’s, is that
swyx:
really making Patreon? Yeah. Like the, the most talented guys are making, you know, millions and just working for themselves while for you,
Aaron Levie:
that’s not, we don’t want them to make that much money. Okay.
swyx:
We need to be able to hire
Aaron Levie:
people.
swyx:
I mean, I think, I think like, you know, do do what some companies are doing, you know, I’m not saying it’s my situation exactly, but like give them equity and like Uhhuh it should probably would be worth more, uh, just like sort of helping them out.
Aaron Levie:
Well, they are getting Oh, sorry. As full-time employees or not?
swyx:
I’m part-time.
Aaron Levie:
You need full-time.
swyx:
I’m part-time.
Aaron Levie:
Yeah. But, but you’re, you’re you n of one, like, we like also people that are full-time.
swyx:
Yeah. Yeah. My classic joke or, or like, observation [01:12:00] was like, this was when HubSpot bought, like their, they bought like a newsletter business.
Uh, and then they bought the, my first million, like the, the sort of podcast. Oh, okay. Dharmesh, you must know Dharmesh. Um, so he’s like obsessed with this guy. Okay. So, so my conclusion was like every company must either build or buy a media company. Yes. Right. And until you, unless you realize that. You have to take it that seriously that you are running a media business in your company.
Yes. You will never be good at it.
Aaron Levie:
Yes, a hundred percent.
swyx:
Yeah.
Aaron Levie:
Yeah. No, we’re, we’re very much taking that seriously. But, but still, and yet Devrel, I mean, I gotta do one plug. I don’t all is out. Please, please. We’re hiring a Devrel.
swyx:
Yeah.
Like,
Jeff Huber:
like please
swyx:
no, all engineers here. Like, yeah. Like you’ve made it, like, and I just said every, every agent needs a box.
Like, let’s go, let’s go.
Aaron Levie:
Thank you. No, that, that’s the headline. And we are hiring Devrel to make that happen. Uh, but yeah, I think Devrel is like the future job. So we’re all just gonna be doing Devrel in some form.
swyx:
Okay. Yeah.
Aaron Levie:
I mean, what is FD
swyx:
developers are ruling the earth. Yeah.
Jeff Huber:
What is FDI don’t know. Um,
Aaron Levie:
no, it’s, it’s Devrel.
swyx:
Yeah. Okay.
Aaron Levie:
No, you just, you’re going to
swyx:
a company, isn’t it just like glorify consulting? That’s, that’s the downside.
Aaron Levie:
Sure. I mean, I guess nobody can like actually [01:13:00] d you know, fully define this, but, um, uh, but I think it’s, it’s, it’s micro Devrel, like you’re in the company, you’re helping them with the services.
Yeah. You’re doing a little bit extra implementation. Yeah.
swyx:
Yeah.
Aaron Levie:
Um, but, uh, but yeah, so it’s, uh, I, I think we’re all, you know, the thing that’s gonna happen on the ledger of software is we’re gonna produce far more output of code and thus features per dollar. But on the other end of this, we’re gonna actually end up spending probably just as much on how do you get all of that stuff to the customer, and it’s gonna create a new set of roles that we are all doing, partly because I, either, because there’s so much choice and now you have to kind of fight for attention there, or because this stuff is, is just changing so quickly that you have to technically help your customers.
Along the journey. Yeah, so, so I just think like, I, this is why I, I, I always laugh when, you know, people say you don’t need to be an engineer, don’t do computer science. I actually think like that is like still one of the most protected job categories because [01:14:00] things are only getting more technical. Things are only gonna get harder and anybody in a technical position is in the best position.
Yeah. To get agents deployed, get them built, get them adopted, build the, the, the custom code software to the, for the IT system, all of that.
swyx:
So, yeah. Yeah. My, my classic founding story of like why I picked AI engineer as a title and as, as a, as a theme for this podcast as theme for my conference was, um, back in like early 2023, someone al came to me and said like, I’m all in on ai.
What should I do? And I was like, I just looked at her. I was like,
Jeff Huber:
God dammit, there’s nothing you can do.
swyx:
Like engineers are about to get so much more powerful than you Uhhuh. You don’t even understand.
Aaron Levie:
Tell me there’s a good, did she go and then learn?
swyx:
No, I didn’t, I didn’t say any of that to her.
Aaron Levie:
Oh, oh, I see, I see, I see.
swyx:
Okay. Yeah, I’m not, I’m not that honest. Well,
Aaron Levie:
I hope, I hope somewhere out there. She, she did, went to some online academy.
swyx:
Exactly. Learn to code.
Aaron Levie:
Yeah.
swyx:
But there, there’s a lot of people, like, there’s a lot of people who believe AI too much, and then they’re like, well, you don’t need to learn to code, so I won’t learn to code.
Yeah. And then there’s, there’s like, there’s a bunch of us who are like, just in that [01:15:00] sweet spot of like, we can code and we can wield AI a thousand times more effectively than you can. Yeah. And like, well, who’s gonna win here? Like
Jeff Huber:
I, I think I, this was another, uh, a tweet, but it was like the observation that like, really software engineering for the past 30 years was the primary career track for like technical, high agency people that wanted to have a large outsize impact on the world.
swyx:
Yeah.
Jeff Huber:
And like, software was a means to, you know, do that Right. Effectively. Um, and so yeah, with ai, is it like that, uh, and, and for AI could eat software engineering or software engineering could eat all their kind of domains of discipline.
Aaron Levie:
You, those pr same principles then get applied to every other and then function,
Jeff Huber:
right?
Aaron Levie:
Yeah, exactly. Yeah. I
Jeff Huber:
mean, g team engineering, is that a hundred percent Anything else? Yeah.
Aaron Levie:
Well, this is the, you know, uh, anybody who believes that an enterprise, and I’m, I’m, I’m mixed on the, I’m mixed on this is, but if you believe that an enterprise is going to build its own software for all of its problems, then you must be the most long on computer science, you know, as a discipline of all time, because guess what, most of the economy does not have enough engineers to then [01:16:00] maintain all those systems, to update to all those systems, to figure out the, the relationship between the business problem and what the code needs to do to go and actually manage that.
And so, so like that’s, that’s a very pro. Engineering job argument of what the future’s gonna look like. I’m still, again, I go back and forth on like, are you gonna really build all these things versus no prepackaged software, but no matter what, there’s gonna be 10 to a hundred times more code. So I think you can be very long engineering right now as just a, you know, purely on the dimension of, of software’s gonna become increasingly more important once agents are, are, you know, turning everything into software.
swyx:
Yeah. All right. Three software guys say software in room. Okay.
Aaron Levie:
Not biased at all. Okay.
swyx:
But, uh, Aaron, your inspiration. All right. Take you. It’s such a pleasure.
Aaron Levie:
All right. Good to be here.
