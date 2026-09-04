# OpenAI Blog RSS Date Discovery

## Problem

OpenAI blog articles (`openai.com/index/*`) are behind Cloudflare protection. Neither `curl` nor `delegate_task` with web toolset can reliably fetch the page HTML, making meta-tag date extraction impossible.

## Solution: RSS Feed

OpenAI's blog RSS feed is not Cloudflare-protected and provides canonical publication dates:

```bash
curl -sL --max-time 10 "https://openai.com/blog/rss.xml" | grep -B2 -A2 "article-slug"
```

Output example:
```xml
<title><![CDATA[Apple is getting this wrong]]></title>
<description><![CDATA[OpenAI addresses Apple's baseless lawsuit...]]></description>
<link>https://openai.com/index/apple-is-getting-this-wrong</link>
<guid isPermaLink="true">https://openai.com/index/apple-is-getting-this-wrong</guid>
<category><![CDATA[Company]]></category>
<pubDate>Mon, 03 Aug 2026 22:00:00 GMT</pubDate>
```

## For Article Content

Use Jina Reader to bypass Cloudflare for the article body:
```bash
curl -sL --max-time 15 "https://r.jina.ai/https://openai.com/index/article-slug/" -H "Accept: text/plain"
```

See `references/web-article-fetching-pattern.md` for the full Jina Reader pattern.

## Workflow

1. Extract slug from URL: `openai.com/index/{slug}`
2. `grep` RSS for the slug to get `<pubDate>`
3. Parse date from RFC 2822 format (e.g., "Mon, 03 Aug 2026 22:00:00 GMT" → "2026-08-03")
4. Use Jina Reader for article body
5. Construct filename: `{YYYY-MM-DD}_openai_{slug}.md`

## Pitfall

RSS `<pubDate>` uses RFC 2822 format with timezone. OpenAI uses GMT/UTC. If the date is near midnight, verify whether the local date differs from GMT.
