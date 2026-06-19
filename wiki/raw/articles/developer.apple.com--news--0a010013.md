---
title: "New domain for Sign in with Apple and iCloud+ Hide My Email"
url: "https://developer.apple.com/news/?id=sus6t6ab"
fetched_at: 2026-06-19T07:00:57.637958+00:00
source: "daringfireball.net"
tags: [blog, raw]
---

# New domain for Sign in with Apple and iCloud+ Hide My Email

Source: https://developer.apple.com/news/?id=sus6t6ab

Later this summer, Apple will unify the email domains used by Sign in with Apple and iCloud+ Hide My Email under a single, shared domain:
private.icloud.com
.
New addresses generated for both features will be issued on the new domain. For example:
Sign in with Apple addresses, previously issued on
privaterelay.appleid.com
, will be issued on
private.icloud.com
.
iCloud+ Hide My Email addresses, previously issued on
icloud.com
, will be issued on
private.icloud.com
.
Existing addresses on the legacy domains will continue to work and forward mail to users without interruption.
What you need to do
Developers with apps or websites that use Sign in with Apple should ensure that their account systems, email validation logic, and allowlists accept addresses on the new
private.icloud.com
domain in addition to existing domains:
privaterelay.appleid.com
and
icloud.com
.
Email service providers should update any domain-based filtering, suppression lists, or routing rules that explicitly enumerate relay domains so that the new
private.icloud.com
domain is included.
Learn more
about Sign in with Apple
Communicating using the Private Email
Relay Service
