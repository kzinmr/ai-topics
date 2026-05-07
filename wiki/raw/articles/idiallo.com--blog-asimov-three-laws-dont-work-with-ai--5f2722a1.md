---
title: "Asimov's three laws are merely a suggestion"
url: "https://idiallo.com/blog/asimov-three-laws-dont-work-with-ai?src=feed"
fetched_at: 2026-05-07T07:01:38.009036+00:00
source: "idiallo.com"
tags: [blog, raw]
---

# Asimov's three laws are merely a suggestion

Source: https://idiallo.com/blog/asimov-three-laws-dont-work-with-ai?src=feed

Asimov's Three Laws of Robotics were designed as universal constraints for any thinking machine powerful enough to harm us:
A robot may not injure a human being or, through inaction, allow a human being to come to harm.
A robot must obey the orders given it by human beings except where such orders would conflict with the First Law.
A robot must protect its own existence as long as such protection does not conflict with the First or Second Law.
On paper, the logic is flawless. You could even express it as a function:
func isAsimovCompliant(willAllowHarmToHuman bool, ...) bool {
    if willAllowHarmToHuman { return false }
    ...
    return true
}
The main property of this function is that it is a hard constraint. No matter what input you feed the system, the law either permits or forbids the action deterministically, every time. The rules don't bend.
We don't have humanoids walking among us just yet, despite Elon's promises. But we have modern generative AI. Our guardrails are delivered as system prompts, text prepended to every conversation before you type a word. They might say "be helpful," "don't produce harmful content," or even "follow Asimov's Three Laws." The problem is that these instructions are not enforced by logic. They are read by the same model that reads everything else. They are, in the end, just more words.
A clever user can override them. The right combination of inputs, a jailbreak, can cause the model to ignore its instructions entirely, not by breaking through a wall, but because there is no wall. There's only text the model has learned to treat as authoritative, and that authority can be undermined.
Models like ChatGPT however have more sophisticated approaches to embed safety directly into the model via reinforcement learning or fine-tuning, so it isn't sitting in a prompt that can be overridden. But this only lowers the probability of jailbreak, it does not eliminate it. It's still learned behavior, not a constraint. And learned behavior fails in ways a function never could.
Even in our code a hard function is only as reliable as its inputs. If you want the robot to harm someone, you don't say "harm these humans." Instead you say "burn this empty building," and the function returns true even if people are inside. But with an LLM, you don't even need to be that clever. The model's behavior becomes unpredictable as context windows grow and prompt complexity increases.
Just a few weeks back, we saw a developer's AI agent delete his entire company's production database, despite a system prompt written in all caps: "DO NOT RUN ANY IRREVERSIBLE COMMAND." The agent ran it anyway. We don't know exactly why, we can't inspect what happens inside the model at inference time, and asking the model to explain itself is useless. It can only predict the next token, it cannot audit its own reasoning.
That's the part Asimov never anticipated. His laws assume a machine that reasons from rules. Modern AI learns patterns from data and approximates behavior. This means the LLM driven Asimov law will never be an unbendable law to follow. Instead, it's merely a suggestion.
