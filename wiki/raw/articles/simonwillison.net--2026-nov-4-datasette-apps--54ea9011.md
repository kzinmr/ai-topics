---
title: "datasette-apps 0.3a0"
url: "https://simonwillison.net/2026/Nov/4/datasette-apps/"
fetched_at: 2026-11-05T10:01:10.925862+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# datasette-apps 0.3a0

Source: https://simonwillison.net/2026/Nov/4/datasette-apps/

Datasette Apps adds support for hosting and editing custom HTML applications inside of Datasette.
These can be created by hand, but it's easier to create them using LLMs via
Datasette Agent
. This release improves that integration:
Apps can now be tagged in Datasette Agent chat messages by typing
#
, which autocompletes from the apps the user has permission to view.
New
app_add_stored_queries()
and
app_remove_stored_queries()
tools let the agent manage which stored queries an app is allowed to call. Granting a write query requires approval from the user first.
app_create()
now checks that each requested stored query exists and that the user can view it, and asks the user to approve any write queries before the app is created.
The "View app" buttons shown by the agent tools, and the links on
#
app references, now open the app full screen in the Datasette Agent panel.
