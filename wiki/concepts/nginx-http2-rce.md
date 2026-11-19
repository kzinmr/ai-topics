---
title: "NGINX HTTP/2 RCE (CVE-2026-123633 / CVE-2026-123007)"
created: 2026-11-19
updated: 2026-11-19
type: concept
tags: [open-source, vulnerability, cybersecurity, memory-corruption, ci-cd-security, ai-security, vulnerability-discovery]
related:
  - concepts/systemic-software-breakdown
  - concepts/ai-vulnerability-discovery
sources:
  - raw/articles/2026-11-18_wiz.io_nginx-http2-rce.md
  - https://www.wiz.io/blog/nginx-http2-rce-vulnerabilities
  - https://news.ycombinator.com/item?id=50547374
confidence: medium
---

# NGINX HTTP/2 RCE (CVE-2026-123633 / CVE-2026-123007)

On **Nov 18, 2026**, Wiz Research disclosed **two critical unauthenticated remote-code-execution flaws in NGINX itself** — the world's most widely deployed open-source web server, fronting **225M+ websites**. Both are rated **Critical, CVSS 4.0 = 9.2**, and both require **HTTP/2 enabled** on the affected server. Because the bug is in NGINX (the "front door"), sites can be exposed even when their own application code is secure.

## The CVEs

- **CVE-2026-123633** — critical HTTP/2 RCE.
- **CVE-2026-123007** — critical HTTP/2 RCE; affects versions **dating back to NGINX 1.9.5 (2015)**.
- Successful exploitation → take over the NGINX server, steal data, tamper with sites, or disrupt services.
- Reported to **F5** (the company behind NGINX); patched releases shipped within ~30 minutes of disclosure.

## Five-team independent collision

The vulnerabilities were **independently uncovered by five teams** — **Wiz Research, Ikotas Labs, Metnir, Rapid7, and Xint** — prompting HN ("Is this some kind of record for bug collision?", Retr0id). Xint (yerimyerimie) noted they found additional bugs and a full chain-to-root writeup at nginx2root.com.

## AI-assisted discovery framing (HN, 1412 pts)

The thread connected this to the same-week surge of AI-accelerated vulnerability discovery (Java4Shell, Ruby2Shell, the CentOS/ONNX cluster):

- K0nserv: with AI-assisted vulnerability hunting "the notion that humans can write non-trivial amounts of C correctly is false … C is not equipped to meet this moment."
- fn-mote: "AI is burning down the internet … are we going to discover in a year that every server online this month had a rootkit installed?"
- leca: "How many hours before this is exploited in the wild? Probably not all that long" given how much detail the writeup carries.
- superkuh: "it seems like it's always HTTP/2 (except when it's regex) with nginx."

Treat the AI-amplification angle as community speculation — the disclosure itself does not attribute the discovery to AI tooling.

## Related

- [[concepts/systemic-software-breakdown]] — same-week memory-safety / supply-chain cluster
- [[concepts/ai-vulnerability-discovery]]

## Sources

- [Wiz — Unauthenticated RCE in NGINX](https://www.wiz.io/blog/nginx-http2-rce-vulnerabilities)
- [HN discussion](https://news.ycombinator.com/item?id=50547374)
