---
title: "AI Worming through Word"
url: "https://simonwillison.net/2026/Jul/29/ai-worming-through-word/#atom-everything"
fetched_at: 2026-07-30T10:06:47.563738+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# AI Worming through Word

Source: https://simonwillison.net/2026/Jul/29/ai-worming-through-word/#atom-everything

29th July 2026 - Link Blog
AI Worming through Word
(
via
) Neat new prompt injection variant by Håkon Måløy, who found a way to upgrade prompt injection attacks against Microsoft Word to full self-replicating worms:
An attacker places hidden instructions in a document that is later used as source material in Copilot for Word. Copilot may interpret those instructions as part of the user’s request, causing it to manipulate the document being drafted or edited. Copilot may then also copy the hidden instructions into the resulting document, turning that document into a new carrier. If the carrier is subsequently used in another Copilot-assisted workflow, the instructions can trigger again and propagate into further documents, even without the attacker’s original document being present.
We've seen plenty of hidden white-on-white text before - the kids
are using it in their job applications now
- but this is the first one I've seen that deliberately copies instructions to self-replicate itself.
It was responsibly disclosed to Microsoft who then had 144 days to work on a fix, but so far (unsurprisingly) there's no mitigation that covers the full class of attack.
