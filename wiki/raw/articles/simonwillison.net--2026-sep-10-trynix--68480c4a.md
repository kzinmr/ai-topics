---
title: "Any Nix package, live in your browser"
url: "https://simonwillison.net/2026/Sep/10/trynix/"
fetched_at: 2026-09-11T10:01:12.131553+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# Any Nix package, live in your browser

Source: https://simonwillison.net/2026/Sep/10/trynix/

10th September 2026 - Link Blog
Any Nix package, live in your browser
(
via
) Farid Zakaria calls this his "
magnum opus
of Nix work", and I can see why.
trynix.dev
provides a
qemu-wasm
powered x86_64 Linux virtual machine running entirely in your browser through WebAssembly. That VM can then be booted with
any Nix package
from the past 13 years. They are URL addressable, so you can navigate to this page:
https://trynix.dev/?pkg=python3%403.6.2
Then click "Load" and get an interactive shell against a virtual machine running Python 3.6.2 from 2017.
Farid is building all sorts of neat things on top of this. One recent example:
Review a pull request by booting it
introduces
trynix-preview
, described like this:
GitHub action that comments a link on a pull request which lets you boot the PR’s build in the browser using
https://trynix.dev
. No servers, just browsers.
