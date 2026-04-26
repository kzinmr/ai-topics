---
title: Brutecat
type: entity
created: 2026-04-10
updated: 2026-04-10
tags:
- security-researcher
- bug-bounty-hunter
- reverse-engineering
- google-ecosystem
aliases:
- brutecat.com
- brutecat
- dddaaa
sources: []
---

# Brutecat

| | |
|---|---|
| **Blog** | [brutecat.com](https://brutecat.com) |
| **GitHub** | [dddaaa](https://github.com/dddaaa) |
| **Role** | Security researcher, bug bounty hunter, reverse engineer |
| **Known for** | Google ecosystem vulnerability research, API reverse engineering, Ghunt-adjacent OSINT tooling |
| **Bio** | Security researcher specializing in Google's internal API surface. Known for systematic reverse engineering of undocumented Google endpoints, discovery of high-impact vulnerabilities in account recovery and data exposure systems, and development of tooling for converting black-box APIs into analyzable white-box targets. |

## Core Ideas

Brutecat is a **systems-level security researcher** whose work centers on a single, powerful thesis: **large tech platforms hide their most vulnerable surfaces behind abstraction layers, and the key to finding critical bugs is converting those black boxes into white boxes through systematic API discovery and analysis.**

### The Decoding Google Methodology

Brutecat's defining intellectual contribution is a **methodology for reverse-engineering undocumented Google APIs** through what they call "converting a black box to a white box." The approach involves:

1. **Finding discovery documents** — Google maintains "discovery documents" (essentially Swagger/OpenAPI specs) for their public APIs, but these often hide **internal endpoints** behind visibility labels and secret authentication parameters
2. **Extracting API keys and authentication tokens** — By inspecting Android app bundles, web frontend JavaScript, and internal Google services, Brutecat identifies API keys that grant access to broader surface areas than public documentation reveals
3. **Leveraging the `X-Goog-Spatula` header** — This undocumented authentication header, found in Google's internal infrastructure, allows access to API endpoints that aren't exposed in public discovery documents
4. **Reverse-engineering Protocol Buffer definitions** — Google's internal APIs use protobuf instead of JSON. Brutecat developed [`req2proto`](https://github.com/dddaaa/req2proto), a Go tool that reconstructs `.proto` definitions by sending crafted payloads to endpoints and parsing the error messages returned

The core insight: **Google's own error messages are a data source.** By sending malformed requests and analyzing the structured error responses, you can map out entire API surfaces that were never meant to be public. This turns the platform's defensive behavior into an offensive reconnaissance tool.

### The Chain-of-Exploits Pattern

Brutecat's research consistently demonstrates that **the most impactful vulnerabilities come from chaining minor leaks across multiple Google services** rather than finding a single critical bug:

**Google Account Recovery Bypass (CVE-2025, $5,000 bounty):** Brutecat discovered that Google's deprecated JavaScript-disabled username recovery form lacked BotGuard protection. By combining:
- The old recovery endpoint's ability to validate phone numbers
- IPv6 address rotation to bypass rate limiting
- BotGuard tokens harvested from the JS-enabled version to bypass CAPTCHAs
- A technique to leak full display names via Google Looker Studio ownership transfers

...an attacker could brute-force any Google user's full phone number. The attack ran at ~40,000 checks/second on a $0.30/hour cloud server. This wasn't a single vulnerability — it was a **systemic failure of defense-in-depth across multiple deprecation pathways**.

**YouTube Creator Email Leak (March 2025, $20,000 bounty):** In collaboration with Nathan (schizo.org), Brutecat chained two bugs:
1. YouTube's live chat menu endpoint leaked users' internal Google Gaia IDs in base64-encoded responses
2. Google's Pixel Recorder sharing API could convert any Gaia ID into an email address

Combined, this allowed de-anonymizing any YouTube creator. The researchers reported this in September 2024; Google initially classified it as a duplicate worth $3,133, then upgraded after the researchers demonstrated the full chain's impact.

### The Deprecation Lag Vulnerability

A recurring theme in Brutecat's research is **the security risk of incomplete deprecation**. Google frequently "disables" old API endpoints or web flows but leaves them accessible under certain conditions (JavaScript disabled, specific headers, legacy authentication paths). These zombie endpoints lack modern protections and serve as backdoors into otherwise secure systems.

Brutecat's work demonstrates that **large platforms don't fail because their current security is weak — they fail because their past security decisions persist longer than intended.** The attack surface of a company like Google isn't just what's documented; it's everything that was ever built and never fully removed.

### Tool Development Philosophy

Brutecat builds tools that are **purpose-built for a specific attack surface** rather than general-purpose scanners. The `req2proto` tool, for example, was created to solve one specific problem: reconstructing protobuf definitions from Google's error responses. This reflects a broader philosophy shared with researchers in the Google Project Zero ecosystem — **deep understanding of a single system beats shallow scanning of many systems.**

## Key Discoveries

| Date | Discovery | Bounty | Impact |
|---|---|---|---|
| Jun 2025 | Google account recovery phone number brute-forcing | $5,000 | Any Google user's phone number discoverable from display name |
| Mar 2025 | YouTube creator email address disclosure (with Nathan) | $20,000 | De-anonymization of all YouTube creators |
| Feb 2025 | YouTube user email disclosure via Gaia ID + Pixel Recorder | $10,000 | Any YouTube user's email discoverable |
| Nov 2024 | "Decoding Google" methodology published | N/A | Framework for reverse-engineering Google's internal APIs |

## Related

- [[reverse-engineering]] — Binary and protocol analysis of undocumented systems
- [[bug-bounty]] — Coordinated vulnerability disclosure and responsible exploitation
-  — Open-source intelligence gathering techniques
- [[google-tpu]] — Platform under research
-  — Google's internal data serialization format
-  — Layered security architecture and its failure modes

## Sources

- [Decoding Google: Converting a Black Box to a White Box](https://brutecat.com/articles/decoding-google) (Nov 2024)
- [Leaking the email of any YouTube user for $10,000](https://brutecat.com/) (Feb 2025)
- [Disclosing YouTube Creator Emails for a $20k Bounty](https://brutecat.com/) (Mar 2025)
- [Leaking the phone number of any Google user](https://brutecat.com/) (Jun 2025)
- [req2proto — Google protobuf reverse engineering tool](https://github.com/dddaaa/req2proto) (Nov 2024)
- [Google Bug Allowed Brute-Forcing of Any User Phone Number](https://www.darkreading.com/vulnerabilities-threats/google-bug-brute-forcing-phone-number) (Jun 2025)
- [Google fixes flaw that could unmask YouTube users' email addresses](https://www.bleepingcomputer.com/news/security/google-fixes-flaw-that-could-unmask-youtube-users-email-addresses/) (Feb 2025)
