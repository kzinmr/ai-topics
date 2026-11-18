---
title: "Mastodon"
type: concept
aliases:
  - mastodon
  - fediverse
  - ActivityPub
created: 2026-04-25
updated: 2026-11-18
tags:
  - concept
  - community
  - privacy
  - open-source
  - platform
  - x-twitter
sources:
  - https://joinmastodon.org/
  - https://activitypub.io/
  - https://github.com/mastodon/mastodon
---

# Mastodon

**Mastodon** is the flagship **decentralized social network** of the "fediverse" — a federated microblogging platform where anyone can run a **server ("instance")** whose users can follow, post, and interact with users on *any other* server speaking the same protocol, **ActivityPub** (W3C standard, 2018). There is no central Mastodon: `mastodon.social`, `hachyderm.io`, `fosstodon.org` and thousands of others form a network in the way email servers form the email network. It is the practical existence proof that Twitter-style public conversation can run without a single owner — and, for this wiki, it is a meaningful **second channel for the AI research/developer community**, where many tracked authors maintain presences alongside X/Twitter.

## Architecture

```
┌─────────────┐   HTTPS/API    ┌──────────────────┐
│ Client apps  │───────────────▶│  Your instance    │
│ web, mobile, │                │  (Ruby on Rails + │
│ Mastodon-    │                │   Postgres +      │
│ compatible   │                │   Redis + Sidekiq)│
└─────────────┘                 └────────┬─────────┘
                                         │ ActivityPub
                          ┌──────────────▼───────────────┐
                          │ Federation: signed HTTP       │
                          │ (LD/JSON) between servers —   │
                          │ inbox/outbox queues, WebFinger│
                          │ discovery, actor model        │
                          └──────────────┬───────────────┘
                              other instances: Pleroma, Akkoma,
                              Glitch_soc, Firefish, Lemmy*, PeerTube*
                              (*same protocol family, different apps)
```

Core design points:

- **Actor-per-user, server-hosted** — identity is `@user@instance.tld`; the server holds the user's timeline, follows, and posts
- **Push-based federation** — posts are *delivered* to followers' inboxes (like email SMTP), not pulled from one API
- **The "moderation trilemma" answer** — each instance sets its own rules and can defederate (block whole servers), so governance is federated rather than platform-wide
- **Open API** — the Mastodon API became a de-facto standard; many third-party clients (and, notably, Bluesky's early API compatibility) target it
- **Toots / boosts / favourites**; chronological timelines, hashtag-following, no algorithmic feed by default (optional "local/federated" timelines)

## History & the big platform migrations

| Date | Event |
|------|-------|
| 2016 | Eugen Rochko releases Mastodon (Germany) |
| 2018 | ActivityPub standardized by W3C; Mastodon adopts it |
| 2019 | **The G** (Gizmodo's celebrity-run instance) launches and collapses within weeks — early lesson that instances are communities needing real moderation |
| 2022 | **Post-Elon Twitter exodus**: mastodon.social adds hundreds of thousands of users; hachyderm.io (founded for AI/ML folks, partly in response to a viral "AI twitter" moment) and post.news surge; the "come find me on the fediverse" meme |
| 2023 | Bluesky (AT Protocol) splits the migration wave; Threads launches; fediverse growth plateaus |
| 2024–2026 | Stabilization: Mastodon 4.x adds trending, admin tooling, verified-links-style features; remains the durable open protocol hub even as VC-backed Bluesky took the migration spotlight. Mastodon gGmbH stewards the project; funding via sponsorships/grants rather than venture capital |

## Why it matters to this wiki

1. **Trackable authorship channel**: many researchers and builders this wiki tracks have Mastodon accounts alongside their X handles, e.g. `@nolan@toot.cafe` for [[entities/nolan-lawson]], `@trenner@mastodon.social` for [[entities/tom-renner]]. Fediverse handles are an identity anchor less subject to platform policy shifts.
2. **AI-lab presence**: Hugging Face runs `huggingface.co` as a Mastodon instance; many AI researchers migrated partially (notably after the 2022 wave and subsequent X controversies). The **Mastodon.social AI/ML communities** were where parts of the "AI twitter" discourse relocated.
3. **Agent-relevant protocol precedent**: ActivityPub is one of the earliest widely-deployed **actor-to-actor federation protocols** — a template discussed in [[concepts/decentralized-agent-orchestration]] and agent-communication-protocol debates: signed, inbox-based, server-mediated actors exchanging structured documents.
4. **Anti-platform politics**: Mastodon is the worked example for decentralization-vs-moderation tradeoffs; defederation as governance is unique infrastructure (instance/blocklist dynamics presage later X-blocklist and deplatforming debates).

## Criticism & limits

- **Usability**: instance choice, no viral discovery, small-network effects ("ghost town" complaints); growth stalled post-2023
- **Moderation fragmentation**: defederation can shield bad neighborhoods; moderation quality varies per admin
- **Spam waves**: 2022 influx brought spam/phishing waves requiring heavy admin tooling investment
- **No reach parity**: AI-industry discourse largely remained X-native; Mastodon serves as a mirror, not a replacement

## Related Concepts

- [[concepts/privacy-engineering]] — self-hosted identity and data sovereignty
- [[concepts/decentralized-agent-orchestration]] — protocol-pattern descendant
- [[concepts/open-source]] / [[concepts/open-source-sustainability]] — Mastodon gGmbH's funding model

## Sources

- [joinmastodon.org](https://joinmastodon.org/)
- [ActivityPub W3C spec](https://activitypub.io/)
- [mastodon/mastodon on GitHub](https://github.com/mastodon/mastodon)
- Eugen Rochko's posts on Mastodon governance and funding
