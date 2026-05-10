---
title: "Don’t accidentally leak secrets from your terminal"
source: "Warp Blog"
url: "https://www.warp.dev/blog/dont-accidentally-leak-secrets-from-your-terminal"
scraped: "2026-05-10T01:27:19.734591+00:00"
lastmod: "2026-04-24T14:39:24.000Z"
type: "sitemap"
---

# Don’t accidentally leak secrets from your terminal

**Source**: [https://www.warp.dev/blog/dont-accidentally-leak-secrets-from-your-terminal](https://www.warp.dev/blog/dont-accidentally-leak-secrets-from-your-terminal)

Product
Don’t accidentally leak secrets from your terminal
Melanie Crissey
October 19, 2023
Secret Redaction
is available on all Warp plans. You can turn it on today by navigating to
Settings → Privacy → Secret redaction
or by searching for “secret redaction” in the Command Palette (CMD - P).
Redact your secrets while demoing or working in public
Have you ever found yourself working in your terminal from a location that’s, let’s say,
less than private
?
Maybe you need to give a code demo on a conference stage or a live stream. Maybe you’re screen sharing with some coworkers who have different access privileges. Or, maybe you’re simply working from a coffee shop, an airplane, or a crowded coworking space for the day.
Whenever you’re working in public, you need to be extra careful about what information is on your screen, in case somebody’s looking over your shoulder—or worse, recording a “day in the life” selfie video.
When we’re working on the command line, we’re often dealing with sensitive or personal information like API keys, passwords, IP addresses, and otherwise sensitive information. It’s important we’re careful to only reveal these secrets in safe environments.
The good news is: if you’re using Warp, you can enable secret redaction to programmatically hide your secrets and sensitive information while you work, wherever you’re working.
How secret redaction works in Warp
When you enable this privacy setting, Warp will use regular expressions (regex) to superficially detect secrets in terminal output as text is printed. If the content of your terminal output matches any of the regex patterns, Warp will obscure the characters of the string with a lock icon.
Warp’s default list of regex for secrets
includes IP Addresses and common tokens, but you can also define your own custom regex expressions to hide secrets that aren't on the default list.
‍
Set custom rules for secret redaction in Warp's privacy settings.
Copy or reveal obscured secrets
As you’re working, you can hover over any masked secret to copy the secret to your clipboard or reveal it for reference.
Reveal, copy, or hide secrets in terminal output.
Remove secrets entirely when you’re sharing
Warp is unique from other terminals in that you can
share blocks of command line input and output
on permalinks which can be opened in a browser or embedded. Block sharing can be especially useful when you’re collaborating or debugging with your team at work.
Any time you’re sharing from your terminal, you should consider whether it makes sense to enable secret redaction for that shared block.
When you redact secrets for a shared block, Warp will remove the secrets entirely so they will not be included in the shared content. Characters in secrets are replaced with asterisks and cannot be revealed or copied.
Here is an example
of a Warp shared block with the secrets removed:
‍
You can visit this shared block at: https://app.warp.dev/block/1pHwKg52L81RqDRspdjKrI
Enable secret redaction in your terminal today
“Keep it secret, keep it safe!” We hope this small privacy setting will help you maintain some peace of mind while you work.
Please give secret redaction in Warp a try and let us know what you think. If you find this feature useful, we’d love to hear from you in
the Warp Discord community
.
Related articles
Apr 28, 2026  ·  7 min
Warp is now open-source
Warp is now open-source, and the community can participate in building it using an agent-first workflow managed by Oz, our cloud agent orchestration platform.
Apr 14, 2026  ·  2 min
Introducing Universal Agent Support: level up any coding agent with Warp
Warp now supports the most popular CLI coding agents — including Claude Code, Codex, Gemini CLI, and OpenCode — with vertical tabs, notifications, native code review, rich input, and remote control, making it the best terminal for multi-threaded agentic development.
Mar 24, 2026  ·  7 min
Build vs buy: how to deploy coding agents at scale
Should you build an in-house agent orchestration system or buy one off the shelf? Here's how to think about the decision and where the real complexity lies.
