---
title: "Appraisal by AI: Model-driven victim prioritization in the VOLTA infostealer (Cisco Talos)"
url: "https://blog.talosintelligence.com/appraisal-by-ai-model-driven-victim-prioritization-in-the-volta-infostealer/"
date: "2026-10-31"
fetched_at: "2026-11-01T11:10:00+00:00"
source: "blog.talosintelligence.com"
tags: [blog, raw]
---

# Appraisal by AI: Model-driven victim prioritization in the VOLTA infostealer (Cisco Talos)

Source: https://blog.talosintelligence.com/appraisal-by-ai-model-driven-victim-prioritization-in-the-volta-infostealer/

Appraisal by AI: Model-driven victim prioritization in the VOLTA infostealer

VOLTA is a mature stealer implant with an optional AI-integration layer. After stealing credentials, sessions, and cryptocurrency wallets, VOLTA sends a structured evidence bundle to an LLM to rank the victim’s assets by monetization value.

If a model refuses to perform the target assessment, VOLTA fails over to a three-model chain, implying a direct engineering effort and expectation of hitting model guardrails.

This stealer is self-deleting, and there is no attacker-owned infrastructure. The novelty in the AI-integration is that it is not supporting a traditional malware capability but working as an intelligence analyst on behalf of the operator.

There is a new idea in the cybercrime world — cast a wide net, steal everything, and let AI sort out the specifics. A new malware self-named “VOLTA-AUTODOXER,” surfaced through the CAIRN research effort, is a self-deleting Windows infostealer that augments its post-theft workflow with an LLM-powered victim-profiling stage.

After harvesting the standard stealer haul, including browser passwords; cookies; payment cards; cryptocurrency wallet seed phrases; Discord, Telegram, Steam, and Roblox sessions; Microsoft OAuth tokens; SSH and cloud-provider keys; Wi-Fi profiles; and screenshots, VOLTA builds a structured evidence bundle about the person behind the machine. This bundle contains geolocation and home address, employer and employer domain, inferred birth year, card last-4 digits, Slack workspaces, document authorship metadata, iPhone backup indicators, and a live Roblox account valuation. It then uses stolen session access to enrich that bundle further: searching the victim's Gmail for purchase receipts to corroborate a home address, pulling UberEats and DoorDash order history, and enriching Discord accounts via the stolen token.

The bundle is serialized and POSTed to OpenRouter under a system prompt that instructs the model to act as "a forensic intelligence analyst drafting a target assessment." The required output includes a section titled “WHAT THEY'RE WORTH” with valuables ranked by monetization with a low/medium/high tier, and a section on “THEIR OPSEC” containing an assessment of the victim's security posture and password hygiene. The model is the operator's triage analyst; it turns a raw credential log into a prioritized and citation-backed dossier of the victim and their monetizable assets.

The AI configuration: “Go deep, not wide... Be blunt, specific, accurate.”

VOLTA uses a multi-model architecture to fall back resiliently if it hits a model’s refusal, checking each response for phrases like “I can’t” or “I’m not able,” before passing on to a chain of up to three models.

Endpoint

https[:]//openrouter[.]ai/api/v1/chat/completions

Default model

anthropic/claude-opus-4.6

Fallback chain

moonshotai/kimi-k2 → google/gemini-2.5-flash

Temperature

0.2 — deterministic, consistent output

Request format

Hand-assembled JSON; no SDK; User-Agent Mozilla/5.0

Model temperate controls the randomness and predictability of LLM-generated text. The low hardcoded temperature value (0.2) suggests the attacker is emphasizing accuracy and consistency. The malware also employs a chain of cascading models in the event of failures. This multi-model architecture suggests that the operator is anticipating encountering refusals, with the fallback pivoting to a few, smaller, and more permissive models.

The system prompt directly reveals the operator’s use case: Produce a concise analytical assessment of the victim’s suitability as a target, backed by an auditable trail of citations.

The prompt also asks for something out of the ordinary, but that agents excel at: making connections between sparse and disparate data. For example, encouraging connections like the victim’s names, addresses, or universities to patterns in their passwords. In this case, the model isn't being asked to find data; rather, it’s being asked to stretch the data and make useful inferences that extend the value of what has been scraped.

Stealer capabilities

VOLTA’s capabilities are directly aligned with the records produced in modern digital life, and well beyond basic credential theft. In a single pass, the stealer can extract browser credentials, cookies, and saved payment cards across Chromium-based browsers. It hits Firefox and Thunderbird, Outlook profiles, Slack workspaces, Steam and Battle.net sessions, Discord tokens, Telegram sessions, Roblox accounts, and SSH and cloud-provider config files (gcloud, OpenVPN, Hide.me). VOLTA doesn’t just copy cryptocurrency wallets, but runs an embedded cracker against the vault inline, writing the result to a WALLET VAULTS CRACKED line in its own report.

Every saved Wi-Fi password on the machine is pulled via a direct call to WlanGetProfileList and dumped to plaintext.

What really sets VOLTA apart from commodity stealers is what comes after the initial collection. There is a live enrichment pass that leverages stolen sessions to deep dive the victim’s data. For example, using the victim's own authenticated Gmail tokens, it queries their inbox for receipts from Amazon, DoorDash, Uber Eats, Grubhub, Walmart, and PayPal, then review those receipts to establish a confirmed home address. Stolen Uber Eats and DoorDash sessions are called directly for order history. The Discord token is re-used to enrich the victim's account profile. Roblox inventory is valued via a live “Rolimons[.]com” lookup.

After the collection and enrichment stages are complete, the data is assembled and structured locally in a file called “Identity_Report.txt”. This file is serialized into a bundle as JSON and POSTed to OpenRouter along with the system prompt. The returned payload is received as “AI_Analysis.txt”. Both files exfil together in “volta_dox.zip”.

The inference round-trip happens entirely through the victim's own network connection, on their own machine, before the result is exfiltrated.

Deployment model

Instead of hardcoding its Telegram channel, API keys, and settings directly into the code (which is likely what someone writing a tool for personal use would do) VOLTA uses a template with six swappable slots, filled in at build time.

This suggests it’s a builder model: The author sells access, the customer provides their values, and the builder compiles a custom binary for each order. The credentials in those slots are encrypted, but not in a meaningful way. The key is SHA-256 of two constants sitting in the same binary, but it's presumably there because customers expect their API keys not to be sitting in plaintext, not because it provides real protection. Anyone who reverses the file can recover them.

If VOLTA is indeed a commoditized malware, then the AI dossier capability isn't something the author invented for their own operations. It is a feature which enables a customer of any level of sophistication to point it at victims and start receiving ranked target assessments in their Telegram inbox.

All the observed endpoints for this malware are third-party controlled. There is no actor-owned infrastructure.

Countermeasures

Much of the token-stealing capability of VOLTA relies on techniques to bypass App-Bound Encryption (ABE) in Chrome. An application control policy that restricts which processes may launch Chrome with --headless would block the ABE decryption path entirely. At minimum, you can also alert when Chrome is launched with --headless from any process not in a known developer. Best practices for storing credentials in hardware backed stores also apply.

In the event of compromise, the main executable may have deleted itself, but users should attempt to preserve the “APPDATA%\volta_debug.txt” file. This is a timestamped harvest log and contains a record of exactly what was collected and whether the LLM call succeeded. Revoke any potentially compromised tokens and change passwords. For cryptocurrency wallets, if the seed phrase was in plaintext on disk, treat the wallet as fully compromised and migrate funds to a new wallet with a seed generated on an air-gapped device.

Conclusions

VOLTA is a mature stealer with a late-stage AI layer added for one purpose: relieving the operator of analytical work. The axis of AI improvement here is not speed or scale but effort displacement; the same logic visible in CLOSEDQUORUM, though applied to a different phase. These implants reflect the same underlying logic: Identify the step that requires the most sustained human attention and replace it with a model call. The question for defenders is not whether this pattern will appear elsewhere, but which phase it touches next.

The second trend to watch is the anticipation of hitting model refusals, and the approaches to building in resiliency. In this case, it includes a fallback chain from Claude to Kimi to Gemini and the ability to run without the LLM stage altogether if no key is present. As AI integration in malware matures, refusal resilience may become a standard design requirement.

The open question underlying both trends is whether effort displacement in crimeware changes the landscape in a meaningful way: lowering the operational floor, raising the ceiling on scale, or both. Cybercrime operations have always been opportunistic, and the sophistication bar has always been lower than assumed, but there is a difference between a wide net and a wide net that sorts itself.

Sample details

SHA256

57ef4242666d78c50df145b34023df564f0fad38812d6a580e66433d427e2279

Filename

9BY0tjwOc3ut.exe / yLP9m5J3i2Aw.exe

Type

PE32+ x86-64

PE Timestamp

2026-08-17 20:35

First Seen (UTC)

2026-10-11 12:46