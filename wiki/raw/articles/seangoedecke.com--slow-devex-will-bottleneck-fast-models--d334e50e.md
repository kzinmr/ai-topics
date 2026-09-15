---
title: "Slow developer experience will bottleneck fast models"
url: "https://seangoedecke.com/slow-devex-will-bottleneck-fast-models/"
fetched_at: 2026-09-14T10:02:13.145744+00:00
source: "seangoedecke.com"
tags: [blog, raw]
---

# Slow developer experience will bottleneck fast models

Source: https://seangoedecke.com/slow-devex-will-bottleneck-fast-models/

Right now developer experience is measured in seconds. If your tests take a second to run, that’s good; if they take thirty seconds, that’s bad. Any faster than a second doesn’t really matter, because most of your time is spent either thinking or waiting for an AI agent to spin. Shaving milliseconds off your dev server reload time or whatever is pointless: that’s not the bottleneck.
It will be. Small models are getting faster and faster, and smart models are getting smaller. I think most engineers will still want to use the smartest available model — software engineering is hard — but we will increasingly see faster models get used as subagents or for well-understood tasks. This is largely uncharted territory. Very few people have developed intuitions for what it is going to be like to work with agents that run at thousands of tokens-per-second.
GPT-6-Astra can run at about
sixty
tokens per second. That means you spend a lot of time waiting for it to think. You work with it like you would work with another human: delegating a task and then context-switching until that task is complete. If you haven’t yet, have a play around with
Jimmy
, Taalas’ version of LLaMA-3.1-8B running
at
seventeen thousand tokens per second
. No matter how long the response is, it arrives in the instant of you hitting send. The model is not good enough for agentic work, but it gives a glimpse of what it would be like: you would simply get your answer instantly
.
Well, that’s assuming the agent’s tool calls are fast. When generating tokens is not the bottleneck, it will suddenly matter a lot whether it can read a file in 100ms vs 10ms, or whether it can run your tests in 500ms vs two seconds. Fast tool calls are going to be the difference between a near-instant response and having to wait several minutes. There is thus going to be enormous pressure to do agentic coding in languages with fast compilers and tests, like Golang, and to tightly optimize the dev loop in agentic codebases.
Teams focused on DevEx — developer experience — are largely a relic of the 2010s, when companies were
incentivized
to make their engineers happy. Most companies have cut them down to a skeleton crew or removed them entirely. But we may see a return of DevEx in the late 2020s, focused on speeding up the experience for AI agents.
Here's a preview of a related post that shares tags with this one.
