---
title: "Release: llm 0.32rc1"
url: "https://simonwillison.net/2026/Jul/30/llm-rc1/#atom-everything"
fetched_at: 2026-07-31T10:24:10.133854+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# Release: llm 0.32rc1

Source: https://simonwillison.net/2026/Jul/30/llm-rc1/#atom-everything

This RC for LLM 0.32 finishes the work that
started in LLM 0.32a0
- it adds a
new schema design
that does a much better job of capturing the details of the prompts and responses returned by the latest model families.
The most important change is the use of content-addressable hash IDs for stored messages. This allows de-duplication in the database, and means that LLM can now represent trees of messages for forked conversations.
Since it involves a significant schema change - new tables only, and old data should not be affected at all - it's worth running a backup of your existing
logs.db
before upgrading to the RC:
llm logs backup logs-backup.db
The RC also adds support for
gpt-5.6-sol
,
gpt-5.6-terra
, and
gpt-5.6-luna
.
