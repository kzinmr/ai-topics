---
title: "The sample efficiency black hole"
url: "https://www.dwarkesh.com/p/the-sample-efficiency-black-hole"
fetched_at: 2026-06-09T07:01:21.666318+00:00
source: "dwarkesh.com"
tags: [blog, raw]
---

# The sample efficiency black hole

Source: https://www.dwarkesh.com/p/the-sample-efficiency-black-hole

One definition of intelligence is sample efficiency - that is to say, how much data do you need to see in a given domain in order to operate fluently and competently. It’s not clear that we’ve actually made much progress on training sample efficiency over the last few years - it seems like more so we’ve dramatically widened and improved the data distribution.
The main way that AIs have been getting better is from adding
more and better data
, and scaling the compute to develop that data in the first place. Obviously RL is the main way that has happened. You can think of RL as a kind of synthetic data generation - you dump a lot of compute against a verifier in order to find the “good” data. Then you train your model to predict these correct rollouts, much in the same way that you might train it to predict the next word in internet text.
For this process to work, the model must have at least prior some probability to anticipate the correct solution, which is why you also need mind-stretching amounts of human expert trajectories in every single field and skill you want the model to be competent at.
It’s hard to overstate how task specific and bespoke this human expert data is. If you want to get some intuition, go read some job descriptions at
Mercor
or Surge’s websites. There are listings for a
word specialists
who will convert legacy documents into polished Word files, and
legal experts
who will write realistic M&A diligences or securities filings, and
management consultants
who will write up template market research, and dozens more other particular categories.
And it is not only that the data have to be so domain specific, but there has to be so much of it! Each skill corresponds to at least hundreds of human experts who are generating example completions, writing rubrics, and explaining their chain of thought. There’s a reason that the data industry producing these expert labels (and the RL environments in which their meticulously catalogued skills can congeal) is earning billions a year in revenue, soon deca-billions.
Imagine if it took a couple decades worth of courses with hundreds of concurrent professors and millions of practice tasks for you to learn how to polish a word file. Even the task count difference understates the gap - the models have to grind their far more numerous tasks each far harder. Whereas a human student might practice a textbook problem once or twice, GRPO has the model generate hundreds to thousands of rollouts per task. We are building some Frankenstein’s monster, with a billion grafts of carefully constructed examples sewn together.
Epoch recently reported that
open models only lag state-of-the-art closed models by 4 months
. I think the reason it is relatively easy for open source and previous laggards to catch up to within months of the frontier is that data is the real driver of progress. And data can be easily distilled from public APIs, whereas hyper-parameters and training tricks and architectural micro-optimizations cannot - if the latter were driving most of progress, then catching up would be harder than we are observing it to be.
It is easy to forget how much data these models are trained on, and how much more it is than what we humans see in our lifetimes. We see these AIs as a galaxy glittering with capabilities, but at their center, invisible to the naked eye, holding all the constellations together, is an unimaginably massive black hole of data.
If a person hears and sees on average ~2,000 words an hour, then from birth to adulthood, they’ll see ~200 millions tokens. By contrast, frontier models are trained on somewhere between 10s to 100s of trillions of tokens. That is close to a million fold difference.
A person can learn to teleoperate any random humanoid or robot arm within hours. The reason robotics isn’t already a deca-trillion dollar industry, with a endless army of Unitree G1s doing all kinds of useful work in world, is that our AIs learn so much less efficiently than humans, and even the millions of hours of demonstrations we’ve collected is not enough to allow them to perform complex, open ended tasks.
A teenager can learn to drive a car with about 20 hours of practice. Even if you include their ~16 years of accumulated physical intuition as relevant training data, that is at least 3-4 orders of magnitude less than the amount of data Waymo and Tesla have needed to train their self-driving car models.
I wanna deal with some common objections to this kind of comparison:
Many billions of years of evolution is our pre-training, so it’s unfair to compare how little data we see simply within our lifetime to what these cold-started LLMs have to learn from.
Our genome is 3GB, about 1-2% protein coding. That is just not enough space to store the model parameters that are supposedly pretrained (frontier models are terabytes sized). The closer analogy is probably that evolution has found the right hyperparameters and loss functions (Sidenote: I had an interesting
podcast with Adam Marblestone
where he argued that the loss functions were the more significant find from evolution), but that the equivalent of parameter training is still happening within lifetime, and is encoded in the map of neural connections in the brain built up over a lifetime.
Even if it were the case that we can explain away the trillions of tokens required to pretrain a base model as catching up to evolution, it doesn’t explain why the marginal capabilities take so much data - once you have been educated, you don’t need 100 different professors to learn a new programming language, but the AIs (even once pretrained) do.
These comparisons are not including the multimodal data we see in our lifetimes. If you include all this sensory information, we’re probably in the 10s to 100s of billions of tokens range from birth to adulthood
Blind/deaf people who are cut off from this kind of sensory information might lack faculty with the relevant sense, but still have the same general intelligence as everyone else. Which suggests that all these billions of sensory tokens are not really the thing making humans smart.
In fact, deaf people who can only communicate via sign language and reading (and not from hearing) are ingesting far less than the 200 million language tokens we calculated earlier, and even this is sufficient for them to be fully general intelligences.
Scaling laws tell us that bigger models are more sample efficient. The human brain is 100T synapses - if each synapse is ~1 parameter, and frontier models are currently roughly ~5T parameters, then maybe we could achieve human-level sample efficiency with another order of magnitude or two of parameter scaling.
The way the scaling law equations work is that parameter and data terms are added to the loss independently. If you have a model that is trained compute optimally, and suppose you ask, well what if I just wanna maximize sample efficiency and use less data - and I’ll throw in as many parameters as it takes to make that happen. With the constants from the Chinchilla scaling laws paper (and the nature of the result wouldn’t change even with different constants), even if you increased the number of parameters by infinity, that would only decrease by a factor of ~10 the amount of data you need in order to keep the same loss. Humans are somewhere between thousands to millions of times more sample efficient than these models. Scaling of current models simply can’t make up for that discrepancy. This really does suggest that humans are on a different scaling curve altogether.
But you might ask, why does sample efficiency matter? The labs have two overarching objectives: automate white collar work, and automate AI research itself. Is human level sample efficiency necessary for either?
The bet with white collar work is the common tasks that a software engineer or analyst or accountant does are, well common. And we can bring common tasks into distribution quite easily through RL and SFT. The
revenue curves
of these AI labs suggest that there is enormous value from bringing tasks into distribution, even if we don’t replicate human sample efficiency.
Yes it is far more inefficient to train AIs to do these tasks than it is to train humans. But so what? Human lifespan does not allow for the quantity and breath of training these models experience. If you as a human had some weird learning disability where you needed to read through every public repository on Github before you could be a competent developer, it would not make sense to train you up. You’d be on Social Security by the early stages of your education, and even once you were trained, you could work on only one project at a time. But AIs can learn these skills by firehosing gigawatts of training at a time. And what they learn can be amortized across billions of sessions, so we can be ludicrously inefficient in training them and still be wildly in the green.
How much “out-of-distribution” thinking do white collar employees need to do that you simply can’t train for in advance? Well this is more a question about the nature of different jobs rather than a question about AI research. And also depends on the job - some jobs are mechanical and predictable enough that they were automated long before the modern era of AI, for example bank tellers or travel agents. And there are other jobs which require dealing on a daily basis with problems that are quite distant from the data distribution. Even software engineering (the jobs AIs are supposed to take first) is one such. I would be willing to bet that there’s overall more demand for human software engineers in 2028 than there is now, largely due to the complementary input of AI.
The labs’ plan for these later kinds of jobs is to first automate AI research, and then have the automated AI researchers solve this sample efficiency problem. So then the question is, can AIs, which do not have human-level sample efficiency, nonetheless solve the remaining research problems on the way to human-like intelligence and learning.
That question I’ll address in a future blog post - I think the way that people currently think about an intelligence explosion is pretty clumsy. Either people dismiss the possibility of AIs speeding up AI progress altogether, or they just assume that God pops out the other end. People are not reasoning about what extremely rapid progress, but starting with LLMs, looks like.
