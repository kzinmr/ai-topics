---
title: "Blogwatcher"
type: concept
status: incomplete
description: "CLI-based blog and RSS feed monitoring tool for tracking technical blogs and newsletters."
created: 2026-04-27
updated: 2026-04-28
tags: [concept, monitoring, rss, cli, automation]
aliases: [blogwatcher-cli, feed-monitor]
related: [[hermes-agent]], [[entities/simon-willison]]
sources: [https://github.com/NousResearch/hermes-agent]
---

# Blogwatcher

## Summary

**Blogwatcher** (`blogwatcher-cli`) is a CLI-based tool for monitoring blogs, RSS feeds, and newsletters. It is used within AI agent systems — particularly [[concepts/hermes-agent]] — to track technical blogs, detect new content, and trigger downstream processing workflows such as crawling, summarization, and wiki enrichment.

## Key Ideas

- **Feed Discovery**: Automatically discovers RSS/Atom feeds from blog URLs, with fallback to sitemap.xml scanning for static-site blogs (Astro, Hugo, Jekyll, Next.js).
- **CLI-First Design**: Lightweight command-line interface suitable for cron-driven automation and background agent execution.
- **HTML Scraping Fallback**: When RSS/Atom feeds are unavailable, attempts to scrape recent articles directly from the blog HTML or sitemap.
- **Webhook Integration**: New posts can trigger downstream actions (summarization, wiki entry creation, bookmarking).

## Architecture

Blogwatcher operates in several modes:

1. **RSS/Atom Probing**: Tests common feed paths (`/feed`, `/feed.xml`, `/rss.xml`, `/atom.xml`, `/blog/feed`, `/blog?format=rss`) and checks HTML `<head>` for `<link type="application/rss+xml">` tags.
2. **Sitemap.xml Fallback**: If no RSS feed is found, probes `/sitemap.xml` and parses blog-post URLs from the sitemap XML.
3. **Add & Track**: `blogwatcher-cli add "Blog Name" https://example.com` registers a blog for ongoing monitoring.
4. **Scrape Mode**: For blogs without any structured feed, can extract article metadata from HTML using heuristics.

## Usage Context

Blogwatcher is part of the Hermes Agent ecosystem, used in cron-based automated knowledge crawling pipelines. The typical workflow:

1. Blogwatcher detects a new post from a tracked blog
2. The post URL is passed to `web_extract()` for content extraction
3. Content is saved as a raw article to `wiki/raw/articles/`
4. Downstream skills process the article into concept or entity pages

## Related Concepts

- [[hermes-agent]] — The AI agent platform that uses blogwatcher for knowledge ingestion
- [[concepts/rss-monitoring]] — RSS/atom feed monitoring patterns
- [[concepts/automated-knowledge-crawl]] — Automated crawling pipelines

## Sources

- [Hermes Agent GitHub Repository](https://github.com/NousResearch/hermes-agent)
- [Hermes Agent Documentation](https://hermes-agent.nousresearch.com/docs/)
