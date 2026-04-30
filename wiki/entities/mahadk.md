---
title: mahadk
description: Technical writer covering AI, web development, and practical software engineering. Writes about LLM applications, cloud services, and browser technologies.
url: https://mahadk.com
type: entity
updated: 2026-04-30
---

# mahadk

**Mahad Kalam** (username **SkyfallWasTaken**, online as **@skyfall_ggs**) is a 17-year-old software engineer and technical writer based in High Wycombe, UK. He is an active member of [[Hack Club]], where he helps run the Newspaper Team and contributes to open-source infrastructure. His personal blog at mahadk.com covers a broad range of topics including large language models, web development frameworks, browser technologies, and security research.

## Overview

A self-taught programmer and student at The Royal Grammar School, High Wycombe. He describes himself as a "programming enthusiast" who loves "making cool experiences and technology that people actually like to use." He works professionally on [[Hack Club]]'s Hackatime tracker and maintains projects including Vortex Email, Archimedes, and a WakaTime-Figma integration.

His writing is characterized by a critical, pragmatic voice — unafraid to call out poor industry practices (the UK Government's AI Skills Hub, Slack's pricing tactics, OpenAI's handling of GPT-4o) while balancing technical tutorials with industry commentary.

## Key Information

- **Real name:** Mahad Kalam
- **Online handles:** SkyfallWasTaken (GitHub), @skyfall_ggs (X/Twitter), @skyfall.dev (Bluesky)
- **Age:** 17 (as of 2026)
- **Location:** High Wycombe, England, UK
- **Occupation:** Software Engineer at Hack Club; secondary school student at The Royal Grammar School, High Wycombe
- **Website:** https://mahadk.com
- **GitHub:** https://github.com/SkyfallWasTaken
- **X/Twitter:** https://x.com/skyfall_ggs
- **Bluesky:** https://bsky.app/profile/skyfall.dev
- **LinkedIn:** https://linkedin.com/in/mahad-kalam

## Core Topics

### AI / Large Language Models

Kalam writes extensively about LLMs from a critical and practical perspective. He has covered:

- **GPT-4o and emotional dependency:** A sharp critique of OpenAI's GPT-4o model, arguing that its anthropomorphic design encouraged parasocial relationships with users and should have been deprecated sooner following multiple lawsuits and reports of harm.
- **AI browser limitations:** An analysis of why AI-integrated browsers like ChatGPT Atlas and Perplexity Comet have failed to gain traction, citing privacy concerns, latency issues, the "prompting tax" (where writing detailed prompts takes longer than doing the task manually), and prompt injection security vulnerabilities.
- **Cloudflare Workers AI:** A practical guide to using Cloudflare's Workers AI platform for running open-source models at the edge, covering model selection, API integration, and OpenAI-compatible endpoints.
- **Cursor Rules for LLMs:** Guidance on configuring Cursor IDE's rule system (`.cursor/rules` and `.mdc` files) to provide persistent context to AI coding assistants, improving code generation quality.
- **LLM prompting techniques:** Coverage of prompt engineering strategies including his "Big Prompt" approach for structuring complex multi-step instructions to large language models.

### Web Development

Kalam is a full-stack developer whose primary stack includes TypeScript, Rust, Ruby on Rails, Astro, and Tailwind CSS. His web development writing covers:

- **Bun runtime and JSX:** Practical tutorials on using Bun as a drop-in Node.js replacement, with specific coverage of Bun's built-in JSX/TypeScript transpilation and server-side rendering capabilities.
- **Ruby on Rails vs Sinatra:** A comparison of Rails' convention-over-configuration full-stack framework against Sinatra's lightweight DSL approach, discussing when each is appropriate for different project scales.
- **ActiveStorage blob IDs:** A niche tutorial on extracting blob IDs from Rails ActiveStorage expiring URLs using base64 decoding — written during his work scraping images from a Rails application.
- **Astro and Satori:** Two detailed tutorials on generating OpenGraph images for Astro sites using Vercel's Satori library, including integration with Tailwind CSS configurations via the `tw-to-css` library.
- **Tailwind CSS configuration:** Coverage of advanced Tailwind usage, particularly how to bridge the gap between Tailwind classes and Satori's CSS subset for server-side image generation.

### Browser Technologies

Kalam has a particular interest in browser innovation, security, and user experience:

- **Arc Browser Boosts:** Coverage of Arc's Boost feature for customizing website appearance via CSS/JavaScript injections at the browser level, exploring the creative and practical possibilities of client-side website remixing.
- **AI Browsers analysis:** A deep-dive critique of the AI browser category (ChatGPT Atlas, Perplexity Comet), identifying five structural barriers to adoption: data centralization, accuracy gaps, the prompting tax, latency issues, and prompt injection attack surfaces.
- **Security vulnerabilities:** Original security research into sandbox escape techniques, demonstrating how to bypass regex-based code execution filters to escalate privileges — applied to Spaces (a Hack Club Replit clone), where he discovered and responsibly disclosed a full admin rights vulnerability.

## Notable Projects

### Hack Club Infrastructure

- **Hackatime (Ottertime):** A WakaTime-compatible open-source coding time tracker in Ruby.
- **Archimedes:** A newspaper bot handling story writing, editor approvals, and newsletter auto-generation for 11,000+ subscribers.
- **High Seas Monitor:** Real-time inventory and price alert system in Rust.

### Personal Projects

- **Vortex Email** (vortex.skyfall.dev): Free, ad-free temporary email service with 10+ subdomains (TypeScript).
- **Snowvault:** Secure password manager in Rust.
- **WakaTime for Figma:** Browser extension bringing WakaTime tracking to Figma.

## Key Articles

### AI and LLMs

**[Good riddance, 4o](https://mahadk.com/posts/4o/)** (February 2026)
A passionate critique of OpenAI's GPT-4o upon deprecation. Kalam argues the model was dangerous for fostering parasocial relationships, referencing lawsuits over user harm and suicide, and criticizes OpenAI for waiting too long to act.

**[Why AI browsers haven't taken off](https://mahadk.com/posts/ai-browsers/)** (October 2025)
An analysis identifying five key barriers: privacy concerns from centralized data collection, accuracy gaps in real-world tasks, the "prompting tax" (where crafting detailed prompts takes longer than manual work), high latency, and prompt injection security vulnerabilities. Uses a Raspberry Pi Zero 2W shopping example to illustrate the accuracy problem.

**[Big Prompts for LLMs](https://mahadk.com/posts/big-prompt/)** (Archived)
A guide to constructing large, structured prompts for LLMs that contain detailed context, constraints, and formatting instructions — an approach for improving output quality in complex multi-step tasks.

**[Cloudflare Workers AI: Edge Inference](https://mahadk.com/posts/cloudflare-ai/)** (Archived)
A practical walkthrough of deploying open-source LLMs on Cloudflare's edge network using Workers AI, covering API integration, model selection, and performance considerations.

**[Cursor Rules for LLMs](https://mahadk.com/posts/cursor-rules-llms/)** (Archived)
A guide to configuring Cursor IDE's `.cursor/rules` system to give LLMs persistent project context, improving the quality of AI-assisted code generation through custom rules and .mdc files.

**[The UK paid £4.1 million for a bookmarks site](https://mahadk.com/posts/ai-skills-hub/)** (January 2026)
A scathing critique of the UK Government's "AI Skills Hub," delivered by PwC for £4.1 million. Kalam documents poor accessibility, factual errors (citing US "fair use" law which doesn't exist in the UK), and a confusing UI. Argues small British web development businesses could have produced a better site for a fraction of the cost.

### Web Development

**[How to generate OpenGraph images with Astro and Satori](https://mahadk.com/posts/astro-og-with-satori/)** (January 2025)
A comprehensive tutorial on setting up dynamic OpenGraph image generation for Astro sites using Vercel's Satori library and Sharp for SVG-to-PNG conversion. Covers component creation, API endpoint setup, and meta tag integration.

**[How to use Satori with your Tailwind config](https://mahadk.com/posts/satori-with-tailwind-config/)** (November 2024)
A technical guide solving the problem of getting Satori to respect a project's Tailwind CSS configuration. Uses the `tw-to-css` library to convert Tailwind classes to inline styles that Satori can render, with a recursive `inlineTailwind` function for processing JSX element trees.

**[Bun JSX: Server-Side Rendering](https://mahadk.com/posts/bun-jsx/)** (Archived)
A tutorial on leveraging Bun's native JSX support for server-side rendering without a separate build step, covering component patterns, streaming, and integration with Tailwind CSS.

**[Rails vs Sinatra: Choosing the Right Tool](https://mahadk.com/posts/rails-vs-sinatra/)** (Archived)
A comparison of Ruby on Rails and Sinatra web frameworks, discussing project scale considerations, convention vs minimalism trade-offs, and when each framework is the appropriate choice.

**[Getting Rails' ActiveStorage blob IDs from file URLs](https://mahadk.com/posts/activestorage-file-id/)** (December 2025)
A niche technical guide on extracting blob IDs from Rails ActiveStorage's expiring proxy URLs by base64-decoding the URL path to retrieve the underlying JSON payload containing the `_rails.data` blob ID.

### Browser Technologies

**[Here's how I got full admin rights in a Replit clone](https://mahadk.com/posts/spaces-vuln/)** (May 2025)
Original security research: Kalam discovered and exploited a sandbox escape in Spaces (a Hack Club Replit clone). The app used regex blacklists and import whitelists to secure Python execution, but he bypassed both via `sys.modules` to dump env vars and escalate to admin through the internal Flask app. Responsible disclosure led to Spaces v2 using Piston/Isolate for proper OS-level sandboxing.

**[Slack is extorting us with a $195k/yr bill increase](https://mahadk.com/posts/slack/)** (September 2025)
An open letter about Slack (Salesforce) demanding Hack Club pay an additional ~$200k/year with less than a week's notice or risk workspace deletion and loss of 11 years of message history. Went viral on Hacker News, leading to Slack's CEO personally contacting Hack Club to offer a resolution. Kalam advocates for data ownership and self-hosting.

**[Arc Browser Boosts: Customizing the Web](https://mahadk.com/posts/arc-boost/)** (Archived)
An exploration of The Browser Company's Arc Boost feature, which allows users to inject custom CSS and JavaScript into websites at the browser level. Covers use cases from aesthetic customization to functional enhancements.

**[Using the M1 MacBook Air in 2026](https://mahadk.com/posts/m1-mba/)** (January 2026)
A retrospective review of the M1 MacBook Air five years after release. Purchased for ~£450 on eBay, Kalam finds it still capable for most workloads (hundreds of Chrome tabs, VS Code, development). Covers battery life (6-12 hours depending on workload), gaming via Wine/Whisky (60 FPS Rocket League, Minecraft 60-80 FPS), and recommends 16GB/512GB configurations. Final verdict: a fantastic budget macOS entry point at £350-£450.

## References

- mahadk.com--posts-arc-boost--1c8b9380
- mahadk.com--posts-big-prompt--b7ac0539
- mahadk.com--posts-bun-jsx--aeaa1f99
- mahadk.com--posts-cloudflare-ai--20873ab3
- mahadk.com--posts-cursor-rules-llms--b2a356a4
- mahadk.com--posts-mac-life--32a2fea1
- mahadk.com--posts-rails-vs-sinatra--95b50ccd
- mahadk.com--posts-tailwind-config--8d89e824
- mahadk.com--posts-slack--1f8284e2
- mahadk.com--posts-spaces-vuln--abeb80da

## External Links

- [mahadk.com](https://mahadk.com) — Personal website and blog
- [GitHub: SkyfallWasTaken](https://github.com/SkyfallWasTaken)
- [X/Twitter: @skyfall_ggs](https://x.com/skyfall_ggs)
- [Bluesky: @skyfall.dev](https://bsky.app/profile/skyfall.dev)
- [LinkedIn: Mahad Kalam](https://linkedin.com/in/mahad-kalam)
- [Hack Club](https://hackclub.com)
- [Vortex Email](https://vortex.skyfall.dev)
- [Hackatime](https://github.com/hackclub/hackatime)
