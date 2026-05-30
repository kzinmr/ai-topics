---
title: "My Agent Stack For Automating My Personal Life"
type: x_article
x_article_title: "My Agent Stack For Automating My Personal Life"
x_article_author: "Peter Steinberger (@steipete)"
getxapi: false
created: 2026-05-30
sources:
  - https://x.com/i/article/2060579190920110081
---

# My Agent Stack For Automating My Personal Life

My agent manages my emails, SMS, Whatsapp, Telegram and pretty much everything to automate my personal life.

People keep asking me how I use agents in real life. I mean the actual boring things that make a day disappear: reading WhatsApp and Telegram, finding someone's email, searching the web, drafting the intro, updating a document in Google Drive, creating a calendar event, checking who still needs an answer, and doing all of that across the same messy tools I already use.

My answer is disappointingly simple. I use Codex as an operator on top of my actual life data. It has tools. It has data connectors. It has skills. It has a source of truth. It has enough permissions to act locally, and enough approval gates that it does not embarrass me in public.

That is basically the setup. Tools, data connectors, skills, and taste.

I used to do more of this in Claude Code but I have been moving the setup to Codex because GPT-5.5 is currently a better model for this kind of work. The switch from Claude Code to Codex is not really the story. The story is that once a model is good enough, the real leverage comes from wiring it into the world you already live in.

The important part is that the agent can move across boundaries. My personal life is not in one app. It is split between Gmail, WhatsApp, Telegram, iMessage, Google Drive, Calendar, Notion, local files, random PDFs, browser sessions, and a contacts spreadsheet that is much more valuable than it looks.

## A Real Communication Example

A few days ago a friend sent me a WhatsApp message. She was helping a fast-growing San Francisco AI startup recruit in France and wanted to connect their recruiting manager with a recruiter I know. I did not remember the recruiter's email. I did not know the latest funding news about the startup. I needed to search WhatsApp, search Gmail, find the recruiter's email, search the web, understand why the startup was credible, draft an intro email, include the two job links, show the draft to me, send the email after approval, and then text my friend that it was done.

That is normally twenty minutes of annoying app switching. WhatsApp to Gmail to Google search to Gmail again to WhatsApp again. It is not hard work, but it is exactly the kind of work that burns attention because every step is a small context switch.

With the agent, I asked for the outcome. It read the WhatsApp thread, searched Gmail for the recruiter's email, researched the startup's funding and recent news on the web, drafted the intro, waited for my approval, sent the email, and then texted my friend that the intro was done. The user-facing part took about ten seconds. The agent did the glue work (in seconds!)

This is the killer pattern. The agent is not "answering a question." It is operating across my tools to complete a small real-world workflow (aka a "job-to-be-done")

## The License Plate Example

Another example is even more boring, which is why I like it. I got a new license plate for my car. I sent photos and context to Codex. It updated the car information Markdown file I keep in Google Drive, changed the license plate, added the registration notes, preserved the existing VIN, insurance, owners, and address, then uploaded the file back to Drive.

That alone is useful, but the better version is what happens next. The agent can use browser automation to go update the same information everywhere else: FasTrak, the parking app, insurance portals, DMV-related forms, or any other web app that does not have a clean API. For clean systems, it should use an API or CLI. For messy systems, it can use the browser and it's so good! I also now use Computer Use from Codex.

This is what personal agents are for. Not dramatic autonomy. Administrative continuity. I was always afraid of Openclaw yolo mode in the background. I appreciate being in control.

## Google Drive Is My Source Of Truth

The most important architectural decision I made was centralizing valuable personal information in Google Drive. For years, a lot of my knowledge lived in Notion. I like Notion as a human workspace, but I do not love it as the primary source of truth for an agent. The API works, but the workspace is too fluid: nested pages, databases, properties, permissions, formatting, backlinks, and a lot of UI-native structure that is pleasant for humans and annoying for models.

So I used the Notion API to export the valuable information and move it into Google Drive. I was not trying to perfectly preserve the Notion workspace. I was trying to make the information agent-readable. Most of the useful information in Drive is Markdown or CSV, because those formats are easy for the agent to search, diff, edit, and upload back without ceremony. Google Drive became the source of truth because gogcli gives the agent a simple command line surface for Gmail, Drive, Calendar, Docs, Sheets, Contacts, and Tasks.

This is an underrated point. You should not organize your knowledge only for the human UI. You should organize it for the agent's tool path. Agents like stable file IDs, text, tables, Markdown, CSVs, and commands that return JSON. If the agent can search it, download it, edit it, upload it, and cite where it came from, the data is useful.

My personal data layer is embarrassingly simple. Google Drive holds the important docs, mostly as Markdown files and CSVs. Contacts live in a Google Sheet mirrored as a CSV. Notion exports land in Drive. Local instructions live in AGENTS.md. Skills live as Markdown files in folders. The source of truth is not elegant. It is legible.

A lot of personal productivity is just joining across this data. One fact is in WhatsApp. Another is in Gmail. The email address is in Contacts. The date is in Calendar. The document is in Drive. The agent becomes useful when it can cross those boundaries without asking me to be the glue.

One of my best investment was to create a contact.csv with the phone number, email, linkedin etc of all the people I know.

## The Tools

The core tools are boring by design. I use gogcli for Google Workspace, wacli for WhatsApp, imsg for iMessage and SMS, Browser Use or browser automation for web apps, and AppleScript or macOS UI automation when there is no better interface.

The hierarchy is simple. APIs and CLIs are best. Local files are great. Browser automation is acceptable. Screen automation is the last resort.

This hierarchy matters because agents are only as reliable as their tool surface. Asking a model to click around a website is sometimes necessary, but it is not the happy path. A command like `gog gmail messages list` or `wacli messages list --json` is much easier for the model to inspect, retry, and reason about.

## The Skills

Tools give the agent hands. Skills give it habits. A skill is just a small operating manual that tells the agent how to do a recurring task the way I like it done.

My inbox-zero skill is a good example. It tells the agent to list Gmail inbox messages through gog, separate auto-archive from needs-review, show me the important emails, quote the substance, suggest archive or reply, draft replies, wait for explicit approval, send in the original thread, preserve all recipients, archive only after sending, keep replies short, never suggest calls unless I ask, and sign with "Nicolas."

That is not a fancy architecture. It is a procedure. But the procedure is the product and... it's just text instructions.

Without the skill, I have to be the prompt every time. I have to remind the agent not to send without approval, not to drop cc recipients, not to suggest a call, and not to sign with some weird corporate signature. With the skill, I say "run inbox zero," and the workflow already contains my taste.

The important habit is that I improve the skill every time the agent makes a mistake. If it suggests a call when I hate calls, I add that rule. If it forgets to preserve cc recipients, I add that rule. If it archives too aggressively, I tighten the classification. The agent gets better because the procedure gets better.

This is how personal agents become personal. Not by having a cute voice. By accumulating operational taste.

The setup compounds because the mistakes become instructions.

## Approval Gates Are The Product

I do not want an agent that blindly replies to everyone. I want an agent that prepares the work, shows me the draft, and asks at the right moment. For most communication workflows, the loop is: read context, draft response, show me, wait for approval, send, confirm.

Sometimes I let it send directly when the stakes are low. "Tell Hugo I am in Seattle next week" does not need a board meeting. But an investor email, a customer reply, an intro, or anything with social nuance should be drafted first.

This is the difference between useful and terrifying. Read-only scanning is one trust tier. Drafting is another. Sending is another. Deleting, paying, signing, or changing account settings is a completely different tier. The future is not "the agent does everything." The future is "the agent does the tedious work and asks at the right moments."

## The Killer Workflow Is What Did I Miss?

The killer workflow is not email. It is life inbox triage. Every few hours, I want to ask, "What did I miss?" and have the agent scan WhatsApp, Telegram, Gmail, SMS, Calendar, and the relevant Drive changes. Then I want it to tell me who needs a reply, what is urgent, what is stale, what can be ignored, what should become a calendar event, and what needs a document search.

This is the perfect agent task because it is context-heavy, repetitive, cross-tool, and full of small decisions. Humans hate doing the first pass. Agents are good at first passes. Judgment still belongs to me.

The result is not that my life becomes autonomous. The result is that I stop being the person manually digging through five apps to discover the three things that matter.

## My Current Setup Checklist

If someone wants to reproduce my setup, this is the checklist:
- Install Codex
- Install gogcli for Google Workspace
- Install wacli for WhatsApp
- Install a Telegram connector if you use Telegram
- Install imsg for iMessage and SMS
- Add browser automation, ideally through Browser Use or a Chrome controller
- Add macOS automation through AppleScript and UI scripting
- If your knowledge lives in Notion, use the Notion API to export the valuable parts into Google Drive

Then centralize the data:
- Make Google Drive the source of truth
- Keep contacts in a Google Sheet or CSV
- Keep important personal docs as searchable files
- Keep local AGENTS.md instructions
- Keep small skills for recurring workflows

Then grant permissions carefully:
- Full Disk Access is needed for local files and app databases
- Screen Recording is useful as a visual fallback
- Accessibility is needed for clicking and typing in apps
- These are serious permissions, so pair them with serious approval gates

Then write the operating rules.

That is basically it. Tools, data connectors, skills, approval gates, and continuous improvement.

## This Is The New Operating System

The personal computer used to be app-operated. You opened the app, searched, clicked, copied, pasted, wrote, and sent. The agent-operated computer feels different. You state the intent, the agent gathers context, proposes the action, waits for approval when needed, executes, and reports back.

Once you experience this, the old way feels absurd. Why am I manually searching WhatsApp, Gmail, Google Drive, and the web to send one intro? Why am I copying a license plate into five different portals? Why am I reading 100 messages to find the three that matter?

The computer should do that.

The setup is still ugly. The CLIs are rough. Permissions are annoying. Some connectors break. Browser automation is brittle. You have to write skills. You have to maintain a source of truth. But that is how the future usually starts.

The first useful personal agents will not look like polished consumer apps. They will look like a model inside a terminal with access to your files, accounts, memories, and tools.

That is what I use today, and every week I give it one more piece of my life to operate.
