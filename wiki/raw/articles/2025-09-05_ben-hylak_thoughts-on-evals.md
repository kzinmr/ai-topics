---
title: "Thoughts on Evals"
source: https://www.raindrop.ai/blog/thoughts-on-evals/
author: Ben Hylak
date: 2025-09-05
publication: Raindrop Blog
type: blog-post
tags:
  - agent-evaluation
  - evals-vs-monitoring
  - production-monitoring
  - ab-testing
  - controversy
---

# Thoughts on Evals

**Author:** Ben Hylak (CTO + Co-Founder of Raindrop)
**Published:** September 5, 2025
**Source:** https://www.raindrop.ai/blog/thoughts-on-evals/

## Context

Evals are an important part of building AI products. We know this first-hand.

Raindrop uses AI to monitor the performance of AI agents. We generate billions of labels a month. We detect issues, generate reports, and automatically cluster intents. We are also constantly changing and optimizing how we detect issues. If we didn't have evals, it would be impossible to make changes without breaking production.

Internally, we use a custom eval platform inspired by evalite. Many of our customers use Langsmith and Braintrust.

We built Raindrop because evals just weren't enough. Our customers pay for Raindrop alongside tools like Braintrust because Braintrust can't tell them what they need to know.

I'm writing this because Ankur, the CEO of Braintrust, recently wrote a blog post directly dismissing A/B tests, and Raindrop specifically (without naming us). In the blog post, Ankur claims that evals are the future. He claims that they help you measure how good your product is, that they are key for rapid experimentation. He also claims that evals will become increasingly important as software becomes more personalized. I believe the opposite to be true for each of these claims.

> "The recent acquisitions of Statsig by OpenAI and Eppo by Datadog hint at the turning point: A/B testing is no longer sufficient for AI product optimization. The future is evals."

*Side Note: For the sake of brevity, I'm going to avoid critiquing some of the stranger, more mind-bending parts of his blog post, like the above quote… which is like saying that Google's acquisition of Windsurf is proof that coding agents are on the way out.*

## But first, what is an eval anyway?

Right now, it feels like everyone is reaching for a new word and calling it progress. "Offline Evals" "Online Evals" "LLM judges" "Scorers". Fancy labels, familiar ideas.

When we blur definitions, we blur decisions. If you strip away the jargon, you have the two levers engineers have always used to understand change:

1. **Testing changes before shipping** (what Braintrust does best)
2. **Measuring what actually happens after shipping** (what Raindrop does best)

Which one matters more? **The answer is the same it has always been: the one that tells you the truth.** And in the age of agents and rapidly changing models, the truth increasingly lives in production.

Intentionally or not, the word "eval" has become increasingly vague. I've seen at least 6 distinct definitions of evals:

1. A known input with **no validator** (e.g. a human, or team of humans, need to review/score the output)
2. A known input, a **known output, deterministic validator** (e.g. string contains X)
3. A known input, expected output, **LLM judge** decides if correct
4. A known input, **human-aligned "LLM as a Judge"** (e.g. score joke funny)
5. **Frontier model evals** — aspirational, for unsolved capability problems
6. **Online evals** — any of 1-4 run on a small sample of production data

(Technically, A/B tests are just a type of "online evals") But when people talk about "evals" in the context of LLM's, they're usually tests. Sometimes smoke tests, other times unit tests. There's usually a test input, and an expected output. Like tests, evals are great at preventing regressions. They're useful sanity checks. They can make local iteration faster as well.

But our customers also want to know how their changes affect real world performance: which tool calls are causing issues, when agents make critical mistakes (deleting critical data, getting stuck in a loop). As agents get more capable, they become more unpredictable and harder to test deterministically.

Monitoring is the solution. It shows you what you don't know. Our customers can ship fast, then definitively answer the question: "Is this change (model, prompt, etc.) better or worse in the real world?" All they have to do is compare to a baseline (and this is what we mean by "A/B" test).

## Claim 1: Evals are the future

**Reality: Test Driven Development is declining in favor of monitoring**

Thirty years ago, shipping software involved a lot of testing. This was for good reason: at the time, software was shipped on CD-ROMs. If a bug was shipped, it could take years to fix.

Luckily for software engineers, things have changed since then. With the advent of the web, and the shift from client to server, bugs can be resolved in just a few minutes.

This shift significantly reduces what you need to test. Instead of meticulously testing every single environment, or debugging why a specific test is so flaky, teams can just test what matters and **ship faster**.

Of course, you should still have tests for critical parts of your codebase. But for everything else, most people rely on monitoring tools like Sentry or Datadog. And, unlike testing, we're seeing monitoring tools close that gap between bug → fix faster than ever. Tools like Seer from Sentry can diagnose an error, pass that context to Cursor, and have a PR reviewer like Greptile approve the PR in under a minute.

In the real world, how fast you can ship and iterate does matter. When building an AI product, speed matters (this is more true than any industry in history). Eppo and Statsig were successful products, growing fast, used by some of the largest companies in history (including OpenAI and Anthropic).

Monitoring/experimentation makes **even more sense** for AI products vs. traditional software. LLM outputs are even less reproducible, even more stochastic. Underlying dependencies (the models) are deprecated faster than anything we've ever seen before in software engineering. There is no such thing as stable.

## Claim 2: Evals measure how good your product is

**Reality: Evals are not a product-quality metric — production performance is.**

You wouldn't brag about how many unit tests your product passes. Using evals to measure how good your product is equally silly. The real test for how good your product is how it performs in the real world.

When writing a new prompt, you often start with an idea of what "good" means. You can easily define a few test cases. But once you ship to production, the cracks start to appear. Users ask for things you never could have imagined. People on your team start to disagree what a "good" response means, for a given input.

That's why the best AI products are defined and built iteratively. There's a strong feedback loop between production and development. It's some juggling act between the inherent limitations of models, which seem to change from week to week, and the needs of your users.

Funny enough, "not knowing the full scope of what you want ahead of time" is one of the most popular criticisms of Test Driven Development (which feels similar to the current wave of Eval Driven Development). And much like evals, you're not supposed to complain about it.

Instead of evals being "the behavior you want", in practice evals are often **adversarially selected**. That means, you (somehow) found a failure case, and then added it to your eval set. As a result, your evals just become a collection of issues you already know about.

How do you discover issues you don't know about? And when you fix an issue, how do you know whether or not your fix actually worked in the real-world? The answer is **monitoring**.

**Replit's founding engineer confirms:** eval dataset lags behind actual user behavior; A/B testing in production is critical for long-tail outcomes.

> "Engineers need to keep the eval dataset up to date with … actual user behavior, but by definition [that] dataset will constantly lag behind. Since the input space is no longer limited, you can't simply write a few selected tests and follow test-driven development: you'll risk breaking critical features without even being aware of their existence."

> "That's … why testing in production, with traditional A/B tests, is also critical: … to stay as close as possible to the general population you're serving, and have a higher chance to test a long-tail outcome."

Agents are getting more and more capable. The tools they use are getting more and more open-ended. They're able to run for longer and longer. If built correctly, they can perform tasks in ways you couldn't have predicted or imagined. We no longer live in a world where you can just test a single input.

**The agents are too much to test. But not too much to monitor.**

Traditional monitoring tools like Sentry track explicit errors (e.g. type errors, null pointers). But when AI agents fail, there's usually no error code in sight.

It starts with what we call **signals**. There are two types: **semantic signals** and **manual signals**.

Our customers create their own "semantic signals" (like, an agent getting stuck in a loop, forgetting the name of the user's friend, or responding in the wrong language). We train custom, tiny models to look at millions of events every day and pluck these problematic events out.

We combine these semantic signals with "manual" signals sent from your app: thumbs up/down, deployment rates, model switching, and regeneration, for example.

The result is a comprehensive view of how "good" or "bad" your app is, which can be broken down by use case, model, and more.

This approach is essentially the same as what Hamel calls "error analysis."

## Claim 3: Evals are good for rapid iteration

**Reality: The logic is self-contradictory; A/B testing on production signals is faster and more informative.**

Ankur claims that evals unlock rapid iteration. I found his logic hard to follow. I believe it to be false.

Ankur starts off by saying that A/B tests don't work because it's hard to create the variants to A/B: *"A/B testing assumes it's expensive to create variants."* *"Each variant requires significant design and engineering work. You really can't explore 20 options at once."*

But in the next paragraph, he describes exactly how you could use AI to automatically create variants: *"AI eliminates this constraint. When AI can automatically update your onboarding flow (or itself through prompt modifications) … You can now have 20 variants, or as many variants as you have users, or just one that updates automatically every 30 minutes based on real-user feedback."*

He implies that this isn't applicable to A/B testing. He doesn't explain why.

In fact, it feels like a rebuttal to Eval Driven Development: a world of infinite variants implies infinite new types of issues to discover. "Good" becomes increasingly less defined.

It becomes more important to see how things changed in the real-world, not just how changes perform against a set of rigid, adversarially selected criteria.

*"Instead of testing a handful of options and waiting weeks for results, teams can now test dozens of variations and see what works immediately."*

"Weeks for results" is another straw man. A/B tests are much faster in practice: minutes to deploy, hours to get answers.

**Imagine GPT-5 drops.** With Raindrop, you can route 1% of your users to GPT-5 and instantly see how it impacts frustration, or any other signal you define. With evals, you're stuck debugging/adapting old evals and trying to discover all of the new, unpredictable problems you haven't yet made evals for.

**The critical mistake Ankur is making here (and the one I am hesitant to point out to him) is that A/B tests on Braintrust ≠ A/B tests on Raindrop.**

*"…then A/B test how latency differences affect real users"*

That's what Braintrust means by A/B testing. But it's not what it means in Raindrop. Like we discussed earlier, semantic signals and intent tracking allows you to see exactly how behavior changes in a given experiment.

We answer the question: **"How does X change how my agent behaves?"** with ground truth-y signals from production. That's what customers care about.

## Claim 4: Evals for Personalized Software

**Reality: Personalization is the most obvious rebuttal against the obsession with evals.**

Ankur implies that evals are an unlock for the future of personalized software. I believe the opposite: personalization is the most obvious rebuttal against the obsession with evals.

Imagine a future where models can truly adapt to each user: changing tone, brevity, and truly tuning itself to each user.

How could you possibly eval *that*?

Imagine you have 1 million users. You'd need to somehow create evals for each of those users. You'd need to run those evals, for every single user, every single time you want to ship a change (which is, by the way, extremely expensive and slow).

Even if you could make all of these evals, it still wouldn't be enough. Each separate tuning for each user could introduce its own new bugs. Bugs you never even imagined.

I think the right approach is obvious. Instead of millions of evals, you need just enough to perform a smoke-test. (Think ~100 cases to make sure you're not causing known issues/taking down prod/etc)

And then? Well, you just ship. You can start with a small sample of users. You can then:
1. Look for negative signals: anomalies, the user struggling, assistant failing to do something, negative feedback, etc, across millions of events.
2. Cluster + find patterns in those negative signals (does it happen to a specific kind of user? specific scenarios? maybe specific languages/cohort/etc?)
3. Understand number of events/users impacted.

**Or you can write 10,000,000 evals. Your choice.**

## Closing

I don't have many bad things to say about Braintrust. Our customers that use Braintrust primarily use them 1. as a data warehouse and 2. for prompt management. I've heard they do these things pretty well. Most of our customers, however, haven't found their evals to be as useful as they thought. And they seem to be getting less useful.

### Side Note: What about online evals? LLMs as a judge?

Technically, Raindrop is just a type of online evals. The problem is that "online evals" have become synonymous with just running offline-evals on a small sample of production data (usually with "LLMs as a judge"). This isn't very useful in practice.

People love the idea of outsourcing the definition of "good" to an LLM. But the judge model often suffers from the same failure modes as what generated the outputs in the first place. The signals approach — custom tiny models trained on your actual data — is more grounded and more reliable.
