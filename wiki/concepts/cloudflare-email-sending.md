---
title: "Cloudflare Email Sending"
type: concept
aliases: ["Cloudflare Email Service", "Cloudflare transactional email"]
created: 2026-05-11
updated: 2026-05-11
status: L2
tags: [cloudflare, email, infrastructure, api, serverless]
sources:
  - https://developers.cloudflare.com/email-service/
  - https://developers.cloudflare.com/email-service/api/send-emails/rest-api/
  - wiki/raw/articles/2026-05-10_levelsio_cloudflare-email-sending-feature.md
  - wiki/raw/articles/2026-05-10_levelsio_cloudflare-email-migration-prompt.md
related:
  - entities/levelsio
---

## Summary

Cloudflare Email Service is Cloudflare's transactional email API, launched in public beta (April 2026). It provides **outbound email sending** and **inbound email routing** — accessible via REST API (from any app) or Workers bindings (native). Priced aggressively at $5/mo Workers Paid plan + 3,000 free emails + $0.35 per 1,000 after, making it the second-cheapest option after Amazon SES.

## Pricing Comparison (1M emails/month)

| Provider | Price/mo | Relative to Cloudflare |
|----------|----------|----------------------|
| **Amazon SES** | $100 | 0.28× |
| **Cloudflare** | $354 | 1.0× |
| SendGrid | $600 | 1.7× |
| Resend | $650 | 1.8× |
| Postmark | $1,206 | 3.4× |

*Source: Pieter Levels, May 2026. Prices approximate — check provider pricing pages for exact tiers.*

## API Overview

### REST API (any platform)
```
POST https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/email/sending/send
Authorization: Bearer <API_TOKEN>
Content-Type: application/json
```

**Request body fields:**

| Field | Type | Required | Notes |
|-------|------|----------|-------|
| `to` | string \| string[] | ✅ | Max 50 recipients per call |
| `from` | string \| {address, name} | ✅ | Must be onboarded domain |
| `subject` | string | ✅ | |
| `html` | string | — | HTML body |
| `text` | string | — | Plain text (one of html/text required) |
| `cc` | string \| string[] | — | |
| `bcc` | string \| string[] | — | |
| `reply_to` | string \| {address, name} | — | |
| `headers` | object | — | Custom headers (e.g., `List-Unsubscribe`) |
| `attachments` | Attachment[] | — | Base64-encoded, max 5 MiB total |

**Response:**
```json
{
  "success": true,
  "result": {
    "delivered": ["recipient@example.com"],
    "permanent_bounces": [],
    "queued": []
  }
}
```

### Workers API (Cloudflare Workers)
```typescript
await env.EMAIL.send({
  to: "user@example.com",
  from: "welcome@yourdomain.com",
  subject: "Welcome!",
  html: "<h1>Welcome!</h1>",
  text: "Welcome!"
});
```

Bind via `wrangler.jsonc`:
```json
{ "send_email": [{ "name": "EMAIL" }] }
```

## Domain Setup & Deliverability

- **Onboard domains** in Cloudflare Dashboard → Email → Email Sending → Onboard Domain
- Auto-adds SPF, DKIM, DMARC, and `cf-bounce` MX records
- **Automatic IP reputation management** and deliverability optimization
- **Auto-managed suppression list**: Hard bounces, repeated soft bounces, and spam complaints get blocked
- **List-Unsubscribe**: Passed through verbatim in `headers` — Gmail bulk-sender compliance requires manual inclusion

## Current Limitations (Beta)

| Limitation | Impact | Mitigation |
|------------|--------|------------|
| **No batch endpoint** | 1,000 recipients ≈ 2.5 min loop | Use cron jobs; fine for async sends |
| **No bounce webhooks** | Can't react to delivery failures asynchronously | Check `permanent_bounces` in response |
| **No per-message dashboard** | Limited debugging | Use `messageId` from response for tracking |
| **Beta pricing** | May change at GA | Will likely remain competitive given Cloudflare's pricing history |
| **New IP reputation** | Deliverability unproven for critical emails | Keep login/password-reset on current provider for 3+ months |
| **No SLA** | Beta service, no uptime guarantee | Not suitable for mission-critical alone yet |

## Domain Reputation Strategy (recommended)

Split senders across subdomains to isolate reputation:

| Subdomain | Use Case | Header Requirements |
|-----------|----------|---------------------|
| `mail.domain.com` | Transactional (login, receipts, password reset) | Standard |
| `e.domain.com` | Cold/recovery (abandoned cart, win-back) | List-Unsubscribe recommended |
| `newsletter.domain.com` | Opt-in newsletters | `List-Unsubscribe` + `List-Unsubscribe-Post` required |

Each subdomain must be onboarded separately in Cloudflare.

## Ecosystem Context

Cloudflare Email Service enters a mature transactional email market dominated by Postmark (developer-focused, premium), SendGrid (enterprise), Resend (modern DX), and Amazon SES (cheapest, but requires infrastructure management). Its competitive advantage is **price + Cloudflare ecosystem integration** — users already on Cloudflare for DNS/CDN/Workers gain email without adding a new vendor.

## Relevance to AI Agents

Cloudflare Email Service is particularly relevant for:
- **AI agent report delivery**: Agents can send daily digests, alerts, and reports via a simple REST API call — no additional email provider needed if already using Cloudflare
- **Email as agent interface**: Combined with Email Routing, agents can receive tasks via email and respond via email — a universal, low-latency human-agent interface
- **Infrastructure consolidation**: AI tools and agents often already use Cloudflare for other services (R2, Workers, D1) — adding email keeps infrastructure in one place
