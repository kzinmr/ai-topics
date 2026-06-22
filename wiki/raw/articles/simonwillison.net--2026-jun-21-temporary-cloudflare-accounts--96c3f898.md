---
title: "Temporary Cloudflare Accounts for AI agents"
url: "https://simonwillison.net/2026/Jun/21/temporary-cloudflare-accounts/#atom-everything"
fetched_at: 2026-06-22T07:01:36.763462+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# Temporary Cloudflare Accounts for AI agents

Source: https://simonwillison.net/2026/Jun/21/temporary-cloudflare-accounts/#atom-everything

21st June 2026 - Link Blog
Temporary Cloudflare Accounts for AI agents
(
via
) The announcement says this is "for AI agents" but (as is pretty common these days) the AI hook isn't really necessary, this is an interesting feature for everyone else as well.
Short version: you can now create a Cloudflare Workers project and run this, without even creating a Cloudflare account:
npx wrangler deploy --temporary
Cloudflare will deploy the application to a new, ephemeral project which will stay live for 60 minutes.
I
had GPT-5.5 xhigh
in Codex Desktop
build this test application
providing a tool for following HTTP redirects and returning the final destination. The temporary deployment worked as advertised.
Running the deployment spits out the URL to a page for claiming the new project, for if you want it to last for more than 60 minutes. Here's what that claim screen looks like:
