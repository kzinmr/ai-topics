---
title: "Redis Array Playground"
url: "https://simonwillison.net/2026/May/4/redis-array/#atom-everything"
fetched_at: 2026-05-05T07:00:55.875076+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# Redis Array Playground

Source: https://simonwillison.net/2026/May/4/redis-array/#atom-everything

Salvatore Sanfilippo submitted
a PR
adding a new data type - arrays - to Redis.
The new commands are
ARCOUNT
,
ARDEL
,
ARDELRANGE
,
ARGET
,
ARGETRANGE
,
ARGREP
,
ARINFO
,
ARINSERT
,
ARLASTITEMS
,
ARLEN
,
ARMGET
,
ARMSET
,
ARNEXT
,
AROP
,
ARRING
,
ARSCAN
,
ARSEEK
,
ARSET
.
The implementation is currently available in a branch, so I
had Claude Code for web
build this interactive playground for trying out the new commands in a WASM-compiled build of a subset of Redis running in the browser.
The most interesting new command is
ARGREP
which can run a server-side grep against a range of values in the array using the newly vendored
TRE regex library
.
Salvatore wrote more about the AI-assisted development process for the array type in
Redis array type: short story of a long development
.
