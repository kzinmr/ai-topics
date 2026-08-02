---
title: "What is CDP (Chrome DevTools Protocol)?"
source: https://www.browserbase.com/blog/what-is-cdp
author: Kyle Jeong
published: 2026-07-17
scraped: 2026-08-02
type: article
tags: [cdp, browser-automation, browser-agent, chromium, devtools, browserbase]
---

# What is CDP (Chrome DevTools Protocol)?

Author: Kyle Jeong (Browserbase Engineering). Published July 17, 2026 (7 min read).

## TLDR

CDP is the control surface that gives external programs access to Chromium's pages, network stack, JavaScript runtime, input system, debugger, and performance instrumentation.

When you open Chrome and press F12, the DevTools panel that appears is a separate process talking to the browser. The language between them is Chrome DevTools Protocol, or CDP.

## The protocol behind DevTools

CDP ships in Chromium-based browsers including Chrome, Edge, Brave, Arc, and Opera. DevTools, Lighthouse, Puppeteer, Playwright, and many browser agents use it to talk to the browser. If your code controls Chromium, CDP is somewhere underneath it.

## A little history

CDP started as the plumbing behind Chrome's DevTools, not as a general automation API. When Chrome shipped in 2008, its inspector came from WebKit, the rendering engine Chrome (then) shared with Safari. The DevTools front end needed to run separately from the page it inspected, so the team defined a wire protocol between the front end and the browser.

```
┌─────────────────────┐       CDP messages       ┌─────────────────────┐
│ DevTools front end  │  ← commands / events →   │ Chromium browser    │
│ HTML, CSS, JS       │                          │ renderer, network,  │
│                     │                          │ runtime, input      │
└─────────────────────┘                          └─────────────────────┘
```

## Commands and events

CDP has two message types:
- **Commands** — questions or instructions sent by the client (e.g., `Page.navigate`, `Runtime.evaluate`). Each command has an ID; the browser replies with a matching response.
- **Events** — the browser responding asynchronously (e.g., `Network.requestWillBeSent`, `Page.frameNavigated`, `Runtime.executionContextCreated`). Events have no request ID; to read them, enable a domain then consume its event stream.

## Sessions and targets

Think of a CDP connection as a tree. The root is the browser. From there you discover and attach to targets.

A **target** is something Chrome can inspect or control: a page, an out-of-process iframe, a service worker, a shared worker, or an extension page. Attaching to a target creates a **session**. Commands sent through that session affect that target and its events return through the same session.

Chrome uses Site Isolation to keep pages from different sites in separate renderer processes. When a page embeds a cross-site iframe, Chrome may promote that frame into an out-of-process iframe — still nested inside the page visually, but CDP may expose it as another target with its own session.

Workers add more branches: dedicated workers run JavaScript away from the page's main thread; shared workers and service workers can outlive an individual page.

Navigation changes the tree again: loading a new document destroys the frame's old JavaScript execution context and creates a new one. Any object IDs or references from the previous context become invalid, even when tab and frame IDs appear unchanged.

A CDP client has to track both structure and lifetime: which targets exist, which sessions are attached, which execution contexts belong to each frame, and when any of them disappear.

**Flat mode** multiplexes multiple sessions over one connection, identifying each session with a `sessionId`.

## What parts of the browser does CDP expose?

- **Network traffic** — the Network domain observes document requests, scripts, images, API calls, redirects, cache hits, and service worker activity. Events share IDs, so a client can reconstruct the full lifecycle and call `Network.getResponseBody`.
- **JavaScript execution** — the Runtime domain evaluates code and reports console calls, exceptions, and execution contexts.
- **Browser input** — the Input domain sends mouse, keyboard, touch, and drag events through the browser's input system. This is lower-level than calling a JS method on an element; it doesn't decide what to click or wait for layout.
- **Traces and diagnostics** — Performance.getMetrics, Tracing.start, console events, exception events, screenshots, and screencasts. "CDP turns the browser into a fully observable system."

## Why executing raw CDP sucks

Wire format is easy; managing state is hard. A raw CDP client has to:
- Enable domains before useful events arrive
- Track targets and execution contexts as navigation creates and destroys them
- Coordinate responses and events racing across several domains

The reference docs explain message shapes but skip lifecycle details: How long does a session live? What kills it? Does navigation preserve it? Can another WebSocket reuse its sessionId?

Chrome itself changes a lot — stable, experimental, and deprecated methods coexist in the protocol. And CDP can send a mouse event to coordinates, but it can't decide which element deserves the click or whether the result counts as success. That's why libraries such as Playwright and Puppeteer exist: they handle waiting, targeting, lifecycle state, and interaction policy while exposing CDP sessions when you need lower-level capability.

## The boundaries of the protocol

CDP belongs to Chromium and Chromium only — Firefox and WebKit expose different debugging surfaces. WebDriver provides a cross-browser automation standard; WebDriver BiDi adds bidirectional events to that model. CDP goes deeper into Chromium because Chromium owns both sides of the protocol.

A debugging connection is powerful enough to become dangerous: it can inspect pages, execute arbitrary JS, read network traffic, and control authenticated sessions. The tip-of-tree protocol changes with Chromium; production clients need to choose which versions they support and handle missing methods.

## The browser's control surface

> "Humans talk to humans using english, programs talk to other programs using protocols, and agents talk to browsers using CDP." — Kyle Jeong

You can navigate a page, watch its requests, execute JS, inspect workers, send input, collect traces, and follow every target through one protocol. The article recommends using higher-level tools (Stagehand, Playwright, Puppeteer) rather than building every interaction on raw CDP — but understanding how CDP works and what the right abstractions are lets you make the right decision on how to give your agent access to the web.
