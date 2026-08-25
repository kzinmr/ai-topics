---
title: "ElevenLabs CLI v1: agents as code, entire API in terminal"
source: "ElevenLabs Blog"
url: "https://elevenlabs.io/blog/elevenlabs-cli-v1"
scraped: "2026-08-25T06:00:29.370236+00:00"
lastmod: "2026-08-24T15:46:06.492Z"
type: "sitemap"
---

# ElevenLabs CLI v1: agents as code, entire API in terminal

**Source**: [https://elevenlabs.io/blog/elevenlabs-cli-v1](https://elevenlabs.io/blog/elevenlabs-cli-v1)

Blog
Product
Introducing the ElevenLabs CLI v1
Written by
Min
Kim
Paul
Asjes
Tadas
Petra
Published
Aug 24, 2026
Listen
Listen to this article
0:00
0:00
0:00
1.0x
On this page
Introduction
The entire platform from one interface
Agents-as-code
Built for coding agents and developers
Batteries are included with skills
Today we are introducing
v1 of the ElevenLabs CLI
that brings the ElevenLabs API directly into your terminal.
Coding agents already live in the terminal where they run commands, read results, and even
order lunch
. The ElevenLabs CLI was designed to be agents first, providing well documented commands and structured JSON results that are easy to parse and chain. It ships with a
--dry-run
mode to preview any operation before it touches your workspace.
The CLI also brings agents-as-code to ElevenAgents. Pull every agent in your workspace into local config files, edit them like any other part of your codebase, preview the exact diff, and push to production by hand or through your coding agent.
Install on macOS
brew
install elevenlabs/tap/elevenlabs
Windows
scoop
bucket add elevenlabs https://github.com/elevenlabs/scoop-bucket
scoop
install elevenlabs
cURL
curl
--proto
'=https'
--tlsv1.2 -LsSf
https://github.com/elevenlabs/cli/releases/latest/download/elevenlabs-cli-installer.sh
| sh
The entire platform from one interface
Every ElevenLabs API endpoint published in our
OpenAPI spec
is available as subcommands:
# list every agent in your workspace as structured JSON
elevenlabs
agents list
--format
json
# compose a song from a prompt
elevenlabs
music compose
--prompt
"lo-fi track for a rainy afternoon"
--output
track.mp3
# speak a sentence and save the audio
elevenlabs
text-to-speech convert
--voice-id
gPPH6SLdL8XSX6GNJ40G
--text
"Hello from the CLI"
--output
hello.mp3
Agents-as-code
Agents-as-code treats agent configuration the way you treat application code. You work on files on disk, and the CLI keeps them in sync with your workspace. The whole workflow fits in three commands.
elevenlabs
agents pull
# every agent in your workspace becomes a local config file
# edit a config: change the greeting, swap the voice, update the prompt
elevenlabs
agents push
--dry-run
# preview exactly what would change, without changing anything
elevenlabs
agents push
# apply
The same workflow extends to production. Branches keep development and production separate - a dev branch can use a test phone number and a cheaper LLM while production runs the real number and a frontier model. And for new projects,
elevenlabs agents init
scaffolds everything, with starter templates for common configurations like customer support.
With a handful of agents, the dashboard is manageable. However, when managing a fleet of agents spread across hundreds of customer orgs or bulk migrating agents from another platform, files and version control are the only workflow that scales.
Built for coding agents and developers
An agent using a CLI fails differently than a person does. It cannot answer an interactive prompt, it retries constantly, and it learns from whatever the error message gives it. The CLI is designed around this reality.
--help
is for people,
--schema
is for agents. Every API command prints a machine-readable contract like typed inputs, where each one goes, what's required, and the exact shape of the response. This lets the agent construct a valid call without guessing.
$
elevenlabs text-to-speech convert
--schema
{
  "operation"
:
"text-to-speech.convert",
"description"
:
"Create speech",
"binaryResponse"
: true
,
"input"
:
{
"properties"
:
{
"text"
:
{ "location": "body", "type": "string" },
"voice_id"
:
{ "location": "path", "type": "string" },
...
},
    "required"
:
[
"text"
,
"voice_id"]
}
}
Errors also give the agent something to work with. For agents, errors come back as JSON it can parse. When a human user is detected via TTY, a plain error message is shown instead. Both include instructions on how to fix the error.
Given the invalid command:
$
elevenlabs text-to-speech convert
--text
"Hello from the CLI"
Agents would get the following error message:
$
elevenlabs text-to-speech convert
--text
"Hello from the CLI"
{
  "error"
:
{
"code"
:
400,
"message"
:
"Required parameter 'voice_id' is missing. Provide it via --voice-id or --params",
"reason"
:
"validationError"
}
}
Whereas human users see this error that is more legible and includes a hint on how to fix the problem:
error[validation]:
 Required
parameter 'voice_id' is missing. Provide it via
--voice-id
or
--params
Try
`
elevenlabs
text-to-speech convert
--help
`
Batteries are included with skills
--help
and
--schema
are the CLI's built-in manual. But skills go further and teach your coding agent complete workflows like how to build an agent, generate speech, or transcribe a call.
Install them into your project:
elevenlabs
generate-skills
Agents already live in the terminal. Now all of ElevenLabs does too. Install the CLI, hand your agent the skills, and see what it ships. Get started with
docs
.
