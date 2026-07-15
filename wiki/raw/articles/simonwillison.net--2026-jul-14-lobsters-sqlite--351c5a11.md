---
title: "lobste.rs is now running on SQLite"
url: "https://simonwillison.net/2026/Jul/14/lobsters-sqlite/#atom-everything"
fetched_at: 2026-07-15T07:01:41.295788+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# lobste.rs is now running on SQLite

Source: https://simonwillison.net/2026/Jul/14/lobsters-sqlite/#atom-everything

14th July 2026 - Link Blog
lobste.rs is now running on SQLite
. Community site
Lobsters
has been planning a migration away from MariaDB
since August 2018
- originally targeting PostgreSQL, but last year they decided to
investigate SQLite
instead.
This weekend they completed the migration, and now consider it stable enough that it looks like this is the permanent architecture for the site going forward:
SQLite seems to have passed with flying colors: cpu usage is down, memory usage is down, site seems to be snappier at least for me, 1/2 the vps cost once mariadb vps is taken down
The Lobsters Rails application now runs on a single VPS, with a primary content SQLite database file that's around 3.8GB.
There's also
a 1.1GB cache database, a 218MB queue database, and a still growing 555MB rack_attack database used by the
Rack::Attack
middleware for blocking and throttling abusive requests.
There are plenty more details in both the linked thread and this
SQLite migration PR
by Thomas Dziedzic, which added 735 lines and removed 593 lines across 30 commits and 188 files. That PR built on top of previous PRs
#1705
,
#1871
, and
#1924
.
This is a really useful case study, and a great reminder that you can get a whole lot done with a single server and SQLite in 2026.
