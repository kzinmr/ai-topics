---
title: "Meta Muse Spark Open is live on Together AI"
url: "https://www.together.ai/blog/meta-muse-spark-open"
fetched_at: 2026-10-16T10:00:37.186628+00:00
source: "Together AI Blog"
tags: [blog, raw]
---

# Meta Muse Spark Open is live on Together AI

Source: https://www.together.ai/blog/meta-muse-spark-open

Meta's Muse Spark Open is available on Together AI today. We're a Day 0 launch partner for the most capable US open-weight model to date, built for long-running agentic coding workflows that keep entire codebases in context.
Muse Spark Open is a step forward for agentic software engineering, computer use and web automation, and understanding documents, images, audio, and video together. Through our early access program, we offered it to select customers before launch. They evaluated it, prepared to offer it to their own customers on day 0, and shared real-world feedback with Meta.
Read Meta's announcement
.
About Muse Spark Open
Muse Spark Open is trained on real developer work: multi-file refactors, debugging sessions, and long-running tasks. The result is higher first-attempt accuracy, reliable tool calling, and deep codebase understanding across the repositories developers actually work in.
What stands out:
1M-token context window.
It holds entire projects, including complex dependencies, legacy code, and thousands of files, without splitting work into pieces.
Long-horizon autonomy.
It plans, acts, observes, and self-corrects over long horizons, and coordinates subagents for work that can be split up.
Computer use and browsing.
It uses computer-use capabilities across desktop, mobile, and browser, and browses the web with multimodal browsing.
Multimodal input.
It accepts text, image, audio, and audio-video input.
Intent commentary.
It states what it is doing and why before acting, which makes long runs easier to audit.
What early access customers said
Factory and Ollama were two customers with early access. Both used Muse Spark Open before launch, and both offer it to their users from day 0.
"Enterprises choose Factory because they want their Droids running on the best model for the task. In our agentic engineering workflows, Muse Spark Open consistently selected the right tool and kept its responses compact, exactly the decisiveness production agents need. Early access through Together AI let us stress-test it ahead of launch, so our customers get access on day 0."
Zimu Li, Member of technical staff, Factory
"Millions of developers across the globe rely on Ollama as the destination to get up and running with open source models. We are delighted to offer Muse Spark Open in partnership with Together AI. This model performs particularly well on tool calling and long context, including multi-step and parallel calls with clean structured outputs.
Partnering with Together AI for early access allowed us to sufficiently evaluate and optimize the model so that developers experienced a fully supported, production-ready model from the moment it launched."
Dong Chen, Senior AI Engineer, Ollama
Run it on Together AI
Serverless.
Call Muse Spark Open with the Together API:
from together import Together

client = Together()

response = client.chat.completions.create(
    model="meta-models/Muse-Spark-Open-816B-A42B",
    messages=[{"role": "user", "content": "Refactor this module to remove the circular import."}],
)
print(response.choices[0].message.content)
Pricing is $1.25 per 1M input tokens, $4.25 per 1M output tokens, and $0.15 per 1M cached input tokens. You can also try it in the playground.
Get started
or
‍
Talk to an engineer
‍
