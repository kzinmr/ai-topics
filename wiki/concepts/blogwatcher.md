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
- 1wwzn.mjt.lu--lnk-auyaajz-u8saac7fq14aa-j058aaykjinqaotmkadfx-wbp5jxkibhin--076fb7e5.md
- 1wwzn.mjt.lu--lnk-auyaajz-u8saac7fq14aa-j058aaykjinqaotmkadfx-wbp5jxkibhin--1d7fc04b.md
- 1wwzn.mjt.lu--lnk-auyaajz-u8saac7fq14aa-j058aaykjinqaotmkadfx-wbp5jxkibhin--2bcc20cc.md
- 1wwzn.mjt.lu--lnk-auyaajz-u8saac7fq14aa-j058aaykjinqaotmkadfx-wbp5jxkibhin--69163e9c.md
- 1wwzn.mjt.lu--lnk-auyaajz-u8saac7fq14aa-j058aaykjinqaotmkadfx-wbp5jxkibhin--77208c48.md
- 1wwzn.mjt.lu--lnk-auyaajz-u8saac7fq14aa-j058aaykjinqaotmkadfx-wbp5jxkibhin--7721aac4.md
- 1wwzn.mjt.lu--lnk-auyaajz-u8saac7fq14aa-j058aaykjinqaotmkadfx-wbp5jxkibhin--ca7b0c40.md
- 1wwzn.mjt.lu--lnk-auyaajz-u8saac7fq14aa-j058aaykjinqaotmkadfx-wbp5jxkibhin--d079a25e.md
- 1wwzn.mjt.lu--lnk-auyaajz-u8saac7fq14aa-j058aaykjinqaotmkadfx-wbp5jxkibhin--d1f197fd.md
- 1wwzn.mjt.lu--lnk-auyaajz-u8saac7fq14aa-j058aaykjinqaotmkadfx-wbp5jxkibhin--f1599b18.md
- link.mail.beehiiv.com--v1-c-egncq-2f2jvg3z1srwrf0xp8bpezq9blfjerv54xwhpqya03y3hxxho--98301fce.md
- link.mail.beehiiv.com--v1-c-fdwil4uku86wqgvus3egbvwijwnr0qrid1t52cdd3ycpxsgzkdgudcn--d6b97e0d.md
- link.mail.beehiiv.com--v1-c-flmndfoqqdagyp02knd-2btoydtna7dyup8x9ojh9ydyafdw-2facow--833dfc31.md
- link.mail.beehiiv.com--v1-c-rzu84jjuqtlob2xnoxdmevcovpgsrvmtypn-2faksb3vonpp3iit9qm--7c95458f.md
- link.mail.beehiiv.com--v1-c-tuelquqblb9b8x5nfvjl0yxldxqsdi38e0mcgui9o4rogqjs8udbu82--755b683a.md
- link.mail.beehiiv.com--v1-c-wkk9di7edeejysjelesl-2buku9cmuohlf9jsh1zgx6maqhnqowaa46--7187f065.md
- link.mail.beehiiv.com--v1-c-yhaytm4tol-2fdentwekzmsfvk2r8xs3nf7ym-2fpkdc-2f9nfojs0l--1d2d6e9f.md
- link.mail.beehiiv.com--v1-c-zsmnsbs4av5l3tcaburthamkhku5gujltkenmg0htyh0g3aphr1kf3t--0ca94edc.md
- email.beehiivstatus.com--49c1f40fb4dcb29d82bce117a3e26a5e8dc1bee5-hclick--f7a23737.md
- email.beehiivstatus.com--93eaffcb4f7bd068b52ce4c6880ce95134da9322-hclick--549fc6e0.md
- email.beehiivstatus.com--a201af524cdc2d4e93bca0e6854943bd6e0b5c35-hclick--3cbad0a7.md
- hp.beehiiv.com--ccc0ac2a-6a36-45a0-abc7-558e4657920f--1e38ee24.md
- theverge.com--podcast-917965-apple-ceo-cook-ternus-transition--77eb3723.md
- theverge.com--ai-artificial-intelligence-920191-elon-musk-sam-altman-trial--d38a955b.md
- therobotreport.com--zoox-sets-geographic-milestones-product-features-robotaxi--4cd5b33b.md
- theconversation.com--why-iran-targeted-amazon-data-centers-and-what-that-does-and--f30f95b8.md
- taiwannews.com.tw--news-6332336--8809b6ca.md
- sfstandard.com--2026-04-28-oak-sfo-reach-naming-settlement--9d6a555e.md
- 9to5google.com--2026-04-22-samsung-is-increasingly-worried-about-first-ever---6ba1c854.md
- buttondown.com--hillelwayne-archive-illegal-vs-unwanted-states--af0358c8.md
- carraglobe.com--semiconductor-supply-chain-disruption-2026--93988faf.md
- cnbc.com--2026-03-24-amazon-zoox-robotaxi-rides-austin-miami-html--a1af8da3.md
- danieldelaney.net--confirm--80eaaa29.md
- edition.cnn.com--2026-04-04-health-ai-impact-college-student-thinking-wellnes--977d3c46.md
- experimental-history.com--p-the-3rd-annual-blog-post-competition--a5edcdc2.md
- prnewswire.com--news-releases-agibot-reaches-10-000-units-as-real-world-dema--1e894058.md
- repebble.com--blog-spring-2026-dev-contest-results--b85c169a.md
- bidirlm-omnimodal-encoders.md
- aposd-vs-clean-code-debate-2026-04.md
- ainews-tasteful-tokenmaxxing-2026-04-23.md
- 2026-the-linear-algebra-needed-for-aiml-complete-roadmap.md
- 2026-2040-proofdoors-and-efficiency-of-cdcl-solvers.md
- 2026-2040-on-merge-models.md
- 2026-2040-mathematical-methods-and-human-thought-in-the-age-.md
- 2026-2039-on-strengths-and-limitations-of-single-vector-embe.md
- 2026-2025-what-is-oauth?.md
- 2026-04-26-some-notes-on-ai.md
- 2026-04-25-korean-ai-model-rankings.md
