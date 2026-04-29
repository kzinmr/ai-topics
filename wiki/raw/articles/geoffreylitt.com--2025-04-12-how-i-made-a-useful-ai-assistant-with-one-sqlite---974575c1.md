---
title: "Stevens: a hackable AI assistant using a single SQLite table and a handful of cron jobs"
url: "https://geoffreylitt.com/2025/04/12/how-i-made-a-useful-ai-assistant-with-one-sqlite-table-and-a-handful-of-cron-jobs.html"
fetched_at: 2026-04-29T07:02:18.435032+00:00
source: "geoffreylitt.com"
tags: [blog, raw]
---

# Stevens: a hackable AI assistant using a single SQLite table and a handful of cron jobs

Source: https://geoffreylitt.com/2025/04/12/how-i-made-a-useful-ai-assistant-with-one-sqlite-table-and-a-handful-of-cron-jobs.html

There’s a lot of hype these days around patterns for building with AI. Agents, memory, RAG, assistants—so many buzzwords! But the reality is,
you don’t need fancy techniques or libraries to build useful personal tools with LLMs.
In this short post, I’ll show you how I built a useful AI assistant for my family using a dead simple architecture: a single SQLite table of memories, and a handful of cron jobs for ingesting memories and sending updates, all hosted on
Val.town
. The whole thing is so simple that you can easily copy and extend it yourself.
Meet Stevens
The assistant is called Stevens, named after the butler in the great Ishiguro novel
Remains of the Day
. Every morning it sends a brief to me and my wife via Telegram, including our calendar schedules for the day, a preview of the weather forecast, any postal mail or packages we’re expected to receive, and any reminders we’ve asked it to keep track of. All written up nice and formally, just like you’d expect from a proper butler.
Here’s an example. (I’ll use fake data throughout this post, beacuse our actual updates contain private information.)
Beyond the daily brief, we can communicate with Stevens on-demand—we can forward an email with some important info, or just leave a reminder or ask a question via Telegram chat.
That’s Stevens. It’s rudimentary, but already more useful to me than Siri!
Behind the scenes
Let’s break down the simple architecture behind Stevens. The whole thing is hosted on
Val.town
, a lovely platform that offers SQLite storage, HTTP request handling, scheduled cron jobs, and inbound/outbound email: a perfect set of capabilities for this project.
First, how does Stevens know what goes in the morning brief? The key is the butler’s notebook, a log of everything that Stevens knows. There’s an admin view where we can see the notebook contents—let’s peek and see what’s in there:
You can see some of the entries that fed into the morning brief above—for example, the parent-teacher conference has a log entry.
In addition to some text, entries can have a
date
when they are expected to be relevant.  There are also entries with no date that serve as general background info, and are always included. You can see these particular background memories came from a Telegram chat, because Stevens does an intake interview via Telegram when you first get started:
With this notebook in hand, sending the morning brief is easy
: just run a cron job which makes a call to the Claude API to write the update, and then sends the text to a Telegram thread. As context for the model, we include any log entries dated for the coming week, as well as the undated background entries.
Under the hood, the “notebook” is just a single SQLite table with a few columns. Here’s a more boring view of things:
But wait: how did the various log entries get there in the first place? In the admin view, we can watch Stevens buzzing around entering things into the log from various sources:
This is just some data importers populating the table:
An hourly data pull from the Google Calendar API
An hourly check of the local weather forecast using a weather API
I forward
USPS Informed Delivery
containing scans of our postal mail, and Stevens OCRs them using Claude
Inbound Telegram and email messages can also result in log entries
Every week, some “fun facts” get added into the log, as a way of adding some color to future daily updates.
This system is easily extensible with new importers.
An importer is just any process that adds/edits memories in the log. The memory contents can be any arbitrary text, since they’ll just be fed back into an LLM later anyways.
Reflections
A few quick reflections on this project:
It’s very useful for personal AI tools to have access to broader context from other information sources.
Awareness of things like my calendar and the weather forecast turns a dumb chatbot into a useful assistant. ChatGPT recently added memory of past conversations, but there’s lots of information not stored within that silo. I’ve
written before
about how the endgame for AI-driven personal software isn’t more app silos, it’s small tools operating on a shared pool of context about our lives.
“Memory” can start simple.
In this case, the use cases of the assistant are limited, and its information is inherently time-bounded, so it’s fairly easy to query for the relevant context to give to the LLM. It also helps that some modern models have long context windows. As the available information grows in size, RAG and
fancier
approaches
to memory may be needed, but you can start simple.
Vibe coding enables sillier projects.
Initially, Stevens spoke with a dry tone, like you might expect from a generic Apple or Google product. But it turned out it was just more
fun
to have the assistant speak like a formal butler. This was trivial to do, just a couple lines in a prompt. Similarly, I decided to make the admin dashboard views feel like a video game, because why not? I generated the image assets in ChatGPT, and vibe coded the whole UI in Cursor + Claude 3.7 Sonnet; it took a tiny bit of extra effort in exchange for a lot more fun.
Try it yourself
Stevens isn’t a product you can run out of the box, it’s just a personal project I made for myself.
But if you’re curious, you can check out the code and fork the project
here
. You should be able to apply this basic pattern—a single memories table and an extensible constellation of cron jobs—to do lots of other useful things.
I recommend editing the code using your AI editor of choice with the
Val Town CLI
to sync to local filesystem.
