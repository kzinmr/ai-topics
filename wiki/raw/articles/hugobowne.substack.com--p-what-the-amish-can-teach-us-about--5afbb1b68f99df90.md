---
title: "What Happens to the Org Chart When Agents Do the Work?"
source: "https://hugobowne.substack.com/p/what-the-amish-can-teach-us-about"
author: Hugo Bowne-Anderson
publication: Vanishing Gradients (hugobowne.substack.com, pub_id 2632531)
date: 2026-11-25
collected: 2026-11-25T10:35:00+00:00
access: free (isAccessibleForFree=true)
method: curl + <article> paragraph extraction (Substack redirect-stub recovered via substack.com/home/post/p-226449334)
tags: [raw, newsletter]
---

# What Happens to the Org Chart When Agents Do the Work?

Hugo Bowne-Anderson Nov 25, 2026 6 2 Share I recently went to O’Reilly’s Foo Camp (Friends of O’Reilly), a gathering where the people who show up set the agenda and run the sessions. I had a lot of great conversations there, particularly about how people are already working with agents inside their organizations and the future of agentic communities. I gave a lightning talk on building agentic organizations, then ran a session where about ten of us got together to compare notes.

O’Reilly has kindly put my five-minute lightning talk on YouTube . Below are my annotated slides, followed by some of the ideas that came out of our conversation.



👉 If you’re interested in how teams are working with agents, come join me for a free Maven Lightning Lesson, 10 Things People Building Agentic Organizations Told Me . I’ll share what I’ve learned from teams that share every agent session and from founders figuring out which decisions still need them. I’d love to show you what I’m building and hear what you’re trying with your own team. 👈

During the Industrial Revolution, many of our ancestors lost arms and legs to the machines they worked with. My provocation is that when the machine is a bicycle for the mind, we’re all losing our minds. At the time, I worked with six to eight agents on a typical day, and the mental toll of directing them is what I meant by “AI psychosis” in my Foo Camp talk (I use the term in a nonclinical sense! My intention is to be evocative rather than merely descriptive).

Four agents, four projects, and wiped out by 11 a.m.

Simon Willison was in the room at Foo Camp when I quoted him from Lenny’s Podcast, so I had to admit that my agent had found the quote for me. Simon W. said that using coding agents well takes “every inch of my 25 years of experience as a software engineer.” He can put four agents to work on four different projects in parallel and be wiped out for the day by 11 a.m. I felt seen!

But wait, it gets worse: Simon W.’s account also made me wonder what running those agents does to our reward system. Running agents can have much the same pull as scrolling Instagram, with the added incentive that every run looks like productive work. By 3 a.m. you’ve got twelve terminals open and you’re building your eleventh Kanban board. At least the shareholders are happy. Doom-scrolling plus up and to the right!

Eleanor Berger and I have started a series on Software Factories++ called Factory Life, that we also lovingly refer to as Micro Managers Anonymous: we wanted to talk about how far into the weeds we were getting with our agents and how to get out of the loop. What’s interesting is that some of the best builders we’ve seen there and in our Software Factory course have never written a line of code. They’re clear about what they want and careful about checking what comes back, which lets them leave the agent to work out how to get there: we call this evidence-backed verification and it’s a core component of verification-driven development (what we’re seeing in our own work and from colleagues is that specification-driven development is less important now that models and harnesses are getting far better).

If you’re having trouble staying off the factory floor, Eleanor and I put together a free seven-step programme to help you decide what your agents can check for themselves and what evidence you want them to bring back to you. Getting yourself out-of-the-loop is key to reducing AI psychoses.

I am the bottleneck! Even when I’ve specified the work well, I still have to review it. My agents can work on six things in parallel, but I can only make one decision at a time.

In a conversation we had about this, Simon W. gave me the example of writing tests. He used to be able to spend a few hours in the afternoon writing them. He knew how to do it and could get on with the work without having to make many difficult decisions. Now an agent can write those tests while he’s working on something else.

What disappears from the day along with those hours of test writing is a stretch of work that asked relatively little of his judgment. As agents take on more of the execution, more of our own work comes down to decisions that depend on taste. There’s no f***ing way it’s sustainable to be making this many decisions each day.

(In the session after the talk, we discussed something good leaders already do: give people principles they can use to make decisions on their own. Could we do the same for agents, so only the close calls come back to us? More on that below.)

A practical aside on how that work comes back to me. Most of my interaction with agents is voice in, visuals out.

I talk to my agents and use a gaming controller to point and click, which means I can work with them while I’m on the treadmill. They give me text and images in an editable HTML canvas. I can work directly on what I see while the agent works on the code behind it. The principle here is VIVO: voice in, visuals out.

That’s how I work with my agents, but what arrangements have we used when several people need to coordinate their work?

There are many ways to coordinate human action. In the talk, I briefly mention three of the most prevalent models.

Corporations, the military, and the mafia all give us examples of hierarchies, where people coordinate through a chain of command. In a flat team, people coordinate directly with one another (Instagram and Cursor were my examples at Foo Camp). Then there’s the core-and-periphery model, which you can see in an open-source project with a core group of maintainers and occasional contributors, or at a potluck where a few people organize dinner and everyone brings a dish.

What can agent swarms learn from an Amish barn raising?

At Foo Camp I asked who’d seen an Amish barn raising. Watch the people working along the roof in this time-lapse from Clinton, Wisconsin. Several crews can work on different parts of the frame at once, and you can see people move between them as the work progresses:

There’s a master carpenter and a shared plan for the barn. Each crew takes on a different part of the building.

When someone leaves one part of the frame, a person working elsewhere on the barn can see the gap, recognize a job they know how to do, and move over to fill it.

In a company, the person with the skills to help may have no way of seeing that another team needs them. A team tells its manager where it’s stuck, and the request travels up until it reaches someone who knows where to find help.

AI is well placed to close that gap. With a strong frontier model and well-curated context about what teams are working on and who has the skills to help, getting the information to the right person is no longer the bottleneck. That in itself has significant implications because hierarchical organizations are designed entirely around the fact that information flow is a bottleneck.

How are organizations already putting agents to work? One place to start is the org chart.

An agent can take on a role in an existing department alongside a human. You might have a marketing agent working alongside people in marketing, with agents in product and design working with their respective teams.

I have plenty of human collaborators, but at the time of the talk I also worked directly with six to eight agents on any given day. For that part of my work, all the lines in the diagram come back to me.

Since Foo Camp, I’ve been moving back toward working mostly with one agent. It coordinates the work of my other agents, so I can follow one conversation instead of keeping six or eight going in parallel. This allows focus of attention!

Some of the most productive teams I’ve seen are small groups where everyone works with agents and the people coordinate closely with one another. On some software teams, they’re aligned closely enough that they push changes straight to the main branch without opening a pull request.

Greg Ceccarelli , who was chief product officer at Pluralsight and led data science at GitHub, gave me an example from his team at SpecStory. Their agents write code faster than the team can review pull requests, so they push changes straight to main and keep branches for experiments. Watch Greg explain how they work.

The dotted lines add the conversations that a reporting structure leaves out. An agent can communicate with another agent, and people can work with agents elsewhere on the team.

A pull request can itself be the signal for an agent to start work. For example, a background agent can pick up each new pull request and run a security review without someone on the team having to ask for it each time.

A background agent that reviews pull requests already knows what to watch for and what to do. On the Sequoia podcast , Jack Dorsey and Roelof Botha describe what they’re trying at Block. In their essay From Hierarchy to Intelligence , they make a distinction I like: the company can have a shared model of what’s going on while the people doing the work have the context to make their own decisions.

Think back to the barn. The carpenter can see that another crew is short a pair of hands, knows how to do the job, and moves over. In a company, a background agent working from that shared model could spot the gap and bring it to someone who can help. If that person can act on it, the request and the decision can both skip the trip up and down the management chain.

How do you use agents today, and what would you like that arrangement to look like across your organization? These are the questions I asked the other Foo Campers and we had an hour-long session about it.

By the time I get up, my chief-of-staff agent has read my email, looked at my priorities and what my clients, students, and collaborators need, and proposed how I might spend the day. What I wanted to know was whether anything like that was happening at the scale of a company. Could an agent see that a team I’ve never worked with needs help and that I’m the person to give it? Several friends at frontier labs have said they’re seeing more of this at the labs!

There were around ten of us in the session. Foo Camp is off the record, but to give you a sense of the room: the head of a major tech company’s research lab for the Americas was there, as were a founder running four companies with around twenty agents apiece, a founder building software factories, a designer working on an open-source protocol for personal agents, and a co-creator of some of the protocols much of the web runs on, now working on how agents prove who they act for.

The session kind of blew my mind. I’m going to write more about it, but here are a few things I’m still thinking about:

What would maximum openness look like? The research lead suggested taking one willing team fully open and finding out where it needs boundaries. One of her teams already shares every agent session. You can see what a colleague asked, what they tried, and why they changed direction. The finished code rarely tells you all that. It reminded me of the barn raising: you can go where you’re needed because you can see the whole frame.

Whose authority does an agent have, and what happens to secrets? One company defaults to open channels, with exceptions for things like legal and personnel matters. The research team had already discovered a harder case: someone put personal material into a shared session by accident, and by the time they tried to retract it, agents had learned from it. In a large organization, you need to know who an agent acts for, what it can read, and who it can share that information with.

Could a bank or a company like Siemens make the same bet as Block? We’d been talking about people who can do most of their work in software. What does this look like for a technician standing next to a piece of equipment, or inside a bank where an agent could send customer data to the wrong person? The room split on whether an established company can afford to wait. By the time it’s clear who’s figured this out, the winner might be too big to buy. Then again, a company with deep pockets can let someone else do the experimenting and hire the team.

Who helps you find your next project when there are fewer managers? At one company, experienced people were finding their way to new work. People earlier in their careers had a harder time, and losing the group a manager used to connect them to could be isolating. The designer in the room is building a personal agent that looks for opportunities on the employee’s behalf. I like the question that raises: whose interests does the agent represent when it suggests what you should work on next?

While we’re sitting here, is the work still running? A founder put that question to the room. His software factory keeps working while he’s away. When he suspects the agents have settled for something that’s only good enough, he writes a short essay to work out whether his hunch holds up. If it does, he uses the essay to steer what the factory does next.

What belongs in a demand factory? The same founder has agents research potential customers, prepare him for calls, and handle scheduling and follow-up. I asked whether he’d want an agent on the sales call itself. I’ve been trying a notetaker that gives me feedback live. He wants his full attention on the person across from him, down to a word choice or a change in body language. That conversation is where he builds trust.

What happens when your software factory makes more than your business can ship? One founder asked us to think about a factory that starts making tires faster than it makes engines. Soon people are spending their time moving piles of tires out of the way, and the engines take even longer to build. He’d seen the software version of this: install a software factory and code starts pouring out, but the company still has to get it into customers’ hands. Speeding up one part can slow the whole thing down.

“It should literally be just Supreme Court cases all day long.” I’d started the talk by saying I was the bottleneck. This was the most useful answer I heard. When a decision reaches you, can you write down the principle behind your call so the next person or agent can make it without you? Ideally, the questions that still reach you are the 51–49 calls where your judgment might actually tip the decision.

👉 I’ll be digging into these in my free Maven Lightning Lesson, 10 Things People Building Agentic Organizations Told Me . I’ll share what I’m building, what I’ve learned from people already working this way, and what I’d try with a team next week. I’d love to hear what’s working for you and which decisions you still want landing on your desk. 👈

Vanishing Gradients is independent, and most of the podcasts, workshops, articles, skills, and workflows I publish are free.

Become a paid subscriber. Your subscription supports the podcast, newsletter, and open resources.

Share this post with a friend or colleague who builds with AI.

Subscribe to the events calendar for upcoming livestreams, workshops, and meetups.

Subscribe on YouTube for full episodes, live builds, and recordings.

Work with me. I help teams build and improve AI-powered products. Hit reply if you’d like to talk.


