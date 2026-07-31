---
title: "The Session You Cannot Take With You"
type: article
source_url: "https://earendil.com/posts/session-portability/"
author: "Earendil Engineering"
date: 2026-07-30
date_ingested: 2026-07-31
tags:
  - session-portability
  - inference-api
  - vendor-lock-in
  - ai-agents
  - context-engineering
  - distillation
related:
  - concepts/session-portability
  - concepts/earendil
  - concepts/context-engineering/context-lock-in
---

# The Session You Cannot Take With You

**Source:** https://earendil.com/posts/session-portability/
**Author:** Earendil Engineering (rfc@earendil.com)
**Date:** 2026-07-30

---

The original promise of an inference API was wonderfully simple: send some input, receive some output. If you kept both, you had the conversation. You could inspect it, archive it, replay it, or give it to a different model.

That abstraction was never completely true. Prompt caches live on somebody else's GPUs, tokenization differs between models, and sampling is not reproducible (and quite intentionally so). But the *semantic record* of a session in the form of a transcript could still belong to the user. A transcript should contain the instructions, messages, tool calls and tool results. Another sufficiently capable model might not continue identically, but it could understand what happened and take over.

Inference APIs are frustratingly moving away from that property, at least somewhat. They increasingly return a mixture of text and provider-bound state that is very intentionally non-portable.

- reasoning tokens that are billed to the user but returned only as opaque, encrypted blobs, with useless summaries at best
- web searches where the model sees source material the client never sees
- compacted context that only the original provider can decrypt
- subagent instructions and messages hidden from the application running the agents in the form of encrypted payloads
- file, vector-store, container, and cache references that cannot be resolved anywhere else
- response and conversation state that is entirely keyed by IDs that are stored fully on the provider's servers

Each feature comes with a basic justification that's trivial for a provider to come up with, along with good arguments for why this is good for the user. Together all of these things change the ownership reality of an AI session: the transcript on your machine is no longer your session but a partial view of a session whose operational state belongs to an inference provider and not you.

## A Practical Test for Session Ownership

By a portable session we do not mean that switching from one model to another must produce the same next token. Portability means something more modest:

```javascript
const transcript = session.export();
revokeCredentials(oldProvider);
session = newProvider.continueFrom(transcript);
```

The archive should contain enough intelligible information for another model to continue the work. It should not require the old provider to dereference an ID, decrypt a blob, remember a search result, or reconstruct a summary.

Five useful tests:

1. **Inspection:** Can the user see what the model saw, what tools did, and what agents told each other?
2. **Export:** Is the session self-contained, apart from ordinary artifacts that can also be downloaded?
3. **Replay:** Can another implementation reconstruct a semantically equivalent context?
4. **Audit:** Can a human explain why the system took an action after the fact?
5. **Deletion:** Can the user identify and remove every server-side copy on which the session depends?

A response ID is not a transcript, a ciphertext the user cannot decrypt is not user-controlled state, a list of citations is not the evidence that was placed in the model's context by a search result.

## Encryption for Whom?

`encrypted_content` sounds like a privacy feature under the user's control. Usually it is a capsule that the client cannot read and only the provider can open. The provider chooses the keys, decrypts the content for its own models, and defines where the data can be replayed.

A better term is **provider-sealed state**.

Provider sealing can have a real privacy benefit. OpenAI, for example, can return encrypted reasoning to a client using `store: false`, then decrypt it in memory on the next request without persisting the intermediate state. But this encryption does not hide the data from the inference provider; it hides it from you.

## Stored Conversations Turn a Transcript into a Pointer

OpenAI's Responses API stores responses by default (retained for at least 30 days). The new Gemini Interactions API defaults to `store: true` (paid tier: 55 days, free tier: 1 day).

```javascript
const first = responses.create({
  model: "frontier-model",
  input: "Investigate this production failure",
  store: true,
});

const second = responses.create({
  model: "frontier-model",
  previousResponseId: first.id,
  input: "Now implement the fix",
  store: true,
});
```

If the local application only records the user messages and final text, `first.id` is now a foreign key into a database it does not control.

## No Reasoning For You

All major labs claim to have legitimate reasons not to expose raw chain of thought. On non-open-weights models we typically do not see these tokens.

- **OpenAI**: With stored responses, prior reasoning can be recovered through `previous_response_id`. With `store: false`, the API returns `encrypted_content`. Persisted reasoning remains opaque even when `reasoning.context: "all_turns"`.
- **Anthropic**: Returns encrypted full thinking in a `signature` field. The readable thinking text, when enabled, is a summary produced by another model, not the raw chain of thought. Thinking blocks must be passed back unchanged during tool-use turns and are tied to the model that produced them.

## Hidden Searches

With hosted search, the provider performs a private tool loop. OpenAI, Google and Anthropic expose search actions, citations, and optionally a list of source URLs, but not the complete text context used to produce an answer. A URL is not a stable replay: its contents can change, disappear, become personalized, or have been reduced to a provider-specific snippet before the model saw it.

Hosted search should have a full-fidelity export mode containing queries, result metadata, retrieved passages, timestamps, content hashes, and filtering steps.

## Opaque Compaction

OpenAI's server-side compaction emits an encrypted compaction item described as "opaque and not intended to be human-interpretable." The standalone `/responses/compact` endpoint returns a "canonical next context window" that clients are instructed to pass on as-is.

Anthropic's server-side compaction returns a `compaction` block with a readable `content` field, letting the client provide custom summarization instructions. Client-side compaction is also possible with any provider.

## Subagents Come With Hidden Instructions

OpenAI's hosted Responses Multi-agent beta returns three new item types: `multi_agent_call`, `multi_agent_call_output`, and `agent_message`. The example for `spawn_agent` contains an encrypted `message` argument, and inter-agent messages contain only `encrypted_content`. Automatic server-side compaction is implicitly enabled for every agent when Multi-agent is enabled.

A related change landed in the open-source Codex client in June 2026: commit ["Encrypt multi-agent v2 message payloads"](https://github.com/openai/codex/commit/5f4d06ef186b896d316620556e561d59206c3ebf).

An [open Codex issue](https://github.com/openai/codex/issues/28058) asks for the encrypted delivery to retain a separate readable audit copy.

## "Most People Do Not Switch Models Mid-Session"

Probably not. But even if you do not utilize that freedom, it matters because it changes the relationship you have with the provider. As a user you also may need to move a session because a model is retired, a service is down, a price changes, a policy blocks the next request, a confidential phase must run locally, or an auditor needs to reconstruct what happened.

The option to leave also creates discipline. If a provider knows that a user can continue elsewhere, it has to compete on model quality, price, reliability, and trust.

## What a Portable Inference API Should Promise

1. **The local event log is canonical.** Server storage may mirror or accelerate it, but the client can reconstruct the session without dereferencing server IDs.
2. **Storage is explicit.** `store: false` should be easy, documented, and preferably the default.
3. **No opaque item is the sole carrier of meaning.** Encrypted reasoning, compaction, and tool signatures may be included for same-provider quality, but each has a readable, provider-neutral handoff representation.
4. **Hosted tools have full-fidelity logs.** Record exact inputs, outputs, evidence, filtering, provenance, timestamps, and content hashes—not only a polished answer and citations.
5. **Subagent communication is auditable.** Persist the exact readable task, messages, results, lineage, model, and tool permissions for every agent.
6. **Compaction is inspectable.** Return a readable summary, the instructions used to create it, and enough lineage to understand what was discarded.
7. **Artifacts are exportable.** Files, container outputs, search snapshots, and generated media can be downloaded into a content-addressed local archive.

## Distillation Is Great Actually

Some of the largest closed-weight US labs are increasingly hostile to outside distillation. Anthropic's February 2026 post about alleged campaigns by DeepSeek, Moonshot, and MiniMax calls them "distillation attacks." Its commercial terms prohibit using the service to train a competing AI model. At the same time, Anthropic's own post acknowledges that "distillation is a widely used and legitimate training method" when frontier labs use it on their own models.

OpenAI similarly has offered an explicit [first-party API distillation workflow](https://openai.com/index/api-model-distillation/) for using outputs from a stronger OpenAI model to fine-tune a smaller OpenAI model.

The moral asymmetry: the labs ask society to accept that machines may learn from the enormous body of work humans placed on the internet, while insisting that other machines must not learn from outputs the labs generate. The broadest version of that principle conveniently allows learning to flow into closed models but not back out of them.

Distillation can turn expensive frontier capability into smaller, cheaper, faster models that can run locally, offline, on constrained hardware, or under the user's control.

## The Minimum Freedom

A user should be able to close an account, keep a session, and hand it to another model. The new model may disagree, ask questions, or perform worse. It should not be staring at ciphertext where the old model saw the user's history, evidence, plans, and delegated work.

Stateful storage should be optional, hosted tools should be observable, compaction should be readable, agent communication should be auditable and ideally opaque reasoning is not opaque or at least should have a portable handoff. Distillation should be a path by which capability becomes more available, not a taboo used to justify ever higher walls.
