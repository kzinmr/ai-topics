---
title: "The illusion of thinking"
url: "https://substack.com/app-link/post?publication_id=293154&post_id=194385964&utm_source=substack&utm_medium=email&utm_content=share&utm_campaign=email-share&action=share&triggerShare=true&isFreemail=true&r=2flx6&token=eyJ1c2VyX2lkIjo0MDg3NDgyLCJwb3N0X2lkIjoxOTQzODU5NjQsImlhdCI6MTc3NjQzMTQwNSwiZXhwIjoxNzc5MDIzNDA1LCJpc3MiOiJwdWItMjkzMTU0Iiwic3ViIjoicG9zdC1yZWFjdGlvbiJ9.MFqJ4ElFdQKf5y4BcmZNpffBKjJdrg-n0TWYHtN9BDo"
fetched_at: 2026-04-17T13:10:18.836082+00:00
source_date: 2026-04-17
tags: [newsletter, auto-ingested]
---

# The illusion of thinking

Source: https://substack.com/app-link/post?publication_id=293154&post_id=194385964&utm_source=substack&utm_medium=email&utm_content=share&utm_campaign=email-share&action=share&triggerShare=true&isFreemail=true&r=2flx6&token=eyJ1c2VyX2lkIjo0MDg3NDgyLCJwb3N0X2lkIjoxOTQzODU5NjQsImlhdCI6MTc3NjQzMTQwNSwiZXhwIjoxNzc5MDIzNDA1LCJpc3MiOiJwdWItMjkzMTU0Iiwic3ViIjoicG9zdC1yZWFjdGlvbiJ9.MFqJ4ElFdQKf5y4BcmZNpffBKjJdrg-n0TWYHtN9BDo

Earlier this month, OpenAI’s GPT-5.4 scored 95.2% on the 2026 USA Math Olympiad. Claude Opus 4.6 hit 91.3% on GPQA Diamond, a benchmark where the questions are designed to stump PhD holders. These are problems that professional mathematicians spend hours, sometimes days, solving.
Then give these same models a test called ARC-AGI-3. It’s a set of simple visual puzzles that most humans solve in under two minutes. Look at a few input-output examples, infer the underlying rule, apply it to a new case. GPT-5.4 scores 0.2%, Gemini 3.1 Pro scores 0.4%, and Anthropic’s Opus 4.6 tops the leaderboard at 0.5%. Humans score 100%.
These models can barely solve 1 in 110 puzzles that a human handles in minutes. And it costs nearly nine grand to get there.
Andrej Karpathy, one of the most respected minds in AI (co-founder of OpenAI, former head of AI at Tesla), has a name for this. He calls it “
jagged intelligence
”. A term he coined in July 2024 to describe the strange, unintuitive fact that state-of-the-art LLMs can ace Olympiad maths yet fail at trivial tasks a child could manage. Google DeepMind CEO Demis Hassabis also picked up the term recently, arguing it’s the single biggest obstacle to AGI. “A general intelligence shouldn’t be that sort of jagged.”
This is very much a window into how these systems actually work. And it connects directly to a research paper from Apple that’s been rattling the AI community since it was published last year.
If you’ve read my previous issues on
hallucination
and
sycophancy
, think of this as the final piece of the puzzle. Hallucination is when AI confidently gives you wrong answers. Sycophancy is when it tells you what you want to hear. This issue tackles the deepest question: can AI actually
think
?
In June 2025, Apple’s machine learning team published “
The Illusion of Thinking
”. Here, instead of testing AI on the usual maths and coding benchmarks (which are often contaminated by training data), the researchers used simple puzzles such as Tower of Hanoi, where you transfer disks across pegs without placing a larger disk on a smaller one.
Then they cranked up the complexity and watched what happened.
They found that AI performance falls into three distinct zones as problems get harder.
Zone 1: Easy problems.
Standard models actually
outperformed
reasoning models here. The reasoning models overthink. They find the right answer early, then keep going, sometimes talking themselves into a wrong one. It’s a bit like second-guessing yourself when taking an exam.
Zone 2: Medium problems.
This is where reasoning models earn their keep. The extra “thinking” pays off. Chain-of-thought reasoning gives them a serious edge over standard models. This is the zone where most of us experience AI in our daily work, and it’s why tools today feel so capable.
Zone 3: Hard problems.
Both model types collapse completely (red zone). Accuracy drops to zero. Interestingly enough, as problems got harder beyond a certain threshold, the models actually
reduced
their reasoning effort. They used fewer tokens and they essentially gave up, despite having plenty of compute left.
The researchers tested this across multiple frontier models at the time of writing with OpenAI's o3, DeepSeek-R1, Claude 3.7 Sonnet Thinking, and Gemini 2.5 Thinking. The pattern was consistent across all of them.
Perhaps the most revealing finding in the paper was the level of inconsistency across different puzzles. Models could nail over 100 correct sequential steps in Tower of Hanoi but failed after just 4 steps in River Crossing. Both require logical planning and have clear rules, but one appeared in the training data far more than the other.
This strongly suggests that
performance correlates with training data familiarity, not with any general reasoning ability
. The models are simply recognising puzzles vs solving the puzzle itself.
Even more interesting was when researchers handed the models the exact algorithm to solve each puzzle, performance barely improved. They still hit the same wall.
Now it’s worth noting that the paper wasn’t without critics. Alex Lawsen at Open Philanthropy published a rebuttal titled “The Illusion of the Illusion of Thinking,” arguing that some failures were due to output token limits rather than reasoning breakdowns. But a follow-up
replication study
in July 2025 confirmed that even with those constraints removed, models still stumble at moderate complexity. The core finding holds.
Here’s where it gets interesting.
In April 2025, Geoffrey Hinton (the “Godfather of AI” and Nobel laureate)
proposed something
in an interview with the University of Toronto that left many people uncomfortable.
Humans, he argues, aren't logical reasoning machines. We're
analogy engines
. We think by resonance, not deduction. We navigate the world through pattern recognition from past experiences and apply them to new situations. Reasoning is a thin layer on top in order to do things like mathematics, but our primary decision-making engine is through analogies.
Just as Freud revealed that we have unconscious motivations driving our behaviour, Hinton believes that understanding AI reveals that we’re far less rational than we assumed.
Think about how you choose a restaurant in a new city. You don't logically analyse every menu, price point, and review. You walk past a place and think, "hey, this reminds me of that great spot back home." You decide based on vibes, not logic. And it works remarkably well.
This then creates a real paradox. If the Apple paper’s critique of AI is that it’s “just” pattern matching, and humans are
also
fundamentally pattern matchers, then where exactly does the line sit?
There is a line. And finding it matters enormously for how you use these tools.
The difference is this. When humans hit a genuinely novel problem, we can switch gears. We’re able to slow down, break things into first principles, and construct new frameworks from scratch. We might be worse at it compared to pattern matching, but we
can
do it.
Current AI models can’t. They hit the wall and stop. Or worse, they hit the wall and confidently pretend they haven’t.
That’s the illusion.
Andrej Karpathy, the same person who coined “jagged intelligence,” sat down with Dwarkesh Patel in October 2025 and explained
why
this happens.
Reinforcement learning, Karpathy said, is “sucking supervision bits through a straw.” When an AI gets a maths problem right during training, the system reinforces
everything
that led to that correct answer. This even includes the wrong turns and irrelevant detours, which are “noise”. It’s almost like giving a student full marks on an exam and then telling them everything they did was perfect, including the 10 minutes you spent doodling in the margins.
This is exactly what produces the jagged behaviour we see in practice. Models spike in performance near the types of problems they were trained on and crater everywhere else.
This is a structural feature and isn’t something that will just get fixed in the next model release.
Karpathy also made a point that stuck with me. When humans read something, we generate our own understanding. We reconcile new information with what we already know. We think
about
the material. LLMs have no equivalent process. They absorb text. They don’t learn from it the way we do.
He even went as far as saying that human memory being
fallible
might be a feature, not a bug. Our inability to memorise everything forces us to develop generalisable patterns. We learn
how
to think rather than
what
to remember. LLMs do the opposite. They remember everything and generalise inconsistently.
Demis Hassabis proposed what I think is the cleanest test for whether AI is actually reasoning.
Train a system on all human knowledge up to 1911. See if it can independently derive general relativity, like Einstein did in 1915. “It’s clear today’s systems couldn’t do that,” Hassabis said at the India AI Impact Summit in February 2026.
Someone actually tried this. Last month, an independent researcher named Michael Hla
trained an LLM
exclusively on pre-1900 text and prompted it with the same experimental observations that led Einstein and Planck to their discoveries. The result was, at best, a qualified “sort of.” The model could gesture toward some ideas, but couldn’t make those genuine conceptual leaps.
This is the cleanest distinction between pattern matching and reasoning. Pattern matching retrieves known answers. Reasoning constructs new ones. Einstein invented relativity from scratch, and he couldn't have retrieved it from anywhere because it didn't exist yet. That's what reasoning actually looks like, and it's what current AI cannot do.
For most work tasks, retrieval is fine. You
want
it to draw on existing patterns when drafting an email, summarising a report, or formatting data, etc. But when you’re asking for strategic advice or creative solutions to problems it hasn’t yet seen before, you need to be much more sceptical.
Most people prompt AI as if they’re talking to a colleague who thinks. They give it a problem, expect it to reason through it, and trust the output. That works in Zone 2 (medium-complexity problems) but falls apart everywhere else. So, it’s important you adjust your approach. Here’s what I now do.
Since AI can’t construct novel frameworks from first principles, you need to provide them upfront. Don’t say “analyse this data and tell me what’s interesting.” Instead, say “analyse this data using these three frameworks: [X], [Y], [Z].” The AI is doing the pattern matching
within
your structure.
Alternatively, if you don’t know which “scaffolding” might be appropriate for your question, just ask. Ask the AI to suggest the frameworks before you ask it to apply them:
Before answering my question, suggest 3 different frameworks 
or lenses I could use to analyse this problem. Explain what 
each one would prioritise and what it might miss.
Then pick the one that fits and ask your actual question through that lens. You’re separating the “how should I think about this” step from the “now go and do it” step. That separation I’ve found to be especially valuable when breaking down a problem.
This is what Palantir CEO Alex Karp meant when he said LLMs are a “
raw material
that has to be processed” at AIPCon 8.
The processing is your reasoning. The LLM is the execution layer.
Before you rely on an AI output, ask yourself: is this a Zone 1, Zone 2, or Zone 3 problem?
Zone 1 (simple/routine):
AI is fine but might overthink. Keep prompts short and direct. Don’t ask it to “think step by step” for simple tasks. It’ll talk itself into a worse answer.
Zone 2 (moderate complexity):
AI’s sweet spot. Give it rich context, be specific about what you want back, and let it work. This is where most of the value lives day to day.
Zone 3 (novel/complex):
Don’t trust the output without independent verification. The AI won’t tell you it’s out of its depth. It might give you a confident answer that
sounds
right, but might be completely fabricated.
The tricky part is that Zone 3 problems don’t look obviously hard. A straightforward-sounding question might actually require novel reasoning that the model can’t do. That’s why the next section matters.
Here’s the 30-second checklist I run through before trusting any AI output that feeds into a decision. These are the 5 questions I’ve developed over thousands of hours working with these tools, and they’ve saved me from shipping bad work more times than I’d like to admit.
