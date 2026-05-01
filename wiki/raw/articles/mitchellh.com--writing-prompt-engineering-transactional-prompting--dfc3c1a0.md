---
title: "Prompt Engineering is for Transactional Prompting"
url: "https://mitchellh.com/writing/prompt-engineering-transactional-prompting"
fetched_at: 2026-05-01T07:02:03.550378+00:00
source: "mitchellh.com"
tags: [blog, raw]
---

# Prompt Engineering is for Transactional Prompting

Source: https://mitchellh.com/writing/prompt-engineering-transactional-prompting

I've noticed a consistent point of confusion whenever prompt engineering
is discussed and I believe the confusion stems from two distinct ways of using
a language model:
interactive prompting
and
transactional prompting
.
Prompt engineering is primarily about transactional prompting, and a considerable
amount of confusion or negativity arises when an individual tries to apply it
to interactive prompting.
Interactive prompting
is ChatGPT-style prompting where you're having
more of a
discussion
with the language model. If the model returns an
unclear response, you can use the pre-existing context to make clarifications
and guide the model towards the correct response. Further, interactive
prompting is driven primarily by a human being.
Transactional prompting
treats the language model more like a function
in a programing language: you give it some input and desire some output.
This isn't limited to a single prompt, you may chain prompts or perform
"agent"-like behaviors here. The point is that you're treating
the language model transactionally for a very specific problem, usually
at high volume, and driven by software.
I'm assuming terms like "prompting", "prompts", "language model",
etc. are already familiar to you. If you want more background
on these terms and prompt engineering in general, please see my prior
post
Prompt Engineering vs. Blind Prompting
.
Prompt engineering can help both, since the knowledge of prompt engineering
should in theory make someone more effective at getting the desired results
from a model regardless of style. However, I believe the primary benefit
of prompt engineering is for the transactional use case.
Prompt engineering is about getting the desired result from a language model
with the most accuracy and lowest cost. These goals lend themselves more to
transactional use cases.
Objectivity vs. Subjectivity
The nature of a process being interactive or transactional isn't nuanced
enough to cleanly separate the value of prompt engineering. Another dimension
that we can split is between
objectivity
and
subjectivity
.
If we have an input that can produce an objectively correct (or I'd even
argue "mostly correct") output, then prompt engineering can be successfully
applied. Examples of problems with objectively correct results: information
extraction, classification, limited forms of code generation, etc.
However, if we have an input that produces something subjectively correct,
then prompt engineering is much less useful. The best example of subjective
results are creative tasks such as art generation, writing, semantic search.
In the same way that you cannot "engineer" art to be objectively good or bad,
it is impossible to "prompt engineer" an LLM on a subjective task to
be objectively good or bad. You can prompt engineer a subjective task to
improve the likelihood that the resulting output is subjectively accepted,
but you can't have the same level of certainty or accuracy as an objective task.
Of course, you may point out that plenty of well-known "prompt templates"
exist for subjective tasks that help arrive at the desired result. For example,
templates exist to reliably generate art in a specific style. However, to arrive
at these prompt templates is much less an engineering or scientific practice
and more of a creative writing process.
I view "code generation" as an example of both an objective and subjective task.
In theory, code generation can be objectively correct: if software
has a sufficiently accurate specification of its behavior, software can
objectively be said to either pass or fail the specification. In reality, almost
no software has this level of specificity. Therefore, the larger the code
generation task, the more subjective it becomes. Conversely, the smaller
the code generation task, the more likely that test cases or the input language
can be exactly specified, and the more objective it becomes
1
.
Objective, Transactional Prompting
In general, knowledge of prompt engineering will make anyone more effective
at extracting desired information from a language model regardless of the task
at hand. However, prompt engineering for interactive prompts is more akin
to someone being an effective "Googler" (Google Search user) whereas prompt
engineering for transactional prompts is closer to someone being a data
scientist.
Prompt engineering attempts to turn an LLM into an objective, predictable,
transactional API like any other API a program may interface with such
as payments, in-process function calls, SaaS calls, etc. Of course, a
language model is not a deterministic, 100% reliable machine, so the utility
and use case must be different.
In conclusion, prompt engineering doesn't apply to
all prompt interactions
with a language model
. There are some interactions that are more creative
and less data-driven or methodical. But likewise, there are use cases for
language models where an engineering methodology can be applied to yield
the best results. Both exist without invalidating the other.
One specific area I want to clarify is around the rise of "agents" at the
time of writing this post. One could argue that agents are an automated,
interactive process with a language model. Technically, they are. But the
usage of agents is in my opinion primarily transactional: you give the
agent a task and await a result (that may or may not be objectively correct).
Prompt engineering can be applied to agents since there is a high-volume,
software-driven, transactional nature to their usage.
