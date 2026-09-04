# Sitemap-Monitor Hugging Face Blog Blind Spot

**Discovered**: July 2026 (Inkling model release)
**Symptom**: `huggingface.co/blog/thinkingmachines-inkling` was NOT captured by sitemap-monitor (06:00 UTC) even though `together.ai/blog/together-ai-brings-thinking-machines-labs-new-model-inkling` and `modal.com/blog/inklibg-by-thinking-machines-labs` WERE captured.

## Why It Matters

When a newsletter (especially AINews) includes a Hugging Face blog link as the primary technical reference for a model release, the sitemap-monitor's failure to capture it means the newsletter link represents **genuinely new content** that has not been captured by any other pipeline.

## Detection

Before marking a newsletter-discovered HF blog link as already-captured (based on the assumption that "sitemap-monitor ran first"), verify:

```bash
# Check if the specific HF blog path exists in raw articles
ls ~/wiki/raw/articles/ | grep -i "huggingface.*think\|huggingface.*inkling"
```

If absent, the HF blog is:
1. A canonical technical source not captured by any pipeline
2. NOT supplementable by infrastructure blogs (Together AI, Modal) which cover serving details only
3. Likely to contain core model architecture details, training methodology, and evaluation results

## Action When Detected

When a newsletter-discovered model release has:
- ✅ HF blog link (canonical tech source) — **NOT captured**
- ✅ Infrastructure partner blogs (Together, Modal) — **captured by sitemap-monitor**
- ✅ Newsletter aggregation (AINews) — **accessible**

The newsletter aggregation becomes the **primary enrichment source** (it synthesizes the HF blog + infrastructure + community reactions). The HF blog is a secondary reference for verification.

## Root Cause

Hugging Face blog posts follow the URL pattern `huggingface.co/blog/{slug}`. This is a blog hosted on HF's infrastructure, not on the model-producing company's own domain. Sitemap-monitor's target list may include `huggingface.co` but the blog section's sitemap may be structured differently from standard blog sitemaps, or HF may not publish a standard `sitemap.xml` for the blog section.
