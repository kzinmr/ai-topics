# Pitfall: delegate_task Subagent Content Hallucination

## Problem

When `delegate_task` is used to fetch and extract web article content, the subagent may **hallucinate a plausible-sounding summary** instead of actually parsing the fetched HTML. The subagent reports "content extracted successfully" but the returned text is fabricated — matching the expected topic but with invented section headings, made-up data points, and wrong author attributions.

### Observed Case (June 2026)

- **Task**: Extract full article text from `https://jacobxli.com/blog/2026/machine-studying/`
- **Subagent behavior**: Reported "I'll fetch the article" then returned a fabricated summary with plausible-sounding but completely wrong section headings and invented content
- **Actual article**: By Jacob Xiaochen Li, Rick Battle, Omar Khattab (MIT CSAIL/Broadcom) — a research blog about StudyBench benchmark, Qwen3.5-9B experiments, three paradigms (CPT, SFT, cheatsheet)
- **The hallucinated version** had different sections, different arguments, and different framing

## Root Cause

The subagent's `web` tool may return a page title + description but not the full HTML. The LLM then fills in the gaps with plausible content based on the URL, title, and any partial content it received. The `completed` status and "no issues" self-report mask the hallucination.

## Detection

1. **Always fetch raw HTML yourself first** (via `curl` or `read_file` on a downloaded copy) before relying on delegate_task summaries
2. **Cross-check author names**: If the subagent returns generic attributions but the HTML has `<meta name="author">` tags, the subagent didn't parse the HTML
3. **Check section count**: Compare the subagent's section list against `<h2>`/`<h3>` tags in the raw HTML
4. **Look for data points**: If the article has specific numbers (benchmarks, dates, percentages) and the subagent's summary omits all of them, it's likely hallucinated

## Workaround Pattern

1. **Fetch the HTML yourself** via `curl -sL <url>` and save to `/tmp/`
2. **Parse locally** with Python (strip tags, extract `<d-article>` or `<article>` content)
3. **Use delegate_task only for secondary research** (author background, related pages) — not for primary content extraction
4. **If delegate_task is the only option**, verify its output by cross-referencing with `<meta>` tags, heading structure, and JSON-LD data in the raw HTML

## Why This Matters for Wiki Quality

Ingesting hallucinated content creates corrupted wiki pages with wrong claims, wrong author attributions, and wrong section structures. The pre-commit content regression hook catches size regressions but not content hallucination. The only defense is verification against the raw source.
