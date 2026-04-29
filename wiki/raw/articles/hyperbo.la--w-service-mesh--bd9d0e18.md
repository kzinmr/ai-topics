---
title: "Service meshes are organization tools, not technical ones"
url: "https://hyperbo.la/w/service-mesh/"
fetched_at: 2026-04-29T07:02:15.345480+00:00
source: "hyperbola :: blog"
tags: [blog, raw]
---

# Service meshes are organization tools, not technical ones

Source: https://hyperbo.la/w/service-mesh/

Why should we do a service mesh?
A service mesh is great for injecting policy in a way that makes it difficult
for folks to do the wrong thing: connection pooling and keep alive, retries,
timeouts, enforcing data locality constraints, AZ-local routing, etc, etc.
To a certain extent, product engineering wanting to move quickly is at odds with
reliability and a service mesh is difficult to subvert. Services meshes make
sure the right thing happens by default.
This is probably the most succinct reason for deploying one. It allows
separation of responsibilities in ways that don’t add extra steps product teams
have to remember to do.
