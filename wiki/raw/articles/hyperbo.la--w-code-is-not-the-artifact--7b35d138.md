---
title: "Stop Treating Code as the Artifact"
url: "https://hyperbo.la/w/code-is-not-the-artifact/"
fetched_at: 2026-04-29T07:02:15.034492+00:00
source: "hyperbola :: blog"
tags: [blog, raw]
---

# Stop Treating Code as the Artifact

Source: https://hyperbo.la/w/code-is-not-the-artifact/

Once agents write most of the code, stop treating the source files as the
artifact. The durable thing is everything upstream of them: the repo-owned spec,
the guardrails, the typed boundaries, and the operator surface that determines
what code is allowed to exist.
Symphony
is an issue-tracker-based agent orchestration system. It
ships a spec, not source code. Symphony is a
ghost library
: the
implementation is downstream of the spec.
That would have looked backwards when human implementation effort dominated the
cost structure. A library that mostly ships a spec would have felt unfinished.
In an agentic system, the spec
is
the valuable part. It is the same reason
agent-authored PRs should carry the prompt: the description of the work matters
more than the particular source files that fell out of it. If the boundaries and
contracts are sharp enough, generating the implementation is the easy step.
Once the spec is the artifact, the review question changes:
What description of the work produced this diff?
What code is the agent allowed to write?
What operator surface proves the work happened?
Those are the things I want to maintain. The code is downstream.
