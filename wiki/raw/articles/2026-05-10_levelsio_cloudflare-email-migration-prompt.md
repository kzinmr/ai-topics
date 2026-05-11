---
title: "levelsio: Migration prompt — Migrate transactional email to Cloudflare Email Service"
type: raw_article
source: https://x.com/levelsio/status/2053482525780008997
author: "@levelsio (Pieter Levels)"
date: 2026-05-10
scraped: 2026-05-11
tags: [cloudflare, email, transactional-email, migration, prompt-engineering, indie-maker]
---

## Content (X/Twitter Note Tweet — Full Prompt)

If you wanna switch to @Cloudflare Email Sending today, here's my prompt for you, as always I'm unaffiliated, not paid, not sponsored, but I like it.

## Prompt: Migrate transactional email to Cloudflare Email Service

Paste this into Claude Code (or Cursor, or any agent) running inside your project.

---

I want to migrate this codebase's outbound email from its current provider (Postmark / SES / Resend / SendGrid / Mailgun / etc.) to Cloudflare Email Service (public beta, launched April 2026). Help me do this carefully.

### Context: what Cloudflare Email Service is

A new transactional email API from Cloudflare. Endpoint:

```
POST https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/email/sending/send
Authorization: Bearer *** application/json
```

Request body:
```json
{
  "to": "user@example.com",                    // string OR array of strings
  "from": "no-reply@yourdomain.com",           // string OR {address, name}
  "subject": "...",
  "html": "<p>...</p>",                        // optional
  "text": "...",                               // optional (one of html/text required)
  "cc": ["..."],                               // optional, array
  "bcc": ["..."],                              // optional, array
  "reply_to": "...",                           // optional, single string
  "headers": {"List-Unsubscribe": "<...>"}     // optional, e.g. for newsletters
}
```

Success: HTTP 200 + `{"success":true,"result":{"delivered":[],"queued":[],"permanent_bounces":[]}}`
Failure: non-200 OR `success:false` OR non-empty `permanent_bounces`

Pricing: $5/mo Workers Paid plan + 3,000 emails free + $0.35 per 1k after. Roughly 5× cheaper than Postmark. No batch send endpoint — loop single sends.

### Steps

1. **Verify prerequisites**: Cloudflare Workers Paid plan, onboarded sender domain(s), API token with `email_sending:write` scope, Cloudflare account ID
2. **Recommend domain reputation strategy**: Split senders across 2-3 subdomains (mail.domain for transactional, e.domain for cold/recovery, newsletter.domain for newsletters)
3. **Audit existing email sends**: Find every place in codebase that sends email
4. **Add a single helper function**: `sendEmailViaCloudflare()` with config vars, timeout handling, bounce detection
5. **Migrate one low-stakes email type first**: Test end-to-end before scaling
6. **Don't migrate login emails yet**: Magic-link/password-reset stay on current provider until 3 months of clean deliverability
7. **Suggest commit boundaries**: One migration per commit

### Caveats
- Beta product — pricing/SLA not finalized
- No batch endpoint (loop required, ~150ms/send)
- No bounce webhooks yet
- Suppression list auto-managed
- No per-message logs/dashboard yet
- List-Unsubscribe headers passed through verbatim

**Engagement**: 1,602 likes · 54 replies · 65 retweets · 16 quotes · 3,354 bookmarks · 269,035 impressions
