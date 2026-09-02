---
title: "Codex bundles LibreOffice"
url: "https://simonwillison.net/2026/Sep/1/codex-libreoffice/"
fetched_at: 2026-09-02T10:01:16.955764+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# Codex bundles LibreOffice

Source: https://simonwillison.net/2026/Sep/1/codex-libreoffice/

1st September 2026
I was poking around in my
~/.cache/
folder using
OmniDiskSweeper
when I spotted something interesting. The OpenAI Codex desktop app (since
rebranded
to just ChatGPT) has 1.7GB of stuff in there in a folder called
codex-primary-runtime
, including a full Python installation, a full Node.js installation, and native binaries for
Poppler
, git, and the
LibreOffice
open source office suite (which forked from OpenOffice.org in 2010):
The
~/.cache/codex-runtimes/codex-primary-runtime/plugins/openai-primary-runtime/plugins/documents
folder includes skills which tell Codex how to find and use those binaries.
