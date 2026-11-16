---
title: "Your Agent Will Pick the Hackable One (Geoff Stearns)"
url: https://geoffstearns.com/blog/your-agent-will-pick-the-hackable-one/
date: 2026-11-15
fetched_at: 2026-11-16T11:12:00Z
source: active-crawl
status: raw
tags: [ai-agents, hardware, open-source]
---

# Your Agent Will Pick the Hackable One

Geoff Stearns, geoffstearns.com, surfaced HN 2026-11-15 (75 points / 59 comments).

The M-VAVE FM-1 is a pocket FM synthesizer that sells for about $70, and almost nobody who owns one still runs the firmware it shipped with. Owners started writing their own in September. By October there were too many to cover in one article: a virtual analog synth, a multitrack groovebox, a dark ambient sampler, and a port of Doom. Going by what developers post on the forums, nearly all of them were written with AI coding tools.

Then M-Vave did something uncommon for a hardware company. In October it published its own firmware as open source under GPLv3, along with a development kit and a browser emulator for testing custom builds before flashing.

Thesis: this is where most consumer gadgets that run their own firmware are headed — synths, TVs, routers, printers. When software is cheap to write, the firmware a device ships with is just the first version. Devices that let owners replace it will sell better than devices that don't. Most buyers won't care about that. **Their AI agents will, and more buying decisions are going to run through agents.**

## Owners already replace the software

- Cheap retro handhelds (Anbernic etc.) ship with firmware buyers replace within days; muOS and Knulli are the standard recommendations.
- Pebble came back as a fully open project; Core Devices published OS, phone apps, and hardware schematics.
- Google TV home screen replaced with a custom ad-free launcher; Ubiquiti owners hook network controllers to AI agents via community-built servers, having the agent audit firewall rules and tune the network — not custom firmware, but the agent is already running the device.

## Writing firmware got cheap

- Writing firmware used to mean reverse engineering the chip, learning a vendor toolchain, weeks of trial and error. The FM-1 runs on a JieLi chip with little public documentation, and owners still had working firmware within weeks.
- AI made each part cheaper: reading undocumented code, writing new code for an unfamiliar chip, building the editors/installers/emulators around it. A motivated owner can get through all of it in a weekend. Once true, any device with writable flash is a platform whether the maker planned for it or not.

## Agents will do the installing

- Today custom firmware reaches a small group (a few write it, a somewhat larger group installs it). That won't last: as agents take on everyday work, the owner stops being the installer. You ask your agent to fix something that bugs you; it tries a setting, then looks for firmware someone else wrote, forks the closest match, or writes its own. You see the problem went away and may never know the device runs custom code.
- Adoption speed depends more on hardware than AI: the device must accept new firmware (signed firmware and locked bootloaders stop it); the agent needs a way in (USB or a browser tool like M-Vave's Workbench); and a bad install must be recoverable — an agent can't open the case to unbrick a board. M-Vave added a tool that restores stock firmware in about ten seconds.

## Implication (title claim)

When agents choose and modify device software, hackability and openness become selection pressures: agents will pick (and write) the hackable firmware, making open firmware a competitive product feature.
