---
title: "Cohere Transcribe Arabic: Frontier Speech Recognition for Arabic Speakers"
source: "Cohere Blog"
url: "https://cohere.com/blog/transcribe-arabic"
scraped: "2026-07-08T06:00:55.026543+00:00"
lastmod: "2026-07-07"
type: "sitemap"
---

# Cohere Transcribe Arabic: Frontier Speech Recognition for Arabic Speakers

**Source**: [https://cohere.com/blog/transcribe-arabic](https://cohere.com/blog/transcribe-arabic)

Key takeaways
Transcribe Arabic achieves the highest accuracy for Arabic-language transcription among open-weights models.
It is designed to capture the nuances and dialectical richness of Arabic, while being fit for enterprise speech applications.
Human reviewers preferred Cohere Transcribe Arabic to Whisper in 96% of tests.
This is a proud advance in the region’s sovereign AI capabilities, bringing frontier performance to millions of Arabic-speakers.
Today, we are releasing Cohere Transcribe Arabic as an open-source model. Based on our
2B frontier Automatic Speech Recognition (ASR) model
released earlier this year, Cohere Transcribe Arabic is built for the realities of Arabic in business and developer settings: dialect variation, bilingual Arabic-English speech, code-switching, and domain-specific vocabulary.
It is the most accurate, open-source Arabic speech-to-text model to date, outperforming leading alternatives, including Whisper and OmniASR, across dialects and common speech patterns. It also delivers substantial gains over Cohere Transcribe on both Arabic and bilingual Arabic-English audio.
Cohere Transcribe Arabic is available under the
Apache 2.0 license
. Developers can
download the weights
and read our quickstart implementations on Hugging Face, or access the hosted model through the
Cohere API
or
Model Vault
.
One model, many voices
Arabic is a remarkably rich language in both script and speech. More than 300 million people speak Arabic as their mother tongue, across roughly 30 recognized varieties shaped by distinct cultural, regional, and historical contexts. Saudi Arabia alone is home to three major dialect groups and many more linguistic subgroups.
This diversity, however, heavily complicates efforts towards normalisation. While Modern Standard Arabic (MSA) provides a
de facto
common written standard, everyday speech varies significantly across dialects. Morphological differences, regional pronunciation, and code-switching — the use of Arabic and non-Arabic vocabulary in the same conversation, often in professional settings — make a single, uniform approach to communication difficult.
Image 1: a map of the Arabic-speaking world, highlighting some of the largest dialect families, their number of native speakers, and geographic distribution. Source: Ethnologue
The challenge is especially stark in the development of natural language technology, such as ASR. How do you train a model that preserves dialectal nuance while remaining useful beyond a particular market? The result has been a frontier-language gap: Arabic remains under-served by state-of-the-art AI systems while English continues to dominate model development and evaluation.
To help narrow that gap, Cohere embarked on a simple mission: build an enterprise-ready solution that lets Arabic users speak in their natural voice.
We started with Cohere Transcribe (launched in March with leading English-language accuracy and broad multilingual coverage) and trained it extensively on data spanning Arabic dialects, professional language, code-switching, and varied acoustic conditions.
The result is a new state-of-the-art solution in how Arabic speech is captured, ready for production use and openly available to all.
Unrivalled accuracy
Cohere Transcribe Arabic achieves the lowest average word error rate (WER) of any open-source model on the
Hugging Face Arabic ASR Leaderboard
, with a WER of 25.87. This is a 2.45-point improvement over the previous leader, Meta’s OmniASR-LLM-7B, and an 11-point improvement over OpenAI’s Whisper Large V3.
Dataset
Cohere Transcribe Arabic
OmniASR
7B-LLM
OpenAI Whisper Large V3
Cohere Transcribe
Average WER
25.87
28.32
36.86
30.67
SADA
37.47
41.61
55.96
60.11
Common Voice
5.82
9.75
17.83
8.17
MASC (clean)
15.54
19.69
24.66
8.66
MASC (noisy)
27.07
29.29
34.63
19.01
MGB-2
15.54
14.13
16.26
25.33
Casablanca
49.71
56.46
71.81
62.71
Image 2: the Open Universal Arabic ASR leaderboard as of 07.07.26. This public benchmark evaluates zero-shot multi-dialect generalization across six test sets spanning MSA, Egyptian, Gulf, Levantine, and Maghrebi dialects. See the
latest leaderboard and details
on the benchmark methodology.
The gains are broad-based. Cohere Transcribe Arabic delivers the best overall WER and ranks first on four of the six composite task sets. On Casablanca, for example, which evaluates conversational Arabic across eight dialects, it improves on OmniASR by nearly six points. On Common Voice, a crowd-sourced dataset covering 25 dialects, it reduces WER by more than two points from a low previous base.
The performance carried through to human evaluations with native Arabic speakers. Evaluators assessed transcription quality across three dimensions:
Overall accuracy
: How well the transcript captured both the form and semantic meaning of the audio
Dialect faithfulness
: Whether the model preserved the speaker’s dialect rather than converging toward Modern Standard Arabic
Robustness to code-switching
: Whether English terms were correctly transcribed in Latin script
Cohere Transcribe Arabic scored highest on all three dimensions compared with Whisper and Cohere Transcribe. In head-to-head evaluations, it was preferred over Whisper in 95.8% of tests.
Image 3: human preference evaluations of Arabic transcripts, according to overall quality, faithfulness to the dialect used, and ability to handle code-switching elements. Scores were rated on a scale of 1-5, with 5 marking the highest quality.
The model also improved significantly on Cohere Transcribe for English spoken with an Arabic accent, covering many workplace and second-language English use cases. Human evaluators preferred Cohere Transcribe Arabic over Cohere Transcribe in 77.2% of tests, and found it broadly comparable to Whisper on these inputs, with Cohere Transcribe Arabic preferred in 52.6% of tests.
Image 4: human preference scores of Arabic transcripts in pairwise comparisons. A score of 50% or higher indicates that outputs from Cohere Transcribe Arabic were considered more accurate on average.
Enterprise-ready
Cohere Transcribe Arabic is built for high-throughput serving in production environments, where performance under concurrent demand matters as much as model quality.
We optimized the system
around vLLM to handle high-volume speech workloads, even when audio inputs vary in length. Further updates to the runtime and model stack helped yield up to 2x higher throughput.
Overall, Cohere Transcribe Arabic achieves an RTFx (real-time factor multiple) score of 525 versus 146 for Whisper Large V3 and 66 for omniASR 7B-LLM.
Image 5: throughput (RTFx) vs accuracy (WER) plot for three leading models. RTFx (real-time factor multiple) measures how fast an audio model processes its input relative to real time. Source: Open ASR Leaderboard.
See for yourself
Read the following examples to see how Cohere Transcribe Arabic successfully handles code-switching and dialectic nuance within an enterprise setting.
Example 1: A common workplace dialogue about internal processes and human resources
Reference
English
انا ابغي اقدم طلب annual leave من نظام hris بس بصراحة ما عندي خبرة في استخدام النظام ممكن تشرحلي الخطوات بالتفصيل من وين ابدا وكيف ادخل علي النظام وايش هي القوايم اللي لازم اختارها ولين ما اوصل لمرحلة ارسال الطلب كمان ابغي اعرف اذا في اي وثايق لازم ارفقها مع الطلب
I want to submit an annual leave request through the HRIS system, but honestly, I don’t have any experience using it. Could you please explain the steps in detail? Where do I start? How do I access the system? What menus do I need to select? And how do I proceed until I reach the submission stage? Also, I’d like to know if there are any documents I need to attach to the request.
Model
Transcription
WER
Cohere Transcribe Arabic
انا ابغي اقدم طلب annual leave من نظام hris بس بصراحة ما عندي خبرة في استخدام النظام ممكن تشرح لي الخطوات بالتفصيل من وين ابدا كيف ادخل علي النظام وايش هي القوايم اللي لازم اختارها ولين ما اوصل لمرحلة ارسال الطلب كمان ابغي اعرف اذا في اي وثايق لازم ارفقها مع الطلب
5.9
Whisper Large V3
انا اريد ان اقدم طلب annual leave من نظام hris ولكن بصراحة لا املك خبرة في استخدام النظام ويمكن ان تشرح لي الخطوات بالتفصيل من اين ابدا وكيف ادخل علي النظام وما هي القوايم التي يجب ان اختارها ولين ما اوصل لمرحلة ارسال الطلب اريد اكتشاف اذا كان هناك اي وثايق يجب ان ارفقها مع الطلب
51.2
Cohere Transcribe
اقدم طلب من نظام اتش ار اي اس بصراحه ما عندي خبره في استخدام النظام وممكن تشرحلي الخطوات بالتفصيل من وين ابدا كيف ادخل عن النظام ولين ما اوصل لمرحله ارسال الطلب وكمان ابغي اعرف اذا في اي وثايق لازم ارفقها مع الطلب
41.2
Where Cohere Transcribe Arabic wins:
Maintains the Gulf dialect
: Cohere Transcribe Arabic preserves regional phrasing such as
انا ابغي
,
ما عندي خبرة
,
من وين ابدا
and
وايش هي القوايم
, while Whisper standardizes these into less speaker-faithful forms.
Preserves bilinguality
: Cohere Transcribe Arabic captures hybrid workplace vocabulary such as “annual leave” and “HRIS” exactly as spoken. By contrast, Cohere Transcribe either mistranslates these terms, for example rendering HRIS as
اتش ار اي اس
, or misses them entirely.
Example 2: Text involving more technical and domain-specific language
Reference
English
وش ال ai initiatives اللي شغالين عليها internally وكيف نستفيد من ال ai في تحسين ال customer experience وال network optimization كمان عطني examples من ال use cases الناجحة
What AI initiatives are you working on internally, and how can we leverage AI to improve customer experience and network optimization? Also, please provide examples of successful use cases.
Model
Transcription
WER
Cohere Transcribe Arabic
وش ال ai initiatives اللي شغالين عليها internally وكيف نستفيد من ال ai في تحسين ال customer experience وال network optimization اعطني examples من ال use cases الناجحة
6.9
Whisper Large V3
ما هي ال ai initiatives التي نعمل عليها internally وكيف نستفيد من ال ai في تحسين ال customer experience و network optimization وقد اعطينا ايضا مثالات من ال use cases الناجحة
31
Cohere Transcribe
وشي الايكات التي شغالين عليها انترنالي وكيف نستفيد من الايكات في تحسين الكustomer الاكسبيسون والنتورك اوبتيمازيون كما عدنا اي examples من اليوث كيس الناتج عنها
69
Where Cohere Transcribe Arabic wins:
Maintains technical accuracy
: Cohere Transcribe Arabic keeps enterprise terminology intact, including “AI initiatives”, “customer experience”, and “network optimization”, rather than translating or approximating these terms in Arabic.
Semantic completeness
: Cohere Transcribe Arabic retains the speaker’s original ask, such as ا
لناجحة use cases من ال examples اعطني,
instead of changing it into a less natural or semantically altered phrase, as Whisper does with
...وقد اعطينا ايضا مثالات
.
Making speech sovereign
Everyone deserves sovereignty when it comes to AI — no matter their mother tongue. It begins with control: over data, infrastructure, and your models.
Cohere Transcribe Arabic runs efficiently on consumer hardware, with no reliance on external APIs or cloud services, and is available under a permissive license. We’re giving developers open access to state-of-the-art speech AI in their own language and deployable on their own terms.
What’s next? We’re expanding enterprise-grade transcription capabilities and bringing support for new speech-powered applications for North users. This is all in collaboration with our regional partners and fast-growing local developer communities.
If you’d like to know how Cohere can make your AI capabilities more sovereign, please
get in touch
.
Start transcribing
Model weights are available today on
Hugging Face
. You can test the model beforehand in our
Hugging Face Space
.
Cohere Transcribe Arabic is also available through the
Cohere API
with free access subject to rate limits. Get a production key and refer to the
API documentation
to get started.
For managed production deployment
without
rate limits, provision a dedicated Model Vault from your
Cohere dashboard
. Pricing is calculated per instance-hour, with discounted plans available for longer-term commitments.
Let us know
We want to see what developers build with Cohere Transcribe Arabic. Share your projects with us on
X (@Cohere)
,
Discord
, or Hugging Face. These are also the best places to provide feedback and discuss new features or integrations.
Key contributors:
Shaun Cassini, Sebastian Vincent, Xiaolu Lu, Julian Mack, Dhruti Joshi, Pierre Richemond.
Blog
Written By
Cohere Team
Tags
Product Launch
AI for Developers
Company News
Share
AI isn’t a shortcut.
It’s how business gets ahead.
Contact sales
