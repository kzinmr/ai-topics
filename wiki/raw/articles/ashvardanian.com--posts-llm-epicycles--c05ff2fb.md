---
title: "Before AI's Kepler Moment - Are LLMs the Epicycles of Intelligence?"
url: "https://ashvardanian.com/posts/llm-epicycles/"
fetched_at: 2026-05-05T07:01:49.115126+00:00
source: "Ash Vardanyan"
tags: [blog, raw]
---

# Before AI's Kepler Moment - Are LLMs the Epicycles of Intelligence?

Source: https://ashvardanian.com/posts/llm-epicycles/

I’ve always been fascinated by AI and mega-projects — and as
I work on AI infrastructure
, you might assume I’m equally fascinated by the current LLM race.
In reality, I’m far more skeptical than most.
While LLMs are undeniably useful, I’m not convinced “intelligence” is even the right scale to measure them against.
The analogy I keep returning to comes not from computer science, but from astronomy: the story of
epicycles
.
The Epicycle Era
#
Early astronomy began with the simplest model imaginable: planets move in perfect circles. If Earth is at the center, then the position of a planet could be described as
$$
x(t) = R \cos(\omega t), \quad y(t) = R \sin(\omega t),
$$
where $R$ is the radius and $\omega$ the angular speed.
This model had elegance — a single equation for perpetual motion.
But when observations improved, the simplicity broke down: Mars would sometimes appear to move backward (
retrograde
motion), which pure circles could not explain.
To patch this,
Claudius Ptolemy
in 2nd-century AD introduced epicycles — circles riding atop circles.
Instead of a single rotation, they stacked another:
$$
x(t) = R \cos(\omega t) + r \cos(\Omega t), \quad
y(t) = R \sin(\omega t) + r \sin(\Omega t)
$$
with a larger
“deferent”
of radius $R$ and a smaller
“epicycle”
of radius $r$.
This worked remarkably well: by adjusting radii and frequencies, they could mimic retrograde loops.
But every refinement required more parameters.
Soon, astronomers were layering dozens of cycles, a fragile system that fit past data but had little explanatory depth.
By the late Middle Ages, the model had ballooned into an engineering feat of mathematics.
It could predict eclipses and planetary positions with reasonable accuracy, but at the cost of
baroque
complexity — an early example of
overfitting
without understanding.
The equations expanded into Fourier-like series:
$$
x(t) = \sum_i R_i \cos(\omega_i t + \phi_i), \quad
y(t) = \sum_i R_i \sin(\omega_i t + \phi_i),
$$
centuries before
Joseph Fourier
was even born.
Here’s the remarkable thing: epicycles weren’t mathematically wrong — they’re literally Fourier series in disguise.
Any periodic motion can be perfectly decomposed into circles upon circles, just as any function can be approximated by neural networks.
Ptolemaic astronomers had discovered a
universal approximator
for celestial motion.
What began as a single circle had turned into a patchwork of cycles-upon-cycles, accurate enough to guide calendars and navigation for over a millennium — yet blind to the real structure of the cosmos.
Copernicus, Kepler, and Newton
#
Nicolaus Copernicus
(1473-1543) had moved the Sun to the center, but still clung to the ancient idea of uniform circular motion.
To match observations, he still needed dozens of circles.
Mercury — the most irregular of the visible planets — demanded seven or more components in the Ptolemaic model, and nearly as many in Copernicus’s reform.
Each radius, frequency, and phase was a parameter to tweak by hand.
Add enough circles, and Mercury’s loop-de-loops appeared on parchment — but there was no deeper understanding.
Johannes Kepler
(1571-1630) shattered this tradition in 1609.
From
Tycho Brahe
’s observations, he saw that Mercury and Mars followed not circles, but
ellipses
with the Sun at one
focus
.
Suddenly, the entire path could be expressed in two simple numbers: the semi-major axis $a$ and the eccentricity $e$.
The radial distance at any angle $\theta$ became:
$$
r(\theta) = \frac{a(1 - e^2)}{1 + e \cos \theta}.
$$
For Mercury, $e \approx 0.206$.
That one number explains its
eccentric
orbit and variable speed — no towers of epicycles required.
Isaac Newton
(1643-1727) compressed this even further in 1687.
His law of gravitation,
$$
F = G\frac{m_1 m_2}{r^2},
$$
showed that Kepler’s ellipses were not arbitrary.
They were the natural consequence of a single force law applying everywhere — Earth’s apple, the Moon’s orbit, Jupiter’s moons, and Mercury alike.
What took dozens of adjustable circles in Ptolemy or Copernicus collapsed into two equations: one for the orbit, one for the force.
Neural Networks and the Age of LLMs
#
Three centuries later, we’re stacking again — but layers instead of circles. At their core, neural networks are functions built by stacking many simple transformations.
The simplest
feedforward
layer is just a linear map followed by a nonlinearity:
$$
h = \sigma(Wx + b),
$$
where $x$ is the input vector, $W$ a weight matrix, $b$ a bias term, and $\sigma$ a nonlinear activation like ReLU or sigmoid.
By chaining many such layers, we
approximate arbitrarily complex functions
.
Transformers
— the backbone of modern LLMs — replace recurrence with
attention
, letting every token compare itself to every other token in the sequence.
A single attention head computes something like:
$$
\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^\top}{\sqrt{d_k}}\right)V,
$$
where
queries
$Q$,
keys
$K$, and
values
$V$ are linear projections of the input
embeddings
.
Stack dozens of layers, each with many heads, plus billions of
parameters
in the weight matrices, and you get models like GPT-4 or Claude, each with on the order of $10^{11}–10^{12}$ tunable numbers.
These systems work because, much like Ptolemaic astronomy, you can fit almost anything if you keep adding enough components.
The more circles, the closer the match to planetary data; the more parameters, the closer the match to text statistics.
Today’s LLMs are the epicycles of intelligence: extraordinarily useful for navigation through language, capable of producing predictive charts of our symbolic universe — but like their astronomical predecessors, perhaps working well without being fundamentally correct.
In astronomy, it took two orthogonal insights — Copernicus’s heliocentrism and Kepler’s ellipses — spread over seventy years to break free from epicycles, and another eighty for Newton to reveal the logic behind them.
By analogy, we may still be in AI’s pre-Copernican era, using parameter-rich approximations that will eventually give way to a more compact and principled foundation.
Foundations to Intelligence
#
There’s no clear way to know if we’re on the wrong track.
Science is littered with confident dead ends: phlogiston theory gave way to oxygen combustion, caloric fluid to kinetic heat, luminiferous aether to relativity.
Each dominated textbooks and lecture halls until reality intervened.
Perhaps intelligence itself is irreducibly complex — evolution doesn’t optimize for elegance, after all.
But without knowing for certain, seeking deeper principles remains our best defense against drowning in parameters.
If the question is which parts of current AI might survive a paradigm shift, I’d bet on two primitives: memory and optimization.
Memory — whether as
RAG
’s retrieval, attention’s associative lookup, or biological recall — is how intelligence grounds behavior in past experience.
Optimization — whether as
gradient descent
or evolution — is how systems adapt to their environment.
These aren’t architectural choices but fundamental requirements: intelligence without memory is reactive; intelligence without optimization is static.
We’ve hardly cracked either, yet others see different primitives, like self-play, simulation, and causality.
Perhaps we’re all Keplers staring at Mars from different angles, each waiting for our ellipse to appear.
