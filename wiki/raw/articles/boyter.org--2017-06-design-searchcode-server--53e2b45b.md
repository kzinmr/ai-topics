---
title: "Design for searchcode server"
url: "https://boyter.org/2017/06/design-searchcode-server/"
fetched_at: 2026-05-05T07:02:00.075773+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# Design for searchcode server

Source: https://boyter.org/2017/06/design-searchcode-server/

Design for searchcode server
2017/06/27
(107 words)
A very brief update about the progress of searchcode server. Currently I am in the middle of reworking how the index is built and maintained. The idea being I want to add zero downtime index rebuilds which requires a blue/green index strategy. It is still very much in flux but the current design is to merge the indexer and searcher which should allow this to happen. I have been playing around with using an iPad as a production device these days and produced the following document.
Edit. People keep asking me what App I used to create this. It was made Pureflow for iOS and then exported.
