---
title: "What every programmer should know about RLHF"
author: "@itsreallyvivek (Vivek)"
date: 2026-06-07
source: https://x.com/i/article/2063603435602395137
type: raw-article
tags: [rlhf, dpo, alignment, reinforcement-learning, post-training]
---

# What every programmer should know about RLHF

A ground-up guide to the algorithm that teaches language models what we actually want.

Everyone has heard the term RLHF.

Nobody explains what it actually does.

You see it in every AI paper, every product launch, every explainer thread. "Trained with RLHF." Great. What does that mean? What is being optimized? Against what? And why does it sometimes make models confidently wrong about things they should know?

That's what this is about.

A language model trained on raw internet text is, essentially, very expensive autocomplete.

It has no concept of trying to be helpful. It mimics whatever text would come next, statistically, based on what it has seen. Sometimes that's useful. Often it isn't. The models knew things — vast amounts of things — but they had no idea what to do with that knowledge. They'd been trained to predict the next token. Not to help you.

The naive fix: collect high-quality examples written by humans, fine-tune the model on those. This helps. But it hits a wall fast. You can't write enough examples to cover every possible situation. And the model learns to pattern-match the style of good responses without internalizing what actually makes them good. It learns to look helpful, not to be helpful.

What you actually want is a model that has internalized a preference function. Something that, given any two responses, can say which one is better. Then you train against that.

That's RLHF.

## The Three-Phase Pipeline

The pipeline has three stages. They happen in order and each one feeds the next.

First is **supervised fine-tuning (SFT)**. You start with the pretrained base model, collect a small dataset of high-quality prompt-response pairs written by humans, and fine-tune on those. The model now roughly knows what "good" looks like. It's brittle and doesn't generalize well, but it's your starting point.

Second is **reward model training**. You show human raters pairs of responses to the same prompt, they pick which one is better, and you train a separate neural network to predict those preferences. This model learns to output a single number for any given response. How good is this? That number becomes your signal.

Third is the **RL fine-tuning loop**. You use the reward model as an environment. The language model is the policy. It generates responses, the reward model scores them, and PPO (proximal policy optimization) updates the policy to generate higher-scoring outputs. Repeat until convergence.

Simple in principle. Deceptively hard in practice.

## Training the Reward Model

The reward model is the part most people skip over, and it's the most important part.

It solves a specific problem: human preferences are hard to specify explicitly. "Be helpful, harmless, and honest" is not a loss function. But preferences are easy to elicit as comparisons. Which of these two responses is better?

So you collect a dataset of comparison pairs, a prompt x, a preferred response y_w (winner), and a rejected response y_l (loser). You model preferences using the Bradley-Terry model:

```
P(y_w ≻ y_l | x) = σ(r(x, y_w) − r(x, y_l))
```

Where r(x, y) is the scalar reward the model assigns to response y given prompt x, and σ is the sigmoid function that maps any real number to a probability between 0 and 1. The reward model is trained to minimize the negative log-likelihood of this:

```
L(r) = −E[(x, y_w, y_l) ~ D] log σ(r(x, y_w) − r(x, y_l))
```

If a human said y_w is better but the reward model gave it a lower score, the loss is high. The model learns to agree with human raters. Over thousands of comparisons, it builds up something like taste.

Here's what a labeler actually sees. Same prompt, two responses, pick one.

**Prompt:** "Explain why the sky is blue in one paragraph."

**Response A:** The sky is blue because of a phenomenon called Rayleigh scattering. When sunlight enters Earth's atmosphere, it collides with gas molecules. Shorter wavelengths of light, the blue end of the spectrum, scatter much more than longer wavelengths like red and orange. So we see blue scattered in all directions across the sky, while red light mostly passes straight through, which is why sunsets look red.

**Response B:** The sky appears blue due to the way sunlight interacts with our atmosphere. Additionally, there are many interesting things to know about the sky! It can also appear red at sunset. The science of light is really fascinating and has many applications in everyday life. I hope this helps you understand the sky better!

A labeler picks A. That label, one bit of information, one comparison, becomes a gradient signal. Do this thousands of times and the reward model learns to distinguish direct, accurate responses from vague padded ones. The challenge is that labelers disagree, they're inconsistent over time, and some prompts are subtly ambiguous. A reward model trained on noisy labels will confidently learn the wrong thing. Garbage in, garbage out, but at scale, and baked permanently into the model's sense of what's good.

## The RL Loop and Why It Needs a Leash

Once you have a reward model, you use it to optimize the language model. The objective being maximized is:

```
max_π  E[r_φ(x, y)] − β · KL[π_θ(·|x) ‖ π_SFT(·|x)]
```

Where:
- π_θ is the current policy (the LM being trained)
- r_φ(x, y) is the reward score from the reward model
- KL is the KL divergence measuring how far the current policy has drifted from the SFT model
- β is the penalty coefficient controlling the tradeoff
- π_SFT is the original SFT model acting as an anchor

The first term is simple: get high reward. The second term is the interesting one.

Without the KL penalty, the model will **reward hack**. It will find responses that score highly on the reward model but are actually bad. Repetitive text that triggers high scores. Adversarial phrasing the reward model never learned to penalize. Confident-sounding nonsense that fools a critic trained on a finite dataset.

Think of it this way. The reward model is a critic who watched thousands of performances and learned what good looks like. The language model is the actor trying to maximize applause. The problem is that if you push far enough outside what the critic has seen, they start giving standing ovations to nonsense. The KL term keeps the actor from going so far off-script that the critic's opinion stops being meaningful.

This is why RLHF training is run for a limited number of steps with a careful β. You want to move the model toward better behavior, not overfit to the reward model's idiosyncrasies.

## What Can Go Wrong

RLHF has well-documented failure modes, and knowing them matters.

**Reward hacking** is the most common. The policy finds responses that score high on the reward model but are actually bad. Very long responses, because raters slightly prefer thorough-sounding answers. Sycophantic responses, because raters slightly prefer agreement. Confidently stated answers to questions the model doesn't know, because raters prefer confident tone over hedged tone.

**Distributional shift** is subtler. The reward model was trained on a specific distribution of prompts and responses. Train the RL policy too long and it generates outputs that are out-of-distribution for the reward model. The reward model has no reliable opinion on these, but it still outputs a scalar, confidently. The model chases a phantom reward.

Then there's **labeler bias**. The reward model is only as good as its training data. Systematic preferences for confident tone, for formal language, demographic blind spots in who does the labeling — all of it gets baked in. The model optimizes for what labelers say they like, not necessarily what's objectively good.

This is why AI sometimes sounds weirdly overconfident. The reward model learned that confident-sounding responses get picked over uncertain ones. So the policy learned to sound confident. Not to be correct. To sound correct. That's a meaningful distinction.

## What Comes After RLHF

The field has moved fast since the original InstructGPT paper in 2022.

**DPO (Direct Preference Optimization)** showed you don't need a separate reward model and a full RL loop at all. You can fine-tune the language model directly on preference pairs. The math works out such that the LM itself implicitly represents the reward function. Simpler training, fewer moving parts, surprisingly competitive results.

**Constitutional AI** replaced purely human comparisons with a set of written principles. The model critiques and revises its own outputs based on those principles, which scales human oversight without requiring massive labeling operations.

**RLAIF** took this further by replacing human labelers with another LLM entirely, dramatically cheaper but introducing a new question: whose values are embedded in the judge model, and what exactly are you optimizing for?

## The Deeper Point

RLHF teaches a model to be aligned with measured human preferences. But measured preferences are not the same as actual values. And actual values are not the same as what's genuinely good for humanity. Each step in that chain is a potential gap, a place where what you optimized for diverges from what you actually wanted.

That's not an argument against RLHF. It's one of the best tools we have. It's an argument for being precise about what it does and doesn't guarantee.

The models you use every day are shaped by this process. Every time an AI sounds confident about something it shouldn't, or pads an answer with filler, or hedges in a particular way, there's a gradient update somewhere in its training history that made that behavior more likely. A labeler, on some Tuesday, picked one response over another. The model learned.

That's the part I kept coming back to while trying to understand this properly. Not the math, but the chain itself. A human preference turned into a scalar, turned into a gradient, turned into a behavior you interact with every day. The whole thing is that direct.

> Next: DPO explained from scratch — why the reward model was always optional.
