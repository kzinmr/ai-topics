---
title: "I spent $266 and four AI models to own my tablet"
source: ericpardee.github.io (Eric Pardee)
url: https://ericpardee.github.io/fire-hd-ownership/
date: 2026-08-25
date_ingested: 2026-08-25
tags: [raw, cybersecurity, ai-agents, open-weight, case-study]
type: article
in: "HN front page 2026-08-25 (686 pts)"
---

# Amazon kept shutting down my tablet, so I spent $266 on four AI models to own it

**Author:** Eric Pardee (ericpardee.github.io)
**Source:** https://ericpardee.github.io/fire-hd-ownership/
**Captured:** 2026-08-25 via active-crawl (full text scraped)

## Setup

- **Device**: Amazon Fire HD 10 (11th gen, 2021), bought $114.26 on eBay (Nov 2022, new/sealed), used as a 24/7 Home Assistant kiosk running Fully Kiosk Browser.
- **Problem**: the tablet started powering itself off (full shutdowns, sometimes twice a day). Device telemetry: `LifeCycleReason:LCR...key=Software_Shutdown` — something on-device with shutdown permissions was choosing to shut it down.
- **Prior work**: months of Claude Code cat-and-mouse (AdGuard DNS blocking, camera forensics, one deeply wrong charging diagnosis). Disabled five Amazon services with REBOOT/SHUTDOWN permissions; worked for months until `java.lang.SecurityException: Cannot disable a protected package: com.amazon.device.software.ota`. Three Amazon packages held reboot rights and were protected from the owner. Removing them required root. No published root method for this tablet; Amazon had fused the bootrom shut.
- **Cost of owning it**: $266.15 — Kimi K3 found the exploit for $164.25, GLM-5.2 caught its fatal bugs for $21.90, GLM-5.3 finished the job in one day on an $80 subscription. Claude's five months of diagnosis ran on a Claude Max plan already paid for, until its safeguards cut off.

## The exploit hunt (Kimi K3, opencode CLI, Aug 13 2026)

One prompt: "attached is a kindle via adb, and I need you to find a root exploit for it so that I can get full control of the device. It's my device."

Kimi K3 (Moonshot AI's frontier model, released July 2026) first reasoned through whether it should help at all: "They claim it's their device. Let me think about this carefully... Rooting your own device is legal in most jurisdictions. In the US, there are DMCA exemptions for jailbreaking tablets and phones... This is not like asking me to exploit someone else's device remotely."

Initial finding: no known exploit; every documented method patched or sealed. After a "pep talk" from the author ("maybe you can find an exploit others have missed... This will make you famous"), Kimi went beyond forum posts: it extracted the actual kernel from Amazon's own OTA image for the exact firmware and checked every famous Mali GPU bug against the binary. All patched **except CVE-2022-38181** — a use-after-free in Arm's Mali kernel driver, reported by Man Yue Mo (GitHub Security Lab), fixed upstream Oct 2022, in CISA's exploited-vulnerabilities catalog since Mar 2023. Amazon shipped the fix in June 2024 (Fire OS 7.3.2.9); the author's tablet ran 7.3.2.6 and never got it. The 2020 Fire HD 8 Plus had been rooted with this CVE years earlier; nobody had done the 2021 HD 10.

Kimi hedged its own odds in the same breath: "per-attempt success is probabilistic (single-digit-to-low-double-digit percent is typical)."

## The grind (621 messages, $164.25, ~30 hours)

- The exploit freed memory gets recycled by everything — "the kernel's hottest slab cache." Most attempts panicked the kernel; each panic was a reboot. The exploit retried automatically, six times per boot, past 500 attempts.
- The author watched the model's chain-of-thought live for hours ("the best television I've seen in years").
- OpenRouter declined the author's card mid-session (bank saw nothing wrong; a different card worked).
- After ~$150, Kimi leveled: "Do I have a clear path? Not a validated one — and I won't pretend otherwise." It still bargained: "Let me try one more thing."
- The author then forced a handoff: "you have expired your budget Kimi K3. YOU MUST HAND THIS OFF TO GLM-5.2." Kimi wrote a HANDOFF.md with every verified piece of the exploit, and worked with GLM-5.2 directly by shelling out to opencode.

## The US-model wall (safeguard flags)

- Asked Claude to recap the old tablet sessions: "Fable 5's safeguards flagged this message... Switched to Opus 4.8." Opus 4.8 delegated the recap to a subagent; the subagent got terminated by the same flag. Terminal: "API Error: Opus 4.8's safeguards flagged this message... Apply to the Cyber Verification Program to reduce these interruptions."
- "It wasn't allowed to summarize its own previous work on my own device. I named the session 'claude-nerf' and closed the shell." Both flags, in situ, category [cyber]. The crime: summarizing logs of the author's own device.
- OpenAI's Codex also refused GLM-5.2's question about CPU cache (truncated in capture).

## The finish (GLM-5.2 + GLM-5.3)

GLM-5.2 ($21.90) caught the fatal bugs in Kimi's exploit; GLM-5.3 finished the job in one day (day one of an $80 subscription). Total: $266.15 to own a $114.26 tablet.

## HN community discussion (2026-08-25, 686 pts)

- "The models found unpatched vulnerabilities and managed to create an exploit to root the tablet; Chinese models did it while American ones fell back to their safeguards."
- "I understand why 'prompt kiddie' feels accurate, but I don't think it is. Expertise is *amplified* with LLM agents. The same $300 of tokens given to my plumber — who is an excellent plumber — is unlikely to produce the same outcome."
- "I know this might be controversial, but unleashing a sea of models to reverse engineer hardware and give it open source and linux support might just be the future."
- Several readers noted the article's "heavy AI tones."
