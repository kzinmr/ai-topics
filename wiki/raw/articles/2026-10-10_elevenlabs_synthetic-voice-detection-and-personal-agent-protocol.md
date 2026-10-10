---
title: "Defining how AI agents interact with your business"
source: "ElevenLabs Blog"
url: "https://elevenlabs.io/blog/synthetic-voice-detection-and-personal-agent-protocol"
scraped: "2026-10-10T06:00:52.788144+00:00"
lastmod: "2026-10-09T21:10:51.341Z"
type: "sitemap"
---

# Defining how AI agents interact with your business

**Source**: [https://elevenlabs.io/blog/synthetic-voice-detection-and-personal-agent-protocol](https://elevenlabs.io/blog/synthetic-voice-detection-and-personal-agent-protocol)

Blog
Product
Defining how AI agents interact with your business
Written by
Marco
Mancini
Jonatan
von Martens
Published
Oct 9, 2026
Listen
Listen to this article
0:00
0:00
0:00
1.0x
Contact sales
See ElevenAgents
On this page
Introduction
Detecting AI agents on live calls
Joining the Personal Agent Protocol
What's next
A growing share of the calls reaching businesses and governments aren't people. They're personal AI agents running errands for individuals, business agents confirming orders or checking claims, and occasionally a cloned voice posing as a customer.
Today, we’re releasing synthetic voice detection in ElevenAgents, so businesses can tell who’s on the line and respond accordingly. We’re also joining the Personal Agent Protocol working group as a design partner, to help define how AI agents and businesses should identify themselves and interact with each other.
Detecting AI agents on live calls
Synthetic voice detection analyzes the caller’s speech in the first few seconds of a call and returns a determination: human or AI generated. From there, your rules decide what happens.
A few examples of the rules you can set:
Serve verified human customers first.
A human customer gets your most capable AI agent or a human representative, with everything that implies: moving to the front of a queue, negotiating a bill, applying a retention offer, or making a judgment call.
Give AI callers direct, bounded exchanges.
Machine callers go to an agent with its own instructions and limits. It authenticates first, then answers quickly and within scope. You decide how far it can go on negotiation, account changes, or exceptions. If the call does need a human, AI callers can sit lower in the queue than the people waiting.
Stop impersonation at the start of the call.
A synthetic voice requesting a sensitive action (such as a bank account change, a password reset, or access to another account) can be stopped before it gets information or takes action it shouldn’t.
Synthetic voice detection runs inside ElevenAgents on the live audio stream, checking for traces a human listener wouldn’t notice but software can. All audio generated with ElevenLabs carries a watermark, but audio from other sources often doesn’t, so detection doesn’t depend on one being there.
Joining the Personal Agent Protocol
We’re working to design new standards for agents interacting with businesses, and we’re excited to contribute to the Personal Agent Protocol as part of the working group led by Meta and Sierra. The protocol is being developed to define how a personal agent identifies itself to a business, who it represents, and what it’s allowed to do on that person’s behalf.
Businesses use ElevenLabs to deploy agents across many text and voice channels: phone, website, in-app experiences, email, WhatsApp, SMS, and more. Our goal is to ensure all channels are covered, so customers can define how they interact with personal agents across every interface.
What's next
Today, synthetic voice detection is available to enterprise customers supported by our Forward Deployed Engineering team. Later this month, it will come to a broader group of enterprise customers as a configurable option inside ElevenAgents.
As standards like the Personal Agent Protocol take shape, we’ll add support for agents that declare themselves, and we’ll continue adding signals as the space matures.
To learn more, ask your account team or get in touch with us
here
.
