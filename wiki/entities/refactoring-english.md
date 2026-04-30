---
title: refactoring-english
description: Technical blog and forthcoming book by Michael Lynch about effective writing for software developers — covering commit messages, design docs, AI vs human writing quality, passive voice, and blog craftsmanship.
url: https://refactoringenglish.com
type: entity
updated: 2026-04-30
---

# Refactoring English

**Refactoring English** is a website and forthcoming book by **Michael Lynch** (mtlynch.io), a software developer, bootstrapped founder, and former Google/Microsoft engineer. The project applies software engineering principles — refactoring, best practices, structured processes — to the craft of writing, arguing that most developers are not naturally poor writers but simply untrained ones.

The site serves as both a marketing landing page for the book (early access) and a publishing platform for sample chapters, exercises, tools, and blog posts. Several chapters have reached the front page of Hacker News.

## Overview

| Field | Value |
|-------|-------|
| **Author** | [Michael Lynch](https://mtlynch.io) |
| **Launch** | January 2025 (first sample chapter) |
| **Type** | Book project + companion website |
| **Book Title** | *Refactoring English: Effective Writing for Software Developers* |
| **Status** | Early access (digital download, new chapters monthly) |
| **Primary URL** | https://refactoringenglish.com |
| **Author's Blog** | https://mtlynch.io |
| **Mailing List** | https://buttondown.com/refactoring-english |
| **License** | Content CC BY 4.0 |

### Author Background

Michael Lynch graduated from Columbia University in 2007 with a BS in Computer Science. He worked as a software engineer at Microsoft and Google and as a security engineer at NCC Group before leaving Google in 2018 to become an independent bootstrapped founder. He founded **TinyPilot** (tinypilotkvm.com), an indie computer hardware company selling KVM-over-IP devices, which grew to $60–80k/month in revenue. He publishes detailed monthly and annual retrospectives about the indie founder journey on his personal blog at mtlynch.io.

Lynch previously created the course *"Hit the Front Page of Hacker News"*, which teaches developers to write posts that gain traction on HN. He is active on **Bluesky** (@mtlynch.io), **Mastodon** (@michael@m.mtlynch.io), and **Twitter/X** (@deliberatecoder).

## Core Topics

### Software Essays & Technical Writing

Lynch's post **"The Software Essays that Shaped Me"** (Sep 2025) curated ten influential essays, including: "The Joel Test" (Spolsky), "Parse, Don't Validate" (King), "No Silver Bullet" (Brooks), "Choices" (Spolsky), "Choose Boring Technology" (McKinley), and "Don't Put Logic in Tests" (Kuefler). He also analyzed **Nystrom's *Crafting Interpreters*** introduction for its use of narrative hooks, progressive disclosure, and reader empathy.

### Commit Messages

The sample chapter **"How to Write Useful Commit Messages"** (March 2025) teaches developers to treat commit messages as a form of technical communication rather than a chore. Key principles include:
- Separating the **what** from the **why** — the diff shows what changed, the message explains *why*
- Writing for future maintainers (including your future self)
- Using conventional commit prefixes for automated changelog generation
- Including context about trade-offs and alternatives considered
- Structuring messages with a concise summary line followed by detailed body

### Passive Voice

The chapter **"Passive Voice Considered Harmful"** (January 2025) — a deliberate homage to Dijkstra's "Go To Statement Considered Harmful" — argues that passive voice is particularly damaging in technical writing. Key points include:
- Passive voice obscures agency: *"The file was deleted"* vs. *"The deployment script deleted the file"*
- It adds unnecessary word count and reduces readability
- It creates ambiguity in documentation and bug reports
- **Exercise**: A companion exercise tool "Can You Spot the Passive Voice?" was published to help developers train themselves to recognize passive constructions
- **Tool**: An interactive tool for detecting passive voice in text

### Design Documents

Lynch's experiment **"Which Design Doc Did a Human Write?"** (Mar 2026) compared a 16-hour human-written design doc against versions by Claude Opus 4.6 and GPT-5.4. Readers correctly identified the human version 2:1. AI tells included verbosity, overly precise time estimates, generic security recommendations, meaningless bold formatting, and diagrams with layout collisions "a human would instantly recognize as wrong."

The chapter **"Write Effective Design Documents"** and post **"How to Get Meaningful Feedback on Your Design Document"** (Nov 2025) advise structuring docs around decisions rather than chronology, including thorough "alternatives considered" sections, using real estate to signal which problems were hard, and writing for skimmability with action-oriented headings.

### AI Writing Quality

A recurring theme is human vs. AI writing quality in software contexts. Lynch's experiments find AI lacks: (1) judgment about *which* problems were hard (AI treats all topics equally), (2) genuine opinion and personal experience, (3) niche technical judgment, and (4) structure that follows a mental model rather than generic templates. The chapter **"Improve Your Writing with AI"** (Ch. 15) pragmatically covers using AI tools while avoiding generic, bloated output.

### Other Topics

- **Release announcements**: Writing release notes users actually read
- **Emails**: Techniques for effective professional email communication
- **Tutorials**: Rules for writing tutorials that respect the reader's time
- **Feedback**: Giving and receiving useful feedback on technical writing
- **Blogging for developers**: Writing posts developers read — audience understanding, skimmer accommodation, discoverability

## Writing Style & Philosophy

Lynch's writing philosophy for *Refactoring English* is deeply informed by his software engineering background. The book's title itself is a metaphor: just as code refactoring improves structure without changing behavior, *Refactoring English* aims to improve the clarity and effectiveness of technical writing without changing the underlying technical content.

### Core Principles

1. **Writing is a skill, not a talent.** The same mindset shift that helps programmers improve applies to writing.
2. **Brevity is performance optimization.** Every extra word taxes the reader's attention like inefficient code taxes CPU.
3. **Know your reader.** Understanding audience needs is paramount — applies across commit messages, design docs, blog posts, and emails.
4. **Structure signals importance.** Design docs should allocate the most space to the hardest problems; blog posts should front-load interesting content.
5. **Active voice, always.** Passive voice obscures responsibility and increases cognitive load. Technical writing must be direct.
6. **Delete aggressively.** Ruthless pruning is one of the most valuable editing skills.
7. **Accommodate skimmers.** Most technical readers scan rather than read linearly — use clear headings, bullets, and highlighted takeaways.

### Influences

Lynch's writing approach draws from:
- **Joel Spolsky** — clarity, humor, and practical wisdom in technical essays
- **Julia Evans** — making complex topics accessible with plain language and diagrams
- **Paul Graham** — essay structure and persuasive argumentation
- **Simon Willison** — prolific, link-rich blogging that adds value through commentary
- **Robert Nystrom** (*Crafting Interpreters*) — exceptional tutorial structure and reader empathy
- The technical communication traditions of Microsoft and Google engineering cultures

## Blog Structure

The refactoringenglish.com site sections:

### Blog Posts

Articles about writing and software engineering:
- **"The Most Popular Blogs of Hacker News in 2025"** (Jan 2026) — analysis of top HN bloggers Willison (#1), Geerling (#2), Goedecke (#3), Krebs (#4), Agarwal (#5)
- **"Which Design Doc Did a Human Write?"** (Mar 2026) — AI vs. human design doc experiment
- **"The Software Essays that Shaped Me"** (Sep 2025)
- **"What Makes the Intro to Crafting Interpreters so Good?"** (Nov 2025)

### Sample Chapters

Sample chapters published as standalone guides:
- **Why Improve Your Writing?** (Mar 2026)
- **How to Get Meaningful Feedback on Your Design Document** (Nov 2025)
- **Underused Techniques for Effective Emails** (Jul 2025)
- **How to Write Compelling Software Release Announcements** (Jun 2025)
- **How to Write Blog Posts that Developers Read** (Mar 2025)
- **How to Write Useful Commit Messages** (Mar 2025)
- **Passive Voice Considered Harmful** (Jan 2025)
- **Rules for Writing Software Tutorials** (Jan 2025)

### Exercises

Interactive exercises to practice writing skills:
- **Can You Spot the Passive Voice?** (January 2025) — a drill for recognizing passive constructions

### Tools

Practical utilities for improving writing:
- **HN Popularity Contest** (March 2025) — methodology and analysis tool for measuring Hacker News blog popularity
- **Can You Spot the Passive Voice?** (January 2025) — interactive passive voice detection tool

## Reception & Impact

Since launching in January 2025, *Refactoring English* has gained significant traction in the developer community. Multiple sample chapters reached the front page of **Hacker News**, generating extensive discussion about developer writing practices. The HN analysis post (January 2026) became one of the most-discussed HN posts, with Lynch's methodology for ranking personal blogs sparking ongoing community conversation. The AI vs. human design doc experiment was widely shared and cited in discussions about AI limitations in technical communication. Lynch also publishes monthly retrospectives documenting the book-writing process, providing transparency into the indie author journey.

## Cross-References

- **[[simon-willison]]** — #1 HN blogger in Lynch's 2025 analysis; his link-blogging model is studied
- **[[jeff-geerling]]** — #2 HN blogger; cited as an example of quality video-to-text repurposing
- **[[julia-evans]]** — Influence on Lynch's accessible technical writing philosophy
- **[[crafting-interpreters]]** — Analyzed by Lynch as a model of exceptional tutorial writing
- **[[technical-writing]]** — General topic domain
- **[[hacker-news]]** — Platform where Lynch's writing gained visibility

## References

- refactoringenglish.com--blog-2025-hn-top-5--cec035dc
- refactoringenglish.com--blog-ai-vs-human-design-doc--fdbc8a9f
- refactoringenglish.com--blog-chapter-interest-results--4c8236f2
- refactoringenglish.com--blog-crafting-interpreters-intro--c56fde35
- refactoringenglish.com--blog-interview-adam-gordon-bell--9925d3ab
- refactoringenglish.com--blog-software-essays-that-shaped-me--d4f69bc7
- refactoringenglish.com--chapters-commit-messages--0183ef65
- refactoringenglish.com--chapters-passive-voice-considered-harmful--de833e4c
- refactoringenglish.com--chapters-release-announcements--9e3824af
- refactoringenglish.com--chapters-rules-for-software-tutorials--52bcc5a7
- refactoringenglish.com--chapters-techniques-for-writing-emails--d5889809
- refactoringenglish.com--chapters-useful-feedback-on-design-docs--96066621
- refactoringenglish.com--chapters-why-improve-your-writing--f44aad2c
- refactoringenglish.com--chapters-write-blog-posts-developers-read--a0ed73d1
- refactoringenglish.com--exercises-recognize-passive-voice--9d6ed6cf
- refactoringenglish.com--services-blog-editing-sample-future-of-git--a8f91646
- refactoringenglish.com--tools-hn-popularity-methodology--891f8d90
- refactoringenglish.com--tools-recognize-passive-voice--045e046d
