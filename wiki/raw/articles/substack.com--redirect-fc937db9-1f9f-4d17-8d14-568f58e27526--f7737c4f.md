---
title: "Why Nvidia builds open models with Bryan Catanzaro"
url: "https://substack.com/redirect/fc937db9-1f9f-4d17-8d14-568f58e27526?j=eyJ1IjoiMmZseDYifQ.6O_iC1_GWCzChnbrHzSrs1hMpJpoODTUJm_FAk3tf6E"
fetched_at: 2026-04-15T18:21:46.197826+00:00
source_date: 2026-04-15
tags: [newsletter, auto-ingested]
---

# Why Nvidia builds open models with Bryan Catanzaro

Source: https://substack.com/redirect/fc937db9-1f9f-4d17-8d14-568f58e27526?j=eyJ1IjoiMmZseDYifQ.6O_iC1_GWCzChnbrHzSrs1hMpJpoODTUJm_FAk3tf6E

One of the big stories of 2025 for me was how Nvidia massively stepped up their open model program — more releases, higher quality models, joining a small handful of companies releasing datasets, etc. In this interview, I sat down with one of the 3 VP’s leading the effort of 500+ technical staff, Bryan Catanzaro, to discuss:
Their very impressive Nemotron 3 Nano model released in Dec. 2025, and the bigger Super and Ultra variants coming soon,
Why Nvidia’s business clearly benefits from them building open models,
How the Nemotron team culture was crafted in pursuit of better models,
Megatron-LM and the current state of open-source training software,
Career reflections and paths into AI research,
And other topics.
The biggest takeaway I had from this interview is how Nvidia understands their unique roll as a company that and both build and directly capture the value they get from building open language models, giving them a uniquely sustainable advantage.
Bryan has a beautiful analogy for open models this early in AI’s development, and how they are a process of creating “potential energy” for AI’s future applications.
I hope you enjoy it!
Share
Guest:
Bryan Catanzaro
, VP Applied Deep Learning Research (ADLR), NVIDIA. X:
@ctnzr
,
LinkedIn
,
Google Scholar
.
Listen on
Apple Podcasts
,
Spotify
,
YouTube
, and
where ever you get your podcasts
. For other Interconnects interviews,
go here
.
2019–2022 — Foundational Work
Megatron-LM
(model parallelism framework that has become very popular again recently; alternatives:
DeepSpeed
, PyTorch FSDP).
NeMo Framework
(NVIDIA’s end-to-end LLM stack: training recipes, data pipelines, evaluation, deployment).
Nov 2023 — Nemotron-3 8B:
Enterprise-ready NeMo models
.
Models:
base
,
chat-sft
,
chat-rlhf
,
collection
.
Blog
.
Feb 2024 — Nemotron-4 15B:
Multilingual LLM trained to 8T tokens.
Paper
.
Jun 2024 — Nemotron-4 340B:
Major open release detailing their synthetic data pipeline.
Paper
,
blog
. Models:
Instruct
,
Reward
.
Jul–Sep 2024 — Minitron / Nemotron-Mini:
First of their pruned models, pruned from 15B
.
Minitron-4B
(base model),
Nemotron-Mini-4B-Instruct
.
Paper
,
code
.
Oct 2024 — Llama-3.1-Nemotron-70B:
Strong post-training on Llama 3.1 70B.
Model
,
collection
. Key dataset —
HelpSteer2
,
paper
.
Mar–Jun 2025 — Nemotron-H:
First hybrid Mamba-Transformer models for inference efficiency
.
Paper
,
research page
,
blog
. Models:
8B
,
47B
,
4B-128K
.
May 2025 — Llama-Nemotron:
Efficient reasoning models built ontop of Llama (
still!).
Paper
.
Sep 2025 — Nemotron Nano 2:
9B hybrid for reasoning, continuing to improve in performance
.
12B base on 20T tokens (FP8 training) pruned to 9B for post-training.
Report
,
V2 collection
.
Nov 2025 — Nemotron Nano V2 VL:
12B VLM
.
Report
.
Dec 2025 — Nemotron 3:
Nano/Super/Ultra family, hybrid MoE, up to 1M context. Super/Ultra H1 2026.
Nano: 25T tokens, 31.6B total / ~3.2B active, releases recipes + code + datasets.
Papers:
White Paper
,
Technical Report
. Models:
Nano-30B-BF16
,
Base
,
FP8
.
NVIDIA began releasing substantially more data in 2025, including pretraining datasets — making them one of few organizations releasing high-quality pretraining data at scale (which comes with non-negligible legal risk).
Collection
—
CC-v2
,
CC-v2.1
,
CC-Code-v1
,
Code-v2
,
Specialized-v1
,
CC-Math-v1
. Math paper:
arXiv:2508.15096
.
Core post-training dumps (SFT/RL blends):
2025 reasoning/code SFT corpora:
NeMo Gym RLVR datasets:
Collection
Nemotron v3 post-training (Dec 2025):
Collection
HelpSteer (human feedback/preference):
And others, not linked here.
00:00:00 Intro & Why NVIDIA Releases Open Models
00:05:17 Nemotron’s two jobs: systems R&D + ecosystem support
00:15:23 Releasing datasets, not just models
00:22:25 Organizing 500+ people with “invitation, not control”
0:37:29 Scaling Nemotron & The Evolution of Megatron
00:48:26 Career Reflections: From SVMs to DLSS
00:54:12 Lessons from the Baidu Silicon Valley AI Lab
00:57:25 Building an Applied Research Lab with Jensen Huang
01:00:44 Advice for Researchers & Predictions for 2026
00:00:06 Nathan Lambert:
Okay. Hey, Bryan. I’m very excited to talk about Nemotron. I think low-key, one of the biggest evolving stories in twenty-five of open models, outside the obvious things in China that everybody talks about, that gets a ton of attention. So th- thanks for coming on the pod.
00:00:22 Bryan Catanzaro:
Oh, yeah, it’s my honor.
00:00:23 Nathan Lambert:
So I wanted to start, and some of these questions are honestly fulfilling my curiosity as a fan. As like, why does NVIDIA, at a basic level, release Nemotron as open models?
00:00:39 Bryan Catanzaro:
Well, we know that it’s an opportunity for NVIDIA to grow our market whenever AI grows, and we know that having access to open AI models is really important for a lot of developers and researchers that are trying to push AI forward. you know, we were really excited by efforts from some other companies around the industry to push openly developed AI forward. You know, Meta did some amazing work, obviously, with Llama and you know OpenAI released GPT OSS, which was exciting. And the Allen Institute, of course, has been, you know, really leading the charge for research, open research and, you know, also things like the Marin Project and OpenAthena. You know, like there’s, there’s a bunch of things that we’re always excited to see develop.
And, you know, as we think about where AI is gonna go, you know, NVIDIA believes that AI is a form of infrastructure. it’s.. AI is a very useful technology when it’s applied, but on its own you know, it’s kind of a foundation and infrastructure. We think that technology generally works better when there’s openness to the infrastructure so that people can build things in different ways. You know, you think about the way that the internet transformed every aspect of the world economy is pretty profound, and we’re not done yet.
But the way that, for example, retail uses the internet is different from the way that healthcare uses the internet. And the fact that you know, different sectors of the economy were able to figure out how to incorporate the internet into the beating heart of their businesses in different ways was possible because the internet was built on open technologies that, you know, allowed people to try different things. And we think AI is gonna evolve in a similar way, that organizations across every sector of the world economy are gonna find new and surprising and fun, and important things to do with AI, and they’ll be able to do that better if they have the ability to customize AI and incorporate it directly into the work that they do. and so -- and by the way, this is not to detract from any of the you know, more closed approaches to AI, you know, the APIs that we see from a number of leading labs that, you know, are just extraordinary and have amazing capabilities. We’re excited about those, too.
You know, NVIDIA loves to support AI in all of its manifestations, but we feel like right now the sort of closed approaches to deploying AI are doing pretty well but we, you know, could use some more energy in the openly developed AI ecosystem, and so that’s why we’ve been putting more effort into it this past year.
00:03:42 Nathan Lambert:
Yeah. So I’m definitely gonna dig into this a lot ‘cause I have seen this. We’re sitting here recording in January twenty-six, which is in the midst of the rollout of these Nemotron three models. There’s the-- I think the Nano has released in the fall, which was probably one of the biggest splashes the org has made, and everybody’s eagerly awaiting these super and ultra-larger variants.
And it’s like how far are you, how far are you willing to push this Nemotron platform? Like, is it just depending on the users and the uptake and the ecosystem? Like, like, what is the-- is there a North Star in this? Or you hear a lot of.. if you listen to a lot of other open labs, they’re like: “We want to build open AGI,” which is like, I don’t necessarily think grounded, but there’s like a very unifying vision.
Is there something that you try to set the tone for it that goes through the organization? I mean, AI too, it’s like-
00:04:31 Bryan Catanzaro:
You know, my North-
00:04:32 Nathan Lambert:
.. academics is so-
00:04:34 Bryan Catanzaro:
For Nemotron.
00:04:36 Nathan Lambert:
Okay, go ahead.
00:04:37 Bryan Catanzaro:
Oh, sorry. Go ahead.
00:04:39 Nathan Lambert:
I was just, like, gonna compare to, like, AI too, where we can have such a-- like, we have a very specific vision, being so open that it’s like, I think, like, research is so needed, and there’s so little recipes to build on, like, with really credible research. So there’s, like, a research infrastructure, and then when you have something like Llama, it was, like, built on Zuckerberg’s vision, and he changed his mind, which I actually thought his vision was ex- was excellent, the way he articulated the need for open models, and it kind of faded. So it’s like, is there a way to set a vision for an org that, like, permeates every- everyone and is really compelling and exciting?
00:05:17 Bryan Catanzaro:
Right. Well, we built Nemotron for two main reasons. The first is because we need to for our main product line. So what I mean by that?
Well, accelerated computing, what NVIDIA does, we build fast computers, right? But the point of building fast computers is to help people do new things. and actually every fast computer is also a slow computer. you know, the observation that it would be nice if computers were faster and could do more things isn’t new. that’s been around since the beginning of computing. So what makes accelerated computing different from standard computing is that we’re prioritizing, you know, we’re focusing, we’re deciding we’re gonna accelerate this workload. This other workload, which is like ninety-nine percent of all of the workloads, we’re gonna let somebody else do that, right?
So, like, you do not buy NVIDIA systems to do any general purpose computation. You buy them for a purpose, right? Which is these days, all about AI. But when you think about the workload, the compute workloads involved in AI there’s a, there’s a lot of diversity and there’s a lot of really important -.. parameters, hyperparameters, or algorithmic approaches that all have enormous imp- impacts on the systems that we need to build for AI.
So things like numeric precision MoE architecture, which of course, influence net-- it influences network design. you know, we’re dreaming about sparsity. We, you know, we’ve had, we’ve had sparse neural network acceleration in the GPU since Ampere. I don’t think that it’s being used enough. you know, so how do we, how do we figure out how to use that? These, these sorts of things have an enormous impact on the future of NVIDIA’s main product line, and we have to understand the answers to those questions deeply ourselves in order to know what we’re going to build.
We can’t just go to our customers and do a survey and say, “Hey “ you know, Meta, for example, since we were just talking about them, “what would you like to see in a future product line from NVIDIA?” Of course, Meta’s always trying to help us as much as they can, but there’s limits to what they can tell us because, you know a lot of the information that influences the design of these systems, it’s very expensive to derive, and so therefore, it’s, it’s very closely held. And so we need to be able to understand these questions very deeply in order to understand what kind of systems to build, in order to understand what we’re accelerating in AI and what we’re not gonna worry about. and so that’s kind of the first job for Nemotron models, is to make it possible for NVIDIA to continue to exist as a company. And I think it’s important that the community knows that because that’s the reason why NVIDIA is making the investments in Nemotron, is because we believe it’s essential for the future of our company. and so this isn’t-- and although as much, as much as it feels good to say, you know, NVIDIA believes in open openly developed AI because you know, we’re so charitable, but actually, that’s not the case. This is actually a business decision-
00:08:34 Nathan Lambert:
It’s smart
00:08:34 Bryan Catanzaro:
.. like, for NVIDIA, our business needs us to know about AI very deeply. And and so, you know, the amount of investment that is justified to carry on NVIDIA’s ongoing business, I think, is large. and so that’s that’s job number one for Nemotron. Now job number two for Nemotron is to support the ecosystem more broadly outside of NVIDIA. and, you know, NVIDIA has a special position in the AI landscape. of all of the big AI companies I think we’re the one that works with the most other companies. We support every company small and large, AI native company to old established enterprise.
We work with hyperscalers, we work with tiny little startups, we work with countries around the world. so we have this unique position and I think also a uni- unique responsibility and al- maybe also a unique opportunity, that whenever AI is able to grow in any sort of direction, in any capability, then you know, that’s an opportunity for us to grow our business. Obviously, it’s not automatic, right? you know, the AI market is diverse, and it’s getting more diverse, and it should be, ‘cause it’s the most important market in the history of humanity. So so we acknowledge that, and at the same time, we know that it’s in our interest to develop the AI ecosystem. The more people that are building, inventing, and deploying AI, the more opportunity that we have as a company.
So that’s job number two for Nemotron.
00:10:17 Nathan Lambert:
Yeah. I really appreciate you saying it so directly ‘cause it’s like we’ve worked.. We- I launched this thing, the Adam Project, last summer, which is trying to get more investment in the US open models, and it’s like the only company that has an obvious business model for open models is something like NVIDIA, where you need to make sure that the open models and the research ecosystem plays nicely on CUDA, because then you’re gonna be able to be one-- You’re so many steps closer to research that’s happening. If not, like, if it like- There’s such an advantage to have research happen mostly on GPUs relative to AMD or anything like this, so.
00:10:49 Bryan Catanzaro:
Well, you know, we are-- we’re, we’re not thinking about how to prevent competition. You know, we welcome competition. There’s lots of competition. There should be more competition in this space, but we are very self-interested in staying engaged with the community.
You know, it’s very important. You know, CUDA not many people remember this because it happened so long ago, but you know, CUDA started out with a lot of outreach from NVIDIA to the academic and industrial community saying, “Hey, we have this new way of doing computing. we’d love to see what you can do with it.” In fact, you know, I started using CUDA in 2006 when I was a grad student at Berkeley because David Kirk, who was the chief scientist of NVIDIA at the time, came over to Berkeley and said, “Hey we just released this new GPU, and it has this new programming model called CUDA. You should give it a try.” And I was-- at the time, I was working on machine learning on FPGAs, and I had been working on this one particular piece of support vector machine training on the FPGA, and I decided to take that little piece and write it in CUDA, and it took me like fifteen minutes, and then I ran it, and it was like two hundred times faster than my single-threaded CPU code, and I was like: “Whoa, that was way easier than what I was doing before. I’m just gonna go do that,” right?
So, like, my own personal involvement with CUDA and NVIDIA came about because of this outreach that NVIDIA conducted right from the beginning of CUDA. you know, of course, that led to a lot of great things for NVIDIA, including AlexNet, which was another academic project, you know, where Alex Krizhevsky and Ilya Sutskever were thinking about: “How do we train larger neural networks on more data? we’re gonna go write a bunch of GPU code that uses the GPU in a, in a kinda new and clever way, so that we can train a better image classification model.” And, you know, that had such astonishing results, it kicked off the deep learning era for the whole community. and again, not something that-.. could have been done top-down. That was a, that was a very much a result of NVIDIA supporting open development and re- research in parallel computing and artificial intelligence. And so we remember that, and we’re thinking about in twenty-six, what does it look like to help, you know, the Alex Krizhevsky of the future, who’s, who’s a grad student in a lab somewhere, invent the next technology that changes the world? It seems really difficult to do that without something like Nemotron or, or the other openly developed AI projects out there. yeah, I also wanna say in regards to this Nemotron is not trying to be the only project out there.
We’re part of the community. We love other people doing great work in openly developed AI. We learn from things that other people do and you know, so we’re, we’re trying to support the community because it’s in our interest, but we you know, we’re very happy to see other people contributing as well.
00:13:57 Nathan Lambert:
Yeah, I mean, I can transition into something I wanted to ask about is like, I see multiple ways, twenty-five Nemotron mat-- in, I don’t wanna use the word maturing ‘cause I wanna ask you about how it feels in the org, but just like the output reached levels that were more noticed by the community and people building with models. And there’s a lot of ways that can happen, but one of them is like, in my niche community, I’ve been using Nemotron datasets a lot. Like we-- when we redo our post-training recipe, one of the only people we look at is like, okay, NVIDIA, Nemotron has released a lot of high-quality, openly licensed post-training data. this year, you also started releasing some pre-training data, which among AI2 got a lot of notice. Like, what is that? is that like a distinct shift within Nemotron?
Is that something that you’ve wanted to do for a while and finally just did? But it’s ‘cause it’s like-- it is just like a zero to one moment where releasing pre-training data comes with legal risk for any company, but so few people do it, where on my side of the world, it’s like pretty easy to normally say what the best pre-training dataset is, and it had, for a long time, oscillated between like Hugging Face, AI2, DCLM, and there was like literally only two or three options. So in terms of fundamental research, like I think that’s a big step from an org to support the community and take on some risk. So if you have any story you can tell and or just say like, I appreciate it, that’s, that’s all.. that’s all I got.
00:15:23 Bryan Catanzaro:
Well, yeah. I mean, so I think it’d be great if more people could understand that Nemotron is not just a model, right? Like, what we’re trying to do with Nemotron is to support openly developed AI, because, again, that’s our big opportunity, right? Now, there’s a lot of organizations that are incentivized to build a model, and the model is maybe the thing that runs their business, right?
But at NVIDIA, the model is not the thing that runs our business, it’s the systems. So when we’re thinking about how do we support the ecosystem, it’s clear to us that the ecosystem needs more than just a model. There’s a lot of models out there already, you know? And of course, we want Nemotron to be awesome, but you know, if Nemotron can convince other people to work on AI because of a dataset or a technique, you know, we’re, we’re trying to be very open with all of the things we learn, you know, including..
I mean, we do a lot of expensive experiments in order to figure out how to do blending for our datasets or to figure out, you know, optimize our settings and, you know, these sorts of things. we’re very happy for other people to pick that up and run with it if it’s useful to them, you know. And so that makes Nemotron a different kind of AI effort. Of course, there is a model component, and that’s a tangible thing, and it’s, it’s easy to focus on that, but we see Nemotron as you know, an effort that includes models, but also includes datasets, techniques, all of all of the research that goes into Nemotron. And again we’re a unique kind of AI organization because of the way that we work with AI companies around the industry and because of the way that our business works, we can afford to be more open with some of these things than maybe some other organizations could be.
Now to your question about, like, does it take some courage in order to be open? Yeah, absolutely it does. and you know, I think there’s been-- one of the things that’s happened in twenty-five is that there’s been an evolving understanding within NVIDIA about the benefits of openness, and that has really enabled the company to make some investments that perhaps it was a little gun-shy to make in the past. And so that’s really encouraging for me. it’s something that I’ve you know, advocated for a while, and so it’s, it’s great to see the company kind of lining up behind it. I also, you know, to your point about like twenty-five being a, a year where Nemotron really made some strides, I want to say thank you for noticing that, and then maybe tell you a little bit about how that happened, because I think it’s instructive for me about how I think the work is gonna go forward in the future.
So you know, NVIDIA is a very decentralized company with a lot of volunteers. You know, everybody that works at NVIDIA is a volunteer. And what do I mean by that? Well, I mean, look, the industry is moving quick.
You know, people can always move from one job to the next. So the way that we think about the work that we do is like, it’s very decentralized, it’s very much let smart people figure out what they should be doing and then kind of self-organize. Now one of the challenges of self-organization in a field that’s moving quickly is that sometimes a whole bunch of people decide to-.. do similar kind of overlapping things but aren’t really coordinated. and that’s okay at the beginning because, you know in a place like NVIDIA, it’s just great to have some energy. It, it took us a while, I think, as a company to figure out that Nemotron was better together.
That rather than having, like, this group has a, has a model and that group has a dataset, and like, you know, then we end up publishing papers that kind of you know don’t really acknowledge each other and aren’t really coordinated. And then, of course along with that, we need to have k times the GPUs, where k is the number of independent efforts. we realized that, you know building AI, you really do need to figure out how to collaborate. the AI efforts that are built from teams of people focused on the overall effort succeeding rather than their own particular piece of the project succeeding, those are the ones that, you know, really change the world. And, you know, of course, NVIDIA works that way for the systems that we build, right? So, like, the people working on the memory controller on the GPU know that they also have to work with the people working on the SM that does the math, right?
Like, you can’t, you can’t make a GPU where it’s just like, “Well, we’ve got an awesome memory controller,” if the math doesn’t work, right? It all has to, has to kinda work together. And so that coordination, I think in the field of AI, it took us a little bit longer to do maybe than you could imagine that it could have. and I think that slowed the progress for Nemotron. so I give a lot of credit to the Nemotron team for realizing over the past, I don’t know, year and a half or so, that it was really time to join up and build one thing and make it awesome, and deeply understand that the success of the Nemotron project was more important than the success of any individual piece of that project. And the reason why I’m telling you all of this is because I think that’s actually true more broadly than just inside NVIDIA, and I think it’s, it’s difficult. you know, researchers like those of us with PhDs, for example, we are taught how to be independent, you know, and how to, how to build up our Google Scholar profile, and there’s, like, an incentive to go ahead and focus on that.
And a lot of successful academics and people researchers you know, they manage to push that pretty far and get some pretty amazing results. But, you know, I do believe that in 2020- in the 2020s you know, that the best research is done as part of a larger team. so how do we figure out how to work together? You know, how do we figure out how to put the success of the team first? That is a thing that is challenging to do but if we can achieve it, I think yield significant results.
And, you know, to the extent that we made progress in that part of the organization, I think we also saw progress in the technology. and that’s.. That gives me great hope for 2026 for Nemotron because the way the team is working together, I think is you know, pretty extraordinary. There’s just an enormous number of brilliant people that have decided that they’re gonna volunteer to make Nemotron awesome, and we’re, we’re starting to see some pretty great things come together.
00:22:25 Nathan Lambert:
I agree with everything you said. Do you have any advice for making the orgs come together? I think we’ve seen big-- Wait, I’ve seen two class-- there’s two classes of AI companies right now. One is startup, does everything, and you have a model in six months, but you’re building from zero, and you have-- you p-- everybody agrees when they start that they do this. And then you have Google’s famous long-winded reorgs, which they actually eventually got right. Like, they got it very right with what’s going on with Gemini and Google DeepMind-.. right now. And it’s like, do you have any advice on doing this? I think, like, I’m, AI too, also advocating for this, but it’s very hard. I think personally-
00:22:58 Bryan Catanzaro:
It’s-
00:22:58 Nathan Lambert:
.. it’s like, I mean, I’m, I’m a special case ‘cause I’m also visible, where it’s e-- very easy for me to turn internet activity into, like, reputation points because of algorithms and size. But it’s very hard to do bottom-up technical work and get all of this and get all the culture alignment. So do you have any advice on actually, like, what works in this domain?
00:23:20 Bryan Catanzaro:
You know what’s worked for us is invitation and not control. so you know, one way that, like, for a while I kinda wanted to try to implement was, like, nobody gets to publish any papers in AI unless they’re clearly part of Nemotron. So this is kind of a top-down, like, we’re gonna make you do it, right? I came to the realization that which we never implemented this, by the way, but I came to realization that this was a bad idea because it would just breed resentment, and, you know, NVIDIA is a company of volunteers. Everybody here is a volunteer.
So what we need to do is create the conditions by which it makes sense for people to volunteer to be part of Nemotron. And so the way that we went about doing that first of all it involved like, some top-level agreements between me and some of the other leaders of Nemotron, for example, John Cohen and Kerry Briski. I work very closely with the two of them. And you know, that hadn’t always been the case.
Like, we kind of had all come to this place independently. but we realized, like, Nemotron, better together, all three of us, and then we started telling our teams that: “You know, we really think Nemotron is gonna be better together.” so that top-down alignment, I think was really helpful. We-- again, we weren’t telling people exactly what to do, but we were just sending a con constant message like, you know, “Nemotron’s better together.” And then we built some structures that facilitated collaboration. So in the past decisions in the Nemotron project tended to be made in kind of a an opaque way. and the reason for that is just, you know-.. it’s hard to tell everybody about the middle of the sausage-making process. You know, it’s, like, messy and dif- difficult, and so, like, you know, it’s natural.
Like, researchers, we’re used to doing this, right? It’s a fait accompli. Like, “Here’s my ICML paper,” and like, you know, the fact that you spent, like, two years failing at that task before you finally succeeded, and then you tied a bow around it and gave it to the ICML committee, you don’t really talk about that, right? And so it’s difficult for researchers to, to be open about the middle of the process of research.
There’s a lot of failure, and it’s hard for people to feel like they’re, they’re not looking amazing. But what we, what we decided to do is we structured the project with.. There’s about twenty different areas for the project. Each of them has a clear leader, what we call a pilot in command.
Their job is to-- the job of the pilot in command is to land the airplane. You know, you just want the airplane to land, okay? So somebody, if you’re landing an airplane, there might be multiple pilots on board, but only one of them is gonna land the airplane at any time, right? Because it would be chaos if two of them tried to land at the same time, people would die.
So so this is not a committee structure; it is a delineated responsibility structure. And then the purpose of that pilot in command for each of these sections is to gather together all the best ideas, help the group of people that are interested in working on that space to come up with data-driven answers to what we should do, what technical decisions we should make, and then document that, you know, in a, in a way that other people can review. and you know, the thing that’s been really great about that is that it is inviting to people because when they see, like, okay, here’s the group of volunteers that are working on this area of Nemotron and then they want to contribute, it’s much clearer about how they could go about doing that, and it’s also clearer what the group needs because you know, these meetings are being held in the open. and we have-- we actually have a website where all of the ideas are submitted. they each get, like, a unique identifier, and then they get engaged with, you know, the PIC is trying to understand what the implications are, what kinds of experiments need to be run in order to prove or disprove the idea? how do we do what I call integration studies? You know, I, integration studies are so key for bringing researchers together, and they’re so opposite of what we are taught when we’re learning how to do ablations as a graduate student. You know, rather than, like, isolating the particular contribution of one idea, integration studies are about putting a hundred ideas together and seeing if they’re better than what we had before. so this kind of thing, doing that in a structured way and in a, in an open way internally has then made it possible for more people to volunteer, and that has then generally raised the rigor of the experiments and also the I think the outcome of the work.
00:28:15 Nathan Lambert:
Yeah, this is great. I think that over the last few years, there’s been more consensus on things that work for research. And I think the- we also do integration tests very regularly of like, is this feature gonna land for the model? And that’s kind of a..
It’s a good- it’s a nice mirror to ablations, where we know research is changing so much. There’s a lot of turmoil in the academic research community, and it’s nice to have things that are tangible as ways that are a little bit different when you’re doing these large-scale projects. So people that underst- like, you still need to do ablations. But then it needs to survive, like, an additional test in order to land into the model.
So it’s like an additional type of work that needs to be done, and I just like to have words to describe what is actually happening. I think on the Nemotron-3 Nano front, I do a lot of analysis on just looking at basic adoption metrics and Nemotron we created this, what we called like a relative adoption metric, which is essentially looking at downloads over time for models, because it’s easy to know which models have a ton of downloads that are released a while ago. But to, like, look at the trajectory of downloads changing over time, this is a lot-- this is a mouthful. It’s kind of an aside, but, like, Nemotron Nano 3 was in the thirty B size range, like, on track to be one of the top ten models downloaded of all time.
The point that I bring this up, other than to just flatter you, is like, do you think last mile adoption takes a substantial amount of work other than making, like, a very functional model? Or does adoption-- like, do you need to, like, change the recipe that you’re making and put a lot of focus and evaluation and, like, change this over time so that you actually get people to really use the model, rather than, like, “Oh, the benchmarks are good,” look at NVIDIA flying high?
00:30:03 Bryan Catanzaro:
Right. Yeah, I mean, wow, it has taken the whole company coming together in order to make Nano V3 have more of an impact than the models that we released before. and there’s so many different aspects to that. obviously, there’s a lot of technical aspects which frankly, I think we have more work to do. So, like you know, making sure that on day zero, when we release something, that the quantizations, all the quantizations, the best quantizations are out there, that the speed on all of the important inference frameworks is out there, that it runs on all of the edge devices that we care about fla- flawlessly, that the install experience is great. You know, this kind of work is extraordinarily important because you know, it’s a crowded world.
There’s so many different things that people could choose to work with, and any amount of friction that gets in the way of people even evaluating something that you do is gonna blunt the results, no matter how good that technology is.. I don’t think that we’re amazing at this yet, so this is something that I anticipate we’re gonna see a lot more investment in as the, you know more people at NVIDIA from all over the company, from marketing, from developer relations, from software engineering, you know as they-- as we all come together in support of this effort. so yeah, so it does, it does take an enormous amount of work. and then, you know, something that I’m particularly interested in is you know, how do we work engage-- i-in a new way, sort of engage with the community to make future Nemotron models even stronger? You know if the only things that we were to optimize for with a Nemotron model would be kind of academic benchmarks that are, you know, highly cited it’s likely the case that the model wouldn’t be general enough to really be useful. And so what we’re trying to build is a technology that other people can extend and deploy, and that means we need to have, like, other ways of understanding the strength of a model besides you know, a handful of academic benchmarks.
I think we have a lot of room to grow here. I’m hoping over time that we develop the muscle of being able to engage with the community and learn from them. Like, you know, okay, this particular thing that I tried to do with Nemotron, it didn’t work. It did this other thing that, you know, I wasn’t expecting, it was wrong. well, that can become feedback that then is used to make the next version better.
I think we’ve got a lot of work to do in that regard.
00:33:10 Nathan Lambert:
Do you think there’s any magic to it? I’ve-- I’m blown away by how successful OpenAI’s two open-source models are. Like, yes, they’re obviously the number one name brand in AI, but on the same metric that I see you guys, like, overperforming, like, what I would expect. I’m like, “Wow, great job, NVIDIA.” They’re, like, totally off the charts, like, on track to like, beat Llama’s, like, most downloaded numbers ever with these two GPT OSS models.
And I feel like what they-- like, even on release, they had hiccups where people were pretty negative on it. But for whatever reason, it has just like.. People figured it out, and it just clicked, and then just, like, for a company to say so little about it. Like, we-- Meta put so much effort into Llama being adopted, and you obviously are putting a lot of effort into this.
Like, I’m just like, did OpenAI just crack the code, or is there sometimes a bit of luck?
00:33:59 Bryan Catanzaro:
Well, I don’t think I, I don’t think about OpenAI as a, as a lucky company. I think of them as a visionary company that works incredibly hard and you know, I think their success is well deserved. I love the GPT OSS models. You know definitely they’re an inspiration for us here at Nemotron. and yeah, so I think OpenAI also has, like, some other ways of engaging with the community just because of the large number of people that use their services, and that helps them learn things about what are people trying to do with AI, that then they can address when they’re building models, and you know, obviously, you know, people talk about that as a flywheel. you know, I think that’s really interesting and really important.
NVIDIA is never going to have the same kind of flywheel as OpenAI does. We’re not trying to build a service like ChatGPT. What we’re trying to do is help the ecosystem, you know, be strong and enduring. we think that it’s important for there to be this openly developed AI ecosystem, and also we’re, we’re trying to build our next generation of systems, and so we have our own reasons for doing this. But we’re not ever going to have the same exact user base or flywheel that OpenAI does.
On the other hand, you know, we are able to work with institutions around the world in our own way, that I think offers us different opportunities and hopefully, that helps us make things that are, that are useful, too.
00:35:38 Nathan Lambert:
Yeah, this makes me realize, I’m having a lot of conversations on.. There are many open model efforts, especially even among people that are fully open, and it’s like, how do we better coordinate? So especially at the smaller scale, it’s like AI2 and Hugging Face. So they’re not big teams.
Like, how do we make sure we’re not doing the same data project at the same-- the same exact thing at the same time? And it’s like, I wonder if there’s opportunities for open companies, like LM Arena has historically released a lot of user data to, like, better help us close this kind of what are people using models for flywheel. And but it’s just-- it’s very hard to build cross-organizational model improvement pipelines, is something that I think. I think models become pretty vertical in terms of somebody at NVIDIA getting the feedback and the model making better.
So that’s what would be something I would like to see this year, but I don’t have ideas for doing it well.
00:36:28 Bryan Catanzaro:
Yeah. You know at NVIDIA, we have a tradition of working really closely with, you know, organizations that use our technology. and, you know, we really-- we have, we have teams of engineers that their job is to enable success for our customers. in fact, there’s more people at NVIDIA that care about the success of people outside of NVIDIA than I feel like sometimes there are people that care about the success of things inside NVIDIA. So, like, sometimes I’m like, I’m like: “Hey, could we use a little bit of that e-energy to support Nemotron?” And, and the answer is yes, and NVIDIA is doing that. But I think as Nemotron matures, we’re gonna find that you know, the organizations that work with NVIDIA to make Nemotron awesome for their business, for their use case are gonna have a say in how Nemotron evolves and hopefully, that helps Nemotron address their needs.
00:37:29 Nathan Lambert:
.. Yeah, a basic question: how many people, like, how many employees does it take to build all the different versions of Nemotron? I haven’t brought this up because you also have other great types of models. I think our, like, open model analyst, Florian, is obsessed with the Parakeet model, ‘cause- Much faster at typing and is much faster at speaking than typing.
So there’s a lot of other-- I don’t know-- I don’t have the full list of other NVIDIA models off the top of my head, but you are releasing a lot of varieties of models. So I think it’s a bit of a there’s more context to my original question, which is I think about language models ‘cause I’m a n-- like, I just think of AI’s progress is gonna continue to go very fast, so I focus as that as the engine. So but it’s like, how many people is putting this kind of movement into place?
00:38:16 Bryan Catanzaro:
Yeah. Well, it’s, it’s, it’s hard to know exactly, and as I said, NVIDIA is a company of volunteers. But and also these days, things are changing, right? Like, so the Parakeet team, which is an excellent team, by the way they I would say a year ago wouldn’t have really considered themselves so much part of the core Nemotron effort, but these days they absolutely are. for the obvious reason that, you know, LLMs these days need to be able to consume all sorts of data, right?
Including audio data. And so you know, as the pro-- as the characteristics, the capabilities of Nemotron models expand obviously, the number of people contributing is gonna expand. I’d say right now there’s about five hundred people that are working pretty much full-time on Nemotron technologies in different ways. This is everything from numerics quantization recipes to speech recognition or image understanding or, you know, pre-training, post-training, RL systems inference software. you know, there’s, there’s a, there’s a whole bunch of different dimensions, right?
So I’d say it’s about five hundred people. but also we’re having our Nemotron all-hands meeting this week, and so I took a look to see how many people were invited to that all-hands meeting, and it was about two thousand. so those are people around the company that are interested in working with Nemotron and either expanding its capabilities or helping its adoption. and so I think you know, the number is somewhere in between and it’s hopefully gonna keep growing as, as Nemotron matures.
00:40:07 Nathan Lambert:
Yeah, I mean, that’s one of the greatest attestations to what you’re saying is like, if the interest outside the company-- inside the company is four times as big as the people doing it, you’re gonna, you’re gonna keep scaling up, it seems. People are gonna-.. find ways to help. - One of the other things I’m interested in, I don’t know, like, on the point of five hundred, it’s like, it sounds like a lot of people, but with how many things you have going on, it seems also very few. ‘Cause I’m transitioning to thinking about the long-standing, like, open-source software that you’ve had for NeMo, and I think Megatron, and it’s like they’ve been around for a long time. I think Megatron has gone through many eras. I have a note here.
It’s like these softwares have been going around since, like, twenty nineteen in some form. And it’s, it-
00:40:51 Bryan Catanzaro:
Publicly. We had our first public release in twenty nineteen, but we started earlier.
00:40:56 Nathan Lambert:
And it’s something that I’ve found is that when I started doing lang- language models, so I was a late bloomer, and we’ll transition to some career talk in a few minutes at Hugging Face. Like Megatron had, like, a bad rap of being very hard to use. But now, like three years later, I hear from anyone that’s founding a new language modeling startup, they’re like, “Just use Megatron.” like, do you pick up on things like this? Is it just, like, random-
00:41:22 Bryan Catanzaro:
Well, we-
00:41:22 Nathan Lambert:
.. but it’s like-
00:41:22 Bryan Catanzaro:
We hard on it. You know, we’re trying really hard to make Megatron easier to use. It’s difficult. Megatron is a complicated piece of technology, and, you know, when we originally started Megatron, the point was to show the community that you could make state-of-the-art large transformer language models with NVIDIA.
I don’t know if you recall, but it-- there was some assertions by some other companies back in twenty seventeen when the transformer was invented, that they could only be made without NVIDIA. in fact, there were statements to that effect on bl-- on official blog posts, which I think got redacted later on. But it was important for NVIDIA to show up and say, “We love language models. We love transformers. Let’s see what we could do, you know, if we partitioned the work properly on lots of GPUs with an amazing interconnect, what kinds of models could we train?” And so that’s where the Megatron project started.
You know, I actually came up with the name Megatron. one of my proudest moments, I suppose. I was thinking about it, I was like: This is a really big transformer. What’s the biggest and baddest transformer? Oh, it’s Megatron.
So that’s, you know, where the name came from. but you’ll think about that had nothing to do with usability, right? Like, I wasn’t, I wasn’t thinking about, like, how do we make a platform that’s really easy for other people to use? I was just trying to show the world that, like, NVIDIA systems could be awesome for transformers. You know, that was, that was my goal.
Over the years, you know, it has evolved. We have a lot more people trying to use Megatron. We got a lot of complaints about how hard it was to use, and then we did a lot of work to try to improve the software engineering around Megatron. You know, these days Megatron software engineering is actually shared between about four different teams at NVIDIA. and we have to coordinate that work very closely.
That has also not been easy. There has been times when you know, people wanted to fork Megatron, and then there were times when we, like, had to bring it back together, and it’s like: Look, I know forking things is always tempting, but look, better together. It’s better for all of us to keep working together.. and so I feel like Megatron the-- and especially Megatron Core, which is like a subset of Megatron that’s, like, especially protected, and we try to put more software engineering into that that has gotten dramatically better since we started paying more attention to it as a company. are we done yet? No, there’s a lot, a lot, a lot more work.
00:43:52 Nathan Lambert:
a ba-- a basic question: Is is Megatron or Megatron Core, like, this is what Nemotron is trained on? And also-- And it’s also something that many of the hottest, like, AI startups are training their models on. I would guess that there’s nothing else that does that. So, like, could you summarize why it’s so hard?
00:44:11 Bryan Catanzaro:
Well, you know, there’s a, there’s a lot of other great frameworks out there. Megatron’s not the only one. and you know, we’re happy about that. NVIDIA doesn’t need to control the space. What we, what we do wanna do is make sure that we’re putting our products forward in the best light, you know, and it’s a challenging problem.
We’ve got so many things going on with precision and you know, the networking. Like, those questions, like, the software is so complicated. these days, you know, we’re pre-training our Nemotron-3 Super and Ultra models using FP4 which is a thing that, you know, hasn’t been done publicly anyway and something that, you know, we’re pretty excited about because our GPUs have really awesome FP4 throughput. But obviously, the numerical challenges of, like, trying to train a state-of-the-art language model using four bits is non-trivial. So, like, you know, all of that work has to go into Megatron, into Transformer Engine which is a, another open-source project that Megatron relies on and, you know coordinating all of that making sure that, you know, we can actually deliver the benefits of NVIDIA systems to people that are trying to make state-of-the-art models, that’s really important to us.
And, you know, of the five hundred or so people working on Megatron, like, a pretty good fraction.. or on Nemotron, a pretty good fraction of them are working on these kinds of systems issues, right? Because NVIDIA at its core, is a systems company. and Megatron, you know, Nemotron’s first job really is about systems, you know, and so we, we care, we care deeply about that.
00:45:51 Nathan Lambert:
Yeah. I mean, from my perspective, I was at Hugging Face before AI2, and Hugging Face is, like, the best company at doing public work. But also, and switching to AI2 and focusing on, like, we’re focused on the output artifact the most. Seeing the different type-- Like, it’s such a different type of work, going from you’re trying to build a tool that’s good for training models, to build a tool that’s good for everybody else and whatever heck use case they are.
00:46:13 Bryan Catanzaro:
It’s different.
00:46:13 Nathan Lambert:
So I think-
00:46:13 Bryan Catanzaro:
Yeah. Different work.
00:46:14 Nathan Lambert:
To do both is like.. I’m, I’m happy that AI2’s repos aren’t that popular in terms-
00:46:21 Bryan Catanzaro:
Oh,
00:46:21 Nathan Lambert:
.. of open-source adoption because, like, we can’t handle it. We just can’t. It’s, like, so hard because it’s people-- it’s, like, it ends up being researchers that are supporting it, and we don’t have the ability to scale the organization structure. So I just think, like, that’s a, that’s a very fun turnaround for me to think of all these things happening at once.
00:46:39 Bryan Catanzaro:
Yeah. Well, thanks for noticing we’re putting effort in. I would say Megatron is still not nearly as user-friendly as Hugging Face libraries. Like-.. Hugging Face libraries are legendary, and I admire the work they’ve done to make the community so productive. people, you know, are able to get so much research done thanks to the work that, you know, Hugging Face has put into to their library. So you know, my hat’s off to them as well.
00:47:06 Nathan Lambert:
Yeah. One of my hot takes, you don’t have to reply, is that Hugging Face and NVIDIA have been very good partners.
00:47:10 Bryan Catanzaro:
Oh, absolutely.
00:47:10 Nathan Lambert:
And it’s like bringing that Hugging Face culture to the NVIDIA stuff would be so good. It’s just so hard, so I don’t know how that would work, but-
00:47:17 Bryan Catanzaro:
We’re trying, you know, and you know, it is, it is challenging. NVIDIA is always a company that is gonna prioritize speed like hardware speed, above really anything else, ‘cause that’s, like, who we are. I am always trying to make the case that developer speed is important, too, right? It’s like there’s different ways of thinking about speed. and it is definitely the case that a lot of NVIDIA’s software is so cumbersome to use that you know people can’t get the actual hardware speed as fast as it should be because they just give up.
You know, they just don’t, don’t even figure out how to use that. So I think NVIDIA’s making strides there. I think the, the company is understanding more deeply how important developer experience is, and I hope we continue to push that, so that the benefits of all of the systems technology that NVIDIA works so hard on can be more widely used. but at the same time, you know, there is gonna be a tension between those things. It’s, it’s not gonna go away, and you know, to a certain extent, I think that’s just life on planet Earth.
00:48:26 Nathan Lambert:
It is. I think you’re do- you’re doing a good job, and I’m gonna kind of shift gears in this interview. So I’ve.. In becoming more back in language- in becoming a person that works in language models, I’ve seen your name more and more times.
I was like, “Bryan Catanzaro, like, where have I seen this?” And then I went and did the research of the Berkeley PhD in, like.. It says April of 2021, you gave a Berkeley EECS Colloquium titled “Applications of Deep Learning and Graphics, Conversational AI, and Systems Design.” I’m not even gonna posit that I actually went, but that’s definitely where I remembered the name from in grad school. And we both have backgrounds that aren’t traditionally in AI and end up working in language models. I just wanted to, like-- what have you learned from your path th- through NVIDIA into what, like, people should be thinking about with AI or open models today?
This could be career reflections, like technical reflections. I just think that there’s-- there are actually a lot of people that come from all over the, like, STEM field to work in AI, so giving it-
00:49:29 Bryan Catanzaro:
Sure
00:49:29 Nathan Lambert:
.. space to think about is-
00:49:31 Bryan Catanzaro:
.. useful, even if it’s just like, it was the big problem, and I wanted to go solve it. Well, I think, you know I’ve, I’ve had a lot of opportunity and a lot of luck in my career. I think in hindsight, it seems like an extraordinarily lucky thing that, you know, I did my first internship at NVIDIA in 2008, and I was, like, building machine learning models on the GPU, and I went to NVIDIA, and nobody else was really doing that. And I was like, “Hey, like, we should have more people doing machine learning on the GPU.
I think this could be an opportunity.” And you know, it took a few years for me to make any headway. NVIDIA didn’t really wanna listen to me. I was a brand-new PhD. I was in the research organization, which is very independent, but, you know, sometimes struggles to change the way that the, you know, the bigger company thinks about things.
And and yet, I just had this conviction, you know, I just was following my heart about what I think is gonna be important, what do I think could really change the world? And that has been, I think, the thread that has taken me through my whole career, is that I’m constantly trying to refine my beliefs about what matters and then hold to them. And that.. I don’t know how helpful it is to say that, but I feel like sometimes people you know, tend to follow the, whatever the thing is that people are talking about on Twitter.
And like I’ve- I’ve done a lot of unpopular things during my career because I believed in them, you know? I remember I published my first paper in 2008 on, at ICML, on training support vector machines on the GPU, and I actually had somebody at the conference, it was in Helsinki at dinner, you know, we were all telling each other what we’re doing, and, and I was like: Yeah, I wanna help people train bigger models on bigger data sets with GPUs. And, and I had you know, a couple of people just say, “Well, why are you here at ICML? That just doesn’t really feel like a good thing for us.” And in 2008, ICML was momly- mainly about new mathematical frameworks for thinking about data, and you know, maybe if you trained a model at all, you would train one on your laptop.
You know, that was the state of machine learning in 2008. So for somebody to come in and say, “I think I want to focus on, like, parallel computing, new kinds of hardware for machine learning, programming frameworks for machine learning, so that, you know, we- more people can try inventing new models on complicated machines with a lot more compute throughput on bigger data sets,” that was like a, an unpopular thing. At least it felt very unpopular. I felt very marginalized at the time by the community.
But I believed in it, you know? I just felt like, look, technology.. Like I have this sense of, like, where do I think technology is going? I knew that traditional computing was running out of steam.
You know, I had, I had done a few internships at Intel, and I was trying to help Intel make processors that ran at, like, ten gigahertz back in 2001, and, you know, it was, like, clear that th- they were running into a wall. And I was thinking: Okay, so if the compute hardware is gonna have to be different, it’s gonna be more restricted. It’s not gonna be able to be so general-purpose in order to get speed. What kinds of applications are gonna have, like, an infinite need for more computing?
And I thought, well, machine learning and AI, that could really change the world if it ever actually worked. But, you know, but, you know, back then it, back then, it kinda worked inside of Google. outside of Google, it kind of didn’t work. and so I had kinda these signals, like it was possible, but it was hard. It was a little weird. It was a little niche.
I was a little bit caught in between different fields, like the systems people didn’t think I was systems enough, and the machine learning people didn’t think I was machine learning enough. But, but I believed in what I was doing, and I found a way to keep following that belief. And, you know, ultimately it was very rewarding when all of a sudden NVIDIA decided, “Hey deep learning is changing the world. What do we know about deep learning?” And then it was like: Oh, well, Bryan’s been doing that for several years, and he’s written some libraries that we could turn into a product.
Let’s go do that. And, you know, so that all happened really quickly after many years of nothing happening, you know? And that was really obviously an amazing opportunity for me. you know, an- another thing that was important to me, I left NVIDIA in 2014 to go work at the Silicon Valley AI Lab at Baidu with a group of really talented people, including Andrew Ng and Dario Amodei and Awni Hannun and Adam Coates, and you know, this was a, a really once-in-a-lifetime opportunity, I think for me, to learn some things that would have been hard for me to learn on my own. you know, I felt at the time at NVIDIA that although I had this great opportunity to help NVIDIA become an AI company, and I was doing that, and I was succeeding at that back in 2013 2014, I also felt like I really wanted to learn from a broader community of people applying machine learning and AI to solve really important business problems. And so going to work at Baidu really gave me that chance. and I was there for a couple of years, learned a ton. very grateful to the team there especially to Andrew Ng, who, who encouraged me to, to join with him on that. and then, you know, I ran into limits of what I could do in California, working for a Chinese company.
I was thinking about, you know, what should I do next? And Jensen asked me to come back and build an applied research lab at NVIDIA in 2016. and -.. I wasn’t sure, like, if that was a good idea. I thought NVIDIA’s already grown so much, you know.
The, the years from twenty fourteen to twenty sixteen, NVIDIA actually grew a lot. these days you look back at it, and you’re like: It was still really tiny. But, but back then, I was like: I don’t know, maybe NVIDIA’s already tapped out. I don’t know if you recall, in twenty sixteen, there was already, like, ten different companies making GPU competitors, right? The TPU had already been out for a while and you know, it, it wasn’t clear that NVIDIA was gonna become as large as it, as it has.
But I believed in the opportunity. I believed in the people. you know, one of the things I loved about NVIDIA was that it’s a very stable organization. So Jensen, he’s been running it since he founded it in nineteen ninety-three. my boss, Jonah Alben, who’s an absolutely extraordinary person has been here for you know quite a, quite a long time, almost since the very beginning of NVIDIA. And these people a lot of the leadership at NVIDIA they love the work.
Their heart is in the work. Jensen and Jonah and many other leaders at NVIDIA, they don’t need to be doing this, right? They, they have earned the right to go sit on a beach and drink mai tais all day, but their heart is in the work, and they work incredibly hard. you know, the.. I feel like if there was an Olympics for email, you know Jensen would get the gold medal.
You know, like it’s, it’s unfathomable to me, like, how much information he’s able to process. and it’s a skill that he’s built up over a long time running this company, but it’s also a reflection of his commitment to the work. And I felt like working at a place where we’ve got this very stable organization that loves the work, that really wants to change the world. You know, why does, why does Jensen get up in the morning? Well, it’s-- this is his chance to do something meaningful.
I thought, associating with these people, you know, I could do worse. I could-- I think I could learn from this as well. And so I came to NVIDIA, and back then it was really hard to explain to people why I was trying to build an AI lab inside of NVIDIA. At, at the time, NVIDIA wasn’t doing very much AI, and so I had to kind of develop a vision for that and then explain it to people. that’s ended up being a really good idea for me as well.
You know, the lab, I think, has really helped NVIDIA. you know, Megatron, I think, has really shown the industry, like, how valuable NVIDIA systems can be for language modeling, which is, which is awesome. DLSS, you know I’m continuing to, to push DLSS forward. Very excited about making graphics, you know more efficient with AI. These days, you know, fifteen out of every sixteen pixels a gamer sees are rendered by AI models that, you know, my team developed, and that then makes the GPU ten times more power efficient.
This is a really exciting you know, thing for me to be involved with, something that I’ve, you know, dreamed about for years. So, so that’s the kind of thing that continues to push me forward, is that I have strong beliefs about what I think is possible, where I think technology’s going, and I’m willing to do things that are we- weird and unpopular but, you know, basically following my convictions. I’m very much always thinking about the people I’m working with, the tribe. You know, I think tribes matter enormously. like you know if I..
So, so back when I was a grad student, I was working on programming models for machine learning. I joined the Python tribe. There are other people that were in the Scala tribe, and the people that did their work in the Scala tribe, trying to make programming models for machine learning in, like, two thousand and ten you know, that work, although a lot of it was technically excellent, didn’t matter to the community as much as the people who were in the Python tribe. It ended up.. and, you know, it kind of sucks sometimes that the world is tribal like this, but it’s just the case.
You know, that like the people that you work with, the community that you work with has a big impact on the problems you think about and then the impact that your work has. So I think a lot about the people and the tribes that I’m collaborating with or that I’m part of. and you know, that’s, that’s kind of been the thread that has carried me through my career.
00:59:56 Nathan Lambert:
Yeah. Than- thanks for sharing this full arc. I think you’ve said things that I tell people but in different languages, and the first one, the early days, it seems like there can be space in between fields, where people-- two fields will have their way of describing things, but both of them are probably incomplete, and there can be space there, which is a lot of what I was doing transitioning from novel robots to model-based RL, where I, like, didn’t sit and bear in the actual AI lab, but I started doing AI with my, like, total electrical engineering friends. And then the second thing is, like, I’d wholeheartedly recommend this to people, is, like, choose your work based on the people and people that sincerely are in it for-.. the, what they want to do, and a lot of-
01:00:41 Bryan Catanzaro:
And follow your beliefs. You know, think about it. What do you believe in? And it’s okay to change your mind, you know, but, like, figure out what is it that you believe in.
Ask yourself every day: Do I still believe in that? If I do, what next? You know. If I don’t, well, what do I believe in?
You know, that’s been really important to me. I think too many people end up kind of just following trends. That’s not usually helpful because the trends are too late. So if you wanna, if you wanna change the world, you need to be ahead of the trends, and you need to know, you know, it-- trends-- I don’t think trends in computing are just fashion.
I think there’s truth that drives those trends. Not always, but often. You know, it’s just-- this is, it’s there’s kind of an inevitable force of gravity. It just can be really hard to par- parse out the noise and figure out what is the truth that is gonna push the industry forward, and how can you push that with it.
You know, if you can join with that, you can accomplish great things.
01:01:36 Nathan Lambert:
Yeah, I agree. I think in building language models, it’s like you want to build a model that the community wants in six months. I think if you’re building a model to compete-.. with the models that are already out, you’re not gonna keep up. And I think that it’s like, what is the right thing is building open language models in six months, and like, where do you need to try to steer things is one of the hardest problems that I think about. So I don’t-- if you want to close with any predictions where you see, like, open models, like, if we’re-- if you’re gonna be here at the end of twenty-six, if there’s anything you think will be far more obvious than it is today, or any bets that you want to make, I think it’s kind of a good place to wrap.
01:02:18 Bryan Catanzaro:
Well predictions are always hard, and I don’t feel like I’m very good at making predictions. But I am-- I feel like I am good at identifying what I believe in, and what I believe in right now is that compute remains one of the fundamental challenges behind AI. It has been that way for a very long time and I think it continues to be. I think as we find new ways to apply compute to AI, we discover new forms of scaling laws that help AI become more useful and therefore, it becomes more widespread.
So I’m gonna keep thinking about compute. I continue to believe that the fastest-- that, you know, the way to think about AI is not just in terms of absolute intelligence, but rather intelligence per second. You know, there’s some sort of normalization in there that relates to how fast a model can think, how fast a model can be trained or post-trained. You know, that models that kind of incorporate this compute acceleration characteristic, where they’re thinking about intelligence per unit time, those are gonna end up winning because they end up getting trained on more data, they end up getting post-trained with more cycles, they end up with more iterations during thinking when they’re deployed. and you know, of course, if they happen to fit the hardware really well whatever hardware that is then, you know, that can have a pretty non-trivial effect on the intelligence as well.
So that’s something that I really believe in. I really believe in AI as an infrastructure. You know, there’s, there’s different ways of thinking about AI. I think some people believe AI is more like the singularity, like once AGI has been declared, then the whole world is different forever, and all humans have lost their jobs and, you know, there’s a lot of like-- there’s a lot of things about AI that people believe that I personally don’t believe.
You know, I believe, first of all, that intelligence is very multifaceted that it is not easy to pin down, that as soon as we try to pin down intelligence, we find that there’s very many more forms of intelligence that aren’t covered by that. So, for example, a model that achieves gold medal status on the International Math Olympiad, that’s an extraordinary achievement, but it doesn’t make me have no job, right? Like, I’m actually not solving math problems all day, even though, like, having the ability to solve math problems is clearly very useful. And you know, it’s also the case that intelligence is, you know, is kind of like a potential energy it’s not a kinetic energy, right?
In order to transform intelligence into kinetic energy, it needs to have a platform. It needs to be applied in the proper way. and you know, that is why I believe in open models and open- openly developed and deployed intelligence. I believe every company, every organization, has secrets that only they know. They have special data, they have special ways of thinking about their problems, their customers, their solutions, and they’re gonna know how to apply AI better than anyone else.
And so AI as infrastructure that transforms companies, turbocharges them, allows them to take the things they know and multiply their impact, that’s something that I believe in more than AI as an event, that one day, when it happens, makes everyone obsolete. I don’t.. I just don’t believe in that. you know, I often joke that, like if, for example, the CEO were to retire at some point, and we needed to find a replacement you know, handing out an IQ test or asking, you know, who has the highest SAT score that would not be a very good way of finding a replacement, you know? intelligence is just far too complex for that. And so you know, so this, these beliefs, you know, you can disagree with me about anything that I just said, and I’m not offended by that.
I have a lot of friends that do. but you know, I’m asking myself, well, if I believe that intelligence has these characteristics and that AI is gonna change the world by turbocharging institutions that exist a-and also creating new applications that we haven’t even dreamed of yet rather than replacing all humans, then, you know, how do I go about building that, you know? And so that’s, that’s kind of the direction that I’m on right now.
01:07:00 Nathan Lambert:
Yeah, I love it. I agree, I agree that we’re entering an interesting area where the open models are taking so many different shapes and sizes and have so many different strengths and trade-offs, that there can start to be interesting interplay as an ecosystem, where there’s just so many different things going on. And I think I like your idea of potential energy, and you have to build things that are kind of unclear of what-- It’s like you have to build the energy in a way, and you don’t really know what the goal is, but you have to do.. try to build these good models. So I appreciate it, and-
01:07:30 Bryan Catanzaro:
Yeah, and then let people apply it. Let it-- let them make the kinetic energy happen.
01:07:35 Nathan Lambert:
I agree. Thanks for coming on.
01:07:37 Bryan Catanzaro:
Thanks so much for inviting me. It’s been a great conversation.
