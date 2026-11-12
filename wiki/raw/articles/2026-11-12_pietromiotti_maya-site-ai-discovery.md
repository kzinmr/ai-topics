---
title: "My AI Agents (Re)discovered a Maya Site in 72 Hours"
date: 2026-11-11
source: https://pietromiotti.com/latest/maya-site
author: Pietro Miotti (Google engineer)
type: article
hn: https://news.ycombinator.com/item?id=50452455
tags: [raw, ai-discovery]
sha256: b8d7156690025b535ce89f4acf6e5ce2651ea16c1cf0b714ff593bde4af3cf68
---

My AI Agents (Re)discovered a Maya Site in 72 Hours — 5 min read (last edit Nov 11)

Update (11 November): it turns out the site had already been mapped in Estrada-Belli et al. 2025. The agents missed it while going through the literature, so they rediscovered it rather than discovered it (it just wasn't in the register of Mexico's National Institute of Anthropology and History, INAH, yet). Still work to do then!

"By analyzing NASA lidar data, my AI agents found a Maya site in Mexico that wasn't in the official register. It took less than 72 hours to go from a random thought while traveling to an official reply from the Mexican government."

## Method

- 18 Oct: while traveling in Peru, the author read about Hiram Bingham and Machu Picchu, brainstormed with Gemini/ChatGPT/Claude/Grok about modern equivalents of accidental discovery; all suggested lidar. Peru is poorly covered by public lidar, so he pivoted to the Maya region, which is well covered by public (NASA) lidar.
- 19 Oct: "They turned the lidar strips (about 1,200 km2 of jungle) into images, and 48 agents went through them one by one like very patient archaeologists, looking for pyramids, platforms, and plazas while filtering out natural hills, sinkholes, and roads. There was no special model or classifier involved: the agents literally looked at the pictures, following a precise guide."
- The agents flagged many villages and regular shapes; then, asked to cross-check literature and archives, reported "One major village doesn't seem to have been registered."
- The site: a hilltop on the edge of a cliff, under jungle, with straight edges and sharp corners; a levelled plaza, an oval pyramid at least 8-12 m tall, a raised courtyard attached to it, and a flat-bottomed hollow that might have been a water reservoir.
- INAH replied: they checked their records and found no registered archaeological site at that location. Not official yet.

## Caveats

- The author is not an archaeologist; the post is written as a diary.
- The November 11 update downgrades "discovery" to "rediscovery" — the site was already mapped in Estrada-Belli et al. 2025, which the agents failed to find in the literature; it was simply absent from the INAH register.

## HN discussion highlights (item 50452455, ~999 pts, 369 comments)

- [runarberg] "Turns out that an expert archeologist Dr. Francisco Estrada-Belli of Tulane University already found it. You are right to be skeptical." (linking HN item 50453616)
- [traches] "The LIDAR image (based on measured data, not AI) clearly shows human-made structures, and the Mexican government's response said that it's not registered. The chatbots just found it... Now all the bits about what sort of site it probably was and the slop [speculation] is another matter."
- [chirau] "I will personally wait for an expert archaeologist's verification on this. I have dealt with agents making up stuff that sounds fantastic and ground-breaking but completely falters on further review. And I doubt the folks you contacted have the audacity to question a Google engineer and his 48 agents."
- [eks391] "from his blogpost, he doesn't imply that he cross checked anything and instead trusted all agentic output... submitting this to INAH after only chatting with the agents is really bold."
- [TSiege] "There's a lot of assumptions coming out about what the structures are... The actual archeology involved though will be slow as it's a science done layer by layer. It will be interesting to see if any predictions made by the AI match up to the facts."
- [myrmidon] "The technology is pretty new. It would not have been realistic for PhD students to manually comb through thousands of square kilometers of LIDAR data... LLMs have turned this into low-hanging fruit."
- [piltdownman] on academic gatekeeping: "We saw this with the Dead Sea Scrolls where exclusive control was given to a select group of academics who monopolized the research."
- [thomasben] "@openai @anthropic @google @spacexai: can you please proceed with scanning the entire planet and let us know what you found?"

## Related sources

- https://pietromiotti.com/latest/maya-site
- https://news.ycombinator.com/item?id=50452455
