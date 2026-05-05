---
title: "Building AI Safely"
url: "https://ashvardanian.com/posts/building-ai-safely/"
fetched_at: 2026-05-05T07:01:52.089949+00:00
source: "Ash Vardanyan"
tags: [blog, raw]
---

# Building AI Safely

Source: https://ashvardanian.com/posts/building-ai-safely/

In 2018 – three years after leaving physics to focus on high-performance AI infrastructure (
project Unum
) – I gave the interview below during a
LessWrong
meetup on the
ITMO University
campus in St. Petersburg, Russia, arguably the strongest Computer Science department in the world.
The recording was later posted on
VKontakte
.
To preserve the conversation and reflect on it in the future, I’ve run it through automatic translation and posted it here, with some notes in the end on
how the ideas have aged through 2025
.
Intro
#
From 2-5 August 2018, Prague hosted the
Human-Aligned AI Summer School
, gathering researchers to discuss the safe development of machine learning systems.
Before the event, a representative of the Russian
Effective Altruism society
sat down with me to talk about AI Safety,
Reinforcement Learning
, and the state of the field.
The Less Wrong Interview, 2018
#
Current Work
#
Interviewer: What are you currently working on?
I am developing a framework for high-performance computing in ML tasks.
There are many machine learning (ML) libraries available for open use and for rapid prototyping of various neural networks on the fly.
However, I am building a highly optimized system for specific tasks.
For these tasks, my code runs 10 times faster than Facebook’s or Microsoft’s libraries.
This shouldn’t be surprising.
When creating a public product, you are forced to maintain backward compatibility.
This ensures that users of an old version of your product can update to a new one without changing their existing work.
But this also limits you, preventing revolutionary changes to the old version.
My code, on the other hand, is like a living organism – all cells regenerate.
Over the past 2.5 years, the project has undergone five to six rewrites.
The design continuously improves, and there is no need to worry about compatibility.
Motivation for Prague
#
Interviewer: Why did you decide to go to Prague?
Firstly, it conveniently coincided with another trip.
I did not have a specific mission to attend an AI safety conference.
I am not afraid of a strong AI that will come and enslave everyone; a weaker mind cannot comprehend the thoughts of a stronger one.
If strong AI becomes significantly smarter than humans (which is likely), then we won’t even be able to imagine what it is capable of, and discussing it would be pointless.
I am more concerned about powerful ML models – let’s call them weak AI.
A small paranoid lives within each of us.
My paranoia fears that organizations will use weak AI to solve their problems more effectively.
Everyone’s problems sound different, but essentially, they aim to increase their power:
States want more control over their citizens and dominance over other countries.
Religion wants more adherents and control over them.
Businesses want to maximize their profits. To achieve this, they need either to raise prices or increase the number of clients by pushing competitors out of the market.
This can manifest in any way imaginable: advertising, blackmail, speculation – you choose.
Moreover, harm can be inflicted unintentionally.
Machine Learning Abuse
#
Interviewer:
Is that [ML abuse] already happening?
It isn’t easy to define ML.
I would call it a branch of statistics or statistics on steroids, depending on how you look at it.
You collect information about the workings of the surrounding world and then use the results of that analysis to make predictions.
Our consciousness probably works similarly.
A huge problem that few people talk about is that any statistics you accumulate have a limited scope of application.
In the world around us, not all quantities can be described by a uniform distribution.
However, many adhere to a
Gaussian distribution
.
In such a distribution, a small proportion of examples will be at the extremes, but these are often the important ones.
Any ML model will struggle to predict its target function for data points falling into the tails of the distribution – for unusual input data.
This is neither good nor bad; it is a fact.
To overcome these problems, a significant amount of high-quality data is required.
Some corporations possess this.
But that’s not all.
Business is not as categorical and demanding as science.
In science, the best solution wins, but everything requires proof.
In business, people often make compromises.
Even if a more optimal model emerges that yields similar average results for the business, the new solution might not be implemented.
A manager writes a task, an analyst creates a model, a programmer writes a library, and a system administrator configures a cluster.
But none of them have any idea how it all works together.
It’s difficult to say where and what might go wrong.
But ultimately, everyone will suffer.
We have to start from scratch.
This sounds entirely unrealistic for most AI specialists.
The greatest foolishness is to do the same thing over and over again and expect a different result.
Albert Einstein
Most ML consists of complex and multi-layered models that conceal a significant amount of logic.
As a result, even programmers poorly understand what is happening inside.
From a historical perspective, it looks like this:
New industries emerge, and enthusiasts are the first to flock to them.
This was the case with computers about 40 years ago: only geeks understood them.
Pioneers are often individuals with exceptional intelligence, knowledge, and other metrics that differ significantly from those of the general population.
They build the foundation for the entire industry, attracting the attention of forward-looking organizations.
The industry matures, with many people already involved.
They are distributed by skill level according to a Gaussian curve.
Artificial intelligence (AI) has been a significant field for approximately 5 years.
Many programmers do not understand how their models work.
Products released by large companies only exacerbate the situation, as they greatly simplify the implementation of neural networks and lower the barrier to entry.
Now, anyone can download a library (
TensorFlow
,
Caffe
,
Torch
) and start experimenting.
This approach is characteristic of Western culture – it’s playful.
You can play with something before you use it.
I prefer the Soviet approach: before you start doing anything, you must thoroughly understand what you are doing and what your responsibilities are.
This process is more complex and tedious, but it significantly safeguards against risks.
What should be done with an intern at a nuclear power plant?
Can they be allowed to play with all the buttons and react spontaneously?
No.
AI is an even more powerful tool than nuclear energy.
It is so much more powerful that we cannot even grasp its potential.
Therefore, it is better to have a high barrier to entry than to take on high risks.
Oversight and Regulation
#
Interviewer:
Is it possible that someone has already created a strong AI, and we don’t know about it?
If a full-fledged AI had emerged, we would all know about it.
Alternatively, no one would know, including its creator.
The scenario where someone developed it and only they know is unlikely.
Either no one knows, or suddenly everyone does.
I am not afraid of a computer that passes the Turing test.
I am scared of a computer that intentionally fails it.
(Unknown quote)
Interviewer:
There are two main scenarios with AI:
AI is initially designed with a destructive purpose and goes out of control,
AI is initially designed for a positive task, but in the process of executing it, it chooses a destructive method to achieve the goal.
Which of these is most likely?
Again, if we’re talking about strong AI, guessing its plans is pointless.
It’s like hoping a worm can understand human thoughts.
Interviewer:
Have you read
Nick Bostrom’s book “Superintelligence”
?
I hardly read any fiction; mostly, I read scientific articles.
Interviewer:
Okay.
There’s an article on this topic called
“Concrete Problems in AI Safety.”
It discusses several issues, for example, how adding a few pixels can drastically change model results.
What are your thoughts on this?
Yes, there’s a whole class of models called
Generative Adversarial Networks (GANs)
.
These are typically
Convolutional Neural Networks (CNNs)
used for image and video analysis.
They are pretty effective at addressing such problems.
Two neural networks are trained: one solves the original task, and the second tries to hinder it.
You can always find something to nitpick.
When one problem surfaces, a solution soon appears.
Usually, it just treats the symptoms rather than curing the disease.
Modern ML models are often multi-layered.
Even if each layer individually cannot significantly distort the signal, the entire network can change it beyond recognition.
Small changes in input data can cause significant changes in output data.
Previously, ML primarily used very primitive classifiers based on linear algebra, which rarely produced significant jumps with minor changes.
However, we now use neural networks, and between layers of neurons, we employ nonlinear operations.
These make it much easier to approximate complex distributions.
Interviewer:
So, previously, programs were easier to understand but solved simpler problems?
Yes.
Deep Neural Networks have been the primary tool in the ML world for the past 5 years.
And we encountered what you described above.
The task became more complicated.
We need to counter pixel attacks.
And we added another layer of complexity.
Now, we have many concepts: regularization, dropout…
It works more accurately.
This is a classic evolutionary scenario for development.
Cars with internal combustion engines (ICE) have not fundamentally changed in quality over the last 50 years.
They have become much more complex and fragile, yet more efficient compared to older models.
Instead of complicating ICEs for decades, we could switch to electric vehicles.
I prefer that approach.
Interviewer:
I mentioned Bostrom’s book because, after its release, attention to AI safety increased.
Elon Musk read it.
In 2015, hundreds of scientists signed an open letter calling for a more serious study of AI safety.
He is a very knowledgeable person, but one should never mindlessly duplicate another person’s opinions.
I do not personally share his concerns on this topic.
I doubt that creating additional AI oversight organizations will be of any help.
Bureaucracy has not saved anyone yet.
Any scientist and inventor thinks about the future application of their technologies and the greater good.
However, regulatory bodies are not always prudent.
History records numerous instances where authorities have used scientists’ developments against their will.
Many entrepreneurs, including Mark Zuckerberg and Sergey Brin, are much more positive about AI.
Google acquired DeepMind several years ago – one of the most sensational AI companies.
They have achieved great success with Reinforcement Learning.
This is a promising approach, as it implies continuous learning and improvement.
Future Plans
#
Interviewer:
What do you plan to do in the field of AI safety?
This field is attracting considerable attention today.
I would continue to work on AI itself.
The best thing I can do to advance safety is to encourage everyone to take on tedious and complex tasks.
Only hard work provides deep understanding.
This path will require a significant amount of time and effort.
In the end, only the best will see it through.
This may sound unpleasant to most, but ultimately, we will all benefit from it.
Every person on Earth now lives better than kings did 400 years ago.
And all of this is thanks to scientific and technological progress.
As long as people are willing to sit over code day and night or solve equations in notebooks, we will be fine!
Reflections, 2025
#
This section was added on June 16, 2025.
On AI Scaling
#
Parameter counts jumped from billions to trillions, validating the “more data, more compute, more parameters” mantra.
Sparsity, my favorite topic in applied numerics, became a hot topic… but the industry is still stuck on half-measures – like Mixture-of-Experts (MoE) models.
I hope to see MoE models superseded by proper sparsity.
On AI Infra Software
#
Capital is finally flowing into better AI infrastructure – both bits and atoms.
PyTorch has replaced Caffe, Google’s TensorFlow, Amazon’s MXNet, and other major frameworks for training mainstream architectures.
New open-source projects cover almost every alternative design:
Modular
by Chris Lattner is working on Mojo, a new Python-esque programming language tailored for High-Performance Computing (HPC) and AI.
TinyCorp
by George Hotz is building TinyGrad, a minimalist compiler for AI model Directed Acyclic computational Graphs (DAGs).
LLM.c
and
LLAMA.cpp
by Andrey Karpathy and Georgi Gerganov, respectively, efficiently reimplement models in C and C++ from scratch.
The inference space is more fragmented, with frameworks such as ONNX, Nvidia’s TensorRT, and Apple’s CoreML tailored to individual hardware vendors.
Few companies work on the surrounding software stack, such as Storage, Search, and Networking, where Unum operates.
On AI Infra Hardware
#
Just like with software, the influx of capital attracted many new players to the AI hardware space.
Many came from the cryptocurrency industry, pivoting from crypto-mining
ASICs
to AI inference accelerators.
Training often requires more work and more expertise in interconnects.
The current headliners are:
Nvidia’s Graphics Processing Units (GPUs).
Google’s Tensor Processing Units (TPUs).
Cerebras’s Wafer-Scale Engine (WSE).
Groq’s Language Processing Unit (LPU).
Graphcore and other companies we’ve partnered with over the years have seemingly fallen behind
.
AMD and Intel are struggling to catch up with Nvidia, primarily earning revenue from CPU sales and investing in GPUs.
All CPU and GPU-like vendors integrate “AI accelerators” into their products, which is just a marketing term for adding matrix multiplication SIMD Assembly instructions, similar to the ones used in
StringZilla
,
SimSIMD
, and other libraries of mine.
Compilers still struggle to generate efficient code for those platforms, and the fight for AI Researchers and HPC Engineering talent is fierce.
Individual Contributors (ICs) are rejecting multi-million-dollar offers from large companies, preferring to work on startups and, sometimes, public-good, open-source projects 😉
On AI Future
#
I’ve almost instantly lost interest in RL as a whole.
The industry, however, found broader applications for it, focusing on
“Reinforcement Learning from Human Feedback”
(RLHF) hybrid fine-tuning of large language models.
I’m not a fan of RLHF and Auto-regressive Language Models either, and I hope to see those models replaced soon.
Unfortunately, people associate “AI Memory” with
“Retrieval-Augmented Generation”
(RAG) and “Vector Databases”, even though I’ve ended up being one of the biggest benefactors of the RAG hype around
Unum’s USearch Vector Search engine
.
There is more to “AI Memory” than people think, and I’m still betting the next few years of my life on it.
