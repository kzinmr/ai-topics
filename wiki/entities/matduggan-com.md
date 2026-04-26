---
title: "Mat Duggan"
tags: [- person]
created: 2026-04-24
updated: 2026-04-24
---

# Mat Duggan

**URL:** https://matduggan.com
**Blog:** matduggan.com
**Tagline:** "It's JSON all the way down"
**Identity:** Mathew Duggan, American sysadmin/DevOps engineer based in Denmark
**Social:** Mastodon @matdevdug@c.im
**Themes:** DevOps, Kubernetes, cloud infrastructure, open source sustainability, AI's impact on software, tech industry analysis, personal technology choices
**Tech Stack:** Ghost CMS, custom Handlebars themes, Kubernetes, AWS, Linux

## Overview

Mat Duggan is an **American sysadmin and DevOps engineer living in Denmark** who writes about the practical realities of infrastructure, open source sustainability, the evolution of technology platforms, and the **macroeconomic forces shaping the tech industry**. His blog's tagline — "It's JSON all the way down" — reflects both his deep experience with configuration-heavy infrastructure and his wry awareness of the absurdity of modern DevOps.

Duggan's career spans **Windows repair in rural Ohio**, **school IT support in Chicago**, **enterprise AWS/Kubernetes operations**, and now **DevOps engineering in Denmark**. This unusual trajectory — from fixing Windows PCs in a small-town computer shop to managing container orchestration at scale — gives him a unique perspective on how technology and the industry have evolved over two decades.

His writing is characterized by:
- **Deep technical knowledge** — Kubernetes debugging, AWS EKS, Ghost CMS theming, network troubleshooting
- **Willingness to critique industry trends** — Google's shift toward closed-loop search, Broadcom's monetization of Bitnami, AI hype cycles
- **Personal, story-driven approach** — tech support stories, career reflections, life in Denmark
- **Practical, hands-on perspective** — writes code, runs infrastructure, debugs real problems

The blog covers a wide range of topics: DevOps tutorials, career advice, tech industry analysis, personal essays about life in Denmark, and practical guides (like writing custom Ghost themes). Duggan's willingness to write about both highly technical topics (kubectl debug, Koolkits, socket library networking) and deeply personal ones (climate change discussions over beers, career transitions, growing up in rural America) creates a blog that feels like a conversation with a knowledgeable, thoughtful colleague.

## Timeline

| Date | Event |
|------|-------|
| ~2000s | Early career: Windows repair at local computer shop in rural Ohio, CCNA certification in high school |
| 2010s | School IT support in Chicago (Mac administration, AppleScript automation), transition to Linux sysadmin work |
| ~2012-2013 | First exposure to Google's Borg container system; follows Kubernetes development |
| 2015-2019 | Enterprise DevOps work, AWS EKS adoption, infrastructure at scale |
| ~2020 | Moves to Denmark; begins blogging more regularly |
| 2021 | Writes about EKS vs. Docker Swarm migration experience; begins analyzing AI and tech trends |
| 2024 | "Tech Support Stories Part 2" — personal essays about career origins |
| 2024 | "What Does a Post-Google Internet Look Like" — analysis of search ecosystem changes |
| 2025 | "FYI: Broadcom is ruining Bitnami containers" — DevOps industry critique |
| 2025 | Publishes custom Ghost theme (minimal design with Mastodon integration) |
| 2026 | Continues writing on AI, Kubernetes, DevOps, and tech industry analysis |

## Core Ideas

### The Post-Google Internet: Search Is Becoming a Closed Loop

Duggan's most significant industry analysis is his prediction about Google's transformation:

> "Google has decided to abandon the previous concept of how internet search worked... OpenAI and its rise to fame seems to have forced Google's hand in this space."

He identifies the cycle:
1. Google's AI Overview takes the top 100 search results and synthesizes an answer
2. Content creators get less traffic from their existing content
3. The cost of producing content exceeds the benefit
4. Creators put content behind paywalls or stop publishing
5. Google's AI has less raw material to work with
6. The loop accelerates

His conclusion is stark:

> "Because we didn't regulate the internet, we're going to end up with an unbreakable monopoly on all human knowledge held by one company."

> "Welcome to the future, where asking a question costs $4.99 and you'll never be able to find out if the answer is right or not."

This analysis is notable for connecting **macroeconomic forces** (monopoly power, content economics) with **technical decisions** (LLM integration in search) and **social consequences** (paywalled knowledge).

### Broadcom's Monetization of Open Source Infrastructure

In "FYI: Broadcom is ruining Bitnami containers," Duggan provides a detailed analysis of how Broadcom's acquisition of VMware is affecting the broader DevOps ecosystem:

- Bitnami containers (widely used for quick deployment of open source software) are being moved to paid tiers
- Existing images are being moved to `docker.io/bitnamilegacy`
- Kubernetes Helm charts will break without image repository overrides
- Enterprise customers are being forced into paid tiers

The broader point: **open source infrastructure that companies depend on can be commoditized and monetized at any point by acquisition.** This is a warning to the DevOps community about supply chain risk.

### Kubernetes Debugging: Practical, Not Theoretical

Duggan's approach to Kubernetes troubleshooting is hands-on and pragmatic:

> "I regularly use the socket library for tons of networking troubleshooting and ensuring ports and other resources are not blocked by a VPC or other security policy."

He advocates for **ephemeral debug containers** (`kubectl debug`) with pre-built toolkits (Lightrun's Koolkits) rather than baking debugging tools into every container image. This is a specific, actionable recommendation that reflects real production experience.

His debugging workflow:
1. Attach a debug container to a running pod
2. Use Python's `socket.getaddrinfo()` for DNS lookups
3. Use `netmiko` for datacenter networking issues
4. Avoid baking tools into production images

### The Ghost CMS Experience: Building Your Own Theme

Duggan wrote a custom Ghost theme because the default themes were "completely cluttered with junk I don't need." His analysis of Ghost:

- **Good**: Fast, reliable, quick bug fixes from the Ghost team
- **Bad**: Newsletter-first design, most themes assume you want email capture
- **Solution**: Build your own minimal theme using Handlebars

He documents the template hierarchy (`index.hbs`, `post.hbs`, `page.hbs`, `tag.hbs`, `author.hbs`) and provides practical advice: start with the three required files, add specific templates as needed. The Mastodon share button was "the only part that was complex" — a testament to the simplicity of the rest.

### Tech Support Stories: The Human Side of Infrastructure

Duggan's "Tech Support Stories" series is a personal essay format that traces his career from:
- **Fixing Windows PCs** in a rural Ohio computer shop (learning "Troubleshooting Theory" from a Vietnam veteran radio operator)
- **High school CCNA certification** (in a poor agricultural town where "people in my life still made $8/hour")
- **Mac IT support** for Chicago schools (AppleScript automation for teachers)
- **Linux sysadmin work** (the transition from desktop support to infrastructure)

These stories are notable because they **demystify the path to senior engineering**. There's no CS degree, no FAANG internship — just curiosity, hands-on experience, and a willingness to learn from anyone who knows more than you.

### Climate Change and Programming: A Thought Experiment

In a uniquely philosophical post, Duggan and colleagues (a Dane, an American, and a Hungarian) discussed **what programming and software infrastructure will look like in 2050** under various climate scenarios:

> "They'll discuss being nervous or unsure about it. We should talk about it like we talk about nuclear weapons."

The discussion covers:
- Language popularity trends (Rust, Clojure, Go as likely winners)
- Open source sustainability (who maintains the infrastructure?)
- AI's role in future software development
- The impact of climate change on technical work

This is one of the most unusual posts in tech writing — a casual conversation over beers in a Danish park, treated as a serious intellectual exercise.

## Key Quotes

> "It's JSON all the way down."

> "Because we didn't regulate the internet, we're going to end up with an unbreakable monopoly on all human knowledge held by one company."

> "Welcome to the future, where asking a question costs $4.99 and you'll never be able to find out if the answer is right or not."

> "OpenAI and its rise to fame seems to have forced Google's hand in this space."

> "I grew up in a place that could serve as the laboratory calibration small town USA."

> "We should talk about it like we talk about nuclear weapons."

> "Every job I've ever had relies on a large collection of Open Source software, whose survival depends on a small number of programmers having the available free time to maintain and add features to them."

## Writing Style & Philosophy

Duggan writes with a **conversational, story-driven style** that blends technical depth with personal narrative. Characteristics:

- **Personal voice** — uses "I" freely, shares opinions and experiences
- **Technical specificity** — exact commands, specific tool versions, concrete examples
- **Industry critique** — willing to call out companies (Broadcom, Google) by name
- **Storytelling** — tech support stories, career narratives, casual conversations
- **Practical focus** — "here's what I did, here's what worked, here's what didn't"
- **Self-aware humor** — "It's JSON all the way down" as both a complaint and a badge of honor

His blog is built on **Ghost CMS** with a custom minimal Handlebars theme. He chose Ghost for speed and reliability, then customized it to remove newsletter features he didn't need. The blog supports RSS feeds and email subscriptions.

## Technical Breadth

- **DevOps**: Kubernetes, Docker, Helm charts, container orchestration
- **Cloud Infrastructure**: AWS EKS, VPC networking, cloud migration
- **Networking**: Socket library debugging, netmiko, DNS troubleshooting
- **CMS/Content**: Ghost, Handlebars themes, RSS, web publishing
- **Programming**: Python (networking, automation), AppleScript, shell scripting
- **Open Source**: Sustainability, maintenance burden, community dynamics
- **AI/LLMs**: Industry impact, search disruption, practical applications
- **Career**: Tech support, sysadmin path, DevOps transition, international work

## Recent Themes (2024–2026)

- **Google search disruption**: AI overviews creating a closed knowledge loop
- **Open source monetization**: Broadcom's Bitnami changes as a cautionary tale
- **Kubernetes debugging**: Practical tools and techniques for production
- **Career narratives**: Tech support stories as professional development
- **Climate and tech**: Long-term thinking about the industry's future
- **Content publishing**: Ghost CMS, custom themes, RSS feeds
- **AI impact**: How LLMs are changing the information ecosystem

## Related

- [[devops]] — Kubernetes, container orchestration, cloud infrastructure
- [[open-source]] — Sustainability, maintenance burden, community dynamics
- [[search-engines]] — Google's AI overview, knowledge monopolization
-  — AWS, EKS, VPC networking
-  — Non-traditional paths to senior engineering
-  — Macroeconomic forces, monopolization, AI disruption

## Influence

- Blog has a dedicated readership via RSS and email subscriptions
- Posts are shared on Mastodon and tech communities
- The "Post-Google Internet" analysis is one of the more thoughtful critiques of AI search integration
- Tech support stories provide rare visibility into non-traditional engineering career paths
- Custom Ghost theme is available on GitLab for others to use

## Sources

- matduggan.com — Primary blog
- "FYI: Broadcom is ruining Bitnami containers" (August 2025)
- "What Does a Post-Google Internet Look Like" (June 2025)
- "Tech Support Stories Part 2" (February 2024)
- "Write your own Ghost Theme"
- "Climate change what-if" conversation post
- Mastodon: @matdevdug@c.im
- Ghost CMS theme: GitLab repository (minimal design with Mastodon integration)
