---
title: "Dan Abramov"
tags: [person]
created: 2026-04-24
updated: 2026-04-24
type: entity
---

# Dan Abramov

**URL:** https://overreacted.io
**Blog:** overreacted.io
**Twitter/X:** @dan_abramov
**Bluesky:** @danabra.mov
**GitHub:** gaearon

## Overview

Dan Abramov is a core contributor to React and a prominent voice in the frontend development community. He co-created Redux and Create React App, and has worked at Meta on the React team. His blog overreacted.io has been one of the most influential technical blogs in the JavaScript ecosystem since its founding in 2018.

His writing is characterized by deep conceptual exploration, animated explanations, and a willingness to challenge his own past conclusions publicly. He has a distinctive teaching style that favors interactive understanding over memorization.

## Timeline

| Date | Event |
|------|-------|
| 2015 | Co-created Redux with Andrew Clark; joined Meta's React team |
| 2018 | Launched overreacted.io personal blog |
| 2018 | Published "A Complete Guide to useEffect" — the canonical reference for React hooks |
| 2018 | Published "Wrote a hook. Lost my mind." — a self-critical reflection on over-engineering |
| 2019 | Published "How Are Function Components Different from Classes?" |
| 2019 | Published "Before You memo()" — arguing that memoization is often premature |
| 2020 | Published "Why Do React Elements Have a $$typeof Property?" — on security and serialization |
| 2020 | Published "Goodbye, Clean Code" — challenging rigid code review conventions |
| 2021 | Published "Why React Re-Renders" — deep dive into rendering semantics |
| 2022 | Published "React as a UI Runtime" — framing React as a stateful runtime, not just a rendering library |
| 2022 | Published "Before You useReducer()" — arguing state machines for most use cases |
| 2023 | Published "React Canaries: Incremental Feature Rollout for Ecosystem Libraries" |
| 2023 | Published "Can AI Save Programming?" — skeptical examination of AI code generation |
| 2024 | Published "How to Make a React App from Scratch" — frameworkless React setup |
| 2024 | Published "Why Is React Called 'React'?" — historical deep dive |
| 2025 | Published "My Apology to the React Community" — acknowledging React's communication failures around RSC |
| 2025 | Published "Progressive JSON" — exploring the RSC protocol internals |
| 2025 | Published "Introducing RSC Explorer" — interactive tool for understanding React Server Components |
| 2026 | Published "A Social Filesystem" — exploring AT Protocol and Bluesky's data model |
| 2026 | Announced relocation to Japan for independent work |

## Core Ideas

### React as a Mental Model, Not Just a Library

Dan's most distinctive contribution to frontend discourse is his focus on **mental models**. He consistently argues that React is not about APIs but about developing an accurate mental model of how rendering, state, and time interact. His posts "React as a UI Runtime" and "Why React Re-Renders" frame React as a stateful system with its own execution semantics — a runtime that manages UI state across renders.

> "I think the biggest mental shift for people who learn React is that it's not about writing HTML in JavaScript. It's about describing what the UI should look like for any given state, and letting React figure out the rest."

### Hooks and Closures: The Mental Cost

His "Complete Guide to useEffect" is arguably the most-read React blog post ever, and for good reason — it explains the relationship between hooks and JavaScript closures with pedagogical precision. But Dan has also been reflexively critical of hooks' complexity. In "Wrote a hook. Lost my mind" (2018), he documented his own over-engineering with hooks and concluded:

> "The point is: you don't always need a hook. Sometimes a variable and a function will do."

This willingness to publicly doubt his own creations has earned him unusual credibility in the developer community.

### Memoization Is Often Premature

In "Before You memo()" (2019), Dan challenged the reflexive use of `React.memo()`, arguing that unnecessary optimization is a common source of bugs:

> "React is pretty fast by default. Most of the time, you don't need to optimize renders. When you do need to optimize, reach for memo as a last resort."

The same pattern appears in "Before You useReducer()" (2022), where he argues that most state management is better served by colocated useState and the occasional state machine than by useReducer.

### Frameworkless React

Starting around 2024, Dan has advocated for understanding React without frameworks. "How to Make a React App from Scratch" demonstrates that React can be used without Vite, Next.js, or any build tool — a reaction against the complexity creep in the React ecosystem. This connects to his broader theme of **looking under the hood** rather than treating tooling as opaque magic.

### Social Computing and the AT Protocol

Dan's most recent major post, "A Social Filesystem" (January 2026), is a deep exploration of the AT Protocol (the protocol behind Bluesky). He walks through the design space of identity, data ownership, and cross-user references in a decentralized social network. The post is notable because:

1. It extends far beyond React into distributed systems design
2. It uses the same interactive, step-by-step reasoning style he's known for
3. It culminates in the insight that **the file format is the API** — open data formats enable interoperability in ways that proprietary APIs cannot

### RSC: Transparency Over Abstraction

His RSC Explorer tool (December 2025) embodies his teaching philosophy: instead of documenting React Server Components abstractly, he built an interactive debugger that lets you step through the actual protocol. His approach is consistently "show, don't tell" — he wants developers to understand the mechanics, not just the interface.

### Self-Correction as a Feature

Perhaps Dan's most influential meta-contribution is his willingness to change his mind publicly. He has repeatedly revisited and corrected his own past recommendations:
- In 2018 he promoted hooks enthusiastically, then spent years documenting their pitfalls
- In 2019 he promoted clean code patterns, then published "Goodbye, Clean Code" arguing that naming and conventions can hurt more than help
- In 2025 he apologized for React's communication around Server Components, acknowledging that the team had made it too difficult for developers to understand what was happening

## Key Quotes

> "React is not just a library. It's a way of thinking about UI."

> "The point is: you don't always need a hook. Sometimes a variable and a function will do."

> "React is pretty fast by default. Most of the time, you don't need to optimize renders."

> "I think the biggest mental shift for people who learn React is that it's not about writing HTML in JavaScript. It's about describing what the UI should look like for any given state, and letting React figure out the rest."

> "The file format is the API." — on open data formats enabling interoperability

> "I'm still not sure if 'use server' is a good idea." — on React Server Components

> "Goodbye, Clean Code. Let me tell you why." — from his 2020 post challenging rigid naming conventions

> "Can AI save programming? I'm not convinced." — from his 2023 post on AI code generation

## Recent Themes (2024–2026)

- **Independent work**: Left Meta, relocated to Japan, working on hobby projects like RSC Explorer
- **RSC transparency**: Built tools to demystify React Server Components after the CVE-2025-55182 security disclosure
- **Decentralized social**: Deep engagement with AT Protocol and Bluesky's architecture
- **Framework skepticism**: Advocating for understanding tools without abstraction layers
- **Community repair**: Publicly acknowledging React team communication failures

## Related Concepts

- [[overreacted-io]] — His primary area of technical contribution
- [[concepts/redux]] — Co-created this state management library
- [[concepts/at-protocol]] — Subject of his "Social Filesystem" analysis
-  — Interactive debugging over abstraction
-  — His central teaching methodology
-  — His argument against rigid naming conventions

## Influence Metrics

- "A Complete Guide to useEffect" (2019): One of the most-read React articles ever published
- Redux: ~60K+ GitHub stars, foundational to React ecosystem
- His blog consistently ranks among the top technical blogs in JavaScript surveys
- Known for animated, interactive blog posts that teach through exploration rather than exposition
