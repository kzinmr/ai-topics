---
title: "Running three hours of Ruby tests in under three minutes"
url: "https://boyter.org/2015/08/running-hours-ruby-tests-minutes/"
fetched_at: 2026-05-05T07:02:01.686470+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# Running three hours of Ruby tests in under three minutes

Source: https://boyter.org/2015/08/running-hours-ruby-tests-minutes/

Running three hours of Ruby tests in under three minutes
2015/08/18
(135 words)
Recently the very cool hard working developers working on Stripe released a post about how they modified their build/test pipeline to reduce their test suite runtime from 3 hours to about 3 minutes.
The article is very
much worth reading
, as is the discussions that have come around it including those on
Hacker News
.
A few key takeaways,
For dynamic languages such as Ruby or Python consider forking to run tests in parallel
Forks are usually faster then threads in these cases and provide good test isolation
For integration tests use docker which allows you to revert the file system easily
The above ensures that the tests are generally more reliable and you avoid having to write your own teardown code which restores state, both in memory for the forks and on disk using Docker.
