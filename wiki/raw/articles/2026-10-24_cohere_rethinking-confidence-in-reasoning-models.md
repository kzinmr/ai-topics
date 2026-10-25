---
title: "Rethinking Confidence in Reasoning Models"
source: "Cohere Blog"
url: "https://cohere.com/blog/rethinking-confidence-in-reasoning-models"
scraped: "2026-10-24T06:01:01.546473+00:00"
lastmod: "2026-10-20"
type: "sitemap"
---

# Rethinking Confidence in Reasoning Models

**Source**: [https://cohere.com/blog/rethinking-confidence-in-reasoning-models](https://cohere.com/blog/rethinking-confidence-in-reasoning-models)

You roll two fair six-sided dice. What is the probability that their sum is at least 10?
A model might hesitate at first. Then it counts the possibilities: three ways to roll 10, two ways to roll 11, and one way to roll 12. Six outcomes out of 36.
The answer is 1/6
.
In our illustrative example (figure below, on the left), the model starts at 25% confidence and finishes at 88%. Those percentages describe its confidence in getting the answer right, not the probability of the dice outcome. Working through the problem has changed its assessment.
Confidence can move the other way, too (figure below, on the right). Reasoning through a solution that initially looks straightforward may reveal a mistaken assumption or a contradiction. A useful confidence estimate should be able to reflect that change, even when the model still gives the wrong answer. However, standard reasoning models do not necessarily come with this ability: producing a detailed reasoning process does not guarantee that a model can reliably assess and communicate its uncertainty.
This is the idea behind our method
CALIBER
: train a reasoning model to estimate its chance of success before it begins, then assess its particular answer afterwards. On our math benchmark, the calibrated 7B model reduces calibration error by more than half compared with the best single-confidence baseline on this metriic. The key is that the two confidence estimates answer different questions.
One confidence score hides two questions
Before reasoning, the model has only seen the question. It can recognise the topic and judge whether the problem looks manageable. Its confidence answers:
“How likely am I to solve this?”
After reasoning, it has something more specific to assess: the solution it actually produced. Now the question is:
“How likely is this answer to be correct?”
These predictions are related, but they serve different purposes. Initial confidence gives an indication of whether the model expects to handle the question successfully. Final confidence helps a user judge whether the resulting answer needs closer scrutiny. A model might often solve this kind of problem and still make a mistake on this attempt. Or it might approach a difficult question cautiously, then find a solution it can check.
CALIBER
trains the model to report both estimates in one response: initial confidence, reasoning, an answer, and final confidence. The two numbers can disagree because reasoning gives the model new information to assess. The goal is to make these estimates meaningful enough to support decisions about when to accept an answer, verify it, or seek help.
Teaching confidence what to predict
To train initial confidence, we let the model try the same question several times. If seven out of ten attempts succeed, 70% becomes the training target. That captures how often the current model can solve the question, before we know which particular attempt it will produce.
Final confidence gets a different target: whether that individual answer is correct. A successful and an unsuccessful attempt at the same question share an initial-confidence target, but receive different final-confidence targets. The figure below shows how this works.
In this example, three of four attempts succeed, giving an initial-confidence target of 75%. The fourth attempt produces a wrong answer, so its final-confidence target is 0. The displayed 60% and 20% are the model’s predictions. Training rewards it for moving those predictions closer to their respective targets.
We combine these confidence rewards with a reward for answering correctly. The model is encouraged both to solve the problem and to assess its chances accurately. Recognizing uncertainty about a wrong answer can improve its confidence reward, but it does not earn the reward for a correct solution. The aim is to make confidence more useful while keeping the model focused on getting the answer right.
Why saying 70 percent every time is not enough
Imagine a model that answers 70% of questions correctly and reports 70% confidence every time. Its confidence matches its overall accuracy perfectly. But if you only have time to check a few answers, those identical scores give you no way to choose.
Now imagine another model with the same overall accuracy. It assigns 90% confidence to half its answers and 50% to the other half. If those groups are correct 90% and 50% of the time, respectively, this model is also calibrated. Its confidence is more useful, though: it helps you focus your checks on the answers more likely to contain mistakes.
We therefore evaluate two properties together.
Expected Calibration Error (ECE)
measures whether confidence matches observed accuracy: among answers assigned roughly 80% confidence, roughly 80% should be correct.
AUROC
measures whether correct answers tend to receive higher confidence than incorrect ones. Lower ECE and higher AUROC are better. Together, they show whether the confidence values are reliable and whether they help identify likely errors.
The figure illustrates these complementary goals: confidence should match observed accuracy and help distinguish correct answers from mistakes.
Better confidence on math and beyond
We trained 7B and 30B models on 30,000 math problems and evaluated them on 1,000 held-out problems, plus three question-answering benchmarks. Our comparisons use a shared training setup; the
“lite”
baselines are simplified adaptations of earlier methods. For CALIBER, the reported calibration metrics evaluate final confidence.
On BigMathDigits, the 7B model’s ECE falls from 0.059 for the strongest single-confidence baseline to 0.028 for CALIBER –
a 52.5% reduction
. CALIBER also achieves the best AUROC (0.806) and Brier score (0.130), showing improvements both in how closely confidence matches accuracy and in how well it distinguishes correct answers from mistakes.
The improvements extend beyond math. Without further training or task-specific checkpoint selection, the 7B model reduces calibration error by
26.8% on GPQA, 32.2% on TriviaQA, and 36.2% on SimpleQA
, compared with the strongest single-confidence baseline on each dataset.
The 30B results show why the metrics matter together. On BigMathDigits, CALIBER’s ECE of 0.022 is only slightly better than CoCA-lite’s 0.023. But its AUROC is 0.797, compared with 0.508 for CoCA-lite: a large difference in how well confidence distinguishes correct from incorrect answers. Other baselines achieve slightly higher AUROC than CALIBER, so the benefit depends on which property we measure.
Confidence versus observed accuracy on BigMathDigits for the 30B model. Curves closer to the diagonal are better calibrated.
What a change in confidence tells us
Having two estimates lets us see whether the model revises its assessment after reasoning. On BigMathDigits, the 7B model’s mean confidence rises from 78.5% to 83.5% for correct answers and falls from 62.6% to 54.5% for incorrect answers. On other datasets, it sometimes lowers confidence for both groups, with a larger decrease for incorrect answers.
A rise or fall is therefore context, not a verdict. Two answers that finish at 70% confidence express the same estimated probability of correctness, even if one estimate rose and the other fell. The final estimate assesses the answer; the change tells us how the model’s assessment evolved.
Our experiments take this measurement before and after a single reasoning process. A next question is whether reliable confidence updates could help a model decide when to verify, retrieve more information, or abstain. We have not tested those uses here. CALIBER provides a starting point: confidence trained to reflect what the model can assess at each stage of reasoning.
Read the paper for the full experimental setup and results:
CALIBER
.
Blog
Written By
Beyza Ermis
Research Scientist
Tags
Research
Share
AI isn’t a shortcut.
It’s how business gets ahead.
Contact sales
