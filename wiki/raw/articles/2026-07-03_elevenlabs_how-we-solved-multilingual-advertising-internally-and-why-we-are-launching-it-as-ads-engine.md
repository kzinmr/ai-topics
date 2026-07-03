---
title: "How we solved multilingual advertising and built Ads Engine"
source: "ElevenLabs Blog"
url: "https://elevenlabs.io/blog/how-we-solved-multilingual-advertising-internally-and-why-we-are-launching-it-as-ads-engine"
scraped: "2026-07-03T06:01:00.870614+00:00"
lastmod: "2026-07-02T15:42:39.933Z"
type: "sitemap"
---

# How we solved multilingual advertising and built Ads Engine

**Source**: [https://elevenlabs.io/blog/how-we-solved-multilingual-advertising-internally-and-why-we-are-launching-it-as-ads-engine](https://elevenlabs.io/blog/how-we-solved-multilingual-advertising-internally-and-why-we-are-launching-it-as-ads-engine)

Blog
Company
How we solved multilingual advertising internally - and why we are launching it as Ads Engine
Written by
Aneri
Amin
Published
Jul 2, 2026
Listen
Listen to this article
0:00
0:00
0:00
1.0x
Contact Sales
On this page
Introduction
The problem
Video localization without visual localization
The static image bottleneck
What we built
The results
Winning the Google Ads Impact Award
From internal tooling to Ads Engine
Our paid marketing team built an internal workflow to localize ad campaigns across seven languages without adding headcount. It generated $3.78 million in incremental conversion value and won a 2026 Google Ads Impact Award - Google's most rigorous recognition of advertising performance, judged entirely on measurable business results. The internal product that powered it is now available to every brand and agency as Ads Engine.
The problem
Tim Davis, our Head of Paid Marketing, runs paid acquisition across every market ElevenLabs sells into. His team is four people, all English-speaking, managing search, display, and video campaigns across seven languages.
For most of the past year, the localization workflow was entirely manual.
For paid search, every keyword the team bid on was downloaded from the ad platform and translated column by column in a Google Sheet. Hundreds of rows. One language at a time. Translate to Spanish. Translate to Japanese. Pull the formula down. Upload the translated keywords back into Google Ads Editor or Bing Ads Editor.
That was the simple part. The real constraint was the ads. Google Search headlines have a hard 30-character limit including spaces. Descriptions get 90. When you translate a 28-character English headline like "AI First Call Center Solution" into Spanish, German, or any other language, it rarely fits. The translated version blows past the character limit, and the marketer has to manually shorten every headline - across every ad group, every language, every campaign.
When Tim's team checked character counts after translating a full set of headlines, the majority exceeded the limit. Each one required individual adjustment before it could go live. Beyond the time cost, the delay had a direct revenue impact. Every day spent reformatting headlines was a day the campaign was absent from that market. And the character-limit compliance was only the front door. Once the campaigns were live, the team still needed to optimize and manage performance across every language, multiplying the ongoing workload with no additional headcount.
Video localization without visual localization
For video ads, the audio side worked. Dubbing V2 preserved the original speaker's voice, tone, and pacing in each target language. But the visual layer stayed in English. Text overlays, product UI screenshots, on-screen copy - none of it was adapted. The videos sounded local but looked American.
The team understood the difference between translation and true localization. Localization accounts for cultural context - how colors carry different associations across markets, the distinction between Latin American Spanish and Spain Spanish, the reality that a black-and-white color palette designed for a developer audience in the US can carry connotations of mourning in Japan. There is a reason Diet Coke is sold as Coke Light in Latin America. But the production overhead to localize properly was significant, and the team was already stretched thin running campaigns in English.
When the team did invest in fully localized creative, adapting visuals, dubbing, and copy together, the results performed well. That work was handled through freelancers and ElevenProductions, our human-in-the-loop creative services team. It required dedicated production cycles that took weeks to turn around. The quality was high, but the process did not scale to every campaign in every language.
The static image bottleneck
Static display ads created the longest delays. When a creative performed well in English, Tim's team would identify it, translate the headlines and copy in the spreadsheet, and submit the translations to the design team to rebuild the image with localized text overlays.
Turnaround was three to five business days. Sometimes longer, depending on design bandwidth. During that window, the campaign ran in English markets and was completely absent from every other language. Competitors were in front of those users while we waited for a design queue to clear.
Every new high-performing creative triggered the same cycle: translate in the spreadsheet, brief the design team, wait for the rebuild, upload the new assets to each platform manually. Multiple tools were involved - the ad platforms, the spreadsheets, the creative measurement platform, the design request queue. Each handoff added days.
What we built
We started building internal tooling to compress the entire process. The goal was specific: if a creative is performing well in one language, the time between that signal and the localized version going live in every other market should be minutes, not days.
The tooling connected directly to our ad accounts, pulled existing creatives, handled translation with automatic character-limit compliance for search ads, adapted static images with localized text, dubbed video with Dubbing V2, and pushed finished assets back to the ad platform. The spreadsheet step, the design team request, the multi-day wait, the manual uploads across platforms - all of it collapsed into a single workflow.
Tim's team went from running English-only campaigns to running campaigns across seven languages. Same four people.
The results
The performance data was clear. Non-English campaigns delivered a 17.6% lift in conversions compared to English campaigns alone. Those localized campaigns generated $3.78 million in incremental conversion value at a 7.16 ROAS.
The team used native-language search demand data to identify where high-intent users were already searching for AI voice solutions in their own languages, then launched localized search and video campaigns to meet that demand. AI Max for Search extended reach into adjacent queries. The entire international expansion - seven languages, localized search, display, and video - ran on the same team that had previously been limited to English.
Winning the Google Ads Impact Award
The
Google Ads Impact Awards
are the highest recognition Google grants for advertising performance. Unlike creative awards judged on craft or concept, the Impact Awards evaluate on the hardest metric in the industry: measurable business outcomes. Conversion lifts, revenue generated, return on ad spend. The 2026 class includes campaigns from companies with dedicated international teams, full-service agency partnerships, and localization budgets many times the size of ours.
Our internal localization work was selected as a winner. The award recognized how a four-person, English-speaking team used AI-powered tools alongside our own product to expand into seven international markets profitably - delivering results that typically require significantly larger teams, dedicated localization vendors, and months of production infrastructure.
The campaign was led by Tim Davis with contributions from Kat Nguyen, Stavrianos Skalidis, and Tristan Hackney.
From internal tooling to Ads Engine
The award confirmed what the performance data had already shown us: the gap between where brands advertise and where their customers actually are is one of the largest sources of unrealized revenue in digital marketing. Most brands do not close that gap because the production process is too slow, too expensive, and too fragmented - not because the strategic case is unclear.
We solved that operationally for ourselves - and Google recognized the results as among the most impactful advertising work on its platform in 2026. The internal tooling that powered this work is now becoming a product we call Ads Engine, available inside ElevenCreative and through ElevenProductions.
Ads Engine connects to your ad accounts, localizes creatives across text, image, and dubbed video, respects platform specs automatically, and pushes finished ads back to where they run. It builds on the models where ElevenLabs has a genuine technical advantage - voice, dubbing, and multilingual audio - applied to the specific constraints of advertising production.
Localization is the entry point. What comes next is a continuous loop: performance data flowing back from running campaigns, fatigue detection surfacing when creatives need refreshing, and fresh variants generated without restarting the production process from scratch.
We built Ads Engine because we needed it to scale our brand. We are launching it because the problem is not ours alone.
