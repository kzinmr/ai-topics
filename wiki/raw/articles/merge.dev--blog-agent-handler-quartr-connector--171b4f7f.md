---
title: "Agent Handler’s Quartr connector is live! Here's how your AI can securely use it"
url: "https://www.merge.dev/blog/agent-handler-quartr-connector"
fetched_at: 2026-05-30T07:01:27.075158+00:00
source: "Merge Blog"
tags: [blog, raw]
---

# Agent Handler’s Quartr connector is live! Here's how your AI can securely use it

Source: https://www.merge.dev/blog/agent-handler-quartr-connector

Quartr
is the leading first-party data layer for institutional finance and AI, covering earnings calls, conferences, investor events, and related documents across 15,000+ listed companies.
Now, their data is accessible to any internal or customer-facing AI through
Merge Agent Handler
!
Whether you're an AI company building on financial data, or a hedge fund, asset manager, research team, or IR department that already relies on Quartr, your AI can now access real-time earnings transcripts, investor presentations, financial reports, and AI-generated summaries without any custom integration work.
Quartr handles the data. Agent Handler handles the access control, authentication, and governance. And your team focuses on what the data enables.
Overview on Agent Handler’s Quartr connector
The Quartr connector
includes dozens of pre-built tools spanning the full range of IR data and AI-enriched outputs Quartr provides.
A snapshot of the pre-built tools featured on
our connector page
Every document type Quartr covers is queryable: earnings calls, capital markets days, AGMs, investor updates, fireside chats, and M&A announcements, across both live and recorded formats.
Tools like
list_companies
,
get_transcript
,
list_events
, and
get_slides
, for example, give your AI the ability to navigate Quartr's full coverage with precision.
On top of the raw data, the connector exposes Quartr's AI-generated summary layer directly. Your AI can, for instance, use
get_event_summary
,
get_transcript_summary
, or
get_report_summary
with configurable lengths—line, short, or long—so the output fits the context of whatever task is running.
The connector also surfaces timestamped audio and transcript chapters with speaker attribution, enabling AI to navigate to specific moments in an earnings call rather than processing the full document.
You can ultimately use the connector in one of two ways:
1. For your employees:
Connect Quartr and your IdP once, assign Quartr tools via SCIM-synced groups/roles, and employees access Quartr-backed workflows from their AI assistant via natural language. Agent Handler will enforce policies in the background and log each tool call.
Related:
A guide to using SCIM for AI
2. For your AI product:
Embed Quartr's tools into your product’s agent with Agent Handler as the execution and governance layer. In other words, Quartr becomes a native capability inside your product, and Agent Handler ensures every tool call is authenticated, scoped to the right user, and logged.
Common ways to use the Quartr connector
Here are just a few common ways to leverage the connector.
Enable your portfolio team to monitor earnings with ease
An asset manager can build an internal research agent that tracks every earnings event across its coverage universe.
When a company reports, the agent pulls the transcript, surfaces the AI-generated summary, and flags key passages: guidance language, segment commentary, management tone, etc.
Analysts get a structured briefing before the market opens instead of spending the first hour reading raw transcripts.
Related:
Examples of employee agents
Power a customer-facing research assistant
A wealth management platform can implement an AI assistant that lets clients ask questions about companies in their portfolio.
The agent retrieves earnings summaries, investor presentations, and event history from Quartr, then synthesizes an answer grounded in first-party IR material.
Agent Handler can control exactly which Quartr tools are exposed to end users, keeping internal research capabilities separate from the customer product.
Accelerate your due diligence process
An investment bank's coverage team can use an agent to rapidly synthesize IR material on a target company.
The agent retrieves transcripts and slide decks across a configurable lookback window, generates summaries at multiple lengths, and extracts segment data.
What previously took a junior analyst a full day of document gathering takes minutes.
Start using our Quartr connector for free
The Quartr connector is now generally available on Merge Agent Handler.
‍
Create a free account
to start testing it alongside Agent Handler's security and observability features in seconds. Or
schedule a demo
with one of our integration experts for a guided walkthrough.
