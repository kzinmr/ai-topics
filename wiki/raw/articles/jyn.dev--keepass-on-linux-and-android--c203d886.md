---
title: "Keepass on Linux and Android"
url: "https://jyn.dev/keepass-on-linux-and-android/"
fetched_at: 2026-04-28T07:02:51.916835+00:00
source: "jyn.dev"
tags: [blog, raw]
---

# Keepass on Linux and Android

Source: https://jyn.dev/keepass-on-linux-and-android/

Previously, I wrote about
using a password manager
.
However, the disadvantage of using an audited, local manager like
Keepass
is that it's hard to share passwords between devices.
You can put the encrypted database in a file-sharing service like Google Drive,
but that means you need a sync client on all of your devices, and Google
doesn't have one for Linux
.
Fortunately, it's Linux, so there are alternatives.
My current favorite sync client is
google-drive-ocamlfuse
.
Although it's annoying to have to
build from source
and is
command-line only
,
it lets you treat Drive as a user-land file system using
FUSE
,
which is particularly nice for clients that aren't web-aware (like keepass).
It also has an excellent
walkthrough
on how to automount on boot
(this is Linux, nothing is automatic).
Appendix
Why not just use Dropbox? It doesn't support NTFS drives
(or anything other than
ext4
).
Why not use an encrypted service, like
MEGA
or
Spideroak
? They don't support WebDAV,
and I don't feel like going through a file system every time I update passwords
(most phone clients only allow file access through a specific app).
Why not use <some other service> that (supports WebDAV or syncs automatically on phones) and has a Linux client? I haven't heard of <some other service>.
