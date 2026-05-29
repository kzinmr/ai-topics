---
title: "AI-native product localization"
url: "https://sierra.ai/blog/ai-native-product-localization"
fetched_at: 2026-05-29T07:01:25.199519+00:00
source: "Sierra Blog"
tags: [blog, raw]
---

# AI-native product localization

Source: https://sierra.ai/blog/ai-native-product-localization

About a decade ago I was part of a 10-person team at Slack that localized the app. It took nine to 12 months. This year at Sierra I worked on a similar project, mostly solo, using AI coding agents. It took less than four months.
AI made the work faster and easier because what previously required a dedicated cross-functional team can be done by a single engineer orchestrating AI workflows across a large surface area.
In this post I’ll walk through how I approached the migration and what I learned.
Preparing an app for localization
Before I get to the AI side, it’s worth describing what preparing an app for localization involves, because “just run it through a translator” massively undersells the work.
Slack and Sierra’s Agent Studio were originally built with English text baked directly into the codebase. So text inside React components, API strings, pluralization helpers that just append an “s”, concatenated strings, and more all assume English is the only language.
Preparing an app for localization means systematically removing those assumptions across the stack.
Find user-facing strings and wrap them in localization functions
Restructure English-centric patterns and convert strings into
ICU MessageFormat syntax
that can support multiple locales correctly
Extract strings into translation files
Generate localized translations
Fix UI breakage caused by longer translated strings
Add linting and CI automation so new strings stay localized over time
Alongside this, you need locale preferences, locale-aware formatting, and infrastructure for propagating locale state across the stack.
Comparing projects and teams
Slack
— 9 to 12 months, 4 locales
3 backend engineers
3 frontend engineers
2 mobile engineers
1 engineering manager
1 product manager
QA & design
Sierra
— 4 months, 2 initial locales (Spanish and Japanese) with 4 more to come
While I still relied on native speakers, internal dogfooding, and human review for translation quality, language nuance, and overall UX correctness, fewer human eyes meant fewer Q&A catches — that’s a real tradeoff. For example, I still find untranslated strings hiding in less-visited parts of the app.
Also it’s not a perfect 1:1 comparison. My prior experience helped a lot. And the products have different surface areas and levels of maturity.
Cutting co-ordination overhead
AI alone doesn't make this work 10x faster — it’s the consequences: dramatically lower coordination. Historically, with projects like this you need to divide work, synchronize migrations, coordinate reviews, and manage QA across teams.
When one engineer can do most of that with AI assistance, so much of the overhead disappears.
The string wrapping journey
This was where AI saved hundreds of hours of tedious work.
At Slack we experimented with codegen approaches to automate parts of this process, but they were never reliable enough. Preparing strings for localization is more than mechanically wrapping text in i18n.t(). They often need to be rewritten, restructured to remove concatenation, or converted into ICU MessageFormat syntax.
It’s the kind of task AI excels at because it can understand intent, not just transform syntax. That said, it was still a lot of work. We had user-facing strings across more than 900 frontend files, and every AI-generated change still needed human review.
Here’s the progression I went through.
Approach 1: IDE agents
I initially started by asking Cursor to prepare individual files for localization.
The results were surprisingly good, but the workflow was inherently blocking and sequential. One file at a time was never going to scale across a large codebase.
Approach 2: Cloud agents
Next I tried cloud agents so multiple agents could work across many files simultaneously.
This improved throughput immediately, but introduced a new problem: tracking mistakes at scale.
The agents were generally very good at string wrapping, but there was still a small error rate — incorrectly concatenated strings, subtle ICU syntax mistakes, awkward possessives around variables.
There was also a workflow issue. Each agent generated its own pull request, which meant every batch of work created another review queue. As a solo engineer, I still needed human approvals, and waiting on dozens of narrowly scoped PRs quickly became a bottleneck.
I found myself constantly bouncing between agents, reviewing outputs, correcting mistakes, managing PRs, and updating the documentation to prevent the same failures in future runs.
Approach 3: The batch script
The real unlock was writing a batch script that called Claude directly, bypassing agent UIs entirely.
The script accepted either a list of files or a glob pattern, sent each file to the API alongside the localization skills documentation, and wrote the transformed result back to disk with configurable concurrency.
This turned the workflow into a repeatable pipeline and let me batch changes into larger, tightly scoped migrations that were much easier to review.
I processed files in batches of roughly thirty. After each batch, I manually reviewed every changed file — not because the AI was usually wrong, but because when it was wrong, I needed to catch the pattern before it propagated across hundreds more files.
After each review cycle, I’d collect the mistakes, have an agent explain why they happened, and then update the skills documentation with explicit guidance for future runs.
Over time the documentation evolved into a highly specialized playbook of edge cases, project-specific patterns, and common localization failures.
At that point the process became surprisingly efficient:
Run a batch
Review for pattern failures
Improve the instructions
Repeat
The linter: coevolution
Once the bulk of the string wrapping was done, I turned to building a linter rule that flagged user-facing strings which weren’t wrapped in t().
The linter itself was largely written by AI. I’d describe the behavior I wanted, the agent would generate or modify the rule, and the iteration loop was fast enough that I could refine it almost in real time.
The workflow eventually became:
Run the linter
Prepare flagged files using the batch script
Run the linter again
Investigate remaining warnings
Some remaining warnings were legitimate misses from the migration process, but most turned out to be false positives.
At that point I could point an AI agent directly at the prepared file, ask it which warnings were false positives, and then refine the linter to avoid flagging those patterns in future runs.
What emerged was an interesting form of coevolution. The migration pipeline and the linter were effectively cross-validating each other, with AI helping maintain both systems simultaneously.
Neither system was perfect independently, but together they produced a much higher-confidence signal about whether a file was actually localization-ready.
The important part was economic: because the cost of refining either system had become so low, I kept improving them instead of tolerating known inaccuracies and moving on.
The plot twist: Context windows
Once I was back in Cursor — iterating on the linter, handling edge cases, and continuing to refine the skills documentation — something unexpected happened: the error rate started going up again.
Even stranger, the mistakes were things already documented in the skills files — patterns the documentation explicitly told the AI not to use.
The answer turned out to be the context window.
The agent responsible for updating the skills docs had gradually been adding verbose explanations and large code examples for every failure we found. Over time, the documentation became large enough that the API was no longer reliably processing all of it. It would consume the beginning of the document and silently lose instructions buried later on. Unlike the batch script, which makes a fresh stateless API call per file, an interactive Cursor session accumulates state — conversation history, tool results, and file reads all stack up across turns.
The biggest technical lesson from the entire project was realizing that a feedback loop designed to improve AI output could eventually degrade it by making the context too large to effectively consume.
The fix required two changes.
First, I rewrote the documentation to be dramatically more concise: fewer words, fewer examples, and more signal per line.
Second, I split the docs into smaller focused files that could be selectively referenced instead of loaded all at once.
Rather than one giant document covering every edge case, the system became more like an index:
If you're working on panels, read panels-and-typing.md
If you're unsure whether something should be translated, read what-not-to-translate.md
The resulting documentation structure looked very different from traditional human-oriented docs. It was dense, highly scannable, and optimized for selective retrieval rather than sequential reading.
String context and descriptions
Another area where AI significantly changed the workflow was string descriptions.
One of the subtler problems in localization is context. The English word “close” could mean closing a dialog, ending a session, or describing proximity. Translators need enough information to know which interpretation is correct.
At Slack we handled this using @i18n comments above localized strings. During extraction, those comments were pulled into the translation files and shown to translators.
Initially I followed the same pattern at Sierra. Because we were using AI to help generate translations, the descriptions became even more important. I had AI generate the comments, which made them fast to produce — and also extremely verbose.
In most contexts AI verbosity is a bug. For localization context, it was often a feature, because translation models perform better when they have richer context about what a string actually means and how it’s used.
But during an early proof-of-concept review, I got feedback that the comments were making components much harder to read. UI files were becoming cluttered with metadata that humans didn’t actually need.
That feedback turned out to be important.
In practice, we were filling the codebase with comments that only AI would ever read, and only during translation generation. Once I realized that, the architecture started to feel backwards. If AI was generating the descriptions, and AI was the primary consumer of them, why did they need to live inline in the source code at all?
The process the agent used to generate descriptions was already straightforward: it read the surrounding code to infer the purpose and context of the string. That meant the descriptions could be generated dynamically during extraction instead of permanently embedded in the codebase.
So that’s what we built.
During extraction, the system records the file location and source position for every string. A follow-up enrichment step then sends a small window of surrounding code to Claude and asks it to generate a contextual description. That description gets stored directly in the translation files rather than alongside the application code.
The result was surprisingly clean. We could generate detailed contextual descriptions for translators without bloating the codebase with metadata humans didn’t actually need to read.
Conclusion
Going into this project, I expected AI to mostly help me move faster. What I didn’t expect was how much it would change the structure of the work itself.
The biggest gains didn’t come from AI magically writing perfect code. They came from reducing coordination overhead, shortening refinement loops, and making tedious engineering work cheap enough to continuously improve.
Over time, the workflow evolved into something that felt very different from traditional software development. Instead of manually transforming files, I was building systems that generated transformations, validated them, identified failures, refined instructions, and repeated the process. The work shifted from directly performing migrations to designing feedback loops.
At the same time, none of this eliminated the need for engineering judgment. AI helped execute the migration, but it didn’t design the architecture, identify systemic failure patterns, or decide what “good” looked like. In many ways those skills became even more important.
Working as a one-person team has tradeoffs. Human code reviews were sometimes a bottleneck, and there’s an obvious knowledge-silo risk when operating this way. Keeping documentation up to date — both for coding agents and future human engineers/archaeologists — becomes really important.
I also benefited enormously from having done this work before. Experience made it easier to distinguish cosmetic issues from consequential ones, recognize failure patterns early, and design workflows that would hold up under real use. AI accelerated the execution, but experience shaped the process.
Localization happened to be the project where I experienced these shifts most clearly, but I don’t think the lessons are specific to localization. I suspect a lot of software engineering workflows are about to be redesigned around similar patterns.
