# RSS Feed Batch Discovery

When you have a list of company/blog URLs and need to discover which have RSS feeds in bulk.

## Pattern

Use `concurrent.futures.ThreadPoolExecutor` with 15 workers to curl-check common RSS paths in parallel:

```python
import subprocess, concurrent.futures

def check_rss(name, base_url):
    """Check common RSS paths for a blog. Returns 'FOUND: <url>' or 'NOT FOUND'."""
    paths = [
        "/rss.xml", "/feed.xml", "/atom.xml", "/index.xml", "/feed", "/rss",
        "/blog/rss.xml", "/blog/feed.xml", "/blog/feed", "/blog/atom.xml",
        "/engineering/feed.xml", "/blog/rss", "/news/rss.xml", "/news/feed.xml",
    ]
    
    for path in paths[:10]:  # Try first 10 paths
        url = base_url.rstrip('/') + path
        try:
            # HEAD check for HTTP status
            result = subprocess.run(
                ["curl", "-sI", "-o", "/dev/null", "-w", "%{http_code}", "--max-time", "8", url],
                capture_output=True, text=True, timeout=10
            )
            code = result.stdout.strip()
            
            if code in ("200", "301", "302"):
                # Verify content is actually XML/RSS
                content_check = subprocess.run(
                    ["curl", "-sL", "--max-time", "8", url],
                    capture_output=True, text=True, timeout=10
                )
                content = content_check.stdout[:500].lower()
                if any(tag in content for tag in ["<rss", "<feed", "<channel", "xmlns"]):
                    return f"FOUND: {url} (HTTP {code})"
        except:
            pass
    return "NOT FOUND"

# Run in parallel
results = {}
blogs = {
    "Company Name": "https://company.com",
    # ... more companies
}

with concurrent.futures.ThreadPoolExecutor(max_workers=15) as executor:
    futures = {executor.submit(check_rss, name, url): name for name, url in blogs.items()}
    for future in concurrent.futures.as_completed(futures):
        name = futures[future]
        try:
            results[name] = future.result(timeout=15)
        except:
            results[name] = "TIMEOUT"

# Report
found = {k: v for k, v in results.items() if "FOUND" in v}
not_found = {k: v for k, v in results.items() if "FOUND" not in v}
```

## Expected Results

- **Corporate blogs on headless CMS** (Webflow, Contentful, Ghost): Usually NO RSS. ~20-25% discovery rate.
- **Self-hosted/Hugo/Jekyll blogs**: Often have RSS at `/index.xml` or `/feed.xml`.
- **WordPress blogs**: Usually at `/feed/` or `/feed.xml`.
- **Substack/Beehiiv**: Always at `/feed` (check the blog page for the actual URL pattern).

## Common Failures

- **HTTP 200 but HTML content**: The server returns 200 for everything (SPA routing). Content check catches these.
- **302 redirects**: blogwatcher-cli does NOT follow redirects. Use the final URL, not the redirect source.
- **Cloudflare/security blocks**: Some sites return 403 or captcha pages. Try adding `-H "User-Agent: blogwatcher/1.0"` to the curl command.

## Post-Discovery

For confirmed RSS feeds, add to monitoring:
```bash
# Add to blogwatcher DB
/opt/data/bin/blogwatcher-cli add "Company Blog" "BLOG_URL" --feed-url "RSS_URL"

# Test scan
/opt/data/bin/blogwatcher-cli scan "Company Blog"

# Mark backlog as read (critical!)
/opt/data/bin/blogwatcher-cli read-all --blog "Company Blog" --yes
```

Add to OPML Company Tech Blogs section:
```xml
<outline type="rss" text="Company Blog" title="Company Blog" xmlUrl="RSS_URL" htmlUrl="BLOG_URL" />
```
