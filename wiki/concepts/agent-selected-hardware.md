---
title: "Agent-Selected Hardware (Hackability as a Buying Criterion)"
type: concept
created: 2026-11-16
updated: 2026-11-16
tags: [ai-agents, hardware, open-source, agent-security]
sources:
  - raw/articles/2026-11-15_geoffstearns_agent-will-pick-hackable-one.md
  - https://geoffstearns.com/blog/your-agent-will-pick-the-hackable-one/
confidence: medium
related:
  - "[[concepts/skill-constellations-github-supply-chain]]"
  - "[[concepts/software-supply-chain-security]]"
  - "[[concepts/agent-security-patterns]]"
  - "[[concepts/death-of-browser]]"
---

# Agent-Selected Hardware

**Agent-selected hardware** is Geoff Stearns' thesis (Nov 2026) that as AI agents take over everyday device management, **hackability and open firmware become competitive product features** — because the buyer's agent, not the buyer, evaluates and installs device software. Title claim: *"Your agent will pick the hackable one."* (HN 75 pts / 59 comments, Nov 15 2026.)

## The FM-1 case study

- The M-VAVE FM-1 (~$70 pocket FM synthesizer) is the canonical example: almost no owner still runs the shipping firmware. Custom firmwares written by owners starting Sept 2026 — virtual analog synth, groovebox, ambient sampler, a Doom port — **nearly all written with AI coding tools**, on an undocumented JieLi chip.
- In October, M-Vave open-sourced its stock firmware under GPLv3 plus a dev kit and a browser emulator (Workbench) for pre-flash testing — "uncommon for a hardware company."
- Stearns generalizes: synths, TVs, routers, printers. When software is cheap to write, shipped firmware is just v1; devices that permit replacement will outsell devices that don't. Most buyers won't care — their agents will.

## The mechanism: agents become the installer

1. AI made firmware work cheap end-to-end: reading undocumented code, writing for unfamiliar chips, building editors/installers/emulators. A motivated owner ships custom firmware in a weekend; "any device with writable flash is a platform, whether the maker planned for it or not."
2. As agents take on everyday work, **the owner stops being the installer**: you ask the agent to fix an annoyance; it tries a setting, then finds firmware someone wrote, forks the closest match, or writes its own. The user may never know the device runs custom code.
3. Adoption is gated by hardware policy, not AI: writable flash (signed firmware/locked bootloaders block it), an agent-accessible entry point (USB, browser tool like Workbench), and recoverability — an agent can't open the case to unbrick a board, so fast stock-restore (~10 s in M-Vave's tool) is table stakes.

## Existing precedents (already-normal owner replacement)

- Anbernic retro handhelds replaced within days (muOS, Knulli); Pebble reborn fully open; Core Devices open OS + schematics; custom launchers on Google TV; Ubiquiti owners already connect network controllers to AI agents that audit firewall rules — "the agent is already running the device."

## Security tension

The same property agents select for — writable, hackable firmware — is an attack surface: an agent that autonomously finds, forks, and flashes third-party firmware is also an agent that can pick a *malicious* fork. This makes agent-selected hardware a downstream case of [[concepts/software-supply-chain-security|supply-chain trust]] problems (cf. skill-constellation copy networks, where models can't rank safety by stars) applied to device firmware, and motivates [[concepts/agent-security-patterns|verified-install / recovery patterns]]: signed community registries, recoverable installs, and pre-flash emulators as agent-safety infrastructure.

## Related

- [[concepts/software-supply-chain-security]] — agent-chosen firmware = trust-on-install at machine speed
- [[concepts/agent-security-patterns]] — containment patterns for autonomous install/flash actions
- [[concepts/death-of-browser]] — sibling thesis: agents displace human-facing interfaces; here, human-facing device settings pages
- [[concepts/agweb-browser-for-agents]] — tooling built *for* agents rather than humans, same "design for the agent buyer" shift

## Sources

- [[raw/articles/2026-11-15_geoffstearns_agent-will-pick-hackable-one]] — Stearns essay, HN 75 pts
