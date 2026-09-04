# System Card / Safety Document Ingestion

Pattern for ingesting AI model system cards, model cards, and safety documentation into the wiki.

## Sources

| Provider | Hub URL | Format |
|---|---|---|
| OpenAI | deploymentsafety.openai.com | Astro web pages (SSR) |
| Anthropic | anthropic.com/system-cards | PDF links |
| Google DeepMind | storage.googleapis.com/deepmind-media/ | PDF links |

## OpenAI Deployment Safety Hub

The hub at `deploymentsafety.openai.com` renders system cards as multi-page Astro documents. Each card has a root page (e.g., `/gpt-5`) with sub-pages for each section.

### Content Extraction

Astro pages have content in `<p>` tags after removing `<script>` and `<style>` blocks:

```python
import re
html = open('page.html').read()
html = re.sub(r'<script[^>]*>.*?</script>', '', html, flags=re.DOTALL)
html = re.sub(r'<style[^>]*>.*?</style>', '', html, flags=re.DOTALL)
paras = re.findall(r'<p[^>]*>(.*?)</p>', html, re.DOTALL)
clean = [re.sub(r'<[^>]+>', ' ', p).strip() for p in paras if len(re.sub(r'<[^>]+>', '', p).strip()) > 50]
```

### Bulk Fetch

All cards can be fetched with curl (the hub is SSR, not SPA):
```bash
curl -sL "https://deploymentsafety.openai.com/${slug}" -o /tmp/${slug}.html
```

### Sitemap

The sitemap at `/sitemap.xml` lists all sub-pages per system card (each section is a separate URL).

### RSS

The RSS feed at `/posts.xml` is currently empty (editorial posts only).

## File Naming

System card pages: `gpt-{model-name}-system-card.md` under `concepts/gpt/`
Model card pages: `gpt-{model-name}-model-card.md` (when labeled "model card" by provider, e.g., gpt-oss)

## Content Structure

Each system card concept page should include:

1. **Model Overview** — architecture, variants, training approach
2. **Key Benchmarks** — tables with numbers
3. **Preparedness/Framework Assessment** — risk levels per category
4. **Safety Evaluations** — disallowed content, jailbreaks, hallucinations, fairness
5. **External Assessments** — METR, Apollo, Pattern Labs, government evaluators
6. **Safeguards** — technical mitigations, deployment controls
7. **Red Teaming Results** — if available
8. **Significance** — what this card established/changed
9. **See Also** — cross-references to related pages

## Pitfalls

- **403 on openai.com**: Main openai.com pages (GPT-4, GPT-4V, GPT-4o-mini system cards) return 403 from curl due to Cloudflare protection. Use browser-based delegation or check if the page is available on the deployment safety hub instead.
- **PDF availability**: Not all system cards have PDFs on the CDN. The deployment safety hub has web versions; PDFs may be at different URLs. Try `cdn.openai.com/papers/` but expect 404s.
- **Duplicate pages**: If a concept page already exists for a model (e.g., `gpt-5-5.md`), the system card page should be a separate file (`gpt-5-5-system-card.md`) and cross-link to the model page.
- **Hub index updates**: After creating all system card pages, update the hub page (e.g., `gpt-deployment-safety-hub.md`) with a table linking to all individual pages.
- **SCHEMA tags**: System card pages need `system-card` tag. Check SCHEMA.md has it before committing. Common missing tags: `preparedness-framework`, `domain-specific`, `safe-completions`, `deliberative-alignment`.
