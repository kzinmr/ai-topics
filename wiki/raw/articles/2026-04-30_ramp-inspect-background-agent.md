# Why Ramp Built "Inspect": A Background Coding Agent

**Source:** https://builders.ramp.com/post/why-we-built-our-background-agent
**Author:** Ramp Engineering Team
**Date:** 2026-04-30 (ingested)

## Overview

Ramp developed **Inspect**, a custom background coding agent designed to verify its own work with the same context and tools as a human engineer. Unlike off-the-shelf tools, Inspect is deeply integrated into Ramp's specific infrastructure, allowing it to handle ~30% of all merged pull requests.

---

## 1. Core Philosophy & Capabilities

Inspect is designed to "close the loop" on verification. It doesn't just write code; it proves the code works.

* **Agency & Context:** It can run tests, review telemetry, query feature flags (backend), and visually verify changes via screenshots and live previews (frontend).
* **Unlimited Concurrency:** Sessions run in the cloud, meaning builders can kick off multiple versions of a prompt or swap models without taxing local hardware.
* **Multiplayer Support:** Sessions are shareable. Colleagues can jump into a session to help, perform live QA, or request changes during a PR review.
* **Zero-Setup Speed:** Environments are pre-cloned and pre-installed. Speed is limited only by the model's time-to-first-token.

> "When background agents are fast, they're strictly better than local: same intelligence, more power, and unlimited concurrency."

---

## 2. The Technical Stack: The Sandbox

The execution environment is the heart of the agent, built on **Modal** for near-instant scaling.

### Infrastructure Strategy
* **Modal Sandboxes:** Used for isolated, sandboxed VMs.
* **Image Registry:** Images for each repo are rebuilt every 30 minutes (cloning, installing dependencies, and initial builds).
* **Snapshots:** Modal's file system snapshots allow freezing and restoring state. This ensures the repo is never more than 30 minutes out of date.
* **OpenCode:** Ramp uses [OpenCode](https://opencode.ai/) as the agent framework because it is server-first, has a typed SDK, and is open-source (allowing the agent to read its own source code to understand its capabilities).

### Optimization Tactics
* **Warm Starts:** The sandbox begins warming up as soon as a user starts typing a prompt, often finishing before the user hits "Enter."
* **Immediate Research:** The agent is allowed to read files immediately upon startup; file *edits* are blocked only until the 30-minute git sync completes.
* **Build-Step Heavy:** Everything possible (including running test suites once to populate caches) is moved to the image build step.

---

## 3. API & State Management

To support multiple clients (Slack, Web, Chrome) and real-time updates, Ramp built a robust backend.

* **Cloudflare Durable Objects:** Every session has its own SQLite database. This prevents performance interference between parallel sessions.
* **Cloudflare Agents SDK:** Handles real-time streaming and WebSocket hibernation to keep costs low during idle periods.
* **Authentication:** Uses GitHub OAuth. Changes are pushed via the sandbox, but the PR is opened using the **user's token**. 
    * *Reasoning:* This prevents "unreviewed code" vectors where an app-owned bot could theoretically bypass human approval rules.

---

## 4. Client Interfaces

Inspect meets builders where they already work through three primary interfaces:

### Slack Bot
* **Virality:** Working in public channels encourages adoption.
* **Auto-Classification:** Uses a fast model (GPT-4o/equivalent) to determine which repository to work in based on message context and channel name.
* **Status Updates:** Uses a "Slack message tool" to post progress updates via Block Kit.

### Web Interface
* **Hosted VS Code:** A `code-server` instance runs inside the sandbox for manual tweaks.
* **Streamed Desktop:** Allows "computer use" for the agent to navigate web apps and take "before/after" screenshots for PRs.
* **Analytics:** Tracks the "Merge Rate"—the percentage of sessions resulting in a merged PR.

### Chrome Extension
* **Visual Editing:** Allows non-engineers to highlight React components to request changes.
* **Technical Detail:** Instead of sending heavy screenshots, it extracts the DOM and React internals to provide the model with a precise element tree.
* **Deployment:** Distributed via Managed Device Policy (MDM) to bypass the Chrome Web Store and force-install for the team.

---

## 5. Actionable Advice for Builders

Ramp encourages other companies to build their own internal agents rather than buying generic ones:

> "Owning the tooling lets you build something significantly more powerful than an off-the-shelf tool will ever be. After all, it only has to work on your code."

**Key Implementation Steps:**
1. **Use Modal** for fast-starting sandboxes.
2. **Adopt OpenCode** for the agent logic.
3. **Leverage Durable Objects** for session state.
4. **Automate the environment** so the agent has every tool a human dev has (Postgres, Sentry, Datadog, etc.).
