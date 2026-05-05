---
title: "Five ways to avoid and control flaky tests"
url: "https://boyter.org/2015/07/ways-avoid-control-flaky-tests/"
fetched_at: 2026-05-05T07:02:01.865775+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# Five ways to avoid and control flaky tests

Source: https://boyter.org/2015/07/ways-avoid-control-flaky-tests/

Having a reliable test suite should always be the goal in software development. After all if you can’t trust the tests then why bother running them at all? This is especially important in a shared coding environment and when running through Continuous Integration (CI).
1 - Test in Isolation
It may seem obvious but writing focused tests which do a single thing is one of the most effective ways to avoid them being flaky. Tests which do multiple things increases the chance for failure and can make the tests non deterministic. Always remember to test features and issues in isolation.
2 - Write Helpful Error’s
When a test does fail having an error such as “Error 23: Something went wrong ¯_(ツ)_/¯” is incredibly frustrating. Firstly you need to run the test again with either a debugger or some code modifications to spot the bug which slows down development its also unprofessional. Write meaningful error messages. For example “Error: The value “a” was unexpected for this input” is a far better error. Another thing to remember is avoid swallowing the exception in languages which support exception handling.
3 - Control the Environment
Regularly run tests should run in a controlled environment which will be the same for the current test and future tests. This usually means a clean deploy, restoring databases and generally ensuring that however the application was setup originally is done again. This ensures the tests always start with the same conditions. This also ensures you have a good CI process and are able to recreate environments from scratch when required which is good development process.
4 - Fix it, delete it or mark it
A test that fails is proving its value, unless its flaky. Tests that fail randomly slow down your development process. In time they will be ignored and neglected. The moment a test is identified as failing it should be fixed. If it will take time then mark it as being flaky, remove it from the CI pipeline and investigate as part of paying down technical debt. If after time it still isn’t resolved it should be investigated to see if it is providing any actual value. Odds are if it hasn’t been fixed for a month it may be a test you can live without.
5 - Be forgiving but verify
For any integration test you need to have your tests be forgiving in how the application responds. After all submitting an image into a text field may result in an error which is probably acceptable. Other things to keep in mind are that there will be timeouts you will need to deal with. Be sure to have a reasonable length of time to wait for a response and only once this has expired to fail. Be wary of any test that waits forever for something to happen.
