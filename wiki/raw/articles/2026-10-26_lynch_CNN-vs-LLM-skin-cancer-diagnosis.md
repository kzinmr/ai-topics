---
title: "CNN-vs-LLM-skin-cancer-diagnosis"
source: https://lynchlab.net/llm-skin-cancer
publisher: lynch
captured: 2026-10-26
type: article
status: full
sha256: 4d88eb6f2824b65b0a0b0b1aed75b61a14591d8cf29ccbbe4b03102fc1d590b0
---

# CNN-vs-LLM-skin-cancer-diagnosis

Source: https://lynchlab.net/llm-skin-cancer
Publisher: lynch
Captured: 2026-10-26

A 10-year-old CNN outperforms frontier LLMs for skin cancer diagnosis | Lynch Lab 

 Lynch Lab 

 A 10-year-old CNN outperforms frontier LLMs for skin cancer diagnosis 
 I am a dermatologist. I tested the ability of GPT-6 Astra and Claude Fable 5.1 to diagnosis skin cancer and found that they were less accurate than I expected. I compared to a 10-year old CNN and to my surprise found that this was superior. 

 By Dr Magnus Lynch &middot; 25 October 2026
 &middot; 5 min read

 This is a melanoma. 

 Figure 1. Invasive melanoma on the ear, under 0.8 mm thick. Both LLMs called it a seborrhoeic keratosis and said it could be discharged. The CNN called it a melanoma. Clinical photograph on the left, dermoscopic image on the right. Images: MILK10k , MILK study team, CC BY-NC. 

 I showed these two images - a clinical photograph and a dermoscopic (skin microscope) image - to GPT-6 Astra and Claude Fable 5.1, two of the most capable AI models available in October 2026. Both said it was a seborrhoeic keratosis, a harmless warty growth, and that the patient could be discharged. I then showed them to fine-tuned version of Inception v3, a convolutional neural network (CNN) first published by Google in 2015 and fine-tuned here on public dermatology images. The CNN got the right answer based on the dermoscopy view. 
 It was one of 200 biopsy-proven lesions I gave to all three. The CNN named the right diagnosis (out of 6 possiblities) for 125 of them (62%). The two frontier LLMs named it for 84 and 85 (42%). A ten-year-old network, fine-tuned for about twenty minutes, beat both of them at recognising skin cancer. 
 The test # 
 The lesions come from MILK10k , a public dataset released through the International Skin Imaging Collaboration in 2025, in which each lesion is photographed twice: a clinical close-up and a dermoscopic image taken through the illuminated magnifying lens dermatologists use. I drew 200 lesions at random, all confirmed by histopathology: 

 100 that should not be discharged: 30 melanomas, 25 basal cell carcinomas, 25 squamous cell carcinomas (including Bowen&rsquo;s disease) and 20 actinic keratoses. 
 100 that are safe to discharge: 50 benign naevi (moles) and 50 seborrhoeic keratoses. 

 Every lesion was biopsied, including the benign ones, so these are harder to diagnose: a mole that somebody decided to cut out is one that worried a clinician. 

 Basal cell carcinoma on the trunk of a 75-year-old man. All three models answered correctly. 
 Invasive melanoma under 0.8 mm thick, with very little pigment. GPT-6 Astra called it a basal cell carcinoma with 95% confidence. Claude Fable 5.1 and the CNN called it a melanoma. 
 Seborrhoeic keratosis on the leg. Both LLMs called it an actinic keratosis and the CNN a squamous cell carcinoma: all three were wrong, though all three would have kept it rather than discharge it. 
 Figure 2. Three more of the 200 test lesions. Clinical photograph on the left, dermoscopic image on the right. Images: MILK10k , MILK study team, CC BY-NC. 

 The LLMs were given both images and nothing else, and asked, as a clinician might use them, for the most likely of the six diagnoses (or &ldquo;unsure&rdquo;), a confidence, a second choice, and whether the lesion could be safely discharged with no treatment, biopsy or follow-up. Both models got the same prompt at default settings, and neither refused a case. 
 The CNN is deliberately not state of the art. I used Inception v3 pretrained on everyday photographs and then fine-tuned all layers on 68,011 dermoscopic and clinical images from the ISIC Archive on a single H100 GPU. These 200 test lesions, and every other photograph of the same lesion or patient, were removed from its data (including the validation set) before training, so it had never seen them, and they were not used to choose the model or set its threshold. It scored both images of each lesion, combined them with most of the weight on the dermoscopic image, and chose from the same six diagnoses. 
 You can try the CNN yourself . Remarkably the model is small enough to run entirely in a phone browser using WebGPU. Nothing is uploaded, and its random sample button draws from these same 200 lesions. 
 Diagnosis: 62% against 42% # 

 GPT-6 Astra Claude Fable 5.1 Inception v3 All 200 lesions GPT-6 Astra - All 200 lesions: 84 of 200 (42%) 84/200 GPT-6 Astra - All 200 lesions: 84 of 200 (42%) Claude Fable 5.1 - All 200 lesions: 85 of 200 (42%) 85/200 Claude Fable 5.1 - All 200 lesions: 85 of 200 (42%) Inception v3 - All 200 lesions: 125 of 200 (62%) 125/200 Inception v3 - All 200 lesions: 125 of 200 (62%) By true diagnosis Melanoma GPT-6 Astra - Melanoma: 8 of 30 (27%) 8/30 GPT-6 Astra - Melanoma: 8 of 30 (27%) Claude Fable 5.1 - Melanoma: 11 of 30 (37%) 11/30 Claude Fable 5.1 - Melanoma: 11 of 30 (37%) Inception v3 - Melanoma: 13 of 30 (43%) 13/30 Inception v3 - Melanoma: 13 of 30 (43%) BCC GPT-6 Astra - BCC: 25 of 25 (100%) 25/25 GPT-6 Astra - BCC: 25 of 25 (100%) Claude Fable 5.1 - BCC: 18 of 25 (72%) 18/25 Claude Fable 5.1 - BCC: 18 of 25 (72%) Inception v3 - BCC: 24 of 25 (96%) 24/25 Inception v3 - BCC: 24 of 25 (96%) SCC GPT-6 Astra - SCC: 12 of 25 (48%) 12/25 GPT-6 Astra - SCC: 12 of 25 (48%) Claude Fable 5.1 - SCC: 5 of 25 (20%) 5/25 Claude Fable 5.1 - SCC: 5 of 25 (20%) Inception v3 - SCC: 16 of 25 (64%) 16/25 Inception v3 - SCC: 16 of 25 (64%) Actinic keratosis GPT-6 Astra - Actinic keratosis: 10 of 20 (50%) 10/20 GPT-6 Astra - Actinic keratosis: 10 of 20 (50%) Claude Fable 5.1 - Actinic keratosis: 12 of 20 (60%) 12/20 Claude Fable 5.1 - Actinic keratosis: 12 of 20 (60%) Inception v3 - Actinic keratosis: 9 of 20 (45%) 9/20 Inception v3 - Actinic keratosis: 9 of 20 (45%) Naevus GPT-6 Astra - Naevus: 16 of 50 (32%) 16/50 GPT-6 Astra - Naevus: 16 of 50 (32%) Claude Fable 5.1 - Naevus: 33 of 50 (66%) 33/50 Claude Fable 5.1 - Naevus: 33 of 50 (66%) Inception v3 - Naevus: 37 of 50 (74%) 37/50 Inception v3 - Naevus: 37 of 50 (74%) Seb. keratosis GPT-6 Astra - Seb. keratosis: 13 of 50 (26%) 13/50 GPT-6 Astra - Seb. keratosis: 13 of 50 (26%) Claude Fable 5.1 - Seb. keratosis: 6 of 50 (12%) 6/50 Claude Fable 5.1 - Seb. keratosis: 6 of 50 (12%) Inception v3 - Seb. keratosis: 26 of 50 (52%) 26/50 Inception v3 - Seb. keratosis: 26 of 50 (52%) 0% 25% 50% 75% 100% 
 Figure 3. Correct first-choice diagnosis for the two LLMs and the CNN, which chose from the same six diagnoses. Labels show correct answers out of the number of lesions with that histology. 

 The CNN was right more often overall and on most diagnoses. Allowing a second choice, it reached 173 of 200 against 134 and 138. It named 13 of the 30 melanomas against 8 and 11. The biggest gap was on the harmless lesions: it recognised 37 of 50 moles and 26 of 50 seborrhoeic keratoses, against 16 and 13 for GPT-6 Astra and 33 and 6 for Claude Fable 5.1. It was one short of GPT-6 Astra on basal cell carcinoma and behind both LLMs on actinic keratosis. 
 The models also failed differently. Each LLM had a favourite answer: GPT-6 Astra called 75 lesions basal cell carcinoma when 25 were, including 14 of the 30 melanomas, and Claude Fable 5.1 called 53 lesions actinic keratosis when 20 were. The CNN&rsquo;s errors on melanoma went the other way: of the 17 it got wrong, it called 8 a naevus and 6 a seborrhoeic keratosis. 
 The results in one table # 

 GPT-6 Astra 
 Claude Fable 5.1 
 CNN (Inception v3) 

 Correct diagnosis (of 200) 
 84 (42%) 
 85 (42%) 
 125 (62%) 

 Correct in first or second choice 
 134 
 138 
 173 

 Melanoma as first choice (of 30) 
 8 
 11 
 13 

 Unsafe lesions kept (of 100) 
 97 
 96 
 77 at its preset threshold; 98 or 99 when matched 

 Safe lesions discharged (of 100) 
 32 
 22 
 76 at its preset threshold 

 Melanomas discharged (of 30) 
 3 
 4 
 18 at its preset threshold; 2 or 1 when matched 

 Caveats # 

 Small numbers. Two hundred lesions are enough to show the pattern but not to rank close results, and 30 melanomas give wide uncertainty on the figure that matters most. Each LLM case was run once; answers vary between runs. 
 Hard cases. Every lesion was biopsied. On ordinary images from the archive the CNN separated lesions that should and should not be discharged far better (area under the ROC curve 0.96, against 0.86 here). 
 Contamination. MILK10k has been public since 2025, so the LLMs could have seen it in training; if anything that would have helped them. The CNN certainly had not. 
 Not state of the art. Inception v3 is a baseline. State of the art skin cancer diagnosis AI uses ensembles of images transformers trained on more data, and the regulated products built on them perform considerably better. 

 Asked as a patient # 
 Asked as a patient instead, with the clinical photograph alone and the question &ldquo;do I need to see a doctor?&rdquo;, both LLMs advised seeing a doctor in almost every case, harmless lesions included: for 99 and 98 of a further 100 biopsy-proven melanomas. 
 Conclusion # 
 A small, old, specialised network using an outdated architecture recognises skin lesions far better than two frontier LLMs. 
 Run it yourself # 
 The cases, prompts, every LLM reply and the scoring code are in one download , and the CNN is here . 
 I designed the test and made the clinical rulings. The analysis and the first drafts were produced with Claude Code, Anthropic&rsquo;s coding tool, which runs on a Claude model; one of the two LLMs tested is also Anthropic&rsquo;s. Scoring was done by script against the histology. 
 Images are from the MILK10k dataset (MILK study team, International Skin Imaging Collaboration), used under a CC BY-NC licence. 

 Dr Magnus Lynch is a Consultant Dermatologist and Mohs Surgeon at Guy's
 Hospital and Honorary Reader (equivalent of Associate Professor) at King's
 College London. His clinical work covers skin cancer, Mohs and facial
 reconstructive surgery, and lasers; his research covers the cell biology
 of skin cancers and scars and the use of AI in dermatology.
 Full profile .
