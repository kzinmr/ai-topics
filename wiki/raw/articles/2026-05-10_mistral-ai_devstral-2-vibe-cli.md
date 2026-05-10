---
title: "Introducing: Devstral 2 and Mistral Vibe CLI."
source: "Mistral AI Blog"
url: "https://mistral.ai/news/devstral-2-vibe-cli"
scraped: "2026-05-10T01:20:59.107455+00:00"
lastmod: "2025-12-17T13:58:38.039Z"
type: "sitemap"
---

# Introducing: Devstral 2 and Mistral Vibe CLI.

**Source**: [https://mistral.ai/news/devstral-2-vibe-cli](https://mistral.ai/news/devstral-2-vibe-cli)

[ESC] Exit Terminal
██████████████████
██████████████████
████
██
██████
██
████
████
████
██
████
████
████
██████████
████
████
██
██
██
██
██
████
██
██████
██
██████
██
██████████████████
██████████████████
Devstral2
Mistral Vibe CLI
State-of-the-art, open-source agentic coding models and CLI agent.
curl -LsSf
h
t
t
p
s
:
/
/
m
i
s
t
r
a
l
.
a
i
/
v
i
b
e
/
i
n
s
t
a
l
l
.
s
h
| bash
Copy to clipboard
Copied to clipboard!
█░ Date:
Dec 9, 2025
█░ Category:
Research
█░ Author:
Mistral AI
Content
Today, we're releasing Devstral 2—our next-generation coding model family available in two sizes: Devstral 2 (123B) and Devstral Small 2 (24B). Devstral 2 ships under a modified MIT license, while Devstral Small 2 uses Apache 2.0. Both are open-source and permissively licensed to accelerate distributed intelligence.
Devstral 2 is currently free to use via
our API
.
We are also introducing Mistral Vibe, a native CLI built for Devstral that enables end-to-end code automation.
Highlights.
Devstral 2: SOTA open model for code agents with a fraction of the parameters of its competitors and achieving 72.2% on SWE-bench Verified.
Up to 7x more cost-efficient than Claude Sonnet at real-world tasks.
Mistral Vibe CLI: Native, open-source agent in your terminal solving software engineering tasks autonomously.
Devstral Small 2: 24B parameter model available via API or deployable locally on consumer hardware.
Compatible with on-prem deployment and custom fine-tuning.
Devstral: the next generation of SOTA coding.
Devstral 2 is a 123B-parameter dense transformer supporting a 256K context window. It reaches 72.2% on SWE-bench Verified—establishing it as one of the best open-weight models while remaining highly cost efficient. Released under a modified MIT license, Devstral sets the open state-of-the-art for code agents.
Devstral Small 2 scores 68.0% on SWE-bench Verified, and places firmly among models up to five times its size while being capable of running locally on consumer hardware.
Devstral 2 (123B) and Devstral Small 2 (24B) are 5x and 28x smaller than DeepSeek V3.2, and 8x and 41x smaller than Kimi K2—proving that compact models can match or exceed the performance of much larger competitors. Their reduced size makes deployment practical on limited hardware, lowering barriers for developers, small businesses, and hobbyists.hardware.
Built for production-grade workflows.
Devstral 2 supports exploring codebases and orchestrating changes across multiple files while maintaining architecture-level context. It tracks framework dependencies, detects failures, and retries with corrections—solving challenges like bug fixing and modernizing legacy systems.
The model can be fine-tuned to prioritize specific languages or optimize for large enterprise codebases.
We evaluated Devstral 2 against DeepSeek V3.2 and Claude Sonnet 4.5 using human evaluations conducted by an independent annotation provider, with tasks scaffolded through Cline. Devstral 2 shows a clear advantage over DeepSeek V3.2, with a 42.8% win rate versus 28.6% loss rate. However, Claude Sonnet 4.5 remains significantly preferred, indicating a gap with closed-source models persists.
“Devstral 2 is at the frontier of open-source coding models. In Cline, it delivers a tool-calling success rate on par with the best closed models; it's a remarkably smooth driver. This is a massive contribution to the open-source ecosystem.” — Cline.
“Devstral 2 was one of our most successful stealth launches yet, surpassing 17B tokens in the first 24 hours. Mistral AI is moving at Kilo Speed with a cost-efficient model that truly works at scale.” — Kilo Code.
Devstral Small 2, a 24B-parameter model with the same 256K context window and released under Apache 2.0, brings these capabilities to a compact, locally deployable form. Its size enables fast inference, tight feedback loops, and easy customization—with fully private, on-device runtime. It also supports image inputs, and can power multimodal agents.
Mistral Vibe CLI.
Mistral Vibe CLI is an open-source command-line coding assistant powered by Devstral. It explores, modifies, and executes changes across your codebase using natural language—in your terminal or integrated into your preferred IDE via the Agent Communication Protocol. It is released under the Apache 2.0 license.
Vibe CLI provides an interactive chat interface with tools for file manipulation, code searching, version control, and command execution. Key features:
Project-aware context: Automatically scans your file structure and Git status to provide relevant context
Smart references: Reference files with @ autocomplete, execute shell commands with !, and use slash commands for configuration changes
Multi-file orchestration: Understands your entire codebase—not just the file you're editing—enabling architecture-level reasoning that can halve your PR cycle time
Persistent history, autocompletion, and customizable themes.
You can run Vibe CLI programmatically for scripting, toggle auto-approval for tool execution, configure local models and providers through a simple config.toml, and control tool permissions to match your workflow.
Get started.
Devstral 2 is currently offered free via
our API
. After the free period, the API pricing will be $0.40/$2.00 per million tokens (input/output) for Devstral 2 and $0.10/$0.30 for Devstral Small 2.
We’ve partnered with leading, open agent tools
Kilo Code
and
Cline
to bring Devstral 2 to where you already build.
Mistral Vibe CLI is available as an extension in
Zed
, so you can use it directly inside your IDE.
Recommended deployment for Devstral.
Devstral 2 is optimized for data center GPUs and requires a minimum of 4 H100-class GPUs for deployment. You can try it today on
build.nvidia.com
. Devstral Small 2 is built for single-GPU operation and runs across a broad range of NVIDIA systems, including DGX Spark and GeForce RTX. NVIDIA NIM support will be available soon.
Devstral Small runs on consumer-grade GPUs as well as CPU-only configurations with no dedicated GPU required.
For optimal performance, we recommend a temperature of 0.2 and following the best practices defined for
Mistral Vibe CLI
.
Contact us.
We’re excited to see what you will build with Devstral 2, Devstral Small 2, and Vibe CLI!
Share your projects, questions, or discoveries with us on
X/Twitter
,
Discord
, or
GitHub
.
We’re hiring!
If you’re interested in shaping open-source research and building world-class interfaces that bring truly open, frontier AI to users, we welcome you to
apply to join our team
.
Share and more
□ Linkedin
□ Facebook
□ X
□
News
□
Models
□
Services
The next chapter of AI is yours.
Try le Chat
Build on AI Studio
Talk to an expert
