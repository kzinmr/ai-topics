---
title: "LLM-generated skills work, if you generate them afterwards"
url: "https://seangoedecke.com/generate-skills-afterwards/"
fetched_at: 2026-04-30T07:01:10.416024+00:00
source: "seangoedecke.com"
tags: [blog, raw]
---

# LLM-generated skills work, if you generate them afterwards

Source: https://seangoedecke.com/generate-skills-afterwards/

LLM
“skills”
are a short explanatory prompt for a particular task, typically bundled with helper scripts. A recent
paper
showed that while skills are useful to LLMs,
LLM-authored
skills are not. From the abstract:
Self-generated skills provide no benefit on average, showing that models cannot reliably author the procedural knowledge they benefit from consuming
For the moment, I don’t really want to dive into the paper. I just want to note that the way the paper uses LLMs to generate skills is bad, and you shouldn’t do this. Here’s how the paper prompts a LLM to produce skills:
Before attempting to solve this task, please follow these steps: 1. Analyze the task requirements and identify what domain knowledge, APIs, or techniques are needed. 2. Write 1–5 modular skill documents that would help solve this task. Each skill should: focus on a specific tool, library, API, or technique; include installation/setup instructions if applicable; provide code examples and usage patterns; be reusable for similar tasks. 3. Save each skill as a markdown file in the environment/skills/ directory with a descriptive name. 4. Then solve the task using the skills you created as reference
The key idea here is that they’re asking the LLM to produce a skill
before
it starts on the task. It’s essentially a strange version of the “make a plan first” or “think step by step” prompting strategy. I’m not at all surprised that this doesn’t help, because current reasoning models already think carefully about the task before they begin.
What should you do instead? You should
ask the LLM to write up a skill
after
it’s completed the task
. Obviously this isn’t useful for truly one-off tasks. But few tasks are truly one-off. For instance, I’ve recently been playing around with
SAEs
and trying to clamp features in open-source models, a la
Golden Gate Claude
. It took a while for Codex to get this right. Here are some things it had to figure out:
Extracting features from the final layernorm is too late - you may as well just boost individual logits during sampling
You have to extract from about halfway through the model layers to get features that can be usefully clamped
Training a SAE on ~10k activations is two OOMs too few to get useful features. You need to train until features account for >50% of variance
Once I was able (with Codex’s help) to clamp an 8B model and force it to obsess about a subject
, I
then
asked Codex to summarize the process into an agent skill
. That worked great! I was able to spin up a brand-new Codex instance with that skill and immediately get clamping working on a different 8B model. But if I’d asked Codex to write the skill at the start, it would have baked in all of its incorrect assumptions (like extracting from the final layernorm), and the skill wouldn’t have helped at all.
In other words, the purpose of LLM-generated skills is to get it to distil the knowledge it’s gained by iterating on the problem for millions of tokens, not to distil the knowledge it already has from its training data. You can get a LLM to generate skills for you,
so long as you do it
after
the LLM has already solved the problem the hard way
.
Here's a preview of a related post that shares tags with this one.
