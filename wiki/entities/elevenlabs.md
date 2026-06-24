---
title: "ElevenLabs"
type: entity
created: 2026-05-08
updated: 2026-06-24
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
  - raw/articles/2026-06-02_elevenlabs_webinar-recap-deploying-agents-across-every-channel.md
  - raw/articles/2026-06-05_elevenlabs_introducing-flows-agent.md
  - raw/articles/2026-06-17_elevenlabs_processing-images-and-documents-in-elevenagents.md
  - raw/articles/2026-06-20_elevenlabs_voice-agent-evaluation-framework-6-pillars-explained.md
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


### Music v2 (May 2026)

ElevenLabs released **Music v2**, a significant upgrade to its music generation model with:
- **Better vocals, instrumentation, and arrangement** across all genres
- **Improved multilingual support** — lyrics, vocals, and arrangements more reliable in target languages
- **Song-length composition**: Build full songs section-by-section (intro, verse, chorus) with structural continuity
- **Improved inpainting**: Select any section of a track and regenerate just that part
- **Cross-genre coherence**: Single song can move from opera to heavy metal and back
- **Non-musical sound effects**: Embed SFX directly within the track

Music v2 powers three platforms:
- **ElevenMusic** — listen, remix, and create tracks
- **ElevenAPI** — embed music generation in products
- **ElevenCreative** — downloadable music for ads, branded content, and video

**Pricing**: Music v1 and v2 prices cut by up to 50% for ElevenAPI and up to 40% for ElevenCreative.

Source: raw/articles/2026-05-27_elevenlabs_introducing-music-v2.md

## AI Customer Service Agents (June 2026)

ElevenLabs published a comprehensive guide to building AI customer service agents with ElevenAgents, covering the full voice pipeline and deployment best practices.

### Architecture Pipeline

ElevenAgents processes voice and text through a **real-time pipeline**:

1. **Input** — Voice via ElevenLabs' **Scribe** (Speech-to-Text model), transcribing in real-time before the customer finishes speaking. Text inputs go directly to the pipeline.
2. **Context assembly** — The LLM assembles full conversation context: prior messages, knowledge base retrieval, live data from connected tools, and the system prompt.
3. **Response delivery** — Text responses go directly; voice responses are converted back via ElevenLabs' Text-to-Speech system.

### Supporting Technologies

- **Turn-taking model**: Detects when a user has finished speaking for natural back-and-forth conversation
- **VAD (Voice Activity Detection)**: Separates primary speaker audio from background noise
- **Voicemail detection**: Identifies when calls reach voicemail rather than a live person
- **Guardrails**: Response validators, focus mode, prompt injection protection, custom rules

### Best Practices

**Knowledge base grounding**: Compile SOPs, FAQs, product documentation, and policy documents. Use consistent terminology and keep content up to date. ElevenAgents supports RAG for larger knowledge bases, pulling only relevant content to prevent context overflow.

**System prompt structure**: Well-structured prompts include four sections — Personality, Goal (ordered steps), Tools (when and how to use them), and Guardrails (what never to do). For enterprise deployments, keep each agent specialized rather than multi-purpose.

**Case study — mdhub**: Behavioral health platform deployed ElevenAgents across clinic admissions and patient support. AI agents now handle **90% of inbound calls end-to-end** (capturing demographics, verifying insurance, booking appointments). Time from first inquiry to appointment dropped from **weeks to days**, and bookings increased **30%**.

**Omnichannel routing pattern** (June 2026): ElevenLabs demonstrated a three-tier omnichannel architecture. A single **greeting/FAQ router** handles initial customer contact across SMS, voice, and in-app channels, then routes to specialized sub-agents — **Transaction Agent** (payment/commerce), **Rebooking Agent** (schedule changes), and **Baggage Claim Agent** (issue resolution) — via LLM-based intent classification. The architecture keeps knowledge base and policies centralized at the logic layer while deploying channel-specific front-ends, eliminating per-channel rebuild costs.

Source: raw/articles/2026-06-02_elevenlabs_webinar-recap-deploying-agents-across-every-channel.md

Source: raw/articles/2026-06-03_elevenlabs_ai-customer-service-agents.md

### PhysicsWallah Education Case Study (June 2026)

ElevenLabs partnered with **PhysicsWallah** (Indian edtech platform) to deploy voice AI across four use cases:

- **AI Doubt Solver** — students ask questions verbally, get instant voice responses in their language
- **Student Calling** — voice generation for counseling two-way conversations, automating outreach that previously required human counselors
- **AI Mentor** — voice bot for emotional well-being, providing human-like supportive interaction
- **Ask AI** — evolved from text-based to conversational voice tutoring

PhysicsWallah reports **90%+ of student doubts already resolved by AI**. The broader thesis: recorded learning is giving way to conversational AI as the primary mode of instruction, with voice as a critical layer making AI interactions feel like natural conversations with human teachers.

> "With ElevenLabs, we've been able to transform Ask AI from a text-based tool into a more human, conversational learning experience. The quality and realism of the voice output has significantly improved how students engage with AI-driven explanations."
> — Sandeep Varma, Head of Data Science & Engineering, PhysicsWallah

Source: raw/articles/2026-06-03_elevenlabs_physicswallah.md

### ElevenCreative Flows Agent (June 2026)

Flows Agent is a conversational AI assistant within ElevenLabs' creative canvas, ElevenCreative Flows — a node-based workspace connecting 50+ image and video models alongside all ElevenLabs audio models into a single visual pipeline.

**How it works**: Describe the desired output in natural language (e.g., "Build me a podcast intro with custom music and voiceover") and the agent selects appropriate models, creates and connects nodes, and executes the full generation pipeline. The agent asks clarifying questions before committing to expensive operations.

**Key features:**
- **Conversational iteration**: Modify outputs through natural language — "Try a warmer voice," "Swap the background to an office," "Make a version in Spanish" — the agent modifies the existing pipeline and re-runs without rebuilding from scratch.
- **Assist mode**: Approval control over costly operations; agent pauses before expensive runs requiring confirmation.
- **Background execution**: Start a complex workflow, close the tab, and return to a completed flow.
- **Multiplayer**: Collaborators in the same workspace can see the agent building nodes and executing generations in real time.

**Significance**: Flows Agent marks ElevenLabs' transition from a voice-synthesis platform to a multi-modal creative agent orchestrator, competing with Runway's Gen-3, Pika, and Adobe Firefly in the AI creative workflow space while leveraging ElevenLabs' audio-native advantages.

Source: raw/articles/2026-06-05_elevenlabs_introducing-flows-agent.md

### Multimodal Input Processing (June 2026)

ElevenLabs introduced **multimodal input processing** for ElevenAgents, enabling agents to process images and PDFs as first-class inputs alongside voice and text. Files reach the underlying model as native messages — preserving spatial relationships, visual layout, and document formatting — rather than being reduced to text summaries.

**Channel support**: File inputs (images and PDFs) supported on web, mobile, and WhatsApp. A single agent can be deployed across all channels simultaneously.

**Two internal input paths**:
1. **File-backed inputs** — Images and PDFs passed as native file references. The platform stores the file, assigns a `file_id`, and the vision-capable model receives the raw file in context. Integration: capture `file_id` from the upload endpoint, include in message payload. Storage is scoped to the conversation.
2. **Inline (everything else)** — Voice transcribed to text, WhatsApp location pins become coordinates+address, contacts become name+phone. No file storage needed.

**SDK/WebSocket flow**: File must be uploaded before the message is sent. Upload returns a `file_id`, then a `multimodal_message` with the `file_id` is sent over WebSocket.

**WhatsApp flow**: Differs from web/mobile. Meta receives the file; ElevenLabs retrieves it server-to-server via the WhatsApp Business API webhook. No client-side upload step — ElevenLabs handles delivery, storage, and agent turn.

**Context across sessions**: Each conversation is processed independently. Post-call webhook delivers transcript, analysis, and file URLs. Dynamic variables inject stored context at session start for return customers. Webhook file URLs are valid for 15 minutes — download immediately.

**Case study — Rohlik**: The European online grocery platform runs agents across phone, web, app, and WhatsApp in six languages, resolving **90% of customer inquiries** automatically using multimodal capabilities.

Source: raw/articles/2026-06-17_elevenlabs_processing-images-and-documents-in-elevenagents.md

### Voice Agent Evaluation Framework (6 Pillars)

ElevenLabs published a comprehensive voice agent evaluation framework (June 2026) defining six pillars for measuring voice agent performance:

| Pillar | Description | Key Metrics |
|--------|-------------|-------------|
| **TTS Voice Quality** | Naturalness, clarity, emotional expressiveness of synthesized speech | MOS ≥4.3, jitter <30ms |
| **Conversation Quality** | Speech recognition accuracy, contextual understanding across turns | STT WER, time-to-first-audio <500ms |
| **Tool Usage & Task Completion** | Autonomous task completion using available resources | TSR >85% |
| **Intelligence** | Reasoning, handling novel inputs, avoiding hallucination | FCR, CSAT |
| **Compliance & Safety** | Regulatory adherence, guardrails | Compliance audit results |
| **Reliability** | Uptime, consistent performance under load | P99 latency, uptime % |

**Production targets**: MOS 4.3–4.5, TSR >85%, time-to-first-audio <500ms. ElevenLabs' Scribe v2 achieves the lowest WER at 2.2% (Artificial Analysis, June 2026), Flash v2.5 and Turbo v2.5 lead in speed, and ElevenAgents deliver ~75ms model inference latency.

**Industry-specific weighting**: Different industries weigh pillars differently — healthcare prioritizes compliance and safety, customer service prioritizes conversation quality and tool usage.

**Common testing mistakes**: Only evaluating clean audio (ignoring noise/accents/edge cases), ignoring P99 latency spikes, testing without realistic multi-turn conversation flows.

See [[concepts/voice-agent-evaluation]] for related concept coverage.

Source: raw/articles/2026-06-20_elevenlabs_voice-agent-evaluation-framework-6-pillars-explained.md

## Ads Engine — ElevenCreative (June 2026)

ElevenLabs launched **Ads Engine** within ElevenCreative, automating ad localization across 50+ languages with direct publishing to Google, Meta, and LinkedIn ad platforms.

**Key capabilities:**
- **50+ language localization**: Automated translation and voice synthesis for global ad campaigns
- **Direct platform push**: Publish localized ads directly to Google Ads, Meta Ads, and LinkedIn Campaign Manager
- **Creative adaptation**: Not just translation — adapts visual and audio elements for cultural relevance
- **Scale**: Enables a single creative asset to be deployed as 50+ localized variants without manual production

Source: [Introducing Ads Engine in ElevenCreative — ElevenLabs Blog](https://elevenlabs.io/blog/introducing-ads-engine-in-elevencreative)

## Anarock Case Study — Voice AI for Real Estate (June 2026)

**Anarock**, India's largest real estate services firm, deployed ElevenLabs voice AI agents to transform their sales operations:

- **5x sales capacity**: AI voice agents handle initial customer outreach and qualification at scale
- **2x booking growth**: Automated follow-ups and multi-language engagement increased appointment bookings
- **Regional language customization**: Voice personas customized for India's diverse linguistic landscape (Hindi, Tamil, Telugu, Marathi, etc.) — critical for reaching non-English-speaking property buyers
- **Human escalation**: Complex negotiations and high-value leads routed to human agents

This case study demonstrates voice AI's killer application in emerging markets where multilingual coverage directly translates to market reach.

Source: [Anarock Case Study — ElevenLabs Blog](https://elevenlabs.io/blog/anarock)

## Voice Agent Latency Optimization (June 2026)

ElevenLabs published a technical deep-dive on voice agent latency optimization, covering the end-to-end pipeline from speech recognition to response delivery.

Source: [Voice Agent Latency Optimization — ElevenLabs Blog](https://elevenlabs.io/blog/voice-agent-latency-optimization)

---

## Related
- [[entities/openai]] — Competitor via GPT-4o voice and TTS capabilities
- [[entities/anthropic]] — Competitor in enterprise AI agent space
- [[entities/nvidia]] — Investor and partner; provides GPU infrastructure
