---
title: "Signal Technology Foundation"
created: 2026-11-27
updated: 2026-11-27
type: entity
tags:
  - organization
  - nonprofit
  - privacy
  - open-source
  - cybersecurity
  - platform-policy
sources:
  - "raw/articles/2026-11-20_signal_restricting-ai-agents-from-screen-capture.md"
  - "https://signal.org/blog/protecting-your-privacy/"
related:
  - "[[concepts/os-agent-screen-capture-privacy]]"
  - "[[concepts/computer-using-agent]]"
  - "[[entities/openai]]"
---

# Signal Technology Foundation

The nonprofit (US 501(c)(3)) home of the **Signal** encrypted-messaging app, led by CEO **Meredith Whittaker**. It develops open-source client code and the formally verified Signal Protocol, and its business is singularly defined by one guarantee: end-to-end confidentiality for users' conversations.

## Key positions and actions

- **2025** — Added screenshot blocking on Windows 11 to defeat **Microsoft Recall**, which captured the screen every few seconds, OCR'd it, and populated a searchable local database (including disappearing messages).
- **November 20, 2026** — Extended the same defense to **OS-embedded AI agents**: blocks screenshots on iOS 27 (against Siri AI's "Onscreen Awareness") and auto-enables Screen security on Android when Google's "Gemini Intelligence"-style assistants attempt to read Signal's screen. Cannot yet protect macOS. Full analysis: [[concepts/os-agent-screen-capture-privacy]].
- Publicly demands that Apple, Google, and Microsoft ship a **documented per-app opt-out from AI data access** (screen reading, filesystem, notifications, APIs) and publish technical specifications for how OS agents process app data; rejects confidential computing as a sufficient answer.
- Calls out the abuse of **accessibility permissions** as a "skeleton key" for third-party AI agents (e.g., Meta's Muse), and notes "cautiously optimistic" direct engagement from Google and Apple.

## Significance

Signal is the highest-profile example of an **application-layer incumbent whose security model is being invalidated from above by the OS-agent paradigm** — its self-description as "the canary in the coal mine" frames the app-vs-OS privacy conflict as ecosystem-wide, not a Signal-specific bug.

## Related

- [[concepts/os-agent-screen-capture-privacy]] — the 2026-11-20 policy and its analysis
- [[concepts/computer-using-agent]] — the screen-reading paradigm Signal blocks
- [[entities/openai]] — OS-agent integrations (e.g., ChatGPT voice/screen features) intensify the same boundary problem
