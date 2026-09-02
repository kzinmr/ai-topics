---
title: "Python 3.15.0 candidate 2 is here!"
url: "https://simonwillison.net/2026/Sep/1/python-315-rc-2/"
fetched_at: 2026-09-02T10:01:17.038865+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# Python 3.15.0 candidate 2 is here!

Source: https://simonwillison.net/2026/Sep/1/python-315-rc-2/

1st September 2026 - Link Blog
Python 3.15.0 candidate 2 is here!
(
via
) Hugo van Kemenade (release manager for Python 3.14 and 3.15) announces the final release candidate for Python 3.15, scheduled for release in October:
Entering the release candidate phase, only reviewed code changes which are clear bug fixes are allowed between this release candidate and the final release. [...]
We
strongly encourage
maintainers of third-party Python projects to prepare their projects for 3.15 during this phase, and publish Python 3.15 wheels on PyPI to be ready for the final release of 3.15.0, and to help other projects do their own testing. Any binary wheels built against Python 3.15.0 release candidates
will work
with future versions of Python 3.15.
Back in 2021 I
found a bug in Python 3.10
by running my test suites against it... but I hadn't done this during the RC period, so that bug had already shipped! Since then I've always paid much closer attention to these RCs.
The new RC isn't available for GitHub Actions just yet - keep an eye on
actions/python-versions
for that. For the moment though you can add this to a testing matrix:
strategy
:
matrix
:
python-version
:
["3.14", "3.15"]
steps
:
  -
uses
:
actions/setup-python@v7
with
:
python-version
:
${{ matrix.python-version }}
allow-prereleases
:
true
check-latest
:
true
The
allow-prereleases
and
check-latest
flags mean that today this will test against RC1, and when RC2 lands it will automatically switch to that version (and then the stable version once that comes out.)
Update
:
Datasette passes
,
sqlite-utils passes
, LLM is
currently blocked
waiting for a 3.15 wheel for
scikit-learn
, which is optionally used in the test suite.
