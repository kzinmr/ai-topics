---
title: "Why Fine-Tuning is Dead w/ Emmanuel Ameisen (Lecture Transcript)"
author: Emmanuel Ameisen
date: 2024-01-24
date_ingested: 2026-06-15
source: "Hamel Husain's ML/LLM workshop series"
type: transcript
tags:
  - fine-tuning
  - post-training
  - rag
  - prompting
  - anthropic
  - training
  - evaluation
  - context-engineering
  - transcript
related_article: articles/2024-01-24_emeisen_why-fine-tuning-is-dead.md
participants:
  - Emmanuel Ameisen (speaker, Anthropic)
  - Hamel Husain (host, Parlance Labs)
  - Dan Becker (moderator)
  - Simon Willison (questioner)
  - Ian Maurer (questioner, precision oncology)
  - Jake Mannix (questioner)
---

# Why Fine-Tuning is Dead w/ Emmanuel Ameisen

> A hot-take talk from Hamel Husain's ML/LLM workshop series (Jan 24, 2024). Emmanuel Ameisen (Anthropic) argues that fine-tuning is becoming less important relative to prompting, RAG, and in-context learning — and that the trend is accelerating.

**Companion article:** [[raw/articles/2024-01-24_emeisen_why-fine-tuning-is-dead|Summary Article]]

---

## Introduction & Context

**[00:00:00]** Emmanuel introduces the talk as a "hot take" rather than a deep tutorial. The idea came from tweets where he expressed skepticism about fine-tuning, and Hamel challenged him to defend that position.

**[00:00:48]** **Background**: Emmanuel has been doing ML for ~10 years. Data science → ML education → wrote a practical guide on training ML models (mlpower.com) → Staff Manager at Stripe (trained models) → Anthropic (fine-tuning models + interpretability research).

**[00:01:38]** **Hamel plugs** Emmanuel's book as "a classic in applied machine learning."

**[00:01:52]** **Disclaimer**: This talk is Emmanuel's personal opinion, not Anthropic's. Anthropic offers fine-tuning services, so "fine-tuning is dead" wouldn't make sense as an official position.

---

## Part 1: Trends — "Be Afraid of Anything That Sounds Cool"

**[00:02:16]** "I've been training models for 10 years. I don't recommend it."

**[00:02:56]** **The pattern**: In ML, the best way to have impact is to be suspicious of anything that sounds cool. The boring thing almost always delivers more value:

| Year | Cool Thing | What Actually Worked |
|------|-----------|---------------------|
| 2009 | "Train ML models!" | Data analysts writing good SQL queries |
| 2012–14 | "Use deep learning!" | XGBoost / random forests (deep learning was too early) |
| 2015 | "Invent a new loss function!" | Clean your dataset, fix obvious errors (10× improvement, 1/10 effort) |
| 2023 | "Fine-tune your own model!" | Prompt engineering + RAG |

**[00:04:37]** **Key insight**: Fine-tuning sounds very cool. Based on priors alone, we should be suspicious — "it's the coolest thing, probably gonna be the worst use of my time."

### The Historical Trend Chart

**[00:05:18]** Emmanuel draws a chart showing the evolution of practical ML:

1. **Early era**: Everyone trained from scratch (no pre-trained models existed)
2. **Fine-tuning era** (VGG, ResNet, BERT): Pre-trained models became available; fine-tuning on smaller datasets was cheaper and better than training from scratch
3. **Prompting era** (GPT-3+): The original promise of LLMs — you don't need any backward pass at all, just prompt them

**[00:07:01]** "The realistic, not-fun answer is nobody knows. But my hot take is that line goes up — the orange line (prompting/no-training) will keep increasing."

### Q: Could Fine-Tuning Come Back?

**[00:07:39]** **Dan Becker** points out that Emmanuel's "don't do X" advice historically became wrong a few years later (don't train ML → XGBoost; don't do deep learning → deep learning wins).

**[00:08:13]** **Emmanuel**: "Invent a new loss function" is still not a thing you should do, even 10 years later. Some "cool things" never become the right thing. It's hard to know early whether fine-tuning will be in the "invent a loss function" category or the "use deep learning" category.

---

## Part 2: Performance — Fine-Tuning vs. RAG vs. Both

### Simon Willison's Question: What About Embedding Models?

**[00:08:48]** Simon asks whether fine-tuning *embedding models* (not LLMs) is worthwhile, e.g., fine-tuning on blog articles for better semantic search.

**[00:09:07]** **Emmanuel**: Similar question to LLM fine-tuning. If you believe embedding models will keep improving, general embeddings will work well. The edge case is highly domain-specific terminology (e.g., your company's product "XS-23" that nobody outside knows about). For that, combined search (keyword + embedding) works really well.

**[00:10:20]** **Hamel** pushes back: domain-specific retrieval ranking can be very specific and hard to capture in any embedding, no matter how good.

**[00:10:48]** **Emmanuel**: "Fine-tuning is dead" is the hot-take version. The realistic version is "fine-tuning goes from 50% of the effort to 5%." For specific search, maybe you'll always need fine-tuning — or maybe LLMs will drive search via in-context understanding and query expansion.

### The RAG vs. Fine-Tuning Paper

**[00:14:42]** Emmanuel shows a paper comparing fine-tuning vs. RAG on relatively old models. Results:

| Approach | Performance |
|----------|------------|
| Baseline (nothing) | ~6.7 |
| RAG only | ~58 |
| Fine-tuning only | Much less than RAG |
| Fine-tuning + RAG | ~61 (for larger models) |

**[00:15:30]** **Key finding**: For larger models, almost all benefit comes from RAG. Fine-tuning adds marginal improvement (63.13 → 63.29). For smaller models, fine-tuning + RAG helps more.

### Hamel's Important Clarification

**[00:16:15]** **Hamel**: "If your model needs context from your data, you should always do RAG. You don't want to try to fine-tune all of that knowledge. Expecting the model to memorize all your documents is not a good idea."

**[00:17:05]** **Emmanuel**: "This is why your course is good — I don't think this is common knowledge. Fine-tuning isn't really the right solution if you want to add knowledge. That's just not what it's for in most cases."

**[00:17:48]** "If your problem is 'this model doesn't know about our business model,' the solution is not fine-tuning — it's just telling it what your business model is."

### Knowledge vs. Style — A Fuzzy Boundary

**[00:18:57]** **Dan Becker**: We don't know what task is being scored. If you wanted to measure adherence to a writing style book, RAG wouldn't help much — fine-tuning would. "We could pick a task and then tell any story we want."

**[00:19:53]** **Emmanuel**: Agreed. He searched for papers showing fine-tuning beating RAG but found mostly Twitter threads, not rigorous papers. "This is a call for good papers that show fine-tuning winning."

**[00:20:33]** **Hamel**: "The word 'knowledge' is not fine-grained enough." There's a spectrum:
- **World-model knowledge** (physics constants) — the model already has this, no need to retrieve
- **Changing personal facts** — clearly RAG
- **Fuzzy middle ground** — strong intuitions but hard to articulate

**[00:20:58]** **Emmanuel**: "My scaling-pill hot take is that this boundary changes with every model generation." Learning a style of speaking used to require fine-tuning; newer models can learn it from a 2-line prompt.

**[00:21:47]** **Dan**: Knowledge and style may not be cleanly separable even within the model's weights. The concept of "knowledge" as we discuss it may not map to distinct attention heads.

### Ian Maurer's Question: Precision Oncology

**[00:23:07]** Ian describes a complex knowledge base for precision oncology (100K+ hours of curation). He wants to fine-tune a model to create first-draft curations.

**[00:23:45]** **Emmanuel's advice**:
1. **Check the trend**: Compare the smartest and dumbest available model (e.g., Claude 3 family) without fine-tuning. If the next generation will be good enough, wait.
2. **Prompt-test first**: Add examples of what you'd fine-tune on to your prompts. If performance plateaus, you don't need fine-tuning.

### Simon Willison's Follow-up: Does Fine-Tuning Ever Work for Adding Knowledge?

**[00:25:34]** **Emmanuel**: Most "knowledge addition" can be done with prompts or RAG. Fine-tuning on "Emmanuel likes strawberries" only works for that exact question — it doesn't truly *learn* the fact in a way that generalizes to other contexts.

**[00:27:55]** "A lot of fine-tuning ends up in that surface-level realm: in the specific context, for this specific question, shaped like the fine-tuning dataset, I will tell you this thing — versus 'I have now learned that Emmanuel likes strawberries.'"

### Jake Mannix's Question: Multilingual Fine-Tuning

**[00:29:16]** Fine-tuning for underrepresented languages seems to work — models already have cross-lingual representations, so small adjustments help.

**[00:30:07]** **Emmanuel**: Could work because the model already maps concepts across languages. Fine-tuning just needs a small change to extend an existing concept to a new language.

**[00:31:15]** For code models, it's more about **style** (code completion = autocomplete the current line) than knowledge. Code-base knowledge works well with RAG/context.

**[00:32:20]** "I'm not convinced that fine-tuning on your whole code base gives huge gains compared to putting as much of that code base in the context."

### Moving Target: BloombergGPT Example

**[00:33:41]** BloombergGPT pre-trained a finance-specific model that beat GPT-3 on financial tasks. Six months later, GPT-4 came out and was way better at everything.

**[00:34:27]** **Hamel**: If you have a fine-tuning pipeline, can't you just keep fine-tuning the latest model?

**[00:35:36]** **Emmanuel**: Yes, but it's a matter of cost. If your pipeline does RAG + prompting, you can swap models easily. If you have to re-fine-tune, "that gets pretty heavy."

**[00:36:44]** Fine-tuning larger and larger models seems to be getting less effective. "As models get better, basically better at everything, fine-tuning seems less and less impactful."

---

## Part 3: Difficulty — The Real Horror Stories

### The ML Hierarchy of Needs

**[00:38:37]** Even if you're fine-tuning, the optimal use of time is:

| Activity | % of Time |
|----------|----------|
| Data work (collect, label, enrich, clean, debug) | 80% |
| General engineering (serve, monitor, drift detection) | 18% |
| Debugging (model won't train, GPU issues) | 2% |
| Cool architecture research | 0% |

**[00:39:25]** "Machine learning is hard even if you don't train the models." Even with RAG + prompting, you still need: input validation, output validation, monitoring, back-testing, evaluation, train/test splits, A/B testing.

**[00:40:10]** **The reasonable version of the hot take**: "If you talk to me, I will only allow you to do fine-tuning if you've done all of this first."

**[00:40:37]** "The thing that grinds my ears is that people don't do any of this and then fine-tune a model before they even have an eval."

### Hamel's Observation: Nothing Has Changed

**[00:41:02]** **Hamel**: "Looking at data takes up 80% — it's almost the same in classic ML."

**[00:41:28]** **Emmanuel**: "The failure mode is that people just don't want to do this. They go on a side quest to fine-tune instead."

**[00:42:34]** **The right order**: Build eval infrastructure first → work on prompts → then consider fine-tuning.

### Recommended Priority Order

**[00:42:44]** Emmanuel's recommendation:
1. **Eval sets first** — representative, large, easy to run
2. **Spend days on prompts** — "I can't count the times I got someone from 30% to 98% accuracy just by improving the prompt"
3. **Dynamic few-shot examples** — RAG over a database of examples, pulling the most relevant ones (common pattern via LangChain)
4. **Only then** consider anything else

### The AI Engineering Debate

**[00:43:32]** **Hamel**: "The first and last bullet are the same as classic ML. Not much has changed, but there's a narrative that 'AI engineering' is a new profession that doesn't need ML thinking."

**[00:43:58]** **Emmanuel**: "The math has been abstracted away in the form of an API. The gravitational pull of the fun stuff is even stronger now — 'I don't even get to see the Jupyter notebook, I just have an API call.'"

### The Price/Context Trend

**[00:45:10]** The strongest argument for fine-tuning declining:

| Metric | 2021 | 2024 |
|--------|------|------|
| Price (Haiku-class model) | ~$60/M tokens | ~$0.50/M tokens |
| Context window | 2K–4K | 200K–1M+ (10M rumored) |
| Latency | 2 min for 100K | 10 sec for 100K |

**[00:46:36]** "If in 2025/2026 you have a model with 1M+ context, crazy fast, and 10–100× cheaper — you just don't fine-tune. You throw everything in context."

**[00:47:24]** **Fine-tuning's remaining niche**: Use cases well outside context window limits, or where chunking through context is too slow for the application.

**[00:47:34]** **Prefix caching** (Anthropic offers this) changes the equation further — if fine-tuning data can be formulated as a prefix, cached KV reduces the cost of repeated context.

### Jake Mannix: The FLOP Argument

**[00:48:24]** Even with cheap inference, passing 100K tokens through every forward pass is wasteful compared to encoding information once via fine-tuning.

**[00:49:47]** **Emmanuel**: True only if models stay at the same efficiency level. As models get more efficient, the cost decreases. And fine-tuning state-of-the-art models will only get harder.

**[00:51:06]** "A lot of use cases people want to fine-tune on are actually smaller datasets — 500 examples that could fit in 5K context. You have an alternative: immediately get a fine-tuned model by just throwing it in the prompt."

---

## Closing

**[00:53:38]** "It's likely there will always be some use case for fine-tuning. My belief is that the prevalence will get lower and lower. That's maybe the controversial opinion."

**[00:54:00]** The trend chart is "fully a vibe plot, but directionally correct."

**[00:54:41]** **Hamel**: "That's pretty much the most important questions."

---

## Key Takeaways

1. **Fine-tuning is not for adding knowledge** — use RAG or prompting instead
2. **RAG delivers most of the value** in knowledge-heavy applications; fine-tuning adds marginal gains
3. **The boundary between "knowledge" and "style" shifts** with each model generation — what required fine-tuning yesterday can be done with a prompt today
4. **The hierarchy of needs**: evals → prompts → dynamic few-shot → RAG → (maybe) fine-tuning
5. **Price/context trends** are the strongest argument: if models keep getting cheaper, faster, and longer-context, fine-tuning becomes unnecessary for most applications
6. **Fine-tuning's remaining niche**: extreme context requirements, style/format enforcement, and cases where latency budgets can't accommodate long prompts
