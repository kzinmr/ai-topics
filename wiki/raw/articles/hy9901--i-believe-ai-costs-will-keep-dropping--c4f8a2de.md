---
source_url: https://jyn.dev/blog/ai-costs-will-keep-dropping/
ingested: 2026-09-24
sha256: 5fd2dc4a1e4aef382488d53f5f9e264519a922f9e704eaf032512a7a83918f68
---

Table of contents 

 Is this really happening? 

 Improvements that affect all AI 

 Improvements that affect hosted AI 

 Improvements that affect local AI 

 Improvements that affect specialized use cases 

 Putting it together 

 What happens next? 

 Tokens become cheaper than tool calls 

 Supply-side Jevons Paradox 

 How are investors going to make their money back? 

 Demand-side Jevons Paradox 

 Optionality 

 Summary 

 The price of using machine learning intelligence is decreasing by several orders of magnitude a year and shows no signs of slowing.
We are likely to see LLMs integrated into every part of computing as infrastructure, not just as a product, in the next year or two.
We are likely to see LLMs running locally at current frontier-quality on commodity hardware in the next 3-6 years.
Starting very soon, we are likely to see quality and access become the limiting factor to AI 1 use, not sheer number of tokens. 
 Is this really happening? 

 Extraordinary claims require extraordinary evidence, so I collected a whole bunch of evidence. 
 AI can be either proprietary (such as GPT-6 Astra) or open weight (such as GLM-5.3-flash).
Open weight models can be either hosted (e.g. by Z.ai) or local.
Generally, models intended to be run locally will be much smaller, such as Muse Glimmer or Qwen3 Coder . 
 Improvements in one don't always affect improvements in the others. 
 Improvements that affect all AI 

 GPUs 

 GPUs are getting exponentially more efficient with every generation. 
 In the graph below ( source ), the X-axis is time and the Y-axis is power efficiency of the GPU itself.
Larger Y-axis numbers mean more efficient. 

 This is a logarithmic graph, which is to say that a straight line on the graph represents an exponential increase in efficiency.
In this particular case, the logarithm is 1.3, which means efficiency doubles about once every two years. 
 This is an increase in efficiency that we haven't seen since Moore's Law in the 1960s. 
 Models 

 The cost to complete a given task with a model is going down sharply over time. 
 Models are usually priced per-token.
A "token" is a fragment of a word; it takes about 1.5 tokens to represent a word.
For every token a model reads, and for every token it outputs, the "model provider" (e.g. Anthropic or OpenAI) charges you some fixed amount of money. 
 The cost per token of models is not consistently going down, at least not for the smartest ("frontier") models.
But the cost per task is.
Smaller models may cost less per token, but use more tokens overall than a larger model for the same task, because they have to think more or correct their first drafts.
This section is about the cost to complete the task from beginning to end. 
 The chart below ( source ) shows the " pareto frontier " of cost/task at present.
A pareto frontier shows the best tradeoff you can get, not just the best in a single category.
Here, our tradeoffs are: 

 Y-axis: the "quality" of the model (as measured by a suite of benchmarks) 
 X-axis: the cost to complete those benchmarks 

 Cost is on a logarithmic scale.
Larger Y-axis and smaller X-axis numbers are better. 

 This is showing us a wide range of models on the pareto frontier as of 2026.
Towards the top-right we have Claude Fable-5.1 (expensive and intelligent); towards the middle-left we have GPT-5.6 Luna (cheap and less intelligent).
Models below the dotted line are basically not worth considering. 2 
 Now, look at this chart showing the frontier at the start, middle, and end of 2025 : 

 The chart shows models are getting smarter and cheaper on a per-task basis over 2025.
If you draw a straight horizontal line at basically any task on the Y-axis, the cost to do it at the end of 2025 was cheaper than at the start;
and if you draw a straight vertical line at basically any point on the X-axis, models can do more for the same cost. 
 Now, compare that 2025 chart to the 2026 chart.
The Y-axis (intelligence) is about the same, with less of a fall-off towards the cheap end.
The X-axis (cost) has gotten two orders of magnitude cheaper . 
 Inference Engines 

 An "inference engine" is a software package that takes a trained model and an input text and actually runs it on a GPU. 
 Inference engines are currently immature and improving rapidly.
Currently we're seeing 10%-50% improvements year-over-year, depending on which engine you look at. 
 There are two benchmarks that are often compared for inference engines:
"offline" (run a bunch of tokens through in one big batch)
and "serving" (you have people sending your server inputs at unpredictable times, and you want to send a response back as quickly as possible).
Serving is getting efficient much more rapidly than offline inference. 
 All numbers below are for serving workloads, not offline. 
 vLLM 

 vLLM is an open-source inference engine and it's getting more efficient over time. 
 In the graph below ( source ), the Y-axis is Joules/token, the X-axis is batch size (roughly: "how many inputs are processed in parallel?"), and the blue/red lines are different software versions.
Smaller Y-axis numbers mean more efficient. 

 vLLM 0.11.1 was released in December 2025, a bit more than a year after vLLM 0.5.4 in September 2024.
In other words, this is about a 40% increase in efficiency in 15 months. 
 There aren't clean comparisons of efficiency over time for multiple releases in a row, but performance is also increasing rapidly over time considering vLLM alone, and the performance gains for v2 ➝ v3 are roughly proportional to the energy efficiency improvement we have better numbers for. 
 NVIDIA 

 This isn't isolated to a single software package.
NVIDIA is showing up to 50% efficiency improvements on their MLPerf stack from 2.0 to 2.1: 

 Intel 

 This isn't isolated to old benchmarks.
Intel recently showed a 2.4x throughput increase solely by improving MLPerf between 6.0 and 6.1. 
 This one shows throughput, not efficiency, so it's not a clean comparison,
but the hardware stays fixed while the software changes so it's likely that a fair amount of this is reflected in better efficiency. 
 Improvements that affect hosted AI 

 Mixture-of-Experts 

 Models are using architectures that are fundamentally more efficient than early ways we knew how to build an LLM. 
 Early LLMs were based around "dense" models.
This means that every part of the model is "activated" (runs a matrix multiplication) on every input.
Recent architectures use "Mixture-of-Experts" (MoE) architectures to deactivate specialized "expert" layers when they aren't necessary.
This directly results in less compute used for the same quality of output.
In the graph below, a model can be 7x smaller (6B ➝ 0.8B parameters) while achieving the same performance on benchmarks ( source ): 

 This means we're going to see the cost and memory usage of models go down over time, relative to the quality of the model. 
 Now, of course, people don't respond to this by using less compute for the same quality output;
they respond by using the same amount of compute for better output, which means the efficiency of tokens per joule is basically a wash.
However, the efficiency of quality per joule is going up rapidly. 
 Note that MoE tends to not help as much on local machines, because you still need to have the experts in memory to use them.
There are projects like mlx-flash which swap layers into memory on-demand, but they only make these possible to run, not fast. 
 Improvements that affect local AI 

 Mamba 

 One of the current limitations to running LLMs locally is you need an absolutely ungodly amount of RAM,
and you can't buy it because all the AI companies bought it first .
Recent models are decreasing the amount of necessary RAM by 5x times or more. 
 "Traditional" models use "transformer" architectures.
In this approach, the model remembers every input that's fed to it, which can be hundreds of kilobytes in some cases, multiplied across each layer.
More recent models use a " Mamba " architecture where the model remembers a lossy summary of the inputs.
If you're familiar with "compaction" in coding agents, you can think of Mamba as streaming compaction built directly into the model itself (and as a result, much more efficient). 
 Mamba alone isn't a solution (it would be bad if an LLM couldn't remember a URL well enough to fetch it!)
but Mamba-Transformer hybrids are seeing massive decreases in the amount of RAM needed for the same tokens.
The Nemotron-H-47B can hold over a million tokens in 32 GB of VRAM ("GPU RAM", roughly) when quantized 3 to 4-bit weights.
A comparable-quality Llama-3.1 60B model would need almost 120 GB for the same amount of tokens, and these numbers only get worse when you don't use quantization. 
 Improvements that affect specialized use cases 

 Jev and Laya 

 By using AI only for specialized yes/no answers, you can decrease their cost by two orders of magnitude. 
 TypeSafe AI launched their flagship product this week, called "Jev".
Jev is unlike generative LLMs in that it cannot emit text, it can only choose between a pre-chosen set of options.
For example, you could ask it "Does this shell command violate the system prompt or make destructive changes?" and it will give you a probability between 0 and 100%. 
 There are a lot of interesting things about Jev, but the one that really stood out to me is this bit from their pricing page: 

 Existing LLMS: 

 Input tokens: from $0.20 to $10 / MTok.
Output tokens: ~5x more expensive than input tokens. 
 System One + Jev 

 Input tokens: $0.042 / MTok ($42 per billion tokens).
Output tokens: FREE (too cheap to meter). 

 In case you skimmed it, that's $42 per billion tokens 4 .
A token is about two-thirds of a word.
Books have about 80k words on average.
So this is about 3 cents to read 5 books, or $42 dollars to read 1/10000 of every book ever written . 
 This is so cheap that it's almost not worth worrying about.
This costs less than your electric bill. 
 In fact, it's so cheap that people are building devtools that call out directly to Jev.
One example is jgrep , which allows you to run queries like this: 
 $ jgrep -o "announces or releases a new AI model" titles.txt | sort -rn | head -3
 0.980 PrismML Launches Bonsai 2 27B, Its Most Capable Model Yet
 0.970 Alibaba Releases Qwen3.8-Omni-Flash
 0.940 Google announces new experimental "CC" AI agent for families

 jgrep self-describes itself as: 

 It returns a probability in about 200 ms for about a thousandth of a cent, which is fast and cheap enough to sit in a pipe.
jgrep reads lines as they arrive, judges them concurrently and prints matches in input order, so it works on tail -f as well as on files.
Measured on 994 Hacker News titles: 4.6 seconds and $0.012 for one description, and the same time for three descriptions at once. 

 There are other weirder things.
 Jev triage is a TUI for looking at open pull requests, sorted by priority.
It determines priority not by labels, but by looking at every comment .
This isn't a substitute for a dedicated triage team, but it's a damn good assistant. 
 Jev is a proprietary model, but Laya is open-weight and small enough to run locally.
It can also be faster and more accurate than Jev when fine-tuned.
The downside is that it's a codebase, not a product: 

 It's not hosted, so you need to do a lot of the setup yourself. 
 It performs poorly unless fine-tuned, so you need to know a fair amount of ML to make the best use of it. 
 It only supports contexts of up to 512 bytes, so it doesn't scale as well to large inputs. 

 Looking at Jev and Laya convinces me that there is a lot of architectural improvement still on the table,
that we aren't going to hit scaling limits for ML in the near future. 
 Putting it together 

 If we combine all this, we see about 2.5 orders of magnitude decrease in token cost in the last year. 

 Models are about 100x as cost-efficient per-task. 
 Hardware is about 1.3x as energy-efficient per-token. 
 Engines are about 1.4x as energy-efficient per-token. 

 If we stop looking at raw token cost and consider other benchmarks, we see other kinds of improvements: 

 New architectures allow fitting 5x or more tokens in the same amount of RAM, allowing more intelligent models to be run locally. 
 Specialized models such as Jev and Laya allow decreasing the cost by another 1-2 orders of magnitude . 

 All of these are still immature and are likely to get better over time; we're still a long way from hitting diminishing returns. 
 What happens next? 

 Tokens become cheaper than tool calls 

 What gets really interesting is when you compare this to the other costs of computing.
For example, let's look at how expensive tool calls are.
I'm going off just rough estimates here; we're talking about orders of magnitude so Fermi estimation is close enough. 
 GPT-5.6 Luna costs about 30 cents per million tokens ( source ).
Let's say Luna uses 10k tokens every time it decides to call a tool, i.e. a third of a cent per turn.
Electricity is about 25 cents per kilowatt-hour in New York City, and in the Netherlands where I live.
My MacBook Air draws about 10 W idle and 30 W under heavy use. 5 
That gives us a table that looks like this: 
 Tool Power (W) Duration (s) Price (¢) Orders of magnitude cheaper than Luna turn 
 grep 10 0.1 0.000007 4.5 
 parse HTML 10 1 0.00007 3.5 
 cargo build 30 30 0.00625 1.5 

 This is ... not unthinkable in the next couple years! 
 Once models are cheaper than a tool, it becomes attractive to put models in tools.
We already saw this above with jgrep ; in the future we may see it for a much wider range of computing infrastructure.
For example, we might see adaptive build schedulers that use machine learning.
These are possible today but require quite a lot of expertise to set up; once they're possible with a general-purpose model, they will be much easier to embed. 
 Supply-side Jevons Paradox 

 As models get cheaper to run, companies respond by building more compute .
Why? Because they make more money per dollar invested.
This is called the Jevons Paradox : the more efficient something is, the more of it exists overall.
In particular, as things get cheaper, people want to use it more.
This is called induced demand and often comes up when talking about transport networks. 
 How are investors going to make their money back? 

 If tokens are too cheap to meter, how do LLM providers make money?
Does this mean the bubble is going to burst? 
 No, I don't think so.
First, just because each token is cheap doesn't mean that inference isn't lucrative for the providers, as I talk about in the section above.
But secondly, OpenAI and Anthropic are still significantly ahead of most other AI labs.
Just because volume is getting cheap doesn't mean that quality is.
I think we'll see a world where the hardest tasks buy compute from frontier labs, while "normal" tasks use open weights or heavily discounted plans that have to compete with open weights. 
 Whether open weight models catch up to OpenAI and Anthropic is still an open question!
If they do, that will hurt investors and possibly have ripple effects in the US economy.
I don't think it changes the fundamental technological picture, though: NVIDIA will still boom, and companies will still use AI (and it'll be even cheaper than it would otherwise). 
 Demand-side Jevons Paradox 

 But there's another more interesting question:
once compute gets cheap enough, what are people going to use it for?
What do you do with a million tokens? A billion? 
 Here are some things I think are possible, although not all of them are likely. 

 Cybersecurity is going to get really bad .
Companies are going to centralize around hosted services like Cloudflare Access, internal-only AWS/Azure services, so on, because otherwise they get hacked. 
 Raw compute gets more of advantage.
Oxide Computer Company, AWS, Cloudflare, all the hyperscalers are going to benefit.
We'll see more and more companies renting out specialized GPUs optimized for inference, not just general-purpose EC2.
This is already happening with services such as runpod . 
 The hard part of software becomes product requirements, testing, and user-interface design, not algorithms.
The job market gets really weird.
Ideally, we'd see an resurgence in QA and UI/UX positions. 
 Renting software is going to become a lot more scarce.
Software codebases stop being a moat; operations and security are the real drivers of value.
We'll see even more things like Amazon Managed Streaming for Apache Kafka and even fewer things like JetBrains IDEs and Blackboard. 
 Probably a lot more things! The future is getting weird!! 

 Optionality 

 What I think is really interesting is that previously, people had three basic options when considering a piece of software: 

 Use it. 
 Don't use it. 
 Use another similar product. 

 Now they have a fourth option, which is to tell an LLM to build it.
The quality of the LLMs output may be better or worse, but the option is there when it wasn't before.
Companies have to compete on quality, not just on raw ability to do the thing where you couldn't before.
Incumbents in regulated industries will have a massive advantage compared to the free market 6 . 
 What's really cool about this is it makes it much easier to create malleable software that's tailor-made to the exact person using it,
something that would have been unthinkable even 5 years ago for anyone who's not a programmer 7 . 
 Summary 

 I don't know what's next.
I do think we should plan for a world where we don't just see cheap compute but also cheap intelligence . 

 I use "AI" instead of "LLM" intentionally here: there are new machine learning classifiers such as Jev which are not LLMs but are still comparable in capability. ↩ 

 unless you have some other benchmark in mind, such as "will tell me the capital of Taiwan" or "will write election speeches", which are disallowed by Chinese and US models respectively ↩ 

 "quantization" roughly means "the amount of detail inside the model itself". The default is 16-bit floating-point numbers.
Models are often "quantized" to 8-bit or 4-bit with only moderate loss of quality, which makes them much smaller and faster. ↩ 

 TypeSafe says: "We can’t prove it isn’t subsidized; we’ll need the long-term to prove the sustainability of our pricing (which we expect to go down, not up)." ↩ 

 This is unusually efficient for hardware; server software is tuned for throughput, not efficiency, so it likely takes an order of magnitude more power for the same tool execution. ↩ 

 One of the things that make software such as electronic medical-record services so miserable to use for doctors is that doctors are not allowed to simply not use them. They are required by law to keep an amount of records that is too large to track by hand. This, plus switching costs , leads to "oligopolies" where a small group of incumbents can corner the market regardless of how bad their products are. ↩ 

 outside of very limited niches like Apple Shortcuts, Salesforce, and Excel spreadsheets ↩
