---
title: "Grouping Tests: Unit/Integration vs Fast/Slow Tests"
url: "https://boyter.org/2015/06/grouping-tests-unitintegration-fastslow-tests/"
fetched_at: 2026-05-05T07:02:02.628236+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# Grouping Tests: Unit/Integration vs Fast/Slow Tests

Source: https://boyter.org/2015/06/grouping-tests-unitintegration-fastslow-tests/

There is a great deal of argument in the testing community over how to label tests. One camp likes to label tests using levels such that unit tests are in one group, integration in another and so forth. The other likes to label them based on how long they take to run ignoring what level they are in. Fast tests are those that run in milliseconds while slow take longer then this. The reason this is important is that when adopting a testing process slow and flaky tests (those which fail often) are the enemy. Slow tests tend to be run less often in the development process. A delay of a few seconds can seriously interrupt a developer or testers workflow. Also the more often your tests fail randomly the less confidence you are likely to have in them, ignoring genuine errors until they fail multiple times.
Its worth keeping in mind that unit tests are less likely to become flaky or fail but if they take a long time to run its unlikely developers will run them before every check in.
Personally I prefer the latter approach.
Getting hung up on the pureness of your unit tests is usually an impediment to progress. Not all unit tests run quickly (although they should run consistently!) just as not all integration tests are slow. By dividing tests into those expected to run quickly and those slowly you can ensure that you run the majority of your tests more often.
An example of a slow running unit test I encountered was for some image recognition software I was working on. There was some fairly involved math in a few functions that slowed down the test to hundreds of milliseconds. Not a huge issue by itself, but it was compounded by having to test this function thousands of times for various edge cases. The result was a test that took almost a minute to run. Technically it was correct (the best kind of correct) to call it a unit test but it was not something you wanted to run for every change. Labelling it as a slow test sped up the development process considerably.
An example of a fast running integration test was a function responsible for writing the current date time to a file on disk as a heart beat check. Doing a pure unit test of this function would have required either mocking away the file system or building wrappers over low level disk access methods. However the test only needed to be run once and ran in less than 50 milliseconds on every piece of hardware tested. It was categorised as being a fast test and as such was run very frequently. Incidentally this turned out to be a boon later on as it was discovered after several months that there were a few exception cases not handled correctly that caused the test to fail. It turned out that this simple error could have caused some cascading failures of the production stack and some serious down time! It was unlikely that this would have been picked up had the test been less often.
