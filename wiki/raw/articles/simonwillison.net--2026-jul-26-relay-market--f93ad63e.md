---
title: "An Inside Look at the Relay Market Powering Token Resellers and Fraud"
url: "https://simonwillison.net/2026/Jul/26/relay-market/#atom-everything"
fetched_at: 2026-07-27T10:17:11.842859+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# An Inside Look at the Relay Market Powering Token Resellers and Fraud

Source: https://simonwillison.net/2026/Jul/26/relay-market/#atom-everything

26th July 2026 - Link Blog
An Inside Look at the Relay Market Powering Token Resellers and Fraud
(
via
) Fascinating investigation by Matt Lenhard into the market that has grown up around reselling LLM tokens at a discount by pooling API keys from various sources.
This looks to be mostly a thing in China. Resellers sell access to an LLM proxy that offers significant discounts on regular API pricing, which they achieve by abusing free trials, proxying through unprotected support bots, or sometimes through stolen credit cards or chargeback attacks.
The software they are using for these proxies is open source - mostly
one-api
and its more actively developed fork
new-api
, both legitimate API proxy products which can be used to load. balance requests across a pool of API credentials.
The buyers are seeking cheap tokens, avoiding geo-restrictions, and in some cases collecting data for model distillation.
I've been cautious about exposing my own LLM-driven applications publicly out of fear of abuse leading to big token bills. The existence of this marketplace makes me even more cautious: there's now an entire ecosystem that can profit from finding a new unprotected endpoint to exploit.
LLM vendors
really
need to get better at offering strict caps for their API keys. I want my LLM apps to stop working the moment they hit a dollar threshold I've set for a period of time.
Here's
the (Chinese language) forum thread
that served as the principal source for Matt's article.
