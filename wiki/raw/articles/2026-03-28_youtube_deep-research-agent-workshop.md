---
title: "Build Your Own Deep Research Agent with Ivan Leo (Google DeepMind)"
source: YouTube / Vanishing Gradients
channel: Vanishing Gradients
speakers: ["Hugo Bowne-Anderson", "Ivan Leo"]
date: 2026-03-28
duration: "89:34"
url: https://www.youtube.com/watch?v=LUfqQgz1-Os
type: talk
tags: [deep-research, subagents, planning-agent, agent-loop, youtube]
---

# Build Your Own Deep Research Agent with Ivan Leo (Google DeepMind)

89-minute live workshop. GitHub companion: https://github.com/hugobowne/build-your-own-deep-research-agent

Ivan Leo built production agents at Manus before joining DeepMind. In this workshop he shows how to build a deep research agent from scratch with Gemini, starting from a raw API call and ending with an agent that asks clarifying questions, writes a research plan, dynamically spawns as many subagents as it needs to search the web with Exa, and synthesizes a cited report.

## Chapters
00:00 Welcome
01:01 Ivan's Path: Manus, Kura, and Now DeepMind
03:47 What We're Building: Raw API to Research Agent in 4 Steps
06:01 When Deep Research Makes Sense (and When It Doesn't)
12:16 Start With the Best Model, Then Optimize Down
13:48 Repo Tour: The 10-Step Build Sequence
16:54 Live Trace: Watch the Agent Plan and Spawn Subagents
27:08 Step 1: Raw Gemini API Call, No Tools
29:03 Why Tool Calling Beats Parsing Text Output
35:00 The Handler Loop: Making Tool Results Useful
37:25 Tool Runtime: One Class to Register Any Tool
40:52 Are All General-Purpose Agents Coding Agents?
44:18 Adding State: Iterations, Todos, and User Permissions
46:23 The Todo Tool: Making the Agent Track Its Own Work
47:24 Don't Break Your Cache: What to Avoid in Production
47:50 Build Your Own vs. Provider SDKs: The Real Trade-offs
53:42 Defensive Coding: Handling Unknown Tools and Bad Arguments
56:16 Agent Loop Demo: Watching the Todos Work
58:59 Hooks: Trigger Logic at Any Point in the Agent Lifecycle
01:03:00 System Prompts and Progressive Disclosure
01:08:08 Deterministic Guardrails: Forcing the Agent to Finish Its Todos
01:19:55 Subagents Live: Spawning Parallel Searches with Exa
01:26:03 Phase Swapping: How the Agent Moves from Planning to Execution
01:27:25 Wrap Up and Next Steps

## Transcript (representative segments)

     1|[00:00] And we are live. What is up, Ivan Leo?
     2|[00:05] Hey, what's up, Hugo? Good to see you
     3|[00:06] after a long time. I think the last time
     4|[00:07] we met was like for the previous AI
     5|[00:09] assistant workshop. Yeah.
     6|[00:11] &gt;&gt; Exactly. Exactly. So, welcome everyone.
     7|[00:13] And Ivan and I actually recently did a
     8|[00:15] workshop on building your own open core.
     9|[00:19] Really, the the premise was to build
    10|[00:20] agents that build themselves and being
    11|[00:22] able to get them to build their own
    12|[00:24] extensions, hooks, and skills in real
    13|[00:25] time and hot reload, so you don't even
    14|[00:27] need to restart them, was so powerful.
    15|[00:30] Uh love to welcome you all to this
    16|[00:31] workshop on building your own uh deep
    17|[00:34] research agent. We're putting YouTube
    18|[00:36] that um the Q&amp;A will happen in Discord.
    19|[00:39] Uh so, please do uh join the Discord in
    20|[00:42] the workshop's channel. And I'm actually
    21|[00:44] just going to put a link there to the
    22|[00:46] previous workshop we did. I've put the
    23|[00:48] GitHub repository there as well. Say hi,
    24|[00:51] introduce yourself. Uh and and let us
    25|[00:53] know what your interest in such things
    26|[00:56] is or are. Like, do you work in AI? Do
    27|[00:58] you work in ML or or or what's up? Um
    28|[01:03] Ivan, congratulations on your new job at
    29|[01:06] DeepMind.
    30|[01:07] Yeah, thanks so much, man. I'm really
    31|[01:08] excited to start on the team. I started
    32|[01:10] on Monday and it's been absolutely
    33|[01:12] incredible. I think everyone is so
    34|[01:13] friendly and I think, you know, I'm just
    35|[01:15] really hoping to spread the good word
    36|[01:16] about Gemini.
    37|[01:18] Absolutely. And uh on top of that, this
    38|[01:21] is pretty funny, but um last year I did
    39|[01:24] many workshops with a good friend of
    40|[01:25] mine, Ruven Kumar, at at DeepMind, um
    41|[01:29] who then was working a lot on Gemma. And
    42|[01:31] we actually put out 10 hours of free
    43|[01:33] workshops on building AI products with
    44|[01:34] Gemma. I'm going to link to that in the
    45|[01:36] Discord as well. What's funny is after I
    46|[01:39] did these, I was like, "Okay, I got to
    47|[01:40] like
    48|[01:41] diversify who I'm doing workshops with
    49|[01:43] at the moment." Um
    50|[01:45] and so, you among other people, but hey,
    51|[01:47] look, it's chill and you're all doing
    52|[01:49] such amazing work at at DeepMind as
    53|[01:51] well. Um
    54|[01:52] hey, everyone, uh
    55|[01:54] we'll get started in a minute or two,
    56|[01:56] but please do um hit like and subscribe,
    57|[02:00] share this with a friend who might be
    58|[02:01] interested. Right now, that's the best
    59|[02:02] way to support the channel. Uh we have
    60|[02:04] upcoming events as well. Check out Luma
    61|[02:06] in the description in
    62|[02:09] YouTube.
    63|[02:11] On top of that, I'd like to say a few
    64|[02:13] words of introduction to uh introduce
    65|[02:17] Ivan today. Ivan,
    66|[02:19] um we met when you were working with
    67|[02:22] Jason Liu, right?
    68|[02:24] &gt;&gt; Yeah. I think we met a long time ago
    69|[02:25] when I was working with Jason. Back
    70|[02:27] then, we were doing a lot of voice and
    71|[02:28] instructor. Yeah. Exactly. Uh and you
    72|[02:31] were also working on something super
    73|[02:33] cool called Cura, which we did some some
    74|[02:36] workshops on or lightning lessons and
    75|[02:38] that type of stuff that I'll also put a
    76|[02:40] a link to, but something I really
    77|[02:41] appreciate about your work on Cura
    78|[02:43] essentially like with agent traces, how
    79|[02:45] to how to like get signal from them. Um
    80|[02:48] and and Cura in terms of clustering and
    81|[02:50] having observability in this type of
    82|[02:51] stuff into agentic traces was super
    83|[02:53] powerful. It was it wasn't Jason who
    84|[02:55] introduced us though. It was Swyx from
    85|[02:57] Latent Space initially. I was like,
    86|[03:00] "Hey, Swyx, I'm going to Singapore.
    87|[03:01] Introduce me to some cool people." He
    88|[03:03] was like, "You've got to meet Ivan." You
    89|[03:04] took me out to hawker hawker markets and
    90|[03:07] we had skewers and I'm still I mean, we
    91|[03:09] got we got good I told you I'm going to
    92|[03:11] Chinatown in Sydney tonight. We got good
    93|[03:12] skewers here, but the food [laughter] in
    94|[03:13] Singapore was amazing. Then you were at
    95|[03:15] Manifold, which is super relevant to
    96|[03:17] what we're doing today. You were working
    97|[03:19] on Manifold agent. Um you built the
    98|[03:22] Manifold
    99|[03:23] Manifold mail as well, which I've I I
   100|[03:26] used a bunch of. And now you're at
   101|[03:29] DeepMind. Is there anything I've
   102|[03:31] I've missed out there? Yeah, no, I think
   103|[03:33] like that roughly covers a lot of open
   104|[03:34] source. I was at Manifold for a bit
   105|[03:36] building like some of the agents and
   106|[03:37] then now at DeepMind trying to spread
   107|[03:39] the good word on Gemini. Um but yeah, I
   108|[03:41] can't believe it's been so long. I feel
   109|[03:43] like I was working in open source maybe
   110|[03:44] like almost 2 years ago.
   111|[03:46] That's pretty wild, isn't it? So, I'm
   112|[03:48] just going to
   113|[03:50] share my screen to just show a slide or
   114|[03:54] two.
   115|[03:55] Just to um
   116|[03:56] give a sense of what we're up to
   117|[03:58] uh today to give people a little bit of
   118|[04:00] structure. And let me
   119|[04:06] sick.
   120|[04:09] Okay. So, we're going to have a brief
   121|[04:10] intro to deep research, what we're
   122|[04:12] building and why
   123|[04:13] and why. Then we're going to jump into
   124|[04:15] building. Um so, we're going to build
   125|[04:17] with Gemini, uh start with a raw API
   126|[04:18] call, then get some tools running and
   127|[04:20] getting a runtime up and running. Then
   128|[04:22] we're going to start adding state,
   129|[04:23] hooks, the agent loop. We'll see what
   130|[04:25] all of this stuff is. Then we're going
   131|[04:26] to let it loose with sub-agents,
   132|[04:27] planning, and observability. Um
   133|[04:30] a schematic of the type of thing we'll
   134|[04:32] build. This isn't quite it because uh
   135|[04:34] Gemini does something far cleverer than
   136|[04:36] what one can actually draw draw here,
   137|[04:38] but it's going to be a prompt.
   138|[04:40] The agent can ask clarifying questions
   139|[04:42] if if needed. I mean, the canonical
   140|[04:44] example is if you say, "Give me tell me
   141|[04:46] about restaurants in Chelsea."
   142|[04:48] Um the agent hopefully will say, "Do you
   143|[04:50] mean London or Manhattan?" Um planner
   144|[04:52] will write a research plan and then uh
   145|[04:54] the main agent will orchestrate
   146|[04:56] sub-agents. Now, something that's really
   147|[04:58] cool about what we're building today is
   148|[04:59] it's not just three sub-agents. It
   149|[05:01] spawns sub-agents that are needed,
   150|[05:03] manages context around them, returns
   151|[05:05] results, and then spins up more if
   152|[05:07] necessary. Uh and then the main agent
   153|[05:09] synthesizes a final report. So,
   154|[05:12] with respect to this the brief
   155|[05:13] architectural diagram, is there anything
   156|[05:15] you'd want to add or clarify, Ivan? Uh
   157|[05:17] yeah, I think um the only thing I'll add
   158|[05:19] is then instead of just like a single
   159|[05:21] run of like sub-agents, really what
   160|[05:22] we've done is we just um written a way
   161|[05:24] that the model can just spawn as many
   162|[05:26] sub-agents as it needs on demand.
   163|[05:28] And so, it can do this as much as it
   164|[05:29] needs. And so, it's kind of a thing you
   165|[05:31] can just tune in the prompt to see like
   166|[05:32] how many rounds of iteration you want to
   167|[05:34] do. Uh maybe you want the model to stop
   168|[05:36] and ask more questions before it spawns
   169|[05:38] more sub-agents.
   170|[05:39] And I think the goal today is just to
   171|[05:40] build like some sort of to sort of show
   172|[05:42] from scratch how you can do you can get
   173|[05:44] a lot out of these models. And
   174|[05:46] especially with something like Gemini
   175|[05:47] where you have
   176|[05:48] especially like Gemini 1.5 Flash and
   177|[05:50] Gemini 1.5 Pro Preview where you have
   178|[05:51] very good pricing, you have a model that
   179|[05:53] is actually has a very low latency.
   180|[05:56] And I think in general it's like pretty
   181|[05:57] good for agentic stuff.
   182|[05:59] So,
   183|[06:01] yeah.
   184|[06:01] So, I do want to first talk before we
   185|[06:04] dive in about why
   186|[06:07] deep research. And I want to preface it
   187|[06:09] by saying, as you know, um I work with a
   188|[06:11] lot of builders and I consult and advise
   189|[06:13] a lot of builders and teach
   190|[06:15] a lot of builders. And a lot of the
   191|[06:16] time, um what people really need are LLM
   192|[06:18] workflows, uh not you know, or and
   193|[06:21] agents embedded in workflows as well,
   194|[06:22] but not like fully fledged
   195|[06:24] uh agents.
   196|[06:27] And I'll actually link to Anthropic's
   197|[06:29] blog post on building effective AI
   198|[06:30] agents, which spells out the types of
   199|[06:32] workflows we're we're we're talking
   200|[06:34] about there. Then when we do get to
   201|[06:35] agents though, a lot of the time, um you
   202|[06:38] actually don't want something as massive
   203|[06:40] of as deep research. You want you want
   204|[06:43] customer service agent or travel
   205|[06:45] assistant or whatever it is, and you
   206|[06:46] want the time to resolution super quick,
   207|[06:49] one or two or three turns. You don't
   208|[06:51] actually have to actively manage any
   209|[06:53] context or anything anything like that
   210|[06:55] cuz there are a handful of retrieval
   211|[06:56] tool calls and that type of stuff. So,
   212|[06:59] I'm just wondering if you can talk a bit
   213|[07:00] about in particular in particular with
   214|[07:02] respect to your work at Manifold, um
   215|[07:04] about when deep research is important
   216|[07:06] and when building these types of agents
   217|[07:08] really comes into its own.
   218|[07:09] Yeah, I think um the most important
   219|[07:11] thing to sort of think about is like
   220|[07:12] what is the metric that matters the most
   221|[07:14] for your users. And so, for example, if
   222|[07:16] you're talking about like customer
   223|[07:17] service um support agents, really what
   224|[07:19] they want is something that can quickly
   225|[07:20] retrieve the relevant data, you know,
   226|[07:22] answer very quickly. And honestly, for
   227|[07:24] something that's just saying, "Hey, what
   228|[07:26] are your opening hours?" or "Hey, are
   229|[07:28] you guys open on Saturday, you know, at
   230|[07:29] like 6:00 p.m.?"
   231|[07:31] Um that's a single-turn sort of agent.
   232|[07:33] Um if you think a lot about, let's say,
   233|[07:34] a lot of the integrations, for example,
   234|[07:36] that have rolled out in, say, um your
   235|[07:38] email clients and even like some of the
   236|[07:40] other like applications, a lot of these
   237|[07:43] are like two or three steps. For
   238|[07:44] example, generate a quick like response
   239|[07:46] to me for this email based on our
   240|[07:48] previous conversations, right? And so,
   241|[07:50] what you want over here is think about
   242|[07:51] from the end user perspective. You don't
   243|[07:54] always need to throw like a really big
   244|[07:55] heavy model. I I know a lot of people,
   245|[07:57] for example, like to throw like Opus 4 6
   246|[08:00] at everything. But the simple truth is
   247|[08:02] if you have like a very well-defined
   248|[08:04] task, if you have good evaluations, like
   249|[08:06] I think what you cover in your course,
   250|[08:07] um
   251|[08:08] once you've verified that a model can
   252|[08:10] actually do the task, like the best
   253|[08:12] models like a GPT-5 and Opus 4 6 or a
   254|[08:14] Gemini 1.5 Pro Preview, um you can
   255|[08:16] actually start experimenting with your
   256|[08:18] evaluation set to start going down to
   257|[08:20] like cheaper models that can do it a lot
   258|[08:21] faster and cheaper. And ultimately, as
   259|[08:23] you start building a product that needs
   260|[08:25] to scale to thousands of users, hundreds
   261|[08:27] of thousands, and hopefully at some
   262|[08:29] point like millions of users,
   263|[08:31] that 20% 10% or even like 2% difference
   264|[08:34] in cost can add up very quickly. And so,
   265|[08:36] I think like a lot of these are quick
   266|[08:38] iterations. And I think like you want to
   267|[08:40] realize that you can tune basically
   268|[08:42] every single part of this pipeline.
   269|[08:44] Whether it's the model you're using, the
   270|[08:45] prompt, and also I think the most
   271|[08:47] important thing is the tools that you
   272|[08:48] give it. Um and I think we also
   273|[08:50] discussed a bit about this whereby
   274|[08:52] now these models are good enough whereby
   275|[08:54] you can basically meta do a lot of meta
   276|[08:57] prompting. So, when I was actually
   277|[08:58] building this um if you go to the
   278|[09:00] repository and you look at, say, step
   279|[09:02] eight to step nine, you notice that the
   280|[09:04] prompt got a lot bigger. Um they got a
   281|[09:06] lot more detail.
   282|[09:08] And actually, a lot of it was me just
   283|[09:09] asking Gemini, "Hey, um here are some
   284|[09:11] examples of writing I like. You try to
   285|[09:13] do a simple bit of a rewrite." And then
   286|[09:15] I would basically say, "Hey, um based on
   287|[09:17] the initial information that you
   288|[09:18] understood,
   289|[09:20] the final result that I wanted, how
   290|[09:21] could we better make it clearer to you?
   291|[09:23] Right? How could we make our
   292|[09:25] instructions clearer? How could we
   293|[09:27] provide better examples?" And then
   294|[09:28] Gemini actually gave some great
   295|[09:29] examples. And so, you can start to see
   296|[09:31] that a lot of these techniques that
   297|[09:32] wouldn't have been possible a year or
   298|[09:34] two ago are really valuable now.
   299|[09:36] You can do things like ask models, "Hey,
   300|[09:38] how should we describe tools? What sort
   301|[09:40] of tools do you need?
   302|[09:42] What are the descriptions of tools that
   303|[09:43] you want? And how like what sort of
   304|[09:45] information are you not getting in your
   305|[09:47] system prompt or in the context that we
   306|[09:48] have?"
   307|[09:50] And I think that sort of calls back to
   308|[09:51] this idea of like context management. Um
   309|[09:53] it's okay to be a bit less careful, I
   310|[09:55] think, sometimes with your context. It
   311|[09:56] can be a little bit dirty whereby you
   312|[09:58] can just throw the raw context in
   313|[09:59] without cleaning it with a very long
   314|[10:01] pipeline. But, it's very important to
   315|[10:02] think about like the type of context
   316|[10:04] you're providing.
   317|[10:05] Um I think we talked about this in
   318|[10:07] context versus capabilities where if you
   319|[10:09] ask the model, "Hey, what's the date
   320|[10:10] today?" And it doesn't have a either the
   321|[10:13] date in the prompt or a bash tool to run
   322|[10:15] it on your local computer, um it can
   323|[10:17] never really answer the question to you,
   324|[10:19] right? That's like a capability. A
   325|[10:21] capability is a tool it can execute to
   326|[10:22] get the date. And a context would be,
   327|[10:24] well, the date is in the prompt. And so,
   328|[10:27] I think like that's a lot of stuff that
   329|[10:28] you should think about when building
   330|[10:29] agents. Like, what is the use case you
   331|[10:30] care about? What is the metric you want
   332|[10:32] to push? Start to think a lot about
   333|[10:34] evaluations from day one. And then
   334|[10:36] realizing that for a lot of these cases,
   335|[10:38] you want to start There are a lot of
   336|[10:40] these different knobs that you can turn
   337|[10:41] and at the end of the day having a clear
   338|[10:43] north star is really important.
   339|[10:45] Totally. And one thing I do want to
   340|[10:46] index on, there was so much wonderful
   341|[10:48] stuff in there. One thing is you
   342|[10:49] mentioned, when building something,
   343|[10:52] try it first with the best model to just
   344|[10:54] see if it's something you can do, right?
   345|[10:56] And then you can go to cheaper, lower
   346|[10:59] latency, uh what whatever it may be. And
   347|[11:01] it's interesting that that's kind of the
   348|[11:02] inverse or the opposite of what we do
   349|[11:05] classically in machine learning where,
   350|[11:07] you know, let's say you've got binary
   351|[11:08] classification, maybe you start with a
   352|[11:09] baseline of multi-class classifier or
   353|[11:11] sorry, of majority majority classifier.
   354|[11:14] Um
   355|[11:15] and so, you start with kind of the
   356|[11:16] silliest, dumbest idea and then that's
   357|[11:18] your baseline. And we've kind of flipped
   358|[11:20] it cuz we've got these powerful
   359|[11:21] pre-trained models that we can use.
   360|[11:23] Yeah, I think like that's a funny thing
   361|[11:25] about like working with agents nowadays
   362|[11:26] is that a lot of people
   363|[11:28] try to apply those same concepts. Um
   364|[11:31] really what you want to really
   365|[11:32] investigate when it comes to building
   366|[11:33] agents is whether or not this task is
   367|[11:35] possible for a language model to create
   368|[11:37] or to operate. And I think like often
   369|[11:39] times you can do a lot less prompting
   370|[11:41] when you use a really powerful model
   371|[11:42] like Gemini 3.1 for preview. Um and so,
   372|[11:46] I think a lot of it is just verifying
   373|[11:48] that the task can be done.
   374|[11:50] And then afterwards optimizing it for a
   375|[11:52] production use case. I think a lot of
   376|[11:53] people start by thinking about the cost
   377|[11:55] like, "Oh my god, like um Gemini 3.4
   378|[11:58] preview is like so much more expensive
   379|[11:59] than flash or like, I want to use Opus."
   380|[12:02] And it's like
   381|[12:03] X number of dollars like Opus cost. But,
   382|[12:06] when you're actually building a
   383|[12:07] prototype or you're trying to show that
   384|[12:08] your product works, you should get it
   385|[12:10] right first and then you should get it
   386|[12:12] then you should make it like optimize
   387|[12:14] after that, you know?
   388|[12:15] Totally. And also, so let's let's jump
   389|[12:18] in a second, but if it if the models
   390|[12:20] don't seem capable today, that doesn't
   391|[12:22] mean they won't be tomorrow. So, dream
   392|[12:24] big. And I'm actually going to link to a
   393|[12:25] podcast and I did a blog post with
   394|[12:28] Nicholas Moy who he was head of AI
   395|[12:30] research at Windsurf. So, now at
   396|[12:33] DeepMind working on anti-gravity among
   397|[12:35] other things in a different part of part
   398|[12:36] of DeepMind today. Yourself, but you
   399|[12:38] know, he built at Windsurf the first
   400|[12:41] multi-hop agent. Um and what they were
   401|[12:45] trying to do just wasn't possible. Like,
   402|[12:47] they they couldn't do it, but they knew
   403|[12:49] what they wanted. So, they were doing
   404|[12:50] something else in the meantime. Then a
   405|[12:52] particular um release of Claude came out
   406|[12:55] and they saw one day that it that it
   407|[12:57] worked. And then they just and they saw
   408|[12:59] it shoot off. They see the saw all of
   409|[13:01] their users going absolutely mad. Um so,
   410|[13:04] you know, dream big and let let your
   411|[13:06] models and agents fly.
   412|[13:07] Yeah, for sure. I think a lot of times
   413|[13:09] they say, you know, spend today for the
   414|[13:11] models of tomorrow.
   415|[13:12] So, like back then, let's say back in
   416|[13:14] the day when this was like a while back,
   417|[13:16] so I'm exposing how long I've been in
   418|[13:18] like the LLM space, but back then when
   419|[13:20] you use like GPT 3.5 versus GPT 4, you
   420|[13:23] know, a lot of people were saying like,
   421|[13:25] "Oh, GPT 4 is really expensive at this
   422|[13:27] cost." And they they kept trying to make
   423|[13:30] things work in GPT 3.5, but if you spend
   424|[13:32] money for the models of tomorrow, you
   425|[13:34] just want to use the best models to make
   426|[13:35] sure it's possible to to make sure this
   427|[13:37] specific very hard case is being catered
   428|[13:39] for.
   429|[13:40] Um often times you can find very
   430|[13:41] surprising results and then when the
   431|[13:43] model prices drop again, then it's
   432|[13:45] beautiful.
   433|[13:46] Exactly. Yeah. So, let's let's jump in,
   434|[13:49] man. Do you want to share your screen?
   435|[13:51] I've linked to the GitHub repository. Um
   436|[13:53] please do introduce introduce yourself
   437|[13:54] in Discord, say what's up if you if
   438|[13:56] you'd like to. Uh links in the chat and
   439|[13:59] in the YouTube description. On top of
   440|[14:02] that, if you're going to code, feel free
   441|[14:04] to code along if if you want. I would
   442|[14:06] encourage you to pay more attention to
   443|[14:08] what we're building and the
   444|[14:10] conversation. Like, don't don't get
   445|[14:11] stuck on trying to get an API key
   446|[14:13] working and fall behind. You can always,
   447|[14:15] you know, run the code after the fact.
   448|[14:17] So, um
   449|[14:21] Yeah.
   450|[14:21] &gt;&gt; go.
   451|[14:22] Yeah, I think we can start coding. Um
   452|[14:25] Can you just zoom in
   453|[14:26] a little bit
   454|[14:27] as well? a little bit so you can see. Um
   455|[14:30] I've zoomed in a little bit here. Let me
   456|[14:32] just pull this down so everyone can take
   457|[14:33] a look at the code. Um
   458|[14:36] maybe this is enough or maybe like one
   459|[14:37] more.
   460|[14:37] &gt;&gt; Yeah, that's Well, one more would be
   461|[14:39] great. And if you want to actually also
   462|[14:41] just open the read me to start. Dude,
   463|[14:46] when I dictate, because I dictate most
   464|[14:48] of my stuff to LLMs now, like most
   465|[14:51] speech-to-text cuz of my accent say read
   466|[14:53] me. Uh
   467|[14:55] A I D M E.
   468|[14:57] So, there you go.
   469|[14:59] Funny things with accents, yeah. Yeah.
   470|[15:03] I I think it happens, yeah. I I just
   471|[15:05] pray that the language model gods can
   472|[15:07] understand what I say and they just just
   473|[15:09] got everything.
   474|[15:11] AJ.
   475|[15:12] &gt;&gt; [laughter]
   476|[15:12] &gt;&gt; That's it. All right, so what what are
   477|[15:14] we doing, man? Right, so today we're
   478|[15:16] going to be building a deep research
   479|[15:18] agent. I think previously Hugo talked a
   480|[15:19] bit about the different steps. So, I
   481|[15:21] think the way that we're going to try
   482|[15:22] running it today is we're going to have
   483|[15:24] these four distinct steps. Uh the first
   484|[15:26] one is just Hello Gemini where we go
   485|[15:28] from a raw API call to a tool runtime.
   486|[15:31] And really what a tool runtime is over
   487|[15:32] here is just that it's a simple class
   488|[15:34] where we can execute tools um very
   489|[15:36] easily without hardcoding a lot of it.
   490|[15:38] Um it'll make a bit more sense down the
   491|[15:40] line. And I think the point of the first
   492|[15:42] section is really to kind of point out
   493|[15:43] like why you need tool calling, right?
   494|[15:46] Um and then the next part we're going to
   495|[15:47] be talking about is like we're going to
   496|[15:49] be introducing like state, hooks, and
   497|[15:50] then agent loop. And this is going to be
   498|[15:53] corresponding to four, five, six, and
   499|[15:56] seven where we have like sub agents for
   500|[15:58] the first time.
   501|

---
Note: Full transcript (93,118 chars, 2,776 segments) available at /tmp/yt_deepresearch_clean.txt
