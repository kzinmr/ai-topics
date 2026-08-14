---
title: "sqlite-utils 4.2.1"
url: "https://simonwillison.net/2026/Aug/13/sqlite-utils-2/"
fetched_at: 2026-08-14T10:21:52.096545+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# sqlite-utils 4.2.1

Source: https://simonwillison.net/2026/Aug/13/sqlite-utils-2/

Fixes a crashing bug in
sqlite-utils 4.2
. I'd introduced code that looks like this:
from typing_extensions import Self
It turned out the
typing-extensions
package was not listed as a dependency for
sqlite-utils
- it was installed by one of the other dependencies in the
dev dependency group
, but when you
uvx sqlite-utils
directly you don't get those dependencies.
As part of fixing this I figured out how to run a smoke test to ensure the CLI tool still works even without those dev dependencies, which can be run from the project checkout:
uv run --isolated --no-default-groups sqlite-utils --help
The
--no-default-groups
argument prevents it from installing that default
dev
group, and
--isolated
means that even if there is a
.venv/
folder containing extra dependencies they will be ignored for the duration of that
uv run
command.
