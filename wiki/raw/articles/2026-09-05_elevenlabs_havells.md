---
title: "Havells brings multilingual voice control to connected home ecosystem with ElevenLabs"
source: "ElevenLabs Blog"
url: "https://elevenlabs.io/blog/havells"
scraped: "2026-09-05T06:00:46.325629+00:00"
lastmod: "2026-09-04T08:11:52.125Z"
type: "sitemap"
---

# Havells brings multilingual voice control to connected home ecosystem with ElevenLabs

**Source**: [https://elevenlabs.io/blog/havells](https://elevenlabs.io/blog/havells)

Customer Stories
Havells brings multilingual voice control to its connected home ecosystem with ElevenLabs
Written by
Vinay
Srinivas
Adarsh
Shiragannavar
Tauseef
Khan
Jitendra
Prajapati
Published
Sep 4, 2026
Listen
Listen to this article
0:00
0:00
0:00
1.0x
Contact Sales
Learn More
On this page
Introduction
Latency and naturalness decided the evaluation
Eight languages that match how Indian households actually speak
One conversational interface across the Havells One platform
Context retention and clarification across multi-turn conversations
Prototype to production in six weeks
Looking ahead
Voice Mode is live across the Havells One user base, an app with approximately 2.7 million downloads, supporting eight languages across seven device categories.
Havells is one of India's leading electrical goods companies, offering a broad portfolio of connected products including air conditioners, fans, air and water purifiers, water heaters, washing machines, and smart switches. To enrich the smart home experience, the Havells Center for Research & Innovation (CRI) developed Agentic AI Voice Mode, an intelligent conversational interface within the Havells One app that enables users to control appliances through natural voice interactions in English and multiple Indian languages. It is built programmatically on
ElevenAPI
, using real-time streaming Speech to Text (Scribe v2 Realtime) and Text to Speech (Eleven v3 Conversational) integrated with Havells' proprietary intelligent device-control agent.
Havells' earlier voice experience initially supported English, then Hindi, across selected appliances, but it remained command-driven. Users had to remember specific phrases and invocation patterns for devices to respond correctly. That is not how Indian households naturally speak, often blending English, Hindi, Marathi, and other regional languages within the same conversation. Agentic AI Voice Mode inverts that. People speak naturally ant the system understands intent, context, and language.
Latency and naturalness decided the evaluation
Havells evaluated several voice AI platforms on language recognition accuracy, multilingual support, latency, and voice synthesis. The team found ElevenLabs while researching providers offering high-quality, low-latency streaming Text to Speech, and shortlisted ElevenLabs on accuracy, speed, and multilingual support, along with the API documentation, the dashboard, support, and the Indian language sample voices.
In head-to-head testing, the difference showed in how quickly and how naturally the assistant responded. For a smart home assistant, latency is not only a technical measure. A delayed reply feels like a traditional voice interface, while a fast one feels like a real-time conversation. Naturalness and real-time responsiveness mattered most to Havells, and both informed the decision to build Voice Mode on ElevenLabs.
Eight languages that match how Indian households actually speak
Voice Mode supports English and seven Indian languages: Hindi, Tamil, Telugu, Bengali, Kannada, Gujarati, and Malayalam. Users control devices by appliance, by room, or by scene, using natural language rather than a fixed command set.
The assistant treats code-mixed and colloquial speech as intent rather than syntax. A request such as "Yaar thoda thanda lag raha hai" (Bro, I am feeling a bit cold) slows the fan and adjusts the air conditioner without the user naming either device.
.
One conversational interface across the Havells One platform
Voice Mode covers multiple smart device categories in the Havells One platform: air conditioners, fans, air purifiers, water purifiers, water heaters, washing machines, smart switches and upcoming devices.
Coverage runs deep within each category as well as across them, spanning models and variants, where voice commands reach speed, modes, timers, and reverse rotation.
Because the same conversational layer sits across all categories, a single spoken instruction can act on smart Havells devices even if they use different connectivity protocols. "Geyser on karo aur fan bhi chalu karo" (Switch on the fan and the geyser) is split and executed across multiple Havells devices at once.
Context retention and clarification across multi-turn conversations
Havells' agent runs ten capabilities in production: natural language understanding, context memory, multi-device orchestration, context awareness, multilingual AI, zero-setup activation, cross-protocol device control, two-way conversational feedback, error diagnostics, and rule-based automation. In practice, that looks like:
"Fan slow karo ... thoda aur"
(Lower the fan speed.. a bit more) is read as a follow-up, so the user does not have to restate the full command.
"AC chalu karo"
in a home with two air conditioners prompts the assistant to ask which room rather than guess.
"AC pe E6 dikh raha hai, kya hua?
" returns a plain-language explanation of the error code and a suggested next step.
Two-way conversational feedback matters as much as recognition here. The assistant confirms what it has done, explains what it cannot do, and asks before taking an action that would otherwise be ambiguous.
Prototype to production in six weeks
Havells had a working prototype of their agent roughly two weeks into the build, validating the path from spoken command to device action to spoken response. The API documentation and dashboard that shaped the platform decision carried into the build itself, and the CRI team integrated streaming Speech to Text and Text to Speech against them directly.
The remaining weeks went into Havells' own complexity rather than the speech layer: the full multilingual device catalogue, varying device capabilities, complex commands, edge cases, and recovery scenarios. ElevenLabs' forward-deployed engineering team worked with Havells to tune voice quality and pronunciation for regional Indian languages, and to configure the streaming setup so latency held steady as concurrent sessions grew. Initial integration to production-ready rollout took approximately six weeks.
Voice Mode is now available to the full Havells One user base, an app that has surpassed 2.7 million downloads. That scale gives the CRI team real-world interaction data to improve across languages, devices, and command types.
This Agentic AI Voice capability is a breakthrough for our customers, allowing them to control and interact with their devices naturally, without having to remember commands or learn rules. Its potential is limitless and will continue to expand as new capabilities are added across our devices and services. As a daily-use AI experience, it showcases the transformative potential of AI agents, far beyond the traditional voice interfaces of the past. Consumers just need a Havells Smart device registered in their Havells One App to use this feature
- Dipesh Shah, Executive President and CTO, Havells
For a hundred years, the appliance industry has sold products. What we are building now is a relationship - a home that senses, learns, and responds to the language and rhythm of the family living in it.
- Harikumar Varrier, Senior Vice President, CRI IoT, Havells
Looking ahead
Havells treats Agentic AI Voice Mode as the foundation of a broader intelligent home experience rather than a finished feature, and has outlined four directions for expansion:
Deeper personalization
, so the home responds to individual household members' preferences and daily rhythms rather than treating every user identically.
Wider language coverage
, on the basis that language remains the largest barrier to adoption in India and eight languages is a starting point.
A voice-first gateway
to the entire Havells ecosystem, complementing apps, individual devices, control panels, and bringing currently unconnected appliances into the ecosystem and then onto the voice platform.
Voice beyond on/off and set-point commands,
extending into product FAQs, troubleshooting, automation routines, and scheduling.
Developed by the CRI team under the philosophy of "Made in India, Made for the World," the platform combines global technology with a deep understanding of Indian homes, languages, and lifestyles. As the ecosystem grows, the focus stays on keeping the experience natural, responsive, multilingual, and personalized, allowing technology to adapt to people rather than requiring people to adapt to technology.
