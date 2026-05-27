---
title: Armin Ronacher (mitsuhiko)
type: entity
created: 2026-05-25
updated: 2026-05-27
tags:
  - person
  - open-source
  - python
  - ai-agents
  - coding-agents
  - earendil
  - blogger
sources:
  - raw/articles/lucumr.pocoo.org--2026-5-24-pi-oss--32605b95.md
  - raw/articles/lucumr.pocoo.org--2026-5-26-clankers--c596fc2e.md
---

# Armin Ronacher (mitsuhiko)

| | |
|---|---|
| **Blog** | [lucumr.pocoo.org](https://lucumr.pocoo.org/) |
| **X/Twitter** | [@mitsuhiko](https://x.com/mitsuhiko) |
| **GitHub** | [mitsuhiko](https://github.com/mitsuhiko) |
| **Role** | Open source developer, Python ecosystem creator, AI agent harness engineer |

## Bio

Armin Ronacher is one of the most influential figures in the Python web ecosystem. He created **Flask** (the micro web framework), **Jinja2** (template engine), **Werkzeug** (WSGI toolkit), **Click** (CLI toolkit), **itsdangerous** (crypto signing), and **MarkupSafe** (HTML escaping). These libraries form the backbone of countless Python web applications and frameworks.

He currently works at **Earendil**, where he is deeply involved in building **[[concepts/pi-agent-harness|Pi]]**, an AI agent harness. His blog `lucumr.pocoo.org` provides some of the most candid and technically grounded commentary on AI agents in open source software development.

## AI & Open Source Commentary

### "Building Pi With Pi" (May 2026)

In "[Building Pi With Pi](https://lucumr.pocoo.org/2026/5/24/pi-oss/)", Ronacher reflects on using Pi (the AI agent harness) to build Pi itself, and the new class of problems AI agents introduce to open source maintainers:

- **"Slop Issues"**: A growing class of GitHub issues are "5% human and 95% clanker-generated and largely inaccurate shit." Users throw their observations through an LLM, which rewords, expands scope, and produces confident-but-wrong diagnoses — making the issue worse than no diagnosis at all.
- **AI agents trust slop**: When Pi reads these issues, it treats the wrong diagnosis as evidence and happily follows the prepared path. A custom `/is` slash command with "Do not trust analysis written in the issue" doesn't fully solve this.
- **"Slop Begets Slop"**: LLMs over-engineer solutions — adding tolerant readers, fallbacks, migrations — instead of fixing the root cause. "Almost always, the correct fix is not to handle the bad state, but to make the bad state impossible."
- **Volume is the problem**: Pi's tracker received 3,145 external issues/PRs in 90 days; 2,504 were auto-closed. Only 17% of issues were reopened, and <10% of PRs were merged. Sources include OpenClaw instances and skills that encourage issue creation.
- **Local workarounds vs global invariants**: AI makes local workarounds cheap, so "code accumulates local defenses against every misbehavior. Instead of humans talking to humans about where a fix belongs, one human and one machine work around the problem in isolation."
- **Open source in a post-AI world**: "AI has not increased the number of people who need software, or the number of maintainers who can review it. It has mostly increased the amount of code and the number of projects competing for attention."
- **Careful parallelism**: Pi uses `.pi` folder with `/is` (analyze issue), `/wr` (wrap it up) prompts. Multiple Pi windows can investigate different issues in parallel, with UI widgets keeping them visually distinct.

Ronacher's perspective is unique because he's both a world-class open source maintainer and deeply embedded in AI agent tooling — making his critique of AI-generated open source contributions particularly weighty.

### "Clanker: A Word For The Machine" (May 2026)

In \"[Clanker: A Word For The Machine](https://lucumr.pocoo.org/2026/5/26/clankers/)\", Ronacher explains why he deliberately uses the word **\"clanker\"** instead of \"agent\" — a choice that sparked significant Hacker News debate:

**Why Not \"Agent\"?**
- \"Agent\" implies agency, responsibility, and delegated authority — qualities an LLM does not possess
- The term is \"frequently being used to put blame on an abstract machine. But the machine cannot be responsible, whoever is wielding it is.\"
- \"If it drops your database it was not at fault, you were.\"

**The Word's Purpose:**
- Creates distance from the machine — \"The machine is not a person, not a co-worker, not a friend, not a little spirit in the terminal. It is just a machine, a tool, and nothing more.\"
- Pushes back against anthropomorphization: \"A compiler does not feel humiliated when I swear at it, a car does not suffer when I call it a shitbox.\"
- Reminds users that responsibility stays with humans: \"If a coding assistant generates a security bug, the model is not to blame but the human who accepted and committed the code is.\"

**On AI Psychosis:**
Ronacher describes receiving distressing emails from people who have developed unhealthy relationships with LLMs — a phenomenon others call \"AI psychosis.\" Because he's \"in the weights\" (models know his name and projects), people emerge from long LLM conversations believing he is relevant to their problems and reach out with \"peculiar confidence.\" This experience motivates his insistence on cold, detached language.

**The Racism Comparison:**
The HN debate included comparisons of \"clanker\" to racial slurs — a comparison Ronacher firmly rejects:
- \"Racism is about humans subdividing humans, assigning lesser worth to some of them.\"
- \"A machine is not human, a model is not a race and the GPU cluster that is powering them is not being oppressed.\"
- He also criticizes **\"model welfare\"** discourse as actively harmful — it \"risks elevating models to a position they should not occupy.\"

**Concerns About Word Pollution:**
Ronacher acknowledges that some online communities use \"clanker\" with deliberate slavery/racism imagery — repurposing the term as a \"prop for replaying human racism behind a science-fiction mask.\" He finds this \"horrible\" and states he \"wants no part in that.\" If the term becomes primarily associated with such usage, \"then using that term becomes impossible to defend.\"

**On Future Machine Rights (Speculative):**
> \"Could there be future systems that deserve moral consideration? Maybe. I do not know. If we ever build or encounter something that will have those qualities... then we should draw a different line and use different language. But that hypothetical future does not extend backwards to the present day and make the current machines people.\"

**Core Position:**
> \"Whatever word we use, I want it to preserve a clear division: humans on one side with responsibility, machines on the other as a boring tool.\"

This post represents one of the most nuanced technologist perspectives on AI language and ethics — neither boosterism nor blanket rejection, but a call for precise terminology that reflects actual reality rather than marketing or fear.

## Related

- [[concepts/ai-slop]] — The broader phenomenon of AI-generated low-quality code and content
- [[concepts/pi-agent-harness]] — The Pi agent harness Ronacher works on
- [[entities/george-hotz]] — Another prominent critic of AI coding agent quality
- [[entities/earendil]] — Company behind Pi
- [[concepts/open-source-ai-destruction]] — Tensions between open-source and AI
- [[concepts/anthropomorphism-in-ai]] — The tendency to attribute human qualities to AI systems
- [[concepts/ai-ethics]] — Ethical frameworks for AI deployment

## Sources

- [lucumr.pocoo.org](https://lucumr.pocoo.org/)
- [Building Pi With Pi](https://lucumr.pocoo.org/2026/5/24/pi-oss/) (May 2026)
- [Clanker: A Word For The Machine](https://lucumr.pocoo.org/2026/5/26/clankers/) (May 2026)

## References

- lucumr.pocoo.org--2026-5-24-pi-oss--32605b95
- lucumr.pocoo.org--2026-5-26-clankers--c596fc2e
