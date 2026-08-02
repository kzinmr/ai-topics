---
title: "datasette-apps 0.2a0"
url: "https://simonwillison.net/2026/Aug/1/datasette-apps/#atom-everything"
fetched_at: 2026-08-02T10:14:19.939303+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# datasette-apps 0.2a0

Source: https://simonwillison.net/2026/Aug/1/datasette-apps/#atom-everything

Changes that improve Datasette Apps when created and edited using
Datasette Agent
:
New
app_debug()
tool allowing agent to open an app (invisibly) and test it using JavaScript.
#33
New
app_list()
tool for listing apps the user has permission to edit, so the agent can edit them.
#36
The
app_debug()
tool is pretty neat: it works by displaying the app in a
opacity: 0
iframe with
pointer-events: none
(so it can't be seen or interacted with) and then executing agent-provided JavaScript inside that sandboxed iframe. This means the agent can smoke test that the app is working and even do things like measure the dimensions of different elements.
This uses the new
context.browser_task()
mechanism added in
datasette-agent 0.4a0
.
