---
title: "Catch Flakes On Main"
url: "https://matklad.github.io/2026/05/14/catch-flakes-on-main.html"
fetched_at: 2026-05-15T07:01:01.338588+00:00
source: "matklad.github.io"
tags: [blog, raw]
---

# Catch Flakes On Main

Source: https://matklad.github.io/2026/05/14/catch-flakes-on-main.html

Catch Flakes On Main
May 14, 2026
A small
Mechanical Habit
today:
When using not rocket science rule / merge queue, continue to
              redundantly run the full test suite on main. Maintain an easily
              accessible list of recent main failures — these are the flaky
              tests to eradicate.
For an example, see the “Flakes” link on
https://devhub.tigerbeetle.com
Flaky tests are tests that fail intermittently, once in a thousand
          runs. This might be due to a genuine bug (assumptions about scheduling
          that
mostly
hold) or due to instability of underlying
          infrastructure (e.g., inability to download a release from GitHub, or
          to delete a folder on Windows). In either case, flaky tests are a huge
          productivity drain — as the size and complexity of test suite grows,
          more and more CI runs fail spuriously, even as each individual test
          almost always passes.
Flaky tests are challenging to deal with — if you are working on
          landing a PR and your CI fails due to an obvious flake, the temptation
          to just re-run the test suite is enormous, especially if there’s a
          certain background dissatisfaction with infrastructure stability.
If you are of a mind to do some flake squashing, then your PRs will be
          green just to spite you! And working off of others’ PRs would require
          first to separate flakes from genuine failures.
This is why the merge queue is powerful: if there’s a guarantee that
          every commit on the main branch passes the tests, then every failure
          on main is a flake, by definition. Collecting all such failures into a
          single list compresses time, allows to prioritize the most impactful
          sources of instability, and reveals correlations between failures.
