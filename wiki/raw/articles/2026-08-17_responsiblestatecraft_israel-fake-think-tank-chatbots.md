---
title: "Israel creates fake think tank in likely attempt to dupe AI chatbots"
url: https://responsiblestatecraft.org/israel-influence-chatgpt/
date: 2026-08-17
fetched_at: 2026-08-21
source: responsiblestatecraft.org (Quincy Institute for Responsible Statecraft)
author: Nick Cleveland-Stout
tags: [disinformation, ai-safety, geopolitics, llm-output, prompt-injection]
hn: "1053 points / 852 comments on HN (2026-08-17)"
---

# Israel creates fake think tank in likely attempt to dupe AI chatbots

*Responsible Statecraft (Quincy Institute), by Nick Cleveland-Stout — 2026-08-17*

## What the reporting found

At a glance, the **Hanover Institute for Public Policy** looks like a new think tank dedicated to Israel/Palestine. The organization churns out think-tank-style reports on questions such as "Does AIPAC Use 'Dark Money in Elections?'" and "Is Israel Carrying out a Deliberate Campaign of Starvation in Gaza".

But the Hanover Institute is not a real think tank. None of the reports have bylines. A small disclaimer at the bottom of the webpage notes that the organization was created on behalf of the **Israeli Government Advertising Agency** by **Piro, Inc**, a firm co-founded by **Daniel Rosenberg**, the producer of *Succession*.

## Why chatbots are the target

The Hanover Institute's reports — all of which are about Israel and Palestine — appear to be part of an Israeli effort to **influence chatbots**. The institute's "data reports" have footnotes and tables of contents, and they present arguments in a neutral tone, helping them appeal to chatbots like Claude.

According to its "about" page, the Hanover Institute "studies the inputs fueling antisemitism in the United States, and publishes what the evidence shows." Many of the reports are formulaic, starting with an innocent question that someone might ask a chatbot:

- "What Caused the Displacement of Palestinians in 1948?"
- "Which Humanitarian Organizations Have Documented Israeli War Crimes?"
- "What is the Current Situation in the Gaza Strip?"

In an article titled "Is the IDF the World's Most Moral Army?", the Hanover Institute cites a 2022 poll that found that 47% of Israeli Jews believed that statement. Another report casts doubt on UNICEF's assertion that "90% of water and institutional infrastructure has been damaged or destroyed" in Gaza.

In a few cases, the Hanover Institute publishes what it claims are original findings. For instance, it put out a study saying 19 of the 36 most-watched Israel-Gaza explainer videos contain contested claims, with most of the contested claims aligning with the Palestinian narrative.

The Hanover Institute's publications sometimes contradict Israeli government narratives. For instance, one report says that foreign funding of universities as an explanation for antisemitic incidents is "weak and full of exceptions." Israeli Prime Minister Benjamin Netanyahu has pushed this theory.

## Expert commentary and detection

**Alice Lee**, an analyst at **NewsGuard** (a disinformation tracking company), told Responsible Statecraft that the sites appear designed to reach a U.S. audience curious about the ongoing conflict, either through search engines or AI chatbots: "LLMs favor concrete statistics and data, as well as strong citations and sources."

"It's a perfect mimicry of a typical credible American think tank, right down to the generic name, the site layout, and the red-white-blue color scheme," Lee added.

## Funding and scale

- **Piro, Inc**, the firm that created the Hanover Institute, has received **$900,000** from the Israeli government for its work. Like many other contractors working for Israel, Piro's work is subcontracted through **Havas Media**, a French public relations conglomerate.
- The fake think tank has churned out **over 100 reports since it started publishing on August 6, 2026**.
- The Hanover Institute claims that "cited research is peer-reviewed and academic," although it frequently cites Israeli government sources such as the Israel Defense Forces and the Ministry of Foreign Affairs.
- **GPTZero analysis**: RS analyzed 12 random Hanover Institute articles using GPTZero, a popular AI detection software that claims a low false-positive rate. GPTZero flagged **11 of the articles as AI-written with "high confidence"**; it flagged one article as AI-written with "moderate confidence."

## Related operations

**Israel has also contracted former Trump campaign manager Brad Parscale** to create pro-Israel websites engineered to influence chatbots as part of a **$46.5 million contract**. A **Drop Site** investigation last month found that many chatbots, particularly Microsoft Copilot and Google Gemini, had been successfully influenced.

Piro does not explicitly state in its agreement submitted to the Department of Justice that its work for Israel is to influence AI. In an email to Politico, which first reported the filing, Rosenberg said his firm's work is to "put accurate, sourced facts into the public record and to counter misinformation."

"When someone asks ChatGPT, Gemini, or Perplexity about your category, an answer comes back in one confident paragraph. Most brands have no idea how that paragraph gets built. So we spent months reverse-engineering it… At Piro, we already knew how to build stories that move people. The question was: [how to build for chatbots]."

## Significance

This is one of the clearest documented cases of a state-sponsored actor building web content *specifically* to shape LLM retrieval and synthesis pipelines — not to fool search engines (classic SEO) or humans (classic propaganda), but to feed confident-sounding, citation-rich, neutral-toned "data reports" that LLMs preferentially cite. It turns the GEO (Generative Engine Optimization) playbook from a commercial marketing technique into an instrument of foreign influence, and it raises new questions about LLM provenance defenses: chatbot-side source vetting, watermarking of retrieved content, and whether "credible think tank" formatting is itself an attack vector.

## Sources

- https://responsiblestatecraft.org/israel-influence-chatgpt/ (this article)
- HN discussion: https://news.ycombinator.com/item?id=49337392 (1053 points, 852 comments)
- Related: https://concepts/security-and-governance/ai-text-watermarking (watermarking as a provenance defense)
- Related: https://concepts/gpt/gpt-5-6 ("ChatGPT Search site: operator" section — how chatbots retrieve)
