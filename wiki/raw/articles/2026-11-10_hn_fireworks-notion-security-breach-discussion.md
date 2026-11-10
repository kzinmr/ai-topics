---
title: "Fireworks AI security breach impacts Notion and their customers (HN discussion)"
url: "https://news.ycombinator.com/item?id=50437106"
source: "https://www.notion.com/help/security-incident-involving-a-third-party-ai-vendor"
fetched_at: 2026-11-10T12:15:00+00:00
type: hn-discussion
tags: [raw, hn]
sha256: cf1bf22299d122ef39019db734170cd3098748eded78d5fb48ab39278dd40f87
---

# Fireworks AI security breach impacts Notion and their customers

HN item 50437106, 64 pts / 20 comments (2026-11-10). Notion published a help-page disclosure "Security
incident involving a third-party AI vendor" — the vendor being Fireworks AI, an inference provider in
Notion's AI stack. Early, small-but-first-of-its-kind: an AI inference vendor breach leaking SaaS customer
conversations.

## HN discussion highlights

- [vinaygundeti18] "a company's security is only as strong as its third-party integrations… Businesses need to carefully evaluate vendor security, limit the data shared with external services, and maintain transparency when incidents happen. As AI adoption grows, third-party risk management should become a core part of every company's security strategy."
- [frankotron] "Forcing us to the Enterprise plan to see which members are affected huh? Classy move Notion."
- [Andugal] quotes the disclosure: "Notion AI conversations from 2 members of your workspace may have been affected. Their conversations stay private to them. They have not been proactively emailed… you must share this page with them" — "spending the morning figuring out which users are affected… Time well spent. Thanks, Notion."
- [chinathrow] "We also have 2 members affected in our org. I wonder if this is a coincidence or just a fixed template."
- [edot] key technical question: "Fireworks is ZDR (zero data retention) by default, yet Notion configured Fireworks to retain data? Otherwise, how is there anything to leak?" — pointing at the customer-side retention configuration, not just the vendor, as the exposure surface.

## Open questions (as of 2026-11-10)

- Scope of the Fireworks-side compromise (which customers/models/log stores) not yet public.
- Whether retained prompt/completion logs were the leaked artifact (per edot's ZDR question).
- Notion's disclosure UX (Enterprise-gated affected-member visibility) drawing most workspace-admin anger.
