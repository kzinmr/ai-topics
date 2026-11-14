---
title: "The avalanche that hit math is coming for AI development"
url: "https://www.dwarkesh.com/p/rsi"
fetched_at: 2026-11-14T10:01:02.347294+00:00
source: "dwarkesh.com"
tags: [blog, raw]
---

# The avalanche that hit math is coming for AI development

Source: https://www.dwarkesh.com/p/rsi

Many thanks to
Max Farrens
,
Gabe Fried
, and
Thomas Larsen
for pairing with me through significant parts of writing and researching this essay.
You can watch or listen to me narrate this essay on
YouTube
,
Spotify
, and
Apple Podcasts.
If you asked me earlier this year how far away we are from superintelligence, I’d probably have said at least the better part of a decade. But over the last three months, I’ve updated my views a ton. I’ve been debating people about this question, both on and off the podcast. And I’ve been watching the progress of AI on verifiable domains and thinking about what that implies for AI research itself.
I’ve now come to the view that we’re only a couple of years away, and possibly only a couple of months away, from AIs that are as good as the best humans at AI research. I’ve also come to believe that automating AI research will compress so much progress into a single year that, soon thereafter (so by 2030, but plausibly as early as next year), we’ll have AIs that are at least as good as the best human experts in every field. I know this is a wild claim, and it’s one that I myself didn’t believe even a couple of months ago. Let me walk you through how my thinking has changed.
Before we get into more speculative arguments, I want to point out that we have a lot of evidence that AI is already dramatically speeding up further AI progress at the frontier.
For example, METR, which is an independent evaluation organization,
concluded
after three months embedded inside Anthropic that Anthropic’s overall rate of progress on well-scoped tasks is 2x what it was a year ago, and that a “majority of this acceleration today is likely attributable to Anthropic’s extensive use of AI to do R&D.”
OpenAI published a
blog post
about this in September, where they showed that the heaviest 10% of AI users among OpenAI’s researchers went from using around $1,000 a day of internal coding agents at the beginning of the summer to over $7,000 a day by the end of August.
In September, Anthropic put out a similar
post
on its own AI uplift. They reported that, as of August, Claude “leads” more than 26% of Anthropic’s AI R&D work—up from under 1% as recently as February.
When I think about how big a deal it could be if AIs automate AI research, and how soon that could happen, a really important update for me has been just seeing how quickly AI capabilities in mathematics have exploded. Current AIs are slicing through well-scoped problems in mathematics like a hot knife through butter. It was only two years ago that
I asked Dario
why LLMs aren’t able to use their vast knowledge across so many different fields in order to connect different ideas and make new discoveries. And lo and behold, here we are: In a wholly verifiable domain like mathematics, AIs are doing this search-and-match discovery to such a great extent that
hundreds of important results
(which the top mathematicians and computer scientists in the world had spent decades trying to resolve) are being churned out as side quests to
hype up future model releases
.
It’s crazy how fast we went from, in 2023, “This model can’t reliably add four-digit numbers,” to, in 2024, “This model can barely solve any problems in a high school math competition,” to, in 2025, “Oh, it can win a gold medal at the International Mathematical Olympiad,” to, earlier this year, “Wow, it’s solving open Erdős problems, but maybe just because no human has attempted to solve these particular problems, and a similar solution was already in the literature,” to, about a month ago, “Okay, it fucking
solved a Millennium Prize problem
in 88 hours.”
There’s a line in the novel
East of Eden
: “And there is one sure thing about the fall of gods: they do not fall a little; they crash and shatter.”
It’s true that progress has skewed disproportionately towards the verification-laden parts of math, like finding counterexamples (rather than coming up with new theories, say). Toby Ord posted a great essay about this recently. He
writes
, “While current AI systems are starting to automate mathematical proof, there is currently very little evidence that they can ask powerful questions or find profound new fields of mathematical enquiry.”
But another way to say the same point would be:
Current AI systems have solved a Millennium Prize problem, all without the ability to ask powerful questions or find profound new fields of mathematical inquiry.
And this ability to solve well-scoped problems is going to be an even bigger deal for machine learning research than for mathematics, broadly construed. That’s because the goal of mathematics research is not just to prove or disprove long lists of conjectures, but to extend human understanding of mathematical concepts. Coming up with the idea of topology, group theory, or the Cartesian grid matters far more than knowing exactly
how many one-unit-apart pairs you can make from n dots
. We mainly care about such abstruse questions insofar as they might elicit new mathematical theories.
But in AI research, the priorities are exactly reversed. AI labs mainly care about how any new algorithmic recipe empirically makes training more efficient or elicits smarter models. They don’t care about theory for its own sake, and all the progress we’ve made in deep learning over the last decade and a half has not required much new theory anyway. The equivalent of grinding through random conjectures would be enormously valuable in machine learning in a way that it just isn’t in mathematics.
AI research is actually surprisingly similar to the type of mathematical progress that current AIs are disproportionately good at: unlocking a ton of low-hanging fruit by applying a combination of incredible persistence and a superhuman capacity to connect ideas from lots of adjacent domains.
For example, let’s talk about the transformer architecture. My friend
Sholto Douglas
, who is an AI researcher, has a perennially half-finished blog post where he explains how you could have invented the transformer two years earlier than people actually did. Maybe this essay will get him to quit stalling and complete it, but in the meantime, I’ll summarize a bit of the discussion I had with him about the contents of that essay.
Before the
transformer paper
was published in 2017, many researchers had already identified attention as a way to better parallelize training and communicate information across longer sequences. Chris Olah, who was an active researcher then, has
said
: “At the time, my sense is that the transformer architecture was a natural combination of many ideas (attention, residual networks) which had independently been effective, taken to quite aggressive lengths.” In other words, none of the core pieces were a surprise to researchers working in the field.
So then why didn’t people invent the transformer sooner? One reason was that this new architecture was only obviously better than the state of the art once you connected half a dozen additional tweaks and innovations. And though all of these had been in the literature for years,
no one knew how to combine the puzzle pieces. Doing so required research taste, of course, but also tons and tons of small experiments.
But what I’ve just described above—persistently and intelligently matching dozens of different combinations of ideas—is exactly the kind of capability that AIs have shown themselves disproportionately skilled at in their contributions to mathematics.
This is all to say, even the transformer, which is arguably the biggest breakthrough in ML since AlexNet kicked off the deep learning revolution in 2012, is the kind of thing that Claude 7 could invent if Chris Olah asked it to try hard to get this attention thing to work better.
I want to clarify that some parts of AI research are, in fact, less verifiable than math. That’s why OpenAI hasn’t fired all of its researchers, despite having a model that can autonomously solve Millennium Prize problems. But I think AI research is verifiable enough that AIs will soon be as good at it as the best humans. Explaining why requires getting into the nitty-gritty of how AI research actually works, and because those details are interesting but technical, I’ve saved them for the Appendix—if you’re curious, just keep reading after the conclusion. But in the meantime, I’ll give you my estimate of when we get there.
If I had to pick my median year for when automated researchers will be as good as the very best human AI researchers (and assuming the labs don’t intentionally slow down), I’d guess 2028.
Why do I think AIs could get this good within two years? In every domain where we can check answers and give AIs thousands of rounds of practice—for example, competitive programming contests, or well-scoped open math problems—they’ve gone from worse than most humans to better than the best humans within a few years. And as I detail in the Appendix, AI research has those same verifiable properties.
Of course, a big part of what makes a top AI researcher like Ilya Sutskever so good can’t be directly verified—for example, his ability to bet, years in advance, on the right research direction. But as we’ve seen in math, models generalize far beyond what they were directly trained on. OpenAI’s model was obviously not trained by solving other Millennium Prize problems. It was trained on lots of less ambitious, more tractable math problems, and from those it generalized all the way to solving a problem no human had ever cracked. I’d expect the same in AI research, where the combination of thousands of rounds of practice on verifiable research tasks, plus the fact that each new generation of models is broadly smarter than the last, will make models excellent even at the parts of AI research we can’t directly check.
I want to be clear that there’s a pretty decent chance that hitting this milestone takes longer because some important part of AI research remains hard to automate. I’d guess there’s a 25% chance that it doesn’t happen until after 2032.
But I also think things could move much faster, and that we could hit this milestone in 2027. Some of the most well-informed researchers I know, people who have had a very good track record of prediction over the last few years, expect AI to beat the best humans at AI research as early as next year. And 2027 is also the straightforward implication of plugging METR’s finding—that Anthropic’s rate of AI progress has doubled in a year—into a takeoff model.
As former guest Ajeya Cotra put it in
a blog post about this report
:
If we take it at face value that AI is now nearly doubling the rate of AI capabilities progress and assume acceleration from AI is smooth, this naively implies that we would reach extreme superintelligence within a year.
The reason my median is not that soon is that I’m uncertain about how accurate this straightforward modeling is. But we should not be surprised if we get to this milestone next year, and we should be prepared for such a world.
Once AI is as good as the best humans at AI research, algorithmic progress will get radically faster. There are three important reasons why: The automated researchers will be much faster, each of them will be very smart, and there’ll be a lot more of them.
Today’s AIs already do work at about 10 times human speed.
And automated researchers would also be working around the clock, nights and weekends included. As a result, each individual automated researcher will be cramming in roughly 50x more work every calendar week than a human researcher can do.
Of course, that doesn’t mean AI progress will immediately accelerate 50x. Those automated researchers would still be bottlenecked by compute for experiments, which aren’t running any faster. So there would be diminishing returns. But even with extremely steep diminishing returns, this alone would make algorithmic progress proceed many times faster than it currently does.
And this is before we account for the fact that, in this scenario, every automated researcher will be at least as good at AI R&D as the very best humans.
My sense is that around 80% of the algorithmic progress at a given frontier lab is driven by its top 50 researchers. It’s not for nothing that Zuckerberg was willing to pay hundreds of millions of dollars to acquire the best talent in the industry. And so you get another big speedup in algorithmic progress from the fact that every single engineer and researcher in this automated company will be at the level of the very best humans in today’s frontier AI labs.
Throwing more workers at a problem isn’t always helpful. For example, a swarm of agents probably couldn’t write a great novel much faster than a single agent could. But other tasks lend themselves to parallelization: For example, look at the animation below, showing a bunch of different
Claudes working together to formalize Fermat’s Last Theorem
. This feat had thousands of modular subtasks, each of which could be completed independently and where each agent could locally check whether its work had succeeded.
AI research is closer to formalizing a theorem than to writing a novel, because there is a lot of independent modular work to do, and there are verifiable proxies for progress. That means a swarm of agents can try a thousand different approaches and see which performs best, and they can do this independently for each different part of the pipeline. AI companies are already made up of dozens of teams working independently on different parts of model development: one team improves how the pretraining data is filtered, another helps design a particular kind of synthetic RL environment, another writes a better attention kernel, and so on. In domains like this, where different streams of work can be done and checked independently, dumping in lots of persistent hill-climbing agents tends to speed up progress a lot.
Again, there will be steeply diminishing returns just from adding more parallel researchers. Anyone who has worked on a team before knows that having 100,000 collaborators doesn’t mean you go 100,000 times faster—probably not even 100 times faster. But it’s implausible that you wouldn’t be going at least a couple of times faster from having orders of magnitude more automated labor.
So the combination of faster, smarter, and more numerous automated researchers will speed up AI progress a lot. But will this pace continue, will it get even faster, or will it slow down? That question is even more important than what the initial pace actually is.
Two competing trends are relevant here. And the subsequent pace of progress will come down to which ends up being more powerful. On the one hand, because of RSI, automated researchers will continue getting faster, smarter, and more plentiful. On the other hand, AI research will be getting harder and harder, as all the easy ideas get eaten away by the swarm.
By the way, “ideas getting harder to find” is a thing that already happens. AI companies have to
quadruple their R&D compute
and
double their workforce
every single year just to maintain the same rate of progress.
If the rate at which AIs get smarter is faster than the rate at which ideas get harder to find, then we’d get something called the “software-only singularity.” In this scenario, even without increasing compute, the AI swarm rapidly makes smarter and smarter versions of itself until, within a matter of months, we end up with a superintelligence that scrapes against the physical limits of our current chips.
But if ideas get harder to find faster than RSI makes AIs better at research, we’ll end up with what I’d call a “spark.” We’d get something like three to six years of AI progress in a single year.
And then things would simmer down until we build more compute, because even the super-genius automated researchers need to run bigger experiments before they can make further breakthroughs.
If pressed, I’d give a 50% chance to the “spark” scenario and a 50% chance to the “software-only singularity.”
To be clear, though, even the “spark” scenario, where we make about four years of progress in the first year after automating AI research, would feel insane. That’s a jump as big as GPT-3.5 to GPT-6 Astra in just 12 months. To remind you of the scale of progress that this leap would compress, GPT-3.5 was able to write a passable limerick and autocomplete a trivial Python function, but was mostly a useless toy, whereas Astra can build
whole
video
games
from scratch and churn out Fields Medal–worthy mathematical contributions to such a great extent that we’re already desensitized.
In the last four years, we’ve gone from a preschooler to a savant intern. If you made another jump that big, but starting in 2027 or 2028, you’d probably get a mind that would be vastly superhuman in domains that are even slightly verifiable. For example, it’d be better than Nvidia at coming up with the next generation of AI accelerators. It would make more money than the current human versions of Citadel and Jane Street (if it had equal access to the market). If you gave it
remote access to a materials science experiment lab
, it’d be better than the rest of humanity at finding a room-temperature superconductor.
Now, at this point, you might ask: How will even a superintelligence trained within a datacenter beat human experts in domains where the basis of that human expertise is years and years of real-world experience?
The way we’re currently making AIs smarter is by RLing them on tasks that are easy to automatically grade from within a datacenter: Do the million new lines of code the AI wrote pass the unit tests? Did the AI solve more open math problems? But of course, most of the world is not like this. I made this point in a
recent essay
:
How would we train an AI to build a business? How would you make an AI that’s really good at winning court cases? Or having a profitable day trading in the markets? Or helping a candidate win an election? The rollout requires interacting with the world and cannot be recreated simply within the datacenter.
So how will superintelligence get good at this kind of stuff? Let me be clear: I don’t think we can just bake the answer to every real-world problem into the weights. Rather, my claim is that scaling up RL training will give AIs the abilities necessary to ramp quickly in new contexts, even in hard-to-verify domains like the ones mentioned above.
Getting really good at any complex task takes two things. One is domain-specific knowledge. The other is a more general set of skills—the kind that capable humans have—like being able to seek out relevant information, make a plan, push forward on it through mistakes and obstacles, keep track of what you’ve learned, and collaborate with other people.
During the intelligence explosion, automated engineers will build tens of thousands of times more RL training environments than we have currently. These will be far longer-running, higher-quality, and more open-ended, and will cover a much wider range, than today’s environments.
The AIs will learn to make their way in an unfathomable number of virtual worlds that are each to today’s video games what a Bugatti is to a horse and buggy. These games will be far more difficult, messy, sprawling, and realistic than anything ever made for human entertainment. They will require AIs to cooperate or compete with teams of other AIs over long periods of time. For example, an AI will be dropped into a thriving simulated digital economy full of millions of other AIs and told to cofound a successful company. And it’s not like this AI will be stuck just thinking about the ideal corporate structure… it’ll go through an evolutionary process that involves centuries of corporate competition to figure out the optimal organizational techniques.
The AIs will also train themselves on endless backtests of everything in the history of science and tech and politics and culture—they’ll have to predict every discovery, invention, war, election, and quarterly earnings report that has ever happened. Here’s one prediction training task: Can an AI figure out general relativity given a training corpus that includes no information beyond 1700, which is far earlier than any human was on track to discover GR? Another example: Given every single newspaper article until 1962, can the AI predict how the Cuban Missile Crisis is going to unfold?
And it’s not just the training data that these automated researchers will be improving. They will also radically improve the basic learning algorithms themselves, through breakthroughs in online learning and sample efficiency (both of which have verifiable proxies, as I discuss
in the Appendix
). In the same way that humans are much more efficient and effective at learning from data than current LLMs are, future AIs could be far beyond humans in learning efficiency.
Why do I think we’ll see lots of transfer from verifiable tasks to these more general skills? One reason is that even at one ten-thousandth of the scale of RL training that will be happening during the intelligence explosion, we’re already seeing lots of generalization. If you point Claude Code or Codex at a project it has never seen before, it knows how to orient itself, figure out how everything fits together, and then tackle an ambitious assignment.
Of course, it’s hard to measure how much models have improved at tasks that are not easily verifiable, because if we could… those tasks would be verifiable. But you can go talk to a new model and compare it to an old one. In my experience, AIs have gotten much better at things that have very little to do with code or math—for example, helping me research the abstract questions I needed to answer to write this essay.
The other big piece of evidence for transfer is human evolution. Our general-purpose mental architecture was developed by evolution, which is an optimization process with a really crude verifier: Did you pass your genes on or not? In the ancestral environment, the tasks which influenced that outcome were things like hunting, fending off predators, and keeping your standing in a tribe.
These are a tiny subset of the kinds of tasks humans are able to tackle today. Evolution did not specifically optimize us to be able to write a Pulitzer Prize–winning biography, or make advanced semiconductors, or lead nations of millions of people, or come up with a new branch of mathematics. But, in optimizing us for survival on the savanna, evolution built a general-purpose learner.
In training these AIs, we’re running a similar process, except we’re doing so deliberately, with tasks more closely related to those needed for success in today’s world. And unlike evolution, AI companies are
trying
to improve transfer during training (for example, by making sure that performance improves on difficult tasks that were held out of training). If even dumb, blind evolution can get this much transfer out of building a mind that is effective at propagating itself on the savanna, then the deliberate effort that AI companies are putting into building a flexible and general intelligence that can ramp up rapidly in any new context should advance much further.
Now, even a superintelligent learner
can’t figure out everything from inside a datacenter
. So even these AIs will need some real-world experience. But I think they’ll be able to get that experience much faster than people expect, and that they’ll beat top human experts within months of being deployed.
Honestly, one thing that’s guiding my intuition with all this stuff is that I have a lot of 20-something-year-old friends whom I’ve watched accomplish incredible things and build world-leading companies and ventures in domains they entered into with no previous experience.
History is full of super-competent young people who ran circles around the world they were dropped into. By the age of 27, Napoleon had stacked victory after victory against far larger armies from the other great powers of Europe. By 25, just two years after he got into the oil business, Rockefeller was running one of the world’s largest refineries.
Rockefeller and Napoleon needed experience, yes, but only a couple of years’ worth, not decades. Whatever was going on inside those guys’ brains, AIs should be able to replicate (or even exceed: There’s no reason to think humans are the ceiling on learning quickly from experience).
Furthermore, unlike Napoleon or Rockefeller, AIs can accumulate years of deployed context in just weeks of calendar time. For example, imagine that you wanted one of these future AIs to run a Fortune 500 company better than its current CEO. How quickly could it ramp up? Well, if you let it shadow that CEO, on its first morning, it could read every email, Slack message, and document that the company has ever produced. By the end of the first day, parallel copies of it could have interviewed every employee and major client, and cumulatively done the amount of work it would have taken a single human
months
to do, before getting merged back together. Obviously, some pieces of feedback—about how your actions impacted the quarterly earnings, say—require months of serial time. But even granting that, we should expect these future AIs to be able to get to top human performance in almost all domains within months of being deployed. That’s still 2028 or 2029 in this median scenario.
And remember, even in the spark scenario, all of this happens in just the first year or two after AI research is fully automated. Things don’t just stop there. Because even if the software progress peters out, AIs will continue to stoke the fire by helping add more compute. Even without help from AIs,
global AI compute has been growing roughly 3x a year
. And the AIs that come out of the spark will be jaggedly superhuman at
helping us continue scaling up compute
. They’d be extremely good at designing AI chips, laying out the design of a new fab, and even teleoperating robots to help build parts of fabs and datacenters.
So in the spark scenario, AI capabilities continue to improve, but because their progress is driven by building more chips, datacenters, and robots, it takes years to get to the same endpoint that the software-only singularity would have achieved in months: a superintelligence that is to us what we are to chimps.
In the next essay, I’ll walk through what I expect these minds to be like, and how I expect them to transform the world.
Earlier, I promised to explain why I think AI research is largely verifiable—so that’s where I’ll start. After that, I’ll go through what I think are the strongest objections to my arguments about RSI.
One thing I want to call out at the very top is that, because pretraining and post-training are verifiable (as I discuss below), so is progress on what is the most galling and important deficiency that AIs have relative to humans: namely, their lack of sample efficiency. If you want a neural network to gain some capability,
you have to feed it much more data
than it would take a human to learn the same thing.
But every kind of sample efficiency is measurable. You can measure how much data it takes to reach a given pretraining loss, how many tasks it takes to reach a given score in an RL environment, or even how much feedback and time within a single session it takes to reach a desired level of performance just from in-context learning.
Sample efficiency and online learning are really two sides of the same problem: how to learn from real-world data quickly and efficiently. For decades, people have recognized this as the deepest open problem in machine learning—AI’s equivalent of a Millennium Prize problem. And mathematics has already shown us what happens to such problems, even when they are very difficult, as long as they are verifiable.
Okay, why do I think that progress on sample efficiency, online learning, and the other problems in ML is verifiable? Well, there are roughly three broad buckets to AI R&D: pretraining, post-training, and inference efficiency. As I’ll explain below, each has strong verifiable proxies that are easy to train against. And since together they comprise all of algorithmic progress, that means that AI progress in general is easy to train against, which, in some sense, shouldn’t be surprising. We can make models much better at things that can be tested inside a datacenter. And AI training is literally happening inside a datacenter.
Keep in mind that this verifiability is valuable for two reasons. First, it allows AI companies to RL a model to get better at a specific part of AI research through thousands of rounds of practice. And second, these proxies make it easier for agents to work in parallel, because they can locally check whether they beat a particular leaderboard before merging their contributions.
As you’re building GPT-7, you can RL it to get better at finding pretraining compute multipliers. For example, you could make an RL objective that says GPT-7 has to minimize how much compute it uses to train a GPT-2-sized model to a fixed pretraining loss.
And once GPT-7 is built, you can deploy a swarm of agents to figure out how to train a GPT-3-sized model to the lowest possible perplexity. Loss on a held-out test set, which is the basis of pretraining progress, is extremely easy to verify.
Of course, what works at small scale doesn’t necessarily work at large scale. And it requires taste to anticipate which promising small-scale improvements will actually bear fruit when composed together in a bigger model. But this kind of intuition is also trainable—for example, you can make an RL environment where GPT-7 has to predict whether an algorithmic improvement made at the 100M-parameter scale will hold at the 10B scale. And while this “taste-bench” environment is more expensive to RL on than the
nanoGPT speedrun
, it’s still not that difficult to train on if you have frontier-lab-scale compute. So even important parts of research taste are verifiable.
By automating pretraining alone, you’d radically speed up AI progress. And there are three important reasons why:
First, pretraining leads to very general improvements in the model’s intelligence and capabilities. There is a deep explanation for why this is true, which has to do with the link between compression and intelligence, and if you want to learn more about this, you should check out
this excellent video by 3Blue1Brown
.
Second, as you make pretraining improvements, you can train a smaller and smaller model that is just as good as a previously larger model, but which trains faster and more cheaply. That not only speeds up pretraining but also makes your experiments and RL rollouts atop this base model more efficient.
And since your automated researchers are also instantiations of this now smaller model, you can now support larger researcher populations too.
Third, because smaller models train faster, this tightens the RSI loop itself. During RSI, labs probably won’t do three-month pretraining runs spread across multiple datacenter campuses. The army of automated researchers would be finding algorithmic innovations so quickly that, by the time a giant run finished, it would already be made obsolete by a much smaller model that first began training only a week ago. It’s similar to how, if you launched a spaceship to Alpha Centauri with today’s technology, it would probably be overtaken in transit by one launched a century from now. Furthermore, since you’re training smaller models faster, on a scale where you can run thousands of experiments daily, you won’t have to bet that small-scale results will hold up in bigger models. You’ve already tested at the scale you’re training.
How much better could base models get, even at today’s parameter sizes? I think there’s a ton more potential. We are far from the limits of pretraining. The AI lab Magic recently
announced
that they pretrained a model that matches the leading open-source base models today, like DeepSeek V4 Pro, for just half of the compute used to train the original GPT-3 (roughly $500k today). Orders-of-magnitude further improvements seem totally plausible.
Here are three different verifiable proxies for post-training:
First, your automated researchers can try to improve your post-training algorithms such that if you want to RL on a new set of environments, it takes less compute or data or time (all easily measurable).
Second, your automated researchers can work on making models better at learning on the fly. And you can easily measure progress on this. For example, if you drop the model into an environment it was never trained on, how quickly does it learn what’s going on and figure out how to get a good score? And how fast does it get better at a video game it’s never played before? You can have more real-world tasks that measure this kind of meta-learning too. Check out ByteDance’s
EdgeBench
for examples of such tasks.
Third, you can also just measure AI R&D capability directly. Anthropic has an internal benchmark called
CoBench
, which contains around 500 real problems that its researchers and engineers solved this year. Every benchmark is also an RL environment, and an RL environment like this would allow Anthropic to have its models practice redoing the last three to six months of human progress at the frontier.
Another important part of AI R&D is designing the model and the surrounding software to get more juice out of your compute. This is especially verifiable. You can easily measure GPU utilization, KV cache size per token, total FLOPs in a forward pass, latency, etc.
Now I want to deal with the strongest objections to my arguments about RSI.
I want to be clear that these bottlenecks are serious, and they do tamp down the probability of the most aggressive possible takeoff. This is why I think we make a GPT-3.5-to-GPT-6-sized jump in 2028 (rather than some crazy overnight singularity that starts tomorrow).
But I think these bottlenecks don’t fully deflate the craziness of this future (and the neck of the bottle is actually pretty wide). Let me explain why.
I’ve spent the past year and a half
arguing
that the main thing missing from today’s AIs is the ability to improve from on-the-job experience. Every new session is their first day on the job. And in each session, they can only retain a couple of hours’ worth of information, so they don’t accumulate the feedback or know-how that arrives over the course of weeks or months. Last December, this was my main reason for doubting that we’d automate AI research anytime soon. As I
wrote then
:
Somehow this automated researcher is going to figure out the algorithm for AGI – a problem humans have been banging their heads against for the better part of a century – while not having the basic learning capabilities that children have? I find this super implausible.
Here’s why I don’t think the current lack of continual learning will stop full automation of the best AI researchers by 2028.
First, AI companies might just solve continual learning by then with architectures much like the ones they already have. Previously, I thought we were bottlenecked by some crazy breakthrough that allowed models to update their own weights at the end of every session. But now I think scaling up in-context learning, so that you have sessions that are effectively many months long, will probably be enough to let a single instance learn on the job effectively. And there are many,
many
promising
ideas
that might let the labs achieve dramatically longer effective context windows.
Second, you might not need a continual learner to solve continual learning. As I explained above, online learning is an ML research problem with clean verifiable proxies. If you’d asked me two years ago which would be harder to solve, Navier-Stokes or continual learning, it wouldn’t have been obvious to me that the answer was Navier-Stokes. It turns out that continual learning was harder, given the fact that the labs haven’t cracked it yet. But are you so confident that it’s
that
much harder that non-online-learning models a year or two smarter than the ones currently solving Millennium Prize problems won’t be able to crack it, even if they are amnesiacs like the current models are?
These models are solving Millennium Prize problems while still being derpy savant interns who have no long-term memory. It’s like watching someone cartwheel down the track and still keep pace with Usain Bolt. If they were allowed to actually run, I’m sure they’d go even faster. But who’s to say they can’t win this race while still cartwheeling?
That being said, I think there is a serious chance that we don’t solve continual learning within the next few years, and that models are not able to compensate for this missing capability through their other advantages. That’s why I put a 25% chance that we won’t be able to automate Ilya-level researchers until after 2032.
Some people might argue that all the verifiable proxies I listed above assume the current paradigm. But figuring out what objective to verify in the first place—choosing which hill to have GPT-7 climb—is itself an important part of AI research. This is what one might call “research taste.” Before 2018, almost nobody thought that minimizing loss on next-token prediction was the most tractable path to AI progress. So nobody would have bothered building the nanoGPT speedrun environments on which the agent swarm could practice reducing the compute needed to get to a certain pretraining loss.
Won’t there be multiple new paradigms that we need to cross in order to get from here to ASI? And won’t each new paradigm have some new associated proxy that we don’t know ex ante? How will the automated researchers find these during RSI?
I have two responses:
The transformer was visible on (in fact was invented to beat) the existing translation benchmark—a similar story for reasoning models and pre-existing coding and math benchmarks. Proxies made before a “paradigm leap” seem perfectly capable of capturing large step changes in performance. This is because AI learning algorithms are quite general.
It’s not that difficult to come up with paradigm-agnostic outer loop proxies: how many Millennium Prize problems does your model solve; if you train your model on data before 1905, how long does it take to discover general relativity; how fast does it master totally unseen video games; and so on.
All in all, I think the other objections to the impact of RSI are much stronger—I would be very surprised if
this
was the reason RSI ended up not being a big deal.
Isn’t data one of the main inputs into AI progress? How will RSI happen without that scaling up at the same rate?
My answer is that data will continue growing during RSI, but the AIs will be the ones compiling it. Producing better training data for both pretraining and post-training is itself an ML research problem, and AIs are getting increasingly good at doing it themselves.
It is true that data is an extremely important input into AI R&D. Jerry Han and I actually did some
research
into this—we found that for pretraining, over the last six years, more than three times as much algorithmic progress has come from data improvements as from model improvements.
However, I don’t think people realize that these “data” improvements in pretraining are very much in line with normal AI research work—basically figuring out which techniques for filtering existing data or generating new synthetic data empirically lead to lower loss on a held-out corpus.
A similar thing seems to be increasingly true for RL. DeepSeek just published a
paper
where they talk about how they post-trained their new model. They say that changes to the basic RL algorithm have not mattered nearly as much, and “systematic improvements in the scale, diversity, and verifiability of synthesized data and environments account for essentially all of the observed gains.”
And the way in which those environments are made is becoming more and more automated: “we invest in large-scale, automated pipelines for data synthesis and environment construction … Using difficulty and correctness as reward signals, we iteratively train the model to construct better tasks.”
Earlier, I made this extended analogy between the current acceleration in mathematics and what we should expect to happen in AI research. But there is one big difference between AI research and mathematics. In mathematics, you can simply reason your way, with pen and paper, to new discoveries. In AI research, you need to run experiments to validate your ideas, which take compute and time. And as the number of automated researchers grows, each gets access to a smaller and smaller slice of the total experiment compute pie.
My answer to this objection is that each agent will still have access to a ton of compute. Frontier labs have been more than
quadrupling
their compute every single year. If this trend continues, then by the end of 2027, OpenAI could give thousands of agents each enough compute to run a GPT-3-sized training run every single day.
Keep in mind that the final model trained in the original transformer paper back in 2017 took 3.5 days on 8 P100s—which costs about 50 bucks to rent today (about one ten-thousandth of the training compute of GPT-3).
If top human AI researchers, like Noam Shazeer and Ilya Sutskever, had enough experiment compute to train a GPT-3-sized model every single day, they might make slower progress than they currently do. But it would be extremely surprising to me if they failed to make meaningful progress altogether, and just sat down and started complaining about how small their cluster was. Now, how productive do you think an AI lab would be if it had thousands of great researchers, each with this much compute, and each thinking 10 times as fast? You wouldn’t want to write a check to this neolab?
The nature of research and experimentation at the labs today reflects the fact that researcher time is extremely scarce relative to compute—top AI researchers individually get paid hundreds of millions of dollars a year. So the way labs use compute today tells us little about how efficiently they
could
use it if compute, rather than researcher time, were the key bottleneck.
There are two main ways in which the RSI agent swarm will use experiment compute much more effectively than researchers use it today:
Immediately, they can trade labor for compute. To save valuable researcher time, experiments today are, and should be, very wasteful with compute.
Instead of painstakingly setting up and carefully monitoring lots of small-scale pretraining experiments, a human researcher today might kick off a couple of huge multi-agent RL runs in parallel. But if you’re bottlenecked by experiment compute, you can just do more of the former.
When those automated researchers
are
doing an RL run, they could read every single rollout transcript and immediately pause and rebuild the whole environment if some task is broken. They could be doing crazy amounts of small-scale ablations of the models to make them oh so slightly better. And when a team of agents decides to combine their compute to do a much bigger run, they could spend many subjective decades designing the most informative pooled experiment, and once it’s done running, they could spend further subjective decades comprehensively analyzing it before designing a new experiment.
These automated researchers could also come up with a much better science of learning from small-scale experiments. Scaling laws themselves are a good example of this—
the GPT-4 paper
says that they were able to predict that model’s final loss using models trained with 10,000x less compute. One of the things that the smarter and faster automated company would be doing is trying to discover more scaling phenomena like
muP
(which lets researchers anticipate the optimal hyperparameters for a larger run from 100x smaller models). How many more similar discoveries are out there?
I remember chatting to an AI researcher who thought learning from extremely small neural networks could be incredibly informative. He put it this way: “The gods above must work from the same principles as the ants below.”
Anyway, thanks for sticking around for the Appendix. I’ll share the next essay on superintelligence soon.
