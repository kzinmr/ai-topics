---
title: "Speed"
source_url: https://learn.chatgpt.com/docs/speed.md
ingested: 2026-09-26
sha256: 715802477886b8379bc8715bbe572ae6d0bd220ac6717e85cbb926a88610f74f
collection: openai-codex-docs
---

# Speed

> For the complete documentation index, see [llms.txt](https://learn.chatgpt.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to the page URL.

**ChatGPT Work and Codex share usage.** Both use the same
  pricing, credits, and usage limits. See [Codex pricing](https://learn.chatgpt.com/docs/pricing) for
  details.

## Fast mode

GPT-5.5 retires from ChatGPT, ChatGPT Work, and Codex on all plans on
October 14, 2026. The OpenAI API isn't affected. See
[GPT-5.5 retirement](https://learn.chatgpt.com/docs/models#gpt-55-retirement) for migration guidance.

Codex offers the ability to increase the speed of the model for increased
credit consumption.

For GPT-5.6, GPT-5.5, and GPT-5.4, Fast mode increases model speed by 1.5x.
GPT-5.6 and GPT-5.5 consume credits at 2.5x the Standard rate; GPT-5.4 consumes
credits at 2x the Standard rate.

For GPT-6 Astra, GPT-6 Sol, and GPT-6 Luna, Fast mode consumes credits at
2.5x the Standard rate where available. See [Models](https://learn.chatgpt.com/docs/models) for model availability and
[Pricing](https://learn.chatgpt.com/docs/pricing#token-rates) for token rates.

Use `/fast on`, `/fast off`, or `/fast status` in the CLI to change or inspect
the current setting. You can also persist the default with `service_tier =
"fast"` plus `[features].fast_mode = true` in `config.toml`. Fast mode is
available in the ChatGPT desktop app, Codex CLI, and IDE extension when you
sign in with ChatGPT. Fast mode is a ChatGPT credit feature. With an API key,
Codex uses API token pricing instead, and ChatGPT credit multipliers don't
apply. API Priority processing has its own billing rate; for GPT-5.6, it costs
2x the Standard API token rate.

<VideoPlayer
  src="/videos/codex/fast-mode-demo.mp4"
  class="[&_video]:mx-auto [&_video]:max-h-[400px] [&_video]:max-w-full [&_video]:w-auto"
/>