---
title: "HIPAA compliant AI"
url: "https://www.johndcook.com/blog/2026/04/05/hipaa-compliant-ai/"
fetched_at: 2026-05-01T07:02:10.441720+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# HIPAA compliant AI

Source: https://www.johndcook.com/blog/2026/04/05/hipaa-compliant-ai/

The best way to run AI and remain HIPAA compliant is to run it locally on your own hardware, instead of transferring protected health information (PHI) to a remote server by using a cloud-hosted service like ChatGPT or Claude. [1].
There are HIPAA-compliant cloud options, but they’re both restrictive and expensive. Even enterprise options are not “HIPAA compliant” out of the box. Instead, they are “HIPAA eligible” or that they “support HIPAA compliance,” because you still need the right Business Associate Agreement (BAA), configuration, logging, access controls, and internal process around it, and the end product often ends up far less capable than a frontier model. The least expensive and therefore most accessible services do not even allow this as an option.
Specific examples:
Only sales-managed ChatGPT Enterprise or Edu customers are eligible for a BAA, and OpenAI explicitly says it does not offer a BAA for ChatGPT Business. The consumer ChatGPT Health product says HIPAA and BAAs do not apply. ChatGPT for Healthcare pricing is based on ChatGPT Enterprise, depends on organization size and deployment needs, and requires contacting sales. Even within Enterprise, OpenAI’s Regulated Workspace
spec
lists Codex and the multi-step Agent feature as “Non-Included Functionality,” i.e. off limits for PHI.
Google says Gemini can support HIPAA workloads in Workspace, but NotebookLM is not covered by Google’s BAA, and Gemini in Chrome is automatically blocked for BAA customers. If a work or school account does not have enterprise-grade data protections, chats in the Gemini app may be reviewed by humans and used to improve Google’s products.
GitHub Copilot, despite being a Microsoft product, is not under Microsoft’s BAA. Azure OpenAI Service is, but only for text endpoints. While Microsoft is working on their own models, it is unlikely that they will deviate significantly here.
Anthropic says its BAA covers only certain “HIPAA-ready” services, namely the first-party API and a HIPAA-ready Enterprise plan, and does not cover Claude Free, Pro, Max, Team, Workbench, Console, Cowork, or Claude for Office. The HIPAA-ready Enterprise offering is sales-assisted only. Bundled Claude Code seats are not covered. AWS Bedrock API calls can work, but this requires extensive configuration and carries its own complexities and restrictions.
Running AI locally is already practical as of early 2026. Open-weight models that approach the quality of commercial coding assistants run on consumer hardware. A single high-end GPU or a recent Mac with enough unified memory can run a 70B-parameter model at a reasonable token speed.
There’s an interesting interplay between economies of scale and diseconomies of scale. Cloud providers can run a data center at a lower cost per server than a small company can. That’s the economies of scale. But running HIPAA-compliant computing in the cloud, particularly with AI providers, incurs a large direct costs and indirect bureaucratic costs. That’s the diseconomies of scale. Smaller companies may benefit more from local AI than larger companies if they need to be HIPAA-compliant.
Related posts
[1] This post is not legal advice. My clients are often lawyers, but I’m not a lawyer.
