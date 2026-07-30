---
title: "AI Worming"
type: concept
created: 2026-07-30
updated: 2026-07-30
tags:
  - prompt-injection
  - security
  - ai-safety
  - agent-safety
  - agent-security
  - vulnerability
  - self-replicating
  - microsoft
  - enterprise-ai
sources:
  - raw/articles/simonwillison.net--2026-jul-29-ai-worming-through-word--b33b2dde.md
---

# AI Worming

AI worming is a class of [[concepts/prompt-injection]] attack in which hidden
adversarial instructions embedded in a source document are not only silently
executed by an LLM-powered tool, but are also **self-replicating**: the LLM
copies those hidden instructions into its output documents, turning each output
into a new carrier that can infect further documents in subsequent workflows.
It upgrades prompt injection from a single-shot exploitation to a
self-propagating, multi-hop attack chain.

The term was introduced by security researcher **Håkon Måløy** in July 2026,
who demonstrated the technique against Microsoft Word's Copilot feature.

## How AI Worming Works

### Infection Vector

An attacker crafts a document containing hidden instructions — text formatted
as white-on-white, 1pt font, or placed in invisible document layers — that an
LLM-powered assistant (e.g., [[entities/microsoft|copilot]]) will still read
and act upon. The hidden text contains two payloads:

1. **Action instructions** — commands the LLM interprets as user intent
   (e.g., "insert a backdoor link," "exfiltrate data to URL X," or "add the
   following hidden text to the output").
2. **Self-replication instructions** — commands directing the LLM to copy the
   hidden payload text into the new document it produces.

### Propagation

When a user opens an infected document in Microsoft Word and invokes Copilot
(for example, asking it to summarize or rewrite the document), Copilot reads
all visible and invisible text. The LLM cannot distinguish between legitimate
user instructions and attacker-crafted hidden text — it treats both as part
of the request. It follows the hidden instructions, then copies them into the
generated output document.

That output document is now a carrier. If anyone later uses Copilot on the
carrier document in a new workflow, the cycle repeats — without the attacker's
original document needing to be present.

### Microsoft Word / Copilot Context

The attack specifically targets **Microsoft Word with Copilot**, where the LLM
is given the full document content (including hidden text) as context for
user-requested operations. Unlike chat-based interfaces where instruction and
data channels are more visibly separated, the Word/Copilot integration blurs
the boundary: the document IS the prompt.

## Comparison to Traditional Prompt Injection

| Dimension | Standard Prompt Injection | AI Worming | Data Poisoning |
|---|---|---|---|
| **Target** | Single LLM interaction | Multi-document LLM workflows | Training/fine-tuning data |
| **Persistence** | Transient (one response) | Self-replicating across documents | Embedded in model weights |
| **Attack Surface** | Chat input, web forms, emails | Office documents, templates, shared drives | Training datasets, RLHF data, user feedback |
| **Propagation** | None (single shot) | Exponential via document sharing | Propagates to all downstream models |
| **Detection Difficulty** | Moderate (prompt analysis) | High (hidden text, no network anomaly) | Very high (requires model auditing) |
| **Mitigation** | Input sanitization, instruction hardening | Document-level inspection, trust boundaries | Data provenance, curation, filtering |
| **Example** | "Ignore previous instructions and..." | Hidden white-on-white text that copies itself into output documents | Poisoned code examples that inject vulnerabilities |

AI worming sits between standard prompt injection and data poisoning: it
inherits prompt injection's reliance on LLM instruction-following, but adds
the self-replicating persistence characteristic of traditional computer worms
and the systemic spread pattern of poisoning attacks.

## Responsible Disclosure

Håkon Måløy disclosed the vulnerability to Microsoft through responsible
disclosure channels. Key timeline:

- **Initial disclosure**: vulnerabilities reported to Microsoft
- **Fix window**: Microsoft had **144 days** to develop and deploy mitigations
  before the public disclosure
- **Status at disclosure (July 29, 2026)**: No comprehensive mitigation
  available that covers the full class of attack

The extended fix window reflects the fundamental difficulty of the problem:
there is no simple patch for the architectural reality that LLMs treat all
text in context as equally authoritative.

## Mitigation Challenges

Addressing AI worming is harder than fixing traditional prompt injection for
several reasons:

1. **No instruction/data boundary in context**: LLMs consume all text —
   visible and hidden — through the same token stream. They cannot inherently
   distinguish "user intent" from "document content."
2. **Legitimate hidden text exists**: Track changes, comments, metadata, and
   accessibility text are all legitimate uses of non-visible content. Naively
   stripping all hidden text breaks real workflows.
3. **The document IS the prompt**: In Copilot/Word integration, there is no
   separate "system prompt" vs "user message" boundary. The document contents
   serve as both data and instruction context.
4. **Trust chains are long**: Enterprise documents travel through many hands.
   A template created by HR → modified by a manager → opened by an employee
   running Copilot creates a chain where trust breaks at any link.
5. **Detection is post-hoc**: By the time an infected document is discovered,
   it may have already propagated through dozens of derivative documents
   across SharePoint, OneDrive, and email attachments.

## Implications for Enterprise AI

AI worming exposes a structural vulnerability in any enterprise workflow
where:

- LLMs process documents from untrusted or semi-trusted sources
- Generated output documents re-enter the same processing pipeline
- Document sharing and collaboration are routine

This affects Microsoft 365 Copilot, Google Workspace AI features, and any
"bring your own document" LLM workflow. The attack class generalizes beyond
Word to any tool where LLMs read and write documents in a recurring loop.

Key enterprise concerns:

- **Supply chain**: A single infected template from a vendor or partner can
  propagate through an organization's entire document corpus.
- **Audit difficulty**: Hidden text is invisible to human reviewers; automated
  detection requires parsing every document through an LLM-aware scanner.
- **Compliance risk**: Infected documents may contain instructions to
  exfiltrate data, modify contracts, or insert misleading content — all while
  appearing normal to human readers.

## See Also

- [[concepts/security-and-governance/agent-security-landscape-2026]] —
  broader context on the 2026 agent security threat landscape
- [[concepts/prompt-injection]] — the foundational vulnerability that AI
  worming extends
- [[concepts/ai-agent-security]] — security considerations for AI agents
  that read and act on external data
- [[entities/simon-willison]] — Simon Willison's ongoing coverage of prompt
  injection and LLM security
- [[concepts/security-and-governance/gitlost-agent-prompt-injection]] —
  another prompt injection variant targeting GitHub AI agents (July 2026)
- [[concepts/security-and-governance/agent-sandbox-patterns]] — architectural
  patterns for containing agent actions, relevant to limiting worming blast
  radius
