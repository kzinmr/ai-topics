---
title: "Claude Fable 5.2 and Mythos 5.2 (Anthropic announcement)"
url: "https://www.anthropic.com/claude-fable-and-mythos-5-2"
source: "anthropic.com"
fetched_at: 2026-11-10T12:15:00+00:00
type: article
tags: [raw]
sha256: b7517e51c98726a8e8e7e5010803d8ff69316f801fe0a31191a5d081506404f9
---

# Claude Fable 5.2 and Mythos 5.2

Source: https://www.anthropic.com/claude-fable-and-mythos-5-2
Published: November 9, 2026

We've upgraded Claude Fable and Claude Mythos—models that are designed to tackle the most daunting technical challenges. Claude Fable 5.2 and Claude Mythos 5.2 show improvements in areas like coding, reasoning, and vision. During prerelease testing they've helped our engineers complete otherwise-infeasible software migrations, designed three working electronic devices from scratch, solved two open problems in the physics of black holes, made substantial progress on robotics evaluations, and formalized the proof of Fermat's Last Theorem in 30 hours—among many other applications we'll discuss below.

Claude Fable and Claude Mythos are the same underlying model. Fable has strong cybersecurity and biology safeguards to guard against misuse, which allows us to make it available to all users. Organizations pursuing beneficial applications in cybersecurity or biomedical research can apply for access to Mythos through our recently expanded Life Sciences and Cyber Verification Programs.

Testers have found that Fable 5.2 and Mythos 5.2 communicate more clearly than past Fable and Mythos models. They generate outputs up to 30% faster than Claude Fable 5.1 and Claude Mythos 5.1, and they're available at a lower price: $8 per million input tokens and $40 per million output tokens. Fable 5.2 and Mythos 5.2 also come with an optional fast mode, which speeds up token generation by up to 2.5 times. Fast mode is available for $16 per million input tokens and $80 per million output tokens.

Safety and alignment. To help ensure safety and alignment keep step with growing model capabilities, we ran extensive prerelease safety testing on the model that underlies Fable 5.2 and Mythos 5.2. This included developing novel evaluations that give deeper insight into specific concerning behaviors like sandbox escapes. We believe high-stakes risks from misalignment remain low, and the model performed as well as, or better than, our recent models on most alignment measures. Fable 5.2's cyber and biology safeguards are as robust as those of Fable 5.1 but produce fewer unnecessary blocks, and we have implemented our strongest-ever protections against distillation attacks. We describe more about our safety testing below, and full details can be found in the Claude Fable 5.2 and Mythos 5.2 System Card.

When to use Claude Fable 5.2 and Mythos 5.2. Fable and Mythos are best for the most ambitious, open-ended technical work. For most coding and knowledge tasks, we recommend that users start with Claude Opus 5.5, our strongest daily driver, and then switch to a different model as required, depending on the scope and complexity of the work—upward to Fable or Mythos, or downward to Claude Sonnet 5.5 or Claude Haiku 5.5. Fable 5.2 can also play the role of Advisor (where Haiku, Sonnet, or Opus models consult it to help solve harder problems) or Orchestrator (where it delegates simpler tasks to smaller models).

## Benchmark performance (Anthropic launch table)

| Benchmark (category) | Fable 5.2 | Fable 5.1 | Opus 5.5 | GPT-6 Astra | Gemini 4 Carbon |
|---|---|---|---|---|---|
| FrontierCode 2.0 (agentic coding, Xhigh) | 49.1% | 32.4% | 45.5% | 42.8% | 41.1% |
| FrontierSWE v2 (agentic coding) | 69.9% | 56.3% | 62.3% | 65.5% | 61.2% |
| AutomationBench (business workflows) | 51.4% | 31.4% | 42.5% | 41.4% | 53.9% |
| Terminal-Bench-Science 0.1 (agentic science) | 74.6% | 75.3% (Mythos 5.2) | 52.6% | 58.7% | 68.1% / 64.8% |
| CyScenarioBench (cybersecurity) | 76.3% (Mythos 5.2) | 61.7% (Mythos 5.1) | 67.6% without safeguards | 61% (GPT-6 Cyber) | — |
| CVE Rediscovery (cybersecurity) | 89.6% (Mythos 5.2) | 78.3% (Mythos 5.1) | 81.3% without safeguards | — | — |
| De novo binder design 24hr (protein design) | 85.1% (Mythos 5.2) | 79.1% (Mythos 5.1) | 82.6% without safeguards | — | — |

## HN discussion highlights (item 50429068, 660 pts / 840 comments)

- [shmoil] "Was this before you lobotomized Opus 5.5 or after?" — questioning whether the Opus 5.5 comparison row uses current or launch-time Opus numbers.
- [minimaxir] "most of the benchmarks don't line up anymore because the benchmarks have changed" relative to the original Opus 5.5 announcement; Humanity's Last Exam result does match.
- [minimaxir] Leaks had said the release would be called Fable 5.5; "Fable 5.2 being better than Opus 5.5 is confusing." Model immediately available in Claude Code.
- [bhu8] Pricing and speed differ from 5.1 → suggests a different architecture/size; "this is probably Model 3 from METR's report" (metr.org blog 2026-11-05, Anthropic AI-R&D acceleration).
- [LeBit] "$200USD is a lot of money… might explain why DeepSeek Flash v4.1 1017 is the most popular model at OpenRouter."
- [mortalapeman] "What you need for real engineering and scaling is cheap and just enough smarts… GPT-6 Luna cheap enough that I can pretend the cost doesn't exist."

## Companion: Anthropic prompting guidance (via Simon Willison, 2026-11-10)

From "Prompting Claude Fable 5.2" (Anthropic documentation): Claude Fable 5.2 responds closely to what the
prompt says about who owns the code it works on. When a prompt said nothing about ownership or presented the
codebase as someone else's, the model tended to add to the existing structure, even repeating existing code.
To make it improve structure as it works: "This codebase is yours: what it's for and how it's built are your
call, and you'll keep building on it." In Anthropic's small-coding-task testing, the model merged repeated
code in about half of the tries with this sentence, and in under a tenth of the tries without it.
