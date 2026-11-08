---
title: "Amutable Foundations: A Technical Overview"
url: "https://lwn.net/Articles/1105934/"
fetched_at: 2026-11-08T10:01:05.114442+00:00
source: "LWN.net"
tags: [blog, raw]
---

# Amutable Foundations: A Technical Overview

Source: https://lwn.net/Articles/1105934/

Amutable Foundations: A Technical Overview
[Posted November 7, 2026 by corbet]
Lennart Poettering, Michael Vogt, and Joaquim Rocha have put together
a
detailed overview
of what the Amutable Operating System (AOS) and
associated infrastructure will look like.
The image-based OS approach enables us to enforce some very strict
	but powerful security properties, which elevate the security
	posture of the system substantially above traditional Linux
	systems. Specifically, let's highlight seven major essential
	security properties of AOS here:
No Shell + No SSH + No Language Interpreters
. By default AOS
     does not install a UNIX shell, nor makes remote access via SSH
     available on the nodes. Moreover, we do not install any of the usual
     language interpreters (Python, Perl, …) by default. For most nodes a
     shell or interpreted language support is not required and it removes a
     whole class of attacks.
Signed Images Only
. On AOS only images that come with Verity
     data signed by a signing key listed in the Verity keyring may be
     activated.
[...]
The LWN site is currently under high scraper load, so comment
    display has been suppressed for anonymous users.
    If you are a
        human, you may read the comments by clicking the button below:
Note
: you can avoid this step in the future by logging
        into your LWN account.
