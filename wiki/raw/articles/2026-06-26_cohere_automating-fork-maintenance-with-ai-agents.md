---
title: "Automating fork maintenance with AI agents"
source: "Cohere Blog"
url: "https://cohere.com/blog/automating-fork-maintenance-with-ai-agents"
scraped: "2026-06-26T06:00:29.864615+00:00"
lastmod: "2026-06-25"
type: "sitemap"
---

# Automating fork maintenance with AI agents

**Source**: [https://cohere.com/blog/automating-fork-maintenance-with-ai-agents](https://cohere.com/blog/automating-fork-maintenance-with-ai-agents)

You maintain a fork. Upstream moves. You sync, things break, you fix them, you verify, you ship. A few weeks later, upstream moves again. The cycle repeats.
This post describes a general method for automating that cycle using AI coding agents. We apply it to our fork of vLLM, walking through a concrete case where a routine upstream release silently broke Cohere's
cohere-transcribe-03-2026
ASR model on our fork, with the fix flowing back upstream as a vLLM PR.
In practice, this approach has compressed the time to absorb a new upstream release from
weeks to days
, with humans only reviewing the outcome. The skills powering this workflow are open-sourced at
cohere-ai/vllm-skills
.
The problem
Maintaining a long-lived fork of an actively developed project is a recurring cost. But upstream releases also carry features, performance improvements, and bug fixes that you want. Staying in sync is not just maintenance, it's how the fork keeps getting better. The problem is that every upstream release also introduces a
disturbance
: merge conflicts, changed APIs, removed functions, new dependencies, or broken tests. The fork maintainer's job is to absorb that disturbance and restore a working state.
The structure of this work is always the same:
Sync
the new upstream version into the fork.
Measure
by running tests, benchmarks, evals to see what broke.
Fix
conflicts, adapt to API changes, update tests.
Repeat
steps 2 to 3 until everything passes.
Ship
the updated fork.
This is a feedback loop. It already exists in every team that maintains a fork; it's just slow and manual. For our vLLM fork, absorbing a typical upstream release used to take weeks of intermittent developer attention, and the goal of the work described below is to bring that down to days of mostly unattended agent time.
Feedback systems
In control theory, a
closed-loop system
continuously compares its output to a reference and adjusts to close the gap. But real systems also face
disturbances
: external inputs that push the system away from its desired state.
r(t)
is the reference, the desired value that the system should produce.
y(t)
is the output, the actual value that the system produces.
e(t)
is the error, the gap between reference and measurement, computed as r(t) − measured_output.
d(t)
is a disturbance, an external force acting on the system that pushes the output away from the reference.
The controller uses the error to adjust the system; the feedback brings output closer to the target. A well-designed feedback loop doesn't just track the reference; it
rejects disturbances
by detecting their effect on the output and driving the error back toward zero without manual intervention.
Cruise control is the textbook example. You set a desired speed (reference), the car maintains it (system), but a hill or headwind appears (disturbance). A good controller notices the speed drop and adjusts throttle automatically.
Fork maintenance has exactly the same structure.
Control theory
Fork maintenance
r(t), reference
Custom changes working correctly on the latest upstream
d(t), disturbance
New upstream release: conflicts, API changes, breaking changes
Controller
Resolve conflicts, update patches, fix tests
System
The fork itself (code, tests, CI)
y(t), output
Runtime behavior of the fork after syncing
Measurement
Test suite, benchmarks, evals
e(t), error
Delta between expected behavior and actual post-sync behavior
The goal is to automate the entire loop —
sync, measure, fix, repeat
— so we can absorb upstream improvements with minimal human intervention.
Our pre-agent process
There are several ways to sync a fork with upstream:
merge
,
cherry-pick
, and
rebase
are the most common. Merge preserves both histories, but produces a tangled commit graph that makes it hard to tell custom changes from upstream. Cherry-pick gives precise control, but doesn't scale when upstream moves hundreds of commits per release; you end up maintaining a growing list of picks that drifts out of sync. Rebase replays your custom commits on top of the new upstream tag, producing a clean, linear history where your patches sit clearly on top. The tradeoff is that rebase rewrites history and forces a force-push, but for a fork with a small number of custom commits on top of a fast-moving upstream, the clarity is worth it.
At Cohere, we settled on rebase early on. Before the agent-based workflow described below, our pipeline already mixed scripted automation with manual work.
Rebase:
A GitHub Actions workflow attempts the rebase onto a target upstream tag, replaying previously-seen conflict resolutions from a shared
git rerere
cache.
Resolve conflicts:
When the workflow's automated rebase fails, a developer picks up locally, resolves the remaining conflicts by hand (often with an LLM assistant), verifies CI, and uploads the updated rerere cache.
Verify and ship:
Once CI is green on the rebased branch, it becomes the new base for the fork.
This process already combines several kinds of automation:
git rerere
replays known resolutions, GitHub Actions runs the rebase attempt and CI, and LLMs assist with individual coding and debugging tasks. But the human is still part of the controller, stitching the pieces together, choosing which fixes to apply, and deciding when to re-run. The feedback loop works; it just turns slowly. The agent-based workflow described below keeps the same structure, but lets an agent play the controller role, so iterations happen at machine speed and humans only intervene at the edges.
Automating each component
This method decomposes the loop into three, agent-automatable components. Each maps to a piece of the control diagram.
1. Disturbance injection
An agent skill detects and applies new upstream releases. It rebases the fork onto the new tag and resolves merge conflicts automatically. This is the disturbance entering the system: a deliberate, automated action that we know will temporarily break things, but that we want to absorb as quickly as possible.
The skill needs to:
Detect which upstream tag the fork is currently based on
Check whether a newer tag exists
Perform
git rebase --onto
with the fork's custom commits
Resolve conflicts (using upstream diff context to make informed decisions)
2. Measurement collection
After a rebase, the fork is in an unknown state. Measurement tells you how far you are from the goal: a working fork with all custom behavior intact. Without it, the agent is flying blind.
The measurements themselves (tests, benchmarks, evals) are defined by the project and already exist before any automation. What the agent automates is
collecting
them: a test-runner skill that knows how to set up the environment, execute the verification suite, and report results.
Tests
: Unit, integration, and correctness tests
Benchmarks
: Performance checks (throughput, latency, resource usage)
Evals
: Domain-specific quality metrics (accuracy, perplexity, task scores)
The output is the error signal: which tests fail, which benchmarks regress, which evals degrade. The richer and more reliable the measurements, the faster the controller can converge. A fork with a thin test suite gives a weak signal; the agent won't know what's broken or how close it is to done.
3. Controller
An agent skill closes the loop. After the rebase lands and measurement results come back, the skill:
Reads test and benchmark results
Identifies failures and regressions
Applies fixes (resolve build errors, update broken tests, adapt to API changes)
Re-runs measurement
Repeats until all measurements pass, or escalates to a human
This is the controller driving the error to zero. The key insight is that the agent doesn't need to get the rebase right on the first try, it just needs to iterate — exactly like a developer would.
Case study: vLLM
vLLM
is an open-source LLM serving engine. At Cohere, we use it across the inference stack, from RL rollouts and evals during model development to serving user requests in production. We maintain a fork to carry custom commits — additional model support, custom kernels and optimizations, modified entrypoints, extra tests — some of which are in the process of being upstreamed, others specific to our needs. The challenge is replaying those commits onto each new upstream release without breaking anything. Upstream cuts a release roughly every few weeks, and each one is substantial: the diff between tags often touches hundreds of files.
The skill stack
We built five skills, open-sourced at
cohere-ai/vllm-skills
, that instantiate the general pattern. Each skill is a markdown document that a coding agent reads and executes interactively, with access to the terminal, file system, and the tools it needs.
Skill
Role in the loop
What it does
install-vllm
Environment setup
Creates a uv virtualenv, installs vLLM in editable mode with the correct precompiled CUDA wheel
local-test-runner
Measurement
Runs Buildkite CI-equivalent tests locally on NVIDIA GPUs; parses .buildkite/test_areas/*.yaml, manages HuggingFace tokens, captures logs
detect-upstream-base
Disturbance detection
Finds the upstream tag (v1) the fork is currently based on via git merge-base + git describe
rebase-assistant
Controller
Rebases custom commits from v1 onto v2, resolves conflicts using upstream diffs for context, verifies the result with test-runner
auto-rebase
Orchestrator
Checks for new upstream releases via gh, invokes detect-upstream-base and rebase-assistant end-to-end
How a rebase runs
Throughout this section:
v1
/
v2
are the old and new upstream tags, and
b1
/
b2
are the fork branches before and after the rebase.
A typical invocation:
"
/auto-rebase sync
the current branch with the latest upstream release and make sure
<test>
passes."
auto-rebase
checks prerequisites (
gh auth status
), then invokes
detect-upstream-base
to find v1 (e.g.,
v0.19.0
).
It fetches upstream tags and discovers v2 (
v0.19.1
). It presents the release to the user and waits for confirmation.
It collects verification checks from the user (e.g.,
pytest tests/entrypoints/openai/correctness/test_transcription_api_correctness.py
).
It invokes
rebase-assistant
, which:
Analyzes the custom commits on b1 (
git log v1..HEAD
)
Verifies that tests pass on b1 first (using
local-test-runner
with the v1 wheel), which is the gate that ensures we have a known-good baseline
Backs up b1, creates b2, optionally squashes custom commits
Runs
git rebase --onto upstream/v0.19.1 <fork-point> HEAD
Resolves conflicts by comparing
upstream/v1..upstream/v2
diffs to understand what changed
Runs tests on b2 (using
local-test-runner
with the v2 wheel)
If tests fail: inspects failures, compares against the v1 baseline, applies fixes, and re-runs (the inner feedback loop)
Once all checks pass,
auto-rebase
presents a summary (commits replayed, conflicts resolved, test results) and offers to push.
As a sequence of skill interactions:
The inner loop is the controller iterating on b2: local-test-runner reports a failure, rebase-assistant applies a fix and re-runs until the tests pass.
Worked example: Cohere Transcribe on v0.19.1
Here is a real invocation of this loop, end to end.
Setup:
Our fork sits at
cohere-transcribe-v0.19.0
, one custom commit on top of upstream
v0.19.0
that enables a correctness test for Cohere's
cohere-transcribe-03-2026
ASR model. vLLM added support for this model architecture in
v0.19.0
, but the upstream test was commented out because the weights weren't published yet. Our custom commit just un-comments one line.
# TODO (ekagra): turn on after asr release
# CohereASR is used to test the variable encoder length code paths
(
"CohereLabs/cohere-transcribe-03-2026"
,
11.92
),
The test runs the model over a filtered slice of the earnings-22 validation set and asserts WER ≤ 11.92. That single number is our measurement signal
y(t)
. When the fork is healthy, the number sits near 11.92; when something is broken, it blows up.
Disturbance:
Upstream cuts
v0.19.1
. It's an incremental release, but not a small one: it includes a
transformers
version upgrade and related refactors. We run auto-rebase with one prompt.
/auto-rebase
let
's sync current branch with latest upstream release,
make sure the test CohereLabs/cohere-transcribe-03-2026 passes
@tests/entrypoints/openai/correctness/test_transcription_api_correctness.py:172-173
Result:
After rebasing the custom commit onto
v0.19.1
and re-running the test on b2, the result came back as
WER = 100
— complete failure, the model emitting garbage.
The controller loop diagnosed the regression: rebase-assistant diffed
upstream/v0.19.0..upstream/v0.19.1
, traced the failure to a bumped
transformers
version that changed how the model's tokenizer handled its prompt prefix, and applied a quick fix to work around it. WER returned to ~11.92 and the fork was green on
v0.19.1
within a single interactive session.
The loop worked end to end: a disturbance arrived, the controller absorbed it, and the fork was back to a healthy state automatically.
Follow-up:
Because the bug affected every downstream user of this model, we submitted
vllm-project/vllm#40582
to turn the workaround into a proper upstream fix. Once merged, the next release will no longer require a fork patch for this model; the disturbance is gone for everyone.
Beyond vLLM
The same closed-loop structure applies whenever a codebase absorbs an external change and needs to converge back to a working state.
Another recent example is our internal fork of HuggingFace transformers, where we maintain
command-a-plus-05-2026
ahead of its public release. When
transformers v5
landed with deprecated arguments removed, new required signatures, and changed tokenizer behavior, all of that was the disturbance. The same loop applied: upgrade to v5, run the model's correctness evals and generation tests, and let an agent iterate on the failures. Several issues surfaced across import paths, API calls, and tokenizer defaults; some were fixed autonomously, others required a human in the loop to resolve. The cycle continued until the model generated correctly on v5 before the public release.
The skills were different, but the structure was identical: introduce the change, measure the gap, close the loop.
Conclusion
The structure of fork maintenance doesn't change: sync, measure, fix, repeat. What changes is how fast the loop turns.
Before the agent-based workflow, syncing our vLLM fork with a new upstream release took
weeks
: waiting for someone to context-switch in, manually triaging conflicts, re-running CI, and debugging failures one at a time. With auto-rebase driving the controller loop, that timeline has compressed to
days
. And because the expected measurements are preset in the repo, the full pipeline runs without human input; a person only needs to review the outcome.
The method generalizes to any fork with a measurable definition of "working": detect the disturbance, collect measurements, and let an agent iterate on the error. The skills are composable and the control-theory framing makes it straightforward to adapt them to new codebases.
The skills described in this post are open-sourced at
cohere-ai/vllm-skills
. If you maintain a fork and want to try the approach, start by writing a measurement (a test, a benchmark, an eval) that captures what "healthy" means for your fork. The rest of the loop follows from there.
Acknowledgements
Thanks to Ekagra Ranjan for assisting with the Cohere Transcribe experiments, Zhoujie Zhao and Walter Beller-Morales for helping shape the agent skills, and Bharat Venkitesh for supporting this work.
Blog
Written By
Donglu Wang
Member of Technical Staff, Foundations
Tags
Technology
AI for Developers
Share
AI isn’t a shortcut.
It’s how business gets ahead.
Contact sales
