---
title: "As an Experienced LLM User, I Actually Don't Use Generative LLMs Often"
url: "https://minimaxir.com/2025/05/llm-use/"
fetched_at: 2026-04-30T07:01:55.582578+00:00
source: "minimaxir.com"
tags: [blog, raw]
---

# As an Experienced LLM User, I Actually Don't Use Generative LLMs Often

Source: https://minimaxir.com/2025/05/llm-use/

Lately, I’ve been working on codifying a personal ethics statement about my stances on generative AI as I have been very critical about
several
aspects
of modern GenAI, and yet
I participate in it
. While working on that statement, I’ve been introspecting on how I myself have been utilizing large language models for both my professional work as a Senior Data Scientist at
BuzzFeed
and for my personal work blogging and
writing open-source software
. For about a decade, I’ve been researching and developing tooling around
text generation from char-rnns
, to the
ability to fine-tune GPT-2
, to
experiments with GPT-3
, and
even more experiments with ChatGPT
and other LLM APIs. Although I don’t claim to the best user of modern LLMs out there, I’ve had plenty of experience working against the cons of next-token predictor models and have become very good at finding the pros.
It turns out, to my surprise, that I don’t use them nearly as often as people think engineers do, but that doesn’t mean LLMs are useless for me. It’s a discussion that requires case-by-case nuance.
How I Interface With LLMs
#
Over the years I’ve utilized all the tricks to get the best results out of LLMs. The most famous trick is
prompt engineering
, or the art of phrasing the prompt in a specific manner to coach the model to generate a specific constrained output. Additions to prompts such as
offering financial incentives to the LLM
or simply
telling the LLM to make their output better
do indeed have a quantifiable positive impact on both improving adherence to the original prompt and the output text quality. Whenever my coworkers ask me why their LLM output is not what they expected, I suggest that they apply more prompt engineering and it almost always fixes their issues.
No one in the AI field is happy about prompt engineering
, especially myself. Attempts to remove the need for prompt engineering with more robust
RLHF
paradigms have only made it
even more rewarding
by allowing LLM developers to make use of better prompt adherence. True, “Prompt Engineer” as a job title
turned out to be a meme
but that’s mostly because prompt engineering is now an expected skill for anyone seriously using LLMs. Prompt engineering works, and part of being a professional is using what works even if it’s silly.
To that end,
I never use ChatGPT.com
or other normal-person frontends for accessing LLMs because they are harder to control. Instead, I typically access the backend UIs provided by each LLM service, which serve as a light wrapper over the API functionality which also makes it easy to port to code if necessary. Accessing LLM APIs like the ChatGPT API directly allow you to set
system prompts
which control the “rules” for the generation that can be very nuanced. Specifying specific constraints for the generated text such as “keep it to no more than 30 words” or “never use the word ‘delve’” tends to be more effective in the system prompt than putting them in the user prompt as you would with ChatGPT.com. Any modern LLM interface that does not let you explicitly set a system prompt is most likely
using their own system prompt
which you can’t control: for example, when ChatGPT.com had an issue where it was
too sycophantic
to its users, OpenAI
changed the system prompt
to command ChatGPT to “avoid ungrounded or sycophantic flattery.” I tend to use
Anthropic
Claude’s API — Claude Sonnet in particular — more than any ChatGPT variant because Claude anecdotally is less “robotic” and also handles coding questions much more accurately.
Additionally with the APIs, you can control the “
temperature
” of the generation, which at a high level controls the creativity of the generation. LLMs by default do not select the next token with the highest probability in order to allow it to give different outputs for each generation, so I prefer to set the temperature to
0.0
so that the output is mostly deterministic, or
0.2 - 0.3
if some light variance is required. Modern LLMs now use a default temperature of
1.0
, and I theorize that higher value is accentuating
LLM hallucination
issues where the text outputs are internally consistent but factually wrong.
LLMs for Professional Problem Solving!
#
With that pretext, I can now talk about how I have used generative LLMs over the past couple years at BuzzFeed. Here are outlines of some (out of many) projects I’ve worked on using LLMs to successfully solve problems quickly:
BuzzFeed site curators developed a new
hierarchal taxonomy
to organize thousands of articles into a specified category and subcategory. Since we had no existing labeled articles to train a traditional
multiclass classification
model to predict these new labels, I wrote a script to hit the Claude Sonnet API with a system prompt saying
The following is a taxonomy: return the category and subcategory that best matches the article the user provides.
plus the JSON-formatted hierarchical taxonomy, then I provided the article metadata as the user prompt, all with a temperature of
0.0
for the most precise results. Running this in a loop for all the articles resulted in appropriate labels.
After identifying hundreds of distinct semantic clusters of BuzzFeed articles using data science shenanigans, it became clear that there wasn’t an easy way to give each one unique labels. I wrote another script to hit the Claude Sonnet API with a system prompt saying
Return a JSON-formatted title and description that applies to all the articles the user provides.
with the user prompt containing five articles from that cluster: again, running the script in a loop for all clusters provided excellent results.
One BuzzFeed writer asked if there was a way to use a LLM to sanity-check grammar questions such as “should I use an
em dash
here?” against the
BuzzFeed style guide
. Once again I hit the Claude Sonnet API, this time copy/pasting the
full
style guide in the system prompt plus a command to
Reference the provided style guide to answer the user's question, and cite the exact rules used to answer the question.
In testing, the citations were accurate and present in the source input, and the reasonings were consistent.
Each of these projects were off-hand ideas pitched in a morning standup or a Slack DM, and yet each project only took an hour or two to complete a proof of concept (including testing) and hand off to the relevant stakeholders for evaluation. For projects such as the hierarchal labeling, without LLMs I would have needed to do more sophisticated R&D and likely would have taken days including building training datasets through manual labeling, which is not intellectually gratifying. Here, LLMs did indeed follow the
Pareto principle
and got me 80% of the way to a working solution, but the remaining 20% of the work iterating, testing and gathering feedback took longer. Even after the model outputs became more reliable, LLM hallucination was still a concern which is why I also advocate to my coworkers to use caution and double-check with a human if the LLM output is peculiar.
There’s also one use case of LLMs that doesn’t involve text generation that’s as useful in my professional work:
text embeddings
. Modern text embedding models technically are LLMs, except instead of having a head which outputs the logits for the next token, it outputs a vector of numbers that uniquely identify the input text in a higher-dimensional space. All improvements to LLMs that the ChatGPT revolution inspired, such as longer context windows and better quality training regimens, also apply to these text embedding models and caused them to improve drastically over time with models such as
nomic-embed-text
and
gte-modernbert-base
. Text embeddings have done a lot at BuzzFeed from identifying similar articles to building recommendation models, but this blog post is about generative LLMs so I’ll save those use cases for another time.
LLMs for Writing?
#
No, I don’t use LLMs for writing the text on this very blog, which I suspect has now become a default assumption for people reading an article written by an experienced LLM user. My blog is far too weird for an LLM to properly emulate. My writing style is blunt, irreverent, and occasionally cringe: even with prompt engineering plus
few-shot prompting
by giving it examples of my existing blog posts and telling the model to follow the same literary style precisely, LLMs output something closer to Marvel movie dialogue. But even if LLMs
could
write articles in my voice I still wouldn’t use them due of the ethics of misrepresenting authorship by having the majority of the work not be my own words. Additionally, I tend to write about very recent events in the tech/coding world that would not be strongly represented in the training data of a LLM if at all, which increases the likelihood of hallucination.
There is one silly technique I discovered to allow a LLM to improve my writing without having it do
my writing
: feed it the text of my mostly-complete blog post, and ask the LLM to pretend to be a cynical
Hacker News
commenter and write five distinct comments based on the blog post. This not only identifies weaker arguments for potential criticism, but it also doesn’t tell me what I
should
write in the post to preemptively address that negative feedback so I have to solve it organically. When running a rough draft of this very blog post and the Hacker News system prompt through the Claude API (
chat log
), it noted that my examples of LLM use at BuzzFeed are too simple and not anything more innovative than traditional
natural language processing
techniques, so I made edits elaborating how NLP would not be as efficient or effective.
LLMs for Companionship?
#
No, I don’t use LLMs as friendly chatbots either. The runaway success of LLM personal companion startups such as
character.ai
and
Replika
are alone enough evidence that LLMs have a use, even if the use is just entertainment/therapy and not more utilitarian.
I admit that I am an outlier since treating LLMs as a friend is the most common use case. Myself being an introvert aside, it’s hard to be friends with an entity who is trained to be as friendly as possible but also habitually lies due to hallucination. I
could
prompt engineer an LLM to call me out on my bullshit instead of just giving me positive affirmations, but there’s no fix for the lying.
LLMs for Coding???
#
Yes, I use LLMs for coding, but only when I am reasonably confident that they’ll increase my productivity. Ever since the dawn of the original ChatGPT, I’ve asked LLMs to help me write
regular expressions
since that alone saves me hours, embarrassing to admit. However, the role of LLMs in coding has expanded far beyond that nowadays, and coding is even more nuanced and more controversial on how you can best utilize LLM assistance.
Like most coders, I Googled coding questions and clicked on the first
Stack Overflow
result that seemed relevant, until I decided to start asking Claude Sonnet the same coding questions and getting much more detailed and bespoke results. This was more pronounced for questions which required specific functional constraints and software frameworks, the combinations of which would likely not be present in a Stack Overflow answer. One paraphrased example I recently asked Claude Sonnet while writing
another blog post
is
Write Python code using the Pillow library to composite five images into a single image: the left half consists of one image, the right half consists of the remaining four images.
(
chat log
). Compositing multiple images with
Pillow
isn’t too difficult and there’s enough
questions/solutions about it on Stack Overflow
, but the specific way it’s composited is unique and requires some positioning shenanigans that I would likely mess up on the first try. But Claude Sonnet’s code
got it mostly correct
and it was easy to test, which saved me time doing unfun debugging.
However, for more complex code questions particularly around less popular libraries which have fewer code examples scraped from Stack Overflow and
GitHub
, I am more cautious of the LLM’s outputs. One real-world issue I’ve had is that I need a way to log detailed metrics to a database while training models — for which I use the
Trainer class
in
Hugging Face transformers
— so that I can visualize and analyze it later. I asked Claude Sonnet to
Write a Callback class in Python for the Trainer class in the Hugging Face transformers Python library such that it logs model training metadata for each step to a local SQLite database, such as current epoch, time for step, step loss, etc.
(
chat log
). This one I was less optimistic about since there isn’t much code about creating custom callbacks, however the Claude-generated code implemented some helpful ideas that weren’t on the top-of-my-mind when I asked, such a buffer to limit blocking I/O, SQLite config speedups, batch inserts, and connection handling. Asking Claude to “make the code better” twice (why not?) results in a few more unexpected ideas such as SQLite connection caching and using a single column with the JSON column type to store an arbitrary number of metrics, in addition to making the code much more Pythonic. It is still a lot of code such that it’s unlikely to work out-of-the-box without testing in the full context of an actual training loop. However, even if the code has flaws, the ideas themselves are extremely useful and in this case it would be much faster and likely higher quality code overall to hack on this generated code instead of writing my own SQLite logger from scratch.
For actual data science in my day-to-day work that I spend most of my time, I’ve found that code generation from LLMs is less useful. LLMs cannot output the text result of mathematical operations reliably, with some APIs working around that by
allowing for a code interpreter
to perform data ETL and analysis, but given the scale of data I typically work with it’s not cost-feasible to do that type of workflow. Although
pandas
is the standard for manipulating tabular data in Python and has been around since 2008, I’ve been using the relatively new
polars
library exclusively, and I’ve noticed that LLMs tend to hallucinate polars functions as if they were pandas functions which requires documentation deep dives to confirm which became annoying. For data visualization, which I don’t use Python at all and instead use
R
and
ggplot2
, I really haven’t had a temptation to consult a LLM, in addition to my skepticism that LLMs would know both those frameworks as well. The techniques I use for data visualization have been
unchanged since 2017
, and the most time-consuming issue I have when making a chart is determining whether the data points are too big or too small for humans to read easily, which is not something a LLM can help with.
Asking LLMs coding questions is only one aspect of coding assistance. One of the other major ones is using a coding assistant with in-line code suggestions such as
GitHub Copilot
. Despite my success in using LLMs for one-off coding questions, I actually dislike using coding assistants for an unexpected reason: it’s distracting. Whenever I see a code suggestion from Copilot pop up, I have to mentally context switch from writing code to reviewing code and then back again, which destroys my focus. Overall, it was a net neutral productivity gain but a net negative cost as Copilots are much more expensive than just asking a LLM ad hoc questions through a web UI.
Now we can talk about the elephants in the room — agents,
MCP
, and vibe coding — and my takes are spicy. Agents and MCP, at a high-level, are a rebranding of the Tools paradigm popularized by the
ReAct paper
in 2022 where LLMs can decide whether a tool is necessary to answer the user input, extract relevant metadata to pass to the tool to run, then return the results. The rapid LLM advancements in context window size and prompt adherence since then have made Agent workflows more reliable, and the standardization of MCP is an objective improvement over normal Tools that I encourage. However,
they don’t open any new use cases
that weren’t already available when
LangChain
first hit the scene a couple years ago, and now
simple implementations of MCP
workflows are even more complicated and confusing
than it was back then
. I personally have not been able to find any novel use case for Agents, not then and not now.
Vibe coding with coding agents like
Claude Code
or
Cursor
is something I have little desire to even experiment with. On paper, coding agents should be able to address my complaints with LLM-generated code reliability since it inherently double-checks itself and it’s able to incorporate the context of an entire code project. However, I have also heard the horror stories of people spending hundreds of dollars by accident and not get anything that solves their coding problems. There’s a fine line between experimenting with code generation and
gambling
with code generation. Vibe coding can get me 80% of the way there, and I agree there’s value in that for building quick personal apps that either aren’t ever released publicly, or are released with disclaimers about its “this is released as-is” nature. But it’s unprofessional to use vibe coding as a defense to ship knowingly substandard code for serious projects, and the only code I can stand by is the code I am fully confident in its implementation.
Of course, the coding landscape is always changing, and everything I’ve said above is how I use LLMs for now. It’s entirely possible I see a post on Hacker News that completely changes my views on vibe coding or other AI coding workflows, but I’m happy with my coding productivity as it is currently and I am able to complete all my coding tasks quickly and correctly.
What’s Next for LLM Users?
#
Discourse about LLMs and their role in society has become bifuricated enough such that making the extremely neutral statement that
LLMs have some uses
is enough to justify a barrage of harrassment. I strongly disagree with AI critic Ed Zitron
about his assertions
that the reason the LLM industry is doomed because OpenAI and other LLM providers can’t earn enough revenue to offset their massive costs as LLMs have no real-world use. Two things can be true simultaneously: (a) LLM provider cost economics are too negative to return positive ROI to investors, and (b) LLMs are useful for solving problems that are meaningful and high impact, albeit not to the AGI hype that would justify point (a). This particular combination creates a frustrating gray area that requires a nuance that an ideologically split social media can no longer support gracefully. Hypothetically, If OpenAI and every other LLM provider suddenly collapsed and no better LLM models would ever be trained and released, open-source and permissively licensed models such as
Qwen3
and
DeepSeek R1
that perform comparable to ChatGPT are valid
substitute goods
and they can be hosted on dedicated LLM hosting providers like
Cerebras
and
Groq
who can actually make money on each user inference query. OpenAI collapsing would not cause the end of LLMs, because LLMs are useful
today
and there will always be a nonzero market demand for them: it’s a bell that can’t be unrung.
As a software engineer — and especially as a data scientist — one thing I’ve learnt over the years is that it’s always best to use the right tool when appropriate, and LLMs are just another tool in that toolbox. LLMs can be both productive and counterproductive depending on where and when you use them, but they are most definitely not useless. LLMs are more akin to forcing a square peg into a round hole (at the risk of damaging either the peg or hole in the process) while doing things without LLM assistance is the equivalent of carefully defining a round peg to pass through the round hole without incident. But for some round holes, sometimes shoving the square peg through and asking questions later makes sense when you need to iterate quickly, while sometimes you have to be more precise with both the peg and the hole to ensure neither becomes damaged, because then you have to spend extra time and money fixing the peg and/or hole.
…maybe it’s okay if I ask an LLM to help me write my metaphors going forward.
