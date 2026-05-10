---
title: "[Deprecated] Pixtral Large"
source: "Mistral AI Blog"
url: "https://mistral.ai/news/pixtral-large"
scraped: "2026-05-10T01:20:24.399630+00:00"
lastmod: "2026-03-01T08:46:58.165Z"
type: "sitemap"
---

# [Deprecated] Pixtral Large

**Source**: [https://mistral.ai/news/pixtral-large](https://mistral.ai/news/pixtral-large)

Pixtral Large
Research
Pixtral grows up.
Nov 18, 2024
Mistral AI team
Heads up: this model is deprecated
Pixtral Large is no longer maintained and has been replaced by our latest, more powerful vision and multimodal models.
Explore our current vision capabilities
Pixtral Large in short:
Frontier-class multimodal performance
State-of-the-art on MathVista, DocVQA, VQAv2
Extends Mistral Large 2 without compromising text performance
123B multimodal decoder, 1B parameter vision encoder
128K context window: fits minimum of 30 high-resolution images
Use:
Try it on
le Chat
In our
API
as
pixtral-large-latest
Download it
here
Today we announce Pixtral Large, a 124B open-weights multimodal model built on top of Mistral Large 2. Pixtral Large is the second model in our multimodal family and demonstrates frontier-level image understanding. Particularly, the model is able to understand documents, charts and natural images, while maintaining the leading text-only understanding of Mistral Large 2.
The model is available under the Mistral Research License (MRL) for research and educational use; and the
Mistral Commercial License
for experimentation, testing, and production for commercial purposes.
Performance
We evaluate Pixtral Large against frontier models on a set of standard multimodal benchmarks, through a common testing harness. On MathVista, which evaluates complex mathematical reasoning over visual data, our model achieves 69.4%, outperforming all other models. To assess reasoning capabilities over complex charts and documents, we evaluate performance using ChartQA and DocVQA, where Pixtral Large surpasses GPT-4o and Gemini-1.5 Pro.
Pixtral Large also demonstrates competitive capabilities on MM-MT-Bench, outperforming all of Claude-3.5 Sonnet (new), Gemini-1.5 Pro and GPT-4o (latest). MM-MT-Bench is an
open-source
, judge-based evaluation intended to reflect real-world use cases of multimodal LLMs (see the
Pixtral 12B technical report
for details).
Finally, on the
LMSys Vision Leaderboard
, Pixtral Large is the best open-weights model by a substantial margin, surpassing the nearest competitor by nearly 50 ELO points. Pixtral Large also outperforms a number of proprietary models, such as GPT-4o (August '24).
Qualitative Samples
Multilingual OCR and reasoning...
Prompt:
I bought the coffee and the sausage. How much do I owe? Add a 18% tip.
Response:
To calculate the total amount you owe, including the 18% tip, follow these steps:
Calculate the cost of the coffee and the sausage:
2x Latte Macchiato: 2 * 4.50 CHF = 9.00 CHF
1x Schweinschnitzel: 22.00 CHF
Total cost for coffee and sausage: 9.00 CHF + 22.00 CHF = 31.00 CHF
Calculate the 18% tip:
Tip: 31.00 CHF * 0.18 = 5.58 CHF
Add the tip to the total cost:
Total amount owed: 31.00 CHF + 5.58 CHF = 36.58 CHF
So, you owe a total of 36.58 CHF.
Chart understanding...
Prompt:
When did things start to go wrong for dark dragon?
Response:
The training loss for the "dark-dragon-50" model starts to exhibit significant instability around the 10,000 steps mark. There is a noticeable spike in the loss value at this point, and the instability continues with another major spike around the 20,000 steps mark. These spikes indicate that the training process for the "dark-dragon-50" model began to encounter issues starting around the 10,000 steps mark.
And more...
Prompt:
Which companies use models made by Mistral AI?
Response:
The companies that use models made by Mistral AI, as shown in the image, are:
BNP Paribas
Brave
Cloudflare
CMA CGM
Front
One more thing...
Along with Pixtral Large,
Mistral Large
, our state-of-the-art text model, also gets an update. The model is available as
pixtral-large-latest
on our
API
, as well as for self-deployment as Mistral Large 24.11 on HuggingFace under the Mistral Research License (MRL) for research, or with a
commercial license
from Mistral AI for commercial use.
This newest model provides a significant upgrade on the previous Mistral Large 24.07, with notable improvements in long context understanding, a new system prompt, and more accurate function calling. The model is highly capable for RAG and agentic workflows, making it a suitable choice for enterprise use cases such as knowledge exploration and sharing, semantic understanding of documents, task automation, and improved customer experiences.
Mistral Large 24.11 will be available from our cloud provider partners soon, starting with Google Cloud and Microsoft Azure within a week.
Share this article
More from Mistral AI
News
Models
AI Services
