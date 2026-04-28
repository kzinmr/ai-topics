---
title: "Prompt Engineering vs. Blind Prompting"
url: "https://mitchellh.com/writing/prompt-engineering-vs-blind-prompting"
fetched_at: 2026-04-28T07:02:40.939781+00:00
source: "mitchellh.com"
tags: [blog, raw]
---

# Prompt Engineering vs. Blind Prompting

Source: https://mitchellh.com/writing/prompt-engineering-vs-blind-prompting

"Prompt Engineering" emerged from the growth of language models to describe
the process of applying prompting to effectively extract information
from language models, typically for use in real-world applications.
A lot of people who claim to be doing prompt engineering today are
actually just
blind prompting.
1
"Blind Prompting" is a term I am using
to describe the method of creating prompts with a crude trial-and-error
approach paired with minimal or no testing and a very surface level
knowedge of prompting.
Blind prompting is not prompt engineering.
There is also a lot of skepticism about whether prompt engineering
can truly be described as "engineering" or if it's just
"witchcraft"
spouted by
hype-chasers.  I think in most cases the skepticism is rooted
in the fact that a lot of tweets and blog posts I've seen claiming to
be on prompt engineering are really at best a thin layer above
blind prompting.
In this blog post, I will make the argument that prompt engineering
is a real skill that can be developed based on real experimental
methodologies. I will use a realistic example to walk through the
process of prompt engineering a solution to a problem that provides
practical value to an application.
This whole post will be biased towards expecting text output, since
text output is the primary use case I've had with language models. Certain
techniques -- such as the testing techniques -- don't translate 1:1 to
other types of outputs such as images. Everything in this post does work
well for multi-modal
inputs
, however.
Table of Contents
What is Prompting?
Feel free to skip this section if you're already very familiar with
the term "prompting" or understand what a "prompt" is.
For language models (imagine ChatGPT if this term is unfamiliar to you),
the
"prompt"
is the user-generated input to the model. In ChatGPT, it can
effectively be understood as the text box you type in. The language model
then "infers" a "completion" to your prompt. For example, if I type "4 + 3 = "
in ChatGPT, it will respond with "7" (probably). In this case, "4 + 3 = "
is the prompt, and "7" is the completion.
"Prompting"
is the act of using prompts as a way to extract desired information
from a model. It is an attractive approach to extracting information because
you don't need a large offline training set, you don't need offline access
to a model, and it feels intuitive even for non-engineers. Prompting is just
one method to tune a model
.
Finally,
"prompt engineering"
describes a more rigorous discipline (as
will be shown in this post) that aims to utilize prompting as a way to
build reliable functionality for real-world applications. It differs from
ChatGPT-style prompting because the prompts generated through prompt engineering
are usually meant to be used repeatedly in high-volume, diverse situations
in order to solve a specific problem reliably for an application.
The Problem
To start, you must have a problem you're trying to build a solution for.
The problem can be used to assess whether prompting is the best solution
or if alternative approaches exist that may be better suited as a solution.
Engineering starts with not using a method for the method's sake, but
driven by the belief that it is the
right method
.
For this example, we will pretend that we're a company that builds a
calendar client. We'd like users to be able to enter events using natural
language. For example:
Dinner with Alice next Tuesday at Taco Bell
CorpConf on 11/4
1:1 with Bob tomorrow at 10 AM
Language models might be a good solution to take this natural language
input and extract structured output to describe the event that we can then
use within our application.
There are obviously other potential solutions. We can utilize a set of
regular expressions
and string search to look for common phrases (
on <Day of Week>
,
tomorrow
,
today
,
next week
, etc.).
Language models have their own benefits: they might
provide an approach that handles other languages better, or might
handle typos or grammatical errors better, or may at worst be a good
backstop if regular expressions fail. In any case, there is enough promise
to continue pursuing prompting as a potential solution.
The Demonstration Set
Next, we have to put together a demonstration set. The demonstration set
contains an expected input along with an expected output. This set will serve
multiple goals:
It will be used to measure the accuracy of our prompt. By using the
input of a single demonstration, we can assert that we receive the expected
output.
It specifies what we expect the prompt inputs and outputs to look like,
allowing us as engineers to determine if it is the right shape for our problem.
We can use a subset of this demonstration set as exemplars for
a few-shot approach if we choose to use a few-shot prompt. For those
unfamiliar with the term "few-shot", few-shot is a style of prompt where
examples are given in addition to the prompt. See
here for a good overview of Few-Shot vs
Zero-Shot prompting
.
Point (2) above is extremely important. We need to have some general
understanding of what input we expect and what output we expect, because
on both sides of this is [usually] software that needs to ensure the data
is in a certain format and will expect a certain format back out.
This is no different from typical software engineering where we decompose
a problem into a set functions that have some input/output expectations.
We can utilize our examples from before and expand them to be complete
demonstrations:
Q: Dinner with Alice next Tuesday at Taco Bell
A: next Tuesday

Q: CorpConf on 11/4
A: 11/4

Q: 1:1 with Bob tomorrow at 10 AM
A: tomorrow
A note on demonstration set size:
For this blog post, we only have three
demonstrations. In reality, you probably want at least a dozen. The more
demonstrations you have the better testing you can do, but also the more
expensive it becomes due to token usage. At a certain size, it is often
more economical to
fine-tune a language model
.
There are two important decisions made for the above demonstrations.
For any prompting problem, you'll have to make similar decisions.
First, we are only extracting one piece of information.
It may be
tempting to try to get the model to extract our entire event such as
event name, attendees, time, location, etc. and output
it as some beautiful ready-to-use JSON or some other format. The model
may be able to do this. But when approaching a new problem, I recommend
decomposing it into a single problem first. This makes the problem more
tractable, and will also eventually give you a baseline accuracy that you
can use to benchmark whether the multi-output approach is actually worth
it or not.
Second, our output is not transformed.
We aren't trying to turn
everything into a date or trying to ensure everything is capitalize
correctly or so on. We're doing literal text extraction. There are fantastic
deterministic libraries out there that can turn strings like "next Tuesday"
into timestamps with extremely high accuracy. This isn't something we need
a language model to do for us. So, let's just get out the rough date format
("next Tuesday", "11/4", "tomorrow") and solve the problem of turning this
into a timestamp using traditional programming methods because it is a
trivial problem. The simpler the output, the easier it will be to get
higher accuracy.
Finally, a brief note on
output decoding
:
LLMs will complete your prompt
in various ways: it may be a complete sentence, it may add a period,
it may be capitalized, etc. You should determine how perfect you want
your output from the LLM to be and how much you're willing to normalize
prior to validating your demonstration set.
For example, if I'm doing text extraction, I typically find it reasonable to
trim whitespace and periods and lowercase the entire output. If I'm doing
something more advanced like JSON generation, I might parse and re-encode
the JSON in some deterministic order and style so comparisons are deterministic.
And so on.
My recommendation: keep the output from the LLM as simple and flexible as
possible, and perform some normalization operations in your application.
Don't try to force the LLM to output
exactly perfect
formats to start.
Performing too much "output shaping" in the LLM early on makes it difficult
to separate an LLM's ability to perform some core task (information extraction
in this case) from its ability to structure the output.
Prompt Candidates
We now come up with some prompt candidates. A prompt candidate is a
prompt that we feel may elicit the desired behavior we want from the
language model. We come up with multiple candidates because its unlikely
we'll choose the best prompt right away.
For the sake of being an introductory level text, we will come up with prompts
manually. To be effective, there is some basic knowledge prompt engineers
should use when building prompts.
For example, it is better to
be assertive than to be defensive. It is often better to be clear and concise
than it is to be repetitive and long. When building a few-shot prompt,
equal distribution of labels matters, demonstrating the full set of labels
matters, etc. When choosing exemplars, exemplars that the LLM was likely
to get wrong typically perform best, exemplars have been shown to often perform
best when ordered shortest to longest, etc.
Citations required!
I'm sorry, I didn't cite the experimental research
to support these recommendations. The honest truth is that I'm too lazy
to look up the papers I read about them (often multiple per point). If
you choose not to believe me,
that's fine
, the more important point
is that experimental studies on prompting techniques and their efficacy
exist. But, I promise I didn't make these up, though it may be possible
some are outdated with modern models.
It is a dedicated post on its own to go over some of these techniques and it
isn't the goal of this post. The goal of this
post is to show the high-level end to end process and to show that
there is an engineering method to extracting value from LLMs
.
At this point, the goal is to come up with some good zero-shot prompts.
The zero-shot prompts can be transformed into few-shot and those can
be further transformed into chain of thought. And each of those can be further
turned into batched prompts and so on. Therefore, since zero-shot is a base
requirement to
try
, we focus on that.
Here are three prompt candidates I came up with:
Identify the date or day mentioned in the given text and provide it as the output.
Identify the date or day mentioned in the given event description.
Determine the date or day from each input and provide the output accordingly as a single word or date.
They're all reasonable prompts. Given any educated human, every prompt would likely
yield very high accuracy. But language models are not human, so we can't
automatically expect equivalent performance. I've shown before how
very reasonable prompts can have abysmal performance
.
So our next step is to inform our decision by doing some testing and
taking some measurements.
Prompt Testing
With a set of candidate prompts as well as a demonstration set, we
can now measure accuracy. The best way I've found to do this today is
to build a simple Python script using a library like LangChain. For my
testing, I usually run through each demonstration and perform the following
prompt template:
{{prompt}}. Q: {{input}} A:
I always test zero-shot first. I want to get a baseline accuracy metric.
From there, you can then test few-shot and compare not only different
candidates but different prompting types. And so on.
This has to be done per-model. The same prompt even on a more powerful
model is not guaranteed to have the same or better accuracy; the accuracy
can go down
2
.
The most basic result of prompt testing should be a table like below.
You may also have additonal dimensions such as model (GPT-3.5 vs GPT-4
for example).
| Zero-Shot | Few-Shot | ... |
-----------------------------------------
Prompt 1   | 64        | 68       | ... |
-----------------------------------------
Prompt ... | 44        | 52       | ... |
-----------------------------------------
Prompt N   | 23        | 22       | ... |
This table shows prompt candidates on the Y-axis, and prompt types
using those prompts on the X-axis. The value is the accuracy as a percentage
of correct answers. Continuing the calendar app example, "prompt 1" as
a zero-shot prompt with one demonstration may look like this:
Identify the date or day mentioned in the given text and provide it as the
output. Q: CorpConf on 11/4 A:
And we expect "11/4" as the answer. The few-shot version may look like this:
Identify the date or day mentioned in the given text and provide it as the
output.
Q: Dinner with Alice next Tuesday at Taco Bell. A: next Tuesday
Q: 1:1 with Bob tomorrow at 10 AM. A: tomorrow
Q: CorpConf on 11/4. A:
A note for experienced prompters:
the few-shot example doesn't say
something like "mimic the examples below." Experimental research has shown
this doesn't reliably increase accuracy, so I like to test without it first
to limit tokens. Second, the few-shot example exemplars don't ever show
the "MM/DD" extraction as an example, which is poor form. In a real few-shot
setting, demonstrating all styles of extraction can be important (
Zhao, et al 2021
).
For certain types of problems, such as classification problems, you
can use a
confusion matrix (Strobelt, et al 2022)
to
visualize the probabilities of other labels and use that to determine
if your label set can potentially be better tuned.
In addition to accuracy, you also want to measure tokens used,
requests used, etc. All of this will have to be taken into consideration
when choosing your final prompt.
Choosing a Prompt
Finally, you choose one of the prompt candidates to integrate into your
application. This isn't necessarily the most accurate
prompt. This is a cost vs. accuracy analysis based on model used, tokens
required, and accuracy presented.
For example, you may find that the few-shot variant performs best, but
its only 4% more accurate on the test set and requires 200% more tokens
(effectively doubling the cost for current API-driven models). You may
determine for your business that its worth being 4%
less
accurate for
half the cost.
Or, you may decide to go back and test
other approaches to increase
accuracy.
For example, you may try a
self-consistency decoding
strategy (Wang, et al 2022)
on a lower cost model to
see if that improves the accuracy enough. Sometimes, using more tokens
on a lower cost model will save significant money vs. low-token usage
on a higher cost model. For example, GPT-4 is ~15x more expensive than
GPT-3.5 today. That means that you effectively have 15x more token budget
to increase the GPT-3.5 prompt accuracy (caveats around rate limits noted).
For our example in this blog post, we may choose to go with the zero-shot
version of
Prompt 1
in our table because it has 64% accuracy with
likely significantly fewer tokens. Maybe we decide 64% accuracy is good
enough to at least populate an event template for our calendar application.
For this particular problem, I think we can do significantly better than
64%, but that's just the number I used in this post.
Most Importantly, you have the data to be make an informed decision.
Trust But Verify and Continuous Improvement
Due to the probabilistic nature of generative AI, your prompt likely
has some issues. Even if your accuracy on your test set is 100%, there
are probably unknown inputs that produce incorrect outputs. Therefore,
you should
trust but verify
and
add verification failures to your
demonstration set
in order to develop new prompts and increase accuracy.
Verification is highly dependent on the problem. For our calendar application
example, we may want to explicitly ask users: "is this event correct?" And
if they say "no," then log the natural language input for human review.
Or, we can maybe do better to automatically track any events our users
manually change after our automatic information extraction
3
.
As a different example, if our prompt is generating code (such as a regular
expression or programming language text), we can -- at a minimum -- try to
parse it
. Parsing should never be a security concern
4
, and it gives
at least the most basic validation that
at least syntax is correct
.
And again, if this verification fails, we can log the input and output,
grow our demonstration set, and develop better prompts.
Verification also helps against
adversarial prompting
.
Adversarial prompting is a whole topic unto itself, and I won't cover it
in this post.
And Onwards...
This blog post demonstrates how developing a prompt can -- in my opinion --
be an engineering practice. It describes a systematic approach to identifying
a problem, forming solutions, validating those solutions, and applying
continuous improvement to refine those solutions.
Compare the approach in this post to "Blind Prompting" which relies on anecdotal experience and
pervasive trial-and-error to arrive at some proposed solution, and often doesn't
build the proper systematic infrastructure to reliably iterate on prompts
as time goes on.
I want to note that blog post is very elementary. There are multiple places
in this post that could be improved with more advanced techniques that
are already well-known. Further, I didn't cover important topics such as
adversarial prompting. As a specific example, there are more scientific approaches
to choosing the best examples for a few-shot prompt, but I wanted to keep
this post to the basics as much as possible. If you want to learn some
more advanced techniques,
Prompt Engineering by Lilian Weng
provides a fantastic overview.
Additionally, everyone is rapidly moving to higher-order LLM integrations: prompt chaining,
agents, etc. Some people argue that future innovations such as these and
more will make human prompting obsolete. Regardless of if this is true or not, I am someone
who believes learning things from
"first principles"
5
is valuable and I think that learning prompting techniques such as this
has only improved my ability to utilize higher-order language model techniques.
I also believe basic prompting such as this still enables better
performance of higher-order concepts.
