---
title: "GLM 5.2 playing text adventures"
url: "https://entropicthoughts.com/glm-5-2-playing-text-adventures"
fetched_at: 2026-06-19T07:00:57.349762+00:00
source: "entropicthoughts.com"
tags: [blog, raw]
---

# GLM 5.2 playing text adventures

Source: https://entropicthoughts.com/glm-5-2-playing-text-adventures

I’ve heard some buzz around the new
glm
5.2 open-weights model. They say it’s
very capable! I won’t run a full comparison benchmark, but I have some credits
sloshing around on OpenRouter so I figured I might compare
glm
5.2 to the
similarly-priced Gemini 3 Flash
1
The market currently infers with the
glm
5.2 model at $4.4 per million output tokens, whereas Google charges $3 per
million output tokens for their model. I expect the price of the
glm
model to
go down somewhat when people figure out how to deploy it more efficiently and/or
the buzz dies down. That’s what happened with previous open-weight models I’ve
tested.
, and see where things land.
This uses the same setup as
the previous benchmark
: each
llm
gets a few
attempts at playing the game, with each attempt being limited to a fixed budget
of around $0.15. The
llm
doesn’t know it, but the harness tracks achievements
for each game, and counts how many the
llm
earns in each attempt.
Here are the number of attempts for each game in this run.
Game
Attempts per model
Lost Pig
4
Organ Grinder’s Monkey
2
Not All That Shimmers
3
Kill Wizard
3
9:05
5
Total
17
💸
$5.1
Then I did the stupid, silly thing and fitted a plain linear regression
predicting the achievement count for each attempt, with the
llm
model as an
explainatory fixed effect, and the game as a random effect.
2
Why didn’t I use
random effects for game difficulty before? I should have! But I didn’t know
about mixed-effects modeling then. I learn things.
When thusly controlling for
game difficulty, Gemini 3 Flash earns just over eight achievements in a typical
attempt. The new
glm
5.2 earns 15 % fewer, and this is statistically
significant at customary significance levels.
This does not tell us much – is 15 % fewer achievements very bad or reasonable?
Hard to tell without comparing to other models, but it’s roughly the same
magnitude as the standard deviation of the residual noise in the fitted model.
Thus we can say it’s about 0.8 levels of noise worse than the king of text
adventure playing
llm
s. That’s impressive. For example, it is definitely
better than Gemini 2.5 Flash, which is 1.6 noise levels worse than Gemini 3
Flash.
(Due to the budget constraint, otherwise capable but very expensive models like
Sonnet 4.5 and
gpt
5.2 are 2.5× noise and 3× worse than the noise level,
respectively.)
