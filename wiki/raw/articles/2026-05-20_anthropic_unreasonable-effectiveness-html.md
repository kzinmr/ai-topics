---
title: "Using Claude Code: The unreasonable effectiveness of HTML"
source: "https://claude.com/blog/using-claude-code-the-unreasonable-effectiveness-of-html"
author: "Thariq Shihipar"
date: 2026-05-20
source_type: blog
source_domain: claude.com
source_org: Anthropic
tags: [claude-code, html, markdown, agent-communication, developer-tooling]
---

# Using Claude Code: The unreasonable effectiveness of HTML

**Author:** Thariq Shihipar (Member of Technical Staff, Anthropic)
**Published:** May 20, 2026 · 5 min read
**Source:** [claude.com/blog](https://claude.com/blog/using-claude-code-the-unreasonable-effectiveness-of-html)

---

## Core Thesis

Markdown has become the dominant agent-to-human communication format, but its limitations become acute for complex work. The author now **strongly prefers HTML** as an output format with Claude Code, and observes a growing internal trend toward the same. HTML enables richer, more readable, shareable, and interactive documents, keeping humans "in the loop" more effectively.

> "Markdown has become an increasingly restrictive format. I find it difficult to read a Markdown file of more than a hundred lines; I want to use Claude to generate richer visualizations, color and diagrams; and I want to be able to share these outputs more easily."

---

## Why Use HTML Instead of Markdown

### 1. Information Density
HTML can natively represent a far broader set of information than Markdown. Examples include tables, CSS-styled design data, SVG illustrations and diagrams, JavaScript interactions, code snippets with `<script>` tags, spatial data via absolute positioning / canvas, and embedded images with `<img>` tags.

> "In my opinion, there is almost no set of information that Claude can read that you cannot efficiently represent with HTML."

### 2. Visual Clarity and Ease of Reading
As Claude produces longer specs and plans, large Markdown files become unreadable. HTML documents can be organized with tabs, illustrations, links, responsive design, making navigation and comprehension effortless.

### 3. Ease of Sharing
Markdown files require attachments; most browsers don't render them natively. HTML files can be shared via a simple link – colleagues can open them anywhere.

### 4. Two-Way Interactions
HTML allows interactive elements (sliders, knobs) to tweak designs or algorithm parameters directly in the document. You can add "copy" buttons to export parameters as a prompt to paste back into Claude Code.

### 5. Data Ingestion
Claude Code can pull in rich context (file system, MCPs like Slack/Linear, web via Claude in Chrome, git history) to generate HTML reports.

## Getting Started

No special configuration needed. Simply prompt Claude Code: "make an HTML file" or "make an HTML artifact."

## Concrete Use Cases

1. **Specs, Planning, Exploration** – Rich canvas for brainstorming, comparing options, creating mockups, writing implementation plans
2. **Code Review & Understanding** – Render diffs, annotations, flowcharts, module diagrams
3. **Design & Prototypes** – HTML is expressive for UI design even if the final surface is React/Swift/etc.
4. **Reporting & Monitoring** – Auto-generated dashboards from git history, Slack threads, etc.
5. **Rich Post-Mortems & Debugging** – Trace dumps, log analysis, timeline views

## Key Takeaway

> "The output surface of an agent is a first-class design problem. HTML is the right medium for that surface."
