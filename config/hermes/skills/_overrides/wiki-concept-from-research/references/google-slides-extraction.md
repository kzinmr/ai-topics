# Google Slides Extraction via HTML Presentation View

## When to Use
When the user provides a Google Slides URL (`docs.google.com/presentation/d/.../edit`) and `web_extract` on the edit URL returns only navigation chrome (toolbar, "HTML-weergave van de presentatie", login prompts) — no slide content.

This happens because Google Slides renders content client-side via JavaScript. `web_extract` sees the static HTML shell, not the rendered slides. And `browser_navigate` may be unavailable (Chrome not installed).

## Solution: Append `/htmlpresent` to the URL

Instead of:
```
https://docs.google.com/presentation/d/PRESENTATION_ID/edit?slide=id.SLIDE_ID
```

Use:
```
https://docs.google.com/presentation/d/PRESENTATION_ID/htmlpresent
```

Or with a specific slide:
```
https://docs.google.com/presentation/d/PRESENTATION_ID/htmlpresent?slide=id.SLIDE_ID
```

The HTML presentation view is a server-rendered, text-first version of the slides that `web_extract` can parse into structured markdown.

## What You Get

`web_extract` on `/htmlpresent` returns:
- Slide titles as markdown headings
- Bullet points and numbered lists
- Code blocks with syntax (language preserved from slides)
- Tables
- Speaker notes
- All text content from the presentation

What you DON'T get: images, diagrams, complex slide layouts. For visual/spatial information, you'd still need `browser_navigate` + `browser_vision`.

## Coverage Strategy

The `/htmlpresent` view may summarize or truncate some slides (especially for long presentations). To get more complete coverage:

1. **Start with the root**: `.../htmlpresent` — gets the full presentation in one extraction
2. **Try specific slides if truncated**: `.../htmlpresent?slide=id.SLIDE_ID` — focuses on a single slide
3. **Merge multiple extractions**: For very long presentations (50+ slides), extract root + a few specific slide sections and combine

In practice, the root `/htmlpresent` extraction is usually sufficient — the LLM summarizer returns a comprehensive synthesis.

### Long Presentation Fallback: Browser Console Chunking

**When to use**: `web_extract` on `/htmlpresent` returns `[... summary truncated for context management ...]` and the content cuts off mid-slide (e.g., at slide 25 of 36). This happens when the extracted markdown exceeds the LLM summarizer's context budget. The single-slide `/htmlpresent?slide=id.SLIDE_ID` URLs are unreliable (Google may return inaccessible errors).

**Procedure**:
1. `browser_navigate` to the `/htmlpresent` URL — loads the full server-rendered presentation
2. `browser_console` with `document.body.innerText.substring(0, 8000)` — first chunk
3. `browser_console` with `document.body.innerText.substring(8000, 16000)` — second chunk
4. Continue in 8000-char chunks until you reach the end
5. Combine all chunks into a single markdown document, reconstructing slide structure

This is the same technique documented in `references/lesswrong-article-extraction.md`. It works because the `/htmlpresent` page renders ALL slide text into `document.body.innerText` server-side — no JS-rendered content gaps. Browser tools see the full DOM; `web_extract` doesn't.

**Validated**: Benjamin Clavié's Tsukuba IR Talk (36 slides, May 2026). `web_extract` on `/htmlpresent` truncated at slide 25 with `[... summary truncated for context management ...]`. `browser_console` chunking recovered all 36 slides complete.

## Provenance

Discovered and validated May 2026 with Doug Turnbull's "Cheat at Search — LLM Query Understanding" presentation (33+ slides). Root `/htmlpresent` extraction returned comprehensive structured markdown covering all major sections (what is QU, why structured QU, 5 types, synonym extraction, category classification, cost optimization, caching, results).

## Comparison with Other Extraction Methods

| Method | Works? | Content Quality | Requires |
|---|---|---|---|
| `web_extract` on `/edit` URL | ❌ Navigation chrome only | — | — |
| `browser_navigate` + `browser_snapshot` | ✅ Full DOM | Good but noisy (includes UI chrome); truncated for 36+ slides | Chrome installed |
| `web_extract` on `/htmlpresent` | ✅ Structured text | Excellent — clean markdown; may truncate at ~25 slides | Nothing special |
| `browser_navigate` + `browser_console` chunking | ✅ Full text | Excellent — complete, no truncation; needs manual chunk merging | Chrome installed |
| `curl` on `/edit` URL | ❌ Empty body | — | — |

**Verdict**: `/htmlpresent` is the preferred first-try method. For presentations with 30+ slides where web_extract truncates, fall back to `browser_navigate` on `/htmlpresent` + `browser_console` chunking (8000-char windows). Only use `browser_vision` if you need actual images/diagrams.
