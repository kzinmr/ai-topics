---
type: article
date: 2026-06-23
source: https://www.youtube.com/watch?v=5BOlWmwoOtg
author: Hugo Bowne-Anderson
title: "Building a Claude Code Skill: 8-Bit Video Generator (full walkthrough)"
fetched: 2026-06-27
---

# Building a Claude Code Skill: 8-Bit Video Generator (full walkthrough)

**Channel:** Vanishing Gradients  
**Author:** Hugo Bowne-Anderson  
**Duration:** 4:03 (243 seconds)  
**Views (at fetch time):** 406  
**Video ID:** 5BOlWmwoOtg  

## Description

In this video I walk through the Claude Code agent skill I use to turn every guest on Show Us Your (Agent) Skills into a side-scrolling 8-bit video game character. Wes McKinney liked his enough to make it his GitHub profile pic.

### What's in the video:
- **Live demo:** headshot in, animated 8-bit video out
- A look at the **skill itself** and how **progressive disclosure** keeps the context window clean
- The **two scripts** the skill orchestrates (Gemini for the pixel art, Replicate / Seedance 2 for the animation)
- Installing **community skills with one command**

### Try it yourself:
```
npx skills add hugobowne/show-us-your-agent-skills
```

### Related Links:
- Ep 1 with Wes, Jeremiah Lowin, Randy Olson, Ph.D., & Thomas Wiecki, PhD: https://youtube.com/live/Pq3xuChdwxQ?feature=share
- Next livestream: https://luma.com/7kfkk6wb

Upcoming episode features Hilary Mason (Hidden Door), Eric Ma (Moderna), Bryan Bischof, and Tomasz Tunguz (Theory Ventures).

## Chapters

| Timestamp | Chapter |
|---|---|
| 0:00 | The 8-bit video of Wes McKinney |
| 0:25 | Live demo in Claude Code |
| 1:10 | Inside the skill (SKILL.md, scripts) |
| 1:30 | Progressive disclosure, explained |
| 2:15 | The finished video |
| 2:45 | Installing community skills |
| 3:30 | What's next |

## Key Concepts Demonstrated

### Claude Code Skills
- Community-installable via `npx skills add`
- Skill structure: SKILL.md + orchestrated scripts
- This skill package: `hugobowne/show-us-your-agent-skills`

### Progressive Disclosure
- Technique to keep the Claude Code context window clean
- Only expose relevant parts of the skill as needed

### Pipeline Architecture
- **Gemini** — used for pixel art generation from headshots
- **Replicate / Seedance 2** — used for animation of the 8-bit sprites
- Two-script orchestration: pixel art generation → animation rendering

### Community / Series Context
- Part of "Show Us Your (Agent) Skills" livestream series
- Guests include notable figures in data/AI: Wes McKinney, Jeremiah Lowin, Randy Olson, Thomas Wiecki, Hilary Mason, Eric Ma, Bryan Bischof, Tomasz Tunguz

---

*Raw scrape of YouTube video page. Content captured 2026-06-27 from ytInitialPlayerResponse JSON embedded in page HTML.*
