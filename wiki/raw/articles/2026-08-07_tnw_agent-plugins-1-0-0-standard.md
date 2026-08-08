---
title: "OpenAI and four rivals just agreed on one standard for AI agents"
url: "https://thenextweb.com/news/openai-agent-plugins-open-standard-skills-mcp"
date: "2026-08-06"
source: "The Next Web"
topics: ["agent-plugins", "agent-standards", "mcp", "openai", "vercel", "aws", "google", "microsoft"]
type: raw_article
---

# Agent Plugins 1.0.0: Industry Standard for AI Agent Interoperability

## Extracted Content

Credit: Canva document.getElementsByClassName('tnw-ad-wrapper')[1]?.classList?.add('ad-wrapper__growth-quarters'); The AI race spent two years being about models. This week it moved to the plumbing. On the eve of GPT-5’s first birthday, OpenAI and four rivals published Agent Plugins , an open standard that lets a single agent extension work across competing products. The pitch is “build once, run anywhere”. Today, every agent tool expects a different folder layout and setup. Agent Plugins replaces that with one package format. It bundles two things developers already use. The first is Model Context Protocol servers , which connect an agent to live tools and data. The second is Agent Skills, reusable sets of instructions. A plugin is just a folder with a small plugin.json file at its root. Who is behind it Despite the OpenAI billing, this is not an OpenAI product. Vercel initiated the proposal . Representatives from Amazon, Cursor’s maker Anysphere, GitHub, Microsoft, OpenAI, and Vercel then shaped the 1.0 specification. The steering committee has five members: Amazon, Cursor, Microsoft, OpenAI, and Vercel. The project is openly licensed, and its backers say no single company’s roadmap sets its direction. OpenAI still framed the launch as its own milestone. GPT-5 turns one on 7 August, and the company is marking the week by looking beyond individual models , per 9to5Mac. Its ChatGPT and Codex apps support the format at launch, alongside Cursor, GitHub Copilot, Kiro, and VS Code. The move goes further than OpenAI’s own Codex plugins , which work only inside its tools. Deliberately small The standard is narrow on purpose. It defines how a plugin is packaged and found, and little else. Marketplaces, installation, permissions, sandboxing, and trust all stay with each client. That keeps the format easy to adopt. It also leaves the hardest problems unsolved. Deciding whether a plugin is safe to run is still every client’s own job, a live worry after fake Agent Skills slipped past security scanners earlier this year. Not everyone is convinced. Dax Raad, who builds the SST developer-tools framework, said he was “very much against” it, calling it “a thin standard” whose useful parts will end up in client-specific extensions anyway. Others cheered. “We neeeeded this,” wrote developer advocate Angie Jones, who had wanted one way to carry her skills between the tools she uses. The bigger question is what standardising the plumbing does to competition. A shared format could let a small developer reach every major agent at once. That is the open-ecosystem case, and it is a real one. It could also cement the handful of clients that already have the users, because a standard rewards whoever people already run. For now the plumbing is agreed. The fight over the parts it leaves out, the marketplaces and the trust, has barely started. Story by Ana Maria Constantin With expertise in digital marketing, product management, and branding &amp; identity, Ana Maria Constantin develops strategies that resonate (show all) With expertise in digital marketing, product management, and branding & identity, Ana Maria Constantin develops strategies that resonate with our target audience in the software/SaaS industry. Collaboration and teamwork are paramount to her, as she loves empowering her colleagues to achieve outstanding results and unlock their full potential. Get the TNW newsletter Get the most important tech news in your inbox each week. Published August 6, 2026 - 6:00 pm UTC Back to top Story by Ana Maria Constantin Popular articles 1 Google built an AI translator that runs entirely offline on a Raspberry Pi 2 Gravity raised $30.5M to place ads inside AI chatbots. Its next product targets the bots themselves. 3 His AI fund lost 67% in a month. Thousands still copy his trades 4 OpenAI removes the daily limit on free ChatGPT chats and upgrades the default model to GPT-5.6 Luna 5 Adobe just put more than 70 of its tools inside ChatGPT

## Context from X/Twitter

- Vercel said it started the proposal
- AWS said it was a founding member
- Google said it was joining as a sixth
- Microsoft wrote the ecosystem framing
- OpenAI posted on X
- agent-plugins.org went live with a specification numbered 1.0.0

Agent Plugins is a portable package format for reusable agent components. It sits alongside MCP (Model Context Protocol) but focuses on the plugin/skill level rather than context access. The standard aims to create an interoperable ecosystem where agent skills and tools can be shared across platforms.

## Relevance

This is a major industry alignment moment — the first time five major AI infrastructure companies (OpenAI, Google, Microsoft, AWS, Vercel) have agreed on a common standard for agent components. This is distinct from MCP (which standardizes context access) and A2A (which standardizes agent-to-agent communication).
