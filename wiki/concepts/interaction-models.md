---
title: "Interaction Models"
created: 2026-05-11
updated: 2026-05-11
type: concept
tags: [multimodal, real-time, human-in-the-loop, streaming, voice-ai, ai-native, tool-use, research]
sources:
  - raw/articles/2026-05-11_thinkingmachines_interaction-models.md
aliases: ["interaction model", "native interaction models"]
related:
  - concepts/ai-agents
  - concepts/human-in-the-loop
  - concepts/agent-architecture
  - concepts/streaming
---

# Interaction Models

Interaction models are AI models trained to handle real-time, multimodal interaction **natively** — without external scaffolding or harnesses. Announced by **Thinking Machines Lab** (May 2026), they represent a paradigm shift from turn-based AI interfaces toward continuous, bidirectional collaboration where the model perceives and responds simultaneously across audio, video, and text.

## The Problem: Turn-Based Interfaces as Bottleneck

Current frontier models experience reality in a single thread. They wait until the user finishes input before processing, and freeze their perception while generating output. This creates a narrow channel for human-AI collaboration that:

- Limits how much human knowledge, intent, and judgment can reach the model
- Limits how much of the model's reasoning can be understood
- Pushes humans out of the loop not because the work doesn't need them, but because the interface has no room for them

As one frontier model card noted: "When used in an interactive, synchronous, 'hands-on-keyboard' pattern, the benefits of the model were less clear. Autonomous, long-running agent harnesses better elicited the model's coding capabilities."

## Design Principles

Interaction models are built on three communication properties:

| Principle | Description |
|-----------|-------------|
| **Copresence** | People can interact with what others (including AI) are interacting with |
| **Contemporality** | People receive information as it's produced, with instant feedback |
| **Simultaneity** | People receive and produce information at the same time |

These properties mirror how humans naturally collaborate — messaging, talking, listening, seeing, showing, and interjecting as needed.

## Architecture

### Time-Aligned Micro-Turns (200ms chunks)

Instead of consuming a complete user-turn and generating a complete response, the interaction model works with **200ms micro-turns** — continuously interleaving input processing and output generation as concurrent streams:

```
Turn-based:        [input1] → [output1] → [input2] → [output2]
Micro-turn based:  [in0|out0|in1|out1|in2|out2|...] — 200ms chunks
```

This enables real-time concurrency of multiple input/output modalities. Silence, overlap, and interruption remain part of the model's context.

### Two-Model Split Architecture

The system is architected around two coordinated models:

| Component | Role | Latency |
|-----------|------|---------|
| **Interaction model** | Real-time presence — continuous audio/video/text exchange with the user | ~200ms |
| **Background model** | Sustained reasoning, tool use, browsing, longer-horizon work | Async |

Both share context. The interaction model delegates to the background model when a task requires deeper reasoning, then integrates results into the conversation as they arrive. This gives users both responsiveness and the full intelligence of reasoning models — planning and tool-use at the latency of non-thinking models.

## Capabilities

By making interactivity part of the model itself (not bolted on via harness), interaction models unlock:

1. **Seamless dialog management** — The model tracks implicitly whether the speaker is thinking, yielding, self-correcting, or inviting a response. No separate dialog management component.

2. **Verbal and visual interjections** — The model jumps in as needed depending on context, not only when the user finishes speaking.

3. **Simultaneous speech** — User and model can speak concurrently (e.g., live translation).

4. **Time-awareness** — The model has a direct sense of elapsed time.

5. **Simultaneous tool calls, search, and generative UI** — While speaking and listening to the user, the model can concurrently search, browse the web, or generate UI.

## Training Approach

The interaction model is **trained from scratch** with a multi-stream, micro-turn design. This builds on prior work in audio full-duplex models (Moshi, PersonaPlex, Nemotron VoiceChat, Seeduplex) but extends it to general-purpose interaction across all modalities.

## Why "The Bitter Lesson" Applies

The Thinking Machines team argues that bolting interactivity onto existing models via harnesses (voice-activity-detection for turn boundaries, stitching components for concurrency) follows the same doomed pattern as other hand-crafted approaches. Following Sutton's "Bitter Lesson," they predict these harness-based approaches will be outpaced by general capabilities that emerge from making interaction part of the model itself.

> "For interactivity to scale with intelligence, it must be part of the model itself. With this approach, scaling a model makes it smarter *and* a better collaborator."

## Significance

Interaction models represent a potential shift in the AI interface paradigm:

- **From prompting to collaborating** — Moving from "send prompt, wait for response" to continuous, multi-modal presence
- **From autonomous to collaborative agents** — Keeping humans productively in the loop by making the interface accommodate natural collaboration patterns
- **From text-first to multi-modal native** — Designing around continuous audio/video as the hardest case, then extending to text

If successful, this could address one of the most significant gaps in current AI systems: the inability of frontier models to support the kind of fluid, iterative collaboration that characterizes effective human teamwork.

## References

- [Thinking Machines Lab: Interaction Models blog post](https://thinkingmachines.ai/blog/interaction-models/) (May 11, 2026)
- Clark H. and Brennan S., "Grounding in Communication" (1991)
- Sutton R., "The Bitter Lesson" (2019)
- METR: Measuring AI Ability to Complete Long Tasks (2025)
- Moshi (Kyutai), PersonaPlex, Nemotron VoiceChat — prior work on audio full-duplex models

## See Also

- [[concepts/ai-agents]] — Autonomous AI agents
- [[concepts/human-in-the-loop]] — Human-in-the-loop interaction patterns
- [[concepts/streaming]] — Streaming LLM output
- [[concepts/voice-ai]] — Voice-based AI interaction
- [[concepts/agent-architecture]] — Agent system architecture
