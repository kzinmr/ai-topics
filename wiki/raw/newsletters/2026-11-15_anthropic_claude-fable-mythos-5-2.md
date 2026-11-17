---
title: "Introducing Claude Fable 5.2 and Claude Mythos 5.2 (Anthropic official)"
date: 2026-11-15
source: https://www.anthropic.com/claude-fable-and-mythos-5-2
fetched_at: 2026-11-16T10:59:23.228944+00:00
tags: [newsletter, raw, full-body, company-announcement]
---

# Introducing Claude Fable 5.2 and Claude Mythos 5.2 — Anthropic (official announcement)

_Full body extracted via curl + `<article>` extraction. Captured during newsletter-wiki-ingest run 20261116T103431Z (The Signal 2026-11-15 issue referenced it; sitemap-monitor had not captured it)._

We’ve upgraded Claude Fable and Claude Mythos—models that are designed to tackle the most daunting technical challenges.

Claude Fable 5.2 and Claude Mythos 5.2 show improvements in areas like coding, reasoning, and vision. During prerelease testing they’ve helped our engineers complete otherwise-infeasible software migrations, designed three working electronic devices from scratch, solved two open problems in the physics of black holes, made substantial progress on robotics evaluations, and formalized the proof of Fermat’s Last Theorem in 30 hours—among many other applications we’ll discuss below.

Claude Fable and Claude Mythos are the same underlying model. Fable has strong cybersecurity and biology safeguards to guard against misuse, which allows us to make it available to all users. Organizations pursuing beneficial applications in cybersecurity or biomedical research can apply for access to Mythos through our recently expanded Life Sciences and Cyber Verification Programs.

Testers have found that Fable 5.2 and Mythos 5.2 communicate more clearly than past Fable and Mythos models. They generate outputs up to 30% faster than Claude Fable 5.1 and Claude Mythos 5.1, and they’re available at a lower price: $8 per million input tokens and $40 per million output tokens.

Fable 5.2 and Mythos 5.2 also come with an optional fast mode, which speeds up token generation by up to 2.5 times. Fast mode is available for $16 per million input tokens and $80 per million output tokens.

Safety and alignment. To help ensure safety and alignment keep step with growing model capabilities, we ran extensive prerelease safety testing on the model that underlies Fable 5.2 and Mythos 5.2. This included developing novel evaluations that give deeper insight into specific concerning behaviors like sandbox escapes. We believe high-stakes risks from misalignment remain low, and the model performed as well as, or better than, our recent models on most alignment measures. Fable 5.2’s cyber and biology safeguards are as robust as those of Fable 5.1 but produce fewer unnecessary blocks, and we have implemented our strongest-ever protections against distillation attacks.

We describe more about our safety testing below, and full details can be found in the Claude Fable 5.2 and Mythos 5.2 System Card.

When to use Claude Fable 5.2 and Mythos 5.2. Fable and Mythos are best for the most ambitious, open-ended technical work. For most coding and knowledge tasks, we recommend that users start with Claude Opus 5.5, our strongest daily driver, and then switch to a different model as required, depending on the scope and complexity of their work—upward to Fable or Mythos, or downward to Claude Sonnet 5.5 or Claude Haiku 5.5. Fable 5.2 can also play the role of Advisor (where Haiku, Sonnet, or Opus models consult it to help solve harder problems) or Orchestrator (where it delegates simpler tasks to smaller models).

Benchmark performance. The benchmarks table below shows that Claude Fable 5.2 and Mythos 5.2 are a step above Opus 5.5 in almost all the capabilities we evaluated:

For details on evaluation methodology, see the Claude Fable 5.2 and Claude Mythos 5.2 System Card. Scores for Fable 5.2, Fable 5.1, and Opus 5.5 show results with safeguards on unless otherwise noted. All scores show each model’s highest-available effort unless otherwise noted. † On CyScenarioBench, each lab’s scores are based on unique tasks. ‡ RoboDojo Sim shows the highest-available effort and was run internally.

Effort and efficiency. On Medium effort (the default in Claude apps and Claude Code), Fable 5.2 can accomplish challenging tasks with fewer tokens than Fable 5.1. In early testing on the FrontierCode 2.0 evaluation, Fable 5.2 at High effort scored about level with Opus 5.5 at Max effort, for roughly half the cost per task. At Xhigh effort, it also scored the highest of any released model tested.

Fable 5.2Opus 5.5Fable 5.1GPT-6 AstraGemini 4 Carbon10203040500Score (%)125102050Cost per task (USD, log scale)LowMedHighXhighMaxFrontierCode measures whether a model’s code changes would be merged by the maintainers of open-source repositories. At High effort, Fable 5.2 scores about the same as Opus 5.5’s best score (45.3% vs. 45.5%) for roughly half the cost per task, and ahead of GPT-6 Astra’s best score (42.8%) at about the same cost. At Xhigh effort, Fable 5.2 reaches 49.1%, the highest score of any released model we’ve tested.

Fable 5.2Opus 5.5Fable 5.1304050607080900Score (%)125102050Cost per attempt (USD, log scale)LowMedHighXhighMaxPerplexity’s WANDR benchmark measures agents on large data-collection tasks. At Medium effort, Fable 5.2 matches Opus 5.5’s top score for about 40% of the cost per task.

Fable 5.2Opus 5.5Fable 5.1020406080Score (0–100)0.030.100.30131030Cost per attempt (USD, log scale)LowMedHighXhighMaxBenchCAD 2.1 measures hardware engineering, specifically how closely a model’s designs match reference geometry and circuits, and is scored 0–100 with partial credit. At Max effort, Fable 5.2 scores 83.5, ahead of Opus 5.5 (65.3) and Fable 5.1 (44.4).

Fable 5.2Opus 5.5Fable 5.1506070800Score (%)0.100.200.50125Cost per attempt (USD, log scale)GPT-6 Astra (Max): 57.2%LowMedHighXhighMaxHumanity’s Last Exam (HLE) is a test of expert-level academic knowledge and reasoning. At Low effort, Fable 5.2 matches Opus 5.5’s top score for less than one-tenth of the cost per task.

Fable 5.2Opus 5.5Fable 5.13040506070800Score (%)0.020.050.100.200.501Cost per attempt (USD, log scale)GPT-6 Astra (Max): 71.0%Gemini 4 Carbon: 72.5%LowMedHighXhighMaxChartography tests how accurately a model can read charts and figures. At Medium effort, Fable 5.2 scores 66.4%, ahead of Opus 5.5 at Max effort (64.4%) for less than one-tenth of the cost per task.

Over 90% of the changes merged into Anthropic’s core codebase are now written by Claude (with human guidance). We’ve used Fable 5.2 to fix stubborn bugs in minutes, optimize performance across all of our services, and complete high-value software projects that would otherwise have been too slow or too costly to attempt. A team of agents running an earlier version of Fable 5.2 migrated a critical production service from Python to Rust—the service is now more efficient, more reliable, and starts about 26 times faster. We’ve found that Fable 5.2 exercises strong engineering judgment and can produce high-quality results from even ambiguous requests.

As an experiment, one Anthropic engineer gave Fable 5.2 the task of designing a prototype operating system. Starting from an empty folder, the model coordinated over 1,000 subagents, working around the clock for eight days writing, testing, and reviewing code. It produced a working operating system that boots on a laptop, with its own core that runs the machine, drivers for the disk, keyboard, and network, permanent file storage, windows, a login screen, an installer, and built-in Claude functionality (see the video below).

Early testers have been impressed at how successfully Fable 5.2’s coding skills can be applied to a wide range of tasks:

“The model is in my head. It understands the intent behind every prompt I’ve given it. I haven’t had to say ‘No, I meant…’ a single time. Projects we’ve been pushing along with other models for weeks got finished and approved by our teammates in a few days with Claude Fable 5.2, and the humans reviewing its code had less to say.”
