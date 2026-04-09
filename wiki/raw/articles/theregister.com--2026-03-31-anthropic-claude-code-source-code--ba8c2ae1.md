---
title: "Anthropic accidentally exposes Claude Code source code • The Register"
url: "https://www.theregister.com/2026/03/31/anthropic_claude_code_source_code/"
fetched_at: 2026-04-09T16:28:07.884584+00:00
source_date: 2026-04-10
tags: [newsletter, auto-ingested]
---

# Anthropic accidentally exposes Claude Code source code • The Register

Source: https://www.theregister.com/2026/03/31/anthropic_claude_code_source_code/

Would you like a closer look at Claude? Someone at Anthropic has some explaining to do, as the official npm package for Claude Code shipped with a map file exposing what appears to be the popular AI coding tool's entire source code.
It did as of Tuesday morning, at least, which is when security researcher Chaofan Shou appears to have spotted the exposure and
told the world
. Snapshots of Claude Code's source code were quickly backed up in a GitHub repository that has been forked more than 41,500 times so far, disseminating it to the masses and ensuring that Anthropic's mistake remains the AI and cybersecurity community’s gain.
According to the GitHub
upload
of the exposed Claude Code source, the leak actually resulted from a reference to an unobfuscated TypeScript source in the map file included in Claude Code's npm package (map files are used to connect bundled code back to the original source). That reference, in turn, pointed to a zip archive hosted on Anthropic's Cloudflare R2 storage bucket that Shou and others were able to download and decompress to their hearts' content.
Contained in the zip archive is a wealth of info: some 1,900 TypeScript files consisting of more than 512,000 lines of code, full libraries of slash commands and built-in tools - the works, in short.
That said, Claude Code's source isn't a complete mystery, and while this exposure gives us a look at a fresh iteration of Claude Code straight from the leaky bucket, it's not blowing the lid off of something that was a secret until now.
Claude Code has been
reverse engineered
, and various projects have resulted in an
entire website
dedicated to exposing the hidden portions of Claude Code that haven't been released to, or shared with, the public.
In other words, what we have is a useful comparison point and update source for the CCLeaks operators, and maybe a few new secrets will come to light as people dig through the exposed code.
Far more interesting is the fact that someone at Anthropic made a mistake as bad as leaving a map file in a publish configuration. Publishing map files is generally frowned upon, as they're meant for debugging obfuscated or bundled code and aren't necessary for production. Not only that, but as we've seen in this example, they can easily be used to expose source code, as they're a reference document for that original.
As pointed out by software engineer Gabriel Anhaia in a deep dive into the exposed code, this should serve as a reminder to even the best developers to check their build pipelines.
"A single misconfigured .npmignore or files field in package.json can expose everything," Anhaia wrote in his
analysis
of the Claude Code leak.
Anthropic admitted as much in a statement to
The Register
, saying that, yes, it was good ol' human error responsible for this snafu.
"Earlier today, a Claude Code release included some internal source code," an Anthropic spokesperson told us in an email, adding that no customer data or credentials were involved or exposed. "This was a release packaging issue caused by human error, not a security breach. We're rolling out measures to prevent this from happening again."
As of this writing, the original uploader of the Claude Code source to GitHub has repurposed his repo to host a Python
feature port
of Claude Code instead of Anthropic's directly exposed source, citing concerns that he could be held legally liable for hosting Anthropic's intellectual property.
Plenty of forks
and mirrors remain for those who want to inspect the exposed code.
We asked Anthropic if it was considering asking people to remove their repositories of its exposed source code, but the company didn't have anything to say beyond its statement. ®
