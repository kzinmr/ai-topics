---
title: "When AI builds itself"
url: "https://www.anthropic.com/institute/recursive-self-improvement"
fetched_at: "2026-06-07"
source: "anthropic"
authors: ["Marina Favaro", "Jack Clark"]
description: "Our progress toward recursive self-improvement, and its implications."
---

# When AI builds itself

**Anthropic Institute — June 4, 2026**

For most of AI's history, humans drove every step in its development cycle. But at Anthropic, we are delegating a growing share of AI development to AI systems themselves, which is speeding up our work.

Taken far enough, and given enough compute, that trend points to an AI system capable of fully autonomously designing and developing its own successor. This is called *recursive self-improvement*. We are not there yet, and recursive self-improvement is not inevitable. But it could come sooner than most institutions are prepared for.

Using public benchmarks and previously unreported data from within Anthropic, The Anthropic Institute is showing that AI is already accelerating the development of AI systems. To take just one example: today, Anthropic engineers on average ship 8x as much code per quarter as they did from 2021-2025.

The technical trends discussed in this piece suggest that AI systems are going to become much more capable in coming years. These trends have huge implications. AI that can build itself would be a major development in the history of technology—one that could bring enormous good for the world in science, healthcare, and beyond. But full recursive self-improvement also might increase the risks of humans losing control over AI systems.

## Timeline of AI-Assisted Development at Anthropic

- **2021–2023: Building the first Claude** — In the early days, work at Anthropic looked like work at any other tech company: people writing code and docs on laptops.
- **2023–2025: Chatbots** — People used early chatbots to help with parts of the process, like generating short code snippets and copying the output into text editors.
- **2025–2026: Coding agents** — As the agents became more capable, they were able to write and edit code on their own, sometimes entire files.
- **Today: Autonomous agents** — Agents can now run code themselves and delegate hours of work to other agents.
- **20XX?: Closing the loop** — In the future, agents could become capable enough to build and train models themselves. If this happens, future versions of Claude could be continuously improved by Claude itself.

## Evidence from the Outside World

The rate at which AI models improve is accelerating. The length of tasks that they can reliably complete on their own has been doubling roughly every four months, up from an earlier trend of doubling every seven months. In March 2024, Claude Opus 3 could complete software tasks that take humans about four minutes to complete. A year later, Claude Sonnet 3.7 managed tasks that took about an hour and a half. A year after that, Claude Opus 4.6 managed 12-hour tasks. If this trend holds, tasks that take a skilled person days could come into range this year. In 2027, AI systems could be capable of tasks that take a person weeks.

On SWE-bench, models went from 2% (Claude 2, late 2023) to 93.9% (Claude Mythos Preview, May 2026). CORE-Bench (reproducing published research) went from succeeding at fewer than 20% of papers to 85% in under a year. MLE-Bench (building ML systems from scratch) jumped from 16.9% to 64.4% between October 2024 and February 2026.

## Evidence from Within Anthropic

### Engineering: 8x Code Output

Anthropic engineers on average ship 8x as much code per quarter as they did from 2021-2025. More than 80% of code merged into Anthropic's codebase was authored by Claude as of May 2026 — up from low single digits before Claude Code launched in February 2025.

A March 2026 poll of 130 employees across Anthropic research teams found the median respondent estimated ~4x output with Mythos Preview vs. without. Claude also shipped over 800 fixes in April 2026 that reduced a class of API errors by a factor of 10.

### Research: Claude Can Now Propose Experiments

Claude's success rate on the most open-ended engineering tasks reached 76% in May 2026, up 50 percentage points in six months. On research, Claude can match or outperform skilled humans at the narrow sub-task level. In April 2026, Anthropic published the first demonstration of Claude running an open-ended research project end to end in AI safety.

Claude is also getting better at steering research sessions: when presented with moments where a human researcher's next move had room for improvement (n=129), models judged Claude's suggestions as better ~40% of the time on Opus 4.6.

## Future Scenarios

Anthropic outlines three possible futures:
1. **Continuation** — Trends continue, AI increasingly handles more of AI development
2. **Acceleration** — A fast takeoff where AI quickly surpasses human capabilities in AI R&D
3. **Failure** — Trends plateau due to fundamental limitations

## Policy Stance

Anthropic believes it would be good for the world to have the *option* to slow or temporarily pause frontier AI development. However, they acknowledge a unilateral pause could let less cautious actors catch up. They will organize conversations with policymakers, researchers, and civil society about full recursive self-improvement and coordination mechanisms.

## Notes

- Marina Favaro and Jack Clark co-authored, with editorial support from Santi Ruiz.
- Quotes from Anthropic employees are from internal discussions, used with permission. They reflect individual views as of May 2026, not official company positions.
