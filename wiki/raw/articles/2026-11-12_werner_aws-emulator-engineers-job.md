---
title: "AWS Emulator and the engineer's job when agents write the code"
date: 2026-11-11
source: https://www.allthingsdistributed.com/2026/11/aws-emulator-and-the-engineers-job-when-agents-write-the-code.html
authors: [Werner Vogels, Swaminathan Sivasubramanian (Swami)]
type: article
hn: https://news.ycombinator.com/item?id=50456740
tags: [raw, agentic-coding]
sha256: 6d56e5bfcbeaa9cf2311f210cc92e7effa11c134675a96eb46997305e8184fbf
---

AWS Emulator and the engineer's job when agents write the code — All Things Distributed, November 11, 2026 (1671 words). Guest post by Swaminathan Sivasubramanian (Swami), introduced by Werner Vogels.

"Today we release AWS Emulator, which gives coding agents a local copy of AWS to test against."

## History: simulation and formal reasoning at AWS

- ~2004-2006: Werner asked Swami to work with Al Vermeulen on "Alf", a Paxos-based distributed lock service powering S3, DynamoDB and more.
- "the best ideas for testing distributed systems were large-scale system testing and chaos-based testing. Both worked, but they were expensive, and they could not reproduce many kinds of conditions on demand."
- They simulated Alf's environment with maximum fidelity: servers inside a JVM, simulated network and infrastructure, packet drops and fault injection on demand; plus formal reasoning via TLA+. "By testing this way we ironed out most of Alf's concurrency bugs before it ran on real servers."
- Simulation worked because a small team could build a copy of ONE system's environment by hand. "But today AWS has over 200 services, and an application that calls AWS needs a test environment for each one it uses. Building all of those by hand would take years of engineering, and agents now write code far faster than any team can check it in production."

## How AWS Emulator was built

- Idea from Matt Goldberg (Senior Principal Engineer, AWS Developer Tools): given a written description of how a service should behave and the real service to check against, an agent could build a working version of that service. The written description is the public API models in Smithy; the real service is AWS cloud itself.
- Fidelity tests: end-to-end customer scenarios devised from public API models (e.g., an SQS message stays hidden until its visibility timeout expires). Agents correct each test until it passes against real AWS, so the test records AWS behavior; agents then build the emulator until it passes the same test.
- "Matt began with SQS alone, and when he gave Kiro one prompt describing this approach, it returned a passable first version of an SQS emulator in about 15 minutes."
- "All of AWS Emulator's code was written and tested by agents, and it is built from more than 400 API models covering more than 200 AWS services. It runs free and offline on your own machine."
- Every change goes through a merge gate: a deep bench of automated checks, including several security agents doing adversarial reviews, plus deterministic checks that stop agents from touching code they are not supposed to.
- Repo: github.com/aws/aws-emulator, CC0 license, ~29,684 commits, Rust (one crate per AWS service; debug build needs 100 GB disk). Launched with official AWS docs at docs.aws.amazon.com/emulator. "things-that-do-not-work" folder tracks behaviors not yet matching real AWS; fidelity scores published with each release.

## The engineer's job when agents write the code

- "A coding agent works in a loop: it writes code, runs it, and reads the result before deciding what to change next. In distributed systems that loop runs inside infrastructure, so the services it calls have to behave like the real ones."
- "When agents write the code and check their own work, the engineer's job is to give them room to work on their own and to build the specs, tests, and merge gates that decide when that work is correct."
- Swami's anecdote: he used Kiro to rebuild Alf's replication engine (originally ~4 months of work). "I supervised the agent for four nights before I saw that it had no way to check its results. Once it had a spec and a test environment, the rebuild took about two hours."
- "Software quality in the AI era depends on the guardrails that engineers design around agents."
- "We expect agents to build and check most software, with engineers deciding what gets built and when the work is correct."

## HN discussion highlights (item 50456631, 875 pts, 239 comments; main repo thread)

- [singron] "I'm curious how many versions they made and the token spend on each one... Is this more of a sly marketing stunt or a real indication that this methodology is practical and economical?"
- [swiftcoder] "I guess they didn't decide this was worth it till they needed it to train an LLM, huh? Not like everyone (inside and outside AWS) has needed such a test harness for years."
- [forgotpwd16] "~30K commits in 3w; quality software for sure. Is someone trying to get promotion by tokenmaxxing? Ironic or unlucky coincidence... that only 2w ago, Amazon published memo discouraging AI abuse?"
- [CharlieDigital] skeptical whether it is a real shippable product vs an exercise; recommends Floci and Testcontainers. [switchbak] reports Floci itself was "the epitome of vibe coded — things breaking randomly between releases."
- [nnucera] (MiniStack maintainer): "We'll definitely keep maintaining MiniStack... many companies using it, including NVIDIA, NASA, Block... Until the AWS emulator can match all our current capabilities — multi-account, multi-region, IAM, running IaC — we'll still be around."
- [olalonde] "It's in their official docs, so probably not just someone's side project: https://docs.aws.amazon.com/emulator/"
- [tonymet] "A mere 20 years too late. Now it's faster to have AI mock your APIs for you."

## Related sources

- https://www.allthingsdistributed.com/2026/11/aws-emulator-and-the-engineers-job-when-agents-write-the-code.html
- https://github.com/aws/aws-emulator
- https://news.ycombinator.com/item?id=50456631 , https://news.ycombinator.com/item?id=50456740
