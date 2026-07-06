---
title: Show Us Your Agent Skills
created: 2026-06-27
updated: 2026-06-27
type: concept
tags: [agent-skills, agent-workflows, video-series, community, tool]
sources:
  - raw/articles/2026-06-23_hugobowne_show-us-your-agent-skills.md
---

# Show Us Your Agent Skills

## Overview

**Show Us Your Agent Skills** is a live YouTube series produced by Vanishing Gradients × PyMC Labs where experienced Python, ML, and AI builders demonstrate how they are *actually* using agents in their daily work. The premise is straightforward: no vibe coding, no polished demos — real builders showing their real workflows in real time. The show is hosted by [[entities/hugo-bowne-anderson|Hugo Bowne-Anderson]] and Thomas Wiecki.

Launched in April 2026 and now in its second season, the series has shipped 5 episodes featuring 20 builders (22 guests booked when counting upcoming EP 06). Together they have demonstrated 51 distinct agent skills and 79 workflows. The show maintains a companion GitHub repository ([hugobowne/show-us-your-agent-skills](https://github.com/hugobowne/show-us-your-agent-skills)) where packaged skills and workflows from the streams are available for installation via `npx skills add`.

The series taglines itself as "EXCEL WORLD CHAMPIONSHIPS × EUROVISION," reflecting its energetic, competitive, and practical tone. Episodes typically run 1.5–3.5 hours and are live-streamed on the [Vanishing Gradients YouTube channel](https://www.youtube.com/@vanishinggradients), with an event calendar on [Luma](https://luma.com/calendar/cal-8ImWFDQ3IEIxNWk) and community discussion on Substack.

## Episodes & Guests

| Episode | Date | Theme | Guests | Runtime |
|---|---|---|---|---|
| EP 01 | April 2026 | The Agentic Software Factory | Wes McKinney (pandas/Posit), Jeremiah Lowin (Prefect/FastMCP), Randy Olson (Goodeye Labs) | 1h 32m |
| EP 02 | May 2026 | Building Agents That Improve the Workflow | Hilary Mason (Hidden Door), Bryan Bischof (Theory Ventures), Eric Ma (Moderna), Tomasz Tunguz (Theory Ventures) | 2h 14m |
| EP 03 | May 2026 | From Skills to Agent Harnesses | Paul Iusztin (Decoding AI), Eleanor Berger (Elite AI Coding), Alan Nichol (Rasa), Vincent Warmerdam (Marimo), Nicolay Gerold (Amp), Matthew Honnibal (spaCy/Explosion), Ines Montani (spaCy/Explosion) | 3h 18m |
| EP 04 | May 2026 | How to Evaluate Agentic Workflows | Hamel Husain (Parlance Labs), Chris Fonnesbeck (PyMC Labs), Doug Turnbull (Search, Shopify/Reddit) | — |
| EP 05 | June 2026 | Copilots & Coding Agents | John Berryman (Arcturus Labs, ex-GitHub Copilot), Isaac Flath (Kentro Tech, ex-Answer.ai), Matt Palmer (Conductor, ex-Replit) | — |
| EP 06 | July 3, 2026 | Agents in the Data Stack | Matt Rocklin (Dask/Coiled), Skylar Payne (Wicked Data, ex-Google, ex-LinkedIn) | upcoming |

## Notable Skills Demonstrated

- **BBPlot (eval-driven chart library)**: Bryan Bischof demonstrated an eval-driven approach to chart generation where an LLM-as-judge evaluates chart quality iteratively before presenting to the user ([see EP 02](#episodes--guests)).
- **8-Bit Video Generation**: Hugo Bowne-Anderson demonstrated a Claude Code skill for generating 8-bit style video content programmatically (EP 01).
- **Prompt Refinement**: Hilary Mason (Hidden Door) demonstrated systematic prompt refinement workflows in EP 02.
- **Marimo Pair / Agentic EDA**: Eric Ma showed agentic exploratory data analysis workflows using Marimo notebooks (EP 02).
- **Weekly Gremlins**: Tomasz Tunguz (Theory Ventures) shared his system for catching and fixing recurring issues (EP 02).
- **Plan-Review-Implementation-Review**: Hamel Husain (Parlance Labs) showed a multi-pass agentic review pattern (EP 04).
- **Auto-Research / Agentic Search**: Doug Turnbull demonstrated agentic search workflows for automated research (EP 04).
- **Try-Except / Pre-Mortem / Mutation Testing**: Paul Iusztin (Decoding AI) showed agent safety patterns including pre-mortem analysis and mutation testing (EP 03).
- **Research Memory / Local Boxes**: Vincent Warmerdam (Marimo) demonstrated local research memory systems (EP 03).
- **Remotion Video Skill**: Matthew Honnibal and Ines Montani (spaCy) showed agent-editable video timelines (EP 03).
- **Rook / Raw2Draft / MCut / Conductor**: John Berryman, Isaac Flath, and Matt Palmer (EP 05) demonstrated agents-that-follow-you patterns, Wikipedia discovery, formatting Notion pages, writing revision, human-editable AI artifacts, and the 90/10 handoff approach.
- **Explain / GitHub-Reply / Ship-It**: Wes McKinney and Jeremiah Lowin (EP 01) showed personal agent commands for code review and deployment.

## Skills Hub

The companion repository at [github.com/hugobowne/show-us-your-agent-skills](https://github.com/hugobowne/show-us-your-agent-skills) contains packaged versions of demonstrated skills. Install with:

```shell
npx skills add https://github.com/hugobowne/show-us-your-agent-skills
```

Packaged skills include: `explain`, `github-reply`, `ship-it`, `high-signal-chart-workflow`, `8-bit-video-gen`, `prompt-refinement`, `marimo-pair`, `agentic-eda`, `eval-driven-charts`, `weekly-gremlins`, and more.

## Stats (as of June 2026)

- **Season**: 02
- **Episodes shipped**: 05
- **Builders featured**: 20 (22 booked)
- **Skills demonstrated**: 51
- **Workflows demonstrated**: 79
- **Episode cadence**: approximately monthly

## See Also

- [[entities/hugo-bowne-anderson]]
- [[entities/bryan-bischof]]
- [[concepts/agent-workflows]]

## Episodes
| Ep | Date | Duration | Guests | YouTube | Topics |
|----|------|----------|--------|---------|--------|
| 1 | 2026-05-08 | 103:45 | [[entities/wes-mckinney\|Wes McKinney]], [[entities/jeremiah-lowin\|Jeremiah Lowin]], [[entities/randy-olson\|Randy Olson]] | [link](https://www.youtube.com/live/Pq3xuChdwxQ) | RoboRev code review, second brain with OpenClaw, generator-evaluator data viz |
| 2 | 2026-05-15 | 139:00 | [[entities/hilary-mason\|Hilary Mason]], [[entities/bryan-bischof\|Bryan Bischof]], [[entities/eric-ma\|Eric Ma]], [[entities/tomasz-tunguz\|Tomasz Tunguz]] | [link](https://www.youtube.com/watch?v=l37PR-OkYKA) | Agentic data science, context engineering, local models, creative AI |
| 3 | 2026-05-21 | 198:20 | Paul Iusztin, [[entities/eleanor-berger\|Eleanor Berger]], [[entities/vincent-warmerdam\|Vincent Warmerdam]], [[entities/alan-nichol\|Alan Nichol]], Nico Gerold, [[entities/matthew-honnibal\|Matthew Honnibal]] | [link](https://www.youtube.com/watch?v=ud2WzkKeDZs) | Agent harness, coding agents, NLP, cron-job agents |
| 4 | 2026-05-29 | 122:30 | [[entities/hamel-husain\|Hamel Husain]], [[entities/chris-fonnesbeck\|Chris Fonnesbeck]], [[entities/doug-turnbull\|Doug Turnbull]], [[entities/john-berryman\|John Berryman]] | [link](https://www.youtube.com/live/XaYQFtca798) | Code review, search, evaluation, agent harness |


## Key Themes (Ep. 1)
1. **Verification** — How to check work when agents produce more than you can personally inspect
2. **Personal software** — Agents make bespoke software for one user's workflow newly cheap
3. **Living skills** — Skills as editable markdown documents that evolve with the builder
4. **Review loops** — Automated code review, generator-evaluator patterns, iterative improvement


## Format
Each episode features practitioners who:
- Walk through their actual agent tools and skills
- Demo live workflows (not just talk about them)
- Share the principles behind their setup
- Describe what a typical session looks like

> *"This is an experiment. We're trying to figure out how to communicate how people are actually building."*


### Ep. 1 Guests & Topics- [[entities/wes-mckinney]] — RoboRev, automated code review, agentic software factory
- [[entities/jeremiah-lowin]] — Second brain, OpenClaw, FastMCP, personal software
- [[entities/randy-olson]] — Generator-evaluator pattern, data visualization, Tuftean criteria
- [[entities/superpowers]] — Skills framework used by McKinney


### Ep. 2 Guests- [[entities/hilary-mason]], [[entities/bryan-bischof]], [[entities/eric-ma]], [[entities/tomasz-tunguz]]


### Ep. 3 Guests- Paul Iusztin, [[entities/eleanor-berger]], [[entities/vincent-warmerdam]], [[entities/alan-nichol]], Nico Gerold, [[entities/matthew-honnibal]]


### Ep. 4 Guests- [[entities/hamel-husain]], [[entities/chris-fonnesbeck]], [[entities/doug-turnbull]], [[entities/john-berryman]]


### Hosts- [[entities/hugo-bowne-anderson]] — Host
- [[entities/thomas-wiecki]] — Co-host


## References
- [YouTube Ep. 1](https://www.youtube.com/live/Pq3xuChdwxQ) (103:45)
- [YouTube Ep. 2](https://www.youtube.com/watch?v=l37PR-OkYKA) (139:00)
- [YouTube Ep. 3](https://www.youtube.com/watch?v=ud2WzkKeDZs) (198:20)
- [YouTube Ep. 4](https://www.youtube.com/watch?v=XaYQFtca798) (122:30)
- [GitHub: show-us-your-agent-skills](https://github.com/hugobowne/show-us-your-agent-skills)
- [The Agentic Software Factory](https://hugobowne.substack.com/p/the-agentic-software-factory) (Vanishing Gradients, May 2026)


## Log
- **2026-06-05**: Linked to existing YouTube transcripts (Ep. 1-4). Updated episode table with dates, durations, YouTube links. Added full guest list across all episodes.
- **2026-06-05**: Initial entity page created.

