---
title: "Rebuilding Harvey's Design System From the Ground Up"
source: "Harvey Blog"
url: "https://www.harvey.ai/blog/rebuilding-harveys-design-system-from-the-ground-up"
scraped: "2026-05-10T01:27:09.299792+00:00"
lastmod: "2026-01-16T14:00:00.000Z"
type: "sitemap"
---

# Rebuilding Harvey's Design System From the Ground Up

**Source**: [https://www.harvey.ai/blog/rebuilding-harveys-design-system-from-the-ground-up](https://www.harvey.ai/blog/rebuilding-harveys-design-system-from-the-ground-up)

Harvey Agents execute legal work end-to-end
Learn more
Harvey Agents execute legal work end-to-end
Learn more
Harvey Agents execute legal work end-to-end
Learn more
→
:Harvey:
Platform
Solutions
Customers
Security
Resources
About
Overview
→
A unified view of how Harvey's products work together to support your entire practice.
Assistant
→
Ask questions, analyze documents, and draft faster with domain-specific AI.
Vault
→
Securely store, organize, and bulk-analyze legal documents.
Knowledge
→
Research complex legal, regulatory, and tax questions across domains.
Workflow Agents
→
Run pre-built Workflow agents or build your own, tailored to your firm's needs.
Harvey Mobile
→
Get up to speed, capture new information, and keep work moving from anywhere.
Ecosystem
→
Access Harvey where you already work and ground every answer in sources you trust.
Harvey Agents
→
Harvey Agents execute legal work end-to-end, so you can focus on what only lawyers can do.
Innovation
→
Scale expertise and impact to drive firmwide transformation.
In-House
→
Streamline work and shift focus to strategy and speed.
Transactional
→
Accelerate due diligence, contract analysis, and review with precision and control.
Litigation
→
Reduce manual effort, prioritize strategy, and drive stronger outcomes in litigation.
Mid-Sized Firms
→
Drive outsize impact with tools built for lean teams.
Collaboration
→
Work with legal teams across organizations in secure, shared spaces.
A New Era of Collaboration for Legal and Professional Services
→
Law firms and professional service networks have been using Harvey to build new service models and add value collaboratively.
Blog
→
Product updates, insights, and behind-the-scenes from the Harvey team.
Resources Hub
→
The latest videos, webinars, guides, and reports from Harvey.
Press Kit
→
Resources for maintaining a uniform and professional presentation of the Harvey brand.
ROI Calculator Law Firm
→
See Harvey's Impact on Your Firm.
ROI Calculator In House
→
See Harvey's Impact on Your Business.
Harvey Academy
→
Introducing Harvey Academy: on-demand training, expert workflows, and step-by-step guidance to help legal teams get the most out of Harvey.
Company
→
About Harvey, our leadership, and career opportunities.
Newsroom
→
Press releases and partnership announcements.
2025 Year in Review
→
In 2025, we celebrated major customer wins, introduced product breakthroughs, and expanded our global presence. Most importantly, we continued to deepen our commitment to building the best AI solutions for our customers.
Login
Request a Demo
Platform
Overview
A unified view of how Harvey's products work together to support your entire practice.
Assistant
Ask questions, analyze documents, and draft faster with domain-specific AI.
Vault
Securely store, organize, and bulk-analyze legal documents.
Knowledge
Research complex legal, regulatory, and tax questions across domains.
Workflow Agents
Run pre-built Workflow agents or build your own, tailored to your firm's needs.
Harvey Mobile
Get up to speed, capture new information, and keep work moving from anywhere.
Ecosystem
Access Harvey where you already work and ground every answer in sources you trust.
Harvey Agents
Harvey Agents execute legal work end-to-end, so you can focus on what only lawyers can do.
Solutions
Innovation
Scale expertise and impact to drive firmwide transformation.
In-House
Streamline work and shift focus to strategy and speed.
Transactional
Accelerate due diligence, contract analysis, and review with precision and control.
Litigation
Reduce manual effort, prioritize strategy, and drive stronger outcomes in litigation.
Mid-Sized Firms
Drive outsize impact with tools built for lean teams.
Collaboration
Work with legal teams across organizations in secure, shared spaces.
A New Era of Collaboration for Legal and Professional Services
Law firms and professional service networks have been using Harvey to build new service models and add value collaboratively.
Customers
Security
Resources
Blog
Product updates, insights, and behind-the-scenes from the Harvey team.
Resources Hub
The latest videos, webinars, guides, and reports from Harvey.
Press Kit
Resources for maintaining a uniform and professional presentation of the Harvey brand.
ROI Calculator Law Firm
See Harvey's Impact on Your Firm.
ROI Calculator In House
See Harvey's Impact on Your Business.
Harvey Academy
Introducing Harvey Academy: on-demand training, expert workflows, and step-by-step guidance to help legal teams get the most out of Harvey.
About
Company
About Harvey, our leadership, and career opportunities.
Newsroom
Press releases and partnership announcements.
2025 Year in Review
In 2025, we celebrated major customer wins, introduced product breakthroughs, and expanded our global presence. Most importantly, we continued to deepen our commitment to building the best AI solutions for our customers.
Request a Demo
Login
US
EU
AU
Technical
Rebuilding :Harvey:'s Design System From the Ground Up
A look at how we re-architected our design system to help teams move faster without sacrificing quality or consistency.
by
Christopher Sim
,
Stephanie Yeung
, and
Brian Nelson
•
Jan 16, 2026
Earlier this year, our Engineering, Product, and Design (EPD) team faced a challenge: Our product complexity was growing faster than our design infrastructure could support. We were expanding into new product pillars, scaling the Design and Engineering teams, and shipping features across increasingly diverse surfaces. But our design system wasn't keeping pace.
Our existing infrastructure was more of a collection of components than a fully realized design system. We had a component library in Figma paired with a React codebase that mixed legacy components, Shadcn components, and custom one-off implementations. This created gaps between design and code that required manual interpretation when building new features. As we continued to grow, it became clear that a more unified foundation would help us move faster without sacrificing consistency or quality.
Throughout the rest of this blog post, I'll walk through how we rebuilt the system: establishing a semantic token architecture, automating token maintenance through the Figma API, migrating existing products without disrupting feature development, and aligning component structure between design and code.
The Problem: Color and Component Sprawl
Our token system had transformed organically over time, which is a polite way of saying it was chaotic. We had neutrals ranging from 910 to 940 in some places, colors spanning 100 to 1000 in others, and 50 to 950 elsewhere. Some colors only had two values, like 200 and 700. Designers were mixing primitive and semantic colors inconsistently, and maintaining it all was becoming impossible.
We also had multiple versions of the same component living in different files, each with slightly different implementations. There was no clear ownership or contribution process, and no way to ensure quality or consistency as new components were added. This wasn't just a design problem or an engineering problem; it was a systems problem that was slowing down the entire Product organization.
Our Approach: Start With a Strong Foundation
We decided to rebuild the system based on three core principles.
First,
we needed designers and engineers to speak the same language
. The translation errors between Figma and implementation were costing us time and creating inconsistencies. We could eliminate much of that friction by aligning our naming conventions and standardizing how we defined and used tokens.
Second,
we needed to shift from naming things based on appearance to naming them based on intent
. Instead of having designers mix primitives like “neutral-400” with semantics like “text-primary” for different use cases, we moved to cleaner, role-based tokens like “foreground-base” that could be used for any foreground element — text, icons, or other UI elements. This semantic approach makes it easier to theme, scale, and maintain the system because tokens capture meaning, not just visual properties.
Third,
we needed to future-proof the architecture
. Whether we introduced new themes, accessibility modes, or product brands down the line, this foundation needed to flex without requiring another major overhaul.
How the System Works
For designers and engineers using the system, it needs to be
understandable
. You should be able to look at a component and see what it does. In Figma's layers panel, you should see a clear hierarchy of elements with everything properly named, making it obvious how components are constructed.
The system also needs to be
comprehensive
: component coverage across use cases, state coverage for all interaction patterns, accessibility coverage by default, and everything mapped to code so there's no ambiguity in implementation. It must be
flexible
enough to combine sub-components in reasonable ways to create new patterns without requiring entirely new components for every variation.
Most importantly, it has to be
maintainable
. We can't build more functionality if we're constantly bogged down in production work. Following Don’t Repeat Yourself (DRY) principles and building reusable foundations helps us scale without accumulating technical debt.
Redefining our Design Tokens
Most of our time went into color tokens, which numbered in the hundreds. Since theming colors was critical for creating an accessible dark mode, we needed fine granularity while ensuring every token had a clear name and purpose.
We spent a lot of time figuring out the schema. How granular should we be? Should we create component-level tokens or keep things semantic? Should we focus on appearance or intent? These weren't abstract questions. Every decision had implications for how designers would work in Figma, how engineers would implement in code, and how maintainable the system would be long term.
We validated our decisions by reconstructing the appearance of existing components using only the new tokens. We tested them across all primary surfaces in both Figma and code to ensure they worked on both sides.
We also cleaned up and recalibrated the entire color palette. This meant adjusting chroma for warmth and neutrality: higher chroma in light tones for cleaner whites, lower chroma in dark tones to avoid brown shifts, and locked the hue around 90° for a consistent warm-neutral feel. This applied across all of our accent and supportive colors like amber, olive, and jade. Every color was now accessible by default, calibrated for WCAG contrast across both light and dark modes.
Maintaining our Tokens
With limited resources, we had to be strategic about maintenance. We needed a solution that would work for both designers and engineers without requiring designers to edit code directly.
To solve for this, we built a GitHub Action that syncs Figma variables directly to our codebase. When a designer updates a token in Figma, they can trigger the sync workflow, which pulls the changes and opens a pull request automatically. Figma's variable table became our single source of truth.
All new tokens are prefixed with “hy-” to differentiate them from legacy tokens and Tailwind's built-in tokens. In code, engineers work with these tokens through Tailwind classes like “bg-hy-bg-base” or “text-hy-fg-subtle,” with full autocomplete support.
Implementing a Migration Strategy
We couldn't just deprecate our old tokens and components overnight. Teams were actively building features, and we needed to maintain velocity while transitioning to the new system. Since there wasn't a direct equivalent for every legacy token, this wasn't a simple find-and-replace operation. We broke migration into phases:
We started with legacy tokens that mapped cleanly to new ones. Things like “bg-primary” → “bg-hy-bg-base” and “text-muted” → “text-hy-fg-subtle.” This gave us quick wins and established patterns.
All new design system components use new tokens exclusively, so we updated our coding agent guides and documentation to reference the new system. New features should use new tokens by default, with exceptions only for specs already designed with legacy tokens. We refactor existing components opportunistically as they're touched for other work. The key is maintaining component-level cohesion: for example, when updating a button in the composer, update all the buttons in that context.
To support adoption, we built enforcement into the developer workflow. We added linter rules that warn when engineers use primitive tokens like “bg-neutral-950” directly. As we approach 80% adoption of new tokens, we'll add warnings for legacy semantic tokens. At 95%, those warnings become errors in pre-commit.
We also created Cursor rules so that AI-assisted development would automatically use the new tokens and patterns. In Figma's Dev Mode, engineers can see exactly which tokens are being used in any design, eliminating ambiguity in implementation.
Rebuilding Components
As the Design team scaled, we lacked clear structure around component contribution. We had discrepancies in how components were built, and no process for deciding when something should be contributed to the system versus isolated in a product pillar.
We worked with the Design team to establish a clearer approach: build components in Figma closer to how engineers build them in code. This alignment reduced the translation gap and made implementation more straightforward.
Similar to our token work, we focused on high-touch components first, rebuilding them with the new tokens and ensuring the anatomy of each component was extensible for our growing variety of use cases.
We also established a branching workflow to maintain quality control. We didn't want to stifle designer contributions, but we needed clearer vetting to ensure work met our standards. Finally, step-by-step contribution guides help designers through each step of the process.
What's Next
We view this work as just the tip of the iceberg. We might need to adjust our approach in the coming months, but these changes equip us to handle the next phase of scale with more confidence and less friction.
As we expand into new surfaces like mobile and Microsoft Office add-ins, we're tackling a particularly interesting challenge: bridging the gap between platform-specific constraints and Harvey's identity. Each platform has its own design language and user expectations. One of our immediate investments is
adapting our components in ways that feel native to each platform, while still unmistakably Harvey
.
We're also investing in tighter collaboration between Brand and Product. We want to start injecting brand elements across the product more deliberately, ensuring there's real symbiosis. Whether someone's using Harvey on web, mobile, or within an Office add-in, it should feel cohesively like Harvey — not just functionally consistent, but aesthetically and emotionally aligned with our brand.
Most importantly, building a design system isn't a one-and-done project. It's an ongoing practice of observation, iteration, and collaboration. The real measure of success is in whether designers and engineers can ship better work, faster, without sacrificing quality or consistency.
Harvey's design system would not have been possible without the extraordinarily talented members of our Design and Engineering teams: Cindy Nguyen, Billy Wan, Phillip Cerles, Utkarsh Saxena, Bjørn Rostad, Nikhil Patel, and many others.
If designing the building blocks that power the future of legal technology sounds interesting to you,
we're hiring
for design system roles across the Design and Engineering teams.
Request a Demo
Unable to load form. Please try again.
Try Again
Thank you!
We'll be in touch shortly.
Next Up
How we Built Image Understanding for Legal Documents
How Harvey Secures Embeddings at Scale
Rebuilding the Review Algorithm to Increase Accuracy and Speed
Unlock Professional Class AI for Your Firm
Request a Demo
Copyright © 2026 Harvey AI Corporation. All rights reserved.
Platform
Assistant
→
Vault
→
Knowledge
→
Workflow Agents
→
Ecosystem
→
Partnerships
→
Solutions
Innovation
→
In-House
→
Transactional
→
Litigation
→
Mid-Sized Firms
→
Collaboration
→
About
Customers
→
Security
→
Company
→
Newsroom
→
Careers
→
Law Schools
→
Resources
Blog
→
Resources Hub
→
Harvey Academy
→
Help Center
→
Legal
→
Privacy Policy
→
Press Kit
→
Your Privacy Choices
→
Follow
X
→
LinkedIn
→
YouTube
→
Copyright © 2026 Harvey AI Corporation. All rights reserved.
