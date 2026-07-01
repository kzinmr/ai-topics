---
title: "Claude Code is steganographically marking requests"
date: 2026-06-30
type: raw_article
sources:
  - https://thereallo.dev/blog/claude-code-prompt-steganography
  - https://news.ycombinator.com/item?id=?? (HN 2100 pts)
source: hn-algolia
status: js_blocked_partial
---
# Claude Code is Steganographically Marking Requests

**Source:** thereallo.dev (blocked .dev TLD). Retrieved via HN Algolia API discussion.

**HN Stats:** 2100 points, by kirushik

## Summary from HN Discussion

Claude Code is reportedly using steganographic techniques to embed watermarks/fingerprints in API requests. This appears to be an anti-distillation and anti-reseller measure implemented by Anthropic.

Key points from the HN discussion:

- The technique resembles anti-observation methods used by sophisticated malware
- It uses simple regex-based stego patterns in prompts
- The feature primarily affects "normal developers doing weird but legitimate things" — easier to fingerprint
- Some commenters question why such a simple obfuscation method was used rather than more sophisticated approaches (hashes, bloom filters)
- One commenter noted: "Claude code does feel very malwarey to be honest. They have been like that from the start."
- Privacy concerns raised: if they collect this data for analysis, what actions do they take on it via their API?
- The technique targets resellers and distillation attempts
- One user reported using Claude Code for a month specifically to build their own harness to avoid Anthropic's practices

## Relevance

This represents a significant development in AI content provenance and anti-abuse measures. It raises questions about:
- AI watermarking techniques and their sophistication
- Privacy implications of embedded tracking in LLM API calls
- The arms race between model providers and unauthorized resellers/distillers
- Legitimate developer friction from anti-abuse measures
