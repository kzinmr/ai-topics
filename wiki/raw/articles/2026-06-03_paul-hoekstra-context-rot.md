# Context Rot: Why AI Gets Worse the More You Explain

**Author:** Paul Hoekstra | **Source:** Paul's Pipeline (Substack)
**URL:** https://paulhoekstra.substack.com/p/context-rot-the-constraint-agentic
**Published:** June 3, 2026

## Summary

Context rot is the steady decline in how reliably a model uses what is in its context, the more you put there. The drift you feel when an AI keeps missing the point is not a bug — it is built into how transformer models work, and you can design around it. Agents, which fill the context fastest, hit it hardest.

## Key Benchmark Evidence

- **OpenAI MRCR v2** (8-needle test): buries eight specific items in distractor text, input grows from 8K to 500K tokens. Every line slopes down: GPT-5.5 leads but still falls to 54% by half a million; Grok 4.20 (sold on a 2M-token window) is down at 12%.
- **Chroma study (July 2025)**: found the same decay shape across 18 frontier models, in a study literally called "Context Rot." A generation newer models did not change the shape.
- **SkillsBench**: a model handed the one-page guide that fit beat a stronger model working with no guide at all — the right context can swing a model hard, but more is not better.
- **Chroma finding**: a short, focused prompt beat the same answer buried in 113K tokens of context, on every model tested.

## How a Language Model Works (Background)

1. **Words become numbers** — each token becomes a vector/embedding on a map of meaning; similar words sit close together.
2. **A tall stack of layers** — the transformer stack (dozens to 100+ layers); each layer hands a sharper version up.
3. **Attention: words reading each other** — inside a layer, every word looks back at earlier words and rates relevance; the word rewrites itself as a blend of attended words.
4. **Order has to be added on** — attention has no innate sense of word order, so position is encoded deliberately (e.g., RoPE).
5. **The last word becomes the next one** — the model scores every known word for next-token probability, picks one (temperature = randomness), and repeats.

## What Context Rot Is

The gap between two numbers that sound alike:
- **Nominal context**: how much you can physically cram in before the model refuses.
- **Functional context**: the length where it still does your task well.

Functional is always smaller, and the gap widens the more you load in.

## Three Causes (They Stack)

### Reason 1: Attention is a pie that never gets bigger
Inside every layer, each word's attention pulls are shares of a single pie (softmax), always summing to the whole regardless of word count. Split the pie across a million words and every slice thins. Not a bug waiting for a patch — it is the cost of making slices sum to one. Liu et al. "Lost in the Middle" (2023) measured it directly: accuracy sags in the middle of long inputs; a bigger window just means more middle.

### Reason 2: The model loses track of where things are
Position is fed in deliberately (RoPE turns each word's position into an angle, like a clock hand). One full turn covers the range the model was built/tuned for — 8K-32K tokens for most current models. Feed it a million tokens and it laps the dial repeatedly; positions at 412K and 478K have hands pointing almost the same way, so the model reads them as the same distance. This is why writing stays fluent while the model loses the plot — local writing needs only short distances; finding one fact in 400K tokens needs a long distance out where angles have collapsed. Rescaling tricks (YaRN and friends) keep writing fluent but do not teach the model what the crowded angles mean — it stays fluent and stays lost.

### Reason 3: The model barely practised at long lengths
Training data is mostly short (web pages, code files, articles, forum posts — vast majority under 8K tokens). Long-context fine-tuning data is thinner still; clean long examples are expensive, so much is synthetic or repetitive. Behavior at 4K tokens is backed by trillions of tokens of practice; behavior at 100K by a few billion at best, much lower quality. Training exposure at position 2048 is < 5%; > 80% of training exposure is at positions ≤ 1024. No architecture change fixes this — you cannot give the model million-token experience after the fact by changing a formula.

## How to Stay Ahead of It

- **Relevant context runs out**: each thing you add is less useful than the last — value climbs fast then flattens while cost keeps climbing. They cross. Context is not the enemy; **useless context is**.
- **A fresh window does** — resetting is the big lever.
- **Bands are generous on clean benchmark text**: by 128K even the strongest model has shed ~15 points. Real work has vaguer questions and messier documents, so the crossing comes sooner.
- **Find your own crossing**: run the same task at a few lengths on your own data, watch where answers start slipping.
- **Treat numbers as a snapshot**: as long-context training improves, the whole staircase shifts right.
- **Tooling**: in Claude Code, a statusline showing context filling up makes this easy to watch (link to his aquarium statusline article).

## Key Quotes

> "The drift was never about how clearly you explained. It was about how much had piled up behind you."

> "So context is not the enemy. Useless context is."
