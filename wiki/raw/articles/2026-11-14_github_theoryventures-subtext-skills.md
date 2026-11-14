---
title: "TheoryVentures/subtext-skills (README)"
url: https://github.com/TheoryVentures/subtext-skills
fetched_at: 2026-11-14T22:35:00+00:00
source: x-accounts-scan
tags: [blog, raw]
---

# TheoryVentures/subtext-skills (README)

Source: https://github.com/TheoryVentures/subtext-skills

GitHub - TheoryVentures/subtext-skills: Agent skills for creating and reading subtext documents — sentence-level annotated prose · GitHub
Skip to content
Navigation Menu
Sign in
Products
Platform
GitHub
Repository hosting, code review, and collaboration
Copilot
AI coding agent for tasks, projects, and automated work
Build & Ship
Actions
CI/CD and automation
Code Quality
Quality analysis, fixes, and enforcement
Codespaces
Cloud development environments
Secure
Code Security
Vulnerability detection and remediation
Secret Protection
Secret scanning and leak prevention
All Features
Developers
Learn
Documentation
Training
Certifications
Build
Build with Copilot
Customize Copilot
Integrations
Explore
Trending repos
GitHub Sponsors
Developer articles
Changelog
Changelog
Your source for the latest features, improvements, and fixes across GitHub products, all in one place.
Businesses
By Stage
Enterprises
Team
Startups
Nonprofits
By Industry
Healthcare
Financial services
Manufacturing
Government
See all industries
Evaluate GitHub
Why GitHub
Customer Stories
Business insights
Trust Center
Add-ons
GitHub Advanced Security
Enterprise-grade code security
Copilot for business
Enterprise-grade AI features
Premium Support
Enterprise-grade 24/7 support
Resources
Learn & Connect
Documentation
Resource center
Blog
Events & webinars
Community Forum
Customer Stories
Integrations
Support
Customer support
Training
GitHub Status
Company
About
Partners
Changelog
GitHub Universe
GitHub Universe
The event for developers, by developers — talks, workshops, and what’s next for GitHub.
Pricing
Search
/
Sign in
Sign up
Appearance settings
You signed in with another tab or window. 
Reload
 to refresh your session.
You signed out in another tab or window. 
Reload
 to refresh your session.
You switched accounts on another tab or window. 
Reload
 to refresh your session.
Dismiss alert
{{ message }}
TheoryVentures
subtext-skills
Repository navigation
Code
Issues
Pull requests
Actions
Projects
Security and quality
Insights
More
 items
subtext-skills
Public
Notifications
You must be signed in to change notification settings
Fork
0
 (
0
)
Star
20
 (
20
)
You must be signed in to star a repository
About
Agent skills for creating and reading subtext documents — sentence-level annotated prose
Resources
Readme
MIT license
Activity
Custom properties
Stars
20
 stars
Watchers
3
 watching
Forks
0
 forks
Report repository
main
Branches
Tags
Go to file
Code
Open more actions menu
Latest commit
History
1 Commit
1 Commit
Folders and files
Name
Name
Last commit message
Last commit date
.github/
workflows
.github/
workflows
subtext-annotate
subtext-annotate
subtext-read
subtext-read
.gitignore
.gitignore
LICENSE
LICENSE
README.md
README.md
package.sh
package.sh
View all files
Repository files navigation
README
MIT license
More
 items
Subtext Skills
Agent skills for working with 
subtext documents
 — prose structured sentence-by-sentence, where each sentence can carry author-supplied clarifications answering the questions a cold reader would have (undefined acronyms, ambiguous references, vague dates, missing context). The clarifications travel with the exact sentences they clarify, in a self-describing JSON format (
contextdoc/columnar-v1
).
Two skills are included:
Skill
What it does
subtext-annotate
Converts raw text (emails, notes, markdown) into a subtext document, then interviews you with clarifying questions and attaches your answers to the sentences they clarify.
subtext-read
Reads a 
.subtext.json
 file and presents it with the clarifications woven in at the point of confusion, plus a list of open questions the author couldn't answer.
Installation
Claude Desktop / claude.ai
Download the zips from the 
latest release
:
subtext-annotate.zip
subtext-read.zip
Go to 
Settings → Capabilities → Skills
 and upload each zip.
Claude Code
Copy the skill folders into your skills directory:
git clone https://github.com/TheoryVentures/subtext-skills.git
cp -R subtext-skills/subtext-annotate subtext-skills/subtext-read 
~
/.claude/skills/
Cursor
git clone https://github.com/TheoryVentures/subtext-skills.git
cp -R subtext-skills/subtext-annotate subtext-skills/subtext-read 
~
/.cursor/skills/
(Or place them in a project's 
.cursor/skills/
 to scope them to that project.)
Other clients
Any client that supports the 
Agent Skills
 convention (a folder containing a 
SKILL.md
 with YAML frontmatter) can use these — point it at the skill folders or unpack the release zips.
Usage
Annotate:
 share a document with your agent and ask it to "subtext this". The agent structures the text, asks you batched clarifying questions, and delivers a 
<title>.subtext.json
 artifact with your answers attached.
Read:
 share a 
.subtext.json
 file with your agent. It renders the document with clarifications inlined where they apply and lists any open questions.
Development
Skill folders live at the repo root; each contains a 
SKILL.md
 (and optionally a 
references/
 directory). To build the distributable zips locally:
./package.sh   
#
 zips land in dist/
Releases are automated: pushing a tag like 
v0.2.0
 builds the zips and attaches them to a GitHub Release.
License
MIT
About
Agent skills for creating and reading subtext documents — sentence-level annotated prose
Resources
Readme
MIT license
Activity
Custom properties
Stars
20
 stars
Watchers
3
 watching
Forks
0
 forks
Report repository
Releases
Packages
Contributors
Languages
Footer
        © 2026 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
Status
Community
Docs
Contact
      Manage cookies
        Do not share my personal information
    You can’t perform that action at this time.
