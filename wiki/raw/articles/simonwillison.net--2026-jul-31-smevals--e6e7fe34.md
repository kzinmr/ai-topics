---
title: "a small eval suite for evaluating models, prompts, and harnesses"
url: "https://simonwillison.net/2026/Jul/31/smevals/#atom-everything"
fetched_at: 2026-08-01T10:13:01.357902+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# a small eval suite for evaluating models, prompts, and harnesses

Source: https://simonwillison.net/2026/Jul/31/smevals/#atom-everything

31st July 2026 - Link Blog
smevals - a small eval suite for evaluating models, prompts, and harnesses
. I've been working with Jesse Vincent's
Prime Radiant
applied AI research lab building out this evals framework to help answer questions about the capabilities of different models.
The result is
smevals
, a new tool for running small eval suites across different model configurations and grading the results.
The
blog entry
describes the tool in detail. Here's the 10 second version:
Tell your coding agent to
run uvx smevals docs
to learn the tool (this outputs
the README
)
Then tell it to build you an eval suite
Once you've created an eval - which takes the form of a directory with some YAML files - you can run it against models like this:
uvx smevals run path-to-eval/ -m gpt-5.5 -m claude-opus-4.6
Runs are treated separately from grading operations - you can grade your runs (against your defined set of checks) using:
uvx smevals grade path-to-eval/
Then you can run a localhost web server to explore the results:
uvx smevals serve path-to-eval/
Or run the
smevals build
command to build that report as static HTML, which you can then host anywhere. Here's
an example
showing an eval suite I built to evaluate how well models can write haikus.
The most time-consuming part of this project was figuring out the vocabulary for it! Here's what I settled on, quoted from the announcement:
An
eval
is a collection of challenges designed to answer a question about a model, for example, how good is that model at generating SVGs?
Each eval is a collection of
tasks
. A task is a specific challenge, for example "Generate an SVG of a pelican riding a bicycle".
When you run the eval you do so against one or more
configs
. Each config specifies a model to be evaluated, but may also include other parameters to test, such as different system prompts, model parameters, or agent harnesses.
A
run
records what happened when a specific config was used to execute a specific task. A
runner
is the script that executes a run.
Once you have collected one or more runs, you need to evaluate the results to see how well the model (or config) did. This is done by a
grader
, which produces a
grade
.
Each grader runs a sequence of
checks
. These can be simple operations, like checking for a specific string in the output, or confirming that the output is valid XML. They can also be more complicated custom operations (implemented as scripts called
checkers
), including using other models to answer questions about the run.
I've been trying to figure out an approach I like for evals for several years now.
smevals
is my third iteration on the idea and it feels right to me. I'm looking forward to expanding this more in the future, as well as pointing it at some of my own projects.
