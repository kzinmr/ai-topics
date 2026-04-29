---
title: "Do the Simplest Thing That Could Possibly Work"
url: "https://hyperbo.la/w/do-the-simplest-thing/"
fetched_at: 2026-04-29T07:02:15.410722+00:00
source: "hyperbola :: blog"
tags: [blog, raw]
---

# Do the Simplest Thing That Could Possibly Work

Source: https://hyperbo.la/w/do-the-simplest-thing/

When working with the tech leads in my group and other senior engineers on cross
functional projects, I often find myself saying
do the simplest thing that
could possibly work
to unstick technical debates and requirements gathering
sinkholes.
When building out a system,
do the simplest thing that could possibly work
means:
Minimum scaffolding, minimum ceremony, minimal automation.
Handle the happy path only.
Stub as much as possible.
Defer specifying as much behavior as possible.
Do the simplest thing that could possibly work
neatly packages up my favorite
extreme programming (XP)
principles of
don’t paint yourself into a
corner
and
you aren’t gonna need it
(YAGNI)
while also not
being overtly confrontational.
Do the simplest thing that could possibly work
communicates the need to shed
scope, think incrementally, bias to action instead of over-design, and get
product in the hands of the folks who will be using it.
Webapp and Mobile App Localization
Recently, I leaned in to a cross-functional project which was working on a
direct KR of a company level objective: to support global expansion of the
business, we sought to localize the web dashboard and mobile apps for the
product.
This project involved about 12 engineers, 1 designer, 2 engineering managers,
and 1 first-time project lead. The squad had frontend-oriented expertise but
little experience with l10n systems and i18n migrations. I was often the only
voice in the room advocating for use of the
Intl
APIs, relying on
user
agents to communicate locale preferences
, and not
rolling our own strings for
month abbreviations
in
German.
This combined with the lack of PM support or a PRD led to an explosion in
complexity:
A backend service was proposed to store per-user individual locale settings
such as decimal separator, RTL vs LTR text direction, and date format.
A design was completed for a 3-service evented workflow on top of a Retool
page and a full-blown Postgres RDS for updating our translation vendor when we
added a new locale.
The team decided to take localizing marketing campagins into scope.
A flow diagram was created for a complex locale defaulting flow which
considered device settings, stored user preferences, the user’s associated
legal entity’s preferences, and enterprise settings.
The team spent multiple 2-hour meetings per week debating edge cases in locale
selection and rendering looking for consensus in the large group. No code was
written for the first 5 weeks of the project.
Do One Thing
To get the team out of the design quagmire and anchored in more concrete
deliverables, I gave the team one goal: show me 3 pages with German strings.
Within a week, the settings page in both the web and mobile apps was rendering
in German, the login page was rendered in the language set by the user’s
browser, and the entire dashboard had a locale selector to toggle between
English and German strings.
What complexity gave way to make this happen?
Translation strings were hardcoded into two JSON files. We skipped all
pipeline and vendor configuration.
The team selected the
react-i18next
library and minimally wired it up.
The
Accept-Language
header drove localization of the login page where users
had not yet authenticated (and thus we didn’t have their locale preference
available). Locale settings were stored in a flat table with at most one
preference per user.
The team was forced to contend with (simple) date formatting.
Take on Toil
A very effective strategy for
do the simplest thing that could possibly work
is to take on toil in lieu of automation.
Rather than build out that evented workflow for orchestrating the translation
vendor, a runbook and click ops in the vendor dashboard will suffice, likely for
forever. The CI pipeline does not need to be complete; instead, the on-call
engineer will download snapshots of the translated locales once per week and
manually push a PR.
Toil can take you a surprisingly long way. Stripe had an
entire organization
(Tech Ops) to manually retry and reconcile payment and ledgering failures.
Ocassionally, Citi would respond with a new payout failure code (did you know
there are like 6 different codes to indicate the recipeint is deceased?); these
failures were manually investigated and added to one of 3 static
Hash
es in a
Ruby source file to remediate.
Wrapup
Do the simplest thing that could possibly work
is a mechanism to be
incremental and focus scarce engineering resources on the higest leverage
deliverable. That can either mean quickly iterating in a 0 to 1 or 1 to 10
context; or it can mean moving on to the next most important unsolved problem.
