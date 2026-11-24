---
title: "datasette-charts 0.2a0"
url: "https://simonwillison.net/2026/Nov/24/datasette-charts/"
fetched_at: 2026-11-24T10:01:25.616321+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# datasette-charts 0.2a0

Source: https://simonwillison.net/2026/Nov/24/datasette-charts/

I introduced this new charting plugin for Datasette
yesterday
. Today it's gained integration with
Datasette Agent
, so now you can ask chat for a chart and it will create one for you using the same underlying chart suggestion and generation tools.
Here's a demo video, recorded on
agent.datasette.io
where you can sign in with GitHub to try the plugin yourself:
Download the video (MP4)
I prompt Datasette Agent to "Use #stats to show sqlite-utils downloads over time as a chart" - where typing "#stats" opens a table search box. It shows me a chart inline in the chat, and when I click "Open in the chart builder" it opens the chart in a panel along with the table page. I use the table page to switch to a chart of "datasette", then when I ask the agent "what does the chart show?" it notices that I changed the content in the panel and describes the new Datasette chart to me.
Here's
a Markdown export
of the chat from the video.
