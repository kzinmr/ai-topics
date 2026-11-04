---
title: "Agentic Verification"
author: "Addy Osmani"
url: "https://addyo.substack.com/p/agentic-verification"
date: 2026-10-14
type: article
source: addyo-substack
---

# Agentic Verification

If you give an AI agent a way to independently verify its work, that can heavily improve the quality of output. Agents write code “much better on average at [scale](https://x.com/poteto/status/2109110547824378140)”. The “at scale” part comes from **verification**. Agents make checking cheap. 

The stuff that made “Good Code” expensive (tests, benchmarks, specs, real e2e runs) is now a cheap thing you can ask an agent for. You can improve the checks.

So our work is less “review every line” and more “build loops the agent can run itself”. Give the agent a way to verify the work. That loop is where quality comes from.

And make taste compound. When the agent gets something wrong, write it down (shared config, a hook, a test) so it doesn’t happen twice. A human still owns what ships but now they’re reviewing evidence and not just diffs.

**To make your agent produce high-quality output, equip it with a way to check its work. Tests are part of that.**  
  
Here are some of the ones I think are worth investing in.  
  
\- Write end-to-end tests that simulate real user flows and act as the ground truth  
\- Use property-based testing to specify what should never happen and generate thousands of test cases that attempt to break those constraints  
\- If replacing a system, compare the old and new versions using randomly selected inputs  
\- Require tests to run quickly and deterministically, which reinforces the agent to retry when the loop is slow or unreliable (the agent may learn to retry, not fix the problem)  
  
Example tests say what should happen; properties say what must not.

[](https://substackcdn.com/image/fetch/$s_!uAH-!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc410f959-0f40-422c-b4d9-f64fbd3a9ada_3200x3200.png)

## Verification is the bottleneck

Today’s models are good enough that the major bottleneck is not code-writing but the ability to verify that the code they’ve written is correct.

If your agent can’t verify its output, it’s essentially guessing, and a wrong guess ends up being verified by your test suite. That is, you’ll have a feedback loop in which you’ll go back and forth until you can read diffs, run your tests, check out the app, find bugs, and report them back. This is the slowest, costliest feedback loop, and it’s not scalable to more than one human.

But if your agent can test its own output, it’ll write a change, run the check, read the output, and try again over and over until it can pass the check. This is what happens before a single human even has to see anything. It’s hard to overstate the improvement in quality that you can get out of a self-verifying agent vs a feedback loop dominated by humans. I would always prefer a much better feedback loop to a slightly better model.

[](https://substackcdn.com/image/fetch/$s_!zlOU!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7a6d4992-3ab1-4ff1-b6a6-f5a31fbd3725_3200x3200.png)

This is a new definition of tests. For years, tests were the main tool humans used to identify bugs and refactor reliably. These are still good reasons to write tests, but tests are also how your agent senses the world and knows when it’s done.

Not every test is equally valuable for this purpose.

## There’s a whole spectrum of tests

### E2E tests

If you had to choose only one test to use, it would be E2E tests. They describe what a real user does.

An E2E test is what a human would do: sign up, add an item to the cart, checkout, and see a confirmation. It ignores the internal structure of your code and sees only what the user can see.

This is the kind of oracle you want for your agent. Machines will often write code that passes checks but misses the big picture. A mock-based unit test might pass, and the feature could be broken because the agent and your test share a misunderstanding. An E2E test, on the other hand, is very hard to trick. Either the whole thing works, or it doesn’t.

[](https://substackcdn.com/image/fetch/$s_!QbKk!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8c0a7e46-ac45-4147-b076-8b8058405b79_3200x3200.png)

What makes E2E tests especially valuable for agents beyond their use in CI/CD pipelines?

\- They cover only important, meaningful user flows, not all possible paths.

\- They tell you what’s wrong: Screenshots, tracing, and an explanation of which step failed tells the agent what went wrong, rather than making it flail in the dark. “Timeout after 30s” tells you nothing.

\- They work on the agent’s local configuration as well as its deployment environment.

\- They define “done”: “Implement this feature” is too vague. “Make this E2E test pass” is a target the agent can chase on its own.

It’s important to say that E2E tests have trade-offs that are real: they are slower and flakier than traditional unit tests. The choice is not to eliminate them, but to prefer a small set of high-value tests.

_Note: E2E tests are excellent, but as Lauren (@poteto) stresses giving the agent hands and eyes on the real running system is worthwhile: a maintained skill/CLI that knows how to launch, drive and observe the app (CDP, simulator, API harness, etc.), plus a**feature map**. A feature map is a user-POV inventory: what features exist, how a real user reaches them, keyboard shortcuts/selectors, expected outcomes and gotchas._

### Property-tests: constraints that can’t break

Many kinds of tests are about what a human thinks might go wrong. Property tests are about what a human doesn’t consider: the cases where agents go wrong.

Much of what humans write in tests is about examples: “If this is the input, then the output should be this.” These tests are good at ensuring that something should work, but they’re poor at ensuring that something should never fail: Humans can’t think of all possible inputs that would fail.

[](https://substackcdn.com/image/fetch/$s_!oqca!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F275a7703-566a-45e1-a775-e36fa8d19499_3200x3200.png)

Property-based tests reverse the premise: You create a rule that should hold, and a tool will generate hundreds or thousands of inputs to break it. Tools like fast-check for JS/TS, Hypothesis for Python, and proptest for Rust do this well. When a failure is found, the input is reduced to the minimal case that breaks the test: It won’t bomb with a random blob of data.

Here are some properties that are common in nearly every software project:

  * Round-trip encoding: the value I encode and then decode is the same as the one I started with. Parsing and serializing a value yields the value I started with.

  * Invariants: sorting doesn’t change the number of elements or the contents of the collection. A balance never becomes a negative number. Money in is money out.

  * Idempotency: migrating, normalizing, or retrying the same thing twice has the same effect as doing it once.

  * Equivalence: the optimized function yields the same result as the simple, correct one.

When you’re working with agents that’s crucial, because the agent is going to make up its own test examples that succeed based on its own internal logic. The property forces the agent to deal with any input generated, not just ones it chooses.

_Note: Property tests and differential checks cover a lot, but Boris Cherny of Claude Code has been using models (Lean, TLA+) on the hairiest state machines, concurrency and data-flow pieces. Short prompts can surface race conditions and subtle bugs by building a model, finding counterexamples, reproducing them, and fixing._

Properties are a great way to specify your requirements. If I say that the total for a cart must always be the same as the sum of its line items, that’s a great specification. The agent can use that specification to construct its own code, and a generator can look for discrepancies.

#### How to start without boiling the ocean:

  * Start with a small, essentially pure function, like a parser, a formatter, a pricing calculation.

  * Write the property in plain English before implementing it in code.

  * When your test library finds a problem, save the minimized test case so you can use it for regression testing.

  * Ask the agent for properties instead of test examples when making new code. It’s very good at it, once you tell it to.

  * When replacing an old system with a new one, generate a diff between them.

  * When doing a rewrite or migration, treat the old system as the oracle.

One of the classic failure modes of a rewrite is that it’s able to pass the new test suite, but it diverges from the old system in many small, undocumented ways. This is the difference between the official specification and actual behavior. Users end up relying on what actually works, not what the specification says should work.

### Differential tests: the old system is the oracle

Differential testing bridges that gap. Instead of relying on your new test suite, run the old and new systems side by side with the same inputs. If there’s a discrepancy in the outputs, you’ve either introduced a bug in the new system, or you’ve deliberately made a change you should document as a breaking change.

[](https://substackcdn.com/image/fetch/$s_!gAxS!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fae5ae9de-9850-48b5-983e-44ff02104f2b_3200x3200.png)

This is where choosing your input matters. If you’re using test cases manually chosen by you, you’ll miss rare edge cases. Randomly generate inputs, replay a sample of live traffic, or both. This is equivalent to property-based testing, with the property that your new system’s outputs match the old system’s outputs.

Differential testing is brilliant for agent-assisted large-scale migrations. You loop between tweaking the new system, running the differential test, reviewing the mismatches, fixing them, and restarting the loop. Because the old system is the oracle, you don’t have to explain every edge case to the agent. Teams that’ve done both versions and run the diff tell me that it was a shift from fixing one breakage and creating another to carefully and methodically progressing through the comparison.

#### A few practical notes:

  * Normalize everything that doesn’t matter and ordering that doesn’t carry any semantic weight. Stripping those differences out before comparing makes sure that you never get an infinite stream of false diffs.

  * Track intended changes in a list of approved changes: every change you want to make is noted with a reason why. This keeps “different” from becoming an acceptable state.

  * The secret to confidence is just getting every last bit moved: the diff harness gives you the confidence to wipe the old system away. Keeping both systems running is twice the work of understanding either one, and it introduces two different ways your migration can break. 

## Make the loop fast and deterministic

Tests must be fast and deterministic, or the agent will pick up the wrong lesson.

It’s not merely a time sink - it’s a training exercise. If the tests are slow or unstable, the agent will learn that sometimes just restarting the test is better than trying to fix the problem.

Humans are kinder to bad testing infrastructure. We know which tests are flakes, we know to rerun the CI in case of failure, we’re willing to wait 20 minutes for a build that might be flaky. The agent, however, learns from the incentives of the loop. If it’s possible to retry a failing test and have it work once in a while, it’ll pick retrying as its preferred strategy. If it takes 15 minutes to run the tests, it’ll run them less often, batch more changes between each run, and lose the ability to pinpoint exactly which change caused a failure.

Both failure modes cause the agent to get worse, but without any visible sign of failure, so you produce lower-quality output for humans to review.

#### What good looks like

Here are a few ideas of what I think “good” might look like - the agent should learn from the incentives of the loop.

[](https://substackcdn.com/image/fetch/$s_!St6s!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd7c0036b-40ac-4bdd-8f15-90a9e4e87205_3200x3200.png)

  * Test suite runs fast enough to run in each cycle. For the core loop, subsecond is great. Write a command that the agent can find and run easily, with any applicable quiet flags.

  * Test suite produces the same results every time. Use seeded randomness, frozen clocks, controlled networking, and isolated state. If it fails, the system is broken.

  * Flaky tests are isolated from the main suite, and removed immediately. A flaky test in the main suite is worse than no test at all, because it breaks trust in every other result.

  * Output is short and to the point. Specific messages about what failed are better than voluminous logs about what passed.

  * Unwanted output costs the agent attention and mental bandwidth on every turn.

  * Quick first loop for the agent, and run the heavy E2E and diff tests before integrating changes.

  * Treat the testing infrastructure as one of the components that the agent depends on. Improving it has compounding positive effects on all tasks.

_Note: A few extra practical habits include explicit goal restatement (“restate what you think the success criteria are”) before coding, fresh-context or separate reviewer agents for verification and treating generated tests themselves as artifacts that need some scrutiny (does this test actually distinguish correct from plausible-incorrect implementations?)._

## Write the check before the code

Before telling your agent to make something, you have to know what it’s supposed to succeed at. That could be an end-to-end workflow, a specific property, or a comparison to a prior system. Whatever it is, make sure that it’s fast and deterministic, and you can let the agent iterate over a solution.

Your job doesn’t need to be reading each line of output, but you need to define what success looks like. You’re getting better value out of your judgment and it will scale better than you will ever read a diff.

When you’re testing your agent, you need to have examples of what should happen and properties of what should not. To win, your agent’s testing process needs to be fast and accurate.

[](https://substackcdn.com/image/fetch/$s_!9coI!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F52129609-d334-4303-924e-2a7089486f91_2754x1536.jpeg)