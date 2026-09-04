# Source URL Cloudflare/403 Verification Block

When verifying `take` candidates from triage during the post-recovery verification phase, the **primary source URL** (e.g., openai.com, anthropic.com) may be behind Cloudflare bot protection (HTTP 403, JavaScript challenge). This is distinct from the beehiiv/Substack Cloudflare blocks documented in the main skill (which happen during triage, not verification).

## Pattern

**Trigger**: Post-Recovery Verification step, when a `take` candidate's `url` points to an official company blog (openai.com, anthropic.com, huggingface.co) that returns HTTP 403 with a JavaScript challenge page.

**Symptoms**:
- `curl -sI` returns `403 text/html` with Cloudflare challenge HTML
- `web_extract` returns empty or truncated content
- The raw newsletter body is the only accessible source for article content
- The newsletter's curated summary (from triage `body_excerpt` + `reason_ja`) may need to serve as the primary source

## Workflow

When the primary source URL is inaccessible:

1. **Accept the limitation**: The newsletter's curated summary (stored in the triage JSON's `body_excerpt` and `reason_ja`) becomes the primary content. Document this in the wiki page's frontmatter `sources` array — list the newsletter raw file, and add a note about the Cloudflare block.

2. **Use secondary cross-references**: Check if other pipelines (sitemap-monitor, blog-ingest, raw-backlog-ingest) have scraped related content from different URLs about the same topic. Use `find ~/ai-topics/wiki/raw/articles -name "*keyword*" -mtime -7`.

3. **Use the newsletter's editorial framing**: Newsletter roundups (The Signal, AINews) often add context about product significance, deployment scope, and enterprise positioning that the official blog post lacks. This editorial framing is valuable wiki content.

4. **Create the page with appropriate confidence markers**: Add a note in the page body about verification limitations:
   ```markdown
   > **Note**: OpenAI's official blog post at openai.com was behind Cloudflare bot protection during ingestion.
   > Content sourced from The Signal newsletter (Jul 26, 2026) editorial summary.
   ```

5. **Frontmatter example**:
   ```yaml
   sources:
     - raw/newsletters/2026-07-26-...-newsletter.md
     # openai.com/index/... was Cloudflare 403 — content from newsletter editorial summary
   ```

## Validated Instances

- **2026-07-27**: Both `openai.com/index/introducing-openai-presence/` and `openai.com/index/health-in-chatgpt/` returned 403 (Cloudflare). Event pages created from The Signal newsletter editorial summary only. Secondary cross-references to existing events (GPT-Live, OpenAI CUA) filled technical context.
- **2026-07-27**: The Signal newsletter post page (`thesignal.substack.com/p/...`) was also Cloudflare-blocked. The triage agent had to fall back entirely on the truncated web_extract output for content extraction — but in this case the newsletter post page was accessed via web_extract (which succeeded) before the source URL verification step failed.

## Recovery Path for No-Primary-Source Verification

When NO primary source is accessible (both newsletter post page AND source URL are blocked):

1. Assess using only the triage `body_excerpt` and the newsletter subject line topics
2. Check against existing wiki pages — if a concept page already covers the topic at the level of detail available from the newsletter summary, mark as reference/skip
3. If the topic IS genuinely new and significant but all sources are blocked, create a minimal event page with the "verification limited" note
4. Do NOT force a `take` — if the blocked content might change the assessment (e.g., the article might reveal the product is vaporware), err on the side of skip/reference

## Differentiation from Beehiiv/Substack Triage Blocks

| Aspect | Beehiiv/Substack Triage Block | Source URL Verification Block |
|--------|------------------------------|------------------------------|
| Phase | Triage (before decisions) | Post-Recovery Verification (after decisions) |
| Impact | Cannot extract article topics | Cannot verify article content against primary source |
| Fallback | Subject line + section headings | Newsletter body_excerpt + editorial framing |
| Action | Skip with reason "content unreachable" | Create page with "verification limited" note |
