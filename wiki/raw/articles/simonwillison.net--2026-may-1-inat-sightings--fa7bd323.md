---
title: "iNaturalist Sightings"
url: "https://simonwillison.net/2026/May/1/inat-sightings/#atom-everything"
fetched_at: 2026-05-02T07:00:43.497120+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# iNaturalist Sightings

Source: https://simonwillison.net/2026/May/1/inat-sightings/#atom-everything

I wanted to see my
iNaturalist
observations - across two separate accounts - grouped by when they occurred. I'm camping this weekend so I built this entirely on my phone using Claude Code for web.
I started by building an
inaturalist-clumper
Python CLI for fetching and "clumping" observations - by default clumps use observations within 2 hours and 5km of each other.
Then I setup
simonw/inaturalist-clumps
as a
Git scraping
repository to run that tool and record the result to
clumps.json
.
That JSON file is hosted on GitHub, which means it can be fetched by JavaScript using CORS.
Finally I ran this prompt against my
simonw/tools
repo:
Build inat-sightings.html - an app that does a fetch() against https://raw.githubusercontent.com/simonw/inaturalist-clumps/refs/heads/main/clumps.json and then displays all of the observations on one page using the https://static.inaturalist.org/photos/538073008/small.jpg small.jpg URLs for the thumbnails - with loading=lazy - but when a thumbnail is clicked showing the large.jpg in an HTML modal. Both small and large should include the common species names if available
