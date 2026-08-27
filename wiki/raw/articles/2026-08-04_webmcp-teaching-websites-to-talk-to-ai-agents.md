# WebMCP: Teaching Your Website to Talk to AI Agents

**Source**: https://sreenathmenon.com/blog/2026-08-04-webmcp-teaching-websites-to-talk-to-ai-agents/  
**Author**: Sreenath M Menon  
**Date**: 2026-08-04 (HN: 2026-08-26)  
**Fetched**: 2026-08-27  
**Type**: technical_blog_post  
**Points**: 55 (HN)  
**Comments**: 55 (HN)  
**URLs**: 
- https://sreenathmenon.com/blog/2026-08-04-webmcp-teaching-websites-to-talk-to-ai-agents/
- https://news.ycombinator.com/item?id=49450417

---


## WebMCP: Teaching Your Website to Talk to AI Agents

August 4, 2026 · #ai #webmcp #mcp #agents #web #browser
Picture an AI agent trying to book you a table on a restaurant’s website. Today, it works like a very patient, slightly confused intern. It loads the page, reads the raw HTML, tries to figure out which of the forty <div> elements is the date picker, guesses that the green button probably means “confirm,” clicks it, waits, and re-reads the whole screen to see if anything happened. Move that button next week and the agent breaks. Rename a CSS class and it breaks. Add a cookie banner on top and it clicks the wrong thing entirely.
This is how almost all “agents using websites” works right now: screen-scraping and hoping. It’s the automation equivalent of operating a computer by describing screenshots over the phone.
WebMCP proposes something much saner. Instead of the agent guessing what your site can do by staring at it, your site declares what it can do, as a set of clean, structured tools the agent can call directly. “Here’s a book_table tool. It takes a date, a time, and a party size. Call it.” No pixel-reading. No guessing. And the best part: it already runs in Chrome behind a trial, and adding your first tool takes about ten minutes.
Let me show you the whole thing.

## The core shift: from scraping to declaring

The entire idea fits in one comparison. Same task, two worlds.

## Today: the agent scrapes


## WebMCP: the site declares

If you’ve read my earlier post on MCP, the port that let AI touch the world, this will feel familiar, and it should. MCP gave AI a standard way to call tools on a server. WebMCP brings that same idea into the browser: the web page itself becomes a place that offers tools, running in the tab you already have open, with the session you’re already logged into.

## What it actually is

WebMCP is a proposed web standard, developed jointly by Google (Chrome) and Microsoft (Edge) in the W3C Web Machine Learning Community Group, that gives a web page a small JavaScript API to register tools that an AI agent can discover and call. Google describes it plainly in the Chrome docs: a way to “build and expose structured tools for AI agents,” where the site annotates its own features so agents “know exactly how to interact” with them. To be precise about maturity, it’s a Community Group draft, not a finished W3C standard and not yet on the standards track, which is exactly why now is the moment to learn it and shape it.
Three things make it click into place:
Discovery. A standard way for a page to say “I offer these tools,” like checkout or filter_results, so an agent can list them.
Schemas. Each tool declares its inputs and outputs as JSON Schema, so the agent knows exactly what to pass and there’s far less room to hallucinate or misread.
State. A shared understanding of what’s on the page right now, so the agent knows what it can actually act on.
WebMCP is real and runnable, but early. It's available as a Chrome origin trial from Chrome 149, and you can switch it on locally with the flag chrome://flags/#enable-webmcp-testing. The proposal lives at github.com/webmachinelearning/webmcp, Angular already has experimental support, and Chrome ships demo sites (a pizza maker, travel search, a restaurant booking). Google's own words: it's "under active discussion and subject to change." So this is a "try it and shape it" moment, not a "ship it to production" one, and that's exactly why it's worth learning now.

## How a call actually flows

Here’s the whole loop, page to agent and back. Nothing exotic happens: the page registers tools, the agent lists them, picks one, calls it with structured arguments, and your own JavaScript does the work in the page.
That “runs in the page you’re already logged into” detail is a big deal. The agent isn’t a separate bot logging in with stolen credentials somewhere. It’s calling a function in your open, authenticated tab, using the session you already have. The site keeps control of what it exposes, and the user can see it happen.

## Watch one call happen

Concretely, when you ask an in-browser agent to do something on a WebMCP-enabled site, it looks like this: your request, the agent picking the declared tool, the tool running, the result.

## The code is genuinely tiny

This is the part that makes people want to try it. Registering a tool is one call. Using the current imperative API from the Chrome docs, a to-do site adding an “add item” tool looks essentially like this:
await document.modelContext.registerTool({ name: 'add_todo', description: 'Add an item to the to-do list', inputSchema: { type: 'object', properties: { text: { type: 'string' } }, required: ['text'] }, execute: async ({ text }) => { addTodoToPage(text); // your own existing function return `Added to-do: ${text}`; } }); That's the whole thing. You give the tool a name, a description, an input schema, and an execute function that calls code you already wrote. The agent discovers it with getTools(), and you can pull a tool back with an AbortController if it stops being relevant. There's also a declarative flavor where you annotate an HTML form instead of writing JS. Notice what execute does: it calls addTodoToPage, a function that already exists on your site. WebMCP isn’t asking you to rebuild anything. You’re wrapping the actions your site can already do in a thin, declared interface so an agent can reach them cleanly. That’s why the ten-minutes claim is real.
One accuracy note, because the API is young and moving: the current entry point is document.modelContext, while earlier drafts used navigator.modelContext, the move makes sense because tools really belong to a document, not the whole browser. If you follow an older tutorial showing navigator, that’s why. A one-line shim (const mc = document.modelContext || navigator.modelContext) bridges both while the change rolls out. Expect a few more edges like this to shift; it’s a draft.

## A real one, worked all the way through

The official WebMCP demos are all “call one tool and you’re done”, order a pizza, book a table. Useful, but they undersell the idea, because the interesting part of WebMCP isn’t one tool call. It’s an agent chaining tools to do real work, with a human gate on the part that matters. So instead of a toy, I built and deployed a real one to go with this post, and this section is the honest walk-through of it, because it teaches the whole model better than any abstract example.
Career Copilot is an experimental agentic career portal. You give it a resume; it reads real job descriptions from live company boards, scores your true fit, tells you your skill gaps, and prepares a batch of applications you approve in one click. Nothing is faked: the jobs are real, the matching is computed from real job-description text, and it applies nothing without your explicit OK.
Open it, tap "See it work instantly", and watch an agent run a full job-search mission over live data: read a resume, pull real openings from GitLab, Stripe and Databricks, read each job description, score your fit, surface your skill gaps, and propose a batch of applications for you to approve. It registers 13 real WebMCP tools on the page.
And this isn’t a diagram of what should happen, here’s the actual browser proving it. Turn the flag on, open DevTools, and Chrome grows a WebMCP panel that lists every tool the page registered, each with the same name and description the agent sees. This is the whole pitch made visible: the website declares its tools, and the browser reads them straight off the page.

## And a real agent actually drove it

Listing tools in a panel is one thing. Getting a production AI agent to use them is the real test. ChatGPT supports WebMCP now, so I pointed it at the live demo and asked it, in plain English, to read the sample frontend resume, find the best job matches with skill gaps, and stop before applying to anything. It did the whole thing through the page’s declared tools.

## The workflow: what the agent actually does

Here’s the real mission, step by step. Each row is a WebMCP tool the page exposes; the agent chains them. Notice the shape: a run phase, then a consequential act phase that stops for a human.

## The tools, grouped by what they can do

This grouping is worth internalizing, because it’s how you should design any WebMCP surface: separate what merely reads from what acts, and put the human gate only where it’s truly needed.

## A real run, not a mockup

Here’s the actual tool-activity log from a validated run with a frontend engineer’s resume. Watch it read real descriptions and score honestly, no fake 99%s:

## The one hard thing, and why the human gate is the right answer

Building this taught me the honest limit of “auto-apply”, and it’s worth stating plainly because it’s the real engineering lesson. Everything up to the apply button is easy to automate and genuinely useful: reading resumes, aggregating openings, matching, tailoring. The last mile, actually submitting into a company’s application system, is the hard part. Those systems (Workday, Greenhouse and friends) are deliberately not open APIs, they sit behind logins and bot-detection, and automating submission usually violates their terms.
This is exactly the gap WebMCP is meant to close. If a careers site exposed a submit_application tool the way this demo does, an agent could apply cleanly, in your own authenticated session, with your approval. Until sites do that, the correct design isn’t to fake the last mile, it’s to automate everything up to it and keep a human on the submit. That’s not a compromise. An agent that silently applies to jobs in your name is a liability; one that does all the work and asks before it acts as you is a superpower. WebMCP’s consent model is what makes that line enforceable.
The full source is a single self-contained HTML file, and I wrote up the deeper product thinking, the candidate and employer sides, the phased build, the honest limits, as a design note in the repo.

## The trust model, because this is the scary part

The obvious worry: if a page can hand tools to an agent, can a malicious page trick the agent into doing something awful? The design takes this seriously, and it’s worth knowing the guards.
It runs visibly, in the tab. No headless, background execution. A browsing context has to be open, so actions happen where the user can see them.
Same-origin only. Tool registration is gated by a tools Permissions Policy that defaults to self, so a random cross-origin iframe can’t quietly register tools unless the top page explicitly allows it.
Sensitive actions can demand a human. For things like making a purchase, a tool can require an explicit user confirmation dialog before it proceeds. Human-in-the-loop is built into the pattern, not bolted on.
Untrusted content is flagged. Tools carry annotation hints like readOnlyHint and untrustedContentHint, so the agent can treat a tool that returns third-party content with appropriate suspicion, which matters given everything we know about prompt injection.
None of this makes it magically safe, the standard is young and the security model is still being worked out, but the shape is right: visible, same-origin, consent-gated, and honest about untrusted data.

## Honest pros and cons


## Where it fits: use cases

The pattern shines anywhere an agent needs to do something on a site, not just read it.

## Where this is headed

Now the fun part, because the ceiling here is high.
The obvious next step is standardization across browsers. Right now it’s a Chrome trial; the destination is a web standard every browser implements, the way fetch or the clipboard API are everywhere. When that lands, “does this site have an agent interface?” becomes as normal a question as “is this site mobile-friendly?”
That direction just got a real push: ChatGPT now supports WebMCP. Visit a WebMCP-enabled page and it can automatically use the tools the page declares to complete your task. That’s the interesting signal, it’s not just Google and Microsoft (who wrote the draft) anymore. When a second major AI vendor starts consuming page-declared tools, a proposal in its incubation window starts looking like a direction the ecosystem is actually moving in.
Then there’s the agentic web itself. Imagine sites shipping an agent interface alongside their visual one, on purpose, the way they ship a mobile layout today. Your site’s UI is for humans; its declared tools are for agents; both are first-class. A site that’s good at being operated by an agent gets used by more agents, which becomes a real reason to invest in the tool surface.
It gets more interesting when you combine WebMCP with remote MCP. WebMCP handles what lives in the browser (the page’s own actions, the user’s session), while remote MCP servers handle backend tools and data. An agent could fluidly use both: call a page’s add_to_cart tool via WebMCP, then hit a remote inventory MCP server for stock, stitching client and server tools into one task.
And further out: agent commerce. If a store exposes clean purchase tools and an agent can call them within the user’s authenticated, consenting session, you get a path to agents that actually complete transactions safely, with the human able to watch and confirm, rather than a scraper hammering a checkout flow. The same shape extends to booking, scheduling, support, anything transactional.
The big bet underneath all of it: the web was built for humans to read and click. The next version is built to also be operated by agents, cleanly and on the site’s own terms. WebMCP is one of the first serious attempts to make that a standard instead of a hack.

## The takeaway, and go try it

Here’s the whole thing in a sentence: WebMCP lets your website hand an AI agent a clean set of tools instead of forcing it to reverse-engineer your buttons. That single shift, declare instead of scrape, makes agent interactions reliable, keeps the site in control, runs in the user’s real session, and survives your next redesign.
It’s early, it’s Chrome-first, and the standard will change. But the barrier to trying it is almost nothing: flip on chrome://flags/#enable-webmcp-testing, add a registerTool call wrapping a function your site already has, and watch an agent call it. Ten minutes, and you’ll understand the agentic web better than most people reading about it. Then go read the proposal, poke the demos, and file the rough edges you hit, because right now, while it’s still being shaped, your feedback actually moves it.
Written from scratch after reading the official documentation. These are the primary, verified sources. Nothing here is copied from them; the code shape follows the documented API.
Chrome for Developers, WebMCP overview: https://developer.chrome.com/docs/ai/webmcp
Chrome for Developers, WebMCP imperative API: https://developer.chrome.com/docs/ai/webmcp/imperative-api
Chrome for Developers, WebMCP declarative API: https://developer.chrome.com/docs/ai/webmcp/declarative-api
WebMCP specification (Draft Community Group Report): https://webmachinelearning.github.io/webmcp/
WebMCP proposal, explainer, and source (W3C Web Machine Learning Community Group): https://github.com/webmachinelearning/webmcp
Chrome Platform Status, WebMCP feature: https://chromestatus.com/feature/5117755740913664
WebMCP demo sites (Google Chrome Labs): https://github.com/GoogleChromeLabs/webmcp-tools/tree/main/demos
Patrick Brosset (Microsoft Edge), WebMCP updates and clarifications: https://patrickbrosset.com/articles/2026-02-23-webmcp-updates-clarifications-and-next-steps/
OpenAI Developers, WebMCP support in the ChatGPT desktop browser (Aug 26, 2026): https://x.com/OpenAIDevs/status/2092344959248761263
Model Context Protocol (MCP), for the underlying protocol: https://modelcontextprotocol.io
Background reading: MCP: The Port That Let AI Finally Touch the World for the protocol WebMCP builds on, and LLM security for why the trust model here matters.
← Back to blog

---

## Wiki Notes

This article explains the WebMCP (Web Model Context Protocol) — a proposed web standard that allows websites to expose structured tools to AI agents. Key points:

1. **Core shift**: From screen-scraping to tool declaration
2. **Standard**: Developed by Google (Chrome) and Microsoft (Edge) in the W3C Web Machine Learning Community Group
3. **Maturity**: Community Group draft, not yet on the standards track
4. **Key features**: Discovery, JSON Schema-based tools, shared state
5. **Availability**: Chrome origin trial

This complements the existing MCP (Model Context Protocol) by extending it to web contexts.
