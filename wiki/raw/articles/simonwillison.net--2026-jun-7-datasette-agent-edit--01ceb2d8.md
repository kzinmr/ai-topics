---
title: "datasette-agent-edit 0.1a0"
url: "https://simonwillison.net/2026/Jun/7/datasette-agent-edit/#atom-everything"
fetched_at: 2026-06-08T07:01:15.164536+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# datasette-agent-edit 0.1a0

Source: https://simonwillison.net/2026/Jun/7/datasette-agent-edit/#atom-everything

I'm planning several plugins for
Datasette Agent
which can make edits to existing pieces of text - things like collaborative Markdown editing, updating large SQL queries, and editing SVG files.
Agentic editing of text is a little tricky to get right. My favorite published design for this is for the
Claude text editor
, which implements the following tools:
view
- view sections of a file, with line numbers added to every line.
str_replace
- find an exact
old_str
and replace it with
new_str
- fail if the original string is not unique
insert
- insert the specified text after the specified line number
Rather than recreate these patterns for every plugin that needs them I decided to create this base plugin,
datasette-agent-edit
, which implements the core tools in a way that allows them to be adapted for other plugins.
