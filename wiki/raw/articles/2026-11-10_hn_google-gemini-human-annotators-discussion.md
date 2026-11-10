---
title: "Google Gemini routes personal Drive files and emails to human annotators (HN discussion)"
url: "https://news.ycombinator.com/item?id=50429426"
source: "https://github.com/thisisme6598/gemini_files/"
fetched_at: 2026-11-10T12:15:00+00:00
type: hn-discussion
tags: [raw, hn]
sha256: b367a1975a9d5653543a6f2ff2311f24bcc36eb20939500b1db9306f74e004d9
---

# Google Gemini routes personal Drive files and emails to human annotators

HN item 50429426, 632 pts / 132 comments. Primary artifact: GitHub repo
https://github.com/thisisme6598/gemini_files/ (README reproduced below), documenting a quiet reversal of
Google's 2023 "not seen by human reviewers" promise for Gemini Workspace extensions.

## README summary (from the repo)

In 2023 Google launched Gemini Workspace extensions with an explicit promise: personal content from Gmail,
Docs, and Drive "is not seen by human reviewers". Google has quietly reversed this commitment. Under updated
Google Help Answer 16836988 and an October 16 edit to their 2023 blogpost, Google explicitly confirms that
connected Drive/email is routed into human review pipelines, warning reviewers "may just see the email or
file" and advising users not to connect apps containing confidential information.

Crucially, testing demonstrates ingestion occurs autonomously in background conversation without explicit
@Drive or @Gmail tags, and the payload capture is probabilistic. When chatting with consumer Gemini with
Connected Apps enabled, ambient mentions of personal topics (trips, bills, names, reservations) autonomously
trigger background Workspace lookups. Because LLM tool-calling and context injection are probabilistic, a test
query yields one of four scenarios:

1. Zero Retrieval: Connected Apps tool not triggered; no personal data pulled (likely if model weights or prior conversation history can resolve the query).
2. Metadata / Generic Summary: e.g. "You have 3 emails regarding your flight".
3. Partial Unredacted Extraction: a 2-4 sentence exact quotation, frequently including sensitive PII, account details, or specific figures.
4. Full-File Ingestion: complete unredacted document/email text into session context.

Observing State 1 or 2 once does not disprove the pipeline — it is a single draw from a nondeterministic system.

## HN discussion highlights

- [rustyhancock] "Really frustrating that our privacy eroded to the point anyone would think this is reasonable. But it does explain some conversations with Gemini when I wonder why it's talking about particular things… uncannily tuned to the email I just got. No mention of 'I just read your emails'."
- [reasonableklout] "very surprising considering Drive and email are products that have had rock solid trust for decades, and Google is not OpenAI!"
- [realsarm] counters: Google was always privacy-invasive; links prior thread (item 40965892).
- [xnickb] / [sdoering] self-hosting reactions: Immich for Google Photos, Nextcloud for Drive, some considering self-hosted email — the privacy incident as a driver of local/self-hosted adoption.
- [sumeno] "Only if you connect it to Gemini. If you're using a local LLM you probably aren't connecting your Google Drive to Gemini."
- [nunez] notes there are still no feasible full alternatives to Google's suite.
