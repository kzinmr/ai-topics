---
title: "rel=next HTTP headers to Firefox for HTML pages"
url: "https://simonwillison.net/2026/Nov/7/link-rel-next/"
fetched_at: 2026-11-08T10:01:03.902383+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# rel=next HTTP headers to Firefox for HTML pages

Source: https://simonwillison.net/2026/Nov/7/link-rel-next/

7th November 2026 - Link Blog
datasette #3046: Don't serve link: rel=next HTTP headers to Firefox for HTML pages
. I was looking at the Firefox network panel today when I noticed that requests to a Datasette table page were triggering an
HTTP prefetch
to the next page of rows in that table.
This was happening because Datasette pages serve an HTTP
link
header like this:
link: <https://latest.datasette.io/fixtures/compound_three_primary_keys?_next=a%2Cd%2Cv>; rel="next"
This is bad. A tiny fraction of the visitors to one of those pages will click the "next" link, which means their browser is fetching unnecessary data and the Datasette server is having to render an entire page that then gets thrown away.
I dug in and learned that Firefox has
an issue
that has been open for 24 years about this behavior...
And one of the early comments on that issue links to
my blog post from 2002
complaining about this feature. I hadn't just forgotten that I had written about it, I had forgotten the feature entirely!
