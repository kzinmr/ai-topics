---
title: "datasette-charts 0.1a0"
url: "https://simonwillison.net/2026/Nov/23/datasette-charts/"
fetched_at: 2026-11-24T10:01:25.613480+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# datasette-charts 0.1a0

Source: https://simonwillison.net/2026/Nov/23/datasette-charts/

I've been thinking about this problem for over a year now, but on Sunday I finally fired up Claude Fable 5.2 to build an initial prototype. The prototype went so well that this is now a full plugin.
You can
try it out in Datasette Lite here
. It looks like this:
The new charts plugin works against any table or arbitrary SQL query in Datasette. It defines several different chart types (using vendored
D3
,
Observable Plot
, and
topojson-client
), each with a set of heuristics for identifying when they might be a good match for a specific set of rows.
Those suggestion thumbnails at the top are actual visualizations driven by the data, and selecting one pulls up the full chart along with tools for modifying it. You can also manually construct a chart from scratch.
As with other Datasette visualization plugins, the current state of your chart is persisted in a
#fragment
in the URL - so you can bookmark charts or share them with others.
The most important feature is that the charts take
all rows into account
. Previous charting plugins like
datasette-vega
would only show charts for the current page of results, generally up to 100 rows.
The new plugin compiles each chart to a SQL query that aggregates across the entire result set (potentially millions of rows) using GROUP BY, time bucketing, and window functions. Each query returns a result capped at 5,000 rows, suitable for display on the chart. The plugin uses sampling to help suggest charts for larger tables without evaluating the full result set.
I'm really happy with this initial release of the plugin. It's still very much an alpha, but it's the closest I've got to the dream of Datasette helping visualize data with as little required direction from the user as possible.
