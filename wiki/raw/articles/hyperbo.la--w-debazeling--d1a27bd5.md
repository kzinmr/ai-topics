---
title: "Debazeling the blog"
url: "https://hyperbo.la/w/debazeling/"
fetched_at: 2026-04-29T07:02:15.348175+00:00
source: "hyperbola :: blog"
tags: [blog, raw]
---

# Debazeling the blog

Source: https://hyperbo.la/w/debazeling/

As of this post’s publishing, the
most recent post on the livestream
reads:
Recently I’ve been on the “I should write a blog post” to “spend 2 hours
updating dependencies across 4 language ecosystems in my blog’s Bazel
monorepo” pipeline. I should still write that blog post though #hypstatic
#bazel
In early 2022, I converted this site’s build system from its previous iteration,
a hand-spun and ad hoc static site generator written in JavaScript which
compiled in multiple passes, to Bazel to learn how to be productive with the
build system since it was a significant chunk of my org’s focus at Brex.
Right before I tore it down, the git repo this blog lives in was
more than 25%
Starlark
!!! I certainly did not
do the simplest thing that could possibly
work
.
History
hyperbo.la
’s past is littered with different builds of the site. From oldest
to newest:
Rendering
Database
Infra
Failure
WordPress
MySQL
httpd, mod_php, dyndns.org
Hacked
Django, handspun CSS
SQLite
httpd, mod_python, dyndns.org
rm -rf
’d the DB
Django, Bootstrap
MySQL
A single linode, httpd, mod_python, mod_wsgi, nginx, gunicorn, ad hoc shell scripts
boredom, desire to automate
Django, Bootstrap
Aurora MySQL and clustered Elasticache, then multi-AZ MySQL RDS with DB-backed caching
ALB, S3, Terraform, Packer, Ansible, spot instances
high cost
Webpack-driven SSG, Bootstrap
YAML and markdown
GitHub Pages, GitHub Actions
page count started crashing Webpack
Custom JS SSG, Bootstrap
YAML and markdown
GitHub Pages, GitHub Actions
dependency hell
A largely golang dev server and SSG compiler, Bootstrap via rules_sass and a custom BUILD.bazel for the Bootstrap repo
YAML and markdown
Bazel, GitHub Pages, GitHub Actions
Bazel ecosystem moves too quickly, things were constantly breaking and I
needed
to keep on top of rules upgrades
Vite, Tailwind CSS
YAML and Markdown
GitHub Pages, GitHub Actions
TBD
Why this version is good
Well for one all of the code here is only there to support rendering HTML
and
there is very little of that code
.
Using modern frontend technologies made switching to Tailwind CSS a couple of
hours of work vs. what would have been days. It feels nice to have modern
typography, a comfier layout, and to support light/dark mode
and
also maintain
the core app shell and branding.
This is what the blog index page looked like before cutting over to Tailwind,
which is essentially the way the site looked for 10 years:
And after the cutover:
Why is this new version bad
I still don’t write. Prior to authoring this post, the last updates on both the
blog and the livestream were 2 years before debazeling.
