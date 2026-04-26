---
title: "Vibe Coding Trip Report: Making a sponsor panel"
url: "https://xeiaso.net/blog/2026/vibe-coding-sponsor-panel/"
fetched_at: 2026-04-25T12:08:14.245303+00:00
source: "xeiaso.net"
tags: [blog, raw]
---

# Vibe Coding Trip Report: Making a sponsor panel

Source: https://xeiaso.net/blog/2026/vibe-coding-sponsor-panel/

Vibe Coding Trip Report: Making a sponsor panel
Published on
2026-03-09
, 1226 words, 5 minutes to read
I needed to ship this before my surgery, so I vibe coded it. It turned out well enough.
-
I'm on
medical leave recovering from surgery
. Before I went under, I wanted to ship one thing I'd been failing to build for months: a sponsor panel at
sponsors.xeiaso.net
. Previous attempts kept dying in the GraphQL swamp. This time I vibe coded it — pointed agent teams at the problem with prepared skills and let them generate the gnarly code I couldn't write myself.
And it works.
The GraphQL swamp
Go and GraphQL are oil and water. I've held this opinion for years and nothing has changed it. The library ecosystem is a mess:
shurcooL/graphql
requires abusive struct tags for its reflection-based query generation, and the code generation tools produce mountains of boilerplate. All of it feels like fighting the language into doing something it actively resists.
Cadey
GitHub removing the GraphQL explorer made this even worse. You used to be able
to poke around the schema interactively and figure out what queries you
needed. Now you're reading docs and guessing. Fun.
I'd tried building this panel before, and each attempt died in that swamp. I'd get partway through wrestling the GitHub Sponsors API into Go structs, lose momentum, and shelve it. At roughly the same point each time: when the query I needed turned out to be four levels of nested connections deep and the struct tags looked like someone fell asleep on their keyboard.
Vibe coding was a hail mary. I figured if it didn't work, I was no worse off. If it did, I'd ship something before disappearing into a hospital for a week.
Preparing the skills
Vibe coding is not "type a prompt and pray." Output quality depends on the context you feed the model. Templ — the Go HTML templating library I use — barely exists in LLM training data. Ask Claude Code to write Templ components cold and it'll hallucinate syntax that looks plausible but doesn't compile. Ask me how I know.
Aoi
Wait, so how do you fix that?
I wrote four agent skills to load into the context window:
templ-syntax
: Templ's actual syntax, with enough detail that the model can look up expressions, conditionals, and loops instead of guessing.
templ-components
: Reusable component patterns — props, children, composition. Obvious if you've used Templ, impossible to infer from sparse training data.
templ-htmx
: The gotchas when combining Templ with HTMX. Attribute rendering and event handling trip up humans and models alike.
templ-http
: Wiring Templ into
net/http
handlers properly — routes, data passing, request lifecycle.
With these loaded, the model copies patterns from authoritative references instead of inventing syntax from vibes. Most of the generated Templ code compiled on the first try, which is more than I can say for my manual attempts.
Mara
Think of it like giving someone a cookbook instead of asking them to invent
recipes from first principles. The ingredients are the same, but the results
are dramatically more consistent.
Building the thing
I pointed an agent team at a spec I'd written with
Mimi
. The spec covered the basics: OAuth login via GitHub, query the Sponsors API, render a panel showing who sponsors me and at what tier, store sponsor logos in
Tigris
.
Cadey
I'm not going to pretend I wrote the spec alone. I talked through the
requirements with Mimi and iterated on it until it was clear enough for an
agent team to execute. The full spec is available as a gist if you want to
see what "clear enough for agents" looks like in practice.
One agent team split the spec into tasks and started building. A second reviewed output and flagged issues. Meanwhile, I provisioned OAuth credentials in the GitHub developer settings, created the Neon Postgres database, and set up the Tigris bucket for sponsor logos. Agents would hit a point where they needed a credential, I'd paste it in, and they'd continue — ops work and code generation happening in parallel.
The GraphQL code the agents wrote is
ugly
. Raw query strings with manual JSON parsing that would make a linting tool weep. But it works. The shurcooL approach uses Go idioms, sure, but it requires so much gymnastics to handle nested connections that the cognitive load is worse. Agent-generated code is direct: send this query string, parse this JSON, done. I'd be embarrassed to show it at a code review. I'd also be embarrassed to admit how many times I failed to ship the "clean" version.
query
:=
`{
viewer {
sponsors(first: 100) {
nodes {
... on User {
login
name
avatarUrl
}
... on Organization {
login
name
avatarUrl
}
}
}
}
}`
Numa
This code exists because the "proper" way kept killing the project. I'll
take ugly-and-shipped over clean-and-imaginary.
The stack
The full stack:
Go
for the backend, because that's what I know and what my site runs on
Templ
for HTML rendering, because I'm tired of
html/template
's limitations
HTMX
for interactivity, because I refuse to write a React app for something this simple
PostgreSQL
via
Neon
for persistence
GitHub OAuth
for authentication
GitHub Sponsors GraphQL API
for the actual sponsor data
Tigris
for sponsor logo storage — plugged it in and it Just Works™
The warts
Org sponsorships are still broken. The schema for organization sponsors differs enough from individual sponsors that it needs its own query path and auth flow. I know what the fix looks like, but it requires reaching out to other devs who've cracked GitHub's org-level sponsor queries.
The code isn't my usual style either — JSON parsing that makes me wince, variable names that are functional but uninspired, missing error context in a few places. I'll rewrite chunks of this after I've recovered. The panel
exists
now, though. It renders real data. People can OAuth in and see their sponsorship status. Before this attempt, it was vaporware.
Cadey
I've been telling people "just ship it" for years. Took vibe coding to make
me actually do it myself.
What I actually learned
I wouldn't vibe code security-critical systems or anything I need to audit line-by-line. But this project had stopped me cold on every attempt, and vibe coding got it across the line in a weekend.
Skills made the difference here. Loading those four documents into the context window turned Claude Code from "plausible but broken Templ" into "working code on the first compile." I suspect that gap will only matter more as people try to use AI with libraries that aren't well-represented in training data.
This sponsor panel probably won't look anything like it does today in six months. I'll rewrite the GraphQL layer once I find a pattern that doesn't make me cringe. Org sponsorships still need work. HTMX might get replaced.
But it exists, and before my surgery, shipping mattered more than polish.
The sponsor panel is at
sponsors.xeiaso.net
. The skills are in
my site's repo
under
.claude/skills/
.
Share
Facts and circumstances may have changed since publication. Please contact me before jumping to conclusions if something seems wrong or unclear.
Tags:
