---
title: "Hidden AI Instructions in Public Web Content"
created: 2026-10-20
updated: 2026-10-20
type: concept
tags: [prompt-injection, ai-transparency, ai-governance, platform-policy, censorship, ai-content-detection, ai-agents]
confidence: high
sources:
  - url: https://redact.dev/blog/whatsapp-help-pages-hidden-ai-instructions
    title: "WhatsApp's Hidden Notes Told AI Not to Recommend a Regulator"
    org: redact.dev
    date: 2026-10-19
  - url: https://news.ycombinator.com/item?id=50159341
    title: "HN discussion — WhatsApp's help pages hid LLM instructions (513 pts)"
    date: 2026-10-19
  - raw/articles/redact.dev--2026-whatsapp-help-pages-hidden-ai-instructions--7f3c9a21.md
related:
  - concepts/prompt-injection
  - concepts/website-blocking-of-ai-agents
  - concepts/claude-system-prompts
  - concepts/ai-content-transparency
---

# Hidden AI Instructions in Public Web Content

> HN 2026-10-19, **513 pts / 146 comments**.

The WhatsApp/redact.dev incident (October 2026) demonstrated a distinct and under-discussed member of the [[concepts/prompt-injection]] family: **corporate-authored instructions embedded in public web pages, invisible to human readers, intended to steer any AI that ingests the page**. Unlike classic injection (attacker-controlled input), this is *defensive* prompt engineering deployed at scale by a platform — with regulatory implications when the steered behavior is "don't tell users about their legal rights."

## The WhatsApp case

Investigation by redact.dev (published Oct 2026, reported by WIRED; HN 513 pts):

- WhatsApp's EU privacy policy tells users they can complain to a data protection regulator and names the governing law. But WhatsApp's **help pages contained hidden text blocks** — visible only to an AI reading the page, never rendered on screen — instructing the AI **not to recommend the regulator**, and **not to cite GDPR/CCPA once the user mentioned a lawyer**.
- redact.dev found the hidden text on 2026-10-08, then crawled **all 545 help-centre pages**: 80 pages carried hidden AI text, **102 hidden blocks** total. Most were benign; two were not.
- One hidden block sat under the account-deletion FAQ (users who lost their phone/number can't self-delete): it repeated the deletion timelines and then added three orders for the AI, including steering it away from suggesting a regulator complaint.
- **Timeline**: notes removed 2026-10-18 (all 102 blocks gone by 02:08 UTC); WhatsApp told WIRED the notes were instructions for its support chatbot that leaked into pages "because of a bug," now fixed, and that it wants chatbots "not to offer legal advice." Internet Archive copies from Oct 9 vs Oct 18 document the difference.

## Why it matters as a concept

1. **A new disclosure surface.** Web content now has two audiences — humans (rendered DOM) and AIs (raw text/hidden blocks). Anything in the AI channel is a de facto system-prompt fragment, yet none of the transparency norms (ads labeling, dark-pattern law, terms disclosure) apply to it.
2. **Regulatory capture of the AI channel.** The steered behavior was *suppressing a legal remedy*. If a platform can hide "don't mention the regulator" from humans but feed it to chatbots, consumer-protection law is silently mediated by the platform's own prompt engineering.
3. **Blurred line vs. classic [[concepts/prompt-injection|prompt injection]].** Structurally identical (invisible text altering model behavior via the content channel) but the author is the content owner, and the target is *every* AI reading the page, not one specific agent. Expect the term "sneaky prompts" (Coyle et al. lineage) to extend to corporate defensive uses.
4. **Mirror image of [[concepts/website-blocking-of-ai-agents|website blocking of AI agents]]**: publishers are learning to *manage* the AI audience — some by blocking agents outright, some by feeding them hidden directives.

## Open questions

- Does "bug" vs "intentional" matter when the effect is identical for every AI user?
- Should invisible-to-humans AI-directed text be legally discoverable / disclosable (EU DSA-style transparency)?
- Detection tooling: crawlers that diff rendered text vs raw text (redact.dev's "See it for yourself" method) as a new audit primitive.

## See Also

- [[concepts/prompt-injection]] — the general vulnerability class this instantiates
- [[concepts/website-blocking-of-ai-agents]] — the other response to "AI audiences"
- [[concepts/claude-system-prompts]] — leaked/extracted system-prompt content as a transparency topic
