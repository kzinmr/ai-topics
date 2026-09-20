---
title: "datasette-auth-github 1.0"
url: "https://simonwillison.net/2026/Sep/19/datasette-auth-github/"
fetched_at: 2026-09-20T10:01:20.216297+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# datasette-auth-github 1.0

Source: https://simonwillison.net/2026/Sep/19/datasette-auth-github/

I run this GitHub login plugin on the
agent.datasette.io
demo site and I noticed that my authenticated sessions weren't lasting very long. It turned out that the plugin was setting cookies without a
Max-Age
parameter, so they were expiring at the end of a browser session (which in Mobile Safari seems to happen pretty often, independently of how you are using the app.)
I fixed that in
#80
and, since this plugin has been around for quite a while and is tested against both Datasette 0.65.x and Datasette 1.0ax, I decided to bump it up to a 1.0 release. I'm trying to get better at promoting stable plugins to 1.0.
