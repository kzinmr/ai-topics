---
title: "A new era for software testing"
url: "http://antirez.com/news/168"
fetched_at: 2026-06-08T07:01:16.719430+00:00
source: "antirez.com"
tags: [blog, raw]
---

# A new era for software testing

Source: http://antirez.com/news/168

antirez
21 hours ago. 18457 views.
Automatic programming dramatically speeds up writing software in certain use cases and in the right hands. In my experience the output does not reach the structural quality and economy of complexity of the best hand-written software. However, not all the software is stellar, and my feeling is that automatic programming surpasses most of the times (and if well managed) the quality of decently developed hand-written code.

Yet, there is a tradeoff between quality and time, in the case of writing new software with AI. This tradeoff in certain projects I developed can be brutal, that is, completing projects that may take many months in a few weeks. However, there are domains where LLMs simply open new strictly more powerful ways to automate processes, without any compromise on quality. One of those domains is software QA and testing.

Traditionally software is tested using test suites that are composed of locally-scoped tests and integration tests (think of Redis: one thing is testing if SET foo 10 will be matched by GET foo => 10, another thing is testing if replication works in this case). And then by QA passes that are usually manually executed, and that can capture holes in the runnable test suite. It is a known fact that covering all the lines of the code does not mean covering all the possible states. Moreover integration testing is structurally hard: there are a number of timing issues, setups, and certain quality outputs that can only be visually inspected and not automatically checked that leave a lot of testing opportunities not really exploited because of time or logistic constraints.

LLMs offer a new way to do QA on top of the existing testing methodologies. The idea is to create a markdown file where an AI agent is asked to work as a QA engineer, performing a number of manual testings on the new release. For instance, in the case of DwarfStar (an inference engine for open weights LLMs) I use the following approach. In the markdown file, the agent is asked to check what are the new commits on top of the already released version of the software project. Then the model is told a list of things that should be performed, like:

- Check that distributed inference works across MacBook A and MacBook B, making sure the output is coherent, the inference works with all the GGUF files we have in both the machines, ...
- Make sure this release does not contain any speed regression.

And so forth. Notably, in the speed regression part, I don't have to tell the agent what was the previous expected speed, as this is a moving target that changes with new releases and new optimizations. Similarly the integration test for distributed inference does not require many instructions, at the start of the file there are just SSH endpoints and the key to use, the paths, and so forth.

The agent is asked to check the long list of QA activities *especially* in light of the added commits, starting with an inspection of the changes and with the identification of what could be affected, so that the QA pass specializes trying to find specific regressions.

In the case of Redis Arrays, I used a similar methodology asking the agent to build a large array-based Redis application, to setup a production environment with replication and persistency, to simulate the usage of the application for days and with many users, checking if something was odd.

Testing that uses these approaches may also move in the more psychological side of software quality, asking the agent to identify all the new features that may look surprising, not documented enough, or generally sloppy from the POV of the user. All things that needed to be executed manually before, and that most of the times were mostly skipped.

I have the feeling that the introduction of automatic QA may raise the bar of quality for new releases of software, and maybe partially compensate for the lower quality of the code produced at high speed with the use of automatic programming.
