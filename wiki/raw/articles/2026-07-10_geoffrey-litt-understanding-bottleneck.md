---
title: "Understanding is the new bottleneck — Geoffrey Litt, Notion"
created: 2026-07-10
author: Geoffrey Litt (@geoffreylitt)
source: YouTube
url: https://www.youtube.com/watch?v=WkBPX-oDMnA
type: talk
duration: 19:33
tags: [ai-agents, developer-experience, autonomous-coding, agent-engineering, human-in-the-loop]
---

# Talk Overview

In this talk from AI Engineer 2026, Geoffrey Litt (Notion) argues that autonomous coding loops are trendy but the reality is that most agentic tasks still require human judgment. He presents techniques for staying in the loop and efficiently developing understanding, combining ideas from education and cognitive science with modern agent capabilities. The core message: to guide agents well, you need to understand the work they are doing — not just verify correctness.

## Core Thesis

Autonomous coding agents still require human judgment. To guide agents well, you need to understand the work they are doing — not just verify correctness. Combines education and cognitive science with modern agent capabilities. "It is not enough to just verify correctness — you actually need to understand the work they are doing."

## Key Insights

- **Understanding vs Verification**: The bottleneck in agent-assisted development is shifting from writing code to understanding code
- **Cognitive Science Applications**: Old ideas from education and cognitive science can be applied to modern agent interactions
- **Human-in-the-Loop Techniques**: Practical tips for moving faster with agents by understanding more, not less
- **Agent Guidance**: How to effectively guide autonomous coding agents while maintaining comprehension

## Transcript

[00:01] [music]

[00:12] &gt;&gt; What's up? Yeah, thank you for coming to

[00:14] the design engineering track at AI. Is

[00:16] everyone having fun?

[00:18] Yeah, I think this is going to be a

[00:19] great track, so get excited.

[00:22] All right, let's get going. Um, my

[00:24] name's Jeffrey Litt. I'm a design

[00:26] engineer at Notion currently.

[00:28] And I'm here to drop a hot take

[00:31] for this room, maybe.

[00:34] I think it is still important for people

[00:37] to understand how code works.

[00:39] &gt;&gt; [applause and cheering]

[00:42] &gt;&gt; Now, some of you might agree, some of

[00:43] you might disagree. Let's actually Let's

[00:44] do Let's try a poll. I'm curious for

[00:46] this room. Raise your hand if you agree

[00:47] with that opinion.

[00:50] Okay, maybe some selection bias. Any

[00:51] brave Okay, raise your hand if you

[00:52] disagree with this opinion.

[00:55] Wow, okay. We have

[00:57] &gt;&gt; [laughter]

[00:57] &gt;&gt; Maybe we'll do a debate later, yeah. I

[00:59] was hoping we'd be at the AI engineer

[01:01] conference, so we'd have more bull Okay.

[01:03] I might be preaching to the choir here.

[01:06] You know, I think we The reality is

[01:07] though we are entering an era where this

[01:09] is a legitimate question that people are

[01:11] debating, right?

[01:13] Agents are writing tons of code for us.

[01:15] They're landing 50,000 line PRs.

[01:18] And it is getting harder to keep up. We

[01:20] all feel this.

[01:22] Now, I think the good news is

[01:24] there are lots of ways to understand.

[01:27] Be, you know, the days of just reading

[01:29] code line by line and that's not the

[01:30] only way anymore.

[01:32] And what the point of this talk is about

[01:34] is I want to share with you a bunch of

[01:36] the practices that I use to understand

[01:38] the code that my agents are writing for

[01:40] me.

[01:41] This includes things like explainer

[01:43] docs,

[01:44] teaching me about how my code works.

[01:47] My agents write quizzes for me to to

[01:49] test my understanding. Am I still really

[01:52] in the loop? Am I keeping up?

[01:55] I have agents build me micro worlds that

[01:58] I can inhabit to get this intuitive

[02:00] sense of how my code works that's deeper

[02:02] and richer than just a written document.

[02:05] And I think all of these are really

[02:06] exciting new possibilities that are

[02:08] opening opening up for AI to help us

[02:10] understand better,

[02:12] not worse. And so that's what the point

[02:14] of this talk is going to be about and I

[02:15] hope I can leave you with some

[02:16] techniques that you can take home and

[02:18] use yourself.

[02:21] By the way, my timer isn't running. If

[02:23] you could get that running, that'd be

[02:24] great so I know

[02:26] blabbering.

[02:28] Okay, but let's start let's back up for

[02:29] a sec. Before we talk about how, let's

[02:31] talk about why.

[02:33] Why bother understanding? This is again,

[02:35] it's a question now, right?

[02:37] And I think a lot of people get this

[02:39] subtly wrong.

[02:42] So what a lot of people think of why do

[02:44] humans still have to understand, they

[02:45] think we understand to verify.

[02:48] The agents do dumb stuff, we've all seen

[02:49] it, and your job as the human is to keep

[02:52] them in line, right? Make sure they

[02:53] don't screw up.

[02:56] When people say things like code review

[02:58] is the new bottleneck, I think that's

[03:00] the first thing that pops into people's

[03:01] heads is

[03:03] correctness

[03:04] checking.

[03:05] There's this mental model that's like,

[03:07] "Hey, the agent's going to give you

[03:08] something, and what's your job? It's to

[03:10] ask, is this correct?"

[03:13] Now, correctness can have lots of

[03:14] definitions. Does it match the spec doc

[03:16] you gave it? Does it take down

[03:18] production? Is it well architected?

[03:21] But fundamentally, those are all kind of

[03:23] thumbs up, thumbs down decisions, right?

[03:26] And the thing is,

[03:27] over time, we've all seen it,

[03:30] the agents are also able to ask these

[03:31] questions and they're getting better at

[03:32] it.

[03:33] You give it the right verification loop,

[03:35] and over time,

[03:37] this is the reality. The the role of

[03:39] humans in correctness checking is

[03:41] decreasing.

[03:43] And you know what? I actually don't hate

[03:44] that.

[03:45] If I have a clear idea of what I want to

[03:47] do, and the agent does it correctly,

[03:49] instead of coming back to me with an

[03:50] incorrect thing, that's great. I'm I'm

[03:52] into it.

[03:54] So then I think people extend this and

[03:56] say, "You know what? That means

[03:58] as the agents get smarter and smarter

[03:59] and smarter, we we don't have to

[04:00] understand it all, right? Get out of the

[04:02] loop, man. Run the loop."

[04:04] And that's where I think people miss

[04:05] something really important.

[04:08] There is a deeper reason to understand

[04:10] what's going on,

[04:11] and that's understanding to participate.

[04:14] Because here's the thing,

[04:17] it's not just one loop.

[04:19] When you review what's happening and get

[04:21] in the loop,

[04:22] you come away changed. You understand

[04:24] something,

[04:25] and that understanding is what you take

[04:27] to the next loop, and the next, and the

[04:29] next.

[04:32] Your understanding of what's going on is

[04:35] the foundation for you having that next

[04:37] idea and being an active creative

[04:39] participant in a project.

[04:42] I think probably you've all you've all

[04:43] felt even before AI, you know, the

[04:45] difference of the kinds of ideas someone

[04:46] can have when they really understand

[04:48] what's going on versus when they're a

[04:49] few layers removed are different.

[04:51] Because when you have rich conceptual

[04:53] structures in your head that you can

[04:55] fluently recombine really fast without

[04:57] going out to like ask some some agent or

[05:00] some human how it works,

[05:02] that gives you the ability to fluidly

[05:03] take creative leaps.

[05:05] And that's the human part of the work,

[05:08] coming up with the next idea and the

[05:09] next idea.

[05:10] So this is actually the real reason I

[05:12] think understanding matters,

[05:13] and this is not something that we can

[05:15] just wash away with better agents.

[05:17] Because if we want to be active

[05:18] participants, you still got to do this.

[05:23] There's a great term maybe some of you

[05:24] have heard called cognitive debt that I

[05:26] think really captures the spirit well.

[05:28] It's an analogy to technical debt,

[05:30] popularized by the scholar Margaret

[05:31] Stories. Simon Willison also blogged

[05:32] about it.

[05:33] And I love this idea because

[05:36] similarly to tech debt, you might get

[05:37] away with it for a little bit,

[05:39] but at some point you get burned if your

[05:40] understanding degrades.

[05:42] And maybe you felt this. I know I felt

[05:43] it. You're vibe coding, things are going

[05:45] well, and then at some point you

[05:47] realize, wait,

[05:48] I've no idea what's going on. I

[05:49] basically can't participate anymore,

[05:51] right? You've built up too much

[05:52] cognitive debt.

[05:56] Okay, so maybe

[05:57] it sounds like all of you were already

[05:59] convinced. We agree. We need to

[06:01] understand.

[06:02] But how?

[06:04] Right?

[06:05] We don't want to live in 2023. We are

[06:08] using agents to move fast, and it is

[06:10] harder and harder to keep up. How do we

[06:11] do it?

[06:13] I think to answer this question, we

[06:15] should actually take a step back and ask

[06:16] a more fundamental question,

[06:19] which is how do we understand stuff in

[06:21] general?

[06:25] Plot twist, this is not the first time

[06:26] that any human has asked this question.

[06:28] There is a field. It's called education.

[06:32] Now, when you think education, you might

[06:33] think of bad memories from sitting in

[06:35] lectures or whatever, but I think we can

[06:36] do better. We can take inspiration from

[06:38] the best ideas that have ever been

[06:40] invented in education and use them to

[06:42] stay in the loop and understand.

[06:44] So, that's what this talk is about.

[06:46] We're going to talk about three

[06:47] techniques.

[06:50] First, explanations.

[06:53] So, when an agent writes some code, it's

[06:55] an opportunity for it to explain the

[06:56] work to you, right? And the most naive

[06:58] explanation is, hey, here's the code

[07:00] diff. That's the raw change, the

[07:01] material of what happened.

[07:03] But we can do, I think, much, much

[07:04] better.

[07:06] What would the best possible explanation

[07:08] be? Like if you sent a team away for a

[07:11] year to come up with a personalized

[07:12] curriculum just to explain this one code

[07:14] change to you, what would that look

[07:15] like? I think this is a very generative

[07:17] question to ask.

[07:20] So, I've done a bunch of attempts at

[07:22] this. One is this skill I wrote called

[07:24] explainedif, which I use every day, and

[07:26] a lot of my co-workers do as well, and I

[07:27] want to walk you through it.

[07:30] So, we're going to go through a little

[07:31] example here. I'm working on a video

[07:32] game where you draw Zen gardens, kind of

[07:35] de-stress, you know.

[07:37] We can all use that these days.

[07:39] And we made a code change to change the

[07:41] perspective of the game from top-down to

[07:43] isometric.

[07:45] And I when I run my skill, it produces a

[07:46] code explainer doc.

[07:48] This can be an HTML file, it can be

[07:49] markdown. I like to put them in Notion

[07:51] because I work there, but also because

[07:53] it's then collaborative, so my team can

[07:54] comment on it and talk about it.

[07:56] And here's how it looks.

[08:00] We start with background. We do not

[08:01] start with what happened in this change.

[08:04] It starts by teaching me, "Hey, here's

[08:05] how the system works.

[08:07] Here's the game engine we're using.

[08:08] Here's the coordinate system, right?

[08:09] Here's the subsystems."

[08:11] It makes sure that I'm sort of being led

[08:13] up to the point where I can even begin

[08:15] to understand what's going on here.

[08:17] Obviously, you can skip this if you

[08:18] already know. You can personalize it to

[08:19] what you already know.

[08:22] Second important principle is intuition

[08:24] before details.

[08:26] So, before we start, you know, looking

[08:28] at code and stuff, it says, "Hey,

[08:30] the goal of this commit is to make the

[08:31] garden feel three-dimensional using only

[08:34] 2D drawing tricks."

[08:36] You can think of this sort of as like a

[08:37] well-written commit message, a little

[08:38] deeper.

[08:39] Give me examples. Give me a feel for the

[08:41] essence before, you know, you throw a

[08:43] bunch of code at me, right?

[08:45] This, by the way, this is good teaching.

[08:47] This is what like good math teachers do.

[08:51] Third, interactive figures. So,

[08:54] where it makes sense, give me things to

[08:55] fiddle with and try. So, with this

[08:57] change, it was like changing how we draw

[08:59] rocks. So, I can drag around rocks in

[09:01] this little simulation, and it shows me

[09:03] the coordinates that are happening, how

[09:04] the Z layers of the painting are

[09:06] changing.

[09:07] This, by the way, is actually using a

[09:08] new feature that Notion literally

[09:10] launched this morning of HTML blocks in

[09:12] Notion pages. So, agents can put

[09:13] interactive simulations into your Notion

[09:15] pages. Pretty cool.

[09:18] I think you have to be careful with

[09:19] interactivity. It can just be a crutch,

[09:21] and it can be kind of slop, to be

[09:22] honest. But used tastefully, it can

[09:25] provide understanding that's hard to

[09:27] achieve with just static pictures.

[09:30] Okay, then we finally get to the code,

[09:32] right? Show me the code. But we don't

[09:34] just throw a list of files in order.

[09:37] We do what we what I call literate code

[09:38] diffs. Give me prose. Explain it to me

[09:40] in the right order.

[09:42] Tell me before each file what's going

[09:43] on.

[09:44] And when you accumulate all this stuff,

[09:46] it's much much easier to follow than

[09:47] just a raw diff.

[09:50] Oops.

[09:51] In fact, I print these out and take them

[09:52] to the coffee shop sometimes and just

[09:53] read them.

[09:55] I find it really beautifully ironic that

[09:57] AI has actually taken this process where

[09:59] I was used to be like glued to my

[10:00] computer my IDE, and now I can go to the

[10:02] cafe and it's like I'm reading a

[10:03] textbook about this PR. It's really

[10:05] cool.

[10:08] Okay, so there is one problem, which is

[10:09] that reading is hard.

[10:11] And I am lazy.

[10:13] People are lazy.

[10:15] You know, there's this one time when I

[10:16] sent a PR to my coworker that I thought

[10:18] I had read the thing. I thought I

[10:19] understood, and she asked me the most

[10:21] basic question.

[10:22] And I was like, "Oh, no.

[10:24] I don't know."

[10:25] I clearly hadn't understood, right? I

[10:27] had fooled myself. So, I thought, "How

[10:29] can I create a system where that never

[10:30] happens again?"

[10:32] For inspiration, I look to the work of

[10:34] the researcher Andy Matuschak, who has

[10:35] this great line, "Books don't work."

[10:38] What he means by that is

[10:40] it's really easy to read a book and not

[10:41] realize you didn't understand it.

[10:43] So, that So, he and his collaborator

[10:44] Michael Nielsen tried this thing where

[10:46] in an essay, there are interactive

[10:48] spaced repetition quizzes that test

[10:50] whether you actually remember what you

[10:51] just read.

[10:52] And this is cool. It actually keep

[10:53] emailing you the quiz to make sure you

[10:55] remember it forever.

[10:57] But, this is nice because you cannot get

[10:58] through this essay without understanding

[11:00] it, or at least without remembering it.

[11:03] That's what I do with my code

[11:04] explainers. At the very bottom, there's

[11:05] a quiz. Five questions, medium

[11:08] difficulty. And my rule is I don't send

[11:10] code to

[11:12] uh others on my team to review unless I

[11:14] can pass the quiz about what my agents

[11:16] wrote.

[11:18] And it might sound kind of silly, but

[11:19] you should try it. It really is shocking

[11:21] the number of times this has caught me

[11:23] and made me and made me realize I didn't

[11:26] I think of it as sort of a speed

[11:28] regulator. Everything AI is speed up,

[11:29] speed up, speed up. There's all these

[11:30] incentives to go faster.

[11:32] How do we make sure we're not just

[11:33] moving at the speed of correctness, but

[11:34] also of understanding? And the quiz is

[11:36] that speed regulator, that's a system I

[11:38] can use for that.

[11:41] I did uh just put the scale on the

[11:43] internet. So, yeah, photo moment. If you

[11:45] want the Explain Diff scale,

[11:47] uh take that QR code, try it out, make

[11:49] it your own. It's really simple,

[11:50] actually.

[11:51] There's two versions at that QR code,

[11:52] one that outputs HTML, one that outputs

[11:54] Notion.

[11:57] Okay.

[11:59] Second technique, microworlds. What does

[12:00] that mean?

[12:02] So, this takes inspiration from the

[12:03] educator Seymour Papert,

[12:06] real visionary, who had this idea of

[12:09] living in Mathland. And what that meant

[12:10] was, "Hey,

[12:11] kids learn French from living in France,

[12:13] where do they go to learn math?

[12:15] Is there a Mathland where you can learn

[12:17] intuitively math just by being there?"

[12:19] So, he did these great things with this

[12:21] is a a robot called the turtle that kids

[12:23] program to draw stuff.

[12:25] But the point isn't making robots, the

[12:26] point is they actually learn math by

[12:28] doing that programming. But the point

[12:30] isn't the robot, it's the kids that are

[12:32] changed.

[12:34] So, how could we apply this to

[12:35] understanding code?

[12:38] Here's one example. Last year, I was

[12:39] trying to implement um for my own

[12:41] learning this interpreter for a

[12:43] programming language Prolog, which is

[12:45] think of it a little bit like a database

[12:46] query language.

[12:47] And there's all these parts of it that

[12:48] look like this, where when you read them

[12:49] on Wikipedia, they seem really

[12:51] complicated. And then when you actually

[12:53] get what's going on, it's like, "Wait a

[12:54] second, that wasn't that hard to

[12:56] understand, it just felt hard when I

[12:57] read it that way, right?" How could we

[12:59] make it click more for my brain?

[13:02] So, I had Claude make me

[13:04] a microworld. This is a debugger,

[13:06] ephemeral UI that was built specifically

[13:09] to visualize the internal implementation

[13:11] of my programming language.

[13:13] What's happening here is that I'm

[13:14] scrubbing through a timeline that's

[13:16] running step-by-step what's my

[13:17] interpreter doing. It's visualizing all

[13:19] the state at every step. So, I can kind

[13:21] of open the hood and see what's going on

[13:23] and start feeling it, you know?

[13:25] And yes, I can use I used this to fix

[13:27] bugs. I even had a little

[13:29] hard to see here, but there's a

[13:30] commenting feature where I can leave

[13:32] comments for myself on the timeline so I

[13:33] remember what I was thinking.

[13:36] And I use this to fix fix narrow bugs,

[13:38] but also as I was fixing the bugs, I was

[13:41] getting a feel for the machine, right?

[13:42] That's something that if you just have

[13:43] an agent go fix the bug, you don't get

[13:45] that peripheral vision. If you live in a

[13:47] micro world, you do.

[13:50] Another example,

[13:51] um

[13:52] I was migrating my personal website from

[13:54] one framework to another. And first

[13:56] thing I did, I had I said, "Claude,

[13:57] write me a script to do."

[13:58] It did this.

[14:00] It seemed like it worked, and I read the

[14:02] script and I was like, "Ah, I don't

[14:03] know." Like

[14:04] I I just don't have a feel for what it's

[14:05] doing. A bunch of files went a bunch of

[14:07] places. It seems right.

[14:10] So, what I did is I said, "Hey Claude,

[14:11] make me essentially a video game where I

[14:14] do the port myself." And the way this

[14:15] works is old website on the left, new

[14:17] website on the right. I just click a

[14:19] button, next, next, next. And at each

[14:20] step, it says, "Here's the commands I'm

[14:22] running. Your new website's coming to

[14:23] life step by step. You see it."

[14:26] There's actually file trees down there

[14:28] where I can see files moving.

[14:29] And it's the the result is it's kind of

[14:31] like if I did it manually,

[14:33] but

[14:34] I'm just clicking a button. So, I'm

[14:35] getting some of the benefit of doing it

[14:36] iteratively without the pain.

[14:42] And I think the big takeaway here is

[14:43] agents can write code to help us

[14:45] understand code. Where the point isn't

[14:47] building software to ship, it's building

[14:49] these little micro worlds for us. It's

[14:51] the math land, right? It's It's a It's a

[14:53] simulation of just this thing.

[15:00] Quickly, the last topic, shared spaces.

[15:03] So far, we've This has all been about

[15:05] me, solo understanding. But a lot of the

[15:07] time, I think the challenge is actually

[15:08] you're working on a team.

[15:10] And your whole team needs to understand

[15:12] together so you can actually jam and

[15:14] have creative ideas together.

[15:16] We think a ton about this at Notion.

[15:19] We believe that, you know,

[15:20] the shared understanding that exists

[15:22] between you and someone else is what

[15:23] lets you communicate effectively.

[15:25] Whether that's

[15:26] names for parts of a system, it could be

[15:29] names for UI elements or concepts,

[15:31] right?

[15:33] So, we we think a lot of Notion about

[15:34] how do you make tools that enable

[15:35] collective understanding.

[15:37] Some things we're exploring,

[15:39] can you have multiplayer chat threads

[15:40] between multiple humans and agents

[15:42] together?

[15:43] So,

[15:44] here, you know, I might ask a product

[15:46] manager on my team, "Hey, you know,

[15:49] what what are users asking for with this

[15:50] feature?"

[15:51] And she might say, "Hey, I don't know.

[15:53] Let's ask a different agent." And that

[15:55] agent comes in and talks to us.

[15:57] What's happening here is that instead of

[15:58] me and my PM both talking to our own

[16:01] agents, we're in a shared space, we can

[16:03] see each other's communication. It's

[16:05] kind of like, you know, going from

[16:06] one-on-one conversations to Slack

[16:07] channels, you know? You see more of the

[16:09] behavior happening together and you

[16:11] understand together.

[16:14] Also, having documents that you can talk

[16:16] about together is a really powerful

[16:17] primitive.

[16:18] Here, you know, Claude made us a plan.

[16:21] What if I have a question about that

[16:22] that I want to discuss with my team? I

[16:24] can just leave a comment because this

[16:25] isn't a collaborative space, not on my

[16:27] computer locally.

[16:29] And then I can ask, "Hey, you know, what

[16:30] do you think about this?"

[16:32] And my teammate can chime in and and we

[16:33] can talk about it right there, right? I

[16:35] think having these spaces for shared

[16:37] discussion around ideas with our agents

[16:39] is really powerful for building up that

[16:44] This, by the way, um we just launched

[16:45] last week the ability to bring coding

[16:47] agents into Notion. So, Claude and

[16:48] Cursor can now live in Notion. And our

[16:50] team actually builds a lot of our code

[16:52] in Notion itself,

[16:54] mainly because of these benefits,

[16:55] because having it in a shared space is

[16:57] just so valuable.

[17:01] Okay, so we've talked about these three

[17:03] I want to bring it back to the

[17:04] beginning.

[17:06] You know, I think at the beginning I

[17:07] said,

[17:09] "It's important for humans to still

[17:10] understand how the code works, right?"

[17:12] But I actually think it's much bigger

[17:13] than that.

[17:15] I kind of think it's just important for

[17:17] humans to still understand how

[17:18] everything works.

[17:22] And maybe, you know, you all agree it

[17:23] sounds like.

[17:24] But this I think is being called into

[17:25] question now and is something we

[17:26] actually have to actively fight for.

[17:29] The thing is this is not a new battle.

[17:32] It actually hearkens back to the very

[17:33] origins of our field.

[17:36] Alan Kay is one of the pioneers of

[17:37] personal computing, co-inventor of the

[17:39] modern GUI. And literally 50 years ago

[17:42] he wrote this essay

[17:43] that I find very prescient, called a

[17:45] personal computer for children of all

[17:46] ages.

[17:48] It looks like two kids on iPads watching

[17:50] YouTube or something, right? It's kind

[17:51] of crazy. This is 50 years ago his

[17:53] vision. But that's not YouTube on the

[17:55] iPads. What he envisioned is, "Hey,

[17:56] these kids, they're playing a video game

[17:59] and they're modifying the code as they

[18:00] play it to learn physics."

[18:03] So the point isn't the computer, it's

[18:04] the kids.

[18:06] The point of computers was to level us

[18:07] up as humans, right?

[18:09] And Alan has talked a lot about how it

[18:11] kind of feels like at some point

[18:12] computers

[18:13] detoured a bit from that vision.

[18:16] But I think the exciting thing is maybe

[18:17] now's the time to bring that back.

[18:20] Here's kind of the meme version of that.

[18:23] I think with AI, a lot of people are

[18:25] waking up to, "Oh my gosh,

[18:27] code is free. We can make ephemeral UIs,

[18:29] dynamic simulations to understand

[18:31] concepts. We can make debuggers,

[18:32] playgrounds."

[18:34] And it's like, "Yes, that's great." And

[18:37] it's actually not a new idea. Like this

[18:39] was the goal all along.

[18:41] And so I think the optimistic thing that

[18:42] I find really exciting is

[18:45] hey, it's still really important to

[18:46] understand how things work.

[18:48] And with the right tools and the right

[18:50] mindset and the right creativity,

[18:52] we can actually understand better than

[18:53] ever before, not less. With AI, we can

[18:56] kind of empower ourselves more,

[18:58] not just taking ourselves out of loops,

[19:00] but actually putting ourselves more

[19:02] deeply in loops than we ever have

[19:03] before.

[19:05] And I think that's a really exciting

[19:06] prospect and I hope it's something that

[19:07] we all, together as an industry, figure

[19:10] out.

[19:12] That's all I have for you today. Thank

[19:13] you so much.

[19:15] &gt;&gt; [applause]

## Connection to Wiki Concepts

- [[entities/geoffrey-litt]] — Speaker entity page
- [[concepts/agent-engineering]] — Human-in-the-loop patterns for agent development
- [[concepts/autonomous-coding]] — Autonomous coding loops and their limitations
- [[concepts/developer-experience]] — Developer productivity and understanding

## Notable Quotes

- "It is not enough to just verify correctness — you actually need to understand the work they are doing."
- "Autonomous loops are hot, but the reality is that most agentic tasks still require human judgement."
