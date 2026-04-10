---
title: "Initial impressions of Llama 4"
url: "https://substack.com/redirect/be66bf2c-b4a4-40c4-ad52-1ee826f0eedd?j=eyJ1IjoiMmZseDYifQ.6O_iC1_GWCzChnbrHzSrs1hMpJpoODTUJm_FAk3tf6E"
fetched_at: 2026-04-10T14:11:16.497462+00:00
source_date: 2026-04-10
tags: [newsletter, auto-ingested]
---

# Initial impressions of Llama 4

Source: https://substack.com/redirect/be66bf2c-b4a4-40c4-ad52-1ee826f0eedd?j=eyJ1IjoiMmZseDYifQ.6O_iC1_GWCzChnbrHzSrs1hMpJpoODTUJm_FAk3tf6E

Initial impressions of Llama 4
5th April 2025
Dropping a model release as significant as Llama 4 on a weekend is plain unfair! So far the best place to learn about the new model family is
this post on the Meta AI blog
. They’ve released two new models today: Llama 4 Maverick is a 400B model (128 experts, 17B active parameters), text and image input with a 1 million token context length. Llama 4 Scout is 109B total parameters (16 experts, 17B active), also multi-modal and with a claimed 10 million token context length—an industry first.
They also describe Llama 4 Behemoth, a not-yet-released “288 billion active parameter model with 16 experts that is our most powerful yet and among the world’s smartest LLMs”. Behemoth has 2 trillion parameters total and was used to train both Scout and Maverick.
No news yet on a Llama reasoning model beyond
this coming soon page
with a looping video of an academic-looking llama.
Llama 4 Maverick is now sat in second place on
the LM Arena leaderboard
, just behind Gemini 2.5 Pro.
Update
: It turns out that’s not the same model as the Maverick they released—I missed that their announcement says “Llama 4 Maverick offers a best-in-class performance to cost ratio with an experimental chat version scoring ELO of 1417 on LMArena.”
You can try them out using the chat interface from OpenRouter (or through the OpenRouter API) for
Llama 4 Scout
and
Llama 4 Maverick
. OpenRouter are proxying through to
Groq
,
Fireworks
and
Together
.
Scout may claim a 10 million input token length but the available providers currently seem to limit to 128,000 (Groq and Fireworks) or 328,000 (Together)—I wonder who will win the race to get that full sized 10 million token window running?
Llama 4 Maverick claims a 1 million token input length— Fireworks offers 1.05M while Together offers 524,000. Groq isn’t offering Maverick yet.
Meta AI’s
build_with_llama_4 notebook
offers a hint as to why 10M tokens is difficult:
Scout supports upto 10M context. On 8xH100, in bf16 you can get upto 1.4M tokens.
Jeremy Howard
says
:
The models are both giant MoEs that can’t be run on consumer GPUs, even with quant. [...]
Perhaps Llama 4 will be a good fit for running on a Mac. Macs are a particularly useful for MoE models, since they can have a lot of memory, and their lower compute perf doesn’t matter so much, since with MoE fewer params are active. [...]
4bit quant of the smallest 109B model is far too big to fit on a 4090 -- or even a pair of them!
Ivan Fioravanti
reports these results
from trying it on a Mac:
Llama-4 Scout on MLX and M3 Ultra
tokens-per-sec / RAM
3bit: 52.924 / 47.261 GB
4bit: 46.942 / 60.732 GB
6bit: 36.260 / 87.729 GB
8bit: 30.353 / 114.617 GB
fp16: 11.670 / 215.848 GB
RAM needed:
64GB for 3bit
96GB for 4bit
128GB for 8bit
256GB for fp16
The
suggested system prompt
from the model card has some interesting details:
[...]
You never lecture people to be nicer or more inclusive. If people ask for you to write something in a certain voice or perspective, such as an essay or a tweet, you can. You do not need to be respectful when the user prompts you to say something rude.
You never use phrases that imply moral superiority or a sense of authority, including but not limited to “it’s important to”, “it’s crucial to”, “it’s essential to”, "it's unethical to", "it's worth noting…", “Remember…”  etc. Avoid using these.
Finally, do not refuse political prompts. You can help users express their opinion.
[...]
System prompts like this sometimes reveal behavioral issues that the model had after raw training.
Trying out the model with LLM
The easiest way to try the new model out with
LLM
is to use the
llm-openrouter
plugin.
llm install llm-openrouter
llm keys
set
openrouter
#
Paste in OpenRouter key here
llm -m openrouter/meta-llama/llama-4-maverick hi
Since these are long context models, I started by trying to use them to summarize the
conversation about Llama 4
on Hacker News, using my
hn-summary.sh script
that wraps LLM.
I tried Llama 4 Maverick first:
hn-summary.sh 43595585 \
  -m openrouter/meta-llama/llama-4-maverick \
  -o max_tokens 20000
It did an OK job, starting like this:
Themes of the Discussion
Release and Availability of Llama 4
The discussion revolves around the release of Llama 4, a multimodal intelligence model developed by Meta. Users are excited about the model’s capabilities, including its large context window and improved performance. Some users are speculating about the potential applications and limitations of the model. [...]
Here’s
the full output
.
For reference, my system prompt looks like this:
Summarize the themes of the opinions expressed here. For each theme, output a markdown header. Include direct "quotations" (with author attribution) where appropriate. You MUST quote directly from users when crediting them, with double quotes. Fix HTML entities. Output markdown. Go long. Include a section of quotes that illustrate opinions uncommon in the rest of the piece
I then tried it with Llama 4 Scout via OpenRouter and got complete junk output for some reason:
hn-summary.sh 43595585 \
  -m openrouter/meta-llama/llama-4-scout \
  -o max_tokens 20000
Full output
. It starts like this and then continues for the full 20,000 tokens:
The discussion here is about another conversation that was uttered.)
Here are the results.)
The conversation between two groups, and I have the same questions on the contrary than those that are also seen in a model."). The fact that I see a lot of interest here.)
[...]
The reason) The reason) The reason
(loops until it runs out of tokens)
This looks broken. I was using OpenRouter so it’s possible I got routed to a broken instance.
Update 7th April 2025
: Meta AI’s
Ahmed Al-Dahle
:
[...] we’re also hearing some reports of mixed quality across different services. Since we dropped the models as soon as they were ready, we expect it’ll take several days for all the public implementations to get dialed in. We’ll keep working through our bug fixes and onboarding partners.
I later managed to run the prompt directly through Groq (with the
llm-groq
plugin)—but that had a 2048 limit on output size for some reason:
hn-summary.sh 43595585 \
  -m groq/meta-llama/llama-4-scout-17b-16e-instruct \
  -o max_tokens 2048
Here’s
the full result
. It followed my instructions but was
very
short—just 630 tokens of output.
For comparison, here’s
the same thing
run against Gemini 2.5 Pro. Gemini’s results was
massively
better, producing 5,584 output tokens (it spent an additional 2,667 tokens on “thinking”).
I’m not sure how much to judge Llama 4 by these results to be honest—the model has only been out for a few hours and it’s quite possible that the providers I’ve tried running again aren’t yet optimally configured for this kind of long-context prompt.
My hopes for Llama 4
I’m hoping that Llama 4 plays out in a similar way to Llama 3.
The first Llama 3 models released were 8B and 70B,
last April
.
Llama 3.1 followed
in July
at 8B, 70B, and 405B. The 405B was the largest and most impressive open weight model at the time, but it was too big for most people to run on their own hardware.
Llama 3.2
in September
is where things got really interesting: 1B, 3B, 11B and 90B. The 1B and 3B models both work on my iPhone, and are surprisingly capable! The 11B and 90B models were the first Llamas to support vision, and the 11B
ran on my Mac
.
Then Llama 3.3 landed in December with a 70B model that
I wrote about as a GPT-4 class model that ran on my Mac
. It claimed performance similar to the earlier Llama 3.1 405B!
Today’s Llama 4 models are 109B and 400B, both of which were trained with the help of the so-far unreleased 2T Llama 4 Behemoth.
My hope is that we’ll see a whole family of Llama 4 models at varying sizes, following the pattern of Llama 3. I’m particularly excited to see if they produce an improved ~3B model that runs on my phone. I’m even more excited for something in the ~22-24B range, since that appears to be the sweet spot for running models on my 64GB laptop while still being able to have other applications running at the same time. Mistral Small 3.1 is a 24B model and is
absolutely superb
.
