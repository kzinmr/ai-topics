---
title: "alchemy-utils 0.1a0"
url: "https://simonwillison.net/2026/Aug/12/alchemy-utils/"
fetched_at: 2026-08-13T10:19:21.351015+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# alchemy-utils 0.1a0

Source: https://simonwillison.net/2026/Aug/12/alchemy-utils/

I've long pondered what a database agnostic version of my
sqlite-utils
Python library and CLI utility might look like. This morning (literally a shower project) I tasked Codex and GPT-5.6 Sol Ultra with building a prototype:
Do a research spike to see what it would take to build a library with the same core API as SQLite-utils - in particular the insert and upsert and insert_all and upsert_all and create and update methods, and the table introspection stuff - but backed by SQLalchemy so it works for multiple database engines
Test against PostgreSQL and SQLite and duckdb
Use ~/dev/sqlite-utils for reference
Create a git repo for this and commit and early and often - use uv init to start the project - use red/green TDD and pytest, see ~/dev/django-sql-dashboard for one idea as to how the PostgreSQL tests could work
It took
very few follow-up prompts
to produce this project in a state good enough to release as an alpha.
Here's a one-liner I can use to list the rows in a table in my local PostgreSQL copy of my blog's database:
uvx --with 'alchemy-utils[postgresql]' alchemy-utils rows 'postgresql+psycopg://simon@localhost:5432/simonwillisonblog'  redirects_redirect
The output from that starts like this:
[
  {
    "id": 2328,
    "domain": "simonwillison.net",
    "path": "2020/May/21/apple-photos-sqlite/",
    "target": "/2020/May/21/dogsheep-photos/",
    "created": "2020-05-21T13:03:46.591692-07:00"
  },
  {
    "id": 3,
    "domain": "feeds.simonwillison.net",
    "path": "swn-links",
    "target": "https://simonwillison.net/atom/links/",
    "created": "2017-10-01T14:12:54.820729-07:00"
  }
Or if you'd like a DuckDB database with
every tree in San Francisco
, schema created automatically to match the file:
curl 'https://raw.githubusercontent.com/simonw/sf-tree-history/refs/heads/main/Street_Tree_List.csv' | uvx --with 'alchemy-utils[duckdb]' alchemy-utils insert 'duckdb:////tmp/trees.db' trees - --csv
(That one took nearly an hour the first time I ran it, so I
had Codex optimize it
and got it down to around 35 seconds.)
