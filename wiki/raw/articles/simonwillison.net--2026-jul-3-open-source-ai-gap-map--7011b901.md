---
title: "Open Source AI Gap Map"
url: "https://simonwillison.net/2026/Jul/3/open-source-ai-gap-map/#atom-everything"
fetched_at: 2026-07-04T07:01:39.512392+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# Open Source AI Gap Map

Source: https://simonwillison.net/2026/Jul/3/open-source-ai-gap-map/#atom-everything

3rd July 2026 - Link Blog
Open Source AI Gap Map
.
Current AI
is "a global partnership building a public option for AI", founded as a non-profit at the AI Action Summit in Paris in February 2025 and backed by serious capital ($400m already committed).
They
launched their Gap Map
a couple of days ago - an attempt at indexing the current state of open source AI:
The Gap Map v0.1 details 421 products in depth: 266 software tools and libraries, 85 models, 50 datasets, and 20 hardware projects, produced by 228 organizations. These products are organized into 14 categories across 3 layers of the stack (model components, product / UX, and infrastructure). The remaining 24,400 artifacts constitute the uncategorized long tail of the open source AI ecosystem, and will carry no score until they are researched and cited.
The map itself is interesting to explore, but I'm more excited about the underlying data - released under an MIT license in the
currentai-org/os-ai-map
GitHub account: 1,184 YAML files plus the notebooks, schemas and other scripts used to help gather them.
Since the files are on GitHub you can use Datasette Lite to explore some of them - here are
16,185 GitHub repos the project is tracking
as a CSV file loaded into Datasette Lite.
