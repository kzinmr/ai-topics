---
title: "datasette-referrer-policy"
type: concept
created: 2026-05-06
updated: 2026-05-06
status: L1
tags:
  - datasette
  - web-security
  - privacy
  - simon-willison
sources:
  - https://simonwillison.net/2026/May/5/datasette-referrer-policy/
---

# datasette-referrer-policy 0.1

**datasette-referrer-policy** is a Datasette plugin by [[entities/simon-willison]] (released May 5, 2026, v0.1) that controls the HTTP `Referrer-Policy` header for Datasette instances.

## Purpose

The plugin addresses a common security/privacy concern: when users click links from a Datasette instance to external sites, the browser may send the full URL (including query parameters) as the `Referer` header to the destination site. This can leak:

- SQL query text that contains sensitive filter values
- Internal table/column names
- API keys or tokens embedded in URLs

## How It Works

The plugin sets the `Referrer-Policy` HTTP header to a more restrictive value (typically `strict-origin-when-cross-origin` or `no-referrer`), preventing full URLs from being leaked to external sites when users navigate away from the Datasette instance.

## Significance

This is a small but important security hardening step, especially for Datasette instances that expose sensitive data or are used internally. It exemplifies Simon's approach of building **security as composable plugins** rather than monolithic features.

## Related

- [[entities/datasette]] — Core data exploration platform
- [[entities/simon-willison]] — Creator
- [[concepts/defense-in-depth]] — Layered security strategy

## Sources

- [datasette-referrer-policy 0.1 release notes](https://simonwillison.net/2026/May/5/datasette-referrer-policy/)

## References

- simonwillison.net--2026-may-5-datasette-referrer-policy--47e367af
