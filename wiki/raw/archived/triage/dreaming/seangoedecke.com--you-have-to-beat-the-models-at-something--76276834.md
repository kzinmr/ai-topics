---
title: "You have to beat the models at something"
url: "https://seangoedecke.com/you-have-to-beat-the-models-at-something/"
fetched_at: 2026-08-30T10:01:00.835176+00:00
source: "seangoedecke.com"
tags: [blog, raw]
---

# You have to beat the models at something

Source: https://seangoedecke.com/you-have-to-beat-the-models-at-something/

In 2025, I wrote that software engineers ought to be assessed by
“value over replacement”
: not how much money they made for their company, but how much they would have made compared to the average engineer in their position. I’ve always found it vaguely silly when engineers put “built a product that made $X” on their resumes, when they just did the
JIRA tickets
that came across their desk.
Today, value over replacement is even more important. A replacement-level engineer in the 2010s was
fine
: maybe not worth promoting, but still
worth paying
, because writing code had a high fixed cost. Now writing code costs
a hundred bucks a month
. What are you doing that GPT-5.6-Sol or Claude Opus 5 wouldn’t do in your position? Why is it worth paying an extra two or three orders of magnitude for?
This is a scary thought. But you’re not doing yourself any favors by pretending that LLMs
can’t actually write code
and it’s all just a scam, or that LLM-written code is
inherently so bad
as to cause companies using it to collapse next year. We are not going to wake up in 2027 to find that the AI craze is over and everyone is writing code by hand again. You ought to put some serious thought into what you can do better than the models in the medium and long term.
Staying ahead of the models is a moving target. At the start of 2026, “make working changes to large codebases” was
in this category
, but now it’s not. For this reason, I doubt that you can retreat to some “hard engineering” area that requires deeper expertise. That might work in the short term, but not forever. If LLMs can find a better
lower bound
on the Riemann hypothesis, they will soon
be able to write solid high-performance kernel drivers or GPU shaders or whatever.
I think it’s more useful to look at the tasks models
haven’t
gotten better at over time, and the tasks that are hard for them get better at in principle. The two best examples of these are:
Deep familiarity with the codebase
Technical communication
Deep familiarity
What do frontier LLMs get wrong? What kind of coding mistakes do they make? It’s been a long time since I’ve seen a straight-up hallucination from a coding agent, or a simple logic error like an off-by-one. The mistakes they make tend to be errors of
ignorance
:
Not knowing that there’s a module in the codebase they could use instead of reimplementing some logic
Making the change in the wrong system because they didn’t know System X was the standard place for this functionality
Adopting a coding style that’s inconsistent with the company’s standard practice
Other times they’re errors of
paranoia
:
Implementing triply-redundant checks for a value that
technically
could be wrong but practically is set once from config and never updated
Assuming that ten milliseconds of stale data is unacceptable and designing a complex, unnecessary system to keep it always up to date
Building in fallbacks and “graceful” degradation into some code that ought to simply crash on error (e.g. a CLI tool, or a restartable k8s service)
What do these errors have in common? They’re the kind of errors a smart engineer might make if they had no context on the system: they’re competent enough to be able to solve the problem, but they haven’t been around long enough to confidently say “yes, we can take this risk to avoid an extra three thousand lines of code”. Until someone cracks
continuous learning
or
truly
massive context windows, this is just an inherent feature of how AI agents operate. If you can catch these errors, you’ll be providing real value.
The only way to catch these errors is to be familiar with the codebase and familiar with the system in general. For much more on this, see my post
You can’t design software you don’t work on
. But there’s also a psychological component to it.
You have to be willing to confidently disagree with the agent.
AI agents can be very convincing. Often they can get “stuck” on some error above where they’re not willing to take a particular risk, so they keep going back and sneaking in code to cover that case (or writing persuasive arguments about why that case is important). To add value, you need to be willing to say “this sucks, I don’t think we need X and Y at all, why can’t we do Z in a much simpler way?” It takes
courage
.
You can’t rely on other AI agents to review each other’s work. If you use the same model, it’ll reliably make the exact same assumptions and mistakes. But even if you use different models, they’ll also tend towards the same
kinds
of mistakes — ignorance and paranoia — for the same structural reasons. AI-driven review loops are in fact
more
likely to get these things wrong, because modern AIs have been
RL-ed
to try to find a few nitpicks no matter what. Having a critic AI and a worker AI bounce off each other is a really good way to end up with ten thousand lines of paranoid slop.
Technical communication
Another area where you can add value on top of AI is
communication
. Newer models are better at coding, but are paradoxically getting worse at writing. GPT-3.5 and GPT-4 had a human-like writing style at times. GPT-4o introduced the modern
slop
idiolect, and the newer Anthropic models speak
“Claudish”
: a bizarre semi-baroque semi-truncated way of communicating that nobody enjoys. There have been a few bright spots — GPT-4.5 was okay, and I quite liked o3
— but in general LLMs are not good at this. Here’s two reasons why.
First,
good writing is not a verifiable domain
. If you want a model to get good at mathematics or coding, you can generate problems for it and automatically grade them. You can’t grade good writing. If you try to get humans to grade it — for instance, via the early OpenAI RLHF attempts — you get the kind of writing that sounds impressive to the average person when consumed in single-paragraph form. This is the origin of the “stick three hundred writing devices into every sentence” style. I think it’d be possible in principle to hand-pick some people with good taste and have them do it, but there are some obvious problems
that prevent this from happening.
Second,
the labs have been monomaniacally focused on capability instead of communication
. When you’re trying to train a model that can break new scientific ground or replace a software engineer, you might trade off some communication ability. In fact, I think we can identify exactly how this has been happening. If you look at
internal model reasoning tokens
, they tend to have strange word choices and oddly truncated grammar:
RESOLUTION: charge the current-leg’s OWN saved-prefix occupancy EAGERLY: when leg i saves e
1..e
t: ALSO commit their occupancy AT LEG i
If you were to translate this into proper English, you would probably end up with something that reads like Claudish:
Charge the current-leg’s saved-prefix occupancy on a clean, eager path: when leg i saves e
1..e
t, commit the occupancy at leg i.
I suspect that the weirdly alien writing style of some LLMs is because you’re reading a semi-literal translation of that model’s internal chain-of-thought, which has become nearly incomprehensible in pursuit of better problem-solving abilities. It is surprisingly hard to translate Claudish to good English: not only do you need to follow the convoluted, compressed language of the original, but you need the technical ability to understand the problem the model is solving.
Because of all this,
technical communication may be a surprisingly durable skill.
In Peter Watts’ novel
Blindsight
, the world is full of cognitively augmented humans. The main character is a “synthesist”: someone whose job is to be a translation layer between these geniuses (who speak in abbreviations and gestures) and everyone else. Watts’ idea is that communication ability may be largely independent from — or even negatively correlated with — intelligence. A
“country of geniuses”
may still need a bunch of ordinary smart people to translate their insights for everyone else.
If you’re trying to communicate to humans, there are also huge advantages to having a human write the content. Many of us are becoming
AI-blind
: developing an instinctive reflex that stops us reading when we encounter AI-generated content. It’s like the reflex that allows people to ignore flashing billboards or sidebar advertisements on websites. If you circulate some planned technical strategy as an AI-written document, most of your colleagues will have to physically force themselves to read it word-by-word.
Conclusion
Whatever you do, don’t be a
meat proxy
: someone who simply copies requests into an AI agent and submits their output as your own work product. Doing that is just begging to be fired, since you’re definitionally not adding any value yourself. Even if you have a cunning system of multiple agents — the so-called “software factory” — you’re still on dangerous ground. When the features of your system work their way into enterprise AI tooling (and they will), you’ll be disposable.
You need to find some way to leverage your expertise to do what the models can’t.
Simply not using AI at all is better than being a meat proxy, since you’ll probably do some things better than the model would have, but it’s far better to figure out what AI can do and position yourself to fill those gaps. Right now, there are two main gaps: familiarity with the technical details of the system, and the ability to clearly and persuasively write about those details.
Here's a preview of a related post that shares tags with this one.
