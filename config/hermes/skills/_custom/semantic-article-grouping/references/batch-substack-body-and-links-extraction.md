# Batch Substack Body + External Links Extraction

When processing 3+ Substack newsletters in a single triage pass, extract **both body paragraphs AND external article links** in one Python script. This eliminates redundant HTTP requests (one curl per newsletter instead of one for body + one for links) and ensures every triage decision has both a body excerpt and a resolved external URL.

## Pattern (validated June 2026)

```python
#!/usr/bin/env python3
"""Extract body paragraphs and external links from Substack newsletters."""
import subprocess, re, sys

# Map: newsletter_key → (human_name, canonical_url)
newsletters = {
    "lenny": ("Lenny's Podcast", "https://open.substack.com/pub/lenny/p/openai-codex-lead-on-the-new-shape"),
    "signal": ("The Signal", "https://open.substack.com/pub/thesignal/p/openai-brings-the-heat-claudes-tag"),
    "artifacts": ("Interconnects / Robotic", "https://open.substack.com/pub/robotic/p/artifacts-22-zyphra-cohere-and-poolside"),
}

for key, (name, url) in newsletters.items():
    result = subprocess.run(["curl", "-sL", url], capture_output=True, text=True, timeout=20)
    html = result.stdout
    
    # Step 1: Extract <article> content for body paragraphs
    article_match = re.search(r'<article[^>]*>(.*?)</article>', html, re.DOTALL)
    if article_match:
        article_html = article_match.group(1)
        # Extract <p> tags, strip HTML, filter short lines
        paras = re.findall(r'<p[^>]*>(.*?)</p>', article_html, re.DOTALL)
        body = []
        for p in paras:
            clean = re.sub(r'<[^>]+>', '', p).strip()
            if clean and len(clean) > 20:
                body.append(clean)
        
        print(f"\n{'='*60}")
        print(f"=== {name.upper()} ({len(body)} body paragraphs)")
        print(f"{'='*60}")
        for i, p in enumerate(body[:20]):  # First 20 paragraphs for triage
            print(f"  [{i+1}] {p[:200]}")
        if len(body) > 20:
            print(f"  ... ({len(body)-20} more paragraphs)")
        
        # Step 2: Extract external links from article area
        links = re.findall(r'href="(https?://[^"]*)"', article_html)
        relevant = [l for l in links if not any(x in l for x in [
            'substackcdn', 'substack.com', 'twitter.com', 'x.com',
            'fonts.', 'enable-javascript', 'open.substack',
            'js.hsforms', 'googleads', 'linkedin.com'
        ])]
        # Deduplicate while preserving order
        unique_links = list(dict.fromkeys(relevant))
        print(f"\n  External article links ({len(unique_links)}):")
        for l in unique_links[:15]:
            print(f"    - {l}")
    else:
        print(f"\n  No <article> tag found for {name}")
```

## Output Format

The script prints a structured per-newsletter block:

```
============================================================
=== LENNY'S PODCAST (36 body paragraphs)
============================================================
  [1] Why AI has completely flipped the product development process
  [2] What "taste" really means as a professional skill...
  ... (16 more paragraphs)
  ... (20 more paragraphs behind)
  
  External article links (40):
    - https://www.lennysnewsletter.com/p/why-humans-are-ais-biggest-bottleneck
    - https://www.lennysnewsletter.com/p/linears-secret-to-building-beloved-b2b-products
    - https://essays.uxdesign.cc/case-study-factory
```

## Why This Pattern Works

| Concern | Solution |
|---------|----------|
| **One curl per newsletter** | Single HTTP request yields both body text and link targets |
| **No JSON-LD body_html dependency** | Direct `<article>` tag extraction is reliable even when JSON-LD body_html is empty |
| **Link noise filtering** | Exclude substack infrastructure, social media, fonts, and tracking domains |
| **Deduplication** | `dict.fromkeys()` preserves order while removing duplicate links |
| **Paragraph threshold** | `len(clean) > 20` filters navigation/fluff; adjust to `> 50` for stricter filtering |

## Guardrails

- **Timeout**: Set `timeout=20` per URL. Substack pages are typically 150-350KB and load in 2-5s.
- **Paragraph count ≠ content depth**: Some newsletters (especially audio-first like Lenny's Podcast) may have 30+ paragraphs where 25 are sponsor messages and reference footnotes. Scan the first 10 paragraphs for editorial depth before committing to a take decision.
- **External link URL filtering is publication-specific**: Substack publishes may embed their own domain links for internal navigation (e.g., `lennysnewsletter.com/p/something`). These are the newsletter's own article links, not the curated external content — they need separate evaluation.
- **Cron mode**: Save to `/tmp/` and execute with `terminal python3 /tmp/script.py` (execute_code and pipe-to-interpreter are blocked in cron mode).

## When to Use

- **3+ Substack newsletters** in a single triage pass (typical morning pipeline)
- **Beehiiv/SemiAnalysis newsletters** need the curl approach for direct HTML access
- **Mixed format batch** (Substack + other platforms): process Substack newsletters with this script, handle others individually
