---
title: "Voice Agent Evaluation"
type: concept
created: 2026-06-24
updated: 2026-06-24
tags:
  - concept
  - voice-ai
  - ai-agents
  - evaluation
  - benchmark
sources:
  - raw/articles/2026-06-20_elevenlabs_voice-agent-evaluation-framework-6-pillars-explained.md
  - raw/articles/2026-06-24_elevenlabs_voice-agent-latency-optimization.md
  - raw/articles/2026-06-23_elevenlabs_what-is-an-ai-voice-agent.md
---

# Voice Agent Evaluation

Voice agent evaluation is the systematic measurement of AI voice agent performance across multiple dimensions. Unlike text-based LLM evaluation, voice agents introduce real-time constraints (latency, turn-taking, interruption handling) and audio-specific quality metrics that require specialized frameworks.

## Six-Pillar Framework (ElevenLabs)

ElevenLabs published a comprehensive evaluation framework defining six pillars for measuring voice agent performance:

| Pillar | Description | Key Metrics |
|--------|-------------|-------------|
| **TTS Voice Quality** | Naturalness, clarity, emotional expressiveness of synthesized speech | MOS ≥4.3, jitter <30ms |
| **Conversation Quality** | Speech recognition accuracy, contextual understanding across turns | STT WER, time-to-first-audio <500ms |
| **Tool Usage & Task Completion** | Autonomous task completion using available resources | TSR >85% |
| **Intelligence** | Reasoning, handling novel inputs, avoiding hallucination | FCR, CSAT |
| **Compliance & Safety** | Regulatory adherence, guardrails | Compliance audit results |
| **Reliability** | Uptime, consistent performance under load | P99 latency, uptime % |

### Production Targets

- **MOS**: 4.3–4.5 (Mean Opinion Score for voice naturalness)
- **TSR**: >85% (Task Success Rate)
- **Time-to-first-audio**: <500ms
- **WER**: 2.2% (ElevenLabs Scribe v2, lowest per Artificial Analysis June 2026)
- **Model inference latency**: ~75ms (ElevenLabs Flash v2.5 / Turbo v2.5)

### Industry-Specific Weighting

Different industries weight pillars differently:

- **Healthcare**: Compliance and safety prioritized (HIPAA, data handling)
- **Customer service**: Conversation quality and tool usage prioritized
- **Education**: Intelligence and TTS voice quality prioritized (engagement)
- **Real estate / sales**: Conversation quality and multilingual support prioritized

### Common Evaluation Mistakes

1. **Only evaluating clean audio** — ignoring noise, accents, and edge cases
2. **Ignoring P99 latency spikes** — average latency hides tail behavior
3. **Testing without realistic multi-turn flows** — single-turn tests miss context drift
4. **Not testing interruption handling** — real users interrupt, overlap, and backtrack

## Related Benchmarks

- [[concepts/ai-benchmarks/tau-voice]] — Full-duplex voice agent benchmark (τ-Voice) measuring real-time conversational ability
- Voice agent latency is a composite of: STT latency + LLM inference + TTS synthesis + network round-trip

## Voice Agent Architecture

A typical voice agent pipeline:

1. **Input** — Voice via STT (e.g., ElevenLabs Scribe), transcribing in real-time
2. **Context assembly** — LLM assembles conversation context: prior messages, knowledge base retrieval, tool data, system prompt
3. **Response generation** — LLM generates text response
4. **Output** — Text converted to voice via TTS (e.g., ElevenLabs v3)
5. **Turn-taking** — Model detects when user has finished speaking, handles pauses and interruptions

Key supporting technologies: VAD (Voice Activity Detection), voicemail detection, barge-in handling, multi-language detection.

## Related

- [[entities/elevenlabs]] — Leading voice AI platform; published the six-pillar framework
- [[entities/cartesia]] — Voice AI competitor with Line for voice agents
- [[entities/decagon]] — Customer support voice agents with Voice 2.0
- [[concepts/modal-sandboxes]] — Infrastructure partner for real-time voice agent deployment
