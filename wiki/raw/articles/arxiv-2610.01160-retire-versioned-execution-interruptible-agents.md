---
source_url: https://arxiv.org/abs/2610.01160
ingested: 2026-10-04
sha256: 74a649ebbe7fd4275ee69f14fc2efb090f2d4d908ad613fedf23c8d262ea206a
---

# Serving a Revisable World: Versioned Execution for Interruptible Agents

Authors: Yanxin Zhang, Rahul Sharma, Nitin Vegesna, Zheyu Fu, Chang Liu, Trivikram Krishnamurthy.
arXiv:2610.01160, submitted 2026-10-01.

## Abstract
LLM agents revise running tasks when users change instructions, tools fail, or new information changes a plan. Today's servers express a revision as aborting old requests and submitting replacements. Yet the old execution's buffered output and outstanding work must stop affecting the application, while completed KV state may still be useful to its replacement. Handling these obligations separately can leave obsolete effects publishable and force the successor to rebuild valid state. We present Retire, a serving control-plane redesign around versioned execution. Requests own scheduling and memory resources; execution versions own authority, the permission to publish output or install state for the current execution. Retire first revokes obsolete work, then bounds its remaining execution and certifies the completed prefix its successor can inherit. The successor runs from that state while isolated old resources are reclaimed asynchronously. This unifies fast invalidation and selective preservation in one version transition. We implement Retire in vLLM across output publication, GPU execution, KV handoff, tiered recovery, and distributed and multi-tenant serving. Correctness experiments verify current-version output and valid state inheritance across these paths. Combining invalidation with inheritance reduces revision-to-successor time-to-first-token by a median 17.1% in controlled paired experiments. A replay of recorded coding-agent interruption arrivals emits no obsolete output and keeps every final version progressing through repeated revisions. Retire turns abort-and-restart into a coordinated handoff that stops obsolete work quickly and preserves useful work for its successor.
