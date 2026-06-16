---
title: "datasette-agent 0.3a0"
url: "https://simonwillison.net/2026/Jun/15/datasette-agent/#atom-everything"
fetched_at: 2026-06-16T07:00:48.826721+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# datasette-agent 0.3a0

Source: https://simonwillison.net/2026/Jun/15/datasette-agent/#atom-everything

New tool,
execute_write_sql
, which requests user approval and then writes to a database - taking user permissions into account.
#27
I added a mechanism for asking user approval in
datasette agent 0.2a0
. The new
execute_write_sql
tool can now prompt the user for all kinds of useful operations. Here's an example where I add some pelican sightings to my
pelican_sightings
table:
The new version also enhances the
datasette agent chat
terminal mode to support approvals, and adds several new options including
--unsafe
mode for auto-approving them:
datasette agent chat
can execute tools that require user approval.
#30
Three new options for
datasette agent chat
-
--root
to run as root,
--yes
to approve all ask user questions, and
--unsafe
for both.
Tools can now provide plain text alternatives to HTML, for display in the
datasette agent chat
CLI.
#31
The
datasette agent chat content.db -m gpt-5.5 --unsafe
command can now be used to chat directly with a specific database
and
directly modify it through prompts like "create a notes table", "add a note about X" etc.
