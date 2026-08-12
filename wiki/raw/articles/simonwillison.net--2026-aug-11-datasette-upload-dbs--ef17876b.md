---
title: "datasette-upload-dbs 0.5a0"
url: "https://simonwillison.net/2026/Aug/11/datasette-upload-dbs/#atom-everything"
fetched_at: 2026-08-12T10:18:34.963109+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# datasette-upload-dbs 0.5a0

Source: https://simonwillison.net/2026/Aug/11/datasette-upload-dbs/#atom-everything

This plugin has been around for a while - it lets users upload a brand new SQLite database to a hosted Datasette instance, at which point that database will start being served by that instance.
It can also be used to atomically swap a database with a more recent version. The uploaded database is saved to a file, verified, then swapped in so
/name
starts serving the new one.
The new release adds a formalized API, so you can replace an existing database (or add a new one) like this:
curl -X POST \
  -H "Authorization: Bearer $API_TOKEN" \
  -H "Accept: application/json" \
  -F "db=@content.db" \
  -F "db_name=content" \
  https://your-instance.example.com/-/upload-dbs
This means you can build fresh databases in an environment such as GitHub Actions and swap them in production as soon as that build has completed.
