---
title: "The Waste Land, annotated (emollick/wasteland-annotated)"
url: "https://github.com/emollick/wasteland-annotated"
fetched_at: 2026-09-23T22:40:00+00:00
source: "github.com"
tags: [project, raw]
---

# The Waste Land, annotated

Sources:
- https://github.com/emollick/wasteland-annotated (README, fetched 2026-09-23)
- https://the-waste-land.netlify.app (built site)
- X thread by Ethan Mollick (@emollick):
  - Root tweet (2102179283737158019, Sep 21 2026): "AI can be a really wonderful tool for exploring topics far from coding. I had Claude Fable 5.1 put together an annotated guide to Eliot's poem 'The Wasteland,' with multiple pathways through the poem, recordings, scholarship, etc. I am quite impressed."
  - Follow-up (2102626794104934520, Sep 23 2026): "Open source here: https://github.com/emollick/wasteland-annotated"

## What it is

The source of https://the-waste-land.netlify.app : the 1922 text of T.S. Eliot's *The Waste Land* with Eliot's notes, a commentary on every part of it, and several ways through the poem — lenses on the notes, the sources, the voices, the languages, the water, the places, the drafts and the hours; pathways on its themes; a map of its London; a listening room; a library of the texts it draws on. "The poem is the page, and everything else opens from it."

## Repository structure

- `site/` — the built site, as Netlify serves it (`netlify.toml: publish = site`)
- `build/` — `build.js`, which writes `site/` from `data/`, `research/` and `art/`
- `data/` — the poem, Eliot's notes and the commentary, in a structured record format: glosses of each part, ways into each part, pathways and their stops, drafts, the library, the listening room, the voices, the dates, page texts and "the tools' words", and `works.txt` (the editions/studies cited)
- `research/` — working files: the 1922 text as fetched, records behind images and recordings, source links
- `art/` — tarot pack for Madame Sosostris, frontispieces/ornaments, London map vignettes, all **drawn as SVG by code**; each directory keeps sources and NOTES.md; STYLE.md is the art direction
- `commentary/` — commentary exported for editorial work, part by part, with debates over each part (`debates/`) and source citations (`citations/`)

## Build

`node build/build.js` — Node alone, **no dependencies**. Reads art and commentary from a shared project directory when present. `build/commentary.js export` writes the commentary out for editing and `build/commentary.js import part1|…|part5|site|all` takes it back, refusing a record whose fixed fields changed.

## Significance

An example of an LLM (Claude Fable 5.1) producing a deep, humanistic scholarly-exploration artifact — annotation, commentary, multi-lens navigation — rather than code. Mollick open-sourced it as a demonstration that "AI can be a really wonderful tool for exploring topics far from coding."
