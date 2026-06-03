---
title: "Microsoft's new MAI models"
url: "https://simonwillison.net/2026/Jun/2/microsofts-new-models/#atom-everything"
fetched_at: 2026-06-03T07:01:40.583100+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# Microsoft's new MAI models

Source: https://simonwillison.net/2026/Jun/2/microsofts-new-models/#atom-everything

Microsoft
announced two new text LLMs
this morning -
MAI-Thinking-1
(reasoning, 1T parameters, 35B active, available to "select early partners") and
MAI-Code-1-Flash
(137B Parameters, 5B active, "purpose-built for GitHub Copilot and VS Code to deliver high performance and lower cost [...] rolling out to GitHub Copilot individual users in Visual Studio Code"). I've not been able to try either of them just yet.
It's very interesting to see Microsoft releasing models with such low parameter counts, especially given how expensive larger models are to access right now. They claim MAI-Thinking-1 "is preferred to Sonnet 4.6 in our blind human side-by-side evaluations", which is impressive for a 35B model seeing as I frequently run models larger than that on my own laptop.
(UPDATE: I got this entirely wrong, see note below.)
Also
of note
:
We trained [MAI-Thinking-1] from the ground up on enterprise grade, clean and commercially licensed data, without distillation from third-party models.
And for
MAI-Code-1-Flash
as well:
It is built end-to-end by Microsoft using clean and appropriately licensed data.
I would
very much
like to learn more about this "appropriately licensed" data! Could these be the first generally useful code-specialist models that didn't train on an unlicensed dump of the web? (
Update
: the answer is no, see note below.)
Update
: My initial published notes got the size of the models wrong. I misread Microsoft's announcements and interpreted the MoE active parameter count as the total parameter count, but the
model card for MAI-Code-1-Flash
lists it as 137B with 5B active and the
MAI-Thinking-1 technical paper
reveals it to be a 1T model with 35B active.
I deeply regret this error.
Update 2
: That technical paper describes the training data in some detail from page 80 onwards. It has the same licensing problems as all of the other major LLMs: it's trained on a crawl of the public web:
The majority of our web HTML corpus comes from a proprietary crawl. After initial page discovery and selection, approximately 1.2 trillion pages are crawled and parsed. [...] In addition to Microsoft standard policy Sec. 2.4, we apply UT1 block list (Prigent, 2026) to remove adult content and piracy-related domains. In all, this filtering reduces the corpus from 1.2 trillion pages to 794 billion pages. Given the prevalence of AI-generated content on the web, we also score pages with a proprietary AI-content detection model and use manual inspection to identify domains with extensive AI-generated content; those domains are filtered out of the training corpus.
[...]
We process Common Crawl with the same pipeline. [...] After filtering, deduplication, merging with the proprietary web corpus, and a final round of exact-URL and content-level fuzzy deduplication, the Common Crawl portion contains 24.2 billion pages.
I did not cover this one at all well, which is somewhat ironic since I was at the Microsoft Build conference when I wrote this up! I'm sorry for not digging deeper before publishing my initial notes.
