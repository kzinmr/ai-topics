# AINews Substack Post Extraction (2026-08-20)

## Context

Newsletter-triage run `20260820T101038Z`. AINews post "Death of Params: Z.ai CEO Jie Tang on GLM 5.3 and the new Post-training Scaling Law" needed body text extraction for triage classification.

## Resolution

1. `curl -sL -o /dev/null -w '%{url_effective}' 'https://open.substack.com/pub/swyx/p/ainews-death-of-params-zai-ceo-jie'` → `https://www.latent.space/p/ainews-death-of-params-zai-ceo-jie?triedRedirect=true`
2. `curl -sL 'https://www.latent.space/p/ainews-death-of-params-zai-ceo-jie' > /tmp/ainews_post.html`
3. Python extraction:
```python
import re
html = open('/tmp/ainews_post.html').read()
html = re.sub(r'<(script|style)[^>]*>.*?</\1>', '', html, flags=re.DOTALL)
match = re.search(r'class="body[^"]*".*?</div>\s*</div>', html, re.DOTALL)
if match:
    text = re.sub(r'<[^>]+>', ' ', match.group())
    text = re.sub(r'\s+', ' ', text).strip()
```

## Outcome

Yielded the key quote: *"Parameter count is only meaningful alongside three others — how much data you have, where you intend to spend your compute, and who will run the model, under what conditions."* Sufficient for triage (★★★★☆ take → update existing `concepts/glm-5-3.md`).

## Notes

- The `class="body[^"]*"` regex matches Substack's `body markup` class. The `.*?</div>\s*</div>` tail is greedy enough to capture multi-paragraph content but stops at the post's closing divs.
- For paywalled posts, this still yields the free preview (lede + first X post embed). For AINews, the free preview typically contains the headline claim + 1-2 X embeds with key quotes — sufficient for triage classification.
- `og:description` in the HTML head gave "Every lab CEO is on X now" — a useful framing signal even when body extraction is partial.
- No `execute_code` needed (blocked in cron) — raw `curl` + inline Python via `terminal` suffices.
