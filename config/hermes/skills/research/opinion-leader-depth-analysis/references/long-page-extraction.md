# Long-Page Content Extraction (web_extract timeout fallback)

## Problem
`web_extract` on long-form pages (e.g., Gwern's 46k+ char essays) times out with:
> "LLM summarization timed out. To fix: increase auxiliary.web_extract.timeout in config.yaml"

Rather than chasing config changes, use browser-based extraction.

## Pattern: browser_console JS extraction

```
# Step 1: Navigate to page
browser_navigate(url)

# Step 2: Extract specific section via JS DOM query
browser_console with expression:
```
```js
(() => {
  const all = document.querySelectorAll('h2, h3');
  for (const el of all) {
    if (el.textContent.toLowerCase().includes('KEYWORD')) {
      let next = el.nextElementSibling;
      let text = ['## ' + el.textContent.trim()];
      let count = 0;
      while (next && count < 20) {
        const t = next.textContent.trim();
        if (t && !t.startsWith('Copy section link')) text.push(t.substring(0, 800));
        next = next.nextElementSibling;
        count++;
        if (next && (next.tagName === 'H2' || next.tagName === 'H3')) break;
      }
      return text.join('\n\n');
    }
  }
  return 'Not found';
})()
```

## Gwern.net specifics
- Gwern essays are often 30k–140k chars → guaranteed `web_extract` timeout
- Section IDs are available in the TOC (e.g., `#ambient-agency`)
- Use `browser_navigate(url#section-id)` then `browser_console` to extract
- Key interconnected essays: `turing-complete` ↔ `scaling-hypothesis` ↔ `unseeing`

## When to use
- Any page over ~20k chars where `web_extract` is likely to fail
- When you need a specific section, not the whole page
- When cross-referencing multiple long essays by the same author
