---
title: "ElevenLabs"
type: entity
created: 2026-05-08
updated: 2026-05-24
tags:
  - company
  - voice-ai
  - ai-agents
aliases: ["11labs", "Eleven Labs"]
sources:
  - https://elevenlabs.io
  - raw/articles/2026-05-19_elevenlabs_building-elevenagents-with-claude-code.md
  - raw/articles/2026-05-22_elevenlabs_elevenreader-launches-premium-audiobooks.md
  - raw/articles/2026-05-23_elevenlabs_22-million-earned-by-voice-creators-on-elevenlabs.md
---

# ElevenLabs

Leading AI voice and speech synthesis company developing natural-sounding text-to-speech, voice cloning, and conversational AI agents. Powers voice experiences for enterprises, creators, and government services worldwide.

| | |
|---|---|
| **Type** | Private (VC-backed) |
| **Founded** | 2022 |
| **Leadership** | Mati Staniszewski (Co-Founder & CEO), Piotr Dąbkowski (Co-Founder & CTO) |
| **Key Products** | ElevenAgents, ElevenCreative, ElevenAPI, Eleven v3 (TTS), Eleven Music, Scribe v2 Realtime, ElevenReader |
| **Website** | [elevenlabs.io](https://elevenlabs.io) |
| **Tech Blog** | [elevenlabs.io/blog](https://elevenlabs.io/blog) |

## Key Facts

### ElevenReader Premium Audiobooks (May 2026)

ElevenLabs launched **200,000 premium audiobooks** in ElevenReader, expanding the AI narration platform from user-generated to professionally produced content. This marks a shift in AI voice's role from tool to content distribution platform.

- Founded in 2022 by Polish childhood friends Mati Staniszewski (ex-Palantir) and Piotr Dąbkowski (ex-Google ML)
- Raised $500M Series D at $11B valuation (Feb 2026); $500M+ ARR
- 400+ employees; investors include BlackRock, NVIDIA, Andreessen Horowitz, and celebrity investors
- 1M+ users within 5 months of beta launch; headquartered in London
- Partners include Deutsche Telekom, Klarna, Revolut, Cisco, Harvey, and the Ukrainian government

### Voice Marketplace Economics (May 2026)

ElevenLabs' **Voice Marketplace** enables voice creators to upload Professional Voice Clones, set licensing terms (use cases, price tiers, notice periods up to 2 years), and earn ongoing royalties from every generation. As of May 2026:

- **$22M total paid to creators** — doubling from $11M in November 2025 (6 months)
- **10,400+ creators** earning on the platform across **32 languages**
- **Creator stories**:
  - **Brad Barlow** — Radio host with 20 voices live on marketplace; uses ElevenLabs for nearly all station audio production
  - **Jessica Anne Bogart** — Professional voice actor who earned more from the Voice Marketplace in her tenure than from the previous 5 years of her acting career combined
  - **Simon Patrick** — User #202 on ElevenLabs Discord; his voice "Christopher" earns a full-time living; his daughter Abby's voice "Amelia" allowed her to quit her day job and write full-time (7th published book)
- **Music Marketplace expansion**: Same architecture launched March 2026, exploring expansion across ElevenCreative
- **Consent & control**: Creators retain full control — can update terms, restrict use cases, or remove voice from marketplace (with notice period buffer)

This model creates a **new economic paradigm for voice IP**: replacing one-time licensing fees with ongoing usage-based royalties. The marketplace serves radio, audiobooks, game development, e-learning, marketing, and podcast production.

## Products & Technology
- **ElevenAgents**: Conversational AI agents with voice; deployed by Klarna, Revolut, Deutsche Telekom
- **ElevenCreative**: Voice cloning, dubbing, and audiobook creation
- **ElevenAPI**: Developer APIs for TTS, voice design, and speech-to-text
- **Eleven v3**: Latest TTS model; on-premise and on-device deployment available

## Claude Code Integration (May 2026)
ElevenLabs published a comprehensive tutorial (May 2026) for building production-ready voice agents using Claude Code via the ElevenLabs Skill. The tutorial demonstrates an end-to-end pipeline: setup → agent creation → knowledge base → workflow → tools → guardrails → testing → telephony deployment.

**Key integration features:**
- **Skill-based setup**: Fetch via `npx skills add elevenlabs/skills`, configure API key scoped to `agents-write` with daily spend cap
- **Knowledge base RAG**: Auto-indexed documents and URLs with auto-reindex on change; retrieval pipeline runs on ElevenLabs platform
- **Workflow routing**: Multi-intent conversation trees with LLM-based conditional routing between scoped nodes
- **Tool categories**: Client tools (UI actions), Webhook tools (server API calls), Built-in tools (end_call, language_detection)
- **Guardrails**: Independent of LLM — response validators catch edge cases missed by system prompts; supports focus mode, prompt injection protection, and custom rules (e.g., block pricing claims, billing write access)
- **Testing**: Response tests (tone/quality), Tool call tests (correct tool + parameters), Simulation tests (multi-turn flows)
- **Telephony**: Native integrations with Twilio, SIP trunk, Vonage, Telnyx, Plivo, Genesys — no third-party media server or manual TwiML routing
- **Performance**: Fastest model ~75ms latency with real-time turn-taking (pauses, interruptions)

This integration positions ElevenLabs as a platform that competes with Twilio for voice agent infrastructure (native integrations with Twilio, SIP trunk, Vonage, Telnyx, Plivo, Genesys), while leveraging [[entities/anthropic]]'s Claude Code as the primary development interface.

## Related
- [[entities/openai]] — Competitor via GPT-4o voice and TTS capabilities
- [[entities/anthropic]] — Competitor in enterprise AI agent space
- [[entities/nvidia]] — Investor and partner; provides GPU infrastructure
