---
title: "Why output caching doesn't work"
url: "https://seangoedecke.com/why-output-caching-doesnt-work/"
fetched_at: 2026-11-21T10:01:11.603827+00:00
source: "seangoedecke.com"
tags: [blog, raw]
---

# Why output caching doesn't work

Source: https://seangoedecke.com/why-output-caching-doesnt-work/

LLM inference economics depends on caching
1
model inputs, to prevent the entire conversation history being recomputed on each message
2
. Should we cache model
outputs
in the same way? As it turns out, no.
Why cache outputs?
First, here’s why we might think caching outputs is a good idea. We cache inputs to prevent repeated work, but LLMs do a lot of repeated work in their output as well:
When I get agents to write PRs I often ask them to repeat and explain relevant code snippets in the conversation
Long-running agent investigations produce lots of evidence docs, but also need to quote from those docs when they respond to the user
Every time I’ve played around with automated AI research I’ve asked the agent to repeat some sample model outputs so I can make my own qualitative check
In all of these cases
3
I could go and read the files myself, but I don’t. Agents produce such a volume of output, and reading agent output is tiresome, so it’s better to simply ask for the key points.
It’s an obvious waste of tokens
4
to repeat all of this content. In fact, it’s worse than the input caching situation, because it’s a waste of
output
tokens, which are significantly more expensive to produce
5
than input tokens are to ingest.
How could we cache outputs?
If you want to prevent this, you’d have to get the model to avoid repeating itself. For instance, you could fine-tune or prompt a coding model to output “src/script.py:12-15” instead of simply regurgitating those lines of the file.
More generally, you could fine-tune a model to reference segments of its own conversation history instead of repeating them. The harness could then trivially expand those references with the actual content, so all of this is transparent to the user.
Why caching outputs is probably a bad idea
Unfortunately none of this is a good idea, because
it only optimizes visible output
. I don’t
think
models repeat themselves often in their internal chain of thought
6
. I can’t read frontier chains of thought, but my sense from open models and general principles is that they shouldn’t need to, because that information is already available to them. So optimizing repetition only optimizes the segment of model output that is visible to the user. How much is that?
Based on my own agent histories, it’s about 6%. 50% of output tokens are reasoning tokens, and the remaining 44% are tool calls
7
. So we’re running headlong into
Amdahl’s law
: even if you can save two-thirds of the tokens in visible output (a ridiculously optimistic estimate), you’re still only saving 4% of total output tokens.
How to save output tokens
If you want to save output tokens, you need to reduce the 94% of output tokens that are invisible, which largely depends on
intelligence
. The smarter the model
8
, the fewer reasoning tokens and tool calls it needs to get to the right answer. This is why we see a strange phenomenon
9
where more expensive models are actually cheaper to use: they might be 5x more expensive per-token, but they can get to the right answer with 6x fewer tokens, so the overall cost is less.
