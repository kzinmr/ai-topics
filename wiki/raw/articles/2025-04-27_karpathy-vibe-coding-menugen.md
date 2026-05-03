---
title: "Vibe Coding MenuGen: A Karpathy Case Study"
source: https://karpathy.bearblog.dev/vibe-coding-menugen/
author: Andrej Karpathy
date: 2025-04-27
tags:
  - vibe-coding
  - karpathy
  - case-study
  - deployment
---

# Vibe Coding MenuGen: A Karpathy Case Study

Full article: https://karpathy.bearblog.dev/vibe-coding-menugen/
Project: https://www.menugen.app/

## Summary

Karpathy's detailed post-mortem of building **MenuGen** — an app that takes photos of restaurant menus, OCRs the text, and generates AI images for every dish — entirely through "vibe coding" with Cursor + Claude 3.7. A real product with authentication and payments, featuring a "good and honest 10% markup" on API costs.

## Key Insights

### The 80/20 Trap
While the local prototype took very little time, deploying a "real" app was a "painful slog." Karpathy felt "80% done" with the prototype but it was "a bit closer to 20%."

### API Integration Hurdles
- **OpenAI (OCR)**: LLM hallucinations about deprecated APIs and model names
- **Replicate (Image Gen)**: Heavy rate limiting and documentation lag — queries didn't work because LLM knowledge was deprecated and even official docs were out of date

### Deployment & Infrastructure
- **Vercel**: Required "pushing fake debugging commits" to force redeploys
- **Environment Variables**: Classic mistake — forgetting to manually add `.env` keys to the Vercel dashboard
- **Clerk (Auth)**: Claude hallucinated ~1000 lines of deprecated code; moving to production required custom domain, DNS changes, and Google Cloud Console configuration for OAuth
- **Stripe (Payments)**: JavaScript snippets generated for a TypeScript project. Critical logic error: Claude tried to match payments to users via email addresses (caught by Karpathy — the Stripe email may not match the Google OAuth email)

### LLM Gaslighting
When corrected, the LLM "thanks me... and tells me that it will do it correctly in the future, which I know is just gaslighting."

### State Management
Current app is ephemeral. Adding a database (Supabase) and work queues (Upstash) was "too much bear" for a quick project, leaving the app prone to timeouts.

## Recommendations for Vibe Coding Era

1. **Batteries-Included Platforms**: Need for an "opposite of Vercel Marketplace" — a single opinionated service that pre-configures domain, auth, payments, and DB out of the box
2. **LLM-Friendly Services**: Documentation should be Markdown-first; configurations accessible via CLI/curl rather than complex web UIs. "Don't talk to a developer... Instruct and empower their LLM."
3. **Simpler Stacks**: Considering moving from "serverless multiverse" to HTML/CSS/JS + Python (FastAPI) backend for future projects
4. **Apps as Prompts**: Questioning if apps should be standalone products or "Artifacts" generated on-the-fly by an LLM

## Conclusion
Barrier to app creation dropping to ~zero — anyone can create custom automations as easily as making a TikTok.
