---
title: "Aakash Gupta"
type: entity
created: 2026-06-23
updated: 2026-10-31
tags:
  - person
  - agent-safety
  - ai-agents
  - context-engineering
aliases: ["aakashgupta"]
sources:
  - raw/newsletters/2026-10-31-claude-duet.md
  - raw/newsletters/2026-10-26-ai-by-aakash-meet-claude-your-new-video-editor.md
  - https://x.com/aakashgupta/status/2067550891843186980
  - raw/newsletters/2026-08-14-grok-bot.md
related:
  - concepts/agent-safety
  - concepts/context-engineering
---

# Aakash Gupta

**Aakash Gupta** (@aakashgupta) is a software engineer and researcher focused on AI safety frameworks and agent architecture, particularly around **separation of duties** in agentic workflows.

## Focus Areas

### Agent Safety Separation of Duties
Gupta's work centers on designing structural safeguards that prevent AI agents from operating outside their intended scope. The **Separation of Duties** principle in agent systems mirrors security best practices from traditional software engineering — ensuring no single agent has unchecked access to critical operations.

### Agent Architecture
Exploring structural designs for autonomous agent systems that maintain safety guarantees while enabling complex multi-step workflows.

## Key Ideas

- **Separation of Duties for AI Agents**: Applying the principle of least privilege and role-based access control to agent architectures. Each agent should have clearly scoped permissions and explicit boundaries.
- **Structural Safeguards**: Rather than relying solely on model-level safety, embedding safety constraints into the orchestration layer of agent systems.

## Grok Bot Review (Aug 2026)

Gupta published a **7-day-trial hands-on review of [[events/grok-4-6-launch|Grok Bot]]** (AI by Aakash, Aug 14, 2026), the day after xAI's launch. Key observations:

- **xAI's $60B acquisition of Cursor closed** the week of the launch — pairing the acquisition with "what some are calling the product launch of the year."
- **Multi-agent substrate**: each bot runs a **persistent cloud computer**, logs into your apps, and handles tasks across interfaces; it returns to the human **only for approvals**; multiple bots run at once and coordinate on their own.
- **Skill self-evolution**: bots can grow their own skills over time — an architecture similar to Hermes-style skill systems ([[concepts/ai-agent-engineering]]).
- **Chief of Staff coordination**: xAI positions a coordinating agent that directs the other bots.
- **Verdict**: better single products exist (Autoresearch, GBrain, Hermes, ChatGPT Work, Claude Design, Cowork), but Grok Bot is **"xAI's strongest entry"** into the AI teammate category.

The review connects to Gupta's broader agent-safety focus: the approval-gated autonomy design (human-in-the-loop for sensitive actions) is an instance of structural safeguards applied to a commercial multi-agent product.

## Claude Code as a Video Editor (Oct 26, 2026)

Gupta's flagship hands-on deep-dive of the month: **"Meet Claude, your new video
editor"** ([[raw/newsletters/2026-10-26-ai-by-aakash-meet-claude-your-new-video-editor.md|raw]]),
testing the Claude 5.5 series inside Claude Code as an end-to-end video-editing agent.
It is one of the more concrete published accounts of a general-purpose coding agent
driving a media pipeline (ffmpeg-style) rather than a repo.

**Headline results he reports:**
- A **60+ minute podcast → 3 shorts in ~7 minutes**; the clip-selection pass alone took
  **2 minutes** and used **8 of its 60 available tool calls**. Claude picked a 40-second
  moment at 49:31 about "shipping twice as fast with the same bug rate" on the stated
  criterion of "the moment a PM would stop scrolling for."
- **18 motion-graphic effects** generated from a 5-second clip of himself, each rendering
  in **10 seconds to ~5 minutes on a Mac**; **2 of 20 failed** (the clone effect, and a
  vertigo zoom that just reads as a wider lens unless it moves). He ships 12 editing
  skills plus an animation kit.
- A **31K-view short** (his channel's second-best ever) from this workflow.

**The transferable technique — "talk to your editor on tape."** While recording, Gupta
speaks editing instructions out loud to Claude; **Whisper** transcribes them into the
same transcript the agent reads, so directorial notes arrive inline with the material
they refer to ("take my last take of something", "too much background noise, can't use
that part", "make sure I'm not looking down", "volume equalization because I was away
from the mic"). He explicitly frames this as *the same instructions you'd give a human
editor* — i.e. the interface change is not a new skill, it is removing the transcription
step between intent and material.

**Cost/comparison datapoint:** a **$47 human-edited** version of a 26-minute raw episode
versus Claude reaching a **9:07** cut by the third iteration.

**Failure modes he documents (the useful part):** Claude picked a hook that was an
unreadable screen-share at 9:16 aspect — so he still selects hooks by hand; some effects
read as dated memes; he keeps notes-to-Claude like *"it was better when it was clean,
just typing in"*. His conclusion — "so bye bye Premiere" — is qualified by these.

**Context: the "Black October" news block** in the same issue is where Gupta's security
focus surfaces: ~27 major incidents counted in about a day, the PHP RCE
([[events/php2shell-php-rce-2026]]), a hacker breaching 100+ companies (incl. John Deere)
at **~$50 of AI tokens per break-in**, key theft from OpenCode users, and Microsoft's
**Storm-0940 / ARTEX** agentic-pentester campaign reaching privileged cloud access in
under 3 hours in some intrusions. His line: *"every company sitting on a secret bug now
has until the first rumor leaks and somebody with an AI subscription goes looking."*

### Claude Duet review + Anthropic IPO thesis (Oct 31, 2026 issue)

The Oct 31 issue ([[raw/newsletters/2026-10-31-claude-duet.md]]) is a three-part essay that shows Gupta's house style — practitioner review + investment analysis + weekly roundup:

- **Claude Duet hands-on**: judged against the proactive-agent race (Instinct, Muse, Hermes, Grok Bot); verdict "Claude Code is the best AI harness" and Duet does not replace it; criticizes the fixed Opus 5.5 backend (no model/effort picker), weak local-session recall, and prompt-dependence. Contrasts Grok Bot's "Vault" secret storage as the differentiator Duet lacks. See [[concepts/duet-style-hierarchical-assistant]].
- **Anthropic IPO thesis**: the most-cited breakdown of the public S-1 in this wiki — $72.4B of the $80.7B H1 loss is non-cash SAFE/convertible marks, Q2 operating profit $974M, 11,900+ $100K+ enterprise customers, buy-the-IPO stance at $1.5–2T. Content ingested into [[entities/anthropic]] §S-1 financial breakdown.
- **Gemini 4 Carbon / Alphabet Q3**: harness-behind-Anthropic judgment plus the search-revenue slowdown motive reading (12% vs 17%, stock −8%). See [[concepts/gemini/gemini-4-carbon]].

## Related Concepts
- [[concepts/agent-safety]] — Broader AI safety frameworks
- [[concepts/ai-agents]] — Agent architectures
- [[concepts/context-engineering]] — Context management in agent systems
- [[entities/akash-gupta]] — Related researcher (separate individual with adjacent focus area)

## Sources
- [Agent Safety Separation Of Duties](https://x.com/aakashgupta/status/2067550891843186980)
