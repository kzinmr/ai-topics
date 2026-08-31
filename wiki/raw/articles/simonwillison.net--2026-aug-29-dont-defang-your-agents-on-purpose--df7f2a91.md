---
source_url: https://simonwillison.net/2026/Aug/29/dont-defang-your-agents-on-purpose/
ingested: 2026-08-31
sha256: 79f30909b663c9de5fd01a9a895457ec5603232a1898e52ba3f06410b2949890
---

# Don't Defang Your Agents, on Purpose

Author: Simon Willison
Published: 2026-08-29
Source: Mozilla Festival 2026 talk, transcribed/summarized by LLM (body text recovered via Wayback Machine; Google takeout at simonwillison.net/defang/)

Simon's Mozilla Festival 2026 talk argues against deliberately handicapping ("defanging") AI agents out of fear. Key points as recovered:

- Anthropic's Fable 5 model — a "Claude Mythos-class" model — is a key example: Simon argues its capabilities justify running it unleashed (with sandboxing + monitoring) rather than in a neutered configuration.
- He demonstrated a live agent session that went off the rails during the talk itself, and used it as evidence for his argument: the answer to an agent misbehaving is more supervision and better harness engineering, not pre-emptively removing the agent's abilities.
- Framing: "deep human understanding" remains the scarce resource; defanging agents shifts risk onto the people who understand the problems least, because they end up working with the weakest tools.
- Defang refers to the claws of the agents — an agent with "defanged claws" is one whose dangerous capabilities (shell, file writes, network) have been removed up-front.
- Simon's conclusion: run dangerous agents in isolated environments with active monitoring; do not substitute capability removal for safety engineering.

Note: full talk body text was not retrievable at ingest time (JS-rendered page + 403s); this raw file captures the confirmed skeleton and recovered fragments. Do not treat unquoted paraphrases as verbatim.
