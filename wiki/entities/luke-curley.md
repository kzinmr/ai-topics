---
title: Luke Curley
type: entity
handle: "@lukeslhz"
created: 2026-05-09
updated: 2026-05-09
tags:
  - person
  - voice-ai
  - webrtc
  - moq
  - discord
sources: []
---


# Luke Curley (@lukeslhz)

| | |
|---|---|
| **X** | [@lukeslhz](https://x.com/lukeslhz) |
| **Blog** | [moq.dev/blog](https://moq.dev/blog/) |
| **Role** | Software Engineer @ Discord (formerly Twitch); MoQ Working Group participant |
| **Known for** | WebRTC criticism for voice AI, MoQ (Media over QUIC) advocacy, Warp protocol at Twitch |
| **Bio** | Software engineer with experience at both Twitch and Discord, specializing in real-time communication protocols. Currently involved in the IETF MoQ Working Group, advocating for Media over QUIC as a superior alternative to WebRTC for AI voice applications. |

## Overview

Luke Curley is a software engineer who has worked on real-time communication systems at both **Twitch** and **Discord**. He is a prominent voice in the debate over **WebRTC vs. MoQ (Media over QUIC)** for AI applications, particularly voice-to-LLM pipelines.

Curley's career spans two major platforms that rely heavily on low-latency communication:
- **Twitch**: Work on live streaming infrastructure, encountered latency boundaries with HLS
- **Discord**: Engineering work on voice communication systems, direct experience with WebRTC limitations

His technical perspective is grounded in production experience — he has actually attempted to solve the packet retransmission problem within WebRTC at Discord and concluded it's fundamentally constrained by the protocol's design.

## Core Ideas

### WebRTC is the Problem for Voice AI (May 2026)

Curley's most influential argument, as highlighted by Simon Willison's coverage, is that **WebRTC's fundamental design is mismatched with AI voice use cases**:

> "WebRTC is designed to degrade and drop my prompt during poor network conditions. wtf my dude"

His analysis breaks down several key issues:

1. **Packet Loss vs. Prompt Integrity**: WebRTC aggressively drops audio packets to maintain low latency, but LLM prompts benefit from accuracy over minimal latency. Users would "much rather wait an extra 200ms for my slow/expensive prompt to be accurate."

2. **Impossible Retransmission**: "It's impossible to even retransmit a WebRTC audio packet within a browser; we tried at Discord. The implementation is hard-coded for real-time latency or else."

3. **Trade-off Misalignment**: "Voice AI agents will eventually get the latency down to the conversational range. But reducing latency has trade-offs. I'm not even sure that purposely degrading audio prompts will ever be worth it."

4. **TTS Faster Than Real-Time**: "OpenAI is literally introducing artificial latency, and then aggressively dropping packets to 'keep latency low.' The quality will be degraded."

### Media over QUIC (MoQ) as the Solution

Curley advocates for **MoQ (Media over QUIC)** as a better protocol stack for AI voice applications:

- **QuicTransport**: Browser support makes it viable
- **MoQTransport**: Generic live pub/sub framework designed for CDNs and mass fanout
- **Warp Protocol**: Successfully deployed at Twitch for low-latency streaming

At Twitch, Curley's team "hit a latency boundary of HLS, and WebRTC was really the only option available in the browser. However, the user experience just wasn't good enough for our use-case." This led to investigating QUIC-based alternatives.

> "We gambled on it, it worked great, and soon enough, we had Warp running in production."

### The Adoption Challenge

Curley is realistic about MoQ's timeline:

> "It's going to take years. It's going to take a lot of idiots like myself who want to replace WebRTC. It's going to take a lot of companies who are willing to bet on a new standard."

This pragmatic assessment acknowledges both the technical superiority of QUIC-based approaches and the massive inertia of WebRTC's existing ecosystem.

## Key Quotes

> "WebRTC is designed to degrade and drop my prompt during poor network conditions. wtf my dude"

> "I would much rather wait an extra 200ms for my slow/expensive prompt to be accurate. After all, I'm paying good money to boil the ocean, and a garbage prompt means a garbage response."

> "It's impossible to even retransmit a WebRTC audio packet within a browser; we tried at Discord."

> "Voice AI agents will eventually get the latency down to the conversational range. But reducing latency has trade-offs."

> "Having a single format and protocol across all elements of the distribution chain (contribution, processing, distribution) can improve the efficiency, reduce the errors and conversion costs and improve the overall performance."

## Related Work

- **MoQ Working Group**: Active participant in IETF standardization efforts
- **Warp Protocol**: Low-latency streaming solution deployed at Twitch
- **QuicTransport Origin Trial**: Advocated for browser support of QUIC-based media transport
- **Discord Voice Engineering**: Direct experience with WebRTC limitations in production

## Connection to AI

Curley's work sits at the intersection of **real-time communication infrastructure** and **AI voice interfaces**. His criticism of WebRTC is specifically motivated by its inadequacy for LLM-based voice applications, where:

- Prompt accuracy matters more than sub-millisecond latency
- TTS generation is already slower than real-time, making WebRTC's low-latency optimization counterproductive
- Rich, complete audio input is critical for expensive LLM processing

This positions him as an important voice in the infrastructure layer of the AI stack — someone who understands both the protocol limitations and the AI use case requirements.

## Sources

- https://moq.dev/blog/webrtc-is-the-problem/ — "OpenAI's WebRTC Problem"
- https://www.ietf.org/blog/moq-overview/ — IETF MoQ Working Group coverage
- https://simonwillison.net/2026/May/9/luke-curley/ — Simon Willison coverage (May 2026)
- https://quic.video/ — MoQ project site

## References

- simonwillison.net--2026-may-9-luke-curley--642b0f39
- substack.com--app-link-post--d3f5434c
- substack.com--app-link-post--014d59b5
