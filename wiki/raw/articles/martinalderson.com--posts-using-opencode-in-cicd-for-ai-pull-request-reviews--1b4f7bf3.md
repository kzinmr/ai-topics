---
title: "Using OpenCode in CI/CD for AI pull request reviews"
url: "https://martinalderson.com/posts/using-opencode-in-cicd-for-ai-pull-request-reviews/?utm_source=rss&utm_medium=rss&utm_campaign=feed"
fetched_at: 2026-04-29T07:02:04.062889+00:00
source: "martinalderson.com"
tags: [blog, raw]
---

# Using OpenCode in CI/CD for AI pull request reviews

Source: https://martinalderson.com/posts/using-opencode-in-cicd-for-ai-pull-request-reviews/?utm_source=rss&utm_medium=rss&utm_campaign=feed

Most existing AI code review tools require you to grant them access to your GitHub or GitLab repositories. While some of these tools are interesting, the security implications of handing over repo access to a third party are significant - and they're typically GitHub or GitLab-first. If you're working on projects that don't use either of those platforms, you're out of luck.
I run a few projects where we don't use GitHub or GitLab, so these tools simply aren't an option. That led me to explore an alternative: using
OpenCode
- an open source agentic coding CLI, similar to Claude Code - with Codex 5.3, powered by a ChatGPT Plus or Team subscription.
Why not just use the existing tools?
The honest answer is I don't want to give another SaaS product access to my repositories. Yes, these companies probably handle your code responsibly - but also, famously, might not. But it's another attack surface, another vendor to evaluate, another set of permissions to manage. I've written before about
agents eating SaaS
- and this is a perfect example. Why pay for a code review wrapper when you can just run the agent yourself?
And for anything that isn't on GitHub or GitLab - Bitbucket, self-hosted Gitea, whatever - you're on your own anyway. These tools (generally) don't support you.
Setting up the pipeline
The setup is surprisingly straightforward if you're working with any YAML-based CI/CD system - GitHub Actions, GitLab CI, Bitbucket Pipelines, whatever you prefer.
Your pipeline needs to:
Clone the repo (most CI providers do this by default)
Install OpenCode - I run it in Docker with limited sandboxing
Copy in your OpenCode
auth.json
config file (I inject this via an environment variable - one annoyance is the OpenAI key expires after 14 days, so there may be a better way to handle this)
Pass a prompt to OpenCode asking it to review the PR for code quality, potential bugs, and suggestions, based on a Git diff, outputting a
report.md
file
Post the output back to your Git provider as a PR comment via what ever API makes sense. You can also send to Slack or any other system here.
That's it. The whole thing took me an afternoon to get working, and the review quality has been
genuinely
useful - not just "add more comments" noise.
It's actually a really short prompt I settled on and has been giving me pretty outstanding results that really just flags critical things:
opencode run -m openai/gpt-5.3-codex "

Code review for {{TYPE OF APP, e.g. TypeScript app doing...}}

1. Read CLAUDE.md first - architecture, lessons learned
2. Run: git diff $BASE_BRANCH...HEAD
3. Read full changed files + related files (interfaces, callers, services)

CONSERVATIVE REVIEW - False positives waste developer time:

- VERIFY every concern by reading the actual code before flagging
- Performance issue? Confirm caching/batching doesn't already exist
- Missing validation? Confirm it's not handled upstream
- Security concern? Trace the full request flow
- If you're not 90%+ sure after verification, don't flag it

Skip: style, formatting, naming, docs, hypotheticals.
                  
Also check what current tests may hit this, and if they are sufficient for these changes? DO NOT run the tests, just quick reasoning.
                  
This should be a separate section of your output report, titled Test Coverage

Write concise review to report.md with file:line refs. LGTM if good.
"
You can tweak this to your requirements. I'd like to extend this further with ticket information, for example.
The economics are hard to argue with
This is the part that really got my attention. OpenAI lets you use your existing ChatGPT Plus, Pro, or Business subscription with OpenCode. There are no additional per-license, per-user, per-developer, or per-CI fees. OpenAI have
confirmed
they're actively working with OpenCode to support this. This is where I think Anthropic are making a major mistake - I'd love to use Claude Code in headless mode for this, but I'm not even sure if it's allowed under their ToS.
Compare that to the existing code review SaaS products charging per seat, per repo, or per PR. For a team of any size, the maths gets ugly fast. And if you're already paying for ChatGPT, the marginal cost of adding PR reviews is effectively zero.
I think this does show just how thin the layer AI wrappers have is. As agents get better and better, it's easier and easier to replace 'specialised' tools with this.
You keep control of your code
This matters more than people think. Your code passes through your CI/CD runners - that's expected and doesn't introduce a new threat surface. You're not granting OAuth access to a third party. You're not trusting that some startup's S3 bucket is properly locked down.
To be clear - your code is still being sent to OpenAI's API for inference, so it's not truly air-gapped in the default setup. But if you're already using any agentic coding tools (Claude Code, Codex, Cursor, etc.), your code is already going to these providers. The difference here is you're cutting out the
middleman
- there's no additional third party with persistent access to your repositories.
For organisations with genuinely high-sensitivity requirements, you can point OpenCode at a local model and run the whole thing air-gapped with absolutely nothing leaving your CI/CD environment. This obviously requires a decent amount of VRAM, but it's a genuinely promising way to bring agentic code review to environments where SaaS tools are a non-starter.
Beyond PR reviews
I've also built a Slack bot that works in exactly the same way. Instead of being triggered by a Git provider, you ask a question directly in Slack. The bot grabs a read-only copy of the repo, fires up OpenCode, and posts the output back as a reply on the thread.
Want to ask "where is the retry logic for payment processing?" without opening your IDE? Done. Need a quick summary of what changed in the last sprint? Done. It's basically giving your entire team a senior engineer they can ask questions to at any time.
A note on Codex CLI
I did try to get this working with Codex CLI itself, but ran into issues with sandboxing. It kept complaining about Landlock not being enabled on the kernel, so I switched to OpenCode.
OpenCode is also provider agnostic, so if OpenAI decides to change their ToS for this kind of activity you can just replace the
opencode run -m openai/gpt-5.3-codex
with
minimax/minimax-m2
in your pipeline file and run on another provider.
What's next
PR reviews are the obvious starting point, but some obvious next steps is getting the agent to actually resolve comments and propose a new PR. This would not be difficult to do with this pattern, but I'd like to spend some time building 'specialised' agents for other tasks past software engineering - for example, auditing the quality of the UX and giving suggestions if that is regressing in a PR.
If you're a smaller team already paying for ChatGPT subscriptions and also paying for a separate AI code review tool, it might be worth spending an afternoon seeing if you can replace the latter with the former.
