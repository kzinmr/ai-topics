---
title: "Should Developers Care about Interpretability?"
author: "Thariq Shihipar"
source_url: "https://www.thariq.io/blog/interpretability/"
date: "2024-11-04"
theme: "AI interpretability and steering"
ingested: "2026-04-14"
updated: "2026-05-08"
---

# Should Developers Care about Interpretability?

**Author:** Thariq Shihipar (@trq212, Anthropic Claude Code team)
**Original URL:** https://www.thariq.io/blog/interpretability/
**Date:** 2024-11-04 · 6 min read

---

Arguably the biggest breakthrough in LLM research this year has been in interpretability — the ability to understand what a LLM is "thinking."

The most famous example is Anthropic's [Golden Gate Claude](https://www.anthropic.com/news/golden-gate-claude), though this work isn't limited to text — researchers are also working on [images](https://featurelab.xyz/), [voice](https://x.com/GopalKRaman/status/1832200457621557594/video/1) and even [protein models](https://www.nature.com/articles/s41587-024-0206-x).

But while interpretability is most often discussed in the context of research & AI safety, it also offers a promise to developers of more fine-grained control and reliability from their models.

## How does Interpretability and Steering work?

The best foundational explanation is in the [Golden Gate Claude](https://www.anthropic.com/news/golden-gate-claude) paper which is both thorough and easy to read, but summarized from the view of an AI dev:

**Interpretability:**
- You can break down a LLM into a set of 'features' which describe different concepts (e.g. The Golden Gate Bridge, the arabic language, etc.)
- Given some text input, you can figure out which features activate in the LLM's "brain." This happens quickly, cheaply and reliably — the same text will always activate the same features.

**Steering:**
- When generating, you can activate a particular feature at a particular intensity.
- Different features at different intensities will have different effects. For example, the Arabic feature at sufficient intensity will make your model speak Arabic. Turning up the Golden Gate Bridge feature all the way will make your model think it IS the Golden Gate Bridge.
- You can steer on the fly by activating and deactivating features based on the tokens and other features you observe. For example, when you detect the start of a coding sequence, you might amplify certain coding-related features.

## The Promise

At the Anthropic hackathon, Dario Amodei described how "interpretability" is maybe not the right word to describe what they are doing.

The other side of interpretability is **steering, preciseness & reliability**. If interpretability delivers on its promise, developers should have a level of control over their models that has not been possible thus far.

## What are the applications?

### 1. Capturing style that cannot be described in words

One of the hardest problems with LLMs is capturing and reproducing a specific style.

In a prompt you might say "friendly and concise," but you might actually want something like "70% friendly, 50% concise, 80% professional." Or you may want to emulate a specific person, but find that "be more like [person]" doesn't work.

Interpretability and steering allows you to break down a style into a set of features, and then steer the model by activating and deactivating those features. Research is already showing that you can steer text, voice, and images.

**Examples:**
- **Text Styles**: Linus writes about [steering text generation](https://thesephist.com/posts/prism/) by training a text embedding classifier. [Goodfire.ai](https://x.com/GoodfireAI/status/1839002465984741745) provides a tool for steering llama models based on detected features.
- **Voice Styles**: [Hume](https://x.com/GopalKRaman/status/1832200457621557594/video/1) breaks down voice into components, letting you tune features like "nasal" or "crisp."
- **Image Styles**: [Featurelab.xyz](http://Featurelab.xyz) by Gytis shows how images can be broken down into distinct features, and how you can generate images by composing features together.

### 2. Less need for RLHF

RLHF (and related techniques) have so far been the primary way of creating a system personality (e.g. concise, helpful) and imposing system limits (e.g. do not respond about topics related to racism).

The problem is that RLHF famously has side effects. It can lead to "false refusals" where the AI refuses to do something it can do (the Llama paper cites 1-5% of new false refusals), and sometimes degrades quality (e.g. RLHF to be more concise can make a model respond with code comments that just say "fill in the code").

Steering potentially allows us to react **only if** we see a feature activate (e.g., Anthropic has detected a ['scam emails'](https://transformer-circuits.pub/2024/scaling-monosemanticity/features/index.html?featureId=34M_15460472) feature) and implement an intervention only then — by activating another feature or deactivating the problematic one.

It also allows us to choose a personality for the model by choosing particular personality and response features to activate (e.g. a [sycophantic](https://transformer-circuits.pub/2024/scaling-monosemanticity/features/index.html?featureId=1M_847723) feature).

There has even been work on 'uncensoring' RLHFed models through a technique called [abliteration](https://huggingface.co/blog/mlabonne/abliteration).

Most promisingly, steering happens at **inference time** — unlike RLHF which happens in post-training. This means API developers should be able to choose how the model is steered more specifically, vs. having to rely on the model providers making large blanket choices that affect everyone via RLHF.

### 3. Remembering User Preferences vs User Requests

When chatting, a user may give a *request* like "tell me the capital of France" or they may state a **preference** like "please respond more briefly" or "speak in Arabic."

Over the course of a long conversation, these preferences may be lost in the context window. But steering allows you to recognize an important preference and save it permanently, making sure your AI always responds more briefly.

### 4. Cheap, Fast, Reproducible Classification

You may have a bunch of examples of emails you would describe as spam, but no concise way to describe to the AI what "spam" means. Currently, you could give GPT-4o-mini 100 examples and ask it to classify each email — not bad, but a bit unreliable and costly.

With interpretability, you can give the AI a large set of spam emails and see what features activate the most compared to non-spam emails. Building this set of "spam features" allows you to create a cheap spam classifier without training a separate model.

## What are the downsides?

### 1. Moving the model 'out of distribution'

Steering is like brain surgery; prompting is like asking politely. Steering a model to overweight a feature can cause it to not just bring it up excessively (e.g., Golden Gate Claude thinking it IS the Golden Gate Bridge), but also to generate incoherent text or text that doesn't follow the rules of language.

### 2. Not understanding what a feature does

Features are labeled by a mixture of humans and machines reading lists of outputs triggered by features. However, labeling is still early — browsing lists of features, Shihipar sometimes finds himself disagreeing with how they're labeled.

Given tens or hundreds of thousands of features, some will certainly be mislabeled or misunderstood, making steering less reliable.

### 3. Activating other features & circuits

Some features activate other features in ways that are complex to understand (sometimes called "circuits"). We may introduce side effects while activating a feature, in the same way RLHF introduces side effects.

There has been no wide-scale use of feature steering (unless Anthropic is doing it under the hood), so it's hard to tell what side effects they might produce.

## Conclusion

While many interpretability features are still too early to show consistent reliability, they promise developers a lot more fine-grained control of models.

As a tradeoff, we should expect next-gen model APIs to get a lot more powerful but also more complicated — requiring more than just prompting and RAG to get the outputs we want.

---

## Key Concepts

- **Interpretability**: Breaking down an LLM into discrete 'features' and detecting which activate for given inputs
- **Activation Steering / Feature Steering**: Clamping or amplifying specific features during generation to control model behavior
- **Monosemanticity**: The property that a feature corresponds to a single, coherent concept (Anthropic's scaling monosemanticity research)
- **Abliteration**: Technique for removing refusal behavior by identifying and suppressing refusal-related directions in activation space
- **Circuits**: Interconnected features that activate each other in complex, sometimes unpredictable ways
- **RLHF vs Steering tradeoff**: RLHF is post-training (provider-controlled, blanket); steering is inference-time (developer-controlled, targeted)
