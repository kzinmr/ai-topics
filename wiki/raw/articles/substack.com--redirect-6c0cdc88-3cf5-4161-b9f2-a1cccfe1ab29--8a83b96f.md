---
title: "We're Learning Backwards"
url: "https://substack.com/redirect/6c0cdc88-3cf5-4161-b9f2-a1cccfe1ab29?j=eyJ1IjoiMmZseDYifQ.6O_iC1_GWCzChnbrHzSrs1hMpJpoODTUJm_FAk3tf6E"
fetched_at: 2026-04-16T19:09:15.203352+00:00
source_date: 2026-04-16
tags: [newsletter, auto-ingested]
---

# We're Learning Backwards

Source: https://substack.com/redirect/6c0cdc88-3cf5-4161-b9f2-a1cccfe1ab29?j=eyJ1IjoiMmZseDYifQ.6O_iC1_GWCzChnbrHzSrs1hMpJpoODTUJm_FAk3tf6E

In March,
Professor Alyosha Efros
delivered what has become my all-time favorite lecture: “Data, Data, Data… Watson, I need Data!” He talked about scene completion: removing an object from a photograph and filling in the missing region. With modern generative models, we can do this pretty
well.
1
1
But we were not talking about 2020s research. Instead, he showed us results from
Hays & Efros (2007)
, “Scene Completion Using Millions of Photographs,” published well before AlexNet and the resurgence of neural networks.
Results from Hays & Efros (2007). Surprisingly convincing output, even by today’s standards.
But it’s not the results that fascinated me. It’s the method. There was no fancy algorithm or hand-tuned feature detector. What they did was essentially:
Download a large corpus of images (2.3 million), and
For each query image, find a similar scene and sample its pixels.
When they initially tried this with 10,000 images, the results were practically unusable. But by increasing the amount of data (with no change to the method), output quality improved dramatically. There was no model of geometry, lighting, or occlusion. Just lookup on a really big table.
simple model
+
lots of data
≈
intelligence
\text{simple model} + \text{lots of data} \approx \text{intelligence}
Halevy, Norvig & Pereira (2009)
wrote the interpretive frame in “The Unreasonable Effectiveness of Data”: simple models with lots of data often beat complex models with less data. That more or less predicted the trajectory of machine learning for the next decade and a half.
Richard Sutton’s
The Bitter Lesson (2019)
echoes the same sentiment. The biggest breakthroughs in AI have come from methods that leverage computation and data, rather than those that try to inject human knowledge or intuition.
The Scaling Hypothesis
Think back to the early days of GPT. The original
GPT-1 (2018)
often generated unintelligible text. With 117M parameters and ~5GB of training data, this was state of the art:
Roses are red, and the flowers are white. "
" i don’t know what you’re talking about. "
" yes, you do. "
" no, i don’t. "
" yes, you do. "
" no, i don’t. "
" yes, you do. "
" no, i don’t. "
" yes, you do. "
" no, i don’t. "
" yes, you do. "
" no, i don’t. "
" yes, you do. "
" no
A real generation from GPT-1 I got just for this article.
GPT-2 (2019)
scaled to 1.5B parameters and 40GB of training data, and brought the first real inkling of “intelligence.” It could generate coherent paragraphs, and OpenAI initially withheld the full model out of concern of misuse. Even the authors seemed surprised by how much improvement they got from what was mostly just “GPT-1, but bigger.”
Gwern’s
Scaling Hypothesis essay (2020)
argued that intelligence is what you get when you apply simple neural units and learning algorithms at sufficient scale. Feed a model enough data and compute, and capabilities like reasoning, generalization, and understanding should emerge. Six years later, we have LLMs that hold conversations, write code, and solve nontrivial math problems. Most of this didn’t come from an architectural breakthrough. It came from bigger machines, more data, and improved training methods.
Just like Hays & Efros, there is a threshold where outputs
*click*
from “obvious nonsense” to “surprisingly convincing.”
Correlation, Causation, and Intelligence
But there’s a difference between “convincing” and “intelligent”. Consider the Hays & Efros case. When presented with a truly unique scene, the system fails abruptly. It doesn’t have a model of how objects interact, so it can’t smoothly fill in the blanks when out of distribution. With LLMs, you can see this by asking whether you should walk or drive to the car
wash.
2
2
Both Claude (Opus, Sonnet, Haiku) and ChatGPT (Thinking, Instant) confidently say to walk since it’s so close by. They even provide a list of situations where driving would be better (bad weather, carrying heavy items), but they fail to reason that a car wash without a car makes for a pretty bad car wash.
This is obviously spot-fixable with more post-training, but it’s not just an isolated
quirk.
3
3
Especially as these models get smarter and seem to approach or exceed human intelligence, the absurdity of these failures becomes more glaring. It doesn’t make cognitive sense that something that explains graduate-level abstract mathematics simultaneously fails to reason through a simple counting problem.
This is the problem of
spiky intelligence
: models that are usually brilliant, but have sharp cliffs in their blind spots.
Ice cream sales cause global warming!
All of this starts to make sense when you consider correlation and causation, two concepts that are notoriously difficult to disentangle. With LLMs, the bet is that forcing enough correlations into a compressed format
necessarily
forces a learned causal model of the world. Backpropagation incentivizes
memorization
4
4
, but with enough data, it’s no longer possible to memorize everything. This is the core of the Scaling Hypothesis as well.
In other words, causality is
emergent
from correlation, given infinite data and compute.
I hope I’ve convinced you that today’s LLMs are, in fact, not truly causal. At the same time, they definitely feel intelligent and capable of “reasoning” (through chain-of-thought). So do we actually care about the distinction? If the output is useful, who cares how it got there?
For most situations, most of the time, it doesn’t matter. But on occasion, you get cosmically unlucky and encounter a problem that pushes the model into a region of confidently wrong correlation.
Novelty Is Hard
ARC Prize
’s goal is to make “low noise, high signal AGI benchmarks”. Their most recent benchmark,
ARC-AGI-3
(March 25th, 2026), tries to do this by putting models in completely new interactive puzzle environments with no instructions, no rules, and no explicit win conditions. The only way to succeed is to explore, test hypotheses, and most importantly,
learn
from the environment in real time. Scoring is based on action efficiency relative to a human baseline.
So far, the benchmark has been rough for LLMs, with frontier models currently scoring under 1%. I don’t doubt that they will get better, but this benchmark highlights the core problem: LLMs need their priors to be
useful.
5
5
As a human, what’s striking about these puzzles is how
conscious
the problem-solving feels. You can watch yourself forming hypotheses, testing them, and revising. I built a
daily Wordle-style
version of this to share that experience with my friends. It’s challenging, but it gives you a deep appreciation for the complexity of “general intelligence” and the fact that we can do this with any consistency at all.
I’m deliberately avoiding saying that humans solve this “with no priors”. Despite an unseen environment, we have a lifetime of experience and a rich world model to draw on. But even a newborn has core perceptual
biases
6
6
and an extremely strong ability to learn, refined over millions of years of evolution.
Fluid Intelligence
In 1943, psychologist Raymond Cattell proposed a distinction between two types of intelligence: “crystallized” (knowledge and skills acquired through experience), and “fluid” (the ability to solve novel problems without priors). Generally, humans start with high fluid intelligence that gradually crystallizes over time. Naturally, the division between the two is blurry, but it’s a useful framework for thinking about intelligence in general.
There’s evidence that humans have causal reasoning abilities preceding knowledge accumulation.
Leslie & Keeble (1987)
showed that 6-month-old infants, with essentially no accumulated experience, react differently to “possible” versus “impossible”
events.
7
7
With negligible experience and no opportunity to accumulate patterns over millions of examples, they’re still able to detect violations of a basic causal model of the world.
Fluid intelligence precedes, and likely enables, crystallized intelligence.
Things get interesting when you think about the implications for LLMs. It’s pretty clear that they have crystallized intelligence at extraordinary scale. They have arguably superhuman performance on an inarguably superhuman range of specializations, and it would be reductive to call this solely “pattern-matching”. And yet, they still fail on genuinely novel tasks, so we can’t say they’re AGI either.
The hardest part of artificial general intelligence is the generalization.
“These models somehow generalize dramatically worse than people. It’s super obvious. that seems like a very fundamental thing.”
Ilya Sutskever,
Dwarkesh Podcast, November 2025
I don’t disagree with the Scaling Hypothesis; with infinite data and compute, we will eventually get fluid intelligence. But even if we keep scaling compute, we definitely don’t have infinite data. If data is the bottleneck, then the “simple model, lots of data” approach will necessarily have a ceiling.
Most of the recent progress in LLM capabilities hasn’t come from scaling pre-training. It’s come from increasingly clever post-training techniques: RLHF to align outputs with human preferences, tool use to offload tasks the model can’t do natively, chain-of-thought to simulate step-by-step reasoning, retrieval-augmented generation to access knowledge beyond the training set. These genuinely improve model performance, but they’re also exactly the kind of human-engineered, domain-specific interventions that Sutton’s Bitter Lesson warned us against.
Sutton’s argument was never “don’t be clever.” It was that cleverness doesn’t scale. Hand-engineered features give you short-term wins, but they lose to methods that scale with compute and data. The irony is that the Bitter Lesson might be right about the destination and the path, but we’re running out of fuel.
Are We AGI Yet?
So what could give us fluid intelligence?
If we revisit ARC-AGI-3,
the results
offer a clue. During the preview period, the best-performing models weren’t the ones with the most knowledge. They were the ones that explored, forming hypotheses, testing them, and revising.
StochasticGoose
scored 12.58% using CNNs and hierarchical sampling, while frontier language models scored under 1%. The systems that explored their environments, tracked what they did, and revised hypotheses outperformed the systems that pattern-matched from prior knowledge.
This mirrors what I’ve observed when I play the same environments. As you press buttons, you deliberately try to build a world model of the game’s mechanics by forming hypotheses and testing them. When a new mechanic is introduced, you revise your world model to accommodate it. Beyond the ARC benchmark, this is what we also see in the real world. Infants learn about physics by dropping things, pushing things, and seeing what happens, not by reading about physics in a textbook.
By contrast, LLMs have an absurd amount of knowledge but no mechanism to develop the fluid foundation it should rest on. This doesn’t mean they’re useless. Their introduction has dramatically transformed a huge number of fields, and even given us hope that AGI might be possible within our lifetimes. But everything I’ve seen suggests that the path to AGI will not be bigger LLMs.
I think the path requires a fundamentally new architecture that learns a dynamic world model through interaction, with the capability to revise that model in real time. Perhaps a different training signal that rewards exploration, testing hypotheses, and adapting. I don’t know what that looks like. I don’t know how to reconcile that with the Scaling Hypothesis, the Bitter Lesson, or The Unreasonable Effectiveness of Data.
But I do know that LLMs learned backwards.
Footnotes
This was actually one of the headline features of
DALL-E 2 (2022)
. It’s also the same problem that Photoshop’s Generative Fill solves.
Yes this is real and very consistent. Just ask, “If the car wash is 100m away, should I drive or walk there?”
Claude Opus 4.6
Claude Sonnet 4.6
Claude Haiku 4.5
ChatGPT 5.4 Thinking
ChatGPT 5.3 Instant
Remember the strawberry problem from two years ago? Even though the core issue was tokenization, the inability to reason prevented the model from breaking down things that it
did
know: “I don’t know the answer. I have code execution. I can count the letters using a simple Python script to get the answer.”
Another famous example is: “Which is greater, 9.11 or 9.9?” Again, an
intelligent
system should be able to reason through this, even if it doesn’t know the answer.
If you were able to memorize the entire training set, you could trivially get a perfect training loss without learning any generalizable patterns. This is why regularization techniques like dropout are important.
Sometimes these models would get stuck thinking they were playing a different game (like Tetris) and apply an incorrect “mental model” to the problem.
For example, infants have a bias towards face-like patterns, which helps them learn to recognize and understand faces. They also have a bias towards certain sounds, which helps with language acquisition. These biases are present before any learning takes place.
Humans are also generally susceptible to illusions, which only work
because
they invert these biases.
The study showed infants two types of events: a “possible” event and an “impossible” event (reversed or altered), and they measured reactions and attention. It can be contested whether this is truly indicative of causal reasoning, but even if they’re just detecting statistical violations, it still suggests a remarkable sensitivity to the structure of the world with very little experience.
