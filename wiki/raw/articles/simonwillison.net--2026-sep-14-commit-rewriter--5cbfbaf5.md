---
title: "commit-rewriter 0.1"
url: "https://simonwillison.net/2026/Sep/14/commit-rewriter/"
fetched_at: 2026-09-14T10:02:12.737198+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# commit-rewriter 0.1

Source: https://simonwillison.net/2026/Sep/14/commit-rewriter/

I built this little web app the other day to help edit the commit messages for the
Datasette security releases
. The initial commits were full of coding agent cruft and references to issue IDs from our private repository, so they weren't fit for publication.
If you want to edit the commit messages for a repository you can run it like this:
uvx commit-rewriter path/to/repo
Omit the path if you are already in the directory for that repo.
When you submit your edits the tool creates a timestamped branch of your current repo state - to allow you to revert if you need to - and then rewrites every commit from the first one you edited to the most recent.
