---
title: "The Problem is Prompt Debt"
source_url: "https://www.dbreunig.com/2026/06/22/the-problem-is-prompt-debt.html"
date: 2026-06-22
author: "Drew Breunig"
captured: 2026-06-25
---

### You can't be model agnostic if you're hand-tuning prompts

![](/img/proust.jpg)

Thanks to natural language interfaces, AI applications can be prototyped quickly. You write what you want in English, hand it to a frontier model, and a working prototype appears in an afternoon. This is extraordinarily powerful and for one-off tasks, optimal. But as a way to build reliable systems, the natural language prompt is a trap. 

The plain-English prompt that makes prototypes effortless turns out to be a poor way to specify how a system should behave, and the bill arrives slowly, disguised as ordinary progress, until the application can barely move. The problem is not any single prompt. It is that natural language was never meant to be a specification language for engineering, and treating it as one quietly caps what you can build.

#### **The Prompt Debt Trap**

The first symptom of prompt debt is slowing iteration. As users flag errors and spot edge cases, additional guidance is added to the instructions, nudging the model into line. If unwanted behaviors persist, instructions are repeated, with increasing severity. Pretty soon, the prompt isn't straightforward and quick fixes regress previous instructions. Errors can no longer be handled with one-line "hot fixes" and your development cycle slows to a crawl.

![Fable's system prompt repeats copyright guidance up to six times, with increasing severity](/img/fable_prompt_short.jpg)
<p class="image-caption">Fable's system prompt repeats copyright guidance up to six times, under sections named <code>search_instructions</code>, <code>search_usage_guidelines</code>, <code>mandatory_copyright_requirements</code>, <code>hard_limits</code>, <code>self_check_before_responding</code>, and <code>critical_reminders</code>.</p>

Next, prompt debt incapacitates your team. Your brittle prompt [full of edge cases and all-caps threats](https://www.dbreunig.com/2026/02/10/system-prompts-define-the-agent-as-much-as-the-model.html#:~:text=The%20Common%20Jobs%20of%20a%20Coding%20Agent%20System%20Prompt) is barely legible to you, and it's downright impenetrable to your colleagues. Many teams mitigate this issue by breaking prompts into complicated templates assembled at run-time, each isolated to specific concerns. But these prompt segments evolve, too, growing into [a thicket of conditions](https://www.dbreunig.com/2026/04/04/how-claude-code-builds-a-system-prompt.html).

Finally, prompt debt ties you to a single model. Your hot fixes work on GPT-4o, but fail in entirely new ways when you point your inference call at GPT-5.4-mini. So you stay with 4o, hope the increasingly frequent deprecation emails from your inference provider are empty threats, and forgo the possibility of potentially cheaper, faster, *better* models. A [recent report from Datadog](https://www.datadoghq.com/state-of-ai-engineering/) suggests this is a common situation: the most-used model in traffic they observed is *GPT-4o*[^4o].

[^4o]: This stat from Datadog is from March of this year, so GPT-4o concentration has likely dropped a bit. However, I've heard from multiple large inference providers that usage of GPT-4o and models of similar vintage can be higher than *50%* of all calls!

Any one of these issues is a nuisance, but together they are the difference between a glorified prototype and a product that can grow with you, your customers, and your business. Your shiny new AI features are frozen, can only be improved through a full rebuild, and are locked to an aging model.

#### **Why Prompt Debt Happens**

Natural language interfaces are wonderful. They're the right mechanism for one-off tasks and broad conversational threads. We get into trouble when we rely on natural language to define durable system behavior. 

The imprecision of natural language paired with probabilistic language models means different words expressing the same intent, can yield different outputs. [In a recent study](https://arxiv.org/abs/2604.07709), a clinical question asked in a patient's voice and then re-asked in a physician's, with identical facts, flipped Opus from declining all ten times to answering all ten.

And it's not only word choice that matters. Seemingly unrelated statements, in the same prompt, can affect results. [In a Harvard study](https://arxiv.org/html/2407.06866v3), researchers found that merely stating which NFL team the user rooted for changed how often the model refused to answer questions regarding sensitive topics. Spurious statements influence the inference pass in ways we can't predict. Which is why prompts become more brittle as you add fixes. An additional instruction to quell a stubborn error could affect how the model interprets a separate instruction that worked yesterday.

Repeating instructions propels us towards prompt debt, but it's necessary when the behavior we want is at odds with a model's training. This is [fighting the weights](https://www.dbreunig.com/2025/11/11/don-t-fight-the-weights.html), and once you recognize it you see it in system prompts everywhere. For example, ChatGPT's image prompts used [to instruct the LLM *eight times* to not reply when a generated image was returned](https://www.dbreunig.com/2025/11/11/don-t-fight-the-weights.html#:~:text=When%20you%20asked%20ChatGPT%20to%20generate%20an%20image%2C%20it%20would%20clean%20up%20or%20even%20improve%20your%20image%20prompt%2C%20create%20the%20image%2C%20then%20append%20the%20following%20instructions:), because it had been trained to always keep the conversation going. 

Every coding agent system prompt we analyzed featured repeated instructions, stern warnings, and all-caps demands. [Claude Code tells Opus *seven times* to return multiple tool calls in a single response](https://blog.nilenso.com/blog/2026/02/12/how-system-prompts-reveal-model-biases/). And even the most advanced models force prompt authors to fight the weights: [Fable's leaked system prompt restates one specific copyright rule six times](https://github.com/asgeirtj/system_prompts_leaks/blob/main/Anthropic/claude-fable-5.md).

None of these examples occurred in isolation. Multiple repeated rules are woven throughout the system prompts we examine. Stubborn errors grow our prompts quickly, with each increasing the brittleness, the risk of regression with every edit. 

And worse: these fixes are tailored to a single model's behavior. A recent [Berkeley-led study](https://arxiv.org/abs/2512.04123) found enterprises stay on older models because newer ones break their existing agents. This is because models are not cleanly versioned software. They have different weights that produce different behaviors, in unpredictable and undocumented ways. A prompt that works beautifully with GPT-4o may fail with GPT-5.5. [Anthropic's own release notes for Fable](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5#:~:text=Refactor%20existing%20prompts%20and%20skills) warn that skills developed for prior models can "degrade output quality". 

Prompt debt locks an application to a single model. Our inability to easily swap models isn't the result of frontier labs coming up with a clever moat. No, it's the result of evolving a lossy, natural language specification against a probabilistic model. 

#### **Preventing Prompt Debt**

Thankfully, we don't have to theorize about how to mitigate prompt debt; one field has already shown the way. Programmers using coding agents sit at the leading edge of what models can do, outliers on the [jagged frontier](https://www.oneusefulthing.org/p/the-shape-of-ai-jaggedness-bottlenecks) of model abilities. Over the last couple years they've [been](https://addyosmani.com/blog/new-sdlc-vibe-coding/) [evolving](https://simonwillison.net/guides/agentic-engineering-patterns/) [best](https://developers.openai.com/codex/learn/best-practices) [practices](https://code.claude.com/docs/en/best-practices) that let the model write more of the code, while delivering maintainable, modular software.

The first principle is to specify your system's behavior with measurements, not prose. When the model's output is probabilistic and language is imprecise, we build hard edges to constrain them: evaluations, metrics, and typed specifications. These are legible, shared artifacts colleagues can read and contribute to, enabling the collaboration that brittle prompts prevented. 

The best engineers now spend more of their bandwidth on tests than ever, as they are no longer a safety net but the thing that *lets the model cook*.

The second principle is to stop writing the prompt by hand. Once we have metrics that can score candidates, the prompt is no longer something to craft but something for which to search. And the surface area of potential words, phrases, and structures that natural language allows is too vast to spend human hours on. This is terrain LLMs were built to explore, and there are already systems (like [DSPy](https://dspy.ai/) and [GEPA](https://sky.cs.berkeley.edu/project/gepa/)) that manage this work for you, holding prompts accountable to your designs.

Once prompts are generated and your program's behavior is defined by measurements, you are no longer bound to a particular model. Evaluating a new model takes hours, not weeks. When a faster, cheaper model arrives you can try it. When a deprecation email arrives, you can secure options in a day. Whether a model is pulled for regulatory reasons ([as we saw with Anthropic's Fable](https://www.theverge.com/ai-artificial-intelligence/949553/anthropic-fable-5-mythos-5-government-national-security)) or deprecated due to age ([as Groq announced last week with Llama-3.1-8b](https://www.reuters.com/world/china/us-holds-off-blacklisting-chinas-deepseek-more-than-100-firms-deemed-security-2026-06-17/)), the fix is a chore, not a fire drill.

Every mature engineering discipline eventually stops doing by hand the very thing it once prided itself on doing by hand. Assembly gave way to compilers, hand-tuned queries gave way to planners, and manual memory management gave way (mostly) to machines that do it better. Prompt-writing is no different. 

Coaxing the model with exactly the right words is a real skill, and for one-off tasks it's often optimal. But to build reliable, improvable, and portable systems we should not be hand-tuning prompts.
