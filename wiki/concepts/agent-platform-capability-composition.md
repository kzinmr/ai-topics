---
title: "Agent Platform Capability Composition — Parameterizing the Agent"
created: 2026-09-07
updated: 2026-09-07
type: concept
confidence: medium
tags:
  - ai-agents
  - agent-platform
  - agent-harness
  - harness-engineering
  - agent-architecture
  - agent-runtime
  - agent-governance
  - agent-identity
  - context-engineering
  - architecture
sources:
  - raw/articles/2026-09-07_hyperbo-lagent-platform.md
related: [harness-engineering, agent-iam, agent-identity-verification, kv-cache-compaction]
---

# Agent Platform Capability Composition

**"An agent is a parameterized program over a set of capabilities."** This formulation — from [[entities/ryan-lopopolo|Ryan Lopopolo]]'s ["Agent Platforms for Inventing Agents"](https://hyperbo.la/w/agent-platform/) (5 September 2026) — is the clearest available statement of a position the agent-platform industry had reached implicitly but rarely stated: the *capabilities* of an agent are now agreed, while their *implementations* are not, and the correct response is to expose every capability as a bindable parameter rather than freeze one implementation inside a harness.

## The Standard Capability Set

By late 2026 the capabilities that constitute an agent have stabilised into a recognizable list:

| Capability | What it is |
|---|---|
| Model and configuration | Which model, with which sampling/reasoning settings |
| Inference-and-tool-calling loop | The orchestrating loop that decides how the model thinks, acts, and perceives |
| Computer | Execution substrate |
| Disk | Durable state outside the context window |
| Context | Everything the model is conditioned on |
| Skills | A named, privileged special case of context (privileged because of post-training) |
| Tools | Actions the agent can take |
| Connectors | A named first-party subset of tools |
| Programming runtimes | Language/toolchain environment |
| Network policy | What the agent may reach |
| Agent identity | Who/what the agent *is* to downstream systems |
| IAM bundle | The credentials and entitlements attached to that identity |
| Guardrails | Constraints on permitted behaviour |
| I/O channels | Interfaces for steering and response |
| System prompt | The standing instruction |

The list's significance is that it is *plural and separable*. Identity, network policy, and IAM are not accessories to the loop — they are first-class capabilities with the same status as the model slug. This is the point at which agent architecture converges with distributed-systems and security engineering. See [[concepts/security-and-governance/agent-iam]] and [[concepts/security-and-governance/agent-identity-verification]].

## The Core Claim: We Do Not Know How to Build Agents Generally

> "We have figured out how to build individual agents. We have not figured out how to generalize what it means to mint an arbitrary agent."

Two distinct unknowns are conflated in most platform discussions, and separating them is the argument's engine:

1. **We don't know the general recipe.** No procedure exists that, given a task, produces a well-built agent.
2. **We don't know the best implementations.** For each capability there is "an infinity of ways to both curate and provide context," no consensus on which tools are good or correct, and system prompts "will want online variation and task- and customer-specific overrides."

From (1) and (2) follows the platform prescription: implementations that work today are *choices we need to be able to revisit for the next agent*. Therefore:

> "Every dependency hidden inside the harness is a parameter the builder cannot bind."

Freezing choices inside a harness "puts everyone building on it at the mercy of its authors." The builder's next experiment depends on whether the harness author anticipated it, exposed the right config knob, or is willing to put it on a roadmap. This is the lock-in mechanism, and it operates through *missing interfaces* rather than through contracts or pricing.

## Evidence: The 400,000-Line Tax

The empirical anchor is a single number. Building a general knowledge-worker agent on OpenAI's Agents SDK v1 **required 400,000 lines of code on top of the SDK**:

> "To let the agent execute its tasks through code, we had to provide (and invent in the first place!) skills for the agent, provision sandboxes and Python environments, install dependencies, manage worktrees, and stand up credential-injecting proxies. All undifferentiated work, but the platform had no reusable primitives for it."

Some of that work later landed in Agents SDK v2 through the container and bundled-skills APIs — which is the intended discovery mechanism working, but slowly and only for one vendor's customers. The 400K figure quantifies the thesis: if the platform had composable primitives, the work would have been *composition* instead of *invention*.

Across six production agents Lopopolo catalogues, the same capabilities reappear in mutually uninterruptible forms: ChatGPT with connectors (gpt-4o / Harmony / opaque file-search backends / plugin-registry credential injection); an agentic data scientist (host-user credentials inherited, credential-injecting proxy upstream); "FDE team in a box" (Agents SDK v1, 12 collaborating subagents, no credentials at all); an agentic TPM (Codex CLI main agent plus mini subagents, EBS-like block device, centralized plugin service injecting credential-bundle handles); an agentic engineering manager in Symphony (Elixir actor system delegating tickets to remote Codex CLI workers, manually provisioned credentials); an agentic SRE on Google Cloud (Vertex-selected models, Antigravity, microVMs or BYO compute, Agent Gateway).

Note what varies across that table: not the *capability set*, but every implementation choice — including whether credentials exist at all.

## Two Consequences Beyond Architecture

### 1. Missing interfaces cap what an organization can teach an agent

A hosted agent cannot be made expert in a customer's internal network topology "if it has no way to supply that context":

> "The organization may have the information and know how to prepare it, but the agent cannot use it. The missing interface prevents the people who understand the task from making the agent good enough to do it."

This is a stronger claim than "the product lacks a feature." The domain expert holds the exact knowledge that would make the agent competent, and no amount of that knowledge can be injected across an absent interface. Lopopolo's illustration: Japanese banks on ChatGPT Enterprise needed bespoke product work to get an admin toggle that *disables* web search — and the resulting control "did not generalize to Codex or their use of the API."

### 2. The harness author is silently setting the safety policy boundary

Customers enable autonomy against controls they trust, and they want attestations on the guardrails and bright lines under which the agent may act. Crucially: **"A model or harness upgrade should not silently change the conditions they approved."**

The concrete case is auto mode — an LLM judge approving or denying tool calls against a rubric. Antigravity exposes no auto mode; Codex and Claude Code have one but "do not let the builder inject an arbitrary rubric or judge into theirs."

> "The harness author therefore gets to define the policy boundary of autonomous execution."

That is a governance finding dressed as an API complaint. Whoever owns the harness owns the compliance posture of everyone building on it, whether or not that was a decision anybody made. The remedy Lopopolo proposes separates the two bindings: the platform lets the *builder* bind policy independently of the loop, and lets the *customer* serve its own rubric, judge, and approval mechanism through an API the customer controls — so "the customer remains in control of its safety and compliance posture" while the builder keeps improving capability.

This is the constructive alternative to the failure mode documented in [[concepts/ai-agent-safety-incidents]], where the containment policy was set by whoever configured the lab's internal sandbox and no external party could express or verify their own boundary.

## Compaction as a Bindable Capability

The same decomposition is applied to context compaction, which is normally treated as a fixed model/harness feature. In Lopopolo's construction the compaction tool is *backed by another agent composed from the same pieces* — its own model, prompt, context, and tools — and the working agent decides when to call it:

> "A tool backed by an agent is another parameterized program over capabilities. The same construction works recursively. We can discover useful behaviors by composing the pieces we already have."

Builders then control both *when* compaction happens and *how* it works, and can optimise those choices against long-horizon task performance — without waiting for a first-party, privileged implementation. It also means compaction need not remain bound to a model family. Given that instruction loss during compaction is now a documented incident class (the Summer Yue / OpenClaw inbox deletion, [[concepts/ai-agent-safety-incidents]]), making the compactor swappable and inspectable is a safety property as much as a performance one. See [[concepts/context-compaction]].

## The Reflexive Argument

The final move applies the thesis to the platform itself. If nobody knows how to build agents generally, then a platform that privileges its own implementations forces every builder to file a feature request in place of running an experiment:

> "the platform makes experimentation possible without requiring its authors to anticipate the results."

Structuring the platform around composable providers "distributes that work across teams and companies," so quality-focused teams can hill-climb rapidly and "what works becomes available for other builders to compose and improve." Lopopolo is explicit that this "is as much a way of operating as a systems architecture."

The closing sentence states what the whole mechanism is for: "Every interface the platform defines, every implementation it ships, and every provider a builder supplies is in service of minting a trajectory so the agent can do a thing."

## Open Questions

- **Composability vs. coherence.** If every capability is bindable, who is responsible when a composed agent misbehaves? Lopopolo's model splits capability (builder) from compliance (customer), but the incidents page suggests split responsibility is exactly where containment fails.
- **Does the parameterization thesis survive a capability jump?** The argument assumes implementations are provisional. If a future model needs a specific harness shape to elicit its capabilities, "bindable" may cost real performance.
- **Commercial alignment.** The platforms most used today (Codex, Claude Code, Antigravity) are precisely the ones withholding injection points. Is that an engineering-sequence choice or a durable moat strategy? Nothing in the essay settles it.
- **The 400K-line number is one practitioner's count** against one SDK version; treat as a vivid data point, not a measured industry constant. Hence `confidence: medium`.

## Related

- [[concepts/harness-engineering]] — the discipline this platform thesis generalizes
- [[concepts/recursive-self-improvement]] — composable harness primitives are the substrate for self-improvement loops
- [[concepts/ai-agent-safety-incidents]] — what happens when the policy boundary is owned by the wrong party
- [[concepts/security-and-governance/agent-iam]] / [[concepts/security-and-governance/agent-identity-verification]] — the identity/IAM capabilities as first-class rows
- [[entities/ryan-lopopolo]] — author; [[entities/openai]], [[entities/anthropic]], [[entities/google-deepmind]] — harness authors named in the critique

## Source

- Lopopolo, Ryan. ["Agent Platforms for Inventing Agents"](https://hyperbo.la/w/agent-platform/). hyperbo.la, 5 September 2026.
