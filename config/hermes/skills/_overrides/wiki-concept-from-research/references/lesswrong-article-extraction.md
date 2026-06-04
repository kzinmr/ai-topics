# LessWrong Article Extraction Guide

## Problem
`web_extract` on LessWrong (www.lesswrong.com and alignmentforum.org) returns a pre-existing machine-generated **summary** rather than the full article body text. The summary is written in third person ("In this essay, the author explores...") and omits most of the detailed content.

## Detection
Check the extracted text: if it starts with phrases like "A Comprehensive Summary" or "In this article/essay, the author explores...", you've received a summary, not the original.

## Extraction Methods

### Method 1: browser_navigate + browser_snapshot (short articles, < ~5K chars)
```
browser_navigate(url)
browser_snapshot(full=true)
```
Use when the article fits in a single snapshot. The snapshot text is spread across paragraph StaticText elements.

### Method 2: browser_console (long articles, > 5K chars)
For mega-posts (19+ min reads, like the Waluigi Effect), the snapshot truncates at ~1500 DOM elements. Use JavaScript:

```python
# Step 1: Navigate and get first chunk
browser_console(expression="document.body.innerText.slice(0, 12000)")

# Step 2: Get subsequent chunks with offset
browser_console(expression="document.body.innerText.slice(12000, 24000)")
browser_console(expression="document.body.innerText.slice(24000, 36000)")
browser_console(expression="document.body.innerText.slice(36000, 50000)")
```

Adjust chunk size based on article length. Use the article's table of contents (visible in the page's TOC links) to estimate length:
- Short posts (< 5 min): 1-2 chunks
- Medium posts (5-10 min): 2-3 chunks
- Long posts (10-20+ min): 3-5 chunks

### Method 3: Check for a print/plaintext version
Some LessWrong posts have a `?format=text` or similar parameter. Not reliable but worth trying.

## What to Capture
The raw article should include:
- **Full article body text** — capture everything from the introduction through the conclusion
- **Comments/discussion** — skip unless a specific comment is mentioned by the user or is critical to understanding the article (e.g., a correction by the author in reply to a critique)
- **Epigraphs** — LessWrong posts often start with a relevant quote (e.g., Carl Jung at the top of the Waluigi Effect)

## Example
For the Waluigi Effect mega-post (644 upvotes, 188 comments):
- Chunk 1 (0-12000): Background, direct prompting, flattery & dialogue, Simulator Theory intro
- Chunk 2 (12000-24000): Limits of flattery, Derrida section, Waluigi Effect definition, 3 mechanisms, K-complexity argument
- Chunk 3 (24000-35000): Structuralist narratology, attractor state conjecture, Microsoft Sydney evidence, RLHF failure, jailbreaking method
- Chunk 4 (35000+): Conclusion, discussion/comments
