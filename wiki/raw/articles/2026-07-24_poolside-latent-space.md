# Inside the Model Factory — Eiso Kant, Poolside AI
**Source**: https://open.substack.com/pub/swyx/p/poolside
**Date**: 2026-07-24
**Author**: swyx/AINews
**Description**: Poolside's co-CEO on how his small team of top researchers built a model factory capable of training Laguna S - a 118B MOE beating Thinky's ~1T open weights model... and this is just the beginning.
**External Links**: [
  "https://www.latent.space",
  "https://www.latent.space/p/poolside/comments",
  "https://www.latent.space/p/poolside/comments",
  "https://www.latent.space/p/ainews-kimi-k3-28t-a50b-the-largest",
  "https://www.latent.space/p/ainews-thinkys-inkling-975b-a41b",
  "https://youtu.be/QLfZamyMls0",
  "https://poolside.ai/blog/introducing-laguna-s-2-1",
  "https://www.latent.space/i/208082176/we-discuss",
  "https://www.latent.space/i/208082176/eiso-kant",
  "https://www.linkedin.com/in/eisokant",
  "https://poolside.ai",
  "https://www.latent.space/i/208082176/timestamps",
  "https://www.latent.space/i/208082176/transcript",
  "https://www.latent.space/i/208082176/introduction-eiso-kant-poolside-and-open-models",
  "https://www.latent.space/i/208082176/from-karpathys-rnn-post-to-sourced",
  "https://www.latent.space/i/208082176/chatgpt-vindication-and-returning-to-open-source",
  "https://www.latent.space/i/208082176/neo-labs-model-choice-and-the-token-economy",
  "https://www.latent.space/i/208082176/open-weights-vs-open-research",
  "https://www.latent.space/i/208082176/poolsides-global-team-and-american-company-story",
  "https://www.latent.space/i/208082176/an-optimizer-bug-and-the-value-of-building-from-scratch"
]

---

3711×0:00Current time: 0:00 / Total time: -1:54:33-1:54:33Audio playback is not supported on your browser. Please upgrade.Inside the Model Factory — Eiso Kant, Poolside AIPoolside's co-CEO on how his small team of top researchers built a model factory capable of training Laguna S - a 118B MOE beating Thinky's ~1T open weights model... and this is just the beginning.Jul 23, 2026371ShareTranscriptIn recent months, the open vs closed, and US vs China discussions on model ownership and sovereign/local AI have heated up to a fever pitch. So it is very very good news that Poolside AI are finally emerging with new models, like Laguna S 2.1, that are beating Thinking Machines’ recent release nearly 10 times their size.

Poolside’s recent tech report got a lot of praise due to their level of detail, and Vibhu first covered Laguna’s recent technical report on our paper club:

Eiso Kant@eisokantLoving the @latentspacepod breakdown of our Laguna M.1/XS.2 Technical Report! The Latent Space paper club just did a deep dive, and their takeaways perfectly capture what we set out to build with our Model Factory. A few quotes from the video 🧵👇 (1/6)
youtu.be/QLfZamyMls08:34 PM · May 28, 2026 · 11.3K Views1 Reply · 8 Reposts · 47 Likes

From spending $12 million building language models for code before the world cared to creating a Model Factory that can take a model from pre-training to release in eight weeks, Eiso Kant has spent more than a decade betting that code is the path to AGI. In this episode, the Poolside co-founder joins swyx and Vibhu to explain why ChatGPT felt like vindication, why Poolside embraced open weights and open research, and why he would rather live in a world with 100 foundation model companies than five even if Poolside were one of the five.

We go deep on Poolside’s Model Factory: the engineering systems behind 10,000–20,000 experiments per month, streaming data directly into training, reproducible experimentation, low-precision compute, and agents that increasingly write code, launch jobs, evaluate results, and modify the pipelines used to train future models. Eiso also unpacks their recent launch Laguna S, why persistence, verification, and backtracking may matter more than raw intelligence, how much capability remains inside smaller models, why reinforcement learning will move earlier into pre-training, and why next-token prediction is still extracting too little from the web.

Poolside@poolsideaiToday we're releasing Laguna S 2.1, our most capable model to date.

It's a 118B total parameter Mixture-of-Experts model with 8B activated per token, a context window of up to 1M tokens, and thinking and no-thinking modes.

Capable enough to hold its own against models many 5:05 PM · Jul 21, 2026 · 656K Views160 Replies · 320 Reposts · 2.18K LikesWe also discuss model-harness co-design, Poolside’s path from coding agents to AGI, why Eiso thinks MCP and traditional tool calls are “stupid,” the real economics behind frontier-model training, Poolside’s $500 million raise, open-source AI, regulation, NVIDIA and TSMC’s influence, engineering productivity in the agent era, high-agency teams, and hiring at Poolside.

How Andrej Karpathy’s RNN work inspired Eiso to start building language models for code in 2015

Why Eiso spent four years and $12 million pursuing an idea before the market cared

Why ChatGPT felt like vindication and brought Poolside back to open source

Why Eiso would prefer 100 foundation model companies over an oligopoly of five

The difference between releasing open weights and publishing genuinely open research

Why Poolside deliberately built a global research organization outside the Bay Area talent war

Why model building is ultimately 90% engineering

The Model Factory: Poolside’s end-to-end system for rapidly training and improving models

How fewer than 70 researchers run roughly 10,000–20,000 experiments each month

How Poolside moved from six-month model cycles to five- and eight-week launches

Why streaming data directly into training unlocked faster experimentation

How immutable data, versioned code, and reproducibility enable rigorous model research

Why Eiso wants capable researchers to leave their labs and become Poolside’s competitors

Why 95% of model building can be reduced to better data or compute efficiency

Laguna S and why persistence, verification, and backtracking can outperform raw intelligence

Why smaller models may handle far more knowledge work than previously expected

Why reinforcement learning will move earlier into pre-training

Why next-token prediction is still failing to extract enough knowledge from the web

Why distillation and environments have become the AI industry’s favorite “drugs”

Why mid-training is really an early form of curriculum design

Low-precision training, networking bottlenecks, and the next gains in compute efficiency

Laguna S: 118 billion total parameters, 8 billion active, and eight weeks from training to launch

Why model builders can often evaluate a new checkpoint within its first 30 minutes

Model versus harness: where agent capabilities actually come from

Why Poolside sees coding and long-horizon software tasks as a path to AGI

Why Eiso thinks MCP and traditional tool calls are “stupid”

Why future agents will write scripts instead of choosing from dozens of predefined tools

The case for minimal harnesses, containers, and model freedom

Why Poolside is prioritizing vision but does not expect to work on audio soon

Why language may be the most compute-efficient modality for encoding knowledge and reasoning

The real cost of model development and why the final training run is anticlimactic

The story behind the Poolside name and why it represents refusing to lower ambitions

How Poolside raised $500 million while investors still questioned whether AGI was real

Why intelligence could become the world’s most demanded and commoditized resource

When open models may become too capable to release without restrictions

Why unilateral AI safety does not work in a globally competitive environment

How regulation could accidentally lock in an oligopoly of two or three AI companies

NVIDIA, TSMC, and the hardware systems underpinning foundation-model progress

Why reinforcement-learning wall-clock time is one of Poolside’s biggest bottlenecks

Why Poolside trains models from scratch instead of simply distilling larger models

How AI changes the way companies should measure engineering productivity

Why agency may become the most important quality for employees in the AI era

How leaders align high-agency people through shared goals and clear constraints

Hiring across research, post-training, pre-training, architecture, evals, and engineering at Poolside

LinkedIn: https://www.linkedin.com/in/eisokant

X: https://x.com/eisokant

Poolside: https://poolside.ai

00:00:00 Introduction

00:00:54 Karpathy, RNNs, and Building Code Models Before Transformers

00:02:26 The $12M Failure and ChatGPT Vindication

00:03:39 Open Source and the Case for 100 Foundation Model Companies

00:09:22 Open Weights, Open Research, and Poolside’s Global Team

00:16:04 The Model Factory: Why Model Building Is 90% Engineering

00:20:19 Agents, Automated Experiments, and Early Signs of RSI

00:24:04 Streaming Data, Reproducibility, and Scientific Rigor

00:30:35 Creating More Foundation Model Companies

00:36:07 Laguna S: Persistence vs. Raw Intelligence

00:43:01 Reinventing Pre-Training, RL, and Curriculum Design

00:52:33 Low-Precision Training and Squeezing More From Smaller Models

00:58:37 Model Harnesses, Coding Agents, and the Path to AGI

01:09:26 Why MCP and Traditional Tool Calls Are “Stupid”

01:13:04 Vision, Multimodality, and Why Language Still Matters

01:18:15 Scaling Models and the Real Economics of Training

01:20:40 Why Poolside Is Called Poolside and Raising $500M

01:27:37 Open Models, AI Safety, and the Risk of an Oligopoly

01:33:53 NVIDIA, TSMC, and the Reinforcement-Learning Bottleneck

01:41:52 Smaller Models, Distillation, Engineering Productivity, and Hiring

Introduction: Eiso Kant, Poolside, and Open ModelsSwyx [00:00:00]: All right, we’re here in the studio with Eiso Kant from Poolside, together with Vibhu. Welcome.

Eiso Kant [00:00:08]: Thanks. Thanks for having me, guys. Good to be here.

Swyx [00:00:10]: Yeah, fresh on the plane. You texted me, you were like, “Hey, I’m on my way to SF.” I was like, “You’re on a plane right now, right?” Like, hey.

Eiso Kant [00:00:16]: I know. After I texted you, I realized that probably coming in with major jet lag was gonna offer some fun experiences today, but let’s do it.

Swyx [00:00:23]: I mean, I think the thing I would tell guests is that they don’t have to prepare that much because if you’re truly working on this every single day, then even, like, what you hazily remember is going to be new for a lot of the audience that don’t live in your world every day, right? so 10 years ago, you did a talk at Google Slush, talking about the democratization of AI. and, now here you are, like, open sourcing an incredible new model that we’re gonna talk about. But I guess, like, what got you into democratization of AI? Like, it’s not obvious from your LinkedIn or something.

Eiso Kant [00:00:57]: No, it’s not at all. I don’t think it’s obvious how I got in this space. I owe getting into this space to Andrej Karpathy.

Eiso Kant [00:01:05]: In 2015, he wrote an article called “The Unreasonable Effectiveness of Recurrent Neural Nets.”

Swyx [00:01:10]: Neural Nets, yep.

Eiso Kant [00:01:11]: And that article, I read it, and I pivoted my startup at the time overnight to working on RNNs, and later LSTMs and Transformer models to be able to write code. If you go to this article and you scroll down, you can start seeing, like, this was the precursor to what ended up becoming language models. So, at least when he was character-level language models that were starting to predict letters, he has an example out here. There’s a little Paul Graham generator, and you can read it, and the text makes sense, but it doesn’t. and there’s a little-- There’s an example of code a little bit further down. Yeah, so Shakespeare.

Swyx [00:01:47]: Shakespeare.

Swyx [00:01:49]: Cool

Eiso Kant [00:01:49]: And for some reason, I read this, and I went down the rabbit hole of learning everything I could about RNNs and LSTMs, right? This is Transformer paper. And I had built a completely unreasonable belief, that neural nets should be able to generalize to anything and everything, and that language should be able to generalize, to a lot of things that are intelligent and the ability to write code. And so I started building Sourced, which was a fully open source company trying to build, what we used to call machine learning on code, language models on code. And we spent about four or five years on this, till the end of 2019. And that sounds really cool today, but back then, no one cared.

Eiso Kant [00:02:29]: Right? Like, no one cared. We were in the dark. Like, we did things along the way. We tried applying convolutional neural nets to, like, the structure of code. We were. when attention came out, we were applying it to LSTMs, and then the Transformer paper came out. And it - it wasn’t obvious, and what we missed throughout that entire journey, that we were on the right track, but we should have just kept scaling up. And today, to all of us, the scaling laws and scaling up seems like the most obvious thing. But having spent four or five years of my life on working on language models on code, it wasn’t obvious. So I have a lot of respect to folks at Google and OpenAI and others who took that confidence and kept going. we failed ultimately at the time, and it was, like, biggest failure of my career, right? You blew $12 million of investors’ money, which was a lot back then.

Swyx [00:03:18]: Yep.

Eiso Kant [00:03:19]: You spent, still a lot, but, And you spent years with, like, a group of 40 people just obsessing over this problem. And life took a different turn, And it was, and family became a focus, and I kept my heads down and really, didn’t really look at language models for the following two years. big mistake considering Following years are gonna be really interesting. And then ChatGPT came out And it was like a vindication. It’s like people started texting me. I found, like, my old, work decks and these old talks. And throughout that whole journey, we,

Eiso Kant [00:03:56]: We really had a strong point of view at the time that, like, as you’re building more capable intelligence, it should be open and open source.

Eiso Kant [00:04:04]: When we started Poolside, that wasn’t the case at all, and I wanna be very open about it. When we started Poolside, we were like, there was a premise of two things. One is this technology is not gonna stop compounding in capabilities. I think to most people obvious today, but three-plus years ago when we started, most people were still arguing if these were stochastic parrots or not.

Eiso Kant [00:04:23]: And the second was that reinforcement learning was gonna be the biggest driver for LLM capabilities. Today, very obvious. Three years ago, was not an opinion held or direction held at either OpenAI or Google or Anthropic or others. And so people looked down on us a little bit. They were like, “ is this really gonna work?” And so we just started working the problem, and we never really thought about open source again. We just kept our heads down and we built our, like, knowledge, understanding from scratch, right? We didn’t roll out of an existing lab. So we picked up the papers and started writing code and figuring things out.

Eiso Kant [00:04:59]: And it wasn’t until the beginning of this year that me and my founder, Jason, picked up the open source conversation again.

Eiso Kant [00:05:07]: And if you go back to some of the early things on our website, it was very straightforward. It was we wanna get to AGI, we wanna support a world of abundance, and we wanna be the first company that gets there.

Eiso Kant [00:05:20]: But we started talking at the beginning of this year because it became obvious that the world was going in a direction that was starting to like, pick at us a little bit. Like, it didn’t, this didn’t happen overnight. It was, like, a little bit we were seeing this and we’re like, “Okay, The world’s going down a path.” And Throughout this journey, there was something that I used as a, as an analogy or thing. So I said well, if I go back to back in those days, 2015 or 2016, we’re working on this, and I picked up a fi book off the shelf, and I was reading the book about 2035. AGI is achieved, and the story would be over the following, decades. And it would have that first chapter where everyone’s trying to figure things out. You’d get the chapter of ChatGPT coming out And then you would get to the chapter where the world was at a fork in the road, and the one that it picked was one where three or four or a handful of companies were going to create all of intelligence moving forward.

Eiso Kant [00:06:21]: And when I thought about that story, it felt like a dystopian fi book, not a utopian fi book. And the reality is, I’m a utopian fi guy. Like, and so We took a step back and said, “Hey, can we play a role here?” Now it was easy for us to do so because we were not at the frontier.

Eiso Kant [00:06:41]: If we were at the frontier, I don’t think we could have changed our mind. and I don’t mean this like it’s when the moment there’s too much capital involved, too much expectations, you’ve built up things, right? We’re a small team, just improving and improving. And so we knew that we could make that decision now, but it would be a lot harder to make as we got closer and closer to the frontier and caught up to others. And did a lot of soul-searching and a lot of conversations, and said, “No, this makes sense,” Even if there’s big unanswered questions, like how the hell do you build a business model with foundation models about open source? Big open-ended question that we do not fully have the answer to yet, right? At what point do you no longer wanna release open source models because misuse of models has, real potential risks associated with it? how is the government gonna respond to open source? but I think it all just came down to one thing, and I’ll stop the monologue, is the fact that I rather live in a world that has 100 foundation model companies than a world that has five, even if I was one of the five. And the smallest and most meaningful contribution we can make for 100 to exist is to open up our research and open up, like, our weights right now and figure out along the way how we can, like, do more.

Swyx [00:08:01]: Yeah. I think if anything, over the past three years, that has become a bit more true. you are one of a cohort of Neo labs

Eiso Kant [00:08:10]: Yeah

Swyx [00:08:10]: That people are now calling that. And, we’re, we’re doing this on the day that Thinky launched their, new model and you are outperforming them on their, on some benchmarks that they released, right? Like, they just don’t have it yet. so it goes to show that I think, like, this is one of those things where, like, there is room for multiple players, and you are seeing a little bit more of the future. Maybe more like 20, not 100, but, like, you are one of the 20.

Eiso Kant [00:08:36]: I really hope so, right? I think we I’m, I’m excited about their release, and I’m excited about everyone releasing because, like, ultimately, like, choice competition is both gonna drive progress in the right direction. But the fact that like, we create models and while we all, drink out of the same well of data effectively, we do introduce very different behaviors and biases in our models. Some are intended biases, some are completely unintended biases.

Swyx [00:09:03]: Yeah.

Eiso Kant [00:09:03]: And if we shape up in an ecosystem in the world where open models are gonna be a part of the token economy, like, I don’t think there’s any question about it anymore Then we want to be able to live in a world where companies, countries, people can choose and say, “Hey, I am most aligned and I trust most this provider for these things.”

Swyx [00:09:25]: Yeah.

Vibhu [00:09:26]: I think more than just one of the 20 Neo labs, up until recently, most of open source innovation was coming from the Chinese labs, right? So there’s the DeepSeek of the West. Is it today? Okay, maybe it’s thinking machines reflection, but there aren’t many, right? So, one of the things you guys started in France, Europe, but very much now you’re taking that American standpoint and more than just that, the point is the Chinese models that we see, they’re not super open research. the work you put out is, I think, some of the best. So every few months you get not only frontier models, but also here’s a breakdown blog, paper, technical report of here’s everything for state of the art to build, frontier intelligence and you’re filling that gap too, right? So not just only open weight, not just Western, but also pretty open research.

Eiso Kant [00:10:20]: No, I appreciate it. Look, I think it’s, I think it’s the most meaningful contribution, right? Weights are a binary. Let’s call them what they are. Yes, we can modify them, we can change them, but, like, giving someone the weights does not allow them ultimately to recreate what you’re doing, right? And so now there’s challenges around releasing data sets, challenges around like releasing certain things, but being able to share your research, like, right, how do we do it? What are the lessons we learned that we spent, tens of thousands of experiments of compute on? I think very much so. One correction though, Vibhu, and I say this because it’s been haunting us for quite a few years. We from day zero were an American company.

Swyx [00:10:55]: Yeah. They moved

Swyx [00:10:56]: To France.

Eiso Kant [00:10:56]: So the story once and for all is very. We start as an American company. We have always been an American company, and early on we made a very conscious decision. We said, “We’re not gonna hire any researchers in the Bay Area. We’re gonna look for talent everywhere else in the world.” and that is everything from Middle Americas, Seattle to, Serbia, and to Taiwan and Singapore and other places. And it was because we took a view that this was gonna become a talent war for this, and I think it has over the years now. Three years ago, that wasn’t fully obvious yet. I think today it very much is. And we also realized that, like, some of the world’s most capable people with, like, the most interesting, innovative ideas were not just gonna be here. And so it led us to create like a fully remote company. and we ended up opening an office in Paris and London and different places and we have a lot of the team in the US and a lot of team outside. But we always took this view of like, we’re an American company, but if we want the best of the best to work with us, we need to take a global view. Now we do also have people here in Silicon Valley, like the company’s grown and others, but I think one of the things that, it slowed us down at the beginning, but it has sped us up now, and it’s why you’re seeing like the progress, I think, on our models and the cadence at which we release, is because we didn’t roll out of an existing lab. Right? we didn’t, we didn’t have a lot of the information that’s freely flowing around here at the time. We just took this point of view as like, “Okay, well, let’s just work the problem. Let’s just go and, like, read the few papers that are out there, and let’s just figure this stuff out.” And we made some hilarious mistakes in model training because of that over the years

Eiso Kant [00:12:35]: Like especially in the first 12 months. there’s a few that I think still haunt me and scare me. We can talk about them later. but it created a, like, a resiliency and persistency in the team, right? with extremely few people have left us over the years, that, like, told us, “Okay, we can do this.” When we first wrote our first training code base completely from scratch, it wasn’t a fork of any open source. It was just like, “Okay, let’s build it from scratch.” I remember we had this one moment where we spent three weeks working out an optimizer bug. Like, it was like training just couldn’t get stable. We, like, obsessed over it, and we thought, like, maybe we were wrong. Maybe we should have just forked this repo, or we should have. But then when we solved it, I still remember at the time we were like five people in the company. when we solved it, we were like, “Oh, we can do things,” like if we’re just willing to work hard. and I think that culture with a very strong engineering bias has helped us, like, get to where we were. And so there’s this notion of open source and talent and these things. I think we, We just took different decisions from a different starting point. and I think we are lucky. I do want to definitely call it lucky. And there was a lot of hard work at the team that now, like, that’s starting to show up in results.

Swyx [00:13:52]: Just ‘cause we probably won’t revisit this again, but, and this is a fun recruiting challenge if someone knows the answer. What was the bug? And then we won’t tell the solution, but we’

Eiso Kant [00:14:01]: So the - This - You’re gonna test my memory here,

Swyx [00:14:04]: Oh, okay

Eiso Kant [00:14:04]: So but I think

Swyx [00:14:05]: Directly

Eiso Kant [00:14:05]: I think I can recall. So if you, so if you look at, So if you take like Adam as an optimizer, you have epsilon

Swyx [00:14:12]: Yeah

Eiso Kant [00:14:13]: Which is, right, like in the denominator

Swyx [00:14:14]: Momentum and weights. Yeah

Eiso Kant [00:14:15]: Is exactly, in the denominator. And at the time, if I recall, you looked at like the early Llama papers and things like that. People were juicing epsilon, like, quite a bit. Like, they were, like, adding, I don’t know if it was E minus four or whatever, like a high value for epsilon.

Eiso Kant [00:14:31]: And if you think about this during training, it’s like a bit weird and counterintuitive that we’re adding noise to our optimizer by just adding effectively, like, a random number in the denominator, right? Like behind the decimal point. And I don’t recall the exact bug, but it had - What I remember is once we solved it, we no longer had to juice epsilon as much as, like, was happening in the Llama paper and other places. and it was like one of those fundamental moments where we had trusted this paper that was out there, and we’re like, “Oh, no, it has to be this way. It has to have this high value of epsilon.” But it made no sense to us intuitively. Like, why do you have to have this so high? Like, if you’re just trying to avoid division by zero, why can’t the value be extremely small? and that was like one of those moments where you realize like, okay, finding things out from scratch yourself builds a better intuition. Because the one thing you learn very quickly with model building is that your intuitions that you start with are gonna get beaten up so hard.

Eiso Kant [00:15:33]: Right? Like - It’s such an experimental science, that the things that seem obvious, you very quickly get to learn, like, you were wrong, and hopefully you figure out why, and sometimes you don’t even.

Swyx [00:15:45]: Yeah. yeah, so, one of the reasons that you, when you released your new models, Vibhu got really excited. I mean, everyone got really excited. But Vibhu led our paper club on it, and you guys saw

Eiso Kant [00:15:58]: Yeah

Swyx [00:15:58]: Obviously. maybe talk through some lessons learned in that, whatever you can disclose. we can focus on the model factory stuff, whatever you think is a good starting point.

Eiso Kant [00:16:08]: So I would say that our view from very early on in the company was that model building is ultimately 90% engineering.

Eiso Kant [00:16:18]: And I think we all know it in the industry because if you look at where’s every researcher spending their time, they’re spending their time writing code, right? Looking at data and writing code. And so we said, okay, The state at the moment, like three years ago, was bash scripts and Slurm and spaghetti code bases for training and, like, data pipelines that were patched together. And we looked at this and said, “Well, ultimately, model building is a process.” You’re going from raw data, right? Like training raw material, the web, et cetera. you’re doing a whole bunch of filtering, cleaning up, transformations, analyzing. These days, that’s, far more complex than it was three years ago. then you’re training a model, which is effectively a large distributed systems problem, right? Across hardware that has still-- It’s become a lot more reliable. It was extremely flaky back then. and now with every new generation, we get our new sets of challenges. And then you go into the next stages, right? There was no training back then, but, like, you got, your post-training and then your reinforcement learning. And so we looked at this and we said, “Well, this looks like an industrialized process. This looks like an end process, that every single part of it has its machinery,” right? If it’s your big data pipelines, if it’s your crawling ingestion of the web, if it’s your, large-scale distributed training, and then you’ve got your reliability. And we said, “Well, why don’t we take some of the world’s smartest distributed systems engineers that we knew and make them part of the process of research from day zero?” Not retrofitting it later on, but, like, really from the beginning. And that became our model factory. And so our model factory started with a handful of components. Today, it’s thousands of components, and I try to equate it to, if you think about, like, someone who was at the very early days of Foxconn, if they had been there for the following, decade, they would be able to rebuild Foxconn because they saw every decision that led to building that system and all the complexity. If you and I walk into Foxconn today, no chance.

Eiso Kant [00:18:18]: Right? Because we don’t have the lineage and history of decisions that led to that. And so we built early on from the beginning- with a team that really understood that, well, the metric that we are optimizing for is the speed of an idea from a researcher to an experimental result that we can trust to then being part of the next model training.

Eiso Kant [00:18:42]: And in the. And because it’s such an experimental science, ultimately, in the beginning when it wasn’t that complex, you could patch your way around it, right? But now, at any foundation model company, you are running. I mean, we’re a small team, right? We’re less than 70 researchers, another 35 engineers. and we are running, I haven’t checked the latest count, but far more than 10,000, maybe 10 to 20,000 experiments a month that we cut. And so if you look at that scale of every model run that is, like it’s ultimately it’s, it’s you need to be able to trust it as an infra problem. And so what we have now done over the years is gotten really good at that, and just by working it and improving it and obsessing over those end decisions. So now what that means is that you looked up Laguna XS 2 that we launched. It was five weeks from the beginning of training to launch. The model that we’re gonna talk about today was eight weeks from start of training, to launch. We started the next model literally yesterday because we now finished the post-training required for the model we’re launching, next week or by the time this comes out today. and we move that compute to the much larger Laguna M model that we’re now training. And so the model should be an artifact of someone’s process. It shouldn’t be really a thing in itself. Like, and we treat this like the way you would look at like a SpaceX factory where, yes, the first rocket, really hard to build, but the much harder challenge was building the factory. And now they’re rolling off, and no one is really thinking about the next launch anymore. So it’s just another launch, it’s another launch, another rocket comes off. And that’s what we’re trying to do with model building.

Eiso Kant [00:20:22]: And what has been, which was not planned from day zero, it was in the back of our mind like this will happen one day, is that when you build a really good end model factory with really good APIs and really good engineering systems, Well, what is it perfect for? It’s perfect for agents.

Eiso Kant [00:20:40]: Because agents are now starting to take over more and more work in our model factory.

Vibhu [00:20:43]: Yeah.

Eiso Kant [00:20:44]: So I look at the screens when I walk, like when we’re, we come together, in our monthly, we do monthly onsites, and I walk behind people’s screens and I stop by and I talk to our researchers. And the default is all of these different agents running on their screen that are writing the code. They’re launching the jobs. They’re evaluating the results that are coming back from the model runs. They are, making the changes. And we’re still in the driver’s seat. We’re still coming up with the ideas. We’re still helping with the debugging. But more and more, and this is right now very profound on the data side of our pipelines in both pre and post and the synthetic data pipelines, it’s starting to become more on the architecture side as well. You’re starting to see these twinklings of what RSI is gonna look like.

Eiso Kant [00:21:27]: And that’s. So when we talk about, like to your question about our models, every talk about the model factory, And my coolest example of these things is always that when we kick off a new run, doesn’t matter if it’s a training like big run or if it’s now a post, like one of 10 post-training versions we do for like release or many experiments, is that at any given moment, the changes that somebody made that they had experimental results from the day before make it into that run.

Eiso Kant [00:21:57]: So there’s not like a cutoff 90 days before. Like no, it’s like literally from that moment because we can now trust the machine enough. And then you also have to invest in the reliability. So one of my favorite metrics about like Laguna S is that there was no call events, Right? Like completely zero. And we haven’t had a meaningful call event, like something to wake up for, as far as I recall this entire year. now there is one asterisk to that. In usually the first six hours of launching a new model run, something breaks because you set a config wrong, you made a small mistake, et cetera. So that’s usually there’s a little bit of intervention, but that’s always within like call periods, right? Not on call. And I think that’s starting to now compound. So the model we’re releasing now, I love it. It’s amazing, but we’re already onto the next one. and I think that’s the way it should be.

Vibhu [00:22:50]: Hey, I also just wanna point out, so for context, this was like a month ago. we found it in the tech report, so we just came in with, “Okay, new model’s dropped. Haven’t heard about it.” We were

Eiso Kant [00:23:02]: Yeah, we’re very used to doing this every few months.

Vibhu [00:23:03]: We’re, we’re very much like, “ okay, look, it’s like, on par with Kimi, DeepSeek, whatnot, the small ones, Gemma level. Oh, it’s a very cool paper on what goes into building.” And then we hit this page, right? Like literally page two of tech report is, “This process allowed us to build the small model from scratch to delivery within five weeks applying the lessons”. And then I’m like, oh, this paper is not about here’s a tech report of benchmarks and here’s how many tokens it was trained on. Like for people that wanna dive more from what we’re not gonna discuss on the podcast, it’s all laid out here, right? From

Eiso Kant [00:23:38]: Yeah

Vibhu [00:23:39]: Custom software that agents can use to interface with training code, training data.

Eiso Kant [00:23:45]: Yeah. Well, link the paper correctly, so yeah.

Vibhu [00:23:47]: Yeah. All that stuff. read the paper here, but,

Eiso Kant [00:23:50]: But I would like to. I love principles, and I think that is a good starting off point for maybe telling some stories. Maybe we can go one by one past the principles. I’ll just call out that Dagster just got bought by a Prefect.

Vibhu [00:24:01]: Yeah.

Eiso Kant [00:24:01]: Isn’t it fun? But yes, I’m very familiar with Dagster. just anything where like they trigger some story.

Vibhu [00:24:07]: So, well, I would say, well, experiments code’s obvious, but I think one of my favorite things is, I don’t know where it is in here, but early on, and I still think this is the case a lot of foundation model companies, people prepare their training data sets, they get packaged up, then they get copied over to a training cluster distributed across all of the nodes, and then training starts.

Vibhu [00:24:30]: And we looked at this like three years ago and we were like That makes no sense

Eiso Kant [00:24:36]: You lose so much time because the moment you have to rematerialize the data set, you have to make a change, you have to fix something, et cetera, you’ve got all this time of like repackaging it, right? Toca- tokenizing it, repacking it, moving it over to a cluster, then distributing it across the nodes. The bigger your clusters are, you start using fancy like torrent-like algorithms to like distribute your data. So why aren’t we streaming data into training? Right? Something that’s very common and like just basic

Vibhu [00:25:00]: Like just in time

Eiso Kant [00:25:01]: Just in time, like good computer science like principle. And that was one of the first things that I think unlocked - the model factory. Because the moment you start thinking about, well, a training job, it doesn’t matter if it’s a big hero run or a small like, post-training experiment, consumes a certain number of tokens per second, right? And it’s not a lot, right? From a like a data, moving data perspective. So we said, well, we have our training cluster, and then we’ve got like our AWS kinda setup where we can build these amazing big data pipelines. We can set things up. We use Spark underneath the hood, like all these things.

Vibhu [00:25:36]: But when you say AWS, it’s not actual AWS, it’s your internal AWS.

Eiso Kant [00:25:39]: It’s our internal-- No, it’s our internal like just running like our infrastructure

Vibhu [00:25:42]: Site web services

Eiso Kant [00:25:43]: Exactly. Our stuff running on like an AWS account or on like any hardware, right?

Vibhu [00:25:47]: Yeah.

Eiso Kant [00:25:48]: And so once we made that shift into I can stream data into training, all of a sudden you realize a lot of things unlock. Because now you don’t have to wait for the whole data set to materialize.

Eiso Kant [00:26:00]: You now all of a sudden when you’re running data experiments about mixing data, it’s a config. Because you’ve got these data sources that are coming in, and you just - we have this service called Blender that’s in the report, where we then say, “Okay, for this run, I want 20% of this source, 10% of this source. I want this much, so many epochs of repetition. I want this to be, shuffled in a certain way,” and your training job can start while the rest of the data is even still materializing. also what it does is because all of this underneath-- So for us, we treated the data layer underneath as like an immutable data layer, and that was really important. Like experiments as code, immutable data layer means that you can always go back and understand literally down to the single token at which cursor it went in on which version of the code.

Vibhu [00:26:47]: Yeah.

Eiso Kant [00:26:48]: And it took us a I have to admit, like the first year of Poolside, we understood that engineering had to get great, But we didn’t understand yet, that this is ultimately in support of like a good rigorous scientific progress. We were quite a - We were a very small number of people, so a lot of it was YOLO ideas and YOLO runs.

Vibhu [00:27:08]: Yeah.

Eiso Kant [00:27:09]: And we built great infra for the YOLO runs. But once we realized that we treated data as immutable and code as always versioned, and you could always track and trace every experiment end to end perfectly, you could repeat everything perfectly, right? You have perfect reproducibility. I can still reproduce runs from two years ago if I wanted to, right? It enables the scientific progress, like the scientific process, and I think that took us probably about a year and a half into the company to figure out. We also had some great hires, like our head of applied research, Nikolai, who joined us from Yandex, who’d been working on language models since like the early 2020s, I think brought that into the company of like, “Hey, we wanna have even more rigor.” And then once we kinda had the combination of like increasingly more capable platform that allowed people to do more, but had this immutability, we were able to start “Okay, every experiment is truly an ablation. We truly need to understand it.” And I think we became much more scientifically rigorous in the last couple of years, and the infra underneath enabled it. and then there’s just fun stuff like, and

Vibhu [00:28:16]: Yeah, a lot of it’s fun, like even just the, one, you share all the ablations, two, picking the data sets, right? There’s like a random small paragraph in here where it’s just like, “Oh yeah, training data, we have some, we have an auto mixer.” it trains eight small models, scales them up, picks the training data set. We don’t even need to look at it. I’m like, “Wow, a lot of engineering rigor there.” And there’s just, there’s just a lot in here.

Eiso Kant [00:28:40]: Yeah, and it’- and look, and we wanna put out more. Like we, We treat writing papers as something that we haven’t earned the right for yet for a long time. So you earn the right to spend time, publishing research once you’re at the frontier, because until then, you’re catching up, and every minute and hour in this industry matters. Like I obsess over it, not just the wall clock time from idea to result, but just general like time every day that we, waste is one that doesn’t allow us to catch up. But in this case, we said, “Okay, we’re gonna give ourselves.” I think we gave the team like three or four days while still doing their work, like give everything in there. And to your point earlier, if your stuff, it’s easy to like put it out. And so there’s so many more things that we wanna talk about over time, and we will definitely start doing. And as we earn more of the right, but also now have like added to our mission that we want more foundation model companies to exist, you’ll see us like be way more proactive, and just trying to keep dropping some of those like things that we’ve learned along the way that can help others like speed up.

Vibhu [00:29:40]: Which is the other cool side of this, right? It’s, it’s not like, back to your point, it’s not just here’s the benchmarks of our training. If you want to replicate, here’s experiments of optimizers, data sets, post-training. you lay out a lot of it here alongside here’s your system for how to do it? So it’s, it’s really like promoting

Eiso Kant [00:29:59]: No, thank you

Vibhu [00:29:59]: Other people can do the same.

Eiso Kant [00:30:00]: And by the way, I also wanna make clear, right, we have been incredible-- Like we’ve taken a lot of advantage of the fact of all the open research that others have published, Right? And you mentioned, the Chinese labs, and we I think it’s important that there’s, from every country and every culture and background, including like Western companies like us, there’s different models that come out that people can choose to trust. But I think we do have to give credit where credit’s due, right? The incredible Chinese lab have done an amazing job at sharing their research, and we have definitely like been on the receiving end of taking advantage of that. So when you’re on the receiving end of something coming to you, I think it’s, you also have an obligation to give back.

Swyx [00:30:39]: Do you have a favorite or underrated Chinese lab that you wanna shout out? Everyone shout outs DeepSeek.

Eiso Kant [00:30:44]: That’s a good question.

Swyx [00:30:45]: Moaan obviously for Therapsi. Yeah.

Eiso Kant [00:30:48]: Yeah, look, I think, I think obviously everyone’s been talking about Zhipu lately, with 5.2. I think what most people don’t realize is when they started.

Swyx [00:30:59]: Yeah.

Eiso Kant [00:30:59]: Right? They started years before ChatGPT.

Swyx [00:31:02]: They just rebranded. Yeah

Eiso Kant [00:31:03]: And so, I’ve like, I remember how hard it was to work on these things Before the rest of the world got excited about it. And so I have an immense amount of respect for people, who were working on improving models when it wasn’t the sexy thing to do, when believing in LLMs, was gonna get you ridiculed. I remember like back in 2016 when we were doing what we’d call, machine learning on code with some of these models. we would-- people would just laugh at us, like they’d be like, “This makes no sense. Like why are you wasting all these, like, millions of dollars on trying to figure this out?” And so I would say they’re probably the one that, I think deserves a shout-out, not just because their latest model is very good, but because they fought to get here. And I think, I think every foundation model company it takes time to get here, right? It took us three years to get to the model that we’re, that we’re now gonna be releasing. and now the time in between the models is coming, is counted in weeks. It’s no longer counted in months or years. But this stuff’s hard. and if we can make it a little bit easier for the next person, like we should all do so. Because if we don’t do so, we’re, we’ve got a small window before models are really impacting recursive self-improvement to a level where catching up otherwise might become unfeasible. And we should try to, in that window, encourage as many labs or however we wanna call them, like to start. And so one of my current

Eiso Kant [00:32:36]: Mission, but qualm is like I wanna encourage whoever is a researcher right now who thinks they can tackle this to go and leave and become my competitor.

Eiso Kant [00:32:45]: Like start another foundation model company because I think we need it. I think otherwise we’re not gonna be in the world where, I don’t want to just be the fifth or the sixth company that wins. I wanna look at a world where there’s lots of choice.

Vibhu [00:32:57]: What else do people not see in starting a foundation model? it’s, there’s a lot of compute, there’s a lot of capital required, a lot of compute. You lay out model factory and how to do the training, but there’s a lot there, right? That’s,

Eiso Kant [00:33:10]: Well, look, it’s, I in turn-- this is an oversimplification, and I always asterisk it with that because it can land a little bit the wrong way in people’s minds. But I think you can sum down, And I saw it, 95% of model building to just doing, you’re just doing two things. You’re improving data or you’re improving compute efficiency. And I know that feels like an oversimplification for the incredible, like, Gifted and skilled work people do. But if you really look at it, like what are we doing? We are looking at data, we’re generating new data, we’re improving data. and the only way to do that is to look at the data, right? That’s a big part of foundation model building. And on the other hand, we come up with these incredible breakthroughs in inference, in architecture, and new attention mechanisms. But what are they really doing? They’re bringing compute efficiency. Now, we have definitely had some breakthroughs over the years that allow for more model capabilities. But at the limit, if you could train a large enough model, right, like, and you had infinite compute, we probably-- if you had infinite compute, you’d be at AGI probably already tomorrow.

Eiso Kant [00:34:12]: Right? Like it’s not. And so, and let me say that infinite compute with infinite ability of much faster networking because networking ends up being more of the bottleneck than compute. But, so I do think that’s, those are the main things. And to just realize that this is engineering. I think it’s become more obvious, but I think for quite a few years, people have held foundation model companies and researchers and others on this pedestal of like you’re doing incredible magic or rocket science, or only like, Nobel laureate physicists can do this. And don’t get me wrong, there are some really hard problems that need to be solved, but a lot of the work that all of us are doing on a day Is not sitting down trying to solve a math theorem. A lot of the work that we’re doing is just really doing the basics right, writing good code, looking at data, improving it, running experiments, looking at plots, trying to see like, hey, trying to shape our intuitions. And a lot more people could be highly capable researchers. and I think that’s, it feels far for people to do so. But I’ve seen in our own company, we’ve seen engineers become researchers because the model factory allowed them to be, have a much lower hurdle of running experiments and trying things. And one of the guys on our team who started as an engineer building our agents is a legit reinforcement learning researcher now, making real progress. and that happened in the span of like six months. that would’ve not been what I think most people assumed was possible, a couple of years ago.

Swyx [00:35:46]: Yeah. I think one of the interesting moments is when you can self-host, like, if in a programming language, like if you can compile the language in the language, the equivalent is can you use your own tools, right? You have the pool CLI, you have your own models. presumably you’re not only using your own models. There’s no way. But like, what’s that percentage over time?

Eiso Kant [00:36:10]: This is the first model that we’re releasing that is starting to meaningfully contribute to our own work. It’s not a it’s not state-art model yet. Fable and other, they’re, they’re very capable models, but Laguna S Is really interesting. I’m gonna pull up the quote. Peng Ming, one of our heads of applied research, said something, last week as the model came out about 10 days ago, much better than we had hoped for or expected. And he said, I have the feeling that a lot of the gains in Laguna S come not from more intelligence, but more from different behavior, more verification, less taking things for granted, not declaring victory early, and being way more persistent. And to be honest, those are more predictive than raw intelligence for success in human also to some degree. And this was, he wrote me this on 5th of July on a Sunday, and it’s been burned in my brain ever since because the Laguna S model, as you’ll see it and why it does so well on benchmarks and why it does so well in using it on a day basis, is that it’s just incredibly persistent. It reasons a lot. I do call that out. We have work to do on making it more efficient. We have to work to do on offering different reasoning modes. But this is the model that has been able to do things that I never thought it could do. A hundred eighteen billion 8B active model, which is not that large. It fits on a DGX Spark and still runs at, thirty, forty tokens a second on a Spark, is able to solve Erdős 397 independently. It’s able to do complex programming tasks. It’s able to. I asked it this morning to make me a Fi scanner without using any external libraries on my Mac, and it’s, like, figuring out, like, the core WLAN API by really persistently trying to understand it without access to the internet. And more, I love vibe checking. I’ve probably spent eight to ten hours a day with this model for the last ten days.

Eiso Kant [00:38:05]: I’m not exaggerating. I was on my eleven-hour flight yesterday. I spent ten hours reading trajectories and traces and, like, of the model.

Eiso Kant [00:38:12]: And what I take away from it is exactly what Peng Ming said. We are gonna be able to squeeze so much more out of smaller models than I think we had imagined in the industry because, yes, there’s intelligence and larger models are more intelligent. Like, no doubt about it. We should continue to scale up. but the behaviors of being really persistent, of being able to backtrack when you’re wrong, of, like, understanding how to interact with your environment show us that we can get a lot more out of it. And this, for me, has created a bit of a Question in my mind the last couple of days. If you think about where we’re using models today, right? We are using models, say, for knowledge work. Represents twenty-five percent of the global economy, twenty-five trillion dollars of work.

Eiso Kant [00:39:00]: As we scale up models and they become more intelligent, we are excited about using them more and more for pushing the frontier of science.

Eiso Kant [00:39:08]: And if you look at the frontier of science, like true breakthroughs in science, they have been linked, they are linked to more intelligence in many places. Einstein figuring out general relativity is able to bring ideas together that other people would have not brought together. And I think one of the many dimensions of intelligence is the ability to do that, and it’s something we clearly see that as models get larger and more capable, they’re able to pull more ideas and threads together that a smaller model wouldn’t be able to.

Eiso Kant [00:39:36]: And we’re starting to see examples of that in medicine and, like, in bio and other things. But if you think about the majority of knowledge work that we do, and it includes building software. I’m a software developer at heart first and foremost probably, although I probably can’t say it that much anymore as I don’t write production code in years, is that what makes us good is our persistence. It’s our ability to encounter a problem and backtrack and say, “I need to go figure out this bug. I need to go research this. I need to go look at the documentation. I need to, like, try different, five different ways to see, like, if I can solve it.” But it is not necessarily bringing three ideas together from radically different fields. And so if we are now seeing, and I think Laguna S is an example, that we are able to make a relatively small model much more capable than I had definitely predicted or any previous, like, benchmarks had shown for any model remotely this size or even larger, At least on coding tasks, that it’s because of the behaviors. And so now the question I have, and I don’t have an answer, it is I know at the limit, so infinite model size, right, extremely large model, and the cost of that model is gonna be very expensive to run. We know this, right? So larger model ROI.

Eiso Kant [00:40:52]: So I know that at the very limit, I’m not gonna use the world’s largest model one day, quadrillion parameter, whatever crazy, like, scale we scale up, to do a basic coding task. Already today, I’m starting to size down for certain tasks.

Eiso Kant [00:41:07]: So it means that there is an optimal. It means there’s some curve that goes as we go up to model size for knowledge work, at some point we’re at the peak, and after that, the return on investment of using a bigger model, just doesn’t make sense.

Eiso Kant [00:41:22]: Now, I think the question is, before I would have thought that peak was extremely very far away.

Eiso Kant [00:41:30]: This model for me is the first sign that Maybe that peak is At a trillion, five trillion, ten trillion. Maybe we can just squeeze way more out of these models. I’m no longer thinking that we need two or three orders of magnitude on the largest models to be able to, solve knowledge work, the accounting, the legal, the code that we write. And so if that holds true, It is an argument for the commoditization of models. It’s an argument that open source can win and, like, succeed in this world. And now it’s of course a self-serving argument and it’s a hopeful argument, but theoretically at the limit it works. We just have to go discover in the next couple of years of how much more we can squeeze out. Now, I do want to put a big asterisk. This does not mean I’m against scaling models. I think we ultimately only succeed if we scale our models as large as our competition. I do not like. I think we should not put our head in the sand and say we’re gonna be king of open source small models. I think that’s, It’s a out. It’s trying to be king of your own kingdom, but not realizing what the rest of the world’s doing. All of us rather use a smarter, faster, more model. It’s a sign of hope. And so I don’t wanna overly state this is a good model. We have a long way to go to get to the state-art. But what hopefully people take away when they use this model is that the behaviors inside of it are what push it to be far more capable, less than necessarily the number of parameters.

Vibhu [00:43:03]: Is that mostly post-training? Like

Eiso Kant [00:43:05]: Yes

Vibhu [00:43:05]: Right.

Eiso Kant [00:43:06]: It’s entirely post-training.

Vibhu [00:43:08]: Are we done improving anything on training? Is, like, training done?

Eiso Kant [00:43:12]: No.

Vibhu [00:43:12]: Okay.

Eiso Kant [00:43:13]: So

Vibhu [00:43:13]: I just wanted to cover training, and then we go post-training

Eiso Kant [00:43:15]: Training is not done. I mean, look, there’s a part of training of just dealing with skill, right? Every new order of magnitude of model skill, you are going to get new things you gotta solve for. That’- but those are ultimately, engineering challenges.

Eiso Kant [00:43:31]: I have a, I would say, a not commonly held opinion that reinforcement learning Will move earlier and earlier into training.

Vibhu [00:43:42]: Yeah, training.

Eiso Kant [00:43:44]: Not even training. Like training today, right, is, like if you look at - So we’ve been working on this for years already. and I think the best-- I think the first time we saw it out in public was the DeepSeek Zero paper. this is a year and a half ago, I think, if I recall correctly. where, you can Very early on in a model as it starts capable of being able to use language, et cetera, induce reasoning. and so the question that I have is like, we have this- we have the dataset that’s the web. and the web, I think we could arguably say probably has The totality of humanity’s knowledge somewhere encoded in different places. It’s a huge variance degree of quality, from garbage data, and like once you look at training data, you really get humbled of like what the web is, to like, the most greatest scientific papers and best blog posts and like, best transcripts and whatnot.

Eiso Kant [00:44:39]: And so now What we are trying to figure out, and have been doing a lot of work on, and it’s a place where maybe not as open as we’re on other things, but we will become more over time. we’ve been spending a couple of years really doing research on how can we turn the web into not just next token prediction, but into a way to teach the model to think earlier in its training. and I think there’s a huge amount of gold to be found there. I think we are right now in, we’ve got some drugs in the industry. One of the drugs is distillation. Another drug is, more environments. Like, and they’re great, and they make us feel good, and they make the models better, and like we’re all addicted to them, and we’ll use them, right? in various different ways. and but ultimately, I think we are still barely squeezing out of the web what we should be getting out of the web.

Eiso Kant [00:45:33]: I think just next token prediction during training is not enough.

Eiso Kant [00:45:36]: And

Vibhu [00:45:38]: Yeah

Eiso Kant [00:45:38]: I think we’ll see some very interesting things still happen. and that RL in post-training to induce behaviors, to improve things, like I think - the whole world knows how to do this now. I think we’re, we’re scaling it up. Everyone is. But I wonder if we need to go as far as we’re going today with environments. I’m not sure yet

Vibhu [00:46:01]: You mean we’re going too far?

Eiso Kant [00:46:02]: I’m, I’m not sure if the path to AGI is just

Vibhu [00:46:06]: Is more environment

Eiso Kant [00:46:07]: More environments.

Vibhu [00:46:08]: It seems like a never-ending, “Okay, I want instruction manual for this table, right? Am I gonna environment out building furniture? Or are we just gonna tail end like we need some general solution?”

Eiso Kant [00:46:19]: I think there is, I think there’s an ability to generalize more from the web. but I also am very encouraged, like when I look at Laguna S and, which is post-training is, well, is the big impact there. and I see like, oh, wait a second, just by making some of these behaviors much better, we’re able to get so much more out of it. It just changes a little bit the way you think about intelligence.

Vibhu [00:46:40]: Yeah. The analogy people draw often is the RL phase is where you don’t learn as much new knowledge. You shift

Eiso Kant [00:46:46]: Yeah.

Vibhu [00:46:46]: Yeah. So, you shift distribution, and you can have it reason towards what you want. on your point about training, a lot of training is still just continue training in a domain, say medicine, then you do RL. So still just

Eiso Kant [00:47:00]: It’s just better data, right? Like, I mean, training, ooh, I like how we invented this word. Like it’s effectively just like,

Vibhu [00:47:06]: Second phase

Eiso Kant [00:47:07]: It’s the second phase of training With like a really dumb way to do a curriculum. But like ultimately, what you’d want is a curriculum from token zero to token 30 whatever or 40 trillion tokens that really truly is the optimal curriculum for the model to learn. But training is essentially a stage curriculum on the web because we do not have to compute, And, effectively to try to ablate the perfect curriculum, right? And so I’m pretty sure that you’ll start to see people talking soon about some other term, and there’s two or - ‘cause now we do this, right? We talk stage two and stage three and stage four training and like. But ultimately, all we’re doing is we’re trying to assign a curriculum to the web data that we have to allow the model to learn better. I think at some point, as things get compute, as models get cheaper to run, as the next generations of compute, this will become more of a continuous spectrum. I also think the reason, by the way, you have training and like stage two and stage three is organizational, Right? It’- this is, I think, a thing where-- that we really try to avoid with the model factory is like Training exists because there’s a training team now, right? There’s people, or like people in training decide to focus on like a training effort. but what you really want is engineering and scale of experiments that allows for a much more continuous spectrum that you don’t, you have infinite stages. Now, we’re not there. Compute’s not there. Organization design is not there for it yet. but I think we’ll get there. we’ll look back on a couple of years and be like, “Oh my God, it was so cute that we did our training data like this in such a like naïve way. Like we barely ordered it. We didn’t really do a good job at like

Vibhu [00:48:48]: The building that curriculum will get you that in the industry.

Eiso Kant [00:48:51]: And I’ll confirm that, when I talk to some researchers that this is a lot of the focus now is like how does training change and what is the next objective other than, next token prediction. I assume you don’t have the answers, but you have some ideas.

Vibhu [00:49:02]: We have some ideas. We’re not ready to talk about it yet.

Eiso Kant [00:49:05]: Yeah.

Vibhu [00:49:05]: We’ve been working on them for years, and I think that’s the one thing that’s also like you asked earlier about, like what’s not obvious about building a foundation model company is that you are constantly balancing the table stakes work, the recipe works

Eiso Kant [00:49:19]: Yeah.

Vibhu [00:49:19]: Versus like your, my crazy

Eiso Kant [00:49:22]: Pure research

Vibhu [00:49:22]: Breakthrough.

Eiso Kant [00:49:22]: Yeah.

Vibhu [00:49:22]: Pure research and finding that balance and adjusting the percentage to it based on where you are in the race is really important.

Eiso Kant [00:49:31]: I mean, so like, this is a nice way. I was gonna bring up auto research at some point

Vibhu [00:49:35]: Yes

Eiso Kant [00:49:35]: As another Andrej invention, or coinage, which is like, I honestly, like how many objective functions can there be, right? Like just try 1,000 of them, set it running, whatever.

Vibhu [00:49:47]: Man, it’s also

Eiso Kant [00:49:48]: Like what you’re looking for. You’re looking for loss curves like that, like

Vibhu [00:49:51]: It’s also a thing people take bets on, right? When you say more Neo labs, you’re doing a version of we’ll do foundation models, scale them up, next token predictors. A lot of other Neo labs that we see want to take a completely different approach, right? At some level, you’re right. It’s all, compute efficiency, and that’s the net objective. But some are okay, different architecture, like vastly different amounts of compute spend. So some are different. They’re not just

Eiso Kant [00:50:19]: Yeah

Vibhu [00:50:19]: They’re like, 99% not balancing, here’s the vanilla and scale up. They’re 99% on, here’s novel research that’ll change everything.

Eiso Kant [00:50:27]: And I think, Luke, I think you. It depends when you started as well, right?

Vibhu [00:50:30]: Yeah.

Eiso Kant [00:50:30]: When we started, like the novel thing we did was reinforcement learning on code. No long- that’s no longer novel by far, but we were like, - that’s where we obsessed over when no one believed in RL. So you have to when you start the company, you have to have your own idea. You have to have something that’s different that allows you to speed up, right? For us, it was RL to LLMs that later became common, like, Knowledge. But in the beginning, it wasn’t

Vibhu [00:50:53]: It’s cool. this was like your original 2023 blog

Eiso Kant [00:50:57]: Yeah

Vibhu [00:50:57]: Of purpose.

Eiso Kant [00:50:58]: Yeah.

Vibhu [00:50:59]: And like you do lay it all out here.

Eiso Kant [00:51:01]: We laid

Vibhu [00:51:01]: The blog is pretty underrated, right? The whole RL on code was very early on.

Eiso Kant [00:51:06]: Very early. And even we had to argue with people, like we say here things like to push beyond current capability, to train your own foundation model. We had to argue with people that it mattered that you had your own like, base model. you can fine-tune your way to success, right? major capabilities emerge from training a base model made accurate and useful during fine-tuning.

Vibhu [00:51:23]: Which like, for perspective at the time, we knew closed models, OpenAI, Anthropic were huge. The open models we had were like Mistral 7B, a 30B, a 70B.

Eiso Kant [00:51:35]: When we

Vibhu [00:51:35]: Yeah

Eiso Kant [00:51:36]: The date on this thing is wrong. When we published this, it was April 2023. I think this was just

Vibhu [00:51:42]: Yeah

Eiso Kant [00:51:42]: Happened on a migration, probably found it on archive.org.

Vibhu [00:51:45]: Mistral.

Eiso Kant [00:51:46]: Mistral had started, we started on the same month, right?

Vibhu [00:51:49]: Yeah.

Eiso Kant [00:51:49]: So this wasn’t even, there was only, I think, Llama out at the time

Vibhu [00:51:52]: Snell

Eiso Kant [00:51:52]: And that’s it, right? And so, but I agree. I think we want, We want as many diversity of ideas, and I do think if you’re starting today, you want something that gives you an edge, right? and what I do think we sometimes over.

Eiso Kant [00:52:13]: I think every archit- like at the limit, every architecture works. An RNN works, it’s just not compute efficient, right? Like, say if you had infinite compute, you could probably just, take a basic RNN from back in the day, and you could get pretty far.

Eiso Kant [00:52:27]: Now there have been, meaningful breakthroughs, attention, other things that are there. but I think we’re still, we’re still very early in figuring these out. The things I’m most excited about, I’m most excited about people doing extremely low precision training, right? So like the ternary stuff that we’re seeing, and it

Vibhu [00:52:47]: Oh my God

Eiso Kant [00:52:47]: Very cool. The Bonsai stuff yesterday was super cool to see. I think that if you can find tweets from me going back to 2023, which is like the notion of like, well, it’s an obvious trade-off. Bigger model, lower precision equals, smaller model with higher precision, by definition, right? It’s just what is, like how does that play out, right? What’s the actual size limit? So you now have companies that are trying to figure that out, but those are the things that can change our industry if they’re done right.

Vibhu [00:53:14]: Yeah.

Eiso Kant [00:53:14]: Because ultimately, like our bottleneck on compute is a MatMul bottleneck, and a networking bottleneck, and the moment you start doing those things. So I’m excited about that. We’re not doing - I mean, we’re doing the usual, like, Laguna S was trained in FP8. only thing that in this run I have to admit that wasn’t FP8 was the all to all in the new run we just started yesterday. The FP8 was all to all. That was just like cut off date, like, oh, we’re not perfectly comfortable wanting to do it. you’ve got amazing work by Nemotron and NVFP4 training. Like, I think it’s underrated what they’ve done there. I’m excited to get to NVFP4 training. doesn’t make sense yet ‘cause we’re still training on Hoppers, right? We’re like relatively small. We’re 10K H200 cluster company right now. We’ll be scaling to a lot more soon, but, and really a lot more if someone is thinking about applying for a job. but like the. Yes, I think it’s, there’s so much more juice to squeeze out of this, and hopefully Laguna S shows people that a model at this size can get a lot more and we did this thing in eight weeks. We think there’s a lot more juice to squeeze out at any model size. we’re now scaling up because it’s the most optimal thing to do for us as a company. But if I had infinite time, I would love to push more the capabilities at other model sizes.

Vibhu [00:54:34]: I don’t think we’ve properly announced what your new size is. So we have XS, which was 30B-ish.

Eiso Kant [00:54:41]: Yep.

Vibhu [00:54:41]: Old medium was 200B, which is gonna be deprecated

Eiso Kant [00:54:45]: Yeah

Vibhu [00:54:45]: It seems. So new Laguna Small

Eiso Kant [00:54:48]: So Laguna S, Laguna Small, 118 billion total parameters, 8B active, so very sparse. It’s a scale-up of the XS architecture. It’s the classic, or call it classic these days, like three-one ratio of sliding window attention to global attention. It’s just, it’s a nice size, for a couple of reasons. One, it’s just very cost efficient. For us, it was a good way to - We wanted to get our progress out quickly. One of the things that we’ve seen is that it’s a balance inside a foundation model company between focus on releasing and shipping And, like, your new novel research. But with the model factory, we are able to, like, treat the release of a model as less of a time investment from the team because it’s just, oh, at this moment in time, do the training run, done, apply the latest post-training. And so this is, I think, a nice weight class. It’s one that also will fit on a DGX Spark, which, I have a small, like, soft spot for. I love having that little thing, like, run a good model.

Swyx [00:55:52]: Yeah, we covered it on this pod, GTC last year.

Eiso Kant [00:55:54]: Nice.

Swyx [00:55:55]: I think a OSS 120B was the first because it’s a large single GPU, which was the H100, right?

Eiso Kant [00:56:02]: Exactly.

Swyx [00:56:02]: Rent one H100, now you’ve got 128 gig Macs, Mac Minis, Sparks. It’s, it’s the home sweet spot.

Eiso Kant [00:56:10]: But I think what I’m most excited about is that this model hopefully shows people what is possible in this size because, when you’ll look at the benchmarks and start using it, you’ll realize that we are outperforming models two or three times their size.

Swyx [00:56:24]: Yeah, and they think-- So for example, today’s Thinky model is like a trillion params.

Eiso Kant [00:56:28]: So yeah, exactly. And look, and by the way, I’m excited about-- I have-- It just came out, so for those of you who are listening to this at like, I saw it on my phone

Swyx [00:56:34]: If you’re, if you’re listening

Eiso Kant [00:56:34]: If you’re humming

Swyx [00:56:35]: Yeah.

Eiso Kant [00:56:35]: Like two seconds, so I haven’t even had a chance to read the post.

Swyx [00:56:39]: But somehow you are, not only you’re, you’re better than Thinky, which is like one of those benchmarks, but also, like, on certain benchmarks, like the τ-bench one, like you’re state-art.

Eiso Kant [00:56:51]: We’- Look, we’re doing, I’m not sure if we’re state-art on I mean, 3 banking, I haven’t checked where we sit on the leaderboard. but I think we are, within our weight class, I feel very comfortable to say, and even in some weight classes twice larger, that we are probably state-art. I also want to caveat this, like, best model still in the world right now is definitely, give me a Fable, give me a 5.6. To your point earlier, we also use other models.

Swyx [00:57:15]: Yeah.

Swyx [00:57:15]: I think the, so the interesting thing you mentioned earlier is you’re starting to shift a lot of your actual usage to it, right? Benchmarks are like

Eiso Kant [00:57:21]: Yeah

Swyx [00:57:22]: They’re good to compare, but they’re not super realistic. It’

Eiso Kant [00:57:24]: They have to, right? This is how they’re gonna dog food benchmarking.

Eiso Kant [00:57:27]: No, you have to. Like, you have to use your own models, and you have to have your own internal evals and benchmarks. And what the funny thing is, like within first 30 minutes of a new checkpoint coming out that’s, the first post-train after a train, you yourself can feel in the first 30 minutes of where this model’s gonna be. Like, you don’t know exactly, but like when this one came out, we were like, “Oh,” like, “this is different.” Like, and I think that’s, I think that’s the best example. but it’s a little bit like your kids. I don’t have kids, but parents, like, they see their kid and it’s perfect and they love it, and then like, they don’t see all the rough edges. You always get that when you build your own model. It’s the most fun part is that you, like, you love a little bit every model that you do. We try to say this thing constantly, it’s like, “It’s the worst model we’ll ever train.” And so I know the team now is like already onto

Swyx [00:58:18]: Yeah

Eiso Kant [00:58:19]: The next one, as it should be, because this is a race. and this model is a moment in time that hopefully shows people that we are serious about this race, that we wanna work really hard at it, that we want feedback, right? Where is it good? Where is it not? Like, one of the nice things about having your models out in open weight and out in the world is that you get a lot of feedback.

Swyx [00:58:40]: How do you think about building it with like, working with a harness, right? So OpenCode, Codex, you have your own pool CLI tool. getting people to use it, the design of model harness, training it in.

Eiso Kant [00:58:54]: So you need to do some multi-harness training. Like if you, especially at these smaller sizes, like you wanna do a little bit of multi-harness training for these models to just get the right. And it’s very little. Like, you don’t need a lot, but it’s just like to get the right behaviors that you see in your harness transferring to the harness that, like, you, other people might use it in. we internally have been just calling this polishing, which is like you’ve got your model and you do a little bit of polishing so that, like, it’s able to work well in other harnesses as it is in your own.

Eiso Kant [00:59:24]: No doubt it’s going to be better in your own harness, and it’s just because of like where are you putting your reinforcement learning compute, right? You’re putting your RL and your synthetic data, you’re putting it to your own harness because it’s the one that you understand the best and you’re able to push the most. because that end control is what allows you to make it better. then transferring those capabilities is more about just making sure the model, induces the right amount of reasoning and like, understands some of the maybe more complex weird tool call formats that might exist somewhere else. and so we do some multi-harness polishing, as we call it. it’s not really what drives capabilities, but it does create a better experience. I think everyone probably does these days, but it is totally fair to see why your own harness is going to still be better than others. And I think we see this with all the foundation model companies. and it’s just that when you are pushing capabilities, you don’t really wanna trade it off by putting 10 harnesses in your RL runs because it’s just complexity. It’s complexity of engineering because these-- When you’re trying to do good science, right, when you’re trying to really understand what made my model improve, you wanna make one variable change to something you understand. And a harness from someone else, you don’t know or understand in the same way as you understand your own, right? They might have different agents or different prompts

Swyx [01:00:48]: Yeah,

Eiso Kant [01:00:48]: In different places

Swyx [01:00:49]: If it’s open source, you can look at the source.

Eiso Kant [01:00:50]: Yeah, but it’s time, right? Like I really cannot stress, like I know I’m like a weird person on this because like I have friends like, “Can we meet up?” Or, “Can we do this?” Or, “Can we go out?” I’m like, “No.” Because ultimately, this is a race, and time is the only thing that matters. And if I look at our team and say, “Okay What is complexity worth introducing on our general trajectory to building more capable models? Which generalized to other harnesses quickly. And by the way, our model works well on other harnesses. I really encourage people to do it. It works well. Like I’we’ve been testing it in OpenCode and Kilo Code and others and like, and in Claude Code.

Swyx [01:01:22]: Which just got bought today.

Eiso Kant [01:01:24]: I saw it.

Swyx [01:01:25]: I mean Honda. Yeah.

Eiso Kant [01:01:25]: Exactly.

Swyx [01:01:26]: Everything’s getting bought.

Eiso Kant [01:01:27]: Exactly. and I think part of that is like, and there’s some amazing. I’m, I’m excited, like I think Hermes is a ridiculously cool harness like, and

Swyx [01:01:37]: And, part of the question was just like how much of it is model versus model plus harness, right? So new benchmarks like Agents Last Exam, it’s not wanting to just measure the model. same with models getting more and more agentic. They need a harness to operate in, right?

Eiso Kant [01:01:55]: I think for when you’re asking that question to a model company, I think you can separate it in two parts, which is like The harness, like we have a very slimmed down harness. When you look at it’s like six tools. It’s like shell and like shell kill, shell wait, write, fetch web, and like, I don’t know, bash. Like I think I’m missing one, but like that’s effectively all the tools. And it’s very simple. It’s very lightweight. So it is not a harness that is designed to try to do well on a benchmark or try to do well on a certain subset of things, right? It’s not a deep research harness. So I think we see incredible ability for complex harnesses that build lots of prompts around and extra data sources and other tools to really push capabilities of models forward.

Eiso Kant [01:02:41]: But our model is still better than some other harnesses who do that in coding-like tasks because it was RL’d with it.

Eiso Kant [01:02:48]: Now, I do encourage people, I think our model, by the way, is perfectly fine and good on ours. The differences are probably maybe too small for anyone to notice, but we see it ultimately still on benchmarks, by a little bit. So I think it’s both are true. Foundation model companies with their harnesses will really push them because it’s just operationally, the best way to have scientific rigor in improving your models. But also someone who takes our model and really does a lot of work on improving a harness is going to compete us, as they should. and that’s just because the harness is the stopgap between what the model is capable of And what it needs as additional instructions, and what it needs is access to data and tools, right? And that’s ultimately, I think, what a harness is. It’s like, is it able. As you build more capable models, you’re improving the instruction following the models. And so additional harness is just saying, “Hey, if you encounter X, Y, or Z, behave this way.” And so even if you would say that two models with two different harnesses can equally reach the same capability that you care about, a harness that is really tailored towards a capability will do it more efficiently.

Eiso Kant [01:03:58]: It’s like a person who’s getting a manual of how to do the task in the most efficient way with the right tools and the right data sources versus a really smart person like, “Go figure it out.” They’ll both solve the task, but one will do it a lot more efficient. So I’m a big fan of all the harness development that’s happening in the world, and we want to work with more harness like creators to also make sure that like if it needs some additional training, like publishing, that we will do it.

Swyx [01:04:22]: I mean, I think when you say it’s a race, there’s a question of what are you racing to? are you racing to be the best coding model company or the best coding model plus harness company? I think that’s a, those are different things.

Swyx [01:04:36]: Or neither.

Eiso Kant [01:04:37]: Or neither.

Swyx [01:04:37]: Yeah.

Eiso Kant [01:04:38]: So we. I race to AGI. Coding for us since day zero of our website has been, and we’ve said this over and over again, we think focusing on coding and long horizon like software tasks is a path towards AGI because it forces us to solve the hard problems. It’s, it forces us to solve the ability to do extremely long horizon complex work that requires lots of reasoning, external tools, data, et cetera. And one of the things I can show you, so we’ll, we’ll have a web chat on with this model, and I’ve loved this model for deep research, just using it in my coding harness. It was never trained for it. It was never like looked at it, but it’s great at it, in my opinion. because ultimately, the skills transfer, they generalize. Now, where we are not focused on today is to make sure that the world’s greatest medical knowledge is encoded in this model or the world’s greatest legal knowledge. But it did. We won’t be publishing this benchmark ‘cause we didn’t have time to really do proper, but it did really well on LegalBench. and at least on our first runs, and we are very rigorous. When we publish evals, we have Checked them for every little thing. We have run them many times. We’ve passed, like we’ve gone and we’ll, like we try to be extremely honest with this, so if we haven’t spent enough time on a benchmark that we use internally that is public, we just say that we won’t publish it. and

Swyx [01:06:01]: I mean, the other way is just to give it to artificial analysis and let them run it.

Swyx [01:06:04]: Like third party standards.

Eiso Kant [01:06:05]: Oh, 100%, and we are gonna be doing this as well. And still it takes time and effort, right? Because you’re working with people to understand like, the infra failures and like the tools they’re using and like, are they set up well. But I agree. You absolutely want to. I’m a big fan of companies like Vals and Artificial Analysis and like others that are doing this stuff.

Swyx [01:06:21]: I found it very nice. You’re the first to bring it up.

Eiso Kant [01:06:22]: Yeah. I think they’re great. They’ve got like. I loved like a lot of the work they’ve done and put out. and so, and there’s, I think, many more, and please create more eval companies. Like create more evals. I think it’s so valuable for the industry.

Swyx [01:06:34]: It’s an actual monopoly I feel like. Oh, and duopoly maybe.

Eiso Kant [01:06:37]: I think it can be broken.

Swyx [01:06:39]: Yeah.

Eiso Kant [01:06:40]: Because I think it can be broken really easily because creating an eval for many people isn’t sexy work, but whoever does it, everyone is happy to get a good eval. You’ve like if an eval is well constructed, everyone’s celebrating it, and everyone’s willing to pay for it, and everyone’s willing, like the foundation model

Swyx [01:06:55]: Oh, yeah. I think creating eval, yes. But like in terms of being like we are the industry standard ones that will

Eiso Kant [01:07:01]: Yeah

Swyx [01:07:01]: Τ-bench and make sure that you didn’t, you didn’t cheat

Eiso Kant [01:07:03]: Yeah, that’s true

Swyx [01:07:03]: And I’ll run it the same way that you run it versus your competitor run it.

Eiso Kant [01:07:05]: Yeah. That is very true, and we need that. And it’s nice that’s like a few standard places that we all have to like, adhere to. It keeps us all honest. I think that’s super important to do so, And, but yeah, no, I think our goal is to build the world’s most capable models. and right now we are focused on the coding agent capabilities, long horizon work. But what you see with that is that you get a lot for free. I’ve always said it’s a lot easier for us as we get to SOTA and frontier on coding to then say, “Okay, now we’re going to obsess in using the model factory to add more data for places that, we’re not as strong on,” like could be medical or legal or any other areas. and similarly, I think what we see, and we see this with reasoning models a lot, if you give models access to the right knowledge sources and they have capable ways of reasoning, they’re able to go very well into domains that are less known to them or even seen less in their training data. So, but yeah. Are we a agent like model plus harness comp-? No, we’re a model company. but I think models today cannot be trained without harnesses. It’s not possible. So it is just like where before it was just the weights in the container, well, now there’s an agent harness that’s attached to it. and but I think there’s a big difference in being an agent harness as a model company than someone who’s truly building an agent company. I think they can do far more than we can.

Swyx [01:08:27]: Yeah. understood. Yeah. I think that is my minor pushback. If you are truly identified as a model company, then make the best model for OpenCode, right? Instead of for pool or whatever. I think that’s not as, that’s, that’s minor compared to if the goal is AGI, make the best model for Hermes.

Swyx [01:08:45]: Right? Like just ‘cause that is the next stage after coding.

Eiso Kant [01:08:48]: I’look, and we’re working like very closely with them

Swyx [01:08:52]: Yeah

Eiso Kant [01:08:52]: Because I do think like it’s, and, you have to care, you have to invest in it. It’s why we do the polishing and we spend time on it. and I think over time, yeah, you’re, you’re right that you wanna balance that out. but ultimately you just want general capabilities that everything works equally in every harness.

Swyx [01:09:10]: Just on the topic, do you guys do much with like Hermes, OpenAI Codex, NanoCodex, whatever? Pi?

Swyx [01:09:16]: Pi.

Eiso Kant [01:09:17]: Pi.

Swyx [01:09:17]: No, Pi is different.

Eiso Kant [01:09:18]: It’s more coding.

Swyx [01:09:19]: Yeah.

Eiso Kant [01:09:19]: I’m a big fan of Pi, though, I have to say. I think it’s a really sexy

Swyx [01:09:22]: I forgot to mention Pi.

Eiso Kant [01:09:23]: Yeah.

Swyx [01:09:23]: Pi, you sound closest to Pi in terms-- pool and Pi in terms of like the minimal surface

Eiso Kant [01:09:28]: In the minimal yeah.

Swyx [01:09:29]: Yeah.

Eiso Kant [01:09:29]: It’s because I don’- I have a. Allow me for one more strong opinion.

Swyx [01:09:33]: Yeah.

Eiso Kant [01:09:34]: I’ve been saying this now for two years.

Eiso Kant [01:09:37]: I think MCP and tools are stupid.

Swyx [01:09:41]: Ooh. Let’s go.

Swyx [01:09:42]: You support MCP.

Eiso Kant [01:09:43]: I support MCP and we support tools and everything. They make absolutely no sense to me.

Eiso Kant [01:09:48]: And like, and I’ll explain a little bit why and I think I can probably get people to come along on this one.

Eiso Kant [01:09:56]: If you are looking for complex tasks, increasingly longer horizon, increasingly complex tasks, doesn’t matter if it’s coding or something else, You are gonna be interacting with data sources, right? And you’re gonna be interacting with things that are installed on some form of a virtual machine.

Eiso Kant [01:10:15]: And what we are doing is that we’re putting a layer in between those things. We’re putting like MCP in between, we’re putting tool calls in between, and this is even more about tool calls than MCP, where the model can just write the code and interact with the system. And we’re starting to see that. Like Laguna S does this a lot. You’ll see this as well in like frontier models. They’re increasingly no longer, “Here we’re gonna stuff 50 tools in the like system prompt,” to “No, here’s a virtual machine with these binaries installed, this code base you can operate in. Here, a folder where you can write, your memory if you want to.” And the model is using code to do complex asks. And when it uses code, it is not one or two tool calls or three things that are chained together. It starts, using if statements and for loops and making things conditional. And so I think we’re moving from, we already are moving from tool calls, to effectively models writing code, little scripts, and you see this a lot when you get the Python,

Swyx [01:11:15]: Code interpreter.

Eiso Kant [01:11:16]: Exactly. Like in just the arrow in, written code in the file. I don’t know what you call

Swyx [01:11:21]: EOF? Yeah.

Eiso Kant [01:11:22]: Yeah, exactly. Like, you already see this happening more in models because when you start training them in RL, the models wanna be free. They wanna be able to do the thing they wanna do in the most efficient possible way, and it is not calling one of the 50 tools in their like system prompt. And so I’m a very big fan of Give the model a minimal harness, as minimal as possible, give it a container in which it has its own code base, right? The, got a models code base that has access to the API keys and data sources and little libraries and documentation that it needs, and just let it run free at the task. and I think that is the way we’re going. I think we will, in 12 months, not see a single system prompt that is stuffed with 20 or 30 or 40 tools anymore.

Swyx [01:12:07]: No comment. no pushback there. I think there will be, it’ll be supported for a long time just because that’s, a lot of people are trained on that now, but maybe you guys don’t have to support it in your models, going forward. So, but yeah, I mean, if you can. I do think that’s, writing code is more generalist and it’s a, it’s a means to an end

Eiso Kant [01:12:26]: And we do support tools.

Swyx [01:12:27]: Yeah.

Eiso Kant [01:12:27]: We support. And this is the first model we’re doing parallel tool calling in which we needed to catch up on. So like that’s there and like

Swyx [01:12:32]: Yeah

Eiso Kant [01:12:32]: So it’s, it’s there, but I,

Swyx [01:12:35]: Yeah

Eiso Kant [01:12:35]: It’s a personal, nitpick. I like, I want the models to have as many degrees of freedom and just like, be free and do capable things.

Swyx [01:12:43]: Yeah. So and then, so that was on the path towards like, okay, how do you use Poolsides models and Laguna models for my Hermes or my OpenAI Codex

Eiso Kant [01:12:52]: Yeah

Swyx [01:12:52]: On all those things. And so typically what I look for is, Computer use or vision. That’s a, that’s a very big one. You guys have a blog post on that. but then also the persistence I think is very strong value, as well as long context, which you guys have a million token context. Anything else?

Eiso Kant [01:13:08]: So for us, look, so for us, vision understanding is the next thing, right?

Swyx [01:13:11]: Yeah.

Eiso Kant [01:13:11]: Like we don’t have vision understanding.

Swyx [01:13:12]: Which I was gonna say is

Eiso Kant [01:13:14]: We don’t have vision understanding in these models yet.

Swyx [01:13:16]: Yeah.

Swyx [01:13:17]: To

Eiso Kant [01:13:17]: And so this is something that we’ve, we’ve started efforts on. Like we think it’s, it’s super important to have visual understanding.

Swyx [01:13:23]: That’s company vision.

Eiso Kant [01:13:24]: And so no, we’ve got work to do there. and this is one of the things I loved about the Thinky model, like from the Two minutes I scrolled the blog post

Swyx [01:13:33]: Yep

Eiso Kant [01:13:33]: Multi, the multi

Swyx [01:13:34]: They’re, they’re very committed to multimodal, including audio. Yeah.

Vibhu [01:13:36]: They’re state-art audio, as much as it’s a trillion parameter state-art audio, but also all trained from scratch, right?

Swyx [01:13:43]: Yeah.

Vibhu [01:13:43]: No encoder in the sense

Swyx [01:13:45]: To me, that’s, that’s, that’s one of the strongest reasons why you need to train from scratch, is you just have a different tokenizer, you’d have different

Eiso Kant [01:13:51]: I’m fully aligned, like zero disagreement from me here. Like, just add the modality and don’t put. keep it simple. we’I don’t think we’ll touch audio for a very long time.

Vibhu [01:14:05]: It’s in the name too, InkLink Inc.

Eiso Kant [01:14:08]: True.

Swyx [01:14:08]: Yeah.

Swyx [01:14:09]: I mean, what’s so hard, what’s so hard about audio?

Eiso Kant [01:14:11]: It’s not about what’s Again, it all comes down to focus.

Swyx [01:14:14]: I see.

Eiso Kant [01:14:15]: Right? Like saying no to things means that there’s a research or an compute that can go to making general progress, and our view is like general progress, is going to come from the ability to push these models to far more capable reasoning, far more longer horizon tasks. I don’t think audio Adds to that. I don’t think it pushes us close to AGI. I think it is a necessary modality as you get closer to AGI. I think visual understanding sits in the middle of those things. I think visual understanding can absolutely, do so, but it also unlocks capabilities that are just valuable today. so but this is the point, right? You want more diversity, you want more different foundation model companies who focus on different things. I think we are just like a horse with blinders on, just like

Swyx [01:14:58]: Yeah, you have your path

Eiso Kant [01:14:59]: We have our path, we wanna catch up to the frontier, and, we don’t wanna distract ourselves with anything else.

Swyx [01:15:05]: Yeah.

Swyx [01:15:06]: I will call out that one of the branches of research is DeepSeek OCR, which is can you just throw away the text tokenizer and just have only vision?

Eiso Kant [01:15:13]: I find this-- I look, geek, the geek in me is like looks at this stuff and it’s like, okay, look at this, like look at the number of bits encode

Swyx [01:15:20]: But they’re right.

Eiso Kant [01:15:21]: I think it’s super cool, right? But I think this is what we’re gonna come back down to. Like probably works, it’s just is it compute efficient enough? Is it Like I think so many of these things ultimately will work. It’s just like, what’s the nice thing about text? And I referenced earlier, Peng Ming and Nikolai are my two heads of applied research who are just incredible, like we wouldn’t have gotten here without them and the entire team.

Eiso Kant [01:15:45]: And Nikolai have-- and I have been debating, for years about like, should reasoning be in latent space? Should reasoning be in tokens? But one thing that I think him and I really agree on, and all three of us, and is that like Language is incredible because it’s such an incredibly dense way to encode knowledge and information and intelligence, right? If you think about like what went into a physics paper that then is, 20 or 30 pages, like the amount of intelligence and thought and whatnot to then generate that, like in that 20-page document, like those little amount of bits, there’s so much encoded. And other modalities like video and images are amazing, but they don’t have the same density of like knowledge or reasoning or however, like the things that we’re trying to push for that are encoded in that modality. They’re there. In many cases, you can watch an incredible lecture for, 50 minutes on YouTube, but the amount-- and but if you treat that as video in data versus text data, right, the bits to like signal-noise ratio, the compute efficiency of the modality is a lot less. And so we have this view as like with language you can go really far, but also when you have limited compute, limited, people, and they’re very much linked to two, I think we can push language. It’s the more, it’s the better investment. But I want all the modalities. I find it super cool and I love what DeepSeek and others are trying. Like I can retweet them all the time, but internally we’re just like, “Let’s stay focused.”

Vibhu [01:17:17]: Which I’ll say, you can see somewhat works looking at Anthropic. OpenAI has a lot of vision, multimodality. Anthropic just didn’t, right? Fable’s a big step up in image processing, but like they’re not known as the multimodal company, right? They’re the language model coding company that has multimodal capabilities that’s never super flex and, goes pretty far.

Eiso Kant [01:17:42]: I look, I in this I think Anthropic, I mean, they’ve done many things right, but I think this maniacal focus on just pushing capabilities, scaling up models is. I couldn’t agree more. I think it’s, it’- that’s the first hurdle, and once we get that, then we can improve a whole bunch of other things. and but at the same time, on the other end of the spectrum, it’s really exciting to see people, building these spatial models, right? That are, and the world models that are being built, like for very different, use cases. but I think ultimately it all comes together at some point.

Vibhu [01:18:19]: Okay. So scaling models, this is Laguna S for small.

Eiso Kant [01:18:23]: Yes.

Vibhu [01:18:23]: You have good naming, extra small, medium, large.

Eiso Kant [01:18:26]: Yeah.

Vibhu [01:18:26]: Still scaling?

Eiso Kant [01:18:28]: So the new medium started training, and it’s much bigger than the last medium, started training yesterday. so it’s a, 39-day training run. and,

Vibhu [01:18:39]: How do the days and events? Just the compute model

Eiso Kant [01:18:41]: Models factory.

Vibhu [01:18:42]: Okay.

Eiso Kant [01:18:42]: Right? And like at this point, like with the model factory, like it’

Vibhu [01:18:46]: I thought it was interesting. So in the Laguna medium and extra small, you even quoted number of GPU hours for how many days and whatever for different size. And I’m like, “Oh, you can also work backwards to how much that costs, right? What GPUs, how many hours “

Eiso Kant [01:18:59]: And you realize it’s not a lot.

Vibhu [01:19:00]: No, it’s not.

Eiso Kant [01:19:01]: It’s not a lot of money. and, you started with DeepSeek of the West and, I think that’s, The DeepSeek moment, right, was a moment when people realized that you can train incredibly capable models for not a lot of money on the training run. But I think that’s the false

... [TRUNCATED]