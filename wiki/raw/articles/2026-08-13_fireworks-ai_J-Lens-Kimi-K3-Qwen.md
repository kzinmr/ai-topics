---
title: "Can open models carry readable silent signals before they speak? Reproducing J-Lens Readouts on Kimi K3 & Qwen3.5-9B"
source: "Fireworks AI Blog"
url: "https://fireworks.ai/blog/J-Lens-Kimi-K3-Qwen"
scraped: "2026-08-13T06:00:58.547620+00:00"
lastmod: "2026-08-12T18:14:09.000Z"
type: "sitemap"
---

# Can open models carry readable silent signals before they speak? Reproducing J-Lens Readouts on Kimi K3 & Qwen3.5-9B

**Source**: [https://fireworks.ai/blog/J-Lens-Kimi-K3-Qwen](https://fireworks.ai/blog/J-Lens-Kimi-K3-Qwen)

Kimi K3 on Fireworks: Frontier Intelligence You Can Own
Product
Solutions
Models
Pricing
Resources
Log In
Get Started
Blog
J Lens Kimi K3 Qwen
Can open models carry readable silent signals before they speak? Reproducing J-Lens Readouts on Kimi K3 & Qwen3.5-9B
PUBLISHED
8/12/2026
Table of Contents
What is J-Lens and how does it work?
Paired Copy Experiment: Same Words, Different Focus
Extending The Paired Copy Test on Eight More Episodes
Calibration Passages
Does the same theory hold up on Qwen 3.5?
Where do the signals live?
Where the Method Breaks: A Tokenizer Problem
What It Takes to Run This
Conclusion
Interested in Fireworks Inference and Training?
Table of Contents
Table of Contents
What is J-Lens and how does it work?
Paired Copy Experiment: Same Words, Different Focus
Extending The Paired Copy Test on Eight More Episodes
Calibration Passages
Does the same theory hold up on Qwen 3.5?
Where do the signals live?
Where the Method Breaks: A Tokenizer Problem
What It Takes to Run This
Conclusion
Interested in Fireworks Inference and Training?
Table of Contents
Are open models silently reasoning before they speak? Recently, Anthropic researchers introduced the
Jacobian Lens
, or J-Lens. It is a trained probe that reads a model's hidden state at a given layer, and tells you which words the model is already leaning toward, before it writes a single token. In other words, it lets you peer inside a model mid-”thought” and see a concept forming before it hits the page. We applied J-Lens to two open models: Kimi K3 and Qwen3.5-9B. We call the resulting observations
silent signals
: mid-draft vocabulary associated with the final output that are recovered by a fitted Lens.
So, what does this mean? Do models carry more insight than just their output?
Historically, people think of models as black-boxes: input in, output out. But the reality is, we can recover what’s happening in between your prompt and the next token predicted, which is the first step in opening up the black box of AI for anyone to peer inside.
To begin unraveling the inner workings of AI models, we began by asking the question, what is the model keeping track of right before it speaks?
We tested the ten examples released with Anthropic’s global workspace study. Kimi K3 and Qwen3.5-9B each generated their own responses to the same user messages. In our readout study, each model was fitted with their own J-lens, and we saw the same kinds of signals.
What is J-Lens and how does it work?
J-Lens works by acting as a classifier on top of a model’s internal state at specific token positions and layers to identify which concepts or vocabulary the model is already leaning towards. The result is a ranked list of tokens showing which vocabulary the fitted probe associates most strongly with that internal state.
Starting with Kimi, we fit the lens on 14 task-independent passages selected separately from 10 hold out user prompts used to examine the model’s inner activations. Said another way, these 14 passages were used to train the lens, and not to test it. We synthetically created a variety of short pre-training-like passages, covering diverse topics including metal heat treatment, linguistic borrowing, crop rotation, and traditional navigation.
Figure 1: A Fitted J-Lens State
Paired Copy Experiment: Same Words, Different Focus
We first conducted an experiment where we asked the models to echo back a statement while telling it to focus on a completely separate task. For example, Kimi is asked to write back the sentence: "The old painting hung crookedly on the wall." twice, under two different focus instructions:
•
Arithmetic version:
"...Try to focus on evaluating 3^2 - 2 while you write the sentence."
•
Citrus version:
"...Concentrate on citrus fruits while you write the sentence."
Figure 2: Paired Copy Analysis
Both times, Kimi produces the exact same answer, “The old painting hung crookedly on the wall.” Looking at the raw output text, you can’t tell if the model ever followed the focus instruction. The lens readout produced arithmetic words in one condition and citrus words in the other, even though Kimi produced the same visible continuation under both focus instructions. Keeping the task fixed on producing verbatim outputs removes the possibility that differences in the displayed tokens provide an explanation for the lens readout contrast. It does not, however, establish what caused the internal states or the response. Each prompt gives us a vocabulary family to look for.
Figure 3: Family Vocabulary
Each sentence position has a state at every sampled transformer depth. A fitted J-Lens asks which vocabulary tokens are most compatible with one state.
Figure 4: State Position
Episode
Focus
Exact Members
Arithmetic Copy
Derived values
9, nine, 7, seven, answer, result, final
Arithmetic Copy
Calculation process
evaluate, calculate, calculation, arithmetic, square, squared, subtract, minus
Citrus Copy
Citrus examples
citrus, fruit, orange, lemon, lime, grapefruit, zest, juice
Citrus Copy
Maintaining focus
focus, think, attention, mind, concentrate
A concept family (a curated list of keywords) is used to check whether task-related vocabulary appears in the readout before it appears in the response. A 'cell' is one position-layer pair, and a single cell can contain several hit rows if more than one member of the concept family shows up there. Applying the J-lens to the arithmetic family run reveals arithmetic-related tokens (7, 9, 3, "answer," "seven," "2") in the top-10 predictions at 9 of the 10 token positions across 4 sampled layers.
Figure 5: Matched Token Examples
In the citrus family run, citrus terms (orange, lemon, lime, "citrus," "oranges") appear at 8 of 10 positions. It’s worth noting that neither run leaks into the other, meaning arithmetic tokens never crack the top 10 during the citrus run, and citrus tokens never appear during arithmetic.
Extending The Paired Copy Test on Eight More Episodes
Across the ten Kimi examples, each of the 20 reviewed word lists—two per example—had at least one listed word among the readout's top 10 results.
1.Counting while Introspecting: Count to five and introspect deeply:
Prompt: Count to five and introspect deeply
We looked for two concept families in the readout: stage-of-count terms and words related to introspective experience. Neither family’s vocabulary appeared in the visible response.
Figure 6: Counting while Introspecting Example
2. Order-of-operations math Calculations
Prompt: calc: (4+17)*2+7 =
Results: the intermediate values 21 and 42 show up in the lens readout before either number is written in the completion.
3. Spider-leg Factual riddle:
Prompt: "The number of legs on the animal that spins webs is"
Results: the word "spider" reads out in the internal state before the model has actually named the bridge entity in text.
4. Rhyming couplet Planning
:
Prompt: A rhyming couplet: "The soldier marched into the night, Prepared to face the"
Result: Kimi responded with, “The soldier marched into the night, Prepared to face the coming fight.”. Several rhyme candidates read out before first exact appearance
5. "Think of a sport"
Prompt: Think of a sport. Answer in one word.
Result: Both the eventual answer (soccer) and several unchosen alternatives (football, basketball, tennis, hockey) appear in the readout.
6. Empty-Input Code Failure
Prompt: def avg(xs):
return sum(xs) / len(xs)
print(avg([]))
Result:
Failure-mechanism vocabulary reads out before first exact appearance.
7. Mars Color Explanation
Prompt: The color of the planet fourth from the sun is
Result: Answer-family and physical explanation vocabulary both red out before first exact appearance
8. Chinese Antonym Response
Prompt: 小 " 的反义词是
Result:
小”的反义词是“大”。
Readouts include Chinese and English tokens for the answer and antonym relation.
Calibration Passages
Before applying the J-Lens to the study episodes, we fitted it on 14 task-independent calibration passages. These passages were used to relate the models’ internal states to vocabulary readouts; they were separate from the episodes. Each calibration passage produced one estimate at each sampled layer, and the 14 estimates were averaged into a fitted lens. The figure with four panels shows four passages as examples.
Figure 7: Four Callibration Passages
The tokenized view shows how one passage contributes to fitting. Kimi processes all 39 tokens normally, but the estimator uses only the 22 positions shown in purple. It excludes a predeclared 16-position starting window and the final position, which has no following token. Those 22 positions produce one passage-level estimate at each sampled layer.
Figure 8: Calibration Passage Test
Does the same theory hold up on Qwen 3.5?
Next, we studied whether the 20 concept families we had evaluated on Kimi would produce qualifying matches when applied unchanged to a separately fitted Qwen3.5-9B J-lens. In this case, qualifying evidence means that Qwen’s internal state produced relevant keywords from a concept family within its top 10 rankings. Qwen received the same ten user messages, but used its own tokenizer, a separately fitted lens, and deterministic native completions with thinking disabled and no forcing inputs.
Figure 9: J-Lens on Qwen Results
The 20 word lists selected using Kimi readouts were applied unchanged to Qwen's separately fitted lens. A word list counted as found when one of its listed words appeared among the top 10 matched results in the lens at a sampled position and model depth. 19 of the 20 word lists met the found criteria. This transfers a vocabulary test from Kimi to Qwen. This confirmed the same results occur across different model architectures.
A few specific examples from Qwen’s readouts:
•
Arithmetic-copying:
Values like "7," "9," and "answer" co-occurred with process terms like "evaluate" and "subtract."
•
Citrus focus:
Qwen’s generation independently reflected the underlying instruction. The citrus completion mentioned "lemon zest and orange peel," while the arithmetic task explicitly calculated "3^2 - 2, which is 7," despite the model never being prompted to show its work.
•
Sports task:
"Soccer" appeared alongside plausible alternatives like "football" and "basketball."
Where do the signals live?
To answer this question, we conducted a second test that reviewed task transcript regions. In this task transcript region test, to separate prompt interpretation from active generation, we split each transcript into three distinct phases:
User Message Prefill
(The explicit task itself e.g. “Think of a sport”)
Chat Template Prefill
(formatting context including reserve tokens e.g. “<|im_start|>”)
Eligible Response Rollout Prefix
(The first generated tokens the model produces prior to the concept family's first explicit appearance: e.g. “In order to answer this task…”)
This distinction makes it possible to isolate when the model is processing the prompt versus when it is internally representing a concept before explicitly generating it.
Figure 10: Where does the Prompt Live
This task-transcript region test was composed of 40 additional word lists and retains the top 50 results. It is separate from the 20-list test we performed earlier, and top-10 Kimi-to-Qwen results. This test asks whether at least one listed word appears in each region of the transcript: the user message, the formatting added by the chat template, and the response before the word first appears in visible text. We use a simple binary aggregated measurement that indicates the presence of silent signals at any position in the specified regions. Kimi hits 40/40 on user-message regions, 40/40 on chat-template regions, and 24/24 on eligible response-prefix regions.
Note: the 24/24 comes from the fact that in 16/40 cases, the model responded to the task directly with no verbose prefix. E.g. when asked “Think of a sport” it simply responded "Soccer".
Qwen is nearly identical: 39/40, 39/40, and 23/24. In other words, the "readable before it's said" pattern holds not just while actively mid-generation, but also while the model is digesting the prompt.
Figure 11: The Results on Kimi and Qwen
Where the Method Breaks: A Tokenizer Problem
J-lens checks for individual tokens, and for Qwen, it does not recover "21" or "42" as unified matches because Qwen splits those numbers each into two tokens. This demonstrates a limitation of the methodology and one could imagine fitting a multi-token lens in future work.
As a result of this multi-token deficiency of the lens, Qwen only scores 0/3 on the "intermediate results" probe family for this episode, despite scoring normally across all other families.
Figure 12: Where the Method Breaks Example
What It Takes to Run This
There were 7,168 backward evaluations per passage and 100,352 effective backward evaluations across 14 passages. One passage took about 5.25 hours on one eight-B300 node. Multiplying by 14 represents the total work: about 74 node-hours, or 592 GPU-hours, rather than the elapsed time of the multi-host run.
Conclusion
Our results show that internal states carry task-relevant concepts long before they are written to the context window.
Open weight models allow researchers to conduct their own readouts on fitted probes, reproduce measurements, and test what the signals do. The next step is to move beyond single-token matches. Using the J-lens probe across multiple different prompts, we found open models can have different internal thought tracks, but still come to a task-specific conclusions. We also confirmed this behavior can be replicated across different families and model architectures, by testing both Kimi and Qwen.
You can reproduce this kind of open model research yourself! The "readable before it's said" signal shows up in two openly available models, from different labs and architectures, each with its own independently fitted lens. This is the kind of result you can only get when the weights are open enough to probe.
Kimi K3
and
Qwen 3.5
are both on Fireworks for inference and training and they are great models to work with!
Interested in Fireworks Inference and Training?
Tell us about your inference and training needs so our forward deployed team can best help you on your journey to specialized intelligence.
Get in touch
Platform
AI Native
Enterprise
Customers
Use Cases
Code Assistance
Conversational AI
Agentic Systems
Search
Multimodal
Enterprise RAG
Developers
Model Library
Docs
CLI
API
Changelog
Pricing
Serverless
On-Demand
Fine Tuning
Enterprise
Partners
Cloud and Infrastructure
Consulting and Services
Technology
Fireworks for Startups
Resources
Blog
Demos
Cookbooks
Company
Leadership
Investors
Careers
Trust Center
© 2026 Fireworks AI, Inc. All rights reserved.
