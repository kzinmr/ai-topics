---
title: "Kuiper Q-Q plot: are these the same?"
url: "https://entropicthoughts.com/kuiper-q-q-plot"
fetched_at: 2026-07-21T07:01:37.414626+00:00
source: "entropicthoughts.com"
tags: [blog, raw]
---

# Kuiper Q-Q plot: are these the same?

Source: https://entropicthoughts.com/kuiper-q-q-plot

Thanks to the random nature of … things, such a test will sometimes show the
wrong result. It can indicate our sample is special even when it is not (a false
positive; a
type I error
). It may also fail to indicate that our sample is
special even when it is (a false negative; a
type II error
).
Since type I and and type II errors trade off against each other, we cannot set
targets for both types of errors to be low. Instead, we set a target for a low
type I error (i.e. low false positive rate), and then we look for a test that
has as low a false negative as possible within that constraint. The reason we
focus on false positives is because we want to be fairly confident before we
claim a sample is special, so we prioritise rarity of false positives.
It is very common in science to pick a test that gives a false positive once
every 20 uses of the test, but the appropriate choice threshold depends on what
decisions are powered by the conclusion. For the sake of argument, let’s say we
want a type I error rate of 10 % – once in every ten applications gives a false
positive.
Then of the tests with that false positive rate, we are looking for a test with
as low type II error rate as possible, or, in statistical terminology, a test
with
high power
. The statistical power of a test is its ability to
successfully detect that a sample is special, even if it’s only very little
special so it might be hard to see.
There’s a third concern, however. For quick-and-dirty decisions, we want a
widely applicable test. This desire is in tension with the desire for a powerful
test, because narrower tests are usually more powerful, but require more thought
on when they are valid to use. We don’t want to pick up a book on statistics
before choosing a test, so we stick with tests that are widely applicable; tests
we can use almost no matter where the data comes from, as long as the sample is
random. These tests will be less powerful, but that’s a tradeoff we’re willing
to make to keep testing simple and easy.
That leaves us with three priorities for the black box that will tell samples
from reference distributions:
A low false positive rate.
Aiming for 10 %, but ideally this would be a
knob we can tweak. This is most important, because we want to be somewhat
confident in our conclusions.
A widely applicable test.
We should need to think as little as possible
about what sort of samples and reference distributions we put into the box.
A test with high power.
This stands in opposition to the above two
priorities, so we’ll have to settle with less power than ideal, but we’ll
still aim for the highest we can within the constraints at hand.
Before we get into the zoo of available tests, we should make a small technical
detour.
