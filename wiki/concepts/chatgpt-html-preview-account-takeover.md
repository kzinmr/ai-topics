---
title: "ChatGPT HTML Preview Account Takeover (Parameter Labs, Oct 2026)"
type: concept
created: 2026-11-01
updated: 2026-11-01
tags:
  - security
  - agent-safety
  - prompt-injection
  - vulnerability
  - ai-agents
  - openai
confidence: high
status: active
sources:
  - raw/articles/2026-10-31_parameter-do-the-math-chatgpt-account-takeover.md
  - raw/articles/simonwillison.net--2026-oct-31-how-we-took-over-chatgpt-accounts--8a2a7527.md
related:
  - concepts/sandbox
  - concepts/prompt-injection
  - concepts/security-and-governance/agent-sandboxing
---

# ChatGPT HTML Preview Account Takeover (Parameter Labs, Oct 2026)

On October 31, 2026 Parameter Labs disclosed a cross-origin attack chain — "Do the Math: How We Took Over ChatGPT Accounts" — that turned an ordinary **public ChatGPT share link** into attacker-controlled JavaScript executing inside the signed-in session of whoever opened it. Opening the link was the *only* required victim action: no app install, project join, code paste, or dev-tools.

## Attack chain

1. **Entry**: attacker publishes a malicious conversation via ChatGPT's normal sharing feature; the conversation contains an HTML **Preview** (formerly "Canvas"/artifacts) block plus a graph.
2. **Sandbox boundary**: Preview HTML runs sandboxed in an iframe on a separate origin — `parent.document` is inaccessible, as designed.
3. **postMessage bridge**: the interactive graph loads **MathLive**, which installs a `postMessage` listener in the *main* chatgpt.com page for its virtual-keyboard feature. The listener renders content via **`innerHTML`** with no origin/sender restriction, so the sandboxed Preview frame could inject HTML into the parent page.
4. **CSP bypass**: `innerHTML` cannot execute `<script>`, and OpenAI's CSP allowed script loading only from a few domains — one of which was **YouTube**, whose oEmbed endpoint reflects attacker-controlled data in a way that executes JavaScript. Injecting an unsandboxed iframe loading the YouTube oEmbed URL yielded full JS execution *as chatgpt.com*.
5. **Impact**: the payload enumerated the victim's conversation list, read content of private (never-shared) conversations, called authenticated APIs as the victim (account changes, actions on their behalf), and exfiltrated data via an image reference.

OpenAI fixed the issue on **October 26, 2026**, classified the report **P1**, and paid a **$5,000** bug bounty — which Simon Willison called "a bit cheap for a vulnerability this serious" (HN 335 pts, 165 comments).

## Why it matters

- **Composition-of-safe-primitives failure**: each element (sandboxed iframe, postMessage API, CSP allowlist, third-party oEmbed) is individually legitimate; the break is in their *interaction* — the same escape class as [[concepts/cve-2026-55607-claude-code-sandbox-escape]], one of several sandbox escapes found in AI developer tools.
- **Share-link threat model**: ChatGPT share URLs are treated as inert content by users, but any user-generated HTML rendered inside the product origin is an untrusted-code execution surface — the same class as prompt-injection-driven tool abuse in [[concepts/prompt-injection]], here escalating from data disclosure to *session hijack*.
- **Sandboxing lesson for agent products**: iframe `sandbox` + separate origin is necessary but not sufficient; every message handler reachable from the frame is part of the TCB. See [[concepts/security-and-governance/agent-sandboxing]].
- Bug-bounty economics for frontier AI surfaces (P1 session takeover at $5k) are likely to stay under-priced relative to impact.

## See also

- [[entities/openai]] — vendor
- [[entities/simon-willison]] — early commentator on the bounty's pricing
- [[concepts/agent-safety]] — the broader containment problem
