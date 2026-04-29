---
title: "SQL functions in Google Sheets to fetch data from Datasette"
url: "https://simonwillison.net/2026/Apr/20/datasette-sql/#atom-everything"
fetched_at: 2026-04-29T07:01:20.227413+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# SQL functions in Google Sheets to fetch data from Datasette

Source: https://simonwillison.net/2026/Apr/20/datasette-sql/#atom-everything

I put together some notes on patterns for fetching data from a Datasette instance directly into Google Sheets - using the
importdata()
function, a "named function" that wraps it or a Google Apps Script if you need to send an API token in an HTTP header (not supported by
importdata()
.)
Here's
an example sheet
demonstrating all three methods.
