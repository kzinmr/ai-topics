---
title: "Building Your Own OpenClaw from Scratch — Workshop (YouTube)"
source: YouTube / Vanishing Gradients
channel: Vanishing Gradients
speakers: ["Hugo Bowne-Anderson", "Ivan Leo"]
date: 2026-02-28
duration: "96:39"
url: https://www.youtube.com/watch?v=dDQ4rKXeHRw
type: talk
tags: [agent-harness, self-improving, openclaw, coding-agents, agent-loop, youtube]
---

# Building Your Own OpenClaw from Scratch with Ivan Leo (Manus)

96-minute live workshop walkthrough. GitHub companion: https://github.com/hugobowne/build-your-own-ai-assistant

## Chapters
00:00 Live Workshop Kickoff
00:35 Discord Q&A And Announcements
03:39 Workshop Roadmap Overview
05:15 What Is An Agent
08:21 Demo of Coding Agent Cleaning Your Desktop
11:19 Pi And OpenClaw Overview
14:58 Agent Design Principles: Context, Capabilities, And Memory
21:19 Agents, Tools, Skills, MCP, & Hooks
27:08 Repo Walkthrough And Requirements
32:13 Model Cost Tradeoffs
33:47 Tool Calling Basics
39:58 Parsing Function Calls
46:34 Refactoring the Agentic Loop
50:29 Choosing Flash vs Opus
56:44 Runtime and Tool Abstractions
01:02:56 Scaling Tools and Testing
01:04:25 The Agent Tooling Factory
01:05:20 Hot Reloading Tools
01:08:07 The Agent Writes Its Own Tools!
01:11:14 Hook System Overview
01:14:43 Hook Rendering Demos
01:18:31 Server And Telegram Bot
01:24:46 Skills And Progressive Disclosure
01:27:30 Sandboxing With Workers
01:33:26 Async Tools And Subagents
01:35:03 Wrap Up And Next Stream

## Transcript (representative segments)

     1|[00:00] We are live. What is up, Ivan Leo? Great
     2|[00:04] to see you, man.
     3|[00:05] &gt;&gt; It's great to see you, too, man. I think
     4|[00:07] really excited to be here today.
     5|[00:09] &gt;&gt; I'm so excited. I mean, we've been we've
     6|[00:11] worked together before and chatted on
     7|[00:14] um you've come and uh given a guest talk
     8|[00:17] at my course uh among other things and
     9|[00:19] we've met in person a couple of times in
    10|[00:21] Singapore and always had a great time
    11|[00:22] chatting. So to put together a workshop
    12|[00:25] on how to build your own agent in
    13|[00:27] particular uh starting off with the pi
    14|[00:29] agent and moving on to uh different
    15|[00:32] parts of o open core is so exciting. I
    16|[00:35] would love to welcome everyone who's
    17|[00:36] watching on YouTube. Uh we are we have
    18|[00:40] our Q&amp;A on discord and that's so that we
    19|[00:42] can continue the conversation
    20|[00:44] afterwards. So I've put the link in the
    21|[00:46] description to discord. I'm also going
    22|[00:48] to put it in the chat. Uh, but put all
    23|[00:51] your comments and questions in Discord.
    24|[00:53] Um, and we'll we'll answer as many as we
    25|[00:56] can in real time and catch up after with
    26|[00:58] things that we don't get to. So, in the
    27|[01:00] workshops channel, that link should take
    28|[01:02] you to workshops uh immediately. But I'm
    29|[01:06] super excited to be here today with Ivan
    30|[01:08] Leo who just wrapped up all the
    31|[01:10] wonderful work you were doing at Manis.
    32|[01:12] Uh, has been working on KURA as well.
    33|[01:14] Worked at 567 with Jason Leu for for
    34|[01:17] some time. Um what's up Ivan?
    35|[01:21] &gt;&gt; Uh yeah I mean I'm just taking a break.
    36|[01:23] I think it's been really exciting diving
    37|[01:24] into things like uh high open call um
    38|[01:27] and just getting my head out after
    39|[01:29] having worked on product for so long. I
    40|[01:31] think the scene has just shifted so fast
    41|[01:32] and what was an agent just a year ago or
    42|[01:34] six months ago has just changed
    43|[01:36] tremendously. And so I think like
    44|[01:38] today's workshop was really such a great
    45|[01:39] way for me to be able to get back get my
    46|[01:41] hands sort of dirty again and really
    47|[01:42] understand like hey like what are some
    48|[01:45] of the new and great ideas that a lot of
    49|[01:46] these open source projects have been
    50|[01:48] working on. So yeah it's been really fun
    51|[01:50] honestly. [laughter]
    52|[01:53] &gt;&gt; Totally. So I just want to remind
    53|[01:55] everyone please do introduce yourself in
    54|[01:56] the chat in in Discord and we'll start
    55|[01:59] in a minute. I do want to say check out
    56|[02:01] our Luma calendar. If you like enjoy
    57|[02:03] these types of things, please do like
    58|[02:04] and subscribe and share with a friend is
    59|[02:05] the best way you can can support when we
    60|[02:08] um you know Ivan and I put put a lot of
    61|[02:10] time and work into this. Um in terms of
    62|[02:12] our Luma calendar, I'm sharing something
    63|[02:14] Ivan and I have been chatting about and
    64|[02:17] just announcing now. Um we'll be running
    65|[02:19] another workshop next month on build
    66|[02:21] your own deep research agent. Uh which
    67|[02:24] I'm pretty excited about. As are you
    68|[02:26] right Ivan?
    69|[02:27] Yeah, I think um a lot of times with all
    70|[02:30] these new agents and everything uh we
    71|[02:32] get a lot more opportunities to build
    72|[02:33] these like really cool applications and
    73|[02:34] so deep research is one of those things
    74|[02:36] that I think it just like is very useful
    75|[02:38] especially as agents can go like so much
    76|[02:40] further. So um really excited about
    77|[02:42] that. You guys should definitely tune
    78|[02:43] in. We're going to be building
    79|[02:44] everything from scratch as usual. A lot
    80|[02:46] of it is just going to be first
    81|[02:47] principles and stripping away the
    82|[02:49] framework so you can sort of understand
    83|[02:50] like what what is the core idea there
    84|[02:52] and um why do you want to even do deep
    85|[02:54] research? Questions like that. Yeah.
    86|[02:56] Totally. Um, and also a a bit of
    87|[02:59] shameless self-promotion on on the
    88|[03:01] channel. Um, I mentioned Ivan has has uh
    89|[03:03] came and given a guest talk at my course
    90|[03:05] before, but Stephan Krachic, who works
    91|[03:07] on agent infrastructure, a friend of
    92|[03:09] mine and I are teaching our final cohort
    93|[03:10] of building AI applications uh next
    94|[03:13] month starting in a couple of weeks. Um,
    95|[03:15] and we've got a lot of wonderful guest
    96|[03:17] guest speakers including Sebastian
    97|[03:18] Rajka, uh, John Barryman, Doug Turble,
    98|[03:21] Inis Montani from Spy, a lot of other
    99|[03:23] cool people. Do check it out if you're
   100|[03:25] interested. We've got over $1,000 in in
   101|[03:27] in uh credits from modal uh which we'll
   102|[03:30] be talking about today as well and
   103|[03:32] pantic logfire and all of these types of
   104|[03:33] things. I'll put that in the description
   105|[03:35] as well. So if you're into such things
   106|[03:37] uh check it out. But without further ado
   107|[03:41] I think we should kind of just jump into
   108|[03:44] it man. And I've actually prepared a few
   109|[03:48] slides. The reason I've done this um is
   110|[03:51] we've got a vast array of people of
   111|[03:53] different experience here. So some
   112|[03:55] people have built agents, other people
   113|[03:57] are just getting their their feet wet.
   114|[04:00] Others are interested and have used LM
   115|[04:02] but don't really know much about agentic
   116|[04:04] stuff. So um in order to make sure that
   117|[04:07] everyone gets something out of this,
   118|[04:09] we've just prepared a bit um you know of
   119|[04:11] uh kind of beginner material which if
   120|[04:15] you've done if you know a lot about this
   121|[04:16] type of stuff um just bear with us. I
   122|[04:18] mean we it'll move very quickly. So, let
   123|[04:21] me share my screen and ask you,
   124|[04:26] Ivan, can you see my screen?
   125|[04:29] &gt;&gt; Uh, yeah, works pretty well for me. I
   126|[04:32] can see it.
   127|[04:32] &gt;&gt; Okay, fantastic. So, to start off with,
   128|[04:35] we're just going to talk about building
   129|[04:37] agents, talk about two in particular,
   130|[04:39] which we'll be building around today, PI
   131|[04:42] and and Open Claw. Then we're going to
   132|[04:44] jump into uh I Ivan's code in layer the
   133|[04:48] land building the base agent giving it
   134|[04:50] hands where it's going to do stuff. Um
   135|[04:52] and it's actually something we'll talk a
   136|[04:54] lot about this more. Um it's going to be
   137|[04:57] extensible. So we don't always give it
   138|[04:59] all the tools, right? We enable it to
   139|[05:01] write its own tools based on what we're
   140|[05:04] what we're talking about. Um then in f
   141|[05:06] the fabulously named ET phone home
   142|[05:08] section we'll be connecting it to
   143|[05:09] telegram uh and then we'll be talking
   144|[05:11] through how to deploy it to modal in
   145|[05:12] order to have it uh sandboxed and
   146|[05:14] secure. So firstly I just wanted to
   147|[05:16] answer the question what is an agent and
   148|[05:18] there are many ways to think about this
   149|[05:20] but actually I did a podcast with Samuel
   150|[05:21] Culvin from paidantic recently um and I
   151|[05:25] like his joke. He uh said there are
   152|[05:27] three definitions. Uh our definition,
   153|[05:30] their LLM, AI person's definition is
   154|[05:32] it's an LLM calling tools in a loop.
   155|[05:34] Infrastructure person's definition, it's
   156|[05:36] a microser. The business person's
   157|[05:38] definition is something that can replace
   158|[05:40] a human and take their salary away. Uh
   159|[05:42] we'll be working with the first
   160|[05:43] definition today, which is an LLM
   161|[05:46] calling tools in a loop. And I just
   162|[05:47] wanted to give a couple of examples.
   163|[05:49] Right? So, you've got a user prompt,
   164|[05:52] send it to the LLM, and then you have it
   165|[05:54] call a tool, uh, and it will send the
   166|[05:57] response back to the LLM, and then the
   167|[05:58] LLM will quote unquote decide or reason
   168|[06:01] about, uh, whether it takes an action,
   169|[06:04] sends [clears throat] a prompt back to
   170|[06:05] the user, uh, sends a response back to
   171|[06:07] the user or calls another tool. And I
   172|[06:09] just want to give you two examples.
   173|[06:10] First is with a coding agent. And we'll
   174|[06:12] see this today. I will say to claude
   175|[06:15] code edit a particular file and it will
   176|[06:19] read that particular file. I joked to
   177|[06:20] Ivan yesterday. Well, it's not even a
   178|[06:21] joke that claude code may even just read
   179|[06:23] my entire codebase at that point and you
   180|[06:25] know lolly gag or bamboozle for you know
   181|[06:28] 6 to 7 minutes but it won't edit it
   182|[06:31] immediately. It will read it. It will
   183|[06:33] return the results of that using that
   184|[06:35] read tool back to the LLM and then it
   185|[06:37] will begin to edit it right and it will
   186|[06:38] do some sort of loop here. Similarly, a
   187|[06:41] search agent. Uh, if I were to ask it,
   188|[06:44] is Ivan cooler than Hugo? Um, I mean,
   189|[06:46] the answer to that is is obvious. Ivan's
   190|[06:48] clearly cooler than than Hugo. But were
   191|[06:51] I to ask it that, perhaps it would
   192|[06:52] perform a search about Ivan, return the
   193|[06:54] result to the LLM, and then go, "Oh,
   194|[06:57] wait. I need to figure out how cool Hugo
   195|[06:59] is as well." And then it will search
   196|[07:01] Hugo and return that. Now, this is a a
   197|[07:03] silly example, right? But if it asks
   198|[07:05] what's better um what's a better API or
   199|[07:08] a better framework X or Y, it will do
   200|[07:10] some research for X and then do some
   201|[07:12] research uh for Y and then perform a
   202|[07:14] comparison.
   203|[07:16] So just to think about how to build
   204|[07:17] these things, I really want to break it
   205|[07:20] down because it is more straightforward
   206|[07:22] than than people think. Um you ping an
   207|[07:24] LLM, you add a tool, you build an
   208|[07:27] agentic loop, and we'll do all of this
   209|[07:29] today. And then you build a
   210|[07:30] conversational loop. So I can uh talk
   211|[07:32] with it [clears throat] time and time
   212|[07:33] again. Uh and perhaps you actually have
   213|[07:36] this conversational loop at the start
   214|[07:37] and doesn't really matter. But these are
   215|[07:39] the building blocks.
   216|[07:42] So what I just want to encourage
   217|[07:45] everyone to internalize is you can
   218|[07:47] actually build a general purpose agent
   219|[07:50] in 133 lines of Python code. And I wrote
   220|[07:52] a blog post on this that I'm going to
   221|[07:54] link to once I stop sharing my screen.
   222|[07:56] um with four tools read, write, edit,
   223|[07:59] bash. And the reason this is so
   224|[08:01] important and this will be a throughine
   225|[08:02] of what we talk about today
   226|[08:05] is and I actually think this is quite
   227|[08:07] profound if if you don't realize it and
   228|[08:09] even if you do that we should stop
   229|[08:11] referring to them as coding agents
   230|[08:13] because they really are computer use
   231|[08:15] agents that happen to be good at coding
   232|[08:17] or great at writing code uh when you
   233|[08:20] give them a bash tool. And I just want
   234|[08:22] to give a quick demo. It's demo time of
   235|[08:25] what what I really [clears throat] mean
   236|[08:27] by that. Okay, this is why things like
   237|[08:30] open claw and co-work and and such
   238|[08:32] things have really uh taken off. So, let
   239|[08:35] me just share my other screen.
   240|[08:43] Let me
   241|[08:51] just one second.
   242|[08:55] Okay.
   243|[09:03] So,
   244|[09:05] Ivan, can you see my terminal?
   245|[09:09] &gt;&gt; Uh, yeah, it works great for me. I can
   246|[09:11] see it.
   247|[09:11] &gt;&gt; Okay, great. Let's just have a look
   248|[09:12] what's in here. Bunch of files and I'll
   249|[09:14] share the code here um when I've I've
   250|[09:17] turned my screen off. But what I'm going
   251|[09:19] to do is I'm going to run um this agent.
   252|[09:23] py file. Okay. Now, this is the 130
   253|[09:26] lines of code that I mentioned earlier
   254|[09:27] or share the code. This is slightly
   255|[09:28] longer because I've made it a bit more
   256|[09:30] verbose so we can see the internals of
   257|[09:32] what's happening. Um, hey, what's up?
   258|[09:36] I'm just using super whisper to dictate
   259|[09:37] here.
   260|[09:39] Thinking. So, it told me it was
   261|[09:41] thinking. I mean, I'm telling it that's
   262|[09:43] that's in the prompt. Um, hey. Okay. So,
   263|[09:45] it's already told me it has reading,
   264|[09:46] writing, editing, and shell commands.
   265|[09:48] Okay. So, those are the four tools I
   266|[09:50] gave it. The four I just showed you.
   267|[09:51] Now, um what I want to show you is Can
   268|[09:55] you see my desktop, Ivan? Uh my file
   269|[09:58] system.
   270|[09:59] &gt;&gt; Uh yeah, it's a bit of a mess.
   271|[10:01] [laughter]
   272|[10:01] &gt;&gt; It's a huge mess. So, let's clear that
   273|[10:05] up. Um okay, so this is my desktop and I
   274|[10:09] actually want to get my agent to Hey,
   275|[10:12] there's a desktop folder. Could you just
   276|[10:14] organize it in some hierarchy set of
   277|[10:16] folders that make sense? Just clean it
   278|[10:17] up for me.
   279|[10:20] Okay, so here it is. Now it's making
   280|[10:23] some tool calls. It's clearly going a
   281|[10:25] loop thinking, let me try a different
   282|[10:27] approach.
   283|[10:30] It's looking in the directory.
   284|[10:34] Ah, it's trying to look at the actual
   285|[10:36] desktop, not the desktop folder. Okay.
   286|[10:38] Ah, now it's gone into this. And now we
   287|[10:41] can see it's it just totally cleaned
   288|[10:44] that desktop folder. Okay, so this is
   289|[10:47] the reason I wanted to demo that is
   290|[10:49] because this is a coding agent. Sure,
   291|[10:52] but what it really is, it's an agent
   292|[10:54] that can do anything that code can do
   293|[10:57] because it has bash. And that's why I
   294|[10:59] really want us all to start thinking of
   295|[11:01] these things as generalpurpose computer
   296|[11:03] use agents and and not just coding
   297|[11:05] agents. And the one of the reasons we
   298|[11:08] decided to um run this workshop is
   299|[11:10] they're easier to build than you than
   300|[11:13] you may think. Um so that that's really
   301|[11:15] all by way of uh motivation and
   302|[11:18] introduction. I do just want to uh share
   303|[11:21] slides again one more time and
   304|[11:25] say a few more things about
   305|[11:28] the types of systems um we're building.
   306|[11:31] So firstly I I want to tell you ah
   307|[11:34] probably need to can you see my pi slide
   308|[11:38] Ivan?
   309|[11:38] &gt;&gt; Uh yeah I can see the pi slide.
   310|[11:40] &gt;&gt; Okay great. So firstly I just want to
   311|[11:42] tell you about pi. Um and I'll I'll
   312|[11:44] share a link in discord but this is the
   313|[11:46] minimal agent within open core. Uh it
   314|[11:48] has four tools the four that I just
   315|[11:50] showed you. It has read writeed bash has
   316|[11:52] a lot of other affordances um including
   317|[11:54] context loading through agents md. It's
   318|[11:56] got a system prompt, has extensibility,
   319|[11:58] which we will be going deep into today.
   320|[12:01] But the real key, this is if you take
   321|[12:04] away nothing except this now. Um, it's
   322|[12:10] this is really the philosophy of how PI
   323|[12:12] works. The entire idea is that if you
   324|[12:15] want the agent to do something it
   325|[12:16] doesn't do yet, you don't necessarily,
   326|[12:19] you know, download an extension, give it
   327|[12:21] a skill, that type of stuff. can do that
   328|[12:22] but you ask the agent to extend itself
   329|[12:25] uh because it celebrates the idea of
   330|[12:26] code writing and and running code. So
   331|[12:28] that's really the the [clears throat]
   332|[12:30] philosophy which we'll see through
   333|[12:31] extensibility um and and through uh so
   334|[12:33] much of what Ivan Ivan has built. A few
   335|[12:36] words about open claw [clears throat] it
   336|[12:38] extends pi in a number of ways uh with a
   337|[12:41] gateway. So you have sessions channels
   338|[12:43] such as telegram cron jobs uh it has a
   339|[12:46] proactive loop which makes it well
   340|[12:48] proactive. Um, you've got heartbeats,
   341|[12:51] you've got chron jobs, they can check
   342|[12:53] your inbox, calendar alerts, reminders,
   343|[12:55] and message proactively. Uh, and it also
   344|[12:57] has uh a sub aent structure. Um, so you
   345|[13:01] got main agents and and sub aents that
   346|[13:03] do a lot of different things in order to
   347|[13:05] uh get results to you. It has a lot of
   348|[13:06] other things in it. As Brian Bishoff
   349|[13:08] might tell you, you know, sub agents are
   350|[13:10] really just tools anyway. Um, so he some
   351|[13:13] people would prefer to call them tools
   352|[13:14] and not necessarily uh sub aents. Um,
   353|[13:17] [clears throat] all that having been
   354|[13:18] said, just to remind you what we're
   355|[13:20] going to do now. That was the brief
   356|[13:22] overview. Ivan's going to build the base
   357|[13:25] agent, give it hands, uh, connect it to
   358|[13:27] Telegram, and then talk about, um,
   359|[13:30] deploying it to modal. And we'll be
   360|[13:31] going through the basic loop with
   361|[13:32] Gemini, tool calling, skills, MCPs,
   362|[13:35] hooks, extensions, memory, compaction,
   363|[13:38] daily files, all the things that are
   364|[13:40] wonderful in OpenCore. Then uh factory
   365|[13:42] patterns um for building tools and oh I
   366|[13:45] don't have this on the yeah I do hot
   367|[13:47] reloading. This is amazing using a
   368|[13:48] factory pattern to be able to uh create
   369|[13:50] a tool and have it not have to restart
   370|[13:53] the the session and be able to use it
   371|[13:54] immediately and then we'll connect to
   372|[13:57] telegram um using a fast API server and
   373|[14:00] then chat through deploying to modal.
   374|[14:02] Have I left anything
   375|[14:05] integral off there Ivan?
   376|[14:08] &gt;&gt; I think that's about it. I think we're I
   377|[14:10] think that's kind of everything that
   378|[14:11] we're going to be covering today. Um
   379|[14:13] really just a lot of the core principles
   380|[14:14] behind building great agents and yeah I
   381|[14:17] can take it away and that
   382|[14:19] &gt;&gt; amazing let's go man. Why don't you
   383|[14:22] share your screen and I'll share a few
   384|[14:23] more links on uh Discord and feel free
   385|[14:26] please ask any questions on Discord as
   386|[14:29] well everyone.
   387|[14:30] &gt;&gt; Uh let me just share my screen. One sec.
   388|[14:33] Entire screen uh should be this one I
   389|[14:35] believe.
   390|[14:37] Cool. Can you guys see my screen? Uh,
   391|[14:40] there should be
   392|[14:41] &gt;&gt; I can now. Yeah.
   393|[14:42] &gt;&gt; All right. Awesome. Yeah.
   394|[14:44] &gt;&gt; So, maybe you could zoom in just a bit.
   395|[14:46] &gt;&gt; All right. Yeah, no problem. So, on my
   396|[14:49] blog at ivalo.com, I've written a
   397|[14:51] series. Uh, it'll be updated after this
   398|[14:54] uh workshop with some of the stuff we've
   399|[14:55] covered. Um, so some of the additional
   400|[14:57] content etc. Um, but really I think
   401|[14:59] we're going to start with just talking a
   402|[15:01] lot about the high level conceptual
   403|[15:02] views and we'll walk through the actual
   404|[15:04] code. So I think it's important to think
   405|[15:05] about what makes an agent like really
   406|[15:08] effective. Um a lot of it comes down to
   407|[15:10] the fact that you have a good model
   408|[15:11] running. For example, if you were
   409|[15:12] running GPD 3.5 versus like Opus 46, the
   410|[15:16] Gemini 3.1 Pro series or even GPD 5.3
   411|[15:19] Codeex, the kind of things that you can
   412|[15:20] imagine
   413|[15:22] doing are like completely different,
   414|[15:24] right? And so you need a really decent
   415|[15:25] model, whatever works for your cost, all
   416|[15:27] latency requirements running in the
   417|[15:29] background. The second thing is that
   418|[15:31] ideally what you have over time if
   419|[15:33] you've used any sort of chat GBT or sort
   420|[15:36] of cloud application or even Gemini
   421|[15:37] recently is that as you use it more and
   422|[15:39] more it has a better sort of
   423|[15:41] understanding of who you are and you
   424|[15:43] notice it starts referencing things that
   425|[15:45] you talked about in the past mistakes
   426|[15:47] you guys made together things you worked
   427|[15:49] through and a lot of it comes down to
   428|[15:51] the fact that at the end of the day it's
   429|[15:52] just a bit of lesson where you just need
   430|[15:54] to give the model either access to the
   431|[15:56] data or just throw it entirely in the
   432|[15:59] model's context. itself. And so often
   433|[16:01] times you see for example OpenAI I think
   434|[16:03] um like with Chad GBT it almost feels
   435|[16:06] like I never see a retrieval tool but it
   436|[16:08] kind of knows and it feels like it's in
   437|[16:10] the context but with cloud sometimes if
   438|[16:12] you ask it certain questions about like
   439|[16:14] what you've been working on hey I've
   440|[16:16] been thinking about this you notice that
   441|[16:17] it starts calling like different tools
   442|[16:18] for retrieval but either way really
   443|[16:20] about it the real takeaway is just that
   444|[16:23] it should have more context on you as
   445|[16:25] you interact more and more with it and
   446|[16:27] in the case of open claw the way they do
   447|[16:29] is that they create memory files for
   448|[16:31] every day every time a compaction is
   449|[16:32] reached. So a compaction happens when
   450|[16:35] you know you have a certain amount of
   451|[16:36] messages and then you say okay it's too
   452|[16:38] much either it's too slow it's too
   453|[16:40] expensive or we're going to reach the
   454|[16:41] context limit of the model and then you
   455|[16:44] do a summarization step. um depending on
   456|[16:46] what you're using this compaction
   457|[16:48] pattern is very different but for open
   458|[16:50] claw what happens is that you actually
   459|[16:51] append it to a memory file and so what
   460|[16:53] the model sees is that you interact with
   461|[16:54] it throughout the day is that it has a
   462|[16:56] timestamp memory where let's say for
   463|[16:58] example now at 8:47 a.m. in Singapore
   464|[17:01] where I am you might see a simple
   465|[17:03] markdown file with 8:47 a.m. this is
   466|[17:06] what we did. This is what we discussed
   467|[17:07] with the user. We ran into these issues
   468|[17:09] and a lot of it comes to the fact that
   469|[17:11] if the model wants to figure out what we
   470|[17:13] talked about during the conversation, it
   471|[17:15] still has access to the raw database or
   472|[17:18] the raw traces in this case JSON files.
   473|[17:21] And the last thing I think that makes
   474|[17:22] like open cloud very good is just that
   475|[17:24] it can extend itself. And a lot of this
   476|[17:25] comes down to the pi coding agent. Uh
   477|[17:28] we'll walk through how this can be
   478|[17:29] implemented under the code with
   479|[17:30] something like a factory method like
   480|[17:32] what Hugo teased just now. But a lot of
   481|[17:35] it comes down to the fact that you want
   482|[17:36] to build software to build software. And
   483|[17:38] so being able to add whether it's
   484|[17:40] skills, whether it's modifying system
   485|[17:41] prompt, whether it's tools, MCPs, at the
   486|[17:44] end of the day, I think when you're
   487|[17:46] building an agent, what you're thinking
   488|[17:47] about is can I give the agent better
   489|[17:50] context, right? If you go back to
   490|[17:51] memories, a lot of it comes down to the
   491|[17:53] fact that, oh, now the model has access
   492|[17:55] to different bits of information that I
   493|[17:57] talked about in the past, right? Or even
   494|[17:59] better data sources like, oh, now it has
   495|[18:01] access to my calendar, right? and it can
   496|[18:03] tell me, oh, in the morning actually
   497|[18:05] maybe before maybe you shouldn't wake up
   498|[18:07] so early. Maybe you should sleep in a
   499|[18:08] bit because the last three days on your
   500|[18:10] calendar you've been having 1:00 a.m. US
   501|[18:11] calls, right? And so this idea of
   502|[18:14] context is really important because with
   503|[18:17] better context, better system prompt,
   504|[18:19] better prompts, better information, the
   505|[18:21] models can do more for you. With
   506|[18:22] capabilities, a lot of it is about
   507|[18:24] extending it and making it easy for the
   508|[18:26] model to either write its own tools or
   509|[18:28] be able to get the information it needs.
   510|[18:30] And so I think it's really important if
   511|[18:31] you don't take anything away from
   512|[18:32] today's talk that you kind of keep this
   513|[18:34] idea at the back of your head of like
   514|[18:36] context and capabilities. Um I got this
   515|[18:38] idea from Jason and it's really helped
   516|[18:40] me shape a lot of how I think about
   517|[18:42] building agents. Um a lot of times when
   518|[18:44] you work with a base model um some sort
   519|[18:47] of like agent um you want to see how
   520|[18:49] good the model is at its core then you
   521|[18:51] start thinking about whether extend in
   522|[18:53] terms of capabilities where extend in
   523|[18:54] terms of like context. Um and so full
   524|[18:58] disclosure for today's um workshop we're
   525|[19:00] not going to clone like open claw pixel
   526|[19:01] for pixel. I think like you know Pete
   527|[19:03] Steinberg did a great job with open claw
   528|[19:05] but what we want to do is we want to
   529|[19:06] break down the key principles that made
   530|[19:08] it good and so we'll be using the Gemini
   531|[19:10] model was in the series specifically
   532|[19:11] Gemini tree flash. Uh it's a really good
   533|[19:14] model and honestly I started using it
   534|[19:15] because it was pretty fast and good. Um,
   535|[19:18] and because initially when I was
   536|[19:19] building out a lot of the code for this
   537|[19:21] workshop, I was thinking of implementing
   538|[19:23] things like streaming, processing the
   539|[19:25] individual events, but Flash is fast
   540|[19:27] enough that it feels like it's almost
   541|[19:29] instant. And so for the use cases of
   542|[19:31] this, and it's also pretty cheap, so I
   543|[19:33] thought I would give it a try. So like
   544|[19:36] what Hugo said, it's not really hard to
   545|[19:38] build a fully functioning agent. um AMP
   546|[19:41] release a code a basically a walk
   547|[19:43] through in go and then I wrote an
   548|[19:45] article on how to do it in typescript
   549|[19:47] for this workshop we'll be running it in
   550|[19:48] pipe fundamentally a lot of it is just
   551|[19:51] running a language model in a loop with
   552|[19:52] enough of a token budget to spare right
   553|[19:55] if you spend enough tokens you let the
   554|[19:57] model run long enough either it goes
   555|[19:58] into a doom loop or it finds your answer
   556|[20:00] right and what makes this really useful
   557|[20:03] is this idea of like tool calling so you
   558|[20:05] might think what's so useful about a
   559|[20:07] model being able to output like JSON
   560|[20:08] text Okay. But if you look at any of the
   561|[20:11] systems that we built today, uh whether
   562|[20:12] it's the code editor you're writing in,
   563|[20:14] whether it's the Telegram messages
   564|[20:16] you're sending, or even like any sort of
   565|[20:18] website that you've used, a lot of times
   566|[20:19] you have multiple services working
   567|[20:21] together, whether it's the front end
   568|[20:22] website, the backend infrastructure, the
   569|[20:25] server, um your local sort of like CLIs
   570|[20:29] by having like type contracts of like,
   571|[20:31] hey, I can call these specific functions
   572|[20:33] and when I call this function, I will
   573|[20:35] send over like a JSON payload that looks
   574|[20:36] like this. But we kind of take our
   575|[20:38] models from just saying like oh these
   576|[20:40] are smart autocomplete machines to these
   577|[20:42] are now agents right which are able to
   578|[20:44] reason and work over very long and
   579|[20:47] autonomous sort of like work workflows
   580|[20:49] because they can call tools to get
   581|[20:51] information. They can call tools to edit
   582|[20:53] the state like what Hugo state reading
   583|[20:55] of Hugo said just now just reading a
   584|[20:57] file editing the file etc. And then they
   585|[20:59] can take that state and make better and
   586|[21:01] more informed decisions as you see later
   587|[21:02] on. Um, and so really I think this is
   588|[21:07] what flipped the switch for me when I
   589|[21:09] saw like um some of these models really
   590|[21:11] getting very good at like just calling
   591|[21:13] two calls being able to gather the
   592|[21:15] context they need themselves and the
   593|[21:16] fact that this could just happen out of
   594|[21:18] the box. U moving on a bit to like
   595|[21:21] skills and MCPs and I guess like hooks
   596|[21:23] and extensions. Um I think going back to
   597|[21:25] the idea of like context and
   598|[21:27] capabilities. Um, a lot of times I think
   599|[21:29] what you realize is that as you build
   600|[21:32] agents, you can't give it like a
   601|

---
Note: Full transcript (96,916 chars, 2,670 segments) available at /tmp/yt_selfbuild_clean.txt
