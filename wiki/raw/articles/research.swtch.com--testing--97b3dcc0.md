---
title: "Go Testing By Example"
url: "https://research.swtch.com/testing"
fetched_at: 2026-05-05T07:01:01.143126+00:00
source: "Russ Cox (research.swtch)"
tags: [blog, raw]
---

# Go Testing By Example

Source: https://research.swtch.com/testing

Go Testing By Example
Russ Cox
December 5, 2023
research.swtch.com/testing
Posted on Tuesday, December 5, 2023.
I opened GopherCon Australia in early November with the talk “Go Testing By Example”.
Being the first talk, there were some A/V issues, so I re-recorded it at home and have posted it here:
Here are the 20 tips from the talk:
Make it easy to add new test cases.
Use test coverage to find untested code.
Coverage is no substitute for thought.
Write exhaustive tests.
Separate test cases from test logic.
Look for special cases.
If you didn’t add a test, you didn’t fix the bug.
Not everything fits in a table.
Test cases can be in testdata files.
Compare against other implementations.
Make test failures readable.
If the answer can change, write code to update them.
Use
txtar
for multi-file test cases.
Annotate existing formats to create testing mini-languages.
Write parsers and printers to simplify tests.
Code quality is limited by test quality.
Scripts make good tests.
Try
rsc.io/script
for your own script-based test cases.
Improve your tests over time.
Aim for continuous deployment.
Enjoy!
