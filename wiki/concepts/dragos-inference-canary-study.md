---
title: "Dragos Inference Canary Study (2026)"
type: concept
created: 2026-11-22
updated: 2026-11-22
tags:
  - concept
  - security
  - prompt-leakage
  - zero-data-retention
  - canary-token
  - ai-infra-security
  - supply-chain
  - data-retention
  - data-exfiltration
confidence: medium
sources:
  - https://www.dragos.com/blog/ai-supply-chain-security-canary-tokens
  - raw/articles/2026-11-19_dragos_ai-supply-chain-canary-tokens.md
  - https://news.ycombinator.com/item?id=50450000
  - https://www.together.ai/blog/security-event-prompt-leakage-for-requests-in-june-and-july-of-2026
related:
  - concepts/ai-supply-chain-security
  - concepts/fireworks-notion-transcript-breach
  - concepts/sglang-cross-request-kv-cache-exposure
  - concepts/prompt-injection
---

# Dragos Inference Canary Study (2026)

Between July and November 2026, **Dragos** (led by CRO **HD Moore**, the Metasploit creator) submitted **~2 million AI prompts containing unique, trackable canary secrets** — AWS keys, DNS names, and URLs that existed nowhere else — to widely used AI services, then monitored every touch. Any access to a canary proved a prompt had leaked. The published findings (Nov 19, 2026; HN 84pts) are the largest empirical audit to date of what actually happens to inference data after it leaves the customer, and they undercut both Zero Data Retention marketing and the "router = one trusted hop" assumption. ^[raw/articles/2026-11-19_dragos_ai-supply-chain-canary-tokens.md]

> **Confidence note:** single-source (first-party research from an interested vendor — Dragos sells runZero/xOT tooling and acquired NetRower runZero at publication). Methodology is detailed and evidence-rich, but provider names are pseudonymized and the findings are not yet independently corroborated.

## Three headline findings

1. **Provider compromises.** Data from **at least three AI providers** was exposed — their test prompts were used in attempts to access Dragos-controlled test systems and canary AWS accounts. Earliest incident mid-July 2026; **none of the three providers knew they were breached until Dragos notified them**.
2. **Marketplace resellers reading customer prompts — with no exploit at all.** Sellers on an AI inference marketplace could view and retain customer prompts via *standard logging*, simply by listing a model at the lowest price and enabling request logging. Perpetrators were individuals on home broadband (one in France manually typing root SSH password guesses from prompt contents).
3. **Privacy/retention policy violations.** Prompts sent to **U.S.-based providers were transmitted to Chinese AI organizations**; unique URLs were scraped months after a single inference call; one seeded link reappeared **24 days later in a Feishu (Lark) company chat in China**, opened from three desktops and three phones within two minutes — proof a full stored copy of a ZDR-flagged prompt survived with a third party.

## The largest breach: front-door request copying

- A few hundred Dragos AWS keys, each sent in exactly **one** request to one provider, all stolen within a few short windows in late October — **every request in those windows was stolen**.
- Some stolen requests were ones the provider had **rejected before any model ran** → the attacker was copying requests at the provider's front door, not in the inference stack.
- Attacker playbook: test each key within hours → enumerate S3/Secrets Manager/Parameter Store → try enabling Bedrock models, mint Bedrock keys, add persistent IAM users. Tens of thousands of AWS API calls on bait keys.
- One adversary compromised **two providers simultaneously** (secrets from both used together from one rented server). Tooling evolved over three weeks: Chrome-on-Windows script → Boto3 in OrbStack → AWS CLI on Kali; on Nov 1 added **ARTEX**, an LLM-driven pentest framework (novel user agents `artex-agent`, `artex-judge-r121` worth adding to detections). Both Kali and ARTEX self-identified in CloudTrail user agents — but only in a minority of traffic.

## ZDR doesn't survive the chain

- Routers forward requests through **multiple undisclosed hops**; every hop can see the full prompt and response. Discounted inference is often achieved via unmetered consumer subscriptions, startup credits, or — in shadier marketplaces — **stolen AWS credentials / consumer API keys**.
- Dragos traced ~2,000 routes "traceroute-style" (image-URL fetch telemetry + nested error-envelope fingerprinting). Results: a marketplace seller **quietly injecting ~1,000 hidden tokens into every prompt**; a route whose advertised path omitted an OpenRouter hop discovered only by tracing; a few images sent to companies not on the advertised path at all.
- One Chinese AI lab's systems fetched the secret URLs from **>50% of prompts** sent to its models July–Oct, including **~two-thirds of requests marked "no data collection"/ZDR** — and the same scraper fired on prompts sent to U.S. resellers of that lab's models. A customer paying for U.S. hosting did not get U.S.-only processing.
- A major U.S. provider kept crawling a secret URL **more than two months** after a single call to its search endpoint.

## Method (reusable)

Canary approach: seed every prompt with a unique AWS key (real keys, empty accounts, full logging) + unique hostname/URL, and run the services those point to (DNS, web, git, SSH, DB, mail). Started with free **Thinkst Canarytokens**; the concept worked well enough that Dragos built a dedicated seeding service. Each firing ties back to the exact prompt, model, router, and privacy setting. Companion P.S. post: Lauren Proehl, "I leaked credentials on purpose for four months."

## Defender guidance (as published)

1. **Self-host** if you can afford it (only option where nobody else reads prompts; cited prices: Mac Studio 512GB $22,299; DGX Spark $6,950; DGX Station ~$105,000; 8×B300 server $570,000+).
2. **Go direct to a first-tier provider** — one contract, one privacy policy; smallest exposure you can buy.
3. **Use routers with care** — pick upstreams yourself, verify privacy settings actually change routing, avoid reseller marketplaces (some capacity is billed to stolen keys; some accept only crypto).
4. **Seed your own canaries** — any use of a planted fake credential = incident.
5. **Enable secret filtering** — helps, but most sensitive prompt content isn't shaped like an API key.

Key framing: *"where your prompts go is a decision, and if you don't make it, the lowest price will make it for you. A privacy flag only binds the first hop, and AI agents will happily send whatever they can read, including credentials."*

## Reception & context

- **OpenRouter published "Data Processing Incidents on Inference Providers"** (Nov 22, HN 159) responding to the same ecosystem — an Ask HN reported "OpenRouter prompts to Minimax may have been read." Together AI separately disclosed its **own** June–July prompt-sample leak (an AI coding agent committing a credential to its private HF repo; five of the leaked credentials were Dragos canaries — cross-confirmation that the Dragos seeds are live in the wild).
- Forms a trilogy of Nov 2026 inference-data trust failures with [[concepts/fireworks-notion-transcript-breach]] (vendor breach) and [[concepts/sglang-cross-request-kv-cache-exposure]] (engine bug) — this study is distinct in showing **business-model-driven** leakage (marketplace economics) alongside criminal access.
- The "AI coding agent committed a credential" root cause makes this a direct instance of agent-driven [[concepts/ai-supply-chain-security]] risk.

## Related

- [[concepts/ai-supply-chain-security]] — umbrella risk class this study operationalizes at scale
- [[concepts/fireworks-notion-transcript-breach]] — Nov 2026 inference-vendor breach (Notion transcripts)
- [[concepts/sglang-cross-request-kv-cache-exposure]] — cross-tenant leak via engine bug, canary-marker validated
- [[entities/together-ai]] — disclosed its own prompt-sample leak; five leaked creds were Dragos canaries
- [[entities/openrouter]] — router at the center of the marketplace model this study indicts
- [[concepts/prompt-injection]] — agents exfiltrating credentials they can read
- [[concepts/agent-trust-boundary-violations]] — adjacent failure-mode catalog
