---
title: "Your executable is a SQLite database"
url: "https://simonwillison.net/2026/Aug/24/your-executable-is-a-sqlite-database/"
fetched_at: 2026-08-25T10:01:27.473608+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# Your executable is a SQLite database

Source: https://simonwillison.net/2026/Aug/24/your-executable-is-a-sqlite-database/

24th August 2026 - Link Blog
Your executable is a SQLite database
(
via
) Farid Zakaria describes a neat Linux pattern for creating a SQLite database file that can be directly used as an executable binary.
The trick sets the SQLite file format's 4-byte application ID (68 bytes into the file) to SELF, standing for Structured Executable & Linkable Format.  The various components of the ELF executable format are then arranged into a number of different SQLite tables, using
this schema
.
Their
self-exec
interpreter (
C code here
) can then extract and execute the necessary pieces.
You can additionally use a Linux mechanism called
binfmt_misc
to teach the kernel to execute that any time it encounters an executable matching that binary pattern. Farid uses NixOS here, but without NixOS I think registration looks something like this:
printf '%s\n' ':self:M:68:SELF::/usr/local/bin/self-exec:' \
  > /proc/sys/fs/binfmt_misc/register
