---
type: article
title: "How to Ditch Codecov for Python Projects"
source: hynek.me
date: 2021-11-18
url: https://hynek.me/articles/ditch-codecov-python/
author: Hynek Schlawack
x_referrer: @hynek
---

How to Ditch Codecov for Python Projects

18 November 2021

9 June 2026

Codecov’s unreliability breaking CI on my open source projects has been a constant source of frustration for me for years. I have found a way to enforce coverage over a whole GitHub Actions build matrix that doesn’t rely on third-party services.

Coverage.pyhas the option to fail the call tocoverage reportif coverage is less thanXXXalready built in: either the settingfail_under=XXXor the command line option--fail-under=XXX. The only reason why I’ve traditionally usedCodecov(including in myPython in GitHub Actionsguide), is because I need to measure coverage over multiple Python versions that run indifferent containers. Therefore I can’t just runcoverage combine, I need to store them somewhere between the various build matrix items.

Coverage.py

has the option to fail the call to

coverage report

if coverage is less than

XXX

already built in: either the setting

fail_under=XXX

or the command line option

--fail-under=XXX

. The only reason why I’ve traditionally used

Codecov

(including in my

Python in GitHub Actions

guide), is because I need to measure coverage over multiple Python versions that run in

different containers

. Therefore I can’t just run

coverage combine

, I need to store them somewhere between the various build matrix items.

Unfortunately, Codecov has grownveryflaky. I have lost any confidence in the fact when it fails a build and my first reaction is always to restart the build and onlytheninvestigate. Sometimes the upload fails, sometimes Codecov fails to report its status back to GitHub, sometimes it can’t find the build, and sometimes it reports an outdated status. What a waste of computing power. What a waste of my time, clicking through their web application, seeing everything green, yet the build is failing due to missing coverage.

Unfortunately, Codecov has grown

very

flaky. I have lost any confidence in the fact when it fails a build and my first reaction is always to restart the build and only

then

investigate. Sometimes the upload fails, sometimes Codecov fails to report its status back to GitHub, sometimes it can’t find the build, and sometimes it reports an outdated status. What a waste of computing power. What a waste of my time, clicking through their web application, seeing everything green, yet the build is failing due to missing coverage.

When Icomplained about this once againand evensketched out my ideahow it could work, I’ve been told that thecookiecutter-hypermodern-pythonproject hasalready been doing it1and there’s aGitHub Actiontaking the same approach!

When I

complained about this once again

and even

sketched out my idea

how it could work, I’ve been told that the

cookiecutter-hypermodern-python

project has

already been doing it

1

and there’s a

GitHub Action

taking the same approach!

So, I removed Codecov from all my projects and it’s glorious! Not only did I get rid of a flaky dependency, it also simplified myworkflow. The interesting parts are the following:

So, I removed Codecov from all my projects and it’s glorious! Not only did I get rid of a flaky dependency, it also simplified my

workflow

. The interesting parts are the following:

After running the testsunder coverage inparallelmode, add astepthat uploads the coverage files as artifacts as part of the test-running jobs:

After running the tests

under coverage in

parallel

mode, add a

step

that uploads the coverage files as artifacts as part of the test-running jobs:

-name:Upload coverage datauses:actions/upload-artifact@043fb46d1a93c77aae656e7c1c64a875d1fc6a0a# v7.0.1with:name:coverage-data-${{ matrix.python-version }}path:.coverage.*include-hidden-files:trueif-no-files-found:ignore

-

name

:

Upload coverage data

uses

:

actions/upload-artifact@043fb46d1a93c77aae656e7c1c64a875d1fc6a0a

# v7.0.1

with

:

name

:

coverage-data-${{ matrix.python-version }}

path

:

.coverage.*

include-hidden-files

:

true

if-no-files-found

:

ignore

You need this for every item in your build matrix whose coverage you want to take into account. You have to add every dimension of your matrix to the name. This example assumes that your matrix only consists of Python versions, which is true for most Python projects.

I useif-no-files-found: ignore, because I don’t run all Python versions under coverage. It’s much slower and I don’t need every Python version to ensure 100% coverage.

I use

if-no-files-found: ignore

, because I don’t run all Python versions under coverage. It’s much slower and I don’t need every Python version to ensure 100% coverage.

After all tests passed, add a newjob:

After all tests passed

, add a new

job

:

coverage:name:Ensure 100% test coverageruns-on:ubuntu-latestneeds:testsif:always()steps:-uses:actions/checkout@df4cb1c069e1874edd31b4311f1884172cec0e10# v6.0.3with:persist-credentials:false-uses:actions/setup-python@a309ff8b426b58ec0e2a45f0f869d46889d02405# v6.2.0with:# latest version you support, so it understands all syntaxpython-version:"3.14"-uses:hynek/setup-cached-uv@4300ec2180bc77d705e626a34e381b81a4772c51# v2.5.0-name:Download coverage datauses:actions/download-artifact@3e5f45b2cfb9172054b4087a40e8e0b5a5461e7c# v8.0.1with:pattern:coverage-data-*merge-multiple:true-name:Combine coverage and fail if it's <100%run:|uv tool install coveragecoverage combinecoverage html --skip-covered --skip-empty# Report and write to summary.coverage report --format=markdown >> $GITHUB_STEP_SUMMARY# Report again and fail if under 100%.coverage report --fail-under=100-name:Upload HTML report if check faileduses:actions/upload-artifact@043fb46d1a93c77aae656e7c1c64a875d1fc6a0a# v7.0.1with:name:html-reportpath:htmlcovif:${{ failure() }}

coverage

:

name

:

Ensure 100% test coverage

runs-on

:

ubuntu-latest

needs

:

tests

if

:

always()

steps

:

-

uses

:

actions/checkout@df4cb1c069e1874edd31b4311f1884172cec0e10

# v6.0.3

with

:

persist-credentials

:

false

-

uses

:

actions/setup-python@a309ff8b426b58ec0e2a45f0f869d46889d02405

# v6.2.0

with

:

# latest version you support, so it understands all syntax

python-version

:

"3.14"

-

uses

:

hynek/setup-cached-uv@4300ec2180bc77d705e626a34e381b81a4772c51

# v2.5.0

-

name

:

Download coverage data

uses

:

actions/download-artifact@3e5f45b2cfb9172054b4087a40e8e0b5a5461e7c

# v8.0.1

with

:

pattern

:

coverage-data-*

merge-multiple

:

true

-

name

:

Combine coverage and fail if it's <100%

run

:

|

uv tool install coverage

coverage combine

coverage html --skip-covered --skip-empty

# Report and write to summary.

coverage report --format=markdown >> $GITHUB_STEP_SUMMARY

# Report again and fail if under 100%.

coverage report --fail-under=100

-

name

:

Upload HTML report if check failed

uses

:

actions/upload-artifact@043fb46d1a93c77aae656e7c1c64a875d1fc6a0a

# v7.0.1

with

:

name

:

html-report

path

:

htmlcov

if

:

${{ failure() }}

It setsneeds: teststo ensure all tests are done, but it also setsif: always()such that the coverage is measured even if one of the tests jobs fails. If your job that runs tests has a different name, you will have to adapt this. Check out the fullworkflowif you’re unsure where exactly to put the snippets.

It sets

needs: tests

to ensure all tests are done, but it also sets

if: always()

such that the coverage is measured even if one of the tests jobs fails. If your job that runs tests has a different name, you will have to adapt this. Check out the full

workflow

if you’re unsure where exactly to put the snippets.

In a nutshell:

It downloads the coverage data that the tests uploaded as artifacts,

combines it,

creates an HTML report,

creates a Markdown report that is added to the job summary,

and finally checks if coverage is 100% – failing the job if it is not. If – and only if! – this step fails (presumably due to a lack of coverage), it also uploads the HTML report as an artifact.

Once the workflow is done, you can see the plain-text report at the bottom of the workflow summary page. If the coverage check failed, there’s also the HTML version for download.

The workflow summary with a plain-text report.

If you’d like a coverage badge, check out Ned’s guide:Making a coverage badge.

If you’d like a coverage badge, check out Ned’s guide:

Making a coverage badge

.

Note onuv

Note on

uv

This workflow usesuvto install Coverage.py, because it’s fast and amazing. The rest of your project doesn’t have to useuv.

This workflow uses

uv

to install Coverage.py, because it’s fast and amazing. The rest of your project doesn’t have to use

uv

.

It uses my ownsetup-cached-uv, but feel free to use Astral’s official one:setup-uv.

It uses my own

setup-cached-uv

, but feel free to use Astral’s official one:

setup-uv

.

If youreallydon’t want to useuv, you can remove thesetup-cached-uvstep and usepython -Im pip install --upgrade coverageto install Coverage.py.

If you

really

don’t want to use

uv

, you can remove the

setup-cached-uv

step and use

python -Im pip install --upgrade coverage

to install Coverage.py.

History

2026-06-09: General updates; makeuvthe default.

2026-06-09

: General updates; make

uv

the default.

2024-09-16: Added a note onuv.

2024-09-16

: Added a note on

uv

.

2024-09-03: Fixed hidden files upload onactions/upload-artifactv4.4.0.

2024-09-03

: Fixed hidden files upload on

actions/upload-artifact

v4.4.0.

2024-01-02: Adapted to v4 ofactions/upload-artifactandactions/download-artifact.

2024-01-02

: Adapted to v4 of

actions/upload-artifact

and

actions/download-artifact

.

2023-07-24:coverage report --format=markdownis a thing“now”!

2023-07-24

:

coverage report --format=markdown

is a thing

“now”

!

2023-04-12: updated with plain-text reporting.

2023-04-12

: updated with plain-text reporting.

They still upload the combined coverage toCodecovwhich can be useful for the web interface. I personally don’t think I wantthispart of my CIs.↩︎

They still upload the combined coverage to

Codecov

which can be useful for the web interface. I personally don’t think I want

this

part of my CIs.

↩︎

This post was made possible by thedonationsfrom people and corporations who appreciate my public work.

This post was made possible by the

donations

from people and corporations who appreciate my public work.

Want more content like this? Here's my free, low-volume, non-creepyHynek Did Somethingnewsletter!
It allows me to share my content directly with you and add extra context:

Want more content like this? Here's my free, low-volume, non-creepy

Hynek Did Something

newsletter

!
It allows me to share my content directly with you and add extra context:

Hynek Schlawack

Code Bohemian in ❤️ with Python 🐍, Go 🐹, and DevOps 🔧.Blogger📝,speaker📢,YouTuber📺,
PSFfellow🏆,
substance over flash 🧠.

Code Bohemian in ❤️ with Python 🐍, Go 🐹, and DevOps 🔧.

Blogger

📝,

speaker

📢,

YouTuber

📺,
PSF

fellow

🏆,
substance over flash 🧠.

Is my content helpful and/or enjoyable to you?
Please considersupporting me!
Every bit helps to motivate me in creating more.

Is my content helpful and/or enjoyable to you?
Please consider

supporting me

!
Every bit helps to motivate me in creating more.