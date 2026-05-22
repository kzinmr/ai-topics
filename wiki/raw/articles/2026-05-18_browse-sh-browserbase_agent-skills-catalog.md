---
type: x_article
x_article_title: "Browse.sh, a catalog of browser skills for the Agentic future"
x_article_author: "Kyle Jeong (@kylejeong) / Browserbase"
source_url: https://x.com/i/article/2056474246222880768
date: 2026-05-18
getxapi: false
tags:
  - browserbase
  - browse-sh
  - agent-skills
  - browser-agents
  - autobrowse
---

# Browse.sh, a catalog of browser skills for the Agentic future

TL;DR We built Browse.sh, an open catalog of 100+ curated browser skills that any agent can install with one CLI command. Our Skills are durable, reusable playbooks that capture how to navigate real websites, so your agents stop re-discovering every site from scratch on every run. All of this is powered by Autobrowse, our system that uses AI to iterate on real tasks until it converges on the cheapest, fastest path. Open source, free, and ready to use today at browse.sh.

Over 100 skills. Zero re-learning. Your agent's brain grew some grooves.

Browser Agents are everywhere right now, living in Claude Code, Cursor, and Codex. AI products are now shipping some version of "let the model drive a browser." And yet, every single one of these agents does the same dumb thing: it re-discovers every website from scratch, every time it runs.

Open a browser. Poke around. Find the button. Click it. Parse the response. Close the session. Forget everything, then do it all again tomorrow.

We've been building browser agents and infra at Browserbase for a while now. We've watched agents burn through tokens re-learning sites they've already conquered. We've watched customers painstakingly hand-write Playwright scripts for workflows an agent already solved last Tuesday. We've watched the same discovery tax get paid over and over, across thousands of sessions, by thousands of teams.

Today we're launching Browse.sh: an open catalog of browser skills that any agent can install and use immediately. 100 curated skills at launch and one CLI command to install.

## What is Browse.sh?

Browse.sh is two things:

1. **A catalog of browser skills** at browse.sh, where you can search, preview, and install curated skills for navigating real websites.
2. **The Browse CLI** (`npm i -g browse`), the open-source command-line tool your agents use to actually drive browsers, fetch pages, search the web, and load skills on demand.

A "skill" is a markdown file (SKILL.md) plus any helper scripts needed to repeat a browser workflow reliably. It contains the exact steps, gotchas, API endpoints, selectors, and fallback strategies an agent needs to complete a task on a specific site. No vector embeddings or screenshot reels. Just plain text that humans can read and agents can execute.

It's like a playbook. An agent that loads the Craigslist skill doesn't need to spend 30 turns figuring out that the search page is fully JS-rendered and that there's a hidden JSON API at sapi.craigslist.org. That knowledge is already in the skill. The agent reads it, runs it, and moves on.

## Why this exists

The unit economics are brutal. We benchmarked this on Craigslist: A generic agent loop searching listings costs ~$0.22 per run. After four Autobrowse iterations, the graduated Browse.sh skill does the same job for ~$0.12 per run — a 45% cost reduction from better memory.

The bottleneck for browser agents was never intelligence. It was amnesia. Browse.sh is the cure.

## How it works

1. **Install the CLI**: `npm i -g browse`
2. **Browse skills**: Search browse.sh for the site or task needed
3. **Install a skill**: `browse skills add zillow.com/extract-listings`
4. **Use it in your agent**: Point your agent at the skill and let it run
5. **Verify**: `browse skills list`

## What's inside a skill?

Every skill graduates from **Autobrowse**, a system that uses AI to improve AI. An agent runs a real task on a real site, studies its own trace, iterates on its strategy, and keeps going until the workflow becomes reliable. Once it converges, it writes out a durable skill.

Example Craigslist skill gotchas:
- Snapshot returns 0 refs on `/search/`: The search page is fully JS-rendered
- `item[0]` is NOT the postingId - it's an offset from `data.decode.minPostingId`
- API geolocates by request IP. Add `postal=<zip>` to override
- Rate-limit: keep ≤ 1 req/s sustained

## What shipped today

100 skills spanning:
- **Marketplaces**: Craigslist, Zillow, Amazon, eBay
- **Food & dining**: OpenTable, DoorDash, McDonald's online ordering
- **Travel**: flight search, hotel booking, Airbnb
- **Government**: federal grants portals, state program catalogs
- **Developer tools**: GitHub, npm, documentation sites
- **Enterprise SaaS**: via partner integrations (Ramp, Lovable, Poke, Reducto)

## The Vision

A dominant story about browser agents is that they'll get good when the underlying models get good. Browserbase doesn't buy that. Even a perfect model still has to discover, on every new site, what a perfect model would already know if it had been there before. Without a place to put what the agent learns, every run is a fresh start.

The real unlock for browser agents isn't better reasoning — it's better memory, in a form that humans can audit and agents can execute.

→ Kyle
