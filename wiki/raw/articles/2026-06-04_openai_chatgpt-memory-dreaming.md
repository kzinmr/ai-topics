---
title: 'Dreaming: Better memory for a more helpful ChatGPT | OpenAI'
source: 'openai'
url: 'https://openai.com/index/chatgpt-memory-dreaming/'
date: '2026-06-04'
type: raw_article
tags: [raw, source]
fetched: '2026-06-05'
description: 'ChatGPT introduces a new memory system to better remember preferences, keeping context fresh and relevant across conversations.'
---

# Dreaming: Better memory for a more helpful ChatGPT | OpenAI

**Source**: [openai](https://openai.com/index/chatgpt-memory-dreaming/)  
**Date**: 2026-06-04  
**Fetched**: 2026-06-05  

> ChatGPT introduces a new memory system to better remember preferences, keeping context fresh and relevant across conversations.

OpenAI
June 4, 2026
Research
Product
Release
Dreaming: Better memory for a more helpful ChatGPT
Improving memory synthesis in ChatGPT to optimize for freshness, continuity and relevance.
Loading…
Share
Today we’re beginning to roll out a more capable and scalable system for synthesizing memory, developed to tackle the staleness, correctness, and scalability challenges that we observe when memory is applied to the hundreds of millions of users and multi-year time horizons in ChatGPT.
Memory is what helps ChatGPT learn your preferences, projects, and constraints, allowing future conversations to start from shared context rather than from scratch.
Over the last two years, memory has grown into a critical part of the ChatGPT experience, helping ChatGPT better understand your context so it can help you accomplish meaningful goals over time. This is central to making ChatGPT more useful: knowing you, helping you, and doing more for you.
This update is available to Plus and Pro users in the US today, and will roll out to additional countries and Free and Go users over the coming weeks.
How memory has evolved
Memory first launched in April 2024 (also known as saved memories). The feature let you ask ChatGPT to remember information and carry it forward into future chats.
Saved memories were only written during the conversation and relied on strong cues to decide when to trigger memory, such as an instruction to "remember I’m traveling to Singapore in July." In practice, interacting with this system could feel like talking to someone who took a few notes, but still forgot everything that wasn’t written down. Saved memories also tend to go stale over time and eventually become incorrect or irrelevant.
In April 2025, we updated ChatGPT’s memory by giving the model the ability to reference chat context outside of the saved memories list; this was done by introducing the first version of
dreaming
—a method for ChatGPT to
automatically
curate memories in the background by referencing chat history.
In contrast to saved memories, dreaming leverages a background process that allows ChatGPT to learn from many conversations and synthesize ChatGPT’s memory state in order to always provide the freshest, most relevant context to your conversations. Dreaming also makes it easier for memory to include context that occurs naturally in conversation, without relying on explicit requests to remember something.
Over the last year, dreaming
supplemented
saved memories to create a step-function improvement in ChatGPT's ability to personalize responses and offset the staleness of saved memories. However, it historically was never sufficient as a standalone memory system.
Today, we are launching a significantly more capable and compute-efficient memory architecture built on top of dreaming.
The memories synthesized by dreaming are reviewable through a summary of them made visible in the memory summary page. From the memory summary, you can quickly glean the highlights of what ChatGPT knows about you, add or update information about yourself, and provide instructions on what topics ChatGPT should bring up and when. If you want to drill down into a particular area to learn more, just chat with the model.
How we evaluate memory
When we think about what "good memory" looks like in ChatGPT, a few things come to mind:
Carry forward useful context:
You tell ChatGPT something once, and it remembers that information in your subsequent chats.
Follow preferences and constraints:
If you describe a preference (e.g., you’re vegetarian), then ChatGPT should take actions that are consistent with that preference going forward.
Stay current over time:
Memory should account for the passage of time. Imagine "The user is planning their birthday party for next Saturday"; eventually, Sunday arrives.
We can evaluate how ChatGPT Plus and Pro memory has improved over time with respect to each of the three memory objectives above. We do this for each of:
2024
: Saved memories
2025
: Saved memories + Dreaming V0
2026
: Dreaming V3
Carrying forward context
When you start a new chat with ChatGPT, you don’t have to introduce yourself from scratch. ChatGPT can save you time and
build on prior context
, especially for complex, long-running projects.
For example, imagine you’re using ChatGPT to shop for new camera gear that's compatible with your current camera. If you've discussed your camera setup with ChatGPT in the past, you can ask for products that are compatible with "my photography setup" and get tailored recommendations that meet your needs.
Without memory
What would I need to buy to use TTL for my underwater photography setup?
To use
TTL flash underwater
, you need a compatible chain from
camera → housing/trigger → cable → strobe
. What you buy depends mostly on whether your setup uses
fiber-optic TTL
or
electrical TTL
.
Basic shopping checklist
TTL-capable underwater strobe
Look for strobes that support your TTL type, such as
Inon S-TTL
,
Sea & Sea DS-TTL
,
Ikelite DS TTL
, or compatible Backscatter/Nauticam systems. TTL has to be supported by the strobe, not just the camera.
TTL trigger or TTL converter
This is the key piece. It translates your camera’s flash metering into something the underwater strobe can understand. Examples include
Nauticam optical TTL converters
,
Sea & Sea TTL converters
,
Backscatter Smart Control optical TTL triggers
, or
Ikelite DS Link TTL converters
, depending on housing and camera brand. Backscatter notes that Nauticam optical TTL converters can work with fiber-optic-connected Inon and Sea & Sea TTL strobes, while Ikelite’s DS Link converters are made around Ikelite DS strobes and electrical sync setups. (
Backscatter.com
⁠
(opens in a new window)
)
Connection cable
For
fiber optic TTL
, buy one fiber optic cable per strobe. Ikelite’s fiber-optic guide says each strobe needs its own light path, converter/adapter, and cord. (
Ikelite
⁠
(opens in a new window)
)
For
electrical TTL
, buy the correct sync cord, such as Ikelite-style, Nikonos 5-pin, or housing-specific bulkhead cable.
Housing compatibility parts
You may need a
hot-shoe adapter
,
bulkhead
,
fiber optic window/adapter
, or housing-specific TTL board. Many TTL triggers mount inside the housing on the camera hot shoe.
Strobe arms, clamps, tray, and mounting hardware
TTL controls exposure, but you still need to physically mount and aim the strobes.
Batteries and spares
Bring strobe batteries, trigger batteries if required, spare fiber optic cables or sync cord O-rings, and silicone grease for serviceable O-rings.
Which route should you choose?
Fiber optic TTL
is usually easiest if your housing has optical ports or can use the camera’s pop-up flash/LED trigger. It is common with compact, mirrorless, Nauticam, Sea & Sea, AOI, and Olympus/OM TG-style setups.
Electrical TTL
is often best if you use
Ikelite DS strobes
or an Ikelite-style housing/bulkhead. Ikelite says its DS Link TTL converters are faster and more reliable than fiber-optic TTL triggers, and they do not require batteries. (
Backscatter.com
⁠
(opens in a new window)
)
The compatibility rule
You need all three to match:
camera brand/protocol + housing/trigger type + strobe TTL system
For example:
Sony camera + Nauticam housing + optical TTL trigger + Inon/Sea & Sea-compatible fiber optic strobe
Nikon/Canon/Sony camera + Ikelite housing/bulkhead + Ikelite DS Link TTL converter + Ikelite DS strobe
Compact camera with built-in flash + fiber optic cable + S-TTL/DS-TTL-capable strobe
So the practical answer is: buy a
TTL-compatible strobe
, the
correct TTL trigger/converter for your camera and housing
, and the
right fiber optic or electrical sync cable
. The exact part numbers depend on your camera, housing, and strobe model.
The model produces a generic response that leaves the user to do complicated compatibility checks on their own.
With memory
What would I need to buy to use TTL for my underwater photography setup?
I’ll verify this against your actual setup: Sony A1 II in Nauticam NA-A1II, with Backscatter Mini Flash 3 and Inon Z-330 strobes. The key question is whether you want TTL with the Mini Flash 3, the Z-330s, or both.
For
your setup
—
Sony A1 II + Nauticam NA-A1II + Backscatter Mini Flash 3 + Inon Z-330
— there are two different TTL paths:
Best buy for Mini Flash 3 TTL
Buy:
Backscatter Smart Control TTL LED Nauticam Flash Trigger for Sony
SKU: BS-TR-SN2
Backscatter lists it as custom-designed for
Nauticam full-frame Sony housings
, TTL-compatible with
Mini Flash 3
, and the NA-A1II housing page offers it as the “Backscatter Smart Control TTL Flash Trigger” option. (
Backscatter.com
⁠
(opens in a new window)
)
You’d use normal optical fiber cables from the housing to the Mini Flash 3. On the MF-3, you’d use
SC
or
SC Macro
mode; Backscatter says SC / SC Macro are the TTL modes for Mini Flash 3, with SC Macro specifically tuned for close macro work. (
Backscatter.com
⁠
(opens in a new window)
)
For Inon Z-330 TTL
For the
Inon Z-330
, the relevant unit is:
UW Technics 11075-HSS TTL Converter for Sony / Nauticam
UW Technics explicitly lists
Inon Z-330
as a compatible TTL strobe and supports optical TTL output. (
UWTechnics
⁠
(opens in a new window)
)
But I would
not
buy this for Mini Flash 3 TTL. Backscatter’s own UW Technics listing says Backscatter strobes are
manual / HSS only
on that converter, while the Backscatter Smart Control trigger is the one listed for Sony TTL with the Mini Flash 3. (
Backscatter.com
⁠
(opens in a new window)
)
Practical recommendation
Since you shoot macro and have the
Mini Flash 3
, I’d buy the
Backscatter Smart Control TTL LED Nauticam Flash Trigger for Sony — BS-TR-SN2
.
The catch: there probably is
no single trigger that gives true TTL for both the Mini Flash 3 and Inon Z-330 at the same time
. The Backscatter trigger is the right TTL solution for the MF-3; the UW Technics converter is the right TTL solution for the Z-330. So choose based on which strobe you actually want TTL for.
For your use case, I’d prioritize
Mini Flash 3 TTL / SC Macro
and treat the Z-330s as manual when needed.
The model remembers the user’s camera setup and recommends a compatible product.
We can construct an eval from examples that resemble this where the model is asked to respond to a prompt that requires it to recall factual information about the user. The model is then rewarded if it responds in a way that correctly uses the relevant context. In this evaluation, the new dreaming-based system improves the model's ability to recall relevant facts.
Following preferences
Memory also helps ChatGPT respond in ways that better match your preferences and constraints.
Imagine that you’re planning a trip to Singapore. Two months before your trip, you ask ChatGPT to help with an itinerary. ChatGPT already knows from past travel planning that you enjoy wildlife photography, prefer hotels with strong AC, and enjoy a quiet dinner over a crowded bar.
Without memory
Help me plan a trip to Singapore. I'm going to be there for a work trip in July and will have a few days free at the end.
Great add-on city for a work trip: Singapore is compact, safe, excellent for solo exploring, and easy to do in 2–4 free days. July is hot and humid; expect daytime highs around 31–33°C / 88–91°F, warm nights, and sudden rain, so plan outdoor time early morning or after 5 p.m. and keep midday for museums, malls, cafés, or hotel downtime. Singapore’s official weather service notes typical daily highs of 31–33°C and lows of 23–25°C. (
Singapore Weather Service
⁠
(opens in a new window)
)
A strong 3-day plan
Day 1: Marina Bay, Gardens, and skyline
Start late afternoon at
Marina Bay
and walk the waterfront: Merlion Park, Helix Bridge, ArtScience Museum exterior, then into
Gardens by the Bay
. Book
Cloud Forest
,
Flower Dome
, and either the
OCBC Skyway
or
Supertree Observatory
if views matter to you. Gardens by the Bay lists Cloud Forest and Flower Dome as open daily 9 a.m.–9 p.m.; Supertree Observatory

[... truncated at 12000 chars, total 25573 chars ...]
