---
title: "Gemini Live audio"
url: "https://simonwillison.net/2026/Sep/15/gemini-live/"
fetched_at: 2026-09-16T10:01:33.421640+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# Gemini Live audio

Source: https://simonwillison.net/2026/Sep/15/gemini-live/

Google released
Gemini 3.8 Live and 3.8 Live Extended Thinking
today - two new speech-to-speech models that are a similar shape to OpenAI's
GPT-Live
family.
I pointed GPT-6 Astra Extra High at the documentation and
had it build me this web UI
for trying out the new models. You can select a model and voice preset, enter an optional system prompt and then start a voice conversation through your browser, including the ability to interrupt the model while it is talking.
The
implementation
uses no libraries. It connects to the
wss://generativelanguage.googleapis.com/ws/google.ai.generativelanguage.v1alpha.GenerativeService.BidiGenerateContent?key=...
WebSocket endpoint and uses a Web Audio API
AudioContext
for both capture and playback.
Here's
the Gemini Live tutorial
for getting started with that WebSockets API.
