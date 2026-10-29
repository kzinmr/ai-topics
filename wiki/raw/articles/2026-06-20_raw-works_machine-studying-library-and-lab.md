---
title: "Machine Studying — The Library and The Lab"
source_url: https://raw.works/machine-studying-the-library-and-the-lab/
author: Raymond Weitekamp (@raw_works)
published: 2026-06-20
ingested: 2026-10-28
source_type: blog
tags: [raw, blog, machine-studying, studybench, omar-khattab, codex, evals, agent-study]
---

# Machine Studying — The Library and The Lab

**Author:** Raymond Weitekamp ([@raw_works](https://x.com/raw_works)) — RAW Works (raw.works)
**Published:** June 20, 2026
**URL:** https://raw.works/machine-studying-the-library-and-the-lab/

As usual, I can't help but dive right into anything that comes out of Omar Khattab's lab. "Machine Studying" is a very interesting blog post that attempts to define "expertise" and "intelligence" based on an agent's ability to quickly learn new material from a corpus.

> "In a way, Machine Learning asks how a system can improve from data when we have a precise objective to optimize. Machine Studying asks what an agent should do when it's given a declarative corpus and no downstream task."

I was curious to see what would happen with a modern harness (Codex CLI) and a top model (GPT 5.5 xhigh reasoning).

I was able to get a very high score right off the bat (76%, roughly 3x the highest reported in the original blog), which would suggest that either this combination of model and harness has high expertise on these tasks (already knows them well), or generally has fairly high intelligence for this category of task (ability to gain expertise).

Both of the examples in the current version of StudyBench involve testing an agent on its ability to use a specific version of a programming tool (DSPy & OpenClaw). The dates of the version in the test are from March and April of 2026, so I thought that it might be possible that these versions might already be in the training data of GPT 5.5, although the official page from OpenAI says the knowledge cutoff is Dec 1, 2025.

This led me to the idea that there are at least two different environments to study in: **"the library"** and **"the lab"**. In the library - you have books (i.e. documentation) and in the lab you have instruments (i.e. packages). My initial environments for DSPy and OpenClaw gave Codex access to both the documentation and the package. So I asked my buddy Codex (GPT 5.5 xhigh) to build out the remaining 3 environments. ("Lab only" turned out to be way trickier than anticipated as you have to block the package's self-documentation.)

So now for each OpenClaw and DSPy StudyBench question we end up with these four environments:

- **Closed book**: the agent only sees the question. It gets no docs, no source tree, no package metadata, and no runtime to experiment with.
- **Lab only**: the agent gets no docs, no source tree, and no static study corpus. It can only learn by running small probes against the pinned tool/runtime through the allowed lab surface.
- **Library only**: the agent can read and search the official static material: pinned source tree, docs, package metadata, and exposed corpus files. It cannot run the package, import it, execute tests, or use a binary/runtime.
- **Library + lab**: the agent gets both surfaces. It can read the official static material and also run experiments against the pinned environment.

(Results table in the post compares Closed book / Lab only / Library only / Library+lab across DSPy and OpenClaw StudyBench questions with per-treatment means.)

## Key takeaways

- "Machine Studying" (Khattab lab): what an agent should do when given a declarative corpus and *no downstream task* — expertise acquisition as an intelligence measure.
- Weitekamp's operationalization: the **library/docs vs lab/runtime** study-environment decomposition as a 2×2 design for measuring how agents gain expertise.
- Modern harness+model (Codex CLI + GPT 5.5 xhigh) scored ~3x the originally reported best, raising training-data-contamination questions for post-cutoff tool versions.
