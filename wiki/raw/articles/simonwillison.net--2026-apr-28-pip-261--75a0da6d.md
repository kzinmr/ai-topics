---
title: "What's new in pip 26.1"
url: "https://simonwillison.net/2026/Apr/28/pip-261/#atom-everything"
fetched_at: 2026-04-29T07:00:52.080243+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# What's new in pip 26.1

Source: https://simonwillison.net/2026/Apr/28/pip-261/#atom-everything

28th April 2026 - Link Blog
What's new in pip 26.1 - lockfiles and dependency cooldowns!
(
via
) Richard Si describes an excellent set of upgrades to Python's default
pip
tool for installing dependencies.
This version drops support for Python 3.9 - fair enough, since it's been EOL
since October
. macOS still ships with
python3
as a default Python 3.9, so I tried out the new Python version against Python 3.14 like this:
uv python install 3.14
mkdir /tmp/experiment
cd /tmp/experiment
python3.14 -m venv venv
source venv/bin/activate
pip install -U pip
pip --version
This confirmed I had
pip 26.1
- then I tried out the new lock files:
pip lock datasette llm
This installs Datasette and LLM and all of their dependencies and writes the whole lot to a 519 line
pylock.toml
file -
here's the result
.
The new release also supports dependency cooldowns,
discussed here previously
, via the new
--uploaded-prior-to PXD
option where X is a number of days. The format is
P-number-of-days-D
, following
ISO duration format
but only supporting days.
I shipped a new release of LLM, version 0.31,
three days ago
. Here's how to use the new
--uploaded-prior-to P4D
option to ask for a version that is at least 4 days old.
pip install llm --uploaded-prior-to P4D
venv/bin/llm --version
This gave me version 0.30.
