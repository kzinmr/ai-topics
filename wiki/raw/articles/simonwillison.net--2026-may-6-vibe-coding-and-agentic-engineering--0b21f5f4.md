---
title: "Vibe coding and agentic engineering are getting closer than I’d like"
url: "https://simonwillison.net/2026/May/6/vibe-coding-and-agentic-engineering/#atom-everything"
fetched_at: 2026-05-07T07:01:37.203116+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# Vibe coding and agentic engineering are getting closer than I’d like

Source: https://simonwillison.net/2026/May/6/vibe-coding-and-agentic-engineering/#atom-everything

Vibe coding and agentic engineering are getting closer than I’d like
6th May 2026
I recently talked with Joseph Ruscio about AI coding tools for Heavybit’s High Leverage podcast:
Ep. #9, The AI Coding Paradigm Shift with Simon Willison
. Here are some of my highlights, including my disturbing realization that vibe coding and agentic engineering have started to converge in my own work.
One thing I really enjoy about podcasts is that they sometimes push me to think out loud in a way that exposes an idea I’ve not previously been able to put into words.
Vibe coding and agentic engineering are starting to overlap
A few weeks after vibe coding was first coined I published
Not all AI-assisted programming is vibe coding (but vibe coding rocks)
, where I firmly staked out my belief that “vibe coding” is a very different beast from responsible use of AI to write code, which I’ve since started to call
agentic engineering
.
When Joseph brought up the distinction between the two I had a sudden realization that they’re not nearly as distinct for me as they used to be:
Weirdly though, those things have started to blur for me already, which is quite upsetting.
I thought we had a very clear delineation where vibe coding is the thing where you’re not looking at the code at all. You might not even know how to program. You might be a non-programmer who asks for a thing, and gets a thing, and if the thing works, then great! And if it doesn’t, you tell it that it doesn’t work and cross your fingers.
But at no point are you really caring about the code quality or any of those additional constraints. And my take on vibe coding was that it’s fantastic, provided you understand when it can be used and when it can’t.
A personal tool for you, where if there’s a bug it hurts only you, go ahead!
If you’re building software for other people, vibe coding is grossly irresponsible because it’s other people’s information. Other people get hurt by your stupid bugs. You need to have a higher level than that.
This contrasts with agentic engineering where you are a professional software engineer. You understand security and maintainability and operations and performance and so forth. You’re using these tools to the highest of your own ability. I’m finding the scope of challenges I can take on has gone up by a significant amount because I’ve got the support of these tools.
But I’m still leaning on my 25 years of experience as a software engineer.
The goal is to build high quality production systems: if you’re building lower quality stuff faster, I think that’s bad. I want to build
higher
quality stuff faster. I want everything I’m building to be better in every way than it was before.
The problem is that as the coding agents get more reliable, I’m not reviewing every line of code that they write anymore, even for my production level stuff.
I know full well that if you ask Claude Code to build a JSON API endpoint that runs a SQL query and outputs the results as JSON, it’s just going to do it right. It’s not going to mess that up. You have it add automated tests, you have it add documentation, you know it’s going to be good.
But I’m not reviewing that code. And now I’ve got that feeling of guilt: if I haven’t reviewed the code, is it really responsible for me to use this in production?
The thing that really helps me is thinking back to when I’ve worked at larger organizations where I’ve been an engineering manager. Other teams are building software that my team depends on.
If another team hands over something and says, “hey, this is the image resize service, here’s how to use it to resize your images”... I’m not going to go and read every line of code that they wrote.
I’m going to look at their documentation and I’m going to use it to resize some images. And then I’m going to start shipping my own features. And if I start running into problems where the image resizer thing appears to have bugs or the performance isn’t good, that’s when I might dig into their Git repositories and see what’s going on. But for the most part I treat that as a semi-black box that I don’t look at until I need to.
I’m starting to treat the agents in the same way. And it still feels uncomfortable, because human beings are accountable for what they do. A team can build a reputation. I can say “I trust that team over there. They built good software in the past. They’re not going to build something rubbish because that affects their professional reputations.”
Claude Code does not have a professional reputation! It can’t take accountability for what it’s done. But it’s been proving itself anyway—time and time again it’s churning out straightforward things and doing them right in the style that I like.
There’s an element of
the normalization of deviance
here—every time a model turns out to have written the right code without me monitoring it closely there’s a risk that I’ll trust it at the wrong moment in the future and get burned.
The new challenge of evaluating software
It used to be if you found a GitHub repository with a hundred commits and a good readme and automated tests and stuff, you could be pretty sure that the person writing that had put a lot of care and attention into that project.
And now I can knock out a git repository with a hundred commits and a beautiful readme and comprehensive tests of every line of code in half an hour! It looks identical to those projects that have had a great deal of care and attention. Maybe it is as good as them. I don’t know. I can’t tell from looking at it. Even for my
own
projects, I can’t tell.
So I realized what I value more than the quality of the tests and documentation is that I want somebody to have
used
the thing. If you’ve got a vibe coded thing which you have used every day for the past two weeks, that’s much more valuable to me than something that you’ve just spat out and hardly even exercised.
The bottlenecks have shifted
If you can go from producing 200 lines of code a day to 2,000 lines of code a day, what else breaks? The entire software development lifecycle was, it turns out, designed around the idea that it takes a day to produce a few hundred lines of code. And now it doesn’t.
It’s not just the downstream stuff, it’s the upstream stuff as well. I saw
a great talk by Jenny Wen
, who’s the design leader at Anthropic, where she said we have all of these design processes that are based around the idea that you need to get the design
right
—because if you hand it off to the engineers and they spend three months building the wrong thing, that’s catastrophic.
There’s this whole very extensive design process that you put in place because that design results in expensive work. But if it doesn’t take three months to build, maybe the design process can be a whole lot riskier because cost, if you get something wrong, has been reduced so much.
Why I’m still not afraid for my career
When I look at my conversations with the agents, it’s very clear to me that this is moon language for the vast majority of human beings.
There are a whole bunch of reasons I’m not scared that my career as a software engineer is over now that computers can write their own code, partly because these things are amplifiers of existing experience. If you know what you’re doing, you can run so much faster with them. [...]
I’m constantly reminded as I work with these tools how hard the thing that we do is. Producing software is a
ferociously
difficult thing to do. And you could give me all of the AI tools in the world and what we’re trying to achieve here is still really difficult. [...]
Matthew Yglesias, who’s a political commentator, yesterday
tweeted
, “Five months in, I think I’ve decided that I don’t want to vibecode — I want professionally managed software companies to use AI coding assistance to make more/better/cheaper software products that they sell to me for money.” And that feels about right to me. I can plumb my house if I watch enough YouTube videos on plumbing. I would rather hire a plumber.
On the threat to SaaS providers of companies rolling their own solutions instead:
I just realized it’s the thing I said earlier about how I only want to use your side project if you’ve used it for a few weeks. The enterprise version of that is I don’t want a CRM unless at least two other giant enterprises have successfully used that CRM for six months. [...] You want solutions that are proven to work before you take a risk on them.
