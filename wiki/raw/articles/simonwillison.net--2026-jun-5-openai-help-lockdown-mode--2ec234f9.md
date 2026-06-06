---
title: "OpenAI Help: Lockdown Mode"
url: "https://simonwillison.net/2026/Jun/5/openai-help-lockdown-mode/#atom-everything"
fetched_at: 2026-06-06T07:01:18.729361+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# OpenAI Help: Lockdown Mode

Source: https://simonwillison.net/2026/Jun/5/openai-help-lockdown-mode/#atom-everything

5th June 2026 - Link Blog
OpenAI Help: Lockdown Mode
. OpenAI first teased this
in February
, but now it's live and "rolling out to eligible personal accounts, including Free, Go, Plus, and Pro, and self-serve ChatGPT Business accounts":
Lockdown Mode is designed to help prevent the final stage of data exfiltration from a prompt injection attack by limiting outbound network requests that could transfer sensitive data to an attacker. Lockdown Mode does not prevent prompt injections from appearing in the content ChatGPT processes. For example, a prompt injection could appear in cached web content or in an uploaded file, and could still affect the behavior or accuracy of a response.
This looks really good to me.
The
Lethal Trifecta
occurs when an LLM system has access to all three of access to private data, exposure to untrusted content and a way to steal data and transmit it back to the attacker.
The only way to solve the trifecta is to cut off one of the three legs, and by far the easiest leg to restrict without making your LLM systems far less useful is the exfiltration vectors to steal data.
It looks to me like lockdown mode directly attacks that leg, using mechanisms that are deterministic and, crucially, are not evaluated by AI systems that themselves can be subverted by sufficiently devious attacks.
The existence of lockdown mode does however imply that ChatGPT, in its default settings, does
not
provide robust protection against sufficiently determined data exfiltration attacks!
