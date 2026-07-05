---
title: "Four vulnerabilities in Guix"
url: "https://lwn.net/Articles/1081199/"
fetched_at: 2026-07-04T07:01:40.229793+00:00
source: "LWN.net"
tags: [blog, raw]
---

# Four vulnerabilities in Guix

Source: https://lwn.net/Articles/1081199/

Four vulnerabilities in Guix
[Posted July 3, 2026 by jzb]
The
GNU Guix
project has
announced
three vulnerabilities in the
guix substitute
utility as well
as a fourth that affects the
guix pull
and
guix
time-machine
commands. The impact of the vulnerabilities ranges from remote privilege
escalation to local disclosure of sensitive files.
The remote exploitation of
guix substitute
only requires that the
vulnerable system attempt to download a binary substitute. Any
configured substitute server, including ones discovered using
guix-daemon
's
--discover
option, can exploit this, and so can a
man-in-the-middle (MITM), regardless of whether
https
is used in the
substitute server urls.
The local exploitation of
guix substitute
only requires
the ability to connect to guix-daemon's socket, which by default any
user can do.
Separately, another security issue (CVE ID pending) was identified
in
guix pull
and
guix time-machine
, which enables anyone who can
control the channels file used by these commands to cause a file to be
created or overwritten wherever the user running the command in
question has permission to create them.
The project is recommending that all users upgrade
guix
and
guix-daemon
immediately. See the announcement for
instructions, how to test for the vulnerabilities, the disclosure
timeline, and more.
