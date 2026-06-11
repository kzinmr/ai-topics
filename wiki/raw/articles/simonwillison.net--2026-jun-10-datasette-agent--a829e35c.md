---
title: "datasette-agent 0.2a0"
url: "https://simonwillison.net/2026/Jun/10/datasette-agent/#atom-everything"
fetched_at: 2026-06-11T07:00:57.127232+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# datasette-agent 0.2a0

Source: https://simonwillison.net/2026/Jun/10/datasette-agent/#atom-everything

Highlights from the release notes:
Tools can now ask the user questions mid-execution. Tools that declare a
context
parameter receive a
ToolContext
object, and
await context.ask_user(...)
can ask a yes/no, multiple-choice (
options=[...]
) or free-text (
free_text=True
) question. While a question is unanswered the agent turn suspends: the question renders as a form in the chat UI and persists to the internal database, so suspended conversations survive a server restart. Once answered, the tool re-executes from the top with stored answers replayed, so call
ask_user()
before performing side effects.
#20
New built-in
save_query
tool: the agent can save SQL it has written as a
Datasette stored query
. Saving always requires human approval - the agent shows the full SQL plus the proposed name, database and visibility, and nothing is stored until you click Yes.
#20
The
ask_user()
feature was enabled by the new LLM alpha I
built yesterday
with the help of Claude Fable 5.
