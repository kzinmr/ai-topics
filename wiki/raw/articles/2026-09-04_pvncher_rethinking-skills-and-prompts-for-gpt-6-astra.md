# Rethinking skills and prompts for GPT-6 Astra

- **Author**: Eric Provencher (@pvncher) — Codex DX @OpenAI, built @repoprompt, prev XR @Unity
- **Source**: https://x.com/pvncher/status/2095991462416490862 (X Article)
- **Published**: 2026-09-04
- **Retrieved**: 2026-09-05 via xurl `tweet.fields=article` (article.plain_text)

---

Coding agents have come a long way, and best practices are changing fast. What used to require a lot of handholding and scaffolding no longer does.

If you've been using agents in your projects over the last year, you've likely accumulated a lot of bloated instructions as you worked to steer the models toward good outcomes. With each release, it's been worth revisiting those assumptions, but with GPT-6 Astra, that's more important than ever.

These instructions can take many forms, with Skills, AGENTS.md, and your task prompts all shaping how the model gets work done.

## Skill files

One form these instructions can take, is with skill files, which are essentially prompts stored as markdown files, sometimes with bundled scripts. Generally, they are most useful for guidance around a workflow the model only needs for certain tasks, or instructions for using a plugin.

Many people default to downloading a lot of skills into their projects, but that's a mistake. Each skill comes with a name and description that are loaded into the model's context so it knows when to use them. Many descriptions are far too long, and when you add too many skills, Codex starts shortening their descriptions to fit. The model ends up seeing less of each description, making it harder to know which skill to pick.

Worse, descriptions can contradict each other or have too much "pick me" energy, leading the model to load instructions that don't actually help the task.

If you've ever asked Codex to create a skill, it probably used the $skill-creator skill. We recently updated its guidance in a few ways to help mitigate many of the failure modes we've seen in practice.

First, skill descriptions should be as short as possible while making it clear when the model should use them.

Here the bad skill description can push the model to use it anytime it touches anything related to a database, vs only when it has to handle a migration.

Second, one of the key markers of a useful skill is progressive disclosure. Reading a skill takes up context, bringing you closer to compaction and introducing guidance that may not apply to the task. For skills with multiple workflows, make the root document a minimal router that points to supporting docs and scripts. Give the model enough guidance to know where to look without forcing it to read things that don't matter in the moment.

Third, many skills were written as elaborate itineraries or recipes. Models have gotten much better at understanding nuance and ambiguity, so overly specific guidance can now hinder results where it previously helped.

Repository skills also guide other contributors' agents, which may use different models. Guidance that helps Sol or Luna may overconstrain GPT-6 Astra, so consider which models will use the instructions you leave behind.

## AGENTS.md

Because AGENTS.md applies whenever the model works in your repository, revisit each instruction and ask whether the task still needs it.

Requiring a stack of docs or a full repo map before every edit is excessive for a typo fix. GPT-6 Astra can work out what it needs to read without being pushed to review the whole project before every change.
