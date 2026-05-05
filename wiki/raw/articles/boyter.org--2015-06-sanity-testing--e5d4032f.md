---
title: "Ben E. C. Boyter"
url: "https://boyter.org/2015/06/sanity-testing/"
fetched_at: 2026-05-05T07:02:02.640132+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# Ben E. C. Boyter

Source: https://boyter.org/2015/06/sanity-testing/

Sanity Testing
2015/06/28
(218 words)
Software sanity tests are closely associated with smoke tests. They attempt to determine if is reasonable to continue with testing a given piece of software. The objective is not to test all functionality, but to determine if there is value in doing so. You can consider it a “Should I continue to test this?” check. Sanity tests differ from smoke tests as they exist to check if new functionality has been met and existing bugs have been resolved.
Sanity tests are a way to avoid wasting time testing obviously flawed software IE is this software sane?
They are almost not automated at first but later can be made into regression tests
Sanity tests generally follow smoke tests in the build pipeline
Differ from smoke tests
Check if planned functionality works or that a bug has been resolved
Sanity tests usually have a narrow focus on a few pieces of functionality or bugs
The following examples are considered sanity tests.
Compiling and running a “Hello world!” program for a new developer environment
Checking that a calculator when given 2 + 2 produces 4 as the result
Confirming that a dialog box closes when the close button is clicked
Many consider sanity testing to be a subset of acceptance testing and one of the first layers in ensuring software quality.
