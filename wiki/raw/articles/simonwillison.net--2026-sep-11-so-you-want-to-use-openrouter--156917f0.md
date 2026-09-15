---
title: "So you want to use OpenRouter?"
url: "https://simonwillison.net/2026/Sep/11/so-you-want-to-use-openrouter/"
fetched_at: 2026-09-12T10:00:55.200801+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# So you want to use OpenRouter?

Source: https://simonwillison.net/2026/Sep/11/so-you-want-to-use-openrouter/

11th September 2026 - Link Blog
So you want to use OpenRouter?
(
via
) One of OpenRouter's selling points is that it "handles fallbacks automatically and picks the most cost-effective option for each request", so you can call a single API endpoint for a model and get routed to the best available backend provider.
Mohamed Moustafa points out a whole set of ways that this can cause you problems. Different providers run different serving software with different optimizations and settings, which means that the same OpenRouter endpoint can serve model requests that behave in different ways.
Some providers even lack vision capability for vision models, and the way the reasoning effort option is processed can differ as well.
Thankfully you can control which provider is routed to using
the provider.only option
. The
/endpoints method
returns the list of available providers for a specific model ID.
