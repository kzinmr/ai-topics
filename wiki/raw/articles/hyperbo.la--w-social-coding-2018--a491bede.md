---
title: "Social Coding 2018 Recap"
url: "https://hyperbo.la/w/social-coding-2018/"
fetched_at: 2026-04-29T07:02:15.775242+00:00
source: "hyperbola :: blog"
tags: [blog, raw]
---

# Social Coding 2018 Recap

Source: https://hyperbo.la/w/social-coding-2018/

I keep track of every open source contribution I have ever made with the
#patch
hashtag on my
lifestream
. 2018 wasn’t a big year, but it was my best
so far. These are the contributions I made.
Contributions
Fix Resource Leak in Gunicorn
Gunicorn
is a Python WSGI server. Gunicorn can be configured using a Python
module that is loaded with
exec
. Gunicorn was not closing the file handle
after opening the provided module, which resulted in a
ResourceWarning: unclosed file
warning.
GH-1889
addresses the leak by
opening and reading the module using a
with
block.
Fix Ansible Deprecation Warnings in lets-encrypt-route-53 Role
ansible-role-lets-encrypt-route-53
is an
Ansible
role that uses Amazon
Route53 for the
dns-01
challenge with the
acme_certificate
module. Ansible
2.7 deprecated using
with_items
to specify packages with package modules, e.g.
apt
.
GH-14
updates the tasks to supply the list of packages directly to the
module.
Reduce Scope of Tokio Dependencies in futures-locks
futures-locks
is a Rust crate that provides
Futures
-aware locking
primitives.
futures-locks
depended on Tokio, which is a
fat
dependency.
tokio
is intended to be an
application crate
dependency; a
library crate
should
depend on tokio sub crates
.
GH-10
reduces the number of crates that
futures-locks
depends on from 51 to 3.
Successes in 2018
All of my PRs in 2018 are
linting
and
warning
shaped. By using these
libraries, I experienced some of their unfinished edges first-hand. This helped
narrow the scope of my first contributions to the projects. Narrowed scope
breeds two benefits: the changes are
good first issues
and the changes are
easier to merge.
Social Coding in 2019
Making an open source contribution has similar motivations to creating a
startup: solve a problem you have in an environment you know. Sending a PR
requires familiarity with the project; it requires you to have used the code. To
send more PRs in 2019, I need to
use more libraries
, which means broadening
scope and taking on projects in new domains.
